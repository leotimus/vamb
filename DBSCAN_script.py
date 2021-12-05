import sys
import os

import numpy as np
import torch
import csv
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

sys.path.append('/home/fwolf/vamb')
import vamb

# Calculate TNF
with open('/home/fwolf/reduced_az-af/scaffolds.fasta', 'rb') as contigfile:
    tnfs, contignames, lengths = vamb.parsecontigs.read_contigs(contigfile)

# Calculate RPKM
bamdir = '/home/fwolf/reduced_az-af/bams/'
bampaths = [bamdir + filename for filename in os.listdir(bamdir) if filename.endswith('.bam')]
rpkms = vamb.parsebam.read_bamfiles(bampaths)

# Encode
vae = vamb.encode.VAE(nsamples=rpkms.shape[1])
dataloader, mask, rpkm = vamb.encode.make_dataloader(rpkms, tnfs)
vae.trainmodel(dataloader)
latent = vae.encode(dataloader)
# vamb.encode.VAE.save(vae, '/home/fwolf/hidden_state/state.pt')

# vae = vamb.encode.VAE.load('/home/fwolf/hidden_state/state.pt')
# dataloader, mask = vamb.encode.make_dataloader(rpkms, tnfs)
# vae.trainmodel(dataloader)
# latent = vae.encode(dataloader)

# cluster_iterator = vamb.cluster.cluster(latent, labels=np.array(contignames)[mask])
# clusters = dict(cluster_iterator)
#
#
# def filterclusters(clusters, lengthof):
#     filtered_bins = dict()
#     for medoid, contigs in clusters.items():
#         binsize = sum(lengthof[contig] for contig in contigs)
#
#         if binsize >= 200000:
#             filtered_bins[medoid] = contigs
#
#     return filtered_bins
#
#
# lengthof = dict(zip(contignames, lengths))
# filtered_bins = filterclusters(vamb.vambtools.binsplit(clusters, '_'), lengthof)
# print('Number of bins before splitting and filtering:', len(clusters))
# print('Number of bins after splitting and filtering:', len(filtered_bins))

# labels = []
#
# for i in range(len(contignames)):
#     labels.append(0)
#
# for n, (medois, cluster) in enumerate(filtered_bins.items()):
#     for i in cluster:
#         labels[contignames.index(i)] = n
#
X_embedded = TSNE(n_components=2, learning_rate='auto', init='random').fit_transform(latent)

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

df = pd.DataFrame()
df["x"] = X_embedded[:, 0]
df["y"] = X_embedded[:, 1]
# df["z"] = X_embedded[:, 2]

# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
#
# ax.scatter(df["x"], df["y"], df["z"], alpha=0.1)

sns.scatterplot(data=df, x="x", y="y", alpha=0.1, palette="deep", legend=False)
plt.show()

# for i in range(1, 100):
#
#     clustering = DBSCAN(eps=0.1*i).fit_predict(X_embedded)
#
#     clusters = {}
#
#     for j in clustering:
#         if j not in clusters.keys():
#             clusters[j] = 1
#         else:
#             clusters[j] += 1
#
#     print('{:.1f}: {}'.format(0.1*i, clusters))

# clustering = DBSCAN(eps=4).fit_predict(X_embedded)


# clustering = DBSCAN(eps=2.8).fit_predict(latent)
#
# clusters = {}
# bins = {}
#
# with open('/home/fwolf/az-af/clusters_tSNE.tsv', 'wt') as out_file:
#     tsv_writer = csv.writer(out_file, delimiter='\t')
#
#     for i, j in enumerate(clustering):
#         if str(j) not in bins.keys():
#             clusters[j] = 1
#             bins[str(j)] = [contignames[i]]
#         else:
#             clusters[j] += 1
#             bins[str(j)].append(contignames[i])
#         tsv_writer.writerow([str(j), contignames[i]])
# #
# with open('/home/fwolf/reduced_az-af/scaffolds.fasta', 'rb') as file:
#     fastadict = vamb.vambtools.loadfasta(file)
#
# bindir = '/home/fwolf/reduced_az-af/bins_rpkm'
# vamb.vambtools.write_bins(bindir, filtered_bins, fastadict, maxbins=500)
