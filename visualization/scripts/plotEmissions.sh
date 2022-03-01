#!/bin/bash

SUMO_VIZ="$SUMO_HOME/tools/visualization"

python $SUMO_VIZ/plotXMLAttributes.py output/emissions.xml -s -x time -y CO2 --idattr id --filter-ids veh0 --label "CO2 Output of veh0"