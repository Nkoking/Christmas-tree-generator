#!/bin/bash

pip3 show colorama
if ! [ $? == 0 ]; then
	pip3 install colorama --user
fi

(exec python3 Tree-generator.py)
