# samples

#samples = {}


# data driven
samples['Fake']  = {    'name': [
				'latino_DoubleEG_fake.root',
				'latino_DoubleMuon_fake.root',
				'latino_SingleMuon_fake.root',
				'latino_SingleElectron_fake.root',
				'latino_MuonEG_fake.root'
                                ],
                     'weight' : 'fakeW3l',              #   weight/cut 
                     #'weight' : 'fakeW3l',              #   weight/cut 
                     'isData': ['all'],   
                     'weights' : [
                                   'std_vector_trigger[8]  || std_vector_trigger[6]',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) &&  (std_vector_trigger[13] || std_vector_trigger[11])',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) && !(std_vector_trigger[13] || std_vector_trigger[11]) &&  (std_vector_trigger[42] || std_vector_trigger[43])',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) && !(std_vector_trigger[13] || std_vector_trigger[11]) && !(std_vector_trigger[42] || std_vector_trigger[43]) &&  (std_vector_trigger[46])',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) && !(std_vector_trigger[13] || std_vector_trigger[11]) && !(std_vector_trigger[42] || std_vector_trigger[43]) && !(std_vector_trigger[46])  && (std_vector_trigger[0] || std_vector_trigger[56])'
                            ],                          
                 }



samples['ttZ']  = {    'name': ['latino_TTZToLLNuNu_M-10.root'],      
                      'weight' : 'puW*baseW*bPogSF*effTrigW3l*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_idisoW[2]*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1]*std_vector_lepton_recoW[2]',
 #                     'weights': ['1'] ,           
                      'isData': ['0'],                            
                  }


samples['WZ']  = {    'name': [
                          'latino_WZTo3LNu.root'
         #                 'latino_WZ.root'
                         ],
                      'weight' : 'puW*baseW*bPogSF*effTrigW3l*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_idisoW[2]*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1]*std_vector_lepton_recoW[2]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*std_vector_lepton_genmatched[2]*GEN_weight_SM/abs(GEN_weight_SM)',
#                      'weights': ['0.002214825'] ,           
                      #'isData': ['0'],                            
                  }


samples['ZZ']  = {    'name': [
                          'latino_ZZTo4L.root'
                         ],
                      'weight' : 'puW*baseW*bPogSF*effTrigW3l*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_idisoW[2]*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1]*std_vector_lepton_recoW[2]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*std_vector_lepton_genmatched[2]*GEN_weight_SM/abs(GEN_weight_SM)',
#                      'weights': ['0.002214825'] ,           
                      #'isData': ['0'],                            
                  }


samples['VVV'] = {    'name': [
                          'latino_WZZ.root', 
#                          'latino_ZZZ.root',
                          'latino_WWW.root',
                          'latino_WWZ.root'
                          ],      
                      'weight' : 'puW*baseW*bPogSF*effTrigW3l*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_idisoW[2]*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1]*std_vector_lepton_recoW[2]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*std_vector_lepton_genmatched[2]*GEN_weight_SM/abs(GEN_weight_SM)',          
                      #'isData': ['0'],                            
                  }


# HWW 

samples['ggZH_hww']  = {    'name': [
                               'latino_ggZH_HToWW_M125.root',
                               ],      
                           'weight' : 'puW*baseW*bPogSF*effTrigW3l*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_idisoW[2]*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1]*std_vector_lepton_recoW[2]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*std_vector_lepton_genmatched[2]*GEN_weight_SM/abs(GEN_weight_SM)',          
                  }


samples['ZH_hww']  = {    'name': ['latino_HZJ_HToWW_M125.root'],      
                           'weight' : 'puW*baseW*bPogSF*effTrigW3l*std_vector_lepton_idisoW[0]*std_vector_lepton_idisoW[1]*std_vector_lepton_idisoW[2]*std_vector_lepton_recoW[0]*std_vector_lepton_recoW[1]*std_vector_lepton_recoW[2]*std_vector_lepton_genmatched[0]*std_vector_lepton_genmatched[1]*std_vector_lepton_genmatched[2]*GEN_weight_SM/abs(GEN_weight_SM)',          
                  }


###########################################
###########################################
###########################################

samples['DATA']  = {   'name': [
				'latino_DoubleEG_data.root',
				'latino_DoubleMuon_data.root',
				'latino_MuonEG_data.root',
				'latino_SingleElectron_data.root',
				'latino_SingleMuon_data.root'


                                ] ,     
                       'weight' : '1',
              #         'weight' : 'std_vector_trigger[43]', #single mu PD
 #                      'weight' : 'std_vector_trigger[0]', #single ele PD
                       'isData': ['all'],

                       'weights' : [
                                   #
                                   'std_vector_trigger[8]  || std_vector_trigger[6]',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) &&  (std_vector_trigger[13] || std_vector_trigger[11])',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) && !(std_vector_trigger[13] || std_vector_trigger[11]) &&  (std_vector_trigger[42] || std_vector_trigger[43])',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) && !(std_vector_trigger[13] || std_vector_trigger[11]) && !(std_vector_trigger[42] || std_vector_trigger[43]) &&  (std_vector_trigger[46])',
                                   '!(std_vector_trigger[8]  || std_vector_trigger[6]) && !(std_vector_trigger[13] || std_vector_trigger[11]) && !(std_vector_trigger[42] || std_vector_trigger[43]) && !(std_vector_trigger[46])  && (std_vector_trigger[0] || std_vector_trigger[56])'
                         ],                            
                  }




