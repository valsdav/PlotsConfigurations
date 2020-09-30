## RAndKff
RAndKff['DYmva0p8'] = {
                      'RFile'   : 'rootFile/plots_DYESTIM080_2018_HTXS_Stage1p2.root',
                      'KffFile' : 'rootFile/plots_DYESTIM080_2018_HTXS_Stage1p2.root',
                      'Regions' : { '2jVHee' : {
                                               'kNum' : 'VH_ee_in/events/histo_DY',
                                               'kDen' : 'VH_mm_in/events/histo_DY',
                                               'RNum' : 'VH_ee_out',
                                               'RDen' : 'VH_ee_in',
                                             },
                                    '2jVHmm' : {
                                               'kNum' : 'VH_mm_in/events/histo_DY',
                                               'kDen' : 'VH_ee_in/events/histo_DY',
                                               'RNum' : 'VH_mm_out',
                                               'RDen' : 'VH_mm_in',
                                             },
                                   },
                     }

RAndKff['DYmva0p9'] = {
                      'RFile'   : 'rootFile/plots_DYESTIM090_2018_HTXS_Stage1p2.root',
                      'KffFile' : 'rootFile/plots_DYESTIM080_2018_HTXS_Stage1p2.root',
                      'Regions' : { '2jVBFee' : {
                                               'kNum' : 'VBF_ee_in/events/histo_DY',
                                               'kDen' : 'VBF_mm_in/events/histo_DY',
                                               'RNum' : 'VBF_ee_out',
                                               'RDen' : 'VBF_ee_in',
                                             },
                                    '2jVBFmm' : {
                                               'kNum' : 'VBF_mm_in/events/histo_DY',
                                               'kDen' : 'VBF_ee_in/events/histo_DY',
                                               'RNum' : 'VBF_mm_out',
                                               'RDen' : 'VBF_mm_in',
                                             },
                                    'hptee' : {
                                               'kNum' : 'hpt_ee_in/events/histo_DY',
                                               'kDen' : 'hpt_mm_in/events/histo_DY',
                                               'RNum' : 'hpt_ee_out',
                                               'RDen' : 'hpt_ee_in',
                                             },
                                    'hptmm' : {
                                               'kNum' : 'hpt_mm_in/events/histo_DY',
                                               'kDen' : 'hpt_ee_in/events/histo_DY',
                                               'RNum' : 'hpt_mm_out',
                                               'RDen' : 'hpt_mm_in',
                                             },
                                   },
                     }


## DYestim in the signal regions
DYestim['hww2l2v_13TeV_2j_mjj65_105_ee'] = {
                                 'rinout'  : 'DYmva0p8',
                                 'rsyst'   : 0.05,
                                 'ksyst'   : 0.02,
                                 'njet'    : '2jVH',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormvh',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjj65_105_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_ee/events/histo_DY',
                                 'asyst'   : 0.16,
                                }

DYestim['hww2l2v_13TeV_2j_mjj65_105_mm'] = {
                                 'rinout'  : 'DYmva0p8',
                                 'rsyst'   : 0.02,
                                 'ksyst'   : 0.03,
                                 'njet'    : '2jVH',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormvh',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjj65_105_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_mm/events/histo_DY',
                                 'asyst'   : 0.01,
                                }

DYestim['hww2l2v_13TeV_2j_mjj350_700_pthLT200_ee'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'rsyst'   : 0.01,
                                 'ksyst'   : 0.01,
                                 'njet'    : '2jVBF',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjj350_700_pthLT200_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_ee/events/histo_DY',
                                 'asyst'   : 0.20,
                                }

DYestim['hww2l2v_13TeV_2j_mjj350_700_pthLT200_mm'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'rsyst'   : 0.01,
                                 'ksyst'   : 0.01,
                                 'njet'    : '2jVBF',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjj350_700_pthLT200_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_mm/events/histo_DY',
                                 'asyst'   : 0.01,
                                }

DYestim['hww2l2v_13TeV_2j_mjjGT700_pthLT200_ee'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'rsyst'   : 0.01,
                                 'ksyst'   : 0.01,
                                 'njet'    : '2jVBF',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjjGT700_pthLT200_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_ee/events/histo_DY',
                                 'asyst'   : 0.20,
                                }

DYestim['hww2l2v_13TeV_2j_mjjGT700_pthLT200_mm'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'rsyst'   : 0.01,
                                 'ksyst'   : 0.01,
                                 'njet'    : '2jVBF',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjjGT700_pthLT200_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_mm/events/histo_DY',
                                 'asyst'   : 0.01,
                                }

DYestim['hww2l2v_13TeV_2j_mjjGT350_pthGT200_ee'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'rsyst'   : 0.01,
                                 'ksyst'   : 0.01,
                                 'njet'    : 'hpt',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormhpt',#'DYeenormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjjGT350_pthGT200_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_hpt_ee/events/histo_DY',
                                 'asyst'   : 0.20,
                                }

DYestim['hww2l2v_13TeV_2j_mjjGT350_pthGT200_mm'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'rsyst'   : 0.01,
                                 'ksyst'   : 0.01,
                                 'njet'    : 'hpt',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormhpt', #'DYmmnormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_HAccNum_2j_mjjGT350_pthGT200_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_hpt_mm/events/histo_DY',
                                 'asyst'   : 0.01,
                                }


## DYestim in the WW control regions
DYestim['hww2l2v_13TeV_WW_2j_vh_ee'] = {
                                 'rinout'  : 'DYmva0p8',
                                 'njet'    : '2jVH',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormvh',
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vh_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_ee/events/histo_DY',
                                 'asyst'   : 0.01,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_vh_mm'] = {
                                 'rinout'  : 'DYmva0p8',
                                 'njet'    : '2jVH',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vh_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vh_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormvh',
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vh_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vh_mm/events/histo_DY',
                                 'asyst'   : 0.05,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_vbf_ee'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'njet'    : '2jVBF',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vbf_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_ee/events/histo_DY',
                                 'asyst'   : 0.03,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_vbf_mm'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'njet'    : '2jVBF',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_vbf_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_vbf_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_vbf_mm/events/histo_DY',
                                 'asyst'   : 0.01,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_hpt_ee'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'njet'    : 'hpt',
                                 'flavour' : 'ee',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_ee',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYeenormhpt', #'DYeenormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_hpt_ee/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_hpt_ee/events/histo_DY',
                                 'asyst'   : 0.03,
                                   }

DYestim['hww2l2v_13TeV_WW_2j_hpt_mm'] = {
                                 'rinout'  : 'DYmva0p9',
                                 'njet'    : 'hpt',
                                 'flavour' : 'mm',
                                 'DYProc'  : 'DY',
                                 'SFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_mm',
                                 'SFinDa'  : 'DATA',
                                 'SFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'DFin'    : 'hww2l2v_13TeV_DYin_2j_hpt_df',
                                 'DFinDa'  : 'DATA',
                                 'DFinMC'  : ['VZ','Vg','VgS_L','VgS_H'],
                                 'NPname'  : 'DYmmnormhpt', #'DYmmnormvbf',
                                 'AccNum'  : 'hww2l2v_13TeV_wwAcc_2j_hpt_mm/events/histo_DY',
                                 'AccDen'  : 'hww2l2v_13TeV_AccDen_2j_hpt_mm/events/histo_DY',
                                 'asyst'   : 0.01,
                                   }
