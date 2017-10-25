# plot configuration



groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used
#

#groupPlot['DY']  = {  
#                  'nameHR' : "DY",
#                  'isSignal' : 0,
#                  'color': 418,    # kGreen+2
#                  'samples'  : ['DY']
#              }



#groupPlot['top']  = {  
#                  'nameHR' : 'tW and t#bart',
#                  'isSignal' : 0,
#                  'color': 400,   # kYellow
#                  'samples'  : ['top']
#              }

groupPlot['Fake']  = {  
                  'nameHR' : 'Non-prompt',
                  'isSignal' : 0,
                  'color': 921,    # kGray + 1
                  'samples'  : ['Fake']
              }

#groupPlot['WW']  = {  
#                  'nameHR' : 'WW',
#                  'isSignal' : 0,
#                  'color': 851, # kAzure -9 
#                  'samples'  : ['WW']
#              }

groupPlot['VVV']  = {  
                  'nameHR' : 'VVV',
                  'isSignal' : 0,
                  'color': 857, # kAzure -3  
                  'samples'  : ['VVV']
              }


#groupPlot['Vg']  = {
#                  'nameHR' : 'Zg',
#                  'color': 859, # kAzure -1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0,
#                  'samples'  : ['Vg']
#                  }

#groupPlot['WWZ']  = {  
#                  'nameHR' : "WWZ",
#                  'isSignal' : 0,
#                  'color'    : 617,   # kViolet + 1  
#                  'samples'  : ['WWZ']
#              }


groupPlot['ttZ']  = {
                  'nameHR' : "ttZ",
                  'isSignal' : 0,
                  'color'    : 857,   # kAzure  
                  'samples'  : ['ttZ']
              }

groupPlot['WZ']  = {
                  'nameHR' : "WZ",
                  'isSignal' : 0,
                  'color'    : 400,   # Yellow
                  'samples'  : ['WZ']
              }

groupPlot['Higgs']  = {  
                  'nameHR' : 'Higgs',
                  'isSignal' : 2,
                  'color': 632, # kRed 
                  'samples'  : ['ZH_hww', 'ggZH_hww']
              }


#groupPlot['WH_htt']  = {  
#                  'nameHR' : 'WH_htt',
#                  'isSignal' : 2,
#                  'color': 600, # kBlue 
#                  'samples'  : ['WH_htt']
#              }

#groupPlot['WH_hww']  = {  
#                  'nameHR' : 'WH_hww',
#                  'isSignal' : 2,
#                  'color': 800, # kOrange 
#                  'samples'  : ['WH_hww']
#              }

groupPlot['ZH_hww']  = {  
                  'nameHR' : 'ZH_hww',
                  'isSignal' : 2,
                  'color': 618, # kMagenta +2
                  'samples'  : ['ZH_hww']
              }

groupPlot['ggZH_hww']  = {  
                  'nameHR' : 'ggZH_hww',
                  'isSignal' : 2,
                  'color': 632, # kRed 
                  'samples'  : ['ggZH_hww']
              }


plot = {}

# keys here must match keys in samples.py    
#                    
#plot['DY']  = {  
#                  'color': 418,    # kGreen+2
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0,
 #                 'cuts'  : {
#                       'hww2l2v_13TeV_of0j'      : 0.95 ,
#                       'hww2l2v_13TeV_top_of0j'  : 0.95 , 
#                       'hww2l2v_13TeV_dytt_of0j' : 0.95 ,
#                       'hww2l2v_13TeV_em_0j'     : 0.95 , 
#                       'hww2l2v_13TeV_me_0j'     : 0.95 , 
                       #
 #                      'hww2l2v_13TeV_of1j'      : 1.08 ,
 #                      'hww2l2v_13TeV_top_of1j'  : 1.08 , 
 #                      'hww2l2v_13TeV_dytt_of1j' : 1.08 ,
 #                      'hww2l2v_13TeV_em_1j'     : 1.08 , 
 #                      'hww2l2v_13TeV_me_1j'     : 1.08 , 
  #                      },
#
 #             }


               
#plot['Wjets']  = {  
#                  'color': 921,    # kGray + 1
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0                  
#              }



               
plot['Fake']  = {  
                  'color': 921,    # kGray + 1
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0                  
              }

              
#plot['FakeQCD']  = {  
#                  'color': 922,    # kGray + 2
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0                  
#              }



#plot['ttbar'] = {   
#                  'nameHR' : 't#bart',
#                  'color': 400,   # kYellow 
#                  'isSignal' : 0,
#                  'isData'   : 0 ,
#                  'scale'    : 1.0
#                  }


#plot['singletop'] = {   
#                  'nameHR' : 't and tW',
#                  'color': 401,   # kYellow +1
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0
#                  }

#plot['top'] = {   
#                  'nameHR' : 'tW and t#bart',
#                  'color': 400,   # kYellow
#                  'isSignal' : 0,
#                  'isData'   : 0, 
#                  'scale'    : 1.0,
            #      'cuts'  : {
#                       'hww2l2v_13TeV_of0j'      : 0.94 ,
#                       'hww2l2v_13TeV_top_of0j'  : 0.94 , 
#                       'hww2l2v_13TeV_dytt_of0j' : 0.94 ,
#                       'hww2l2v_13TeV_em_0j'     : 0.94 , 
#                       'hww2l2v_13TeV_me_0j'     : 0.94 , 
#                       #
#                       'hww2l2v_13TeV_of1j'      : 0.86 ,
#                       'hww2l2v_13TeV_top_of1j'  : 0.86 , 
#                       'hww2l2v_13TeV_dytt_of1j' : 0.86 ,
#                       'hww2l2v_13TeV_em_1j'     : 0.86 , 
#                       'hww2l2v_13TeV_me_1j'     : 0.86 , 
             #           },
 #                 #}


#plot['WWZ']  = {
#                  'color': 857, # kAzure 
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 30.0   # ele/mu trigger efficiency   datadriven
#                  }

plot['VVV']  = { 
                   'color': 857, # kAzure -3  
		   'isSignal' : 0,
		   'isData'   : 0,
		   'scale'    : 1.0
                   } 

#plot['ggWW']  = {
#                  'color': 850, # kAzure -10
#                  'isSignal' : 0,
#                  'isData'   : 0,    
#                  'scale'    : 1.0
#                  }


#plot['Wg']  = { 
#                  'color': 859, # kAzure -1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }

plot['ttZ']  = { 
                  'color': 922, # kGray+2   
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 30.0
                  }

#plot['VgS'] = { 
#                  'color'    : 617,   # kViolet + 1  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }

#plot['VZ']  = { 
#                  'color': 858, # kAzure -2  
#                  'isSignal' : 0,
#                  'isData'   : 0,
#                  'scale'    : 1.0
#                  }

plot['WZ']  = { 
                  'nameHR' : 'WZ',
                  'color': 418, # kGreen +2 
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 30.0
                  }
plot['ZZ']  = {
                  'color': 854, # kAzure -6 
                  'isSignal' : 0,
                  'isData'   : 0,    
                  'scale'    : 1.0
                  }



# Htautau

#plot['WH_htt'] = {
#                  'nameHR' : 'Htt',
#                  'color': 600, # kBlue 
#                  'isSignal' : 2,
#                  'isData'   : 0,    
#                  'scale'    : 20    #
#                  }

# HWW 

#plot['H_hww'] = {
#                  'nameHR' : 'Hww',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

plot['ZH_hww'] = {
                  'nameHR' : 'ZH',
                  'color': 618, # kMagenta +2
                  'isSignal' : 2,
                  'isData'   : 0,    
                  'scale'    : 20    #
                  }

plot['ggZH_hww'] = {
                  'nameHR' : 'ggZH',
                  'color': 632, # kRed
                  'isSignal' : 2,
                  'isData'   : 0,    
                  'scale'    : 20    #
                  }

#plot['WH_hww'] = {
#                  'nameHR' : 'WH',
#                  'color': 800, # kOrange 
#                  'isSignal' : 2,
#                  'isData'   : 0,    
#                  'scale'    : 20    #
#                  }

#plot['qqH_hww'] = {
#                  'nameHR' : 'qqH',
#                  'color': 632+1, # kRed+1 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }


#plot['ggH_hww'] = {
#                  'nameHR' : 'ggH',
#                  'color': 632, # kRed 
#                  'isSignal' : 1,
#                  'isData'   : 0,    
#                  'scale'    : 1    #
#                  }

# data

plot['DATA']  = { 
                  'nameHR' : 'Data',
                  'color': 1 ,  
                  'isSignal' : 0,
                  'isData'   : 1 ,
                  'isBlind'  : 1
              }




# additional options
legend = {}
legend['lumi'] = 'L = 12.9/fb' # 12.8890 fb-1
legend['sqrt'] = '#sqrt{s} = 13 TeV'




