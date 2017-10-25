# cuts

#cuts = {}
  
supercut = 'mllmin3l>12  \
            && std_vector_lepton_pt[0]>25 && std_vector_lepton_pt[1]>15 \
            && std_vector_lepton_pt[2]>10 \
            && std_vector_lepton_pt[3]<10 \
            && abs(chlll) == 1 \
           '

cuts['preselection']   = '1'


cuts['zh3l_ttZ_13TeV'] = 'njet_3l >= 2 && (( std_vector_jet_cmvav2[0] > -0.715 ) || ( std_vector_jet_cmvav2[1] > -0.715 ) || (std_vector_jet_cmvav2[2] > -0.715 ) || ( std_vector_jet_cmvav2[3] > -0.715 ) || ( std_vector_jet_cmvav2[4] > -0.715 ) || ( std_vector_jet_cmvav2[5] > -0.715 ) || ( std_vector_jet_cmvav2[6] > -0.715 )  || ( std_vector_jet_cmvav2[7] > -0.715 ) || (std_vector_jet_cmvav2[8] > -0.715 ) || ( std_vector_jet_cmvav2[9] > -0.715 )) && metPfType1 > 20 && zveto_3l < 25'



#11 = e
# 13 = mu
# 15 = tau

