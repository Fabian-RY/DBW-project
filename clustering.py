# -*- coding: utf-8 -*-

from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
import matplotlib

def get_info_from_project():
    pass

def cluster(array, method, num_clusters, distance_type, linkage_type):
    algorithm = AgglomerativeClustering(
                                        linkage=linkage_type,
                                        n_clusters=num_clusters,
                                        affinity=distance_type)
    algorithm.fit(array)
    validation = silhouette_score(algorithm.labels_, array, metric=distance_type)
    return (algorithm.labels_, validation)
    
def plot(array, labels):
    
    pass