#!/usr/bin/python
#encoding:utf-8
import testlink
import os

os.environ['TESTLINK_API_PYTHON_SERVER_URL'] = "https://testlink.deepin.io/lib/api/xmlrpc/v1/xmlrpc.php"
os.environ['TESTLINK_API_PYTHON_DEVKEY'] = "c78509ab4224c772231f9dd12427b385"

class FillResult():

    def FillResultToTestLink(self,testcaseid, testplanid, buildname, result, note, user, platformid='0'):
        self.testcaseid = testcaseid
        self.testplanid = testplanid
        self.buildname  = buildname
        self.result     = result
        self.note       = note
        self.user       = user
        self.platformid = platformid


        
        tls = testlink.TestLinkHelper().connect(testlink.TestlinkAPIClient)
        print self.testcaseid, self.testplanid, self.buildname, self.result, self.note, self.user, self.platformid
        
        tls.reportTCResult(testcaseid=self.testcaseid, testplanid=self.testplanid, buildname=self.buildname, status=self.result,notes=self.note)

if __name__  == "__main__":

    a = FillResult()    
    #a.FillResultToTestLink(testcaseid='43', testplanid='76', buildname='执行1.0', result='f', note='some notes',user='bonjov1', platformid='0')
