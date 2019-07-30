import subprocess
import random
import time
import csv
import sys

def run_cmd(cmd):
    return
def generate_cmd(params_dict):
    return
def main():
    params_dic = {
	"min_nx" : 100,
	"max_nx" : 1000,
	"min_ny" : 100,
	"max_ny" : 1000,
	"min_xmax" : 1.0,
	"max_xmax" : 10.0,
	"min_ymax" : 1.0,
	"max_ymax" : 10.0,
	"min_xr" : 1.0,
	"max_xr" :10.0,
	"min_yr" : 1.0,
	"max_yr" :10.0,
	"min_np" : 100*10000,
	"max_np" : 1000*10000,
	"nproc_list" : list(range(int(sys.argv[1]),int(sys.argv[2])+1,int(sys.argv[3])))
    }
    print(params_dic["nproc_list"])

if __name__ == "__main__":
    main()

