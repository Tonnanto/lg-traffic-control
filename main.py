import os
import sys

import traci

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

sumoBinary = os.environ.get('SUMO_HOME') + "/bin/sumo-gui.exe"
sumoCmd = [sumoBinary, "-c", "simulation_data/osm.sumocfg"]

traci.start(sumoCmd)
step = 0

while step < 3600:
    traci.simulationStep()
    # if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
    #     traci.trafficlight.setRedYellowGreenState("0", "GrGr")
    step += 1

traci.close()
