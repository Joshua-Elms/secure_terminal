#!/bin/bash

# only works for macOS currently
# cd to the directory you want to install this project in

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p ~/bin
python3 gen_ss_file.py
cp ss ~/bin/ss
chmod +x ~/bin/ss

echo "Installation complete. You can now run the script using the command 'ss'. Please visit safety_config.py to configure the program."