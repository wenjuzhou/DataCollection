#/bin/sh
bsub -q $1 -n $2 -o ../../Log/AppsLog/Cloverleaf/$3-$4-$5.log -e ../../Log/AppsLog/Cloverleaf/$3-$4-$5.err python3 run_file_input.py $3 $4 $5
