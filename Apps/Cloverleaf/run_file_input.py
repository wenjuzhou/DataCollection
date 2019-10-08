import subprocess
import os
import random
import time
import csv
import sys

class Cloverleaf_executor(object):
    def __init__(self,input_path,output_path,beg,end):
        self.input_path = input_path
        self.output_path = output_path
        self.beg = beg
        self.end = end

    def executor(self):
        all_inputs = self.read_input()
        for i in range(self.beg-1,self.end):
            cmd =self.generate_cmd(all_inputs[i])
            exec_time,status = self.run_cmd(cmd)
            if status:
                line = all_inputs[i] + [exec_time]
                self.save_data(line)
            else:
                line = all_inputs[i] + [1000000]
                self.save_data(line)

    def read_input(self):
        all_inputs  =[]
        with open(self.input_path,"r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                all_inputs.append(row)
        return all_inputs

    def generate_cmd(self,params):
        cloverin_path = "clover.in"
        with open(cloverin_path,"w") as f:
            content = '*clover\n\n state 1 density=0.2 energy=1.0\n state 2 density=1.0 energy=2.5 geometry=rectangle xmin=0.0 xmax=5.0 ymin=0.0 ymax=5.0\n\n x_cells={}\n y_cells={}\n\n xmin=0.0\n ymin=0.0\n xmax={}\n ymax={}\n\n initial_timestep=0.04\n timestep_rise=1.5\n max_timestep=0.04\n end_time={}\n\n*endclover'.format(params[0],params[1],params[2],params[3],params[4])
            f.write(content)
        cmd = 'mpijob -n {} /home/cs/ustczwj/compile_intel2019/CloverLeaf/CloverLeaf_MPI/clover_leaf'.format(params[5])
        return cmd

    def run_cmd(self,cmd):
        status = True
        start = time.time()
        try:
            subprocess.run(cmd,shell=True,timeout=3600)
            end = time.time()
            return end-start,status
        except:
            end = time.time()
            status = False
            return end-start,status

    def save_data(self,line):
        with open(self.output_path,"a",newline="") as f:
            writer = csv.writer(f)
            writer.writerow(line)

def main():
    input_dir = "{}/input".format(os.getcwd())
    output_dir = "../../Data/AppsData/Cloverleaf/"
    filename = sys.argv[1]
    beg = int(sys.argv[2])
    end = int(sys.argv[3])
    input_path = "{}/{}".format(input_dir,filename)
    output_path = "{}/{}-{}-{}".format(output_dir,beg,end,filename)
    executor_instance = Cloverleaf_executor(input_path,output_path,beg,end)
    executor_instance.executor()
    

if __name__ == "__main__":
    main()
