#/bin/sh
bsub -q $1 -n $2 -o ../../Log/AppsLog/MCB/MCB-$1-$3_$4_$5-$6_$7.log -e ../../Log/AppsLog/MCB/MCB-$1-$3_$4_$5-$6_$7.err python3 MCB_run.py $3 $4 $5 $6 $7 $1
