#!/usr/bin/python3
#coding: utf-8


import os
import psutil

# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()

cpu_usage = (load15/os.cpu_count()) * 100

print("The CPU usage is : ", cpu_usage)


# Getting % usage of virtual_memory ( 3rd field)
print('RAM memory % used:', psutil.virtual_memory()[2])



# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()

cpu_usage = (load15/os.cpu_count()) * 100

print("The CPU usage is : ", cpu_usage)



# Getting all memory using os.popen()
total_memory, used_memory, free_memory = map(
	int, os.popen('free -t -m').readlines()[-1].split()[1:])

# Memory usage
print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))


