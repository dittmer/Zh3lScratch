{
  TFile *f0 = TFile::Open("rootFiles_repro/plots_ZH3l.root");

  TH1F* h_ZH =   (TH1F*) f0->Get("zh3l_13TeV/ptz/histo_ZH_hww");
  TH1F* h_ggZH = (TH1F*) f0->Get("zh3l_13TeV/ptz/histo_ggZH_hww");
  TH1F* h_WZ =   (TH1F*) f0->Get("zh3l_13TeV/ptz/histo_WZ");

  cout << "S/WZ = " << (h_ZH->Integral() + h_ggZH->Integral()) / h_WZ->Integral() << endl;
  cout << "low = " << (h_ZH->Integral(0,10) + h_ggZH->Integral(0,10)) / h_WZ->Integral(0,10) << endl;
  cout << "high = " << (h_ZH->Integral(10,21) + h_ggZH->Integral(10,21)) / h_WZ->Integral(10,21) << endl;

  h_ZH->Rebin(2);
  h_ggZH->Rebin(2);
  h_WZ->Rebin(2);

  h_ZH->SetLineColor(kViolet+1);
  h_ggZH->SetLineColor(kRed);
  h_WZ->SetLineColor(kGreen+2);

  h_ZH->Scale(1./h_ZH->Integral());
  h_ggZH->Scale(1./h_ggZH->Integral());
  h_WZ->Scale(1./h_WZ->Integral());

  h_ZH->Draw("HIST");
  h_WZ->Draw("HIST SAME");
  h_ggZH->Draw("HIST SAME");
}
