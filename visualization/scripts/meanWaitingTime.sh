#!/bin/bash

SUMO_VIZ="$SUMO_HOME/tools/visualization"

python $SUMO_VIZ/plotXMLAttributes.py summary.xml -s -x time -y meanWaitingTime --idattr loaded