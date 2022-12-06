# — — — — — — -Importing Packages — — — — — — — — — — — -
import matplotlib.pyplot as plt
import numpy as np
from sklearn_extra.cluster import KMedoids
# — — — — — — -Assigning Initial Centers — — — — — — — — — — — -
centers = [[4, 5], [9, 10]]
# — — — — — — -Assigning Data: Dummy Data used in example above — — — — — — — — — — — — — — — — — — 
df=np.array([[7,8], [9,10], [11,5], [4,9], [7,5], [2,3], [4,5]])
# — — — — — — -Fit KMedoids clustering — — — — — — — — — — — -
KMobj = KMedoids(n_clusters=2).fit(df)
# — — — — — — -Assigning Cluster Labels — — — — — — — — — — — -
labels = KMobj.labels_

# — — — — — — -Extracting Unique Labels — — — — — — — — — — — -
unq_lab = set(labels)
# — — — — — — -Setting Up Color Codes — — — — — — — — — — — -
colors_plot = [
 plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unq_lab))
]
for k,col in zip(unq_lab, colors_plot):

    class_member_mask = labels == k
 
 # — — — — — — -Setting datapoint Feature X and Feature Y — — — — — — — — — — — -
xy = df[class_member_mask]
 
 # — — — — — — -Plotting Feature X and Feature Y for each cluster labels — — — — — — — — — — — -
 
plt.plot(
xy[:, 0],
xy[:, 1],
"o",
markerfacecolor=tuple(col),
markeredgecolor="o",
markersize=10,
);
# — — — — — — -Annotate Centroids — — — — — — — — — — — -
plt.plot(
 KMobj.cluster_centers_[:, 0],
 KMobj.cluster_centers_[:, 1],
 "o",
 markerfacecolor="orange",
 markeredgecolor="k",
 markersize=10,
);
# — — — — — — -Add title to the plot — — — — — — — — — — — -
plt.title("KMedoids clustering on Dummy Data- Medoids are represented in Orange.", fontsize=14);