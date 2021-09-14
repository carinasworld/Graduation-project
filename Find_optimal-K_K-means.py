# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 09:16:27 2021

@author: Nelly
"""


import matplotlib.pyplot as plt
from kneed import KneeLocator   #pip install kneed
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


from sklearn.cluster import KMeans

k = 5
kmeans = KMeans(n_clusters=k)
y = kmeans.fit_predict(groups_smol[cols])
y is kmeans.labels_
kmeans.cluster_centers_

###  fun with elbow method 

kmeans_kwargs = {
    "init": "random",
    "n_init": 10,
    "max_iter": 50,
    "random_state": 123, }

sse = [] # list for SSE values for each k
for k in range(1,50):
    kmeans = KMeans(n_clusters=k, **kmeans_kwargs)  #unpack with **
    kmeans.fit(groups_smol)
    sse.append(kmeans.inertia_)


plt.figure(figsize=(16,8))
plt.plot(range(1, 50), sse, 'bx-')
plt.xlabel("Number of optimal clusters (k)")
plt.ylabel("SSE")  # sum of squared error(SSE) for some value of K
plt.show()


## calculating optimal k 
kl = KneeLocator(range(1,50), sse, curve="convex", direction = "decreasing")
kl.elbow    ## 3 is the numer of optimal clusters 
