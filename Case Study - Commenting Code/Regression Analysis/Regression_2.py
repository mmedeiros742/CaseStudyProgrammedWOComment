
import pandas as pd
from pandas import ExcelFile
from pandas import ExcelWriter

import numpy as np
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from numpy import var
from numpy import std
from numpy import median

import scipy.stats as sc
import matplotlib.pyplot as plot

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# import dataset as pandas dataframe
df = pd.read_excel('/Users/mmedeiros/Dropbox/JuniorYear/Spring/CIS362/HW/HW3/casestudy.xlsx', sheet_name='Sheet1')


# print correlation matrix
print(df.corr())
# highest correlations are between
# AoA vs SDT (0.75334) and
#Supplied or from scratch? vs Optional?
# AoA vs CL (-0.504868)
#Supplied or from scratch? vs Optional?

# check for null values and fill with column mean
print(
'\nSupplied or from scratch? null?: ', df['Supplied or from scratch?'].isnull().values.any(), #false
'\nOptional? null?: ', df['Optional?'].isnull().values.any(), #true
'\nSupplied or from scratch? null?: ', df['Supplied or from scratch?'].isnull().values.any(), #false
'\nOptional? null?: ', df['Optional?'].isnull().values.any() #false
)

df['Optional?'] = df['Optional?'].fillna(df['Optional?'].mean())
print('\nNaN filled',
	  '\nOptional? still null?: ',
	  df['Optional?'].isnull().values.any()) #true

# assign independent and dependent variables
x = df['Optional?']
y = df['Supplied or from scratch?']

x2 = df['Optional?']
y2 = df['Supplied or from scratch?']


# use linregress to perform regressions and gather
# slope (m), intercept(b), R value, P value and standard error
# create array of slope and intercept for us in polyval in plots
slope1, intercept1, rvalue1, pvalue1, stderr1 = sc.linregress(x, y)
fit1 = [slope1, intercept1]

slope2, intercept2, rvalue2, pvalue2, stderr2 = sc.linregress(x2, y2)
fit2 = [slope2, intercept2]


# print regression results and best fit model for each regression
print('\nFit 1 (Supplied or from scratch? vs Optional?)',
	  '\nslope:\t\t\t', slope1,
	  '\ny-intercept:\t', intercept1,
	  '\nR value:\t\t', rvalue1,
	  '\nR-squared:\t\t', pow(rvalue1, 2),
	  '\nP value:\t\t', pvalue1,
	  '\nstd err:\t\t', stderr1,
	  '\nRegress. Model:  Supplied or from scratch? = ', intercept1, ' + ', slope1, ' * Optional?',
	  '\n')

print('\nFit 2 (Supplied or from scratch? vs Optional?)',
	  '\nslope:\t\t\t', slope2,
	  '\ny-intercept:\t', intercept2,
	  '\nR value:\t\t', rvalue2,
	  '\nR-squared:\t\t', pow(rvalue2, 2),
	  '\nP value:\t\t', pvalue2,
	  '\nstd err:\t\t', stderr2,
	  '\nRegress. Model:  Supplied or from scratch? = ', intercept2, ' + ', slope2, ' * Optional?',
	  '\n')

# plot given values and regression prediction line
plot.plot(x, y, 'x')
plot.plot(x, np.polyval(fit1, x), 'r-')
plot.xlabel('Optional?')
plot.ylabel('Supplied or from scratch?')
plot.title('Simple Linear Regression (Supplied or from scratch? vs Optional?)')
plot.show()

plot.plot(x2, y2, 'x')
plot.plot(x2, np.polyval(fit2, x2), 'r-')
plot.xlabel('Length in Meters (Optional?)')
plot.ylabel('Angle in Degrees(Supplied or from scratch?)')
plot.title('Simple Linear Regression (Supplied or from scratch? vs Optional?)')
plot.show()

ticks = df.columns


corr_matrix = pd.plotting.scatter_matrix(df)
for subaxis in corr_matrix:
    for ax in subaxis:
        ax.xaxis.set_ticks([])
        ax.yaxis.set_ticks([])
        ax.set_ylabel("")
        ax.set_xlabel("")

pd.plotting.xticks([], ticks)
plot.show()


