#!/bin/bash
machines=`cat $OAR_FILE_NODES | uniq`
nbMachine=`wc -l machines`

deb=0
intervalle=2000
fin= intervalle

for m in $machines; do
    echo "Execution sur $m .....";
    oarsh $m python pi.py deb fin m
    deb=fin
    fin=deb+intervalle
    done
