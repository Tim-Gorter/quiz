import pandas as pd
import seaborn as sns
import numpy as np
import random
import scipy.stats as st
import math
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, expon, gamma
import pandas as pd
from scipy import stats
import os
from pathlib import Path
from IPython.display import clear_output

def is_float(value):
    try:
        float(value) 
        return True
    except ValueError:
        return False


cases = dict()

datalinks = { "Plant growth": 'https://vincentarelbundock.github.io/Rdatasets/csv/datasets/PlantGrowth.csv',
             "Stress scores":'https://statsguru.bham.ac.uk/downloads/between-group-anova/between-group-anova-data.csv',
             "Responses dataset 1": 'https://researchguides.library.vanderbilt.edu/ld.php?content_id=19195047',
             "Responses dataset 2": 'https://researchguides.library.vanderbilt.edu/ld.php?content_id=19195103',
             "Diet dataset": 'https://github.com/muratfirat78/CPP_Datasets/raw/main/diet.csv'
             } 
'''
datalinks = ['https://vincentarelbundock.github.io/Rdatasets/csv/datasets/PlantGrowth.csv'
             ,'https://statsguru.bham.ac.uk/downloads/between-group-anova/between-group-anova-data.csv',
            'https://researchguides.library.vanderbilt.edu/ld.php?content_id=19195047',
             'https://researchguides.library.vanderbilt.edu/ld.php?content_id=19195103',
            'https://researchguides.library.vanderbilt.edu/content/enforced/474750-2024S.1.BSCI.1511L.01/p-qrs-anova-example%202.0.csv',
             'https://github.com/muratfirat78/CPP_Datasets/raw/main/diet.csv']
'''

def ReadCases():    
    try:
        url = "https://github.com/muratfirat78/CPP_Datasets/raw/main/Hypothesis_Cases.csv" 
        cases_df = pd.read_csv(url, sep=',')   
    except: 
        print('No case file found')
            
    
    for i,r in cases_df.iterrows():
        cases[r["Name"]] = r["Description"]
    
    return 


def SamplePopulation(Population,Sample_size):
    
    
    CurrSample = []

    curr_avg = 0
    for i in range(Sample_size):
        element=np.random.randint(len(Population))
        CurrSample.append(Population[element])
        np.delete(Population,element)
    
    for itm in CurrSample:
        np.append(Population,itm)
        
    return CurrSample
    

def TestHypothesis2(sample_size,sample_mean,sample_stdev,pop_mean,pop_stdev,twosided,alt_side,conflevel,wout,mode):
    # pop_stdev is None is population stdev is not specified.
    # sample_stdev is None is sampling stdev is not specified.
    # alt_side is checked only if twosided is False and can be either '<' or '>'

    
    with wout:
        
        clear_output(wait = True)
        ztest = False
        test_stat = 0
        p_val = 0
        conclusion = ''
        H_null = 'H0 : \mu '
        H_alt = 'H1 : \mu '
        
        ayz = None


        typestr = 'Two-sided'
        if not twosided:
            typestr = 'One-sided'
            if alt_side == '>':
                H_null += ' =< '+str(pop_mean)
                H_alt += '> '+str(pop_mean)
            else:
                H_null += ' >= '+str(pop_mean)
                H_alt += '< '+str(pop_mean)

        else:
            H_null += '= '+str(pop_mean)
            H_alt += '!= '+str(pop_mean)

        teststatstr = 'z-score'
        dof = 1

     
        if mode == 'One sample mean':
            
            if pop_stdev is None:
                    # use t-score with sample stdev 
                test_stat = (sample_mean-pop_mean)/(sample_stdev/np.sqrt(sample_size))
                teststatstr = 't-score'
            else:
                if sample_size >= 30:
                    # use z-score
                    test_stat = (sample_mean-pop_mean)/(pop_stdev/np.sqrt(sample_size))
                    ztest = True 
                else:
                    # use t-score with pop_stdev
                    test_stat = (sample_mean-pop_mean)/(pop_stdev/np.sqrt(sample_size))
                    teststatstr = 't-score'
        if mode.find('Proportion') > -1:
            Stdev = math.sqrt((pop_mean*(1-pop_mean))/sample_size) # is None is sampling stdev is not specified.
            
            test_stat = ((sample_mean)-pop_mean)/Stdev

            ztest = True
  
        if mode.find('Difference between two means') > -1:
            std_error1 = sample_stdev[0]/np.sqrt(sample_size[0])
            std_error2 = sample_stdev[1]/np.sqrt(sample_size[1])
            meas_var = np.sqrt(std_error1**2+std_error2**2)
            sample_mean = sample_mean[0] - sample_mean[1]
            test_stat = (sample_mean-pop_mean)/meas_var
            ztest = True
            teststatstr = 't-score'

        if mode.find('Paired sampled t-test') > -1:
            pop_mean = 0
            test_stat = (sample_mean-pop_mean)/(sample_stdev/np.sqrt(sample_size))
            teststatstr = 't-score'
            ztest = False

    
       
        if mode.find('Difference between two means') == -1:     
            dof = sample_size-1 
        else:
            dof = (sample_size[0]-1)+(sample_size[1]-1)
       

        if ztest: 
            cum_area = st.norm.cdf(test_stat) 
        else:
           # p_val = st.t.sf(np.abs(test_stat), dof)
            cum_area = st.t.cdf(test_stat, df = dof)

        if twosided: 
            if sample_mean > pop_mean:
                p_val = 2*(1-cum_area)
            else:
                p_val = 2*cum_area
        else:
            if alt_side == '>':
                p_val = 1- cum_area 
            else:
                p_val =  cum_area 
                
      

        if p_val < conflevel:
            conclusion = 'Reject H0!'
        else:
            conclusion = 'Fail to reject H0!'
            
        

        axs = np.arange(min(-5,p_val-0.25),max(5,p_val+0.25), 0.1) # x from -6 to 6 in steps of 0.1 
        
        width = 6
        height = 6
        sns.set(rc = {'figure.figsize':(width,height)})
      
        plt.xlim(0,0.45)
       
     
        plt.text(min(-5,p_val-0.25)+0.1, 0.34, 'test statistic:', dict(size=10))
        plt.text(min(-5,p_val-0.25)+0.1, 0.32, str(round(test_stat,2)), dict(size=10))
        if twosided:
            plt.text(min(-5,p_val-0.25)+0.1, 0.39, 'Rejection boundaries:', dict(size=10))
        else:
            plt.text(min(-5,p_val-0.25)+0.1, 0.39, 'Rejection region:', dict(size=10))
        plt.xlim(min(-5,p_val-0.25),max(5,p_val+0.25))
        plt.xlabel('Test statistic', fontsize=10, color='black')
        plt.ylabel('PDF value', fontsize=10, color='black')
        plt.title("Hypothesis testing: "+teststatstr)
        
        if ztest:
            # Mean = 0, SD = 1.
            ayz =norm.pdf(axs,0,1)
            plt.plot(axs, ayz,'k')
        else:
            ayz = st.t.pdf(axs,dof)
            plt.plot(axs,ayz, 'r')

        rejreg_left = '- inf'
        rejreg_right = 'inf'

        tcase= ''
        if twosided:

            if ztest: 
                rejreg_left = norm.ppf(abs(0.5*conflevel),loc=0,scale=1)
                rejreg_right = norm.ppf(1-abs(0.5*conflevel),loc=0,scale=1)
 
            else:
                rejreg_left = st.t.ppf(0.5*conflevel,dof)
                rejreg_right = st.t.ppf(1-0.5*conflevel,dof)

            plt.fill_between(axs,ayz,where = (axs<=-abs(rejreg_left)) | (axs>=abs(rejreg_right)))
           
            plt.axvline(x=-test_stat,ymin=0,color='b', label='confidence level',linewidth=1)
            plt.axvline(x=test_stat, color='b', label='confidence level',linewidth=1)
        else:
            if alt_side == '>': # one-side: right tail
                if ztest: 
                    rejreg_left = norm.ppf(1-abs(conflevel),loc=0,scale=1)
                else:
                    rejreg_left = st.t.ppf(1-abs(conflevel),dof)

          
             
                plt.axvline(x=test_stat,ymin=0, color='b', label='confidence level',linewidth=1)   
                plt.fill_between(axs,ayz,where = (axs>=abs(rejreg_left)) )


            else: # one-sided: left tail
                if ztest: 
                    rejreg_right = norm.ppf(abs(conflevel),loc=0,scale=1)
                else:
                    rejreg_right = st.t.ppf(abs(conflevel),dof)

                plt.axvline(x= test_stat,ymin=0, color='b', label='confidence level',linewidth=1)
                plt.fill_between(axs,ayz,where = (axs<=-abs(rejreg_right)) )
                  
        if rejreg_left != '- inf':
            rejreg_left = round(rejreg_left,3)
                   
        if rejreg_right != 'inf':
            rejreg_right = round(rejreg_right,3)
            
        
        
        plt.text(-0.45, 0.32, 'n='+str(sample_size), dict(size=10))
        plt.text(2.5, 0.39, 'Conf. level= '+str(round(conflevel,2)), dict(size=10))
        plt.text(2.5, 0.36, 'P_val = '+str(round(p_val,4)), dict(size=10))
    
        
        if twosided:
            plt.text(min(-5,p_val-0.1)+0.1, 0.37,''+str(rejreg_left)+','+str(rejreg_right)+'', dict(size=10))
        else:
            plt.text(min(-5,p_val-0.1)+0.1, 0.37,'['+str(rejreg_left)+','+str(rejreg_right)+']', dict(size=10))
        plt.show()

    return p_val,conclusion

def ANOVA2(dataframe,groupfeature,valuefeature,resout):

    with resout:
        
        clear_output(wait = True)
    
        print('-------------- ANOVA Testing ---------------')
        print('Data size: ',len(dataframe),', groups feature: ',groupfeature,', feature of values: ',valuefeature)
        N = len(dataframe) ; k = len(pd.unique(dataframe[groupfeature])); n = dataframe.groupby(groupfeature).size()[0] 
        DFbetween = k - 1; DFwithin = N - k; DFtotal = N - 1
        
        df_agg = dataframe.groupby([groupfeature], dropna=True)[valuefeature].agg(lambda x:list(x)).reset_index()
        
        groupsizes = [len(x) for x in df_agg[valuefeature]]
    
        grps = pd.unique(dataframe[groupfeature])
        print('Number of groups: ',k,', all values: ',N,', group sizes: ',groupsizes)
        d_data = {grp:dataframe[valuefeature][dataframe[groupfeature] == grp] for grp in grps}
        
        print('_________________________________')
    
        SSbetween = (sum(dataframe.groupby(groupfeature).sum()[valuefeature]**2)/n) - (dataframe[valuefeature].sum()**2)/N
        sum_y_squared = sum([value**2 for value in dataframe[valuefeature].values])
        SSwithin = sum_y_squared - sum(dataframe.groupby(groupfeature).sum()[valuefeature]**2)/n
        SStotal = SSbetween+SSwithin 
    
    
        MSbetween = SSbetween/DFbetween; MSwithin = SSwithin/DFwithin
        F_man = MSbetween/MSwithin; p_man = stats.f.sf(F_man, DFbetween, DFwithin)
        eta_sqrd = SSbetween/SStotal; om_sqrd = (SSbetween - (DFbetween * MSwithin))/(SStotal + MSwithin)

        my_list = [myset for myset in d_data.values()]
        
    
        F, p = stats.f_oneway(*my_list)
        #print("Manually computation, F-statistic: ",round(F_man,2),", P-value",round(p_man,2))
        print("SciPy, F-Statistic: ",round(F,2),", P-value",round(p,2))
        
        dataframe.boxplot(valuefeature, by=groupfeature, figsize=(8, 5))
        plt.show()
  
        
    return F_man,p_man

