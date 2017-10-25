# variables

#variables = {}
    
#'fold' : # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
   
variables['events']  = {   'name': '1',      
                        'range' : (1,0,2),  
                        'xaxis' : 'events', 
                         'fold' : 3
                        }

variables['njet'] = { 	'name'  : 'njet',
  			'range' : (10,0,10),
			'xaxis' : 'N_{jet}',
                         'fold' : 0
                        }

variables['z4lveto']  = {   'name': 'z4lveto',
                        'range' : (20,0,200),
                        'xaxis' : '|m_{lll}-m_{Z}| [GeV]',
                         'fold' : 0
                        }

variables['dmjjmW']  = {   'name': 'dmjjmW',
                        'range' : (15,-100,200),
                        'xaxis' : 'm_{jj}-m_{W}',
                         'fold' : 0
                        }

variables['mtw_notZ']  = {   'name': 'mtw_notZ',
                        'range' : (20,0,200),
                        'xaxis' : 'mT(notZ) [GeV]',
                         'fold' : 0
                        }

variables['dphilmetjj']  = {   'name': 'dphilmetjj',
                        'range' : (10,0,3.14159),
                        'xaxis' : '#Delta#Phi_{MET-jj} ',
                         'fold' : 0
                        }
 
variables['mTlmetjj']  = {   'name': 'mTlmetjj',
                        'range' : (13,0,260),
                        'xaxis' : 'm_{T} (l #nu jj) [GeV]',
                         'fold' : 0
                        }

variables['pt1']  = {   'name': 'std_vector_lepton_pt[0]',            #   variable name    
                        'range' : (20,0.,200),    #   variable range
                        'xaxis' : 'lept1_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }
    
variables['pt2']  = {   'name': 'std_vector_lepton_pt[1]',            #   variable name    
                        'range' : (20,0.,200),    #   variable range
                        'xaxis' : 'lept2_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['pt3']  = {   'name': 'std_vector_lepton_pt[2]',            #   variable name    
                        'range' : (20,0.,200),    #   variable range
                        'xaxis' : 'lept3_p_{T} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['zveto_3l']  = {   'name': 'zveto_3l',            #   variable name    
                        'range' : (20,0,100),    #   variable range
                        'xaxis' : 'm_{ll} - M_{Z} [GeV]',  #   x axis name
                         'fold' : 0
                        }


variables['ptz']  = {   'name': 'ptz',            #   variable name    
                        'range' : (20,0,200),    #   variable range
                        'xaxis' : 'p_{T}^{Z} [GeV]',  #   x axis name
                         'fold' : 0
                        }

variables['checkmZ']  = { 'name': 'checkmZ',            #   variable name    
                        'range' : (30,0,150),    #   variable range
                        'xaxis' : 'm_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }


variables['drllmin3l']  = {   'name': 'drllmin3l',            #   variable name    
#                        'range' : (6,0,4),    #   variable range
                         'range' : ([0.,0.75, 1.5, 2.0, 2.5, 4.0],),    #   variable range
#                      #   'range' : ([0.,0.5,1.0,1.5,2.0,3.0,4.0],),    #   variable range
                        'xaxis' : 'min #Delta R_{ll}',  #   x axis name
                         'fold' : 0
                        }

variables['mllmin3l']  = {   'name': 'mllmin3l',            #   variable name    
                       'range' : (15,10,150),    #   variable range
                        'xaxis' : 'min m_{ll} [GeV]',  #   x axis name
                         'fold' : 0
                        }


variables['mlll']  = {   'name': 'mlll',            #   variable name    
                        'range' : (50,0.,500),    #   variable range
                        'xaxis' : 'm_{lll} [GeV]',  #   x axis name
                        'fold' : 0
                        }

variables['btagj0']  = {'name': 'std_vector_jet_cmvav2[0]',            #   variable name    
                        'range' : (48,-1.2,1.2),    #   variable range
                        'xaxis' : 'cmvav2[0]',  #   x axis name
                        'fold' : 0
                        }



variables['met']  = {   'name': 'metPfType1',            #   variable name    
                        'range' : (10,0,200),    #   variable range
                        'xaxis' : 'pfmet [GeV]',  #   x axis name
                       'fold' : 0
                      }
