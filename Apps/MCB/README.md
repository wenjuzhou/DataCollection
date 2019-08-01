# MCB scripts

---

## Running

### running in shell directly

**running cmd:** `bsub -q QUEUE -n NPROCESS -o ../../Log/AppsLog/MCB/MCB-QUEUE-MINPROCESS_MAXPROCESS_INTERVALPROCESS-NGROUP_NPERGROUP.log -e ../../Log/AppsLog/MCB/MCB-QUEUE-MINPROCESS_MAXPROCESS_INTERVALPROCESS-NGROUP_NPERGROUP.err python3 MCB_run.py`MINPROCESS MAXPROCESS INTERVALPROCESS NGROUP NPERGROUP QUEUE

- NPROCESS : the number of process applied, normally equals MAXPROCESS
- MINPROCESS : the number of minimus process in the experiment
- MAXPROCESS : the number of maximum process in the experiment
- INTERVALPROCESS : the number of interval of the process in the experiment
- NGROUP : the group number of different inputs
- NPERGROUP : the number of sample  per group(the same input execpt process number)


**example:** `bsub -q testv4 -n 32 -o ../../Log/AppsLog/MCB/MCB-testv4-8_24_8-4_1.log -e ../../Log/AppsLog/MCB/MCB-testv4-8_24_8-4_1.err python3 MCB_run.py 8 32 8 4 1 testv4`

###run.sh has capsolate the complicate cmd, run it is simpler

**shell running:** `bash run.sh QUEUE NPROCESS MINPROCESS MAXPROCESS INTERVALPROCESS NGROUP NPERGROUP`

**shell example:** `bash run.sh testv4 32 8 32 8 4 2`

## Modules

module load intel/2019.update1 && module load intelmpi/2019.update1 && module load python/3.6.1

## Data

runtime data in ../../Data/AppsData/MCB/MCB-QUEUE-MINPROCESS_MAXPROCESS_INTERVALPROCESS-NGROUP_NPERGROUP
