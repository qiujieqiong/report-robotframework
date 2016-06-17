#!/usr/bin/env python
#encoding:utf-8

import sys
import ConfigParser
import os
import subprocess
#import testlink
from pykeyboard import PyKeyboard

k = PyKeyboard()

class GetInfo:
	'''
	def __init__(self):
		cf = ConfigParser.ConfigParser()
		self.infos = cf.read("test.info")
		self.project_name = cf.get("project_info","project_name")
		self.plan_name = cf.get("project_info","plan_name")
		self.build_name = cf.get("project_info","build_name")
		url = "https://testlink.deepin.io/lib/api/xmlrpc/v1/xmlrpc.php"
		key = "c78509ab4224c772231f9dd12427b385"  
		self.tlc = testlink.TestlinkAPIClient(url, key)

	def getUserPath(self):
		self.userPath = os.path.expanduser('~')
		return self.userPath

	def getPlanID(self):
		
		a = self.tlc.getTestPlanByName(self.project_name,self.plan_name)
  		return a[0]['id']

  	def getPlanName(self):
  		return self.plan_name

  	def getBuildName(self):
  		return self.build_name

  	def getCaseID(self):
  		a = self.tlc.getTestPlanByName(self.project_name,self.plan_name)
  		info = self.tlc.getTestCasesForTestPlan(a[0]['id'])
		info = sorted(info.keys())
		return info
	'''
	def send_single_key(self,key):
		k.press_key(key)
		k.release_key(key)

	def getCasesID(self):
		#casesID = os.environ["CASE_ID"]
		IDfile = '/home/deepin/casesID.txt'
		if os.path.exists(IDfile):
			ID_obj = open(IDfile,'r')
			ID_content = ID_obj.read()
			ID_obj.close()
			return ID_content.split(",")

	def openf(self):
		subprocess.check_call(["touch test.result"],shell=True)

	def appendContent(self,content):
		result_obj = open('test.result','a')
		result_obj.write(content+'\n')
		result_obj.close()


if __name__ == '__main__':
	ins = GetInfo()

	plan_id = ins.getPlanID()
	print "getPlanID:",plan_id
	cases_id = ins.getCaseID()
	print "cases_ID:",cases_id
	cases_id = '\n'.join(cases_id)
	with open("casesID.txt",'w') as f:
		f.write(cases_id)
		f.close()