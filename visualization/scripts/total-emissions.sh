#!/bin/bash

SUMO_VIZ="$SUMO_HOME/tools/visualization"

python $SUMO_VIZ/plotXMLAttributes.py output/trip_info.xml -o /tmp/plot.png -v -s -x id -y duration --idattr id --label "CO2 Output" 