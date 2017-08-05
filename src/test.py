#invite people for the Kaggle party
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
#warnings.filterwarnings('ignore')
#%matplotlib inline

print('Columns of the data')
df_train = pd.read_csv('../input/train.csv')
print(df_train.columns)

#print('SalePrice description')
#print(df_train['SalePrice'].describe())

#print('Plot SalePrice')
sns.distplot(df_train['SalePrice'])

#var = 'YearBuilt'
#data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
#data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));

#var = 'YearBuilt'
#data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
##f, ax = plt.subplots(figsize=(8, 6))
#fig = sns.boxplot(x=var, y="SalePrice", data=data)
#fig.axis(ymin=0, ymax=800000);

#corrmat = df_train.corr()
#f, ax = plt.subplots(figsize=(12, 9))
#sns.heatmap(corrmat, vmax=.8, square=True);

#k = 10 #number of variables for heatmap
#cols = corrmat.nlargest(k, 'SalePrice')['SalePrice'].index
#cm = np.corrcoef(df_train[cols].values.T)
#sns.set(font_scale=1.25)
#hm = sns.heatmap(cm, cbar=True, annot=True, square=True, fmt='.2f', annot_kws={'size': 10}, yticklabels=cols.values, xticklabels=cols.values)

#sns.set()
#cols = ['SalePrice', 'OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF', 'FullBath', 'YearBuilt']
#sns.pairplot(df_train[cols], size = 2.5)

#plt.xticks(rotation=90)
#plt.yticks(rotation=0)
#plt.show()

#missing data
#total = df_train.isnull().sum().sort_values(ascending=False)
#percent = (df_train.isnull().sum()/df_train.isnull().count()).sort_values(ascending=False)
#missing_data = pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
#print(missing_data.head(20))
#
#df_train = df_train.drop((missing_data[missing_data['Total'] > 1]).index,1)
#df_train = df_train.drop(df_train.loc[df_train['Electrical'].isnull()].index)
#df_train.isnull().sum().max() #just checking that there's no missing data missing...
#
##standardizing data
#saleprice_scaled = StandardScaler().fit_transform(df_train['SalePrice'][:,np.newaxis]);
#low_range = saleprice_scaled[saleprice_scaled[:,0].argsort()][:10]
#high_range= saleprice_scaled[saleprice_scaled[:,0].argsort()][-10:]
#print('outer range (low) of the distribution:')
#print(low_range)
#print('\nouter range (high) of the distribution:')
#print(high_range)
#
##deleting points
#df_train.sort_values(by = 'GrLivArea', ascending = False)[:2]
#df_train = df_train.drop(df_train[df_train['Id'] == 1299].index)
#df_train = df_train.drop(df_train[df_train['Id'] == 524].index)
#
##bivariate analysis saleprice/grlivarea
##var = 'TotalBsmtSF'
##data = pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
##data.plot.scatter(x=var, y='SalePrice', ylim=(0,800000));
##plt.show()
#
##applying log transformation
#df_train['SalePrice'] = np.log(df_train['SalePrice'])
#
##transformed histogram and normal probability plot
#sns.distplot(df_train['SalePrice'], fit=norm);
#fig = plt.figure()
#res = stats.probplot(df_train['SalePrice'], plot=plt)


plt.show()
