import os
import sys

import traci
import platform
import managed_traffic_light

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = os.environ.get('SUMO_HOME') + "/bin/sumo-gui.exe" 

if platform.system() == 'Darwin':
    sumoBinary = '/usr/local/bin/sumo-gui'

sumoCmd = [
    sumoBinary,
    '-c', 'simulation_data/osm.sumocfg',
    '--summary', 'output/summary.xml',
    '--tripinfo-output', 'output/trip_info.xml',
    '--statistic-output', 'output/statistics.xml',
    '--vehroute-output', 'output/vehicle-routes.xml',
    '--queue-output', 'output/queue.xml',
    '--emission-output', 'output/emissions.xml'
]

traci.start(sumoCmd)
step = 0

while step < 3600:
    traci.simulationStep()
    managed_traffic_light.step()
    step += 1

traci.close()
