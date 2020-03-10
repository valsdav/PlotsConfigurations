
supercut = '    mll>12 \
            && Lepton_pt[0]>25 \
            && Lepton_pt[1]>10 \
            && (abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13) \
            && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && ptll>30 \
            && PuppiMET_pt > 20 \
           '

# Some cuts

dymva0jet = 'dymva_dnn_0j  > 0.975'
dymva1jet = 'dymva_dnn_1j  > 0.975'
dymva2jet = 'dymva_dnn_2j  > 0.965'
dymvaVBF  = 'dymva_dnn_VBF > 0.965'
dymvaVH   = 'dymva_dnn_VH  > 0.850'

# Higgs Signal Regions: ee/uu * 0/1/2 jet
cuts['hww2l2v_13TeV'] = {
   'expr': 'sr && (Lepton_pdgId[0]==-Lepton_pdgId[1])' ,
   'categories' : {
       '0j_ee_pt2lt20'         : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Higgs0jet && Lepton_pt[1]< 20 && '+dymva0jet,
       '0j_mm_pt2lt20'         : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Higgs0jet && Lepton_pt[1]< 20 && '+dymva0jet,
       '0j_ee_pt2ge20'         : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Higgs0jet && Lepton_pt[1]>=20 && '+dymva0jet,
       '0j_mm_pt2ge20'         : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Higgs0jet && Lepton_pt[1]>=20 && '+dymva0jet,
       '1j_ee'                 : ' oneJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Higgs1jet && '+dymva1jet,
       '1j_mm'                 : ' oneJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Higgs1jet && '+dymva1jet,
       '2j_ee'                 : '  2jggH && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && Higgs2jet && '+dymva2jet,
       '2j_mm'                 : '  2jggH && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Higgs2jet && '+dymva2jet,
   }
}

## Top CR: No H sel , bTag , tight DYmva
cuts['hww2l2v_13TeV_top']  = {
   'expr' : 'topcr && ZVeto * (Lepton_pdgId[0]==-Lepton_pdgId[1])',
   'categories' : {
      '0j_ee' : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && '+dymva0jet,
      '0j_mm' : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && '+dymva0jet,
      '1j_ee' : ' oneJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && '+dymva1jet,
      '1j_mm' : ' oneJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && '+dymva1jet,
      '2j_ee' : '  2jggH && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && '+dymva2jet,
      '2j_mm' : '  2jggH && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && '+dymva2jet,
   }
}

## WW CR: No H Sel , mll>80, tight DYMva
cuts['hww2l2v_13TeV_WW']  = {
   'expr' : 'wwcr * (Lepton_pdgId[0]==-Lepton_pdgId[1])',
   'categories' : {
      '0j_ee' : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && '+dymva0jet,
      '0j_mm' : 'zeroJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && '+dymva0jet,
      '1j_ee' : ' oneJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && '+dymva1jet,
      '1j_mm' : ' oneJet && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && '+dymva1jet,
      '2j_ee' : '  2jggH && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11) && '+dymva2jet,
      '2j_mm' : '  2jggH && (Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && '+dymva2jet,
   }
}

