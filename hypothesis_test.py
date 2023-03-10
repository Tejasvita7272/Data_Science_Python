# -*- coding: utf-8 -*-
"""Hypothesis_Test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10t6u1o1o32mohNl6c7ruawZNiaBUn4Mf
"""

#import the libraries
import pandas as pd
import scipy 
import numpy as np
from scipy import stats

"""# Super Market Example"""

stats.t.cdf(2.23,df=79)

# Call center example
#1-stats.t.cdf(1.4,49)
#stats.t.cdf(-1.4,49)
2*stats.t.cdf(-1.4,49)

"""# Call Center Example"""

import numpy as np
from scipy import stats

t=(4.6-4)/(3/np.sqrt(50)) # t value for x bar=4.6, mu=4, s=3, n=50
t

p=2*stats.norm.cdf(t)
p

"""# One Tail Test"""

import pandas as pd
from scipy import stats

data=pd.Series([0.593, 0.142, 0.329, 0.691, 0.231, 0.793, 0.519, 0.392, 0.418])

data

p=stats.ttest_1samp(data,0.3)[1] # index of p-value is 1, so [1] is given
# pvalue=0.05853032968489765 here, p = p1+p2
p

stats.ttest_1samp(data,0.3) # this command always gives you 2 tail p-value
# t-value=2.2050588385131595 and pvalue=0.05853032968489765 here, p = p1+p2
# index of t-value is 0 and p-value is 1

#As this is a one tail test p value so divide by 2 to get final p-value
p_value= p/2
p_value
# Null Hypo. is Mu<=0.3, Alter. Hypo. is Mu>0.3, 
# Alfa = 0.05, P-value we got is 0.029 So p<alfa. So reject Null Hypo.
# So go for Alt. Hypo.
# interpret it: As mean value Mu >0.3 factory is causing problem.

"""# Two Tail Test"""

Control=pd.Series([91, 87, 99, 77, 88, 91])
Treat =pd.Series([101, 110, 103, 93, 99, 104])

stats.ttest_ind( Control,Treat) # two tail independent
# p=p1+p2. We are conducting 2 sample 2 tail test, so no need to divide p by 2.
# p=0.006, alfa=0.05, p<alfa so reject null hypo. so accept alt. Hypo
# interpretation: 2 responses are not equal so drug is working.

"""# 2 Proportion Test"""

import numpy as np
#Data:

n1 = 247
p1 = .37 # proportion is 0.37

n2 = 308
p2 = .39 # proportion is 0.39

population1 = np.random.binomial(1,  p1, n1) # 1 - placed i.e. probability of success, 0-not placed
population2 = np.random.binomial(1, p2, n2) # as its a random function every time you execute, you will get diff ans.

population1 # 247 student's data. 0-not placed, 1-placed

population1.mean()

population2

import statsmodels.api as sm
sm.stats.ttest_ind(population1, population2)# middle is the p-value
# p>0.05 so accept null hypo.
# interpretation: students are amost equally got placed in 2 states. 
# i.e. no significant difference in providing placement opportunities to students in 2 states.

import statsmodels.api as sm

p=0.05

population1 = np.random.binomial(1, p1, n1)
population2 = np.random.binomial(1, p2, n2)

x=sm.stats.ttest_ind(population1, population2)[1]
print(x)
print(round(x,3))
if x>p:
  print(f'Accept null hypothesis\n--------------------------')
else:
  print(f'Failed to reject the null hypothesis\n-------------------')

