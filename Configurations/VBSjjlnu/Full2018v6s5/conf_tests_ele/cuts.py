# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>35)\
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && vbs_0_pt > 50 && vbs_1_pt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs >= 2.5  \
            && mjj_vbs >= 500 \
            && Mtw_lep < 185 \
            '



cuts["res_wjetcr_ele_incl"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                '


cuts["res_wjetcr_ele_incl_loweta"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && abs(Lepton_eta[0])< 2\
                                '

cuts["res_wjetcr_ele_incl_higheta"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && abs(Lepton_eta[0]) >= 2 \
                                '

cuts["res_wjetcr_ele_incl_loweta_highnvtx"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && abs(Lepton_eta[0])< 2\
                                && PV_npvs >= 25\
                                '

cuts["res_wjetcr_ele_incl_higheta_highnvtx"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && abs(Lepton_eta[0]) >= 2 \
                                &&  PV_npvs >= 25\
                                '

cuts["res_wjetcr_ele_incl_loweta_lownvtx"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && abs(Lepton_eta[0])< 2\
                                && PV_npvs < 25\
                                '

cuts["res_wjetcr_ele_incl_higheta_lownvtx"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && whad_pt < 200 \
                                && abs(Lepton_eta[0]) >= 2 \
                                && PV_npvs < 25 \
                                '



cuts["boost_wjetcr_ele_incl"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && vjet_0_pt > 200 \
                            && (mjj_vjet <= 65 || mjj_vjet >= 105)  \
                            && bVeto \
                            '



cuts["boost_wjetcr_ele_loweta"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && vjet_0_pt > 200 \
                            && (mjj_vjet <= 65 || mjj_vjet >= 105)  \
                            && bVeto \
                            && abs(Lepton_eta[0])< 2 \
                             '



cuts["boost_wjetcr_ele_higheta"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && vjet_0_pt > 200 \
                            && (mjj_vjet <= 65 || mjj_vjet >= 105)  \
                            && bVeto \
                            && abs(Lepton_eta[0]) >= 2 \
                            '

                   