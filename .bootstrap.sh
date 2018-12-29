#!/usr/bin/env bash
# .boostrap.sh
# install required python dependencies

bold=$(tput bold)
normal=$(tput sgr0)

echo "${bold}running bootstrap ....${normal}"

if [ ! -e .venv ]; then
    echo "${bold}initializing virtualenv...${normal}"
    virtualenv --python=`which python` .venv
    echo "${bold}activating  venv....${normal}"
    . .venv/bin/activate
    echo "${bold}installing python requirements...${normal}"
    pip install -r requirements.txt
    echo "${bold}installing development python requirements...${normal}"
    pip install -r requirements_dev.txt
    echo "${bold}installing local source...${normal}"
    pip install -e .
fi

echo "${bold}finished bootstrapping...${normal}"
