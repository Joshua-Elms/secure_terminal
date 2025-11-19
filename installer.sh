#!/bin/bash

# only works for macOS currently
# cd to the directory you want to install this project in

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdir -p ~/bin
python3 gen_ss_file.py
touch ~/.bash_profile
echo "export PATH=\"~/bin\":\$PATH" >> ~/.bash_profile
source ~/.bash_profile
cp ss ~/bin/ss
chmod 755 ~/bin/ss

echo "Installation complete @ ~/.bash_profile and ~/bin/ss. You can now run the script using the command 'ss'. Please visit safety_config.py to configure the program."