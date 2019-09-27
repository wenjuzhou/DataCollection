import subprocess
import os
import random
import time
import csv
import sys

#generate running cmd according in-parameters
def generate_cmd(params):
	cmd = "mpijob -n {} /home/cs/ustczwj/applications/mcb-20130723/src/MCBenchmark.exe --nZonesX={} --nZonesY={} --xDim={} --yDim={} --xSource={} --xSource={} --numParticles={}".format(params[7],params[0],params[1],params[2],params[3],params[4],params[5],params[6])
	return cmd

#run a case get running time
def run_cmd(cmd):
	status = True
	start = time.time()
	try:
		os.system(cmd)
		end = time.time()
		return end-start,status
	except:
		end = time.time()
		status = False
		return end-start,status

#save data to csv
def save_data(line,csv_path):
	with open(csv_path,"a",newline="") as f:
		writer = csv.writer(f)
		writer.writerow(line)

def run(input_path,output_path,beg,end):
	all_inputs=[]
	with open(input_path,"r") as f:
		csv_reader=csv.reader(f)
		for row in csv_reader:
			all_inputs.append(row)
	for i in range(beg,end+1):
		#print(all_inputs[i-1])
		cmd=generate_cmd(all_inputs[i])
		print(cmd)
		exec_time,status = run_cmd(cmd)
		if status:
			line = all_inputs[i]+[exec_time]
			save_data(line,output_path)


def main():
	input_dir="{}/input".format(os.getcwd())
	output_dir="../../Data/AppsData/MCB"
	sub_path=sys.argv[1]
	input_path="{}/{}".format(input_dir,sub_path)
	output_path="{}/{}".format(output_dir,sub_path)
	beg=int(sys.argv[2])
	end=int(sys.argv[3])
	run(input_path,output_path,beg,end)

if __name__ == "__main__":
	main()