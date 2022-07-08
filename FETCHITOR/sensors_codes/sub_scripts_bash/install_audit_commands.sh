#!/bin/bash
sudo apt update -y
sudo apt install lynis ssh-audit nmap -y
sudo cp -r systemd-checker-auto /opt/
sudo chmod  -R 0600 /opt/systemd-checker-auto
sudo chmod a+x /opt/systemd-checker-auto/systemd-no-failure.py
sudo chmod a+x /opt/systemd-checker-auto/run_script.sh
sudo mv /opt/systemd-checker-auto/systemd-no-failure.timer /etc/systemd/system/systemd-no-failure.timer
sudo mv /opt/systemd-checker-auto/systemd-no-failure.service /etc/systemd/system/systemd-no-failure.service
sudo ln -s  /opt/systemd-checker-auto/run_script.sh /usr/bin/run_script_systemd-no-failure.sh
sudo ln -s  /opt/systemd-checker-auto/systemd-no-failure.py /usr/bin/systemd-no-failure
echo "Services need to be enable now ! ...next!"
