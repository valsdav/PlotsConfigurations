import os
import subprocess
import string
from LatinoAnalysis.Tools.commonTools import *

samples={}

#skim='__wwSel'
skim=''

##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

directory = treeBaseDir+'Fall2017_102X_nAODv4_Full2017v4/MCl1loose2017__MCCorr2017'+skim
directory_signal = '/eos/user/r/rdfexp/LatinoTrees/Fall2017_102X_nAODv4_Full2017v4/MCl1loose2017__MCCorr2017'

################################################
############ NUMBER OF LEPTONS #################
################################################

Nlep='1'
#Nlep='3'
#Nlep='4'

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP

LepWPCut_1l =  '(Lepton_isTightElectron_'+eleWP+'[0]>0.5 || Lepton_isTightMuon_'+muWP+'[0]>0.5)'
LepWPWeight_1l = 'Lepton_tightElectron_'+eleWP+'_IdIsoSF'+'[0]*\
                Lepton_tightMuon_'+muWP+'_IdIsoSF'+'[0]'

LepWPCut = LepWPCut_1l
LepWPWeight = LepWPWeight_1l
################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight1l =       'puWeight*\
                   TriggerEffWeight_1l*\
                   Lepton_RecoSF[0]*\
                   EMTFbug_veto'
SFweight      = SFweight1l+'*'+LepWPWeight_1l+'*'+LepWPCut_1l+'*PrefireWeight'

                   
GenLepMatch   = 'Lepton_genmatched[0]'



################################################
############## FAKE WEIGHTS ####################
################################################

# if Nlep == '2' :
#   fakeW = 'fakeW2l_ele_'+eleWP+'_mu_'+muWP
# else:
#   fakeW = 'fakeW_ele_'+eleWP+'_mu_'+muWP+'_'+Nlep+'l'


################################################
############### B-Tag  WP ######################
################################################

#FIXME b-tagging to be optimized
# Definitions in aliases.py

SFweight += '*btagSF'

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-31Mar2018-v1'] ,
            ['C','Run2017C-31Mar2018-v1'] ,
            ['D','Run2017D-31Mar2018-v1'] ,
            ['E','Run2017E-31Mar2018-v1'] ,
            ['F','Run2017F-31Mar2018-v1']

          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }

###########################################
#############  BACKGROUNDS  ###############
###########################################

############ DY ############
ptllDYW_NLO = '((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useEmbeddedDY = False
useDYtt = False

if useEmbeddedDY: #Setup
  # Temporarily in a different directory:
  directory2 = treeBaseDir+'Fall2017_nAOD_v1_Full2017v2/MCl1loose2017v2__MCCorr2017__btagPerEvent__l2loose__l2tightOR2017__EmbeddingVeto'+skim
  embed_tautauveto = '*embed_tautauveto'
else:
  directory2 = directory
  embed_tautauveto = ''

if useEmbeddedDY:

  # Actual embedded data
  samples['DY']  = {   'name': [ ] ,
                         'weight' : METFilter_DATA+'*'+LepWPCut+'*embed_total*genWeight',
                         'weights' : [ ] ,
                         'isData': ['all'],
                         'FilesPerJob' : 5,
                      }

  for Run in DataRun :
          directoryEmb = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Embedding2017_nAOD_v1_Full2017v2/DATAl1loose2017v2__DATACorr2017__l2loose__l2tightOR2017__Embedding2017__hadd/'
          FileTarget = getSampleFiles(directoryEmb,'DYToTT_MuEle_Embedded_Run2017'+Run[0],True,'nanoLatino_')
          for iFile in FileTarget:
                  samples['DY']['name'].append(iFile)
                  samples['DY']['weights'].append('Trigger_ElMu || Trigger_dblMu || Trigger_sngMu || Trigger_dblEl || Trigger_sngEl')

  # Vetoed MC: Needed for uncertainty
  samples['DYveto']  = {   'name': getSampleFiles(directory2,'TTTo2L2Nu',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_tW_antitop',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_tW_top',False,'nanoLatino_') 

                                 + getSampleFiles(directory2,'WWTo2L2Nu_PrivateNano',False,'nanoLatino_') 

                                 + getSampleFiles(directory2,'WpWmJJ_EWK',False,'nanoLatino_') 

                                 + getSampleFiles(directory2,'GluGluToWWToTNTN',False,'nanoLatino_') 

                                 + getSampleFiles(directory2,'Zg',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'WZTo3LNu_mllmin01',False,'nanoLatino_') 

                                 + getSampleFiles(directory2,'ZZTo2L2Nu',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ZZTo2L2Q',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ZZTo4L',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'WZTo2L2Q',False,'nanoLatino_') ,

                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+'*'+'(1-embed_tautauveto)',
                         'FilesPerJob' : 1, # There's some error about not finding sample-specific variables like "nllW" when mixing different samples into a single job; so split them all up instead
                      }

  veto_dict = {'TTTo2L2Nu'            : '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )' ,
               'ST_tW_antitop'        : '1' ,
               'ST_tW_top'            : '1' ,

               'WWTo2L2Nu_PrivateNano' : 'nllW' ,

               'WpWmJJ_EWK' : '(Sum$(abs(GenPart_pdgId)==6)==0)',

               'GluGluToWWToTNTN' : '1' ,

               'Zg'                : '((!(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 )) || (Gen_ZGstar_mass >0))' ,
               'WZTo3LNu_mllmin01' : '(Gen_ZGstar_mass>=0.1 || Gen_ZGstar_mass<0)' ,

               'ZZTo2L2Nu' : '1' ,
               'ZZTo2L2Q'  : '1' ,
               'ZZTo4L'    : '1' ,
               'WZTo2L2Q'  : '1'
              }

  for v_samp,v_weight in veto_dict.items():
          if v_weight != '1': addSampleWeight(samples,'DYveto',v_samp,v_weight)

else:
  if useDYtt :
    samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToTT_MuEle_M-50_PSWeights',False,'nanoLatino_')
                                    + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                         'FilesPerJob' : 5,
                    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)
    
    ## Remove OF from inclusive sample (is it needed?)
    #cutSF = '(abs(Lepton_pdgId[0]*Lepton_pdgId[1]) == 11*11)||(Lepton_pdgId[0]*Lepton_pdgId[1]) == 13*13)'
    #addSampleWeight(samples,'DY','DYJetsToLL_M-50',cutSF)

  else:
    samples['DY'] = {    'name'   :   getSampleFiles(directory,'DYJetsToLL_M-50',False,'nanoLatino_')
                                    + getSampleFiles(directory,'DYJetsToLL_M-10to50-LO',False,'nanoLatino_'),
                         'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
                         'FilesPerJob' : 5,
                     }
    addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)



############ Top ############

Top_pTrw = '(TMath::Sqrt( TMath::Exp(0.0615-0.0005*topGenPt) * TMath::Exp(0.0615-0.0005*antitopGenPt) ) )'

samples['top'] = {    'name'   :   getSampleFiles(directory2,'TTTo2L2Nu',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_s-channel',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_t-channel_antitop',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_t-channel_top',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_tW_antitop',False,'nanoLatino_') 
                                 + getSampleFiles(directory2,'ST_tW_top',False,'nanoLatino_') ,
                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto ,
                     'FilesPerJob' : 1,
                 }

addSampleWeight(samples,'top','TTTo2L2Nu',Top_pTrw)

############ WW ############

# samples['WW'] = {    'name'   :   getSampleFiles(directory2,'WWTo2L2Nu_PrivateNano',False,'nanoLatino_') ,
#                      'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto+'*nllW' ,
#                  }

# samples['WWewk'] = {   'name'  : getSampleFiles(directory2, 'WpWmJJ_EWK',False,'nanoLatino_'),
#                        'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto + '*(Sum$(abs(GenPart_pdgId)==6)==0)' #filter tops
#                    }

# #FIXME Check if k-factor is already taken into account in XSWeight
# samples['ggWW']  = {  'name'   :   getSampleFiles(directory2,'GluGluToWWToENEN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToENMN',False,'nanoLatino_') 
#                                  + getSampleFiles(directory2,'GluGluToWWToENTN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToMNEN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToMNMN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToMNTN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToTNEN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToTNMN',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'GluGluToWWToTNTN',False,'nanoLatino_'),
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto ,
#                    }


############ Vg ############

# samples['Vg']  = {  'name'   :   getSampleFiles(directory2,'Wg_MADGRAPHMLM',False,'nanoLatino_')
#                                + getSampleFiles(directory2,'Zg',False,'nanoLatino_'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto+'*(!(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22 ))',
#                     'FilesPerJob': 5,
#                   }


############ VgS ############

# #FIXME Add normalization k-factor
# samples['VgS']  =  {  'name'   :   getSampleFiles(directory2,'Wg_MADGRAPHMLM',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'Zg',False,'nanoLatino_')
#                                  + getSampleFiles(directory2,'WZTo3LNu_mllmin01',False,'nanoLatino_'),
#                       'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto,
#                       'FilesPerJob' : 5 ,
#                    }
# addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM',    '(Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 0.1)')
# addSampleWeight(samples,'VgS','Zg',                '(Gen_ZGstar_mass >0)')
# addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass>=0.1 || Gen_ZGstar_mass<0)')

############ VZ ############

#FIXME Add normalization k-factor
# samples['VZ']  = {  'name'   :   getSampleFiles(directory2,'ZZTo2L2Nu',False,'nanoLatino_')
#                                + getSampleFiles(directory2,'ZZTo2L2Q',False,'nanoLatino_')
#                                + getSampleFiles(directory2,'ZZTo4L',False,'nanoLatino_')
#                                + getSampleFiles(directory2,'WZTo2L2Q',False,'nanoLatino_'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC+embed_tautauveto ,
#                     'FilesPerJob' : 5,
#                  }


############ VVV ############

# samples['VVV']  = {  'name'   :   getSampleFiles(directory,'ZZZ',False,'nanoLatino_')
#                                 + getSampleFiles(directory,'WZZ',False,'nanoLatino_')
#                                 + getSampleFiles(directory,'WWZ',False,'nanoLatino_')
#                                 + getSampleFiles(directory,'WWW',False,'nanoLatino_'),
#                                 #+ getSampleFiles(directory,'WWG',False,'nanoLatino_'), #should this be included? or is it already taken into account in the WW sample?
#                     'weight' : XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#                   }


samples['Wjets'] = { 'name' :   
          getSampleFiles(directory, 'WJetsToLNu_HT100_200', True, 'nanoLatino_')\
				+ getSampleFiles(directory, 'WJetsToLNu_HT200_400', True, 'nanoLatino_')\
				+ getSampleFiles(directory, 'WJetsToLNu_HT400_600', True, 'nanoLatino_')\
				+ getSampleFiles(directory, 'WJetsToLNu_HT600_800', True, 'nanoLatino_')\
				+ getSampleFiles(directory, 'WJetsToLNu_HT800_1200', True, 'nanoLatino_')\
				+ getSampleFiles(directory, 'WJetsToLNu_HT1200_2500', True, 'nanoLatino_')\
				+ getSampleFiles(directory, 'WJetsToLNu_HT2500_inf', True, 'nanoLatino_'),
				'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
				'FilesPerJob' : 3,
		   }



##########################################
################ SIGNALS #################
##########################################

#
samples['VBS']  = { 'name' :  
               getSampleFiles(directory_signal,'WmTo2J_ZTo2L',   True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WmToLNu_WmTo2J', True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WmToLNu_ZTo2J',  True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WpTo2J_WmToLNu', True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WpTo2J_ZTo2L',   True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WpToLNu_WmTo2J', True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WpToLNu_WpTo2J', True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'WpToLNu_ZTo2J',  True, 'nanoLatino_') +
               getSampleFiles(directory_signal,'ZTo2L_ZTo2J',    True, 'nanoLatino_') ,
       'weight': XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC,
       'suppressNegative' :['all'],
       'suppressNegativeNuisances' :['all'],
}


###########################################
################## DATA ###################
###########################################


LepWPCut_data =  '(Lepton_isTightElectron_mvaFall17Iso_WP90[0]>0.5 || Lepton_isTightMuon_cut_Tight_HWWW[0]>0.5)'



samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut_data,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 20,
                  }

for Run in DataRun :
        directory = treeBaseDir+'Run2017_nAOD_v1_Full2017v2/DATAl1loose2017v2__DATACorr2017/'
        for DataSet in DataSets :
                FileTarget = getSampleFiles(directory,DataSet+'_'+Run[1],True,'nanoLatino_')
                for iFile in FileTarget:
                        print(iFile)
                        samples['DATA']['name'].append(iFile)
                        samples['DATA']['weights'].append(DataTrig[DataSet])
