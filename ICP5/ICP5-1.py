import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# create data object
df_train = pd.read_csv('train.csv')
# create scatter plot for Garage Area and Sale Price in the noisy data
data = pd.concat([df_train['SalePrice'], df_train['GarageArea']], axis=1)
print(data)
data.plot.scatter(x='GarageArea', y='SalePrice');

error = stats.zscore(data)
print(stats.zscore(data))
# remove outliers and noise
data1 = data[(error < 2).all(axis=1)]
# recreate graph
data1.plot.scatter(x='GarageArea', y='SalePrice');
plt.show()