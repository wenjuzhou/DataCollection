import csv
import sys
import os
from generate_params import generate_params

DIR=os.getcwd()
print(DIR)

def generate_group_input(nproc_list,num_group,path):
    params_list=generate_params(num_group)
    with open(path,"w",newline='') as f:
        csv_writer=csv.writer(f)
        for nproc in nproc_list:
            for params in params_list:
                #print(type(params))
                line=params+[nproc]
                #print(type(line))
                csv_writer.writerow(line)


def main():
    #get generate_group_intput() params
    min_nproc=int(sys.argv[1])
    max_nproc=int(sys.argv[2])
    gap_nproc=int(sys.argv[3])
    nproc_list=list(range(min_nproc,max_nproc+1,gap_nproc))
    num_group=int(sys.argv[4])
    sub_path="group_input\\MCB-{}-{}-{}-{}.csv".format(min_nproc,max_nproc,gap_nproc,num_group)
    path="{}\\{}".format(DIR,sub_path)
    generate_group_input(nproc_list,num_group,path)
if __name__ == "__main__":
    main()