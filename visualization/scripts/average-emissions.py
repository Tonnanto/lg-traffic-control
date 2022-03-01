# Das Skript nimmt queue.xml (Lanes, in denen gewartet wird) 
# und produziert eine parsed Version.
# Hierbei wird gezählt, in wie vielen lanes zu einem bestimmtem Step gewartet wird

# Braucht beautifulsoup4 und lxml via pip install

from os.path import abspath
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
 
trip_file = abspath('output/trip_info.xml')
trip_file_parsed = abspath('output/trip_info.parsed.xml')

with open(trip_file, 'r') as f:
    data = f.read()

xml = BeautifulSoup(data, 'xml')

trips = xml.find_all('tripinfo')

type_map = {
	'veh_passenger': 'PKWs',
	'pt_train': 'Züge',
	'pt_bus': 'Busse',
}

parsed_trips = {}
num_vehicles = {}
total_emissions = {}

for trip in trips:
	emissions = trip.find('emissions')

	vehicle_type = trip['vType']
	vehicle_emissions = float(emissions['CO2_abs'])

	# Count vehicles
	if vehicle_type in num_vehicles:
		num_vehicles[vehicle_type] += 1
	else:
		num_vehicles[vehicle_type] = 1

	if vehicle_type in total_emissions:
		total_emissions[vehicle_type] += vehicle_emissions
	else:
		total_emissions[vehicle_type] = vehicle_emissions
	
	parsed_trips[trip['id']] = vehicle_emissions

# f = open(trip_file_parsed, 'w')
# f.write(str(xml))
# f.close()


avg_emissions = {}

for vehicle_type in list(num_vehicles.keys()):
	avg_emissions[type_map[vehicle_type]] = (total_emissions[vehicle_type] / num_vehicles[vehicle_type]) / 1000000 # 1000000mg in a kg

print(avg_emissions)

fig, ax = plt.subplots(figsize =(16, 9))

ax.barh(list(avg_emissions.keys()),list(avg_emissions.values()), height=0.4)
ax.set_title('Durchschnittlicher CO2 Output (in kg)',
             loc ='left')
ax.invert_yaxis()

for i in ax.patches:
    plt.text(i.get_x() + 0.05, i.get_y() + 0.25,
             str(round((i.get_width()), 5)),
             fontsize = 22, fontweight ='bold',
             color ='white')

plt.show()