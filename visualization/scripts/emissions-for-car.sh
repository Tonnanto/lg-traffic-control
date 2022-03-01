#!/bin/bash

SUMO_VIZ="$SUMO_HOME/tools/visualization"

if [ -n "$1" ]; then
	echo "Generating emissions graph for vehicle $1"
else
    echo "Usage: ./visualization/scripts/emissions-for-car.sh <VEHICLE_ID>"
    exit 1
fi


python $SUMO_VIZ/plotXMLAttributes.py output/emissions.xml -o /tmp/plot.png -v -s -x time -y CO2 --idattr id --filter-ids $1 --label "CO2 Output of $1"