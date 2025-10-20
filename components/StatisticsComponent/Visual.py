# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 11:46:59 2024

@author: mfirat
"""

##### import ipywidgets as widgets
from IPython.display import clear_output
from IPython import display
from ipywidgets import *
from datetime import timedelta,date,datetime
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import os
import pandas as pd
import warnings
import sys
import numpy as np
from pathlib import Path
from IPython.display import display, HTML
from scipy.stats import uniform, norm, expon, gamma
import numpy as np
import math
from matplotlib.ticker import PercentFormatter

from .Statistics import *


warnings.filterwarnings("ignore")
display(HTML("<style>.red_label { color:red }</style>"))
display(HTML("<style>.blue_label { color:blue }</style>"))

class VisualManager():

    def __init__(self, visualManager):

        self.visualManager = visualManager  
        self.DFPage = None
        self.caseexp = None
        self.POPMEANtxt = None
        self.SAMPSIZEtxt = None     
        self.SAMPMEANtxt = None
        self.POPMEANtxt = None
        self.POPgiven = None
        self.stdtype = None
        self.mytxt = None
        self.exmplst = None
        self.sampstdev = None
        self.testingtext = None
        self.resultexp = None
        self.alternative = None
        self.probtype = None
        self.hyptype = None
        self.mybutton2 = None
        self.conflvl = None
        self.folderselect = None
        self.InvFigPage = None
        self.mybutton3 = None
        self.linelabel = None
        self.smapchange = None
        self.readpfile = None
        self.prfeatures = None
        self.addpr = None
        self.add2pr = None
        self.poplbl = None
        self.poplbl2 = None
        self.popemplbl = None
        self.poptypes = None
        self.popsizetxt= None
        self.popmeantxt= None
        self.popstdevtxt= None
        self.popempmeantxt=  None
        self.popempstdevtxt=  None
        self.PopPage = None
        self.smpmeantxt = None
        self.smpstdevtxt = None
        self.smpsetsizetxt = None
        self.smpsetmeantxt = None
        self.smpsetstdevtxt = None
        self.SampleSets = None
        self.smplay = None
        self.smplbl=  None
        self.smpsizetxt=  None
        self.Population = None 
        self.gnrlbl = None
        self.resbutton = None
        self.chk1 = None
        self.chk2 = None
        self.AvgProg = None 
        self.prtt_bef_feat = None
        self.prtt_aft_feat = None
        self.items = None
        self.items2 = None
        self.Sample = None
        self.SampleSet = None
        self.prd_ttest_df = None
        self.sampleprogress = None

        self.features = None
        self.anova_cat_feat = None
        self.anova_value_feat = None
        self.anova_df = None
        self.source = None

        self.readfile =  None
        self.add =  None
        self.add2 =  None
        self.solveanova =  None
        self.dataout= None
        self.boxout= None
        self.resultout= None

        return

    def getresultout(self):
        return self.resultout

    def setresultout(self,myit):
        self.resultout = myit
        return

    def getboxout(self):
        return self.boxout

    def setboxout(self,myit):
        self.boxout = myit
        return
        

    def getdataout(self):
        return self.dataout

    def setdataout(self,myit):
        self.dataout = myit
        return


    def getsolveanova(self):
        return self.solveanova

    def setsolveanova(self,myit):
        self.solveanova = myit
        return

    def getadd2(self):
        return self.add2

    def setadd2(self,myit):
        self.add2 = myit
        return



    def getadd(self):
        return self.add

    def setadd(self,myit):
        self.add = myit
        return


    
    def getreadfile(self):
        return self.readfile

    def setreadfile(self,myit):
        self.readfile = myit
        return

    
    def getsource(self):
        return self.source

    def setsource(self,myit):
        self.source = myit
        return
        
    def getanova_value_feat(self):
        return self.anova_value_feat

    def setanova_value_feat(self,myit):
        self.anova_value_feat = myit
        return


    def getanova_cat_feat(self):
        return self.anova_cat_feat

    def setanova_cat_feat(self,myit):
        self.anova_cat_feat = myit
        return


    def getfeatures(self):
        return self.features

    def setfeatures(self,myit):
        self.features = myit
        return

    def getanova_df(self):
        return self.anova_df

    def setanova_df(self,myit):
        self.anova_df = myit
        return

    def getsampleprogress(self):
        return self.sampleprogress

    def setsampleprogress(self,myit):
        self.sampleprogress = myit
        return


    def getprd_ttest_df(self):
        return self.prd_ttest_df

    def setprd_ttest_df(self,myit):
        self.prd_ttest_df = myit
        return

    
    def getSampleSet(self):
        return self.SampleSet

    def setSampleSet(self,myit):
        self.SampleSet = myit
        return

    def getSample(self):
        return self.Sample

    def setSample(self,myit):
        self.Sample = myit
        return

    def getitems2(self):
        return self.items2

    def setitems2(self,myit):
        self.items2 = myit
        return

    def getitems(self):
        return self.items

    def setitems(self,myit):
        self.items = myit
        return


    def getprtt_aft_feat(self):
        return self.prtt_aft_feat

    def setprtt_aft_feat(self,myit):
        self.prtt_aft_feat = myit
        return

    def getprtt_bef_feat(self):
        return self.prtt_bef_feat

    def setprtt_bef_feat(self,myit):
        self.prtt_bef_feat = myit
        return

 
    def getAvgProg(self):
        return self.AvgProg

    def setAvgProg(self,myit):
        self.AvgProg = myit
        return

    def getchk2(self):
        return self.chk2

    def setchk2(self,myit):
        self.chk2 = myit
        return


    def getchk1(self):
        return self.chk1

    def setchk1(self,myit):
        self.chk1 = myit
        return


    def getresbutton(self):
        return self.resbutton

    def setresbutton(self,myit):
        self.resbutton = myit
        return


    def getgnrlbl(self):
        return self.gnrlbl

    def setgnrlbl(self,myit):
        self.gnrlbl = myit
        return 



    def getPopulation(self):
        return self.Population

    def setPopulation(self,myit):
        self.Population = myit
        return 


    def getsmpsizetxt(self):
        return self.smpsizetxt

    def setsmpsizetxt(self,myit):
        self.smpsizetxt = myit
        return 


    def getsmplbl(self):
        return self.smplbl

    def setsmplbl(self,myit):
        self.smplbl = myit
        return 


    def getsmplay(self):
        return self.smplay

    def setsmplay(self,myit):
        self.smplay = myit
        return 


    def getSampleSets(self):
        return self.SampleSets

    def setSampleSets(self,myit):
        self.SampleSets = myit
        return 


    def getsmpsetstdevtxt(self):
        return self.smpsetstdevtxt

    def setsmpsetstdevtxt(self,myit):
        self.smpsetstdevtxt = myit
        return 


    
    def getsmpsetmeantxt(self):
        return self.smpsetmeantxt

    def setsmpsetmeantxt(self,myit):
        self.smpsetmeantxt = myit
        return 

    def getsmpsetsizetxt(self):
        return self.smpsetsizetxt

    def setsmpsetsizetxt(self,myit):
        self.smpsetsizetxt = myit
        return 

    def getsmpstdevtxt(self):
        return self.smpstdevtxt

    def setsmpstdevtxt(self,myit):
        self.smpstdevtxt = myit
        return 

    def getsmpmeantxt(self):
        return self.smpmeantxt

    def setsmpmeantxt(self,myit):
        self.smpmeantxt = myit
        return 

    def getPopPage(self):
        return self.PopPage

    def setPopPage(self,myit):
        self.PopPage = myit
        return 

    def getpopempstdevtxt(self):
        return self.popempstdevtxt

    def setpopempstdevtxt(self,myit):
        self.popempstdevtxt = myit
        return 
    
    def getpopempmeantxt(self):
        return self.popempmeantxt

    def setpopempmeantxt(self,myit):
        self.popempmeantxt = myit
        return 
    
    def getpopstdevtxt(self):
        return self.popstdevtxt

    def setpopstdevtxt(self,myit):
        self.popstdevtxt = myit
        return 

    
    def getpopmeantxt(self):
        return self.popmeantxt

    def setpopmeantxt(self,myit):
        self.popmeantxt = myit
        return 

        
    def getpopsizetxt(self):
        return self.popsizetxt

    def setpopsizetxt(self,myit):
        self.popsizetxt = myit
        return 

    def getpoptypes(self):
        return self.poptypes

    def setpoptypes(self,myit):
        self.poptypes = myit
        return 

    def getpopemplbl(self):
        return self.popemplbl

    def setpopemplbl(self,myit):
        self.popemplbl = myit
        return 

    def getpoplbl2(self):
        return self.poplbl2

    def setpoplbl2(self,myit):
        self.poplbl2 = myit
        return 


    def getpoplbl(self):
        return self.poplbl

    def setpoplbl(self,myit):
        self.poplbl = myit
        return 

    def getadd2pr(self):
        return self.add2pr

    def setadd2pr(self,myit):
        self.add2pr = myit
        return 


    def getaddpr(self):
        return self.addpr

    def setaddpr(self,myit):
        self.addpr = myit
        return 


    def getprfeatures(self):
        return self.prfeatures

    def setprfeatures(self,myit):
        self.prfeatures = myit
        return 

    def getreadpfile(self):
        return self.readpfile

    def setreadpfile(self,myit):
        self.readpfile = myit
        return 

    def getsmapchange(self):
        return self.smapchange

    def setsmapchange(self,myit):
        self.smapchange = myit
        return  


    def getlinelabel(self):
        return self.linelabel

    def setlinelabel(self,myit):
        self.linelabel = myit
        return  

    def getmybutton3(self):
        return self.mybutton3

    def setmybutton3(self,myit):
        self.mybutton3 = myit
        return


    def getInvFigPage(self):
        return self.InvFigPage

    def setInvFigPage(self,myit):
        self.InvFigPage = myit
        return


    def getfolderselect(self):
        return self.folderselect

    def setfolderselect(self,myit):
        self.folderselect = myit
        return


    def getconflvl(self):
        return self.conflvl

    def setconflvl(self,myit):
        self.conflvl = myit
        return


    def getmybutton2(self):
        return self.mybutton2

    def setmybutton2(self,myit):
        self.mybutton2 = myit
        return

    def gethyptype(self):
        return self.hyptype

    def sethyptype(self,myit):
        self.hyptype = myit
        return

    def getprobtype(self):
        return self.probtype

    def setprobtype(self,myit):
        self.probtype = myit
        return
    
    


    def getalternative(self):
        return self.alternative

    def setalternative(self,myit):
        self.alternative = myit
        return
    
        
    def getresultexp(self):
        return self.resultexp

    def setresultexp(self,myit):
        self.resultexp = myit
        return

    def gettestingtext(self):
        return self.testingtext

    def settestingtext(self,myit):
        self.testingtext = myit
        return


    def getsampstdev(self):
        return self.sampstdev

    def setsampstdev(self,myit):
        self.sampstdev = myit
        return


    def getexmplst(self):
        return self.exmplst

    def setexmplst(self,myit):
        self.exmplst = myit
        return


    def getmytxt(self):
        return self.mytxt

    def setmytxt(self,myit):
        self.mytxt = myit
        return


    def getstdtype(self):
        return self.stdtype

    def setstdtype(self,myit):
        self.stdtype = myit
        return


    def getPOPgiven(self):
        return self.POPgiven

    def setPOPgiven(self,myit):
        self.POPgiven = myit
        return


    def getSAMPMEANtxt(self):
        return self.SAMPMEANtxt

    def setSAMPMEANtxt(self,myit):
        self.SAMPMEANtxt = myit
        return

    def getDFPage(self):
        return self.DFPage

    def setDFPage(self,myit):
        self.DFPage = myit
        return
    
    def getcaseexp(self):
        return self.caseexp

    def setcaseexp(self,myit):
        self.caseexp = myit
        return

    def getPOPMEANtxt(self):
        return self.POPMEANtxt

    def setPOPMEANtxt(self,myit):
        self.POPMEANtxt = myit
        return

    def getSAMPSIZEtxt(self):
        return self.SAMPSIZEtxt

    def setSAMPSIZEtxt(self,myit):
        self.SAMPSIZEtxt = myit
        return



    def ApplyProblem(self,b):

        self.gettestingtext().value = " configuration...: "+str(self.getprobtype().value)+"\n"

        if self.getprobtype().value == "One sample mean":
            self.getDFPage().layout.visibility= 'hidden'
            self.getDFPage().layout.display = 'none'
            self.getcaseexp().layout.display= 'block'
            self.getcaseexp().layout.visibility = 'visible'
            self.getPOPMEANtxt().description = 'P.Mean'
            self.getPOPMEANtxt().layout.visibility = 'visible'
            self.getSAMPSIZEtxt().description = 'S.Size'
            self.getSAMPSIZEtxt().layout.visibility = 'visible'
            self.getSAMPMEANtxt().description = 'S.Mean'
            self.getSAMPMEANtxt().layout.visibility = 'visible'
            self.getPOPMEANtxt().description = 'P.Mean'
            self.getPOPgiven().layout.visibility = 'visible'
            self.getstdtype().layout.visibility = 'visible'
            self.getmytxt().description = 'StDev'
            self.getmytxt().layout.visibility = 'visible'
            self.getfolderselect().layout.visibility= 'hidden'
            self.getfolderselect().layout.display= 'none'
            self.getexmplst().layout.visibility = 'visible'
            self.getreadpfile().layout.visibility= 'hidden'
            self.getreadpfile().layout.display= 'none'
            self.getprfeatures().layout.visibility= 'hidden'
            self.getprfeatures().layout.display= 'none'
            self.getaddpr().layout.visibility= 'hidden'
            self.getaddpr().layout.display= 'none'
            self.getadd2pr().layout.visibility= 'hidden'
            self.getadd2pr().layout.display= 'none'
            self.getlinelabel().layout.visibility= 'hidden'
            self.getlinelabel().layout.display= 'none'
            
        if self.getprobtype().value == "Proportion":
            self.getDFPage().layout.visibility= 'hidden'
            self.getDFPage().layout.display = 'none'
            self.getcaseexp().layout.display= 'block'
            self.getcaseexp().layout.visibility = 'visible'
            self.getPOPMEANtxt().description = 'P.Proportion'
            self.getPOPMEANtxt().layout.visibility = 'visible'
            self.getSAMPSIZEtxt().layout.visibility = 'visible'
            self.getSAMPMEANtxt().description = 'S.Positives'
            self.getSAMPMEANtxt().layout.visibility = 'visible'
            self.getmytxt().layout.visibility = 'hidden'
            self.getPOPgiven().layout.visibility = 'hidden'
            self.getstdtype().layout.visibility = 'hidden'
            self.getfolderselect().layout.visibility= 'hidden'
            self.getfolderselect().layout.display= 'none'
            self.getexmplst().layout.visibility = 'visible'
            self.getreadpfile().layout.visibility= 'hidden'
            self.getreadpfile().layout.display= 'none'
            self.getprfeatures().layout.visibility= 'hidden'
            self.getprfeatures().layout.display= 'none'
            self.getaddpr().layout.visibility= 'hidden'
            self.getaddpr().layout.display= 'none'
            self.getadd2pr().layout.visibility= 'hidden'
            self.getadd2pr().layout.display= 'none'
            self.getlinelabel().layout.visibility= 'hidden'
            self.getlinelabel().layout.display= 'none'
            self.gettestingtext().value = "Proportion  configuration...: "+"\n"
            
        if self.getprobtype().value  == "Difference between two means":
            self.getDFPage().layout.visibility= 'hidden'
            self.getDFPage().layout.display = 'none'
            self.getcaseexp().layout.display= 'block'
            self.getcaseexp().layout.visibility = 'visible'
            self.getPOPMEANtxt().description = 'Mean Diff.'
            self.getSAMPSIZEtxt().description = 'S.Sizes'
            self.getSAMPMEANtxt().layout.visibility='visible'
            self.getSAMPMEANtxt().description = 'S.Means'
            self.getmytxt().layout.visibility = 'visible'
            self.getmytxt().description = 'StDevs'
            self.getstdtype().layout.visibility = 'hidden'
            self.getfolderselect().layout.visibility= 'hidden'
            self.getfolderselect().layout.display= 'none'
            self.getexmplst().layout.visibility = 'visible'
            self.getreadpfile().layout.visibility= 'hidden'
            self.getreadpfile().layout.display= 'none'
            self.getprfeatures().layout.visibility= 'hidden'
            self.getprfeatures().layout.display= 'none'
            self.getaddpr().layout.visibility= 'hidden'
            self.getaddpr().layout.display= 'none'
            self.getadd2pr().layout.visibility= 'hidden'
            self.getadd2pr().layout.display= 'none'
            self.getlinelabel().layout.visibility= 'hidden'
            self.getlinelabel().layout.display= 'none'
    
        if self.getprobtype().value == "Paired sampled t-test":
            self.getDFPage().layout.display = 'block'
            self.getDFPage().layout.visibility= 'visible'
            self.getexmplst().layout.visibility = 'hidden'
            self.getfolderselect().layout.display= 'block'
            self.getfolderselect().layout.visibility= 'visible'
            self.getPOPMEANtxt().description = 'Mean Diff.'
            self.getSAMPSIZEtxt().description = 'S.Size'
            self.getSAMPMEANtxt().layout.visibility='visible'
            self.getcaseexp().layout.visibility='hidden'
            self.getcaseexp().layout.display= 'none'
            self.getstdtype().layout.visibility='hidden'
            self.getreadpfile().layout.display = 'block'
            self.getreadpfile().layout.visibility= 'visible'
            self.getprfeatures().layout.display = 'block'
            self.getprfeatures().layout.visibility= 'visible'
            self.getaddpr().layout.display = 'block'
            self.getaddpr().layout.visibility= 'visible'
            self.getadd2pr().layout.display = 'block'
            self.getadd2pr().layout.visibility= 'visible'
            self.getlinelabel().layout.display = 'block'
            self.getlinelabel().layout.visibility= 'visible'
    
            return


    def CheckInputComplete(self,mode):
    
        if not is_float(self.getPOPMEANtxt().value):
            return False
        
        if not is_float(self.getSAMPMEANtxt().value):
            return False
        
        if not is_float(self.getSAMPSIZEtxt().value):
            return False
    
        if mode.find('One sample mean') > -1: 
            if not is_float(self.getmytxt().value):
                return False
        
                
        return True

    def Sample_Change(self,Size_delta):
        
        
        self.setsmapchange(Size_delta)
        
       
        if not self.getSAMPSIZEtxt().value.isnumeric():
            return
    
        if self.getsmapchange()+int(self.getSAMPSIZEtxt().value) < 2:
            return
         
            
        self.PlotNumbers(self.getconflvl().value)
    
        return



    def PlotNumbers(self,Conf_level):
       
        self.gettestingtext().value += "Problem type: "+str(self.getprobtype().value)+"\n"
    
        mode = self.getprobtype().value

      
        if mode.find('One sample mean') > -1: 
           
            if not self.CheckInputComplete(mode):
                return

        
        Samp_size = self.getSAMPSIZEtxt().value
        Samp_mean = self.getSAMPMEANtxt().value
        
        if mode.find('Difference between two means') > -1:
            Samp_size = [int(Samp_size[:Samp_size.find(",")]),int(Samp_size[Samp_size.find(",")+1:])]
            Samp_mean = [float(Samp_mean[:Samp_mean.find(",")]),float(Samp_mean[Samp_mean.find(",")+1:])]  
        else:
            if mode.find('Paired sampled t-test') == -1:
                Samp_size = int(Samp_size)+self.getsmapchange()
                Samp_mean = float(Samp_mean)

        Pop_mean = None
        if mode.find('Paired sampled t-test') == -1:
                Pop_mean = float(self.getPOPMEANtxt().value)
        Pop_stdev = None

       
        if mode.find('One sample mean') > -1: 
            if self.getstdtype().value == "Population":
                if is_float(self.getmytxt().value):
                    Pop_stdev = float(self.getmytxt().value)
         
        if mode.find('Difference between two means') == -1:
            if mode.find('Paired sampled t-test') == -1:
                if Samp_size < 2:
                    return

        if mode.find('Paired sampled t-test') > -1:
           
            Samp_size = int(len(self.getprd_ttest_df()))
          
            list1 = [x for x in self.getprd_ttest_df()[self.getprtt_aft_feat()]]
        
            list2 = [x for x in self.getprd_ttest_df()[self.getprtt_bef_feat()]]
            diff = [list1[i] - list2[i] for i in range(len(list1))]
 
           
            Samp_mean = sum(diff)/len(diff)
            stdev = 0
            for i in range(len(list1)):
                stdev+=(diff[i]-Samp_mean)**2
            Samp_stdev= np.sqrt((stdev)/(len(diff)-1))
            Pop_mean = 0
            

        self.gettestingtext().value += "2>>> "+str(mode)+"\n"
        if mode.find('Paired sampled t-test') == -1:
            Samp_stdev = None 
    
        if mode.find('One sample mean') > -1: 
            if self.getstdtype().value == "Sample":
                if is_float(self.getmytxt().value):
                    Samp_stdev = float(self.getmytxt().value)
        if mode.find('Difference between two means') > -1:
            Samp_stdev = self.getmytxt().value
            Samp_stdev = [float(Samp_stdev[:Samp_stdev.find(",")]),float(Samp_stdev[Samp_stdev.find(",")+1:])]
           
       
         
        Conf_lvl = float(self.getconflvl().value)
        Two_sided = (self.gethyptype().value == "Two-tailed") 
        Alt_side = '' # only read in one-sided case: '>' or '<' -> H_1: \mu > x or \mu < x (x is claimed population parameter)
    
        if not Two_sided:
            if self.gethyptype().value == "One-tailed: Alternative >":
                Alt_side = ">"
            else:
                Alt_side = "<"
    
      
        testreturn = TestHypothesis2(Samp_size,Samp_mean,Samp_stdev,Pop_mean,Pop_stdev,Two_sided,Alt_side,Conf_lvl,self.getInvFigPage(),mode) 
        self.getresultexp().value = "P-value: "+str(round(testreturn[0],3))+"\n"
        self.getresultexp().value += "Conclusion: "+str(testreturn[1])+"\n"
        answer_obj = {
        "type": "custom",
        "answer":
            {
            'P-value': round(testreturn[0], 4),
            'Conclusion': str(testreturn[1]),
            'Samp_size': Samp_size,
            'Samp_mean': Samp_mean,
            'Samp_stdev': Samp_stdev,
            'Pop_mean': Pop_mean,
            'Pop_stdev': Pop_stdev,
            'Two_sided': Two_sided,
            'Alt_side': Alt_side,
            'Conf_lvl': Conf_lvl,
            'mode': mode
            }
        }
        self.visualManager.submit_answer(answer_obj)
        
        return


        

    def casechange(self,b):
        if self.getexmplst().value in cases:
            self.getcaseexp().value = cases[self.getexmplst().value]
        return

    def SelBefFeat(self,event):
        self.setprtt_bef_feat(self.getprfeatures().value)
    
        return
    
    def SelAftFeat(self,event):
        self.setprtt_aft_feat(self.getprfeatures().value)
    
        return

    def adjustssize(self,b):
    
        if not is_float(self.getSAMPSIZEtxt().value):
            return False
                                  
        return

    def OpenPRfile(self,event): 
    
        url = "https://github.com/muratfirat78/CPP_Datasets/raw/main/"+self.getfolderselect().value
    
        self.setprd_ttest_df(pd.read_csv(url,sep =',',quotechar="'"))
    
        self.getprfeatures().options = [c for c in self.getprd_ttest_df().columns]
    
        with self.getDFPage():
            clear_output()
            display(self.getprd_ttest_df().head(3)) 
     
        return

        
        
    def generateHTTab(self):

        ReadCases()

        self.setsmapchange(0)
        self.setprd_ttest_df(pd.DataFrame())

        hbox_layout = widgets.Layout(align_items='center')
        
        self.setmytxt(widgets.Text(description = 'StDev', value='',disabled=False,layout = widgets.Layout(width='150px')))
        self.setsampstdev(widgets.Text(description = '', value='',disabled=False,layout = widgets.Layout(width='150px')))

        
        self.setPOPMEANtxt(widgets.Text(description = 'P.Mean', value='',disabled=False,layout = widgets.Layout(width='150px')))
        self.setSAMPMEANtxt(widgets.Text(description = 'S.Mean', value='',disabled=False,layout = widgets.Layout(width='150px')))
        self.setSAMPSIZEtxt(widgets.Text(description = 'S.Size', value='',disabled=False,layout = widgets.Layout(width='150px')))
        self.setPOPgiven(widgets.Dropdown(options=['Given','Not given'], description='Population stdev:'))
        
        self.settestingtext(widgets.Textarea(value='', placeholder=' ',description='',disabled=True,layout = widgets.Layout(width='99%',height='65px')))
        self.setresultexp(widgets.Textarea(value='', placeholder=' ',description='Conclusion:',disabled=False,layout = widgets.Layout(width='90%',height='130px')))
        
        self.setalternative(widgets.Dropdown(options=['<','>'], description='Alternative:'))
        self.getalternative().layout.visibility = 'hidden'
        
    
        
        self.setexmplst(widgets.Dropdown(options=[v for v in cases.keys()], description='Questions'))
        self.setcaseexp(widgets.Textarea(value='', placeholder='example ',description='Text:',disabled=True,layout = widgets.Layout(width='65%',height='130px')))
        
        if self.getexmplst().value in cases:
            self.getcaseexp().value = cases[self.getexmplst().value]
        self.getexmplst().observe(self.casechange)
        
        self.setprobtype(widgets.Dropdown(options=["One sample mean","Proportion","Difference between two means","Paired sampled t-test"], description='Problem'))
        self.setstdtype(widgets.Dropdown(options=["Population","Sample"], description='Type',layout = widgets.Layout(width='125%')))
        self.sethyptype(widgets.Dropdown(options=["Two-tailed","One-tailed: Alternative <","One-tailed: Alternative >"], description='Test Type'))
        
        
        self.getprobtype().observe(self.ApplyProblem)
        
        self.setmybutton2(widgets.Button(description='Solve', disabled=False,layout = widgets.Layout(align_items='flex-end',width = '150px')))
        
        figpg_layout = widgets.Layout(width='85%',height='45%')
        self.setInvFigPage(widgets.Output(layout=figpg_layout))
        
        self.getmybutton2().on_click(self.PlotNumbers)
        
        self.setmybutton3(widgets.Button(description='Save', disabled=False,layout = widgets.Layout(align_items='flex-end',width = '150px')))
        
        
        f =interactive(self.PlotNumbers, Conf_level = widgets.FloatSlider(min=0.01,max=0.1,step=0.01,value=0.05));
        self.setitems([c for c in f.children])
        
        f2 =interactive(self.Sample_Change, Size_delta = widgets.IntSlider(min=-25,max=25,step=5,value=0));
        self.setitems2([c for c in f2.children])
        
        pairedlinks = ['Hypothermia.csv',
                     'Diet_R.csv',
                    'heart_rate_data.csv',
                      'diet.csv',]
        
        self.setfolderselect(widgets.Dropdown(options=[x for x in pairedlinks],description = 'Datasets: '))
        
        self.setlinelabel(widgets.Label(value='_______________________________'))
        self.getlinelabel().layout.display= 'none'
        
        self.setreadpfile(widgets.Button(description="Open"))
        self.getreadpfile().layout.display= 'none'
        self.getreadpfile().on_click(self.OpenPRfile)
        
        self.setprfeatures(widgets.Select(options=[],description = 'Features'))
        self.getprfeatures().layout.display= 'none'
      
        self.setaddpr(widgets.Button(description= " Assign Before "))
        self.getaddpr().layout.display= 'none'
        self.setadd2pr(widgets.Button(description=" Assign After  "))
        self.getadd2pr().layout.display= 'none'
        
        self.getaddpr().on_click(self.SelBefFeat)
        self.getadd2pr().on_click(self.SelAftFeat)
        
        self.getfolderselect().layout.display= 'none'
        self.getSAMPSIZEtxt().observe(self.adjustssize)
        
        self.setDFPage(widgets.Output())
        self.getDFPage().layout.display = 'none'
        
        
        
        self.setconflvl(self.getitems()[0])
        
        tablayout = widgets.Layout(align_items='center',width= '100%',height='1050px')
        
        
        
        tab_1 = VBox(children=[
                         HBox(children = [VBox(children=[self.getprobtype(),HBox(children = [self.getPOPMEANtxt(),self.getSAMPMEANtxt()]),self.getSAMPSIZEtxt(),HBox(children = [self.getmytxt(),self.getstdtype()]),
                                                         self.gethyptype()
                                          ,VBox(children=self.getitems2()),VBox(children=self.getitems())])
                                          ,VBox(children=[HBox(children = [self.getfolderselect()]),
                                                                  HBox(children = [self.getreadpfile(),self.getprfeatures(),VBox(children = [self.getaddpr(),self.getadd2pr()])])
                                                                  ,self.getDFPage()])],layout=Layout(width='95%'))
                        ,self.getmybutton2(),self.gettestingtext(),VBox(children=[self.getInvFigPage()]),self.getresultexp(),self.getmybutton3()],layout=tablayout)

          
        return tab_1

    def ResetSampleSet(self):
    
        self.getsmpmeantxt().value = ''
        self.getsmpstdevtxt().value = ''
        self.getsmpsetsizetxt().value = ''
        self.getsmpsetmeantxt().value = ''
        self.getsmpsetstdevtxt().value = ''
        
        with self.getSampleSets():
            clear_output()
       
        self.getSampleSet().clear()

    
        return 


    def typechangs(self,*args):
        
        if self.getpoptypes().value == 'Exponential':
            self.getpopstdevtxt().value = ''
            self.getpopstdevtxt().disabled = True
        else:
            self.getpopstdevtxt().disabled = False
            
        self.getpopempmeantxt().value = ''
        self.getpopempstdevtxt().value = ''
        self.ResetSampleSet()
          
        with self.getPopPage():
            clear_output()
        
        return
        
        
    def CheckAllInput(self):
 
        if self.getpopsizetxt().value == '':
            return False
        else:
            if not is_float(self.getpopsizetxt().value):
                return False
        
        if self.getpopmeantxt().value == '':
            return False
        else:
            if not is_float(self.getpopmeantxt().value):
                return False
            
        if self.getpoptypes().value != 'Exponential':
            if self.getpopstdevtxt().value == '':
                return False
            else:
                if not is_float(self.getpopstdevtxt().value):
                    return False
        
        return True

    def Draw(self):
  
        if self.getPopulation() is None:
            return

        self.getsampleprogress().value+="Population will be drawn... "+str(len(self.getPopulation()))+"\n"
        
        all_df = None
        
        with self.getPopPage():
            
            clear_output()
            
            popmean = sum(self.getPopulation())/len(self.getPopulation())
            popstdev = math.sqrt(sum([(x-popmean)**2 for x in self.getPopulation()])/len(self.getPopulation()))
            
            poptype = self.getpoptypes().value 
            ystart = 2
            yincrement = 0.25
            
            #if poptype == 'Exponential':
                
    
            width = 10
            height = 4
            sns.set(rc = {'figure.figsize':(width,height)})
            pop_df = pd.DataFrame({'Value': self.getPopulation()[:]})
            sns.displot(x='Value',data = pop_df, kind="hist", stat="percent", kde=True)
            plt.xlim(0.9*min(self.getPopulation()),1.1*max(self.getPopulation()))
            plt.title("Empirical  Population ("+str(self.getpoptypes().value)+")")
            plt.text(min(self.getPopulation())+0.1, ystart, 'n= '+str(len(pop_df)), dict(size=10))
            plt.text(min(self.getPopulation())+0.1, ystart-yincrement, 'Mean= '+str(round(popmean,2)), dict(size=10))
            plt.text(min(self.getPopulation())+0.1, ystart-2*yincrement, 'Stdev= '+str(round(popstdev,2)), dict(size=10))
            plt.show()
        
        return 

    def on_submit_func(self,sender):

        self.getsampleprogress().value+="Input ok: "+str(self.CheckAllInput())+"\n"
    
        if self.CheckAllInput():
        
            popindex =  0
            
            for popty in range(len(self.getpoptypes().options)):
                if self.getpoptypes().options[popty] == self.getpoptypes().value:
                    popindex = popty
                    break
            
            
            if self.getpoptypes().value == 'Normal':
                self.setPopulation(norm.rvs(size=int(self.getpopsizetxt().value), loc = int(self.getpopmeantxt().value), scale=int(self.getpopstdevtxt().value)))
                self.getsampleprogress().value+="Normal Population set.. size "+str(len(self.getPopulation()))+"\n"
                
            if self.getpoptypes().value == 'Uniform':
                b = math.sqrt(3)*int(self.getpopstdevtxt().value)+int(self.getpopmeantxt().value)
                a = int(self.getpopmeantxt().value)-math.sqrt(3)*int(self.getpopstdevtxt().value)
                self.setPopulation(uniform.rvs(size=int(self.getpopsizetxt().value), loc = a, scale=b-a))
            if self.getpoptypes().value == 'Exponential':
                self.setPopulation(expon.rvs(scale=int(self.getpopmeantxt().value),size=int(self.getpopsizetxt().value)))
                    
            emp_mean  =sum(self.getPopulation())/len(self.getPopulation())
            emp_stdev = math.sqrt(sum([(x-emp_mean)**2 for x in self.getPopulation()])/len(self.getPopulation()))
            
            self.getpopempmeantxt().value = str(round(emp_mean,4))
            self.getpopempstdevtxt().value = str(round(emp_stdev,4))
        
        else:
            print('Check is false')

        self.getsampleprogress().value+=" Calling draw function... "+"\n"
        self.Draw()   
    
        return

    def ResetSamples(self,Change):
    
        self.ResetSampleSet()
        
        return 

    def plot1changed(self,b):
        if self.getchk1().value:
            self.getchk2().value = False
    
        return

    
    def plot2changed(self,b):
        if self.getchk2().value:
            self.getchk1().value = False
    
        return


    def smpsizesubmit(self,sender):
          
        if self.getsmpsizetxt().value == '':
            return
        
        if not is_float(self.getsmpsizetxt().value):
            return 
        
        if self.getPopulation() is None:
            return
        
        self.setSample(SamplePopulation(self.getPopulation(),int(self.getsmpsizetxt().value)))
        
        
        smp_mean = sum(self.getSample())/len(self.getSample())
        self.getsmpmeantxt().value = str(round(smp_mean,3))
        
        smp_stdev = sum([(x-smp_mean)**2 for x in self.getSample()])/len(self.getSample())
        self.getsmpstdevtxt().value = str(round(smp_stdev,3))
        
        self.getSampleSet().append(self.getSample())
        
        self.getsmpsetsizetxt().value = str(len(self.getSampleSet()))
        
        ssetmeans = [sum(s)/len(s) for s in self.getSampleSet()]
        overallmean = sum(ssetmeans)/len(ssetmeans)
        self.getsmpsetmeantxt().value = str(overallmean)
        self.getsmpsetstdevtxt().value = str(math.sqrt(sum([(x-overallmean)**2 for x in ssetmeans])/len(ssetmeans)))
        
        if self.getchk2().value: 
     
            with self.getSampleSets():
                clear_output()
                width = 8
                height = 8
                sns.set(rc = {'figure.figsize':(width,height)})
                sns.distplot(ssetmeans,kde=True,hist=True)
                plt.title("Sample Set: n = "+str(len(self.getSampleSet()))+', size '+str(self.getsmpsizetxt().value))
                plt.show()
    
        if self.getchk1().value: 
            
             with self.getSampleSets():
                clear_output()
                width = 8
                height = 8
                sns.set(rc = {'figure.figsize':(width,height)})
                smp_df = pd.DataFrame({'Mean': ssetmeans[:],'ID':[s for s in range(len(self.getSampleSet()))],'Size':[len(s) for s in self.getSampleSet()]})
                sns.relplot(x='ID', y='Mean',hue='Size',data=smp_df,alpha=.5, palette="muted", height=9)       
                plt.title('Means vs Sample Size')
                plt.show()
           
        return



        
    def generateSamplingTab(self):

        self.setSampleSet([])
        self.setSample([])
        # Normal, Uniform, Exponential
        drplyout = widgets.Layout(width= '180px')
        txtlyout = widgets.Layout(width= '150px')
        txtmlyout = widgets.Layout(width= '180px')
        lbllyout = widgets.Layout(width= '195px')
        
        self.setpoplbl(widgets.Label(description = 'Population', value='Population Parameters',disabled=False,layout = lbllyout))
        self.setpoplbl2(widgets.Label(description = 'Population', value='',disabled=False,layout = lbllyout))
        self.setpopemplbl(widgets.Label(description = '', value='Emperical Distribution',disabled=False,layout = lbllyout))
        self.setpoptypes(widgets.Dropdown(options=['Normal','Uniform','Exponential'], description='Pop.Type:',layout = drplyout))
        self.setpopsizetxt(widgets.Text(description = 'Size', value='',disabled=False,layout = txtlyout))
        self.setpopmeantxt(widgets.Text(description = 'Mean', value='',disabled=False,layout =txtmlyout))
        self.setpopstdevtxt(widgets.Text(description = 'StDev', value='',disabled=False,layout = txtlyout))
        self.setpopempmeantxt(widgets.Text(description = 'Mean', value='',disabled=True,layout =txtmlyout))
        self.setpopempstdevtxt(widgets.Text(description = 'StDev', value='',disabled=True,layout = txtlyout))
        
        self.getpoptypes().observe(self.typechangs,'value')
        
        
        if self.getpoptypes().value == 'Exponential':
            self.getpopstdevtxt().value = ''
            self.getpopstdevtxt().disabled = True
        else:
            self.getpopstdevtxt().disabled = False
        
        
        self.setsmplay(widgets.Layout(width= '130px',align_items='flex-start'))
        lsbllyout = widgets.Layout(width= '60px')
        self.setsmplbl(widgets.Label(description = '', value='Sample',disabled=False,layout = lsbllyout))
        self.setsmpsizetxt(widgets.Text(description = 'Size', value='',disabled=False,layout = self.getsmplay()))
        
        self.getpopstdevtxt().on_submit(self.on_submit_func)
        self.getpopmeantxt().on_submit(self.on_submit_func)
        self.getsmpsizetxt().on_submit(self.smpsizesubmit)
        
        
        self.setsmpmeantxt(widgets.Text(description = 'Mean', value='',disabled=True,layout =txtmlyout))
        self.setsmpstdevtxt(widgets.Text(description = 'StDev', value='',disabled=True,layout = txtlyout))
        
        
        gnbllyout = widgets.Layout(width= '60px')
        self.setgnrlbl(widgets.Label(description = '', value='Samp.Set: ',disabled=False,layout = gnbllyout))
        smpsetlay = widgets.Layout(width= '130px')
        self.setsmpsetsizetxt(widgets.Text(description = 'Size:', value='',disabled=True,layout =smpsetlay))
        
        self.setsmpsetmeantxt(widgets.Text(description = 'Mean', value='',disabled=True,layout =txtmlyout))
        self.setsmpsetstdevtxt(widgets.Text(description = 'StDev', value='',disabled=True,layout = txtlyout))
        
        self.setresbutton(widgets.Button(description='Reset', disabled=False,layout = widgets.Layout(align_items='flex-end',width = '150px')))
        
        self.getresbutton().on_click(self.ResetSamples)
        
        
        self.setchk1(widgets.Checkbox(False, description='Means_vs_size'))
        self.setchk2(widgets.Checkbox(True, description='Dist_of_means'))
        
        self.getchk1().observe(self.plot1changed)
        self.getchk2().observe(self.plot2changed)
        
        inplay = widgets.Layout(width= '99%')
        hlyout = widgets.Layout(width= '99%')
        
        
        poppg = widgets.Layout(width='99%')
        self.setPopPage(widgets.Output(layout=poppg))
        
        avgpg = widgets.Layout(width='99%')
        self.setAvgProg(widgets.Output(layout=avgpg))
        
        smppg = widgets.Layout(width='99%')
        self.setSampleSets(widgets.Output(layout=smppg))


        self.setsampleprogress(widgets.Textarea(value='', placeholder=' ',description='',disabled=True,layout = widgets.Layout(width='99%',height='65px')))
        
        tab_2 =   VBox(children = [  HBox(children = [self.getpoplbl(),self.getpoptypes(),self.getpopsizetxt(),self.getpopmeantxt(),self.getpopstdevtxt()]),
                                     
                                                      HBox(children = [self.getsmplbl(),self.getsmpsizetxt(),self.getsmpmeantxt(),self.getsmpstdevtxt()]),
                                                      HBox(children = [self.getgnrlbl(),self.getsmpsetsizetxt(),self.getsmpsetmeantxt(),self.getsmpsetstdevtxt()]),
                                                     HBox(children = [self.getchk1(),self.getchk2(),self.getresbutton()]),
                                                   
                                                      HBox(children = [self.getPopPage(),self.getSampleSets()],layout = hlyout ),
                                   self.getsampleprogress()
                                                     
                                                   ],layout = inplay)
        


        return tab_2


    def SelCatFeat(self,event):    
        self.setanova_cat_feat(self.getfeatures().value)
    
        return

    def SelValFeat(self,event):  
        self.setanova_value_feat(self.getfeatures().value)
    
        return
        
    def SolveANOVA(self,event):

        fncreturn = ANOVA2(self.getanova_df(),self.getanova_cat_feat(),self.getanova_value_feat(),self.getresultout())
        
        with self.getboxout():
            clear_output()
            self.getanova_df().boxplot(self.getanova_value_feat(), by=self.getanova_cat_feat(), figsize=(12, 8))
     
    
        return
    
    def Openfile(self,event): 
    
      
        url = datalinks[self.getsource().value]
    
        self.setanova_df(pd.read_csv(url,sep =',',quotechar="'"))
    
        self.getfeatures().options = [c for c in self.getanova_df().columns]
    
        with self.getdataout():
            clear_output()
            display(self.getanova_df().info()) 
            display(self.getanova_df().head(5)) 


        with self.getboxout():
            clear_output()

        with self.getresultout():
            clear_output()
     
        return


    def generateANTAB(self):

    
        self.setsource(widgets.Dropdown(options = [x for x in datalinks.keys()],description = 'Source file'))
        
        self.setfeatures(widgets.Select(options=[],description = 'Features'))
        self.setanova_df(pd.DataFrame())

        
        self.setreadfile(widgets.Button(description="Open")) 
        self.setadd(widgets.Button(description= ">> Cat. Feat.   >>")) 
        self.setadd2(widgets.Button(description=">> Value Feat.  >>"))
        self.setsolveanova(widgets.Button(description="Solve ANOVA"))
        outlay = widgets.Layout(width="99%")
        self.getadd().on_click(self.SelCatFeat)
        self.getadd2().on_click(self.SelValFeat)
        self.getsolveanova().on_click(self.SolveANOVA)
        
        self.setdataout(widgets.Output(layout=outlay))
        self.setboxout(widgets.Output(layout=outlay))
        self.setresultout(widgets.Output(layout=outlay))
        self.getreadfile().on_click(self.Openfile)
        
        tab_3 = VBox(children = [HBox(children = [self.getsource(),self.getreadfile()]),HBox(children = [self.getfeatures(),VBox(children = [self.getadd(),self.getadd2(),self.getsolveanova()])]),HBox(children = [self.getdataout(),self.getboxout()]),self.getresultout()])
    

        return tab_3

    
#############################################################################################################################################  







#############################################################################################################################################   




 