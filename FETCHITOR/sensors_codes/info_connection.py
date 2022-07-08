#!/usr/bin/python3
#coding: utf-8

from os import system
import hashlib

scripts_ = """
echo "$(date) - USER: $USER - at origin of this running scripts. is $(whoami) the user is confirmed without verification(automatic)." >> /var/log/info_checking_connection_history.log
echo "[Checking connected users]" >> /var/log/info_checking_connection_history.log
echo "$(w && who)" >> /var/log/info_checking_connection_history.log
echo "" >> /var/log/info_checking_connection_history.log
"""

def curiosity_func_who_are_logged_in():
  if loglevel:
    system("{script}".format(
        script = scripts_
    ))
    
  return { "w": "{}", "who": "{}", "hostname": "", "public_ip": "", "user_env_var": "", "user": "", "timestamp": ""}
