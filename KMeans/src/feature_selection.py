from sklearn.feature_extraction import DictVectorizer
from sklearn.cluster import KMeans
from time import time
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.metrics import homogeneity_score, completeness_score, v_measure_score, adjusted_rand_score

# train_data = pd.read_csv('../dataput.csv', header=None)
# train_data['Spaces'] = train_data.applymap(lambda x: str.count(x, ' '))
# train_data['Words'] = train_data['Spaces']/2

data = []




with open('../data/input.mat', 'r') as file:
    for i, line in enumerate(file):
        l = line.split()
        d = dict([(k, v) for k, v in zip(l[::2], l[1::2])])
        data.append(d)


v = DictVectorizer(sparse=True, dtype=float)
X = v.fit_transform(data)

start = time()

pca = PCA(n_components=10)
reduced_X = pca.fit_transform(X.toarray())
kmeans = KMeans(init='k-means++', n_clusters=7, max_iter=100)
kmeans.fit(reduced_X)

labels = kmeans.predict(reduced_X)

np.savetxt('../predictions/kmeans_pca_4.txt', labels, fmt='%i')


print "Explained variance : "

try:
    print pca.explained_variance_ratio_
except:
    pass

print "Time elapsed: ", time() - start