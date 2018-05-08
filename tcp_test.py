import os
import sys
import pdb
import random
import pickle
from itertools import islice
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.util import dumpNodeConnections
from mininet.link import TCLink
from mininet.node import OVSController
from mininet.node import Controller
from mininet.node import RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.util import quietRun
import random
from subprocess import Popen, PIPE
from time import sleep, time
from ripl.ripl.dctopo import JellyfishTopo

def main():
	nSwitches = 10
	nPorts = 3
	adjlist_file = "rrg_small_3_10"

	
	#pox_command = "python pox/pox.py log --file=pox_logs/pox.log,w riplpox.riplpox --topo=jelly,%s,%s,%s --routing=jelly --mode=reactive" % (str(nSwitches), str(nPorts), adjlist_file)
	#pox_args = {"stdin": PIPE, "stdout": PIPE, "stderr": PIPE}
	#pox_process = Popen(pox_command.split(), **pox_args)
	#print("waiting for pox to start up")
	#sleep(2)

	jelly_topo = JellyfishTopo(nSwitches, nPorts, adjlist_file)
	#net = Mininet(topo=jelly_topo, host=CPULimitedHost, link=TCLink, controller=RemoteController, autoSetMacs=True)
	#net.start()
	#print("starting mininet")

	#print("waiting 10s for pox to add connections")
	#sleep(10)

	#print("running pingAll to test connectivity")
	#net.pingAll()
	randomHosts = jelly_topo.hosts()
	random.shuffle(randomHosts)
	clients = randomHosts[0::2]
	servers = randomHosts[1::2]
	pairs_list = zip(clients, servers)
	
	for pair in pairs_list:
		print pair[1] + " iperf -s &"
		print pair[0] + " iperf -c %s -P 8 -t 60 >> results/ecmp_8_eight_output.txt &" %(pair[1])
	
	
	#print("initiating tcp servers")
	#for server in servers:
	#    net.get(server).cmd("iperf -s &")
	#
	#print("initiating tcp clients")
	#for client, server in pairs_list:
	#    net.get(client).cmd("sleep 1; iperf -c %s" % server)
	#
	#print("waiting for results")
	#for client, server in pairs_list:
	#    result = net.get(client).waitOutput()	
	#    
	#
	#net.stop()
	#pox_process.kill()

if __name__ == '__main__':
	main()
