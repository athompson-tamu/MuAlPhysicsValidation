from ROOT import TFile, TTree, TH1F, TLorentzVector
from ROOT import TLorentzVector
from random import randint
import math, sys, os
from math import fabs
#RUN WITH:
#python make_2d_plots.py ../MuAlAnalyzer/MuAlRefit_Legacy/MuAlRefit_Legacy.root MuAlRefit_Legacy -b

# input arguments, first is input root file, second is output root file 
fileIn = sys.argv[1]
fileOut = sys.argv[2]

# read the input root file
f            = TFile.Open(fileIn, "read")
td           = f.Get("muAlAnalyzer")
Events       = td.Get("Events")
genMuons     = td.Get("genMuons")
recoMuons    = td.Get("recoMuons")
recoDimuons  = td.Get("recoDimuons")
savePng      = True
Event_ro_RUN = -1
#Events.Print(); genMuons.Print(); recoMuons.Print(); recoDimuons.Print()

## First step, define your histograms in histograms.py
execfile("functions.py")
execfile("histograms.py")
## Second step, fill recoMuon and recoDimuon histograms  
execfile("recoMuonLoop.py")
execfile("recoDimuonLoop.py")
execfile("drawPng.py")

	#for counter2, types in enumerate(TH2F_pt_ptRes):

	#	name = TH2F_pt_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TH2F_pt_ptRes[counter2].Fill(refPt,(values[2]-values[3])/values[3] )

	#	name = TH2F_eta_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TH2F_eta_ptRes[counter2].Fill(refEta,(values[2]-values[3])/values[3] )

	#	name = TH2F_phi_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TH2F_phi_ptRes[counter2].Fill(refPhi,(values[2]-values[3])/values[3] )


	#	name =  TProfile_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TProfile_ptRes[counter2].Fill(values[0],values[1],(values[2]-values[3])/values[3])

	#	name =  TProfile_pt_ptRes[counter2].GetName()
	#	values = returnValues(name)
	#	TProfile_ptRes[counter2].Fill(values[0],values[1],(values[2]-values[3])/values[3])

	#print counter, values[0], values[1],values[2], values[3]

#for counter, types in enumerate(TH2F_pt_ptRes):
#	TH2F_pt_ptRes[counter].Draw("colz")
#	c1.SaveAs(TH2F_pt_ptRes[counter].GetName()+".png")
#
#	TH2F_phi_ptRes[counter].Draw("colz")
#	c1.SaveAs(TH2F_phi_ptRes[counter].GetName()+".png")

#	TH2F_eta_ptRes[counter].Draw("colz")
#	c1.SaveAs(TH2F_eta_ptRes[counter].GetName()+".png")
#	TProfile_ptRes[counter].Draw("colz")
#	c1.SaveAs(TProfile_ptRes[counter].GetName()+".png")
#leadingMuonPt.Draw()
#1.SaveAs("leadingMuonPt.root")

outFile.Write()
outFile.Close()
