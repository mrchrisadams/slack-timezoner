import os
import slack
import json
from collections import Counter
import pprint



class TimeZoneCounter:

    client = None

    def __init__(self):
        # connect to the slack API
        self.client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])


    def summary(self):

        # make a counter thingo in python
        cntr = Counter()

        # get a list of our users
        res = self.client.users_list()
        da = res.data
        members = da['members']

        # pull out the timezones
        timezones = [mem.get('tz') for mem in members]

        # make running totals of timezones
        for tz in timezones:
            cntr[tz] += 1

        # import ipdb ; ipdb.set_trace()
        return cntr