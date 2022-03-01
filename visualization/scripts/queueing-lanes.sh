#!/bin/bash

SUMO_VIZ="$SUMO_HOME/tools/visualization"

echo "Parsing file..."
python visualization/scripts/num-of-queueing-vehicles.py

echo "Loading plot..."
python $SUMO_VIZ/plotXMLAttributes.py output/queue.parsed.xml -o /tmp/plot.png -s -x timestep -y count --idattr id