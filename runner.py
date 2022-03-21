from vamb.__main__ import run
from datetime import datetime

if __name__ == '__main__':

    rootPath = "/home/ltms/Projects/ex"

    # try something with VAE and check on AMBER
    now = datetime.now().strftime("%m%d%y-%H%M")
    outdir = rootPath + "/" + now
    fasta = "/home/ltms/Projects/ex/CAMI_low_RL_S001__insert_270_GoldStandardAssembly.fasta"
    bams = ""
    nlaten = 32
    logFile = rootPath + "/" + "run.log"
    # run(outdir=outdir, fastapath=fasta, bampaths=bams, cuda=True, nlatent=nlaten)

    run(outdir=outdir,
        fastapath=fasta,
        # args.tnfs,
        # args.names,
        # args.lengths,
        bampaths=bams,
        # args.rpkm,
        # args.jgi,
        mincontiglength=mincontiglength,
        norefcheck=norefcheck,
        minalignscore=minalignscore,
        minid=minid,
        subprocesses=subprocesses,
        nhiddens=nhiddens,
        nlatent=nlatent,
        nepochs=nepochs,
        batchsize=batchsize,
        cuda=True,
        alpha=alpha,
        beta=beta,
        dropout=dropout,
        lrate=lrate,
        batchsteps=batchsteps,
        windowsize=windowsize,
        minsuccesses=minsuccesses,
        minclustersize=minsize,
        separator=separator,
        maxclusters=maxclusters,
        minfasta=minfasta,
        logfile=logfile)