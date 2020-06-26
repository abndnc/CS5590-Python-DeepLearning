import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


sns.set(style='white', color_codes=True)
data = pd.read_csv('CC.csv')
# check how many clusters => 7
print(data['TENURE'].value_counts())
# look for nulls
nulls = pd.DataFrame(data.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)
# remove entire row if it contains null
data = data.dropna(axis=0, how ='any', thresh=None, subset=None, inplace=False)
nullData = pd.DataFrame(data.isnull().sum().sort_values(ascending=False))
nullData.columns = ['Null Count']
nullData.index.name = 'Feature'
print(nullData)

# Divide data into x, y where x is BALANCE and y is TENURE
x = data.iloc[:,1:]
print(x.shape)

# elbow method
# wcss: within-cluster sums of squares
wcss = []
print()
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    # Save within-cluster sums of squares to the list
    wcss.append(kmeans.inertia_)

# display the graph
print(wcss)
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# from the map, at k=3 seems like data slowly reduced => choose k=3
# silhouette score
km = KMeans(n_clusters=3)
km.fit(x)
y_cluster_kmeans = km.predict(x)
score = metrics.silhouette_score(x, y_cluster_kmeans)
print()
print('Silhouette score for',3,'clusters',score)

scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns = x.columns)

km = KMeans(n_clusters=3)
km.fit(X_scaled)
y_cluster_kmeans = km.predict(X_scaled)
score = metrics.silhouette_score(X_scaled, y_cluster_kmeans)
print('Silhouette score for',3,'clusters after scaled',score)

# apply PCA
# scale the features
scaler = StandardScaler()
scaler.fit(x)
x_scaler = scaler.transform(x)

# apply KMeans to PCA, 10 is picked randomly
pca = PCA(4)
x_pca = pca.fit_transform(x_scaler)
# combine data into 10 columns
df = pd.DataFrame(data=x_pca)
# Display PCA
plt.scatter(df[0], df[1], alpha=.1, color='black')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x_pca)
    # save within-cluster sums of squares to the list
    wcss.append(kmeans.inertia_)
print()
print(wcss)
plt.plot(range(1, 11), wcss)
plt.title('the elbow method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# from the graph, choose k=4
km = KMeans(n_clusters=4)
km.fit(x_pca)
y_cluster_kmeans = km.predict(x_pca)
score = metrics.silhouette_score(x_pca  , y_cluster_kmeans)
print('Silhouette score after applying PCA',score)