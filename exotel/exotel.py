#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import requests
class Exotel:
    def __init__(self,sid,token):
        self.sid =  sid
        self.token = token
        self.baseurl = 'https://twilix.exotel.in/v1/Accounts/{sid}'.format(sid=sid)

    def sms(self, from_number, to, body,encoding_type = "plain", priority = "normal", status_callback = None ):
        return requests.post(self.baseurl + '/Sms/send.json',
            auth = (self.sid, self.token),
            data = {
                'From': from_number,
                'To': to,
                'Body': body,
                'EncodingType':encoding_type,
                'Priority' : priority,
                'StatusCallback' : status_callback
             })

    def call_flow(self,from_number,caller_id,flow_id,timelimit):
       return requests.post(self.baseurl + '/Calls/connect.json',
        auth=(self.sid, self.token),
        data={
            'From': from_number,
            'CallerId': caller_id,
            'Url': "http://my.exotel.in/exoml/start/{flow_id}".format(flow_id=flow_id),
            'TimeLimit': timelimit,
            'CallType': "trans",
        })
    def call_number(self,from_number,caller_id,to,timelimit):
       return requests.post(self.baseurl + '/Calls/connect.json',
        auth=(self.sid, self.token),
        data={
            'From': from_number,
            'CallerId': caller_id,
            'To': to,
            'TimeLimit': timelimit,
            'CallType': "trans",
        })
