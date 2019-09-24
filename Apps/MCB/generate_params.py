import csv
import sys
import os
import random

DIR=os.getcwd()
print(DIR)

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
    "min_np" : 1000*10000,
    "max_np" : 2000*10000,
}
def generate_params(n_group):
    res=[]
    for i in range(n_group):
        #generate MCB parameters
        nx = random.randint(params_dic["min_nx"],params_dic["max_nx"])
        ny = random.randint(params_dic["min_ny"],params_dic["max_ny"])
        xmax = random.uniform(params_dic["min_xmax"],params_dic["max_xmax"])
        ymax = random.uniform(params_dic["min_ymax"],params_dic["max_ymax"])
        xr = random.uniform(params_dic["min_xr"],params_dic["max_xr"])
        yr = random.uniform(params_dic["min_yr"],params_dic["max_yr"])
        np = random.randint(params_dic["min_np"],params_dic["max_np"])
        row=[nx,ny,xmax,ymax,xr,yr,np]
        res.append(row)
    return res

def main():
    params_test=generate_params(20)
    print(params_test)

if __name__=="__main__":
    main()