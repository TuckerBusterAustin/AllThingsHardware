#SystemReport
#Reports various aspects, intermittently, of:
#1. CPU utilization, Speed, Processes, and Threads
#2. Memory Utilization
#3. Network Utilization including send and receive
#4. GPU Utilization
#5. disk usage
#Export data to excel file

#Author: Tucker Billimek
#Date: 8/21/23
# Will need to install required packages:
#utilize "pip install psutil pandas openpyxl"

import os
import psutil
import pandas as pd
import time 

#CPU information
print('The CPU usage is: ', psutil.cpu_percent(4), "%")
print('The CPU time is: ', psutil.cpu_percent(4))
print('The CPU usage is: ', psutil.cpu_percent(4))
#memory utilization
print('The virtual memory is: ', psutil.virtual_memory())
print('The swap memory is: ', psutil.swap_memory())
#network util
print('System-wide network I/O statistics: ',psutil.net_io_counters())
print('System wide socket connections: ',psutil.net_connections())
# GPU util
#not supported with Python, looking to provide support

#disk usage
print('The disk usage is: ', psutil.disk_usage())
#excel export

