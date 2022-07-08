#!/usr/bin/python3
#coding: utf-8
#
from os import system


class systemdHealthChecker(objects):
  def __init__(self,):
    pass
  
  def detect_failure_status(self):
    pass
  
  def notify_local(self,title,text,Critical=False):
    pass
  
  def notification_sending_over_SSH(self,hostname,port=22,password=None,ssh_id_keyfile=None):
    pass
  
  def notification_sending_over_TCP(self,hostname,port,data=None):
    pass
  
  def get(self,json_out=None ,csv_out=None):
    pass
