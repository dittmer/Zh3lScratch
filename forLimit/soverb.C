
{
  TFile *f0 = TFile::Open("rootFiles_repro/plots_ZH3l.root");

  float n_ZH =   ((TH1F*) f0->Get("preselection/events/histo_ZH_hww"))->GetBinContent(1);
  float n_ggZH = ((TH1F*) f0->Get("preselection/events/histo_ggZH_hww"))->GetBinContent(1);
  float n_WZ =   ((TH1F*) f0->Get("preselection/events/histo_WZ"))->GetBinContent(1);
  float n_ZZ =   ((TH1F*) f0->Get("preselection/events/histo_ZZ"))->GetBinContent(1);
  float n_Fake =   ((TH1F*) f0->Get("preselection/events/histo_Fake"))->GetBinContent(1);
  float n_ttZ =   ((TH1F*) f0->Get("preselection/events/histo_ttZ"))->GetBinContent(1);
  float n_VVV =   ((TH1F*) f0->Get("preselection/events/histo_VVV"))->GetBinContent(1);

  float n_S = n_ZH + n_ggZH;
  float n_B = n_WZ + n_ZZ + n_Fake + n_ttZ + n_VVV;

//			 12345612345612345612345612345612345678123456123456123456123456123456
  cout << endl;
  printf("                 Zh      ggZh    WZ      ZZ      Fake  totBG   S/B\n\n");
  printf("preselection:%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f%6.3f\n", 
      n_ZH, n_ggZH, n_WZ, n_ZZ, n_Fake, n_B, (n_S/n_B));
      

  n_ZH =   ((TH1F*) f0->Get("zh3l_13TeV/events/histo_ZH_hww"))->GetBinContent(1);
  n_ggZH = ((TH1F*) f0->Get("zh3l_13TeV/events/histo_ggZH_hww"))->GetBinContent(1);
  n_WZ =   ((TH1F*) f0->Get("zh3l_13TeV/events/histo_WZ"))->GetBinContent(1);
  n_ZZ =   ((TH1F*) f0->Get("zh3l_13TeV/events/histo_ZZ"))->GetBinContent(1);
  n_Fake =   ((TH1F*) f0->Get("zh3l_13TeV/events/histo_Fake"))->GetBinContent(1);
  n_ttZ =   ((TH1F*) f0->Get("zh3l_13TeV/events/histo_ttZ"))->GetBinContent(1);
  n_VVV =   ((TH1F*) f0->Get("zh3l_13TeV/events/histo_VVV"))->GetBinContent(1);

  n_S = n_ZH + n_ggZH;
  n_B = n_WZ + n_ZZ + n_Fake + n_ttZ + n_VVV;

  printf("base select :%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f%6.3f\n", 
      n_ZH, n_ggZH, n_WZ, n_ZZ, n_Fake, n_B, (n_S/n_B));
      

  n_ZH =   ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_ZH_hww"))->GetBinContent(1);
  n_ggZH = ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_ggZH_hww"))->GetBinContent(1);
  n_WZ =   ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_WZ"))->GetBinContent(1);
  n_ZZ =   ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_ZZ"))->GetBinContent(1);
  n_Fake =   ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_Fake"))->GetBinContent(1);
  n_ttZ =   ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_ttZ"))->GetBinContent(1);
  n_VVV =   ((TH1F*) f0->Get("zh3l_13TeV_step2/events/histo_VVV"))->GetBinContent(1);

  n_S = n_ZH + n_ggZH;
  n_B = n_WZ + n_ZZ + n_Fake + n_ttZ + n_VVV;

  printf("+ dphilmetjj:%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f%6.3f\n", 
      n_ZH, n_ggZH, n_WZ, n_ZZ, n_Fake, n_B, (n_S/n_B));
      
  n_ZH =   ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_ZH_hww"))->GetBinContent(1);
  n_ggZH = ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_ggZH_hww"))->GetBinContent(1);
  n_WZ =   ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_WZ"))->GetBinContent(1);
  n_ZZ =   ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_ZZ"))->GetBinContent(1);
  n_Fake =   ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_Fake"))->GetBinContent(1);
  n_ttZ =   ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_ttZ"))->GetBinContent(1);
  n_VVV =   ((TH1F*) f0->Get("zh3l_13TeV_step3/events/histo_VVV"))->GetBinContent(1);

  n_S = n_ZH + n_ggZH;
  n_B = n_WZ + n_ZZ + n_Fake + n_ttZ + n_VVV;

  printf("+ dmjjmW    :%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f%6.3f\n", 
      n_ZH, n_ggZH, n_WZ, n_ZZ, n_Fake, n_B, (n_S/n_B));
      
  n_ZH =   ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_ZH_hww"))->GetBinContent(1);
  n_ggZH = ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_ggZH_hww"))->GetBinContent(1);
  n_WZ =   ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_WZ"))->GetBinContent(1);
  n_ZZ =   ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_ZZ"))->GetBinContent(1);
  n_Fake =   ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_Fake"))->GetBinContent(1);
  n_ttZ =   ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_ttZ"))->GetBinContent(1);
  n_VVV =   ((TH1F*) f0->Get("zh3l_13TeV_step4/events/histo_VVV"))->GetBinContent(1);

  n_S = n_ZH + n_ggZH;
  n_B = n_WZ + n_ZZ + n_Fake + n_ttZ + n_VVV;

  printf("+ mTlmetjj  :%8.2f%8.2f%8.2f%8.2f%8.2f%8.2f%6.3f\n", 
      n_ZH, n_ggZH, n_WZ, n_ZZ, n_Fake, n_B, (n_S/n_B));
      

  // TH1F* h_ZH =   (TH1F*) f0->Get("zh3l_13TeV_step2/mtw_notZ/histo_ZH_hww");
  // TH1F* h_ggZH = (TH1F*) f0->Get("zh3l_13TeV_step2/mtw_notZ/histo_ggZH_hww");
  // TH1F* h_WZ =   (TH1F*) f0->Get("zh3l_13TeV_step2/mtw_notZ/histo_WZ");

  cout << endl;
}
