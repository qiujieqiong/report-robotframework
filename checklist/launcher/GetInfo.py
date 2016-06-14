#!/usr/bin/env python
#encoding:utf-8

import sys
import ConfigParser
import testlink

class GetInfo:
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