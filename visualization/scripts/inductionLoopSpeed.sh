#!/bin/bash

SUMO_VIZ="$SUMO_HOME/tools/visualization"

python $SUMO_VIZ/plotXMLAttributes.py output/inductionLoop_test2.xml -s -x begin -y speed