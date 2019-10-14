import csv
import random
import sys
import os

class Cloverleaf_generator(object):
    def __init__(self,nproc_list,n_group,path,way):
        self.params_dict = {
            "min_xcells" : 1000,
            "max_xcells" : 1500,
            "min_ycells" : 1000,
            "max_ycells" : 1500,
            "min_xmax" : 0.1,
            "max_xmax" : 10.0,
            "min_ymax" : 0.1,
            "max_ymax" : 10.0,
            "min_endtime" : 10.0,
            "max_endtime" : 30.0,
        }
        self.nproc_list = nproc_list
        self.n_group = n_group
        self.path=path
        self.way = way
        self.generator_way = {
            "group" : self.generate_group_input,
            "random" : self.generate_random_input,
        }

    def generate_params(self):
        res = []
        for i in range(self.n_group):
            #generate Cloverleaf parameters
            xcells = random.randint(self.params_dict["min_xcells"],self.params_dict["max_xcells"])
            ycells = random.randint(self.params_dict["min_ycells"],self.params_dict["max_ycells"])
            xmax = random.uniform(self.params_dict["min_xmax"],self.params_dict["max_xmax"])
            ymax = random.uniform(self.params_dict["min_ymax"],self.params_dict["max_ymax"])
            endtime = random.uniform(self.params_dict["min_endtime"],self.params_dict["max_endtime"])
            row = [xcells,ycells,xmax,ymax,endtime]
            res.append(row)
        return res
    
    def generate_group_input(self,params_list,path):
        with open(path,"w",newline='') as f:
            csv_writer = csv.writer(f)
            for nproc in self.nproc_list:
                for params in params_list:
                    line = params + [nproc]
                    csv_writer.writerow(line)
    
    def generate_random_input(self,params_list,path):
        with open(path,"w",newline='') as f:
            csv_writer = csv.writer(f)
            for params in params_list:
                nproc=list(random.sample(self.nproc_list,1))
                line = params + nproc
                csv_writer.writerow(line)
    
    def generator(self):
        params_list = self.generate_params()
        min_nproc = min(self.nproc_list)
        max_nproc = max(self.nproc_list)
        gap_nproc = int((max_nproc-min_nproc)/(len(self.nproc_list)-1))
        #test in windows, if linux, replace "\\" with "/"
        path = "{}\\input\\Cloverleaf-{}-{}-{}-{}-{}.csv".format(self.path,self.way,min_nproc,max_nproc,gap_nproc,self.n_group)
        self.generator_way[self.way](params_list,path)


# python run generate_input.py group/random 16 512 16 100 
def main():
    way = sys.argv[1]
    min_nproc=int(sys.argv[2])
    max_nproc=int(sys.argv[3])
    gap_nproc=int(sys.argv[4])
    nproc_list=list(range(min_nproc,max_nproc+1,gap_nproc))
    num_group=int(sys.argv[5])
    path = os.getcwd()
    #instance to run
    generator_instance = Cloverleaf_generator(nproc_list,num_group,path,way)
    generator_instance.generator()

if __name__ == "__main__":
    main()
