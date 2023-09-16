# MiXCR auto analyser
Testing creating a new repository and sharing little script for automating MiXCR analysis of SRA files delivered to a Google Cloud storage bucket.

The script should be run with two command line arguments, eg. `python sra_analyse.py cloudbucket 10x-sc-xcr-vdj`

The first command line argument is name of Google Cloud storage bucket containing files delivered from NCBI (via the SRA Run Selector), and the second argument is the MiXCR preset.

Credit goes to @erilu because I learned the Python syntax for loops and executing bash commands from [this script](https://github.com/erilu/bulk-rnaseq-analysis/blob/master/fastq_download.py).
