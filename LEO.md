#setup project without conda
python setup.py build_ext --inplace

#setup with conda
create conda venv
#under conda venv
pip install -e .

#dataset
https://codeocean.com/capsule/1017583/tree/v1

#create data dir
data/

#put dataset under data
data/urog/*

#create results dir
results/


#run
python vamb/__main__.py --outdir results/urog --fasta data/urog/contigs.fna.gz \
--rpkm data/urog/abundance.npz -o C --cuda

python vamb/__main__.py --outdir results/airways --fasta data/airways/contigs.fna.gz \
--rpkm data/airways/abundance.npz -o C --cuda

python vamb/__main__.py -o SEP -z 0.95 -s 30 --outdir results/metabat2_2 --fasta data/metabat2/assemply/scaffolds.fasta --bamfiles E1.sorted.bam  E2.sorted.bam  E3.sorted.bam  P1.sorted.bam  P2.sorted.bam  P3.sorted.bam --minfasta 200000 --cuda

# working with metabat2's dataset
python vamb/__main__.py --outdir results/metabat2 --fasta data/metabat2/assemply/scaffolds.fasta --jgi data/metabat2/depth_matrix.tab -m 2500 --cuda

#strong100
python vamb/__main__.py --outdir results/strong100 --fasta data/strong100/assembly_graph.gfa --jgi data/strong100/edges_depth.txt --cuda -t 64
                                    
