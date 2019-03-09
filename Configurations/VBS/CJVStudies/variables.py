# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow

variables['jv']  = {   'name': '1*(std_vector_jet_pt[2]<30)',
                       'range' : (4, -1 ,3),    
                       'xaxis' : 'JV',  
                       'fold' : 3
                       } #if jet veto is satisfied jv is equal to 1, else 0

variables['cjv']  = {  'name': '1*(std_vector_jet_pt[2]<=30 || (std_vector_jet_pt[2]>30 && std_vector_jet_eta[2] < ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) && std_vector_jet_eta[2] > ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) ))',
                      'range': (4,-1,3), 
                      'xaxis': 'CJV',
                      'fold': 3
                      } #if central jet veto is satisfied cjv is equal to 1, else 0

variables['prel']  = {   'name': 'std_vector_lepton_pt[0]/((std_vector_jet_pt[2]>20)*std_vector_jet_pt[2]-1*(std_vector_jet_pt[2]<=20))',
                       'range' : (8, -1 ,7),    
                       'xaxis' : 'p_{t}^{lep1} / p_{t}^{jet3}',  
                       'fold' : 3
                       } #usually jet_pt > 20 (if not verified, use -1 instead of jet_pt)

#variables['pt3']  = {   'name': 'std_vector_jet_pt[2]',
                       #'range' : (10, 0 ,100),    
                       #'xaxis' : 'p_{t}^{jet3} [GeV]',  
                       #'fold' : 3
                       #}

#variables['etacond']  = {  'name': 'std_vector_jet_eta[2] < ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[0]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[1]) && std_vector_jet_eta[2] > ((std_vector_jet_eta[0]<std_vector_jet_eta[1])*std_vector_jet_eta[1]+(std_vector_jet_eta[0]>=std_vector_jet_eta[1])*std_vector_jet_eta[0]) ',
                      #'range': (4,-1,3), 
                      #'xaxis': '#eta condition',
                      #'fold': 3
                      #}

# variables['events']  = {   'name': '1',      
                        # 'range' : (1,0,2),  
                        # 'xaxis' : 'events', 
                         # 'fold' : 3
                        # }

# variables['njet']  = {   'name': 'njet',
                       # 'range' : (6,0,6),
                       # 'xaxis' : 'njets',
                        # 'fold' : 3
                       # }


# variables['nlep'] =  {
                # 'name': '1*(std_vector_lepton_pt[0]>20) + 1*(std_vector_lepton_pt[1]>20) + 1*(std_vector_lepton_pt[2]>20)+ 1*(std_vector_lepton_pt[3]>20) + 1*(std_vector_lepton_pt[4]>20)',
                # 'range': (5,0,5),
                # 'xaxis': '# leptons',
                # 'fold': 3
        # }

# variables['nele'] =  {
                # 'name': '1*(std_vector_lepton_pt[0]>20 && abs(std_vector_lepton_flavour[0])==11) + 1*(std_vector_lepton_pt[1]>20 && abs(std_vector_lepton_flavour[1])==11) + 1*(std_vector_lepton_pt[2]>20 && abs(std_vector_lepton_flavour[2])==11)+ 1*(std_vector_lepton_pt[3]>20 && abs(std_vector_lepton_flavour[3])==11) + 1*(std_vector_lepton_pt[4]>20 && abs(std_vector_lepton_flavour[4])==11)',
                # 'range': (5,0,5),
                # 'xaxis': '# electrons',
                # 'fold': 3
        # }


# variables['nmu'] =  {
                # 'name': '1*(std_vector_lepton_pt[0]>20 && abs(std_vector_lepton_flavour[0])==13) + 1*(std_vector_lepton_pt[1]>20 && abs(std_vector_lepton_flavour[1])==13) + 1*(std_vector_lepton_pt[2]>20 && abs(std_vector_lepton_flavour[2])==13)+ 1*(std_vector_lepton_pt[3]>20 && abs(std_vector_lepton_flavour[3])==13) + 1*(std_vector_lepton_pt[4]>20 && abs(std_vector_lepton_flavour[4])==13)',
                # 'range': (5,0,5),
                # 'xaxis': '# muons',
                # 'fold': 3
        # }

#variables['mll']  = {   'name': 'mll',            #   variable name
                       #'range' : (10, 0. ,200),    #   variable range
                       #'xaxis' : 'mll [GeV]',  #   x axis name
                       #'fold' : 3
                       #}


variables['mjj']  = {  'name': 'mjj',
                      'range': (10,500,2000),
                      'xaxis': 'm_{jj} [GeV]',
                      'fold': 3
                      }
                      
# variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',     
                       # 'range' : (10,0.,150),   
                       # 'xaxis' : 'p_{T} 1st lep',
                       # 'fold'  : 3                         
                       # }

# variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',        
                       # 'range' : (10,0.,100),   
                       # 'xaxis' : 'p_{T} 2nd lep',
                       # 'fold'  : 3                         
                       # }

# variables['jetpt1']  = {   'name': 'std_vector_jet_pt[0]',     
                       # 'range' : (15,0.,200),   
                       # 'xaxis' : 'p_{T} 1st jet',
                       # 'fold'  : 3                        
                       # }

# variables['jetpt2']  = {   'name': 'std_vector_jet_pt[1]',     
                       # 'range' : (15,0.,100),   
                       # 'xaxis' : 'p_{T} 2nd jet',
                       # 'fold'  : 3                       
                       # }


# variables['met']  = {   'name': 'metPfType1',            #   variable name    
                       # 'range' : (10,0,200),    #   variable range
                       # 'xaxis' : 'pfmet [GeV]',  #   x axis name
                       # 'fold' : 3
                       # }

#variables['etaj1'] = {  'name': 'std_vector_jet_eta[0]',
                        #'range': (10,-5,5),
                       # 'xaxis': '#eta^{jet1}',
                        #'fold': 3
                    # }

#variables['etaj2'] = {  'name': 'std_vector_jet_eta[1]',
                   #     'range': (10,-5,5),
                    #    'xaxis': '#eta^{jet2}',
                     #   'fold': 3
                     #}

variables['detajj']  = { 'name': 'detajj',
                         'range': (14,2,9),
			 'xaxis': '#Delta#eta_{jj}',
                         'fold': 3
                       }

# variables['Zlep1']  = {  'name': '(std_vector_lepton_eta[0] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj',
                      # 'range': (10,-1.5,1.5),
                      # 'xaxis': 'Z^{lep}_{1}',
                      # 'fold': 3
                      # }

# variables['Zlep2']  = {  'name': '(std_vector_lepton_eta[1] - (std_vector_jet_eta[0]+std_vector_jet_eta[1])/2)/detajj',
                      # 'range': (10,-1.5,1.5),
                      # 'xaxis': 'Z^{lep}_{2}',
                      # 'fold': 3
                      # }

# variables['csvv2ivf_1']  = { 
                        # 'name': 'std_vector_jet_csvv2ivf[0]',     
                        # 'range' : (10,0,1),   
                        # 'xaxis' : 'csvv2ivf 1st jet ',
                        # 'fold'  : 3                         
                        # }



# variables['csvv2ivf_2']  = { 
                        # 'name': 'std_vector_jet_csvv2ivf[1]',     
                        # 'range' : (10,0,1),   
                        # 'xaxis' : 'csvv2ivf 2nd jet ',
                        # 'fold'  : 3                         
                        # }
