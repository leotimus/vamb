#setup project
python setup.py build_ext --inplace

#dataset
https://codeocean.com/capsule/1017583/tree/v1

#create data dir
data/

#put dataset under data
data/urog/*

#create results dir
results/


#run
python vamb/__main__.py --outdir results/urog --fasta data/urog/contigs.fna.gz --rpkm data/urog/abundance.npz -o C
