import os
import sys

import traci
import platform

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
    '--tripinfo-output', 'output/trip_info.xml'
]

traci.start(sumoCmd)
step = 0

while step < 3600:  # traci.simulation.getMinExpectedNumber() > 0:
    traci.simulationStep()

    # [(veh_id, veh_length, entry_time, exit_time, vType), ...]
    vehicleData = traci.inductionloop.getVehicleData("inductionLoop_test2")

    for (vehicleId, _, _, _, vehicleType) in vehicleData:
        co2Emission = traci.vehicle.getCO2Emission(vehicleId)
        timeLoss = traci.vehicle.getTimeLoss(vehicleId)

        idString = f'vehicle: {vehicleId}'
        typeString = f'type: {vehicleType}'
        co2String = f'CO2 emissions: {"%.0f" % co2Emission} mg/s'
        timeLossString = f'time loss: {"%.1f" % timeLoss} s'

        print(f"{idString:<40}{typeString:<40}{co2String:<40}{timeLossString:<40}")

    # if traci.inductionloop.getLastStepVehicleNumber("inductionLoop_test2") > 0:
        # traci.trafficlight.setRedYellowGreenState("0", "GrGr")

    step += 1

traci.close()
