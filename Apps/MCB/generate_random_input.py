import csv
import sys
import os
import random
from generate_params import generate_params

DIR=os.getcwd()
print(DIR)

def generate_random_input(nproc_list,num_group,path):
    params_list=generate_params(num_group)
    with open(path,"w",newline='') as f:
        csv_writer=csv.writer(f)
        for params in params_list:
            nproc=list(random.sample(nproc_list,1))
            line=params+nproc
            csv_writer.writerow(line)


def main():
    #get generate_group_intput() params
    min_nproc=int(sys.argv[1])
    max_nproc=int(sys.argv[2])
    gap_nproc=int(sys.argv[3])
    nproc_list=list(range(min_nproc,max_nproc+1,gap_nproc))
    num_group=int(sys.argv[4])
    sub_path="input\\MCB-random-{}-{}-{}-{}.csv".format(min_nproc,max_nproc,gap_nproc,num_group)
    path="{}\\{}".format(DIR,sub_path)
    generate_random_input(nproc_list,num_group,path)
if __name__ == "__main__":
    main()