#!/bin/bash

export TCLBBUILDPATH=`cd ~/TCLB && pwd`
TCLBTOOLS=`cd ~/TCLB_tools && pwd`
export PYTHONPATH="$PYTHONPATH:$TCLBTOOLS/Python"

function tclb() {
	$TCLBBUILDPATH/CLB/$1/main $2 
}

function tclbmpi() {
	mpirun $TCLBBUILDPATH/CLB/$1/main $2 
}

export -f tclb
export -f tclbmpi

