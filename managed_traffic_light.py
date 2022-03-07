import traci


class ManagedTLS:
    def __init__(self, name, tls_id, ns_edges, ew_edges):
        self.name = name
        self.tls_id = tls_id
        self.ns_edges = ns_edges
        self.ew_edges = ew_edges
        self.last_phase = 0


tls_1 = ManagedTLS(
    'Bahnhofkreuzung',
    'cluster_111246717_2609579002_2609579006_2866734308_2866734309_292943704_4198369468_4834945548_4834945572',
    ['-96311855#2', '-186632793#0', '393505712#0'],
    ['-11627689', '-23918286#1', '-23918286#2', '-46191510#1', '-23918356']
)

tls_2 = ManagedTLS(
    'Stresemann/Willy-Brandt',
    'J0',
    ['-12273115', '-143183287', '118607895', '392719989'],
    ['143183283#0', '284588825', '186198379', '143183286', '390709999']
)

managed_traffic_lights = [tls_1, tls_2]


def get_vehicle_density_on_edges(edge_ids):
    count = 0
    totalTravelTime = 0
    for edge_id in edge_ids:
        count += traci.edge.getLastStepVehicleNumber(edge_id)
        totalTravelTime += traci.edge.getTraveltime(edge_id)
    return count / totalTravelTime


def step():
    
    for tls in managed_traffic_lights:
        
        north_south_density = get_vehicle_density_on_edges(tls.ns_edges)
        east_west_density = get_vehicle_density_on_edges(tls.ew_edges)
    
        ratio = 1.0 if east_west_density == 0 else float(north_south_density) / east_west_density
        phase = traci.trafficlight.getPhase(tls.tls_id)
        
        if phase == 0 and tls.last_phase == 3:
            # north-south turned green
            if ratio > 1.2:
                traci.trafficlight.setPhaseDuration(tls.tls_id, traci.trafficlight.getPhaseDuration(tls.tls_id) + 10)
                print(f'{tls.name} north-south: {traci.trafficlight.getPhaseDuration(tls.tls_id) + 10}s (+10)')
            elif ratio < 1:
                traci.trafficlight.setPhaseDuration(tls.tls_id, traci.trafficlight.getPhaseDuration(tls.tls_id) - 10)
                print(f'{tls.name} north-south: {traci.trafficlight.getPhaseDuration(tls.tls_id) - 10}s (-10)')
            else:
                print(f'{tls.name} north-south: {traci.trafficlight.getPhaseDuration(tls.tls_id)}s')
    
        elif phase == 2 and tls.last_phase == 1:
            # east-west turned green
            if ratio < 0.83:
                traci.trafficlight.setPhaseDuration(tls.tls_id, traci.trafficlight.getPhaseDuration(tls.tls_id) + 10)
                print(f'{tls.name} east-west: {traci.trafficlight.getPhaseDuration(tls.tls_id) + 10}s (+10)')
            elif ratio > 1:
                traci.trafficlight.setPhaseDuration(tls.tls_id, traci.trafficlight.getPhaseDuration(tls.tls_id) - 10)
                print(f'{tls.name} east-west: {traci.trafficlight.getPhaseDuration(tls.tls_id) - 10}s (-10)')
            else:
                print(f'{tls.name} east-west: {traci.trafficlight.getPhaseDuration(tls.tls_id)}s')
    
        tls.last_phase = phase
