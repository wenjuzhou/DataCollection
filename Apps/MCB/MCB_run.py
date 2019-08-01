import subprocess
import random
import time
import csv
import sys
#generate running cmd according in-parameters
def generate_cmd(nx,ny,xmax,ymax,xr,yr,np,nproc):
	cmd = "mpijob -n {} /home/cs/ustczwj/applications/mcb-20130723/src/MCBenchmark.exe --nZonesX={} --nZonesY={} --xDim={} --yDim={} --xSource={} --xSource={} --numParticles={}".format(nproc,nx,ny,xmax,ymax,xr,yr,np)
	return cmd

#run a case get running time
def run_cmd(cmd):
	status = True
	start = time.time()
	try:
		subprocess.run(cmd,shell=True,timeout=36000)
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


#run flow control
def run(params_dic,csv_path):
	
	headers = ["nproc","nx","ny","xmax","ymax","xr","yr","np","exec_time"]
	with open(csv_path,"w",newline="") as f:
		writer = csv.writer(f)
		writer.writerow(headers)

	for i in range(params_dic["n_group"]):
		#generate MCB parameters
		nx = random.randint(params_dic["min_nx"],params_dic["max_nx"])
		ny = random.randint(params_dic["min_ny"],params_dic["max_ny"])
		xmax = random.uniform(params_dic["min_xmax"],params_dic["max_xmax"])
		ymax = random.uniform(params_dic["min_ymax"],params_dic["max_ymax"])
		xr = random.uniform(params_dic["min_xr"],params_dic["max_xr"])
		yr = random.uniform(params_dic["min_yr"],params_dic["max_yr"])
		np = random.randint(params_dic["min_np"],params_dic["max_np"])
		#random select number of process
		nprocs = random.sample(params_dic["nproc_list"],params_dic["n_pergroup"])
		
		#generate and run
		for nproc in nprocs:
			cmd = generate_cmd(nx,ny,xmax,ymax,xr,yr,np,nproc)
			exec_time,status = run_cmd(cmd)
			if status:
				line = [nproc,nx,ny,xmax,ymax,xr,yr,np,exec_time]
				save_data(line,csv_path)
	return


def main():
	#parameters directory, including all information about running data collection
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
	"nproc_list" : list(range(int(sys.argv[1]),int(sys.argv[2])+1,int(sys.argv[3]))),
	"n_group" : int(sys.argv[4]),
	"n_pergroup" : int(sys.argv[5]),
	}
	csv_path = "/home/cs/ustczwj/workspace/Data/AppsData/MCB/MCB-{}-{}_{}_{}-{}_{}.csv".format(sys.argv[6],sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
	run(params_dic,csv_path)
	print(params_dic["nproc_list"])
	

if __name__ == "__main__":
	main()

