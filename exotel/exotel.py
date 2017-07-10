# -*- coding: utf-8 -*-


import datetime
import requests

from ._compat import urljoin


class Exotel:
    def __init__(self,sid,token, baseurl='https://twilix.exotel.in/'):
        self.sid =  sid
        self.token = token
        self.baseurl = urljoin(baseurl, 'v1/Accounts/{sid}/'.format(sid=sid))

    def sms(self, from_number, to, body,encoding_type = "plain", priority = "normal", status_callback = None ):
        """
        sms - sends sms using exotel api
        """
        return requests.post(urljoin(self.baseurl, 'Sms/send.json'),
            auth = (self.sid, self.token),
            data = {
                'From': from_number,
                'To': to,
                'Body': body,
                'EncodingType':encoding_type,
                'Priority' : priority,
                'StatusCallback' : status_callback
             })

    def call_flow(self,from_number,caller_id,flow_id,timelimit = 14400,timeout = 30,status_callback=None,custom_data = None):
       """
       call_flow -creates a call to from_number and flow_id with the exophone(caller_id)
       """
       return requests.post(urljoin(self.baseurl, 'Calls/connect.json'),
        auth=(self.sid, self.token),
        data={
            'From': from_number,
            'CallerId': caller_id,
            'Url': "http://my.exotel.in/exoml/start/{flow_id}".format(flow_id=flow_id),
            'TimeLimit': timelimit,
            'CallType': "trans",
            'TimeOut' : timeout,
            'StatusCallback' : status_callback,
            'CustomField' : custom_data

        })

    def call_number(self, from_number, caller_id, to,timelimit = 14400,timeout = 30,status_callback=None,custom_data = None):
       """
       call_number -creates a call to from_number and then to with the exophone(caller_id)
       """
       return requests.post(urljoin(self.baseurl, 'Calls/connect.json'),
        auth=(self.sid, self.token),
        data={
            'From': from_number,
            'CallerId': caller_id,
            'To': to,
            'TimeLimit': timelimit,
            'CallType': "trans",
            'TimeOut' : timeout,
            'CustomField' : custom_data,
            'StatusCallback' : status_callback
        })

    def call_details(self, call_sid):
      """
       call_details - returns call details object as a response object
      """
      return requests.get(urljoin(self.baseurl, 'Calls/{}.json'.format(call_sid)), auth=(self.sid, self.token))

    def sms_details(self, sms_sid):
      """
       sms_details - returns sms details object as a response object provided the sms sid
      """
      return requests.get(urljoin(self.baseurl, 'Sms/Messages/{}.json'.format(sms_sid)), auth=(self.sid, self.token))
