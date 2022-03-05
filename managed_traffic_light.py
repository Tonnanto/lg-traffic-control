import traci

north_south_edges = ['-96311855#2', '-186632793#0', '393505712#0']
east_west_edges = ['-11627689', '-23918286#1', '-23918286#2', '-46191510#1', '-23918356']
tlsID = 'cluster_111246717_2609579002_2609579006_2866734308_2866734309_292943704_4198369468_4834945548_4834945572'
_lastPhase = 0


def get_vehicle_density_on_edges(edge_ids):
    count = 0
    totalTravelTime = 0
    for edge_id in edge_ids:
        count += traci.edge.getLastStepVehicleNumber(edge_id)
        totalTravelTime += traci.edge.getTraveltime(edge_id)
    return count / totalTravelTime


def step():
    global _lastPhase

    north_south_density = get_vehicle_density_on_edges(north_south_edges)
    east_west_density = get_vehicle_density_on_edges(east_west_edges)

    ratio = 1.0 if east_west_density == 0 else float(north_south_density) / east_west_density

    phase = traci.trafficlight.getPhase(tlsID)
    if phase == 0 and _lastPhase == 3:
        # NORTH SOUTH turned green
        if ratio > 1.2:
            traci.trafficlight.setPhaseDuration(tlsID, traci.trafficlight.getPhaseDuration(tlsID) + 10)
            print(f'NORTH SOUTH: {traci.trafficlight.getPhaseDuration(tlsID) + 10}s (+10)')
        elif ratio < 1:
            traci.trafficlight.setPhaseDuration(tlsID, traci.trafficlight.getPhaseDuration(tlsID) - 10)
            print(f'NORTH SOUTH: {traci.trafficlight.getPhaseDuration(tlsID) - 10}s (-10)')
        else:
            print(f'NORTH SOUTH: {traci.trafficlight.getPhaseDuration(tlsID)}s')

    elif phase == 2 and _lastPhase == 1:
        # EAST WEST turned green
        if ratio < 0.83:
            traci.trafficlight.setPhaseDuration(tlsID, traci.trafficlight.getPhaseDuration(tlsID) + 10)
            print(f'EAST WEST: {traci.trafficlight.getPhaseDuration(tlsID) + 10}s (+10)')
        elif ratio > 1:
            traci.trafficlight.setPhaseDuration(tlsID, traci.trafficlight.getPhaseDuration(tlsID) - 10)
            print(f'EAST WEST: {traci.trafficlight.getPhaseDuration(tlsID) - 10}s (-10)')
        else:
            print(f'EAST WEST: {traci.trafficlight.getPhaseDuration(tlsID)}s')

    _lastPhase = phase

