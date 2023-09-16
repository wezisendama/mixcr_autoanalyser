import subprocess
from pathlib import Path
import glob
import pandas as pd
import sys

# Should be run with two command line arguments, eg. "python sra_analyse.py cloudbucket 10x-sc-xcr-vdj".
# First command line argument is name of Google Cloud data storage bucket containing files delivered from NCBI,
# and the second argument is the MiXCR preset.

bucketname = sys.argv[1]
mixcr_preset = sys.argv[2]

# Make new directory with same name as Google Cloud storage bucket, then download the bucket contents
newdir_command = "mkdir " + bucketname
bucket_download_command = "gsutil -m cp -r gs://" + bucketname + "/* " + bucketname

subprocess.call(newdir_command, shell=True)
subprocess.call(bucket_download_command, shell=True)

# Read in sample list from metadata
metadata_filename = glob.glob(bucketname + "/*.csv")[0]
sra_metadata = pd.read_csv(metadata_filename)
sra_numbers = sra_metadata["Run"]

# this will run MiXCR on each pair of fastq files in turn
for sra_id in sra_numbers:
    print ("Currently analysing: " + sra_id)
    mixcr_analysis_command = "mixcr -Xmx250g analyze " + mixcr_preset + " --species hsa --use-local-temp " + bucketname + "/" + sra_id + "/{{a}}R1.fastq.gz " + bucketname + "/" + sra_id + "/{{a}}R2.fastq.gz " + bucketname + "/" + sra_id + "_output"
    print ("The command used was: " + mixcr_analysis_command)
    subprocess.call(mixcr_analysis_command, shell=True)

# tidy up the MiXCR output files into analysis folder, ready to be imported to immunarch
newdir = "mkdir " + bucketname + "/analysis"
tidyup = "mv " + bucketname + "/*.clones.tsv " + bucketname + "/analysis"

subprocess.call(newdir, shell=True)
subprocess.call(tidyup, shell=True)
