import time
import psutil
import math
import argparse
import json

class Fileclass:
    fextention = "txt"
    def changeext(self,newext):
        self.fextention = newext

fileext = Fileclass()

parser = argparse.ArgumentParser(description='Snapshot parser')
parser.add_argument('-t', type=int, default=300, help='Deley in sec')
parser.add_argument('-f', type=str, default='txt', help='type of output file')
args = parser.parse_args()

fileext.changeext("args.f")
filename = "snapshot." + fileext.fextention

# init outputfile
f = open(filename, 'w')
f.close()

i = 0
while True:
    i += 1
    timestamp = time.ctime()

    #Overall CPU load
    cpu = psutil.cpu_percent(interval=1)
    #printstring += 'CPU load: ' + str(cpu) + '%, '
    #Overall memory usage
    vmem = psutil.virtual_memory()
    smem = psutil.swap_memory()
    mem = (vmem.used + smem.used)

    #Overall virtual memory usage
    #vmem.percent

    #IO information
    diskio = psutil.disk_io_counters()
    diskr = diskio.read_bytes
    diskw = diskio.write_bytes


    net = psutil.net_io_counters()
    #printstring += 'Network sent pkt: ' + str(net.packets_sent) + ', '
    #printstring += 'Network recive pkt: ' + str(net.packets_recv) + '.'

    x = {
        "Snapshot": i,
        "Time": timestamp,
        "CPU load": cpu,
        "Memory usage": mem,
        "Vmemory usage": vmem.percent,
        "Disk read": diskr,
        "Disk write": diskw,
        "Network sent pkt": net.packets_sent,
        "Network recive pkt": net.packets_recv
    }
    print(x)
    if args.f == 'txt':
        f = open('snapshot.txt', 'a')
        f.write(str(x) + '\n')
        f.close()
    elif args.f == 'json':
        y = json.dumps(x)
        f = open('snapshot.json', 'a')
        f.write(y + '\n')
        f.close()

    time.sleep(args.t)
#print(printstring)
