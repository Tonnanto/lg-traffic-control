# Das Skript nimmt queue.xml (Lanes, in denen gewartet wird) 
# und produziert eine parsed Version.
# Hierbei wird gezählt, in wie vielen lanes zu einem bestimmtem Step gewartet wird

# Braucht beautifulsoup4 und lxml via pip install

from os.path import abspath
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
 
queue_file = abspath('output/queue.xml')
queue_file_parsed = abspath('output/queue.parsed.xml')

with open(queue_file, 'r') as f:
    data = f.read()

xml = BeautifulSoup(data, 'xml')

data_items = xml.find_all('data')

queue = {}
ids = 0

for data in data_items:
	lanes = data.find_all('lane')
	queue[data['timestep']] = len(lanes)
	data['count'] = len(lanes)
	data['id'] = ++ids

f = open(queue_file_parsed, 'w')
f.write(str(xml))
f.close()

print(f"Wrote {queue_file_parsed}")

# fig, ax = plt.subplots()

# plt.plot(list(queue.keys()),list(queue.values()), linewidth=2.0)

# plt.show()