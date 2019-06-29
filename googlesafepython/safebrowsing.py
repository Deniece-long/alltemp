#!/usr/bin/env python
#
# Copyright (c) 2016 Jun C. Valdez
# Code is distrubuted under the terms of an MIT style license
# http://www.opensource.org/licenses/mit-license
#

import requests
import json

SB_CLIENT_ID = "malicious-url-detection"
SB_CLIENT_VER = "1.6.4"


class LookupAPI(object):
    def __init__(self, apikey):
        self.apiurl = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=%s' % (apikey)
        self.platform_types = ['ANY_PLATFORM']
        self.threat_types = ['THREAT_TYPE_UNSPECIFIED',
                             'MALWARE',
                             'SOCIAL_ENGINEERING',
                             'UNWANTED_SOFTWARE',
                             'POTENTIALLY_HARMFUL_APPLICATION']
        self.threat_entry_types = ['URL']

    def set_threat_types(self, threats):
        self.threat_types = threats

    def set_platform_types(self, platforms):
        self.platform_types = platforms

    def threat_matches_find(self, *urls):
        threat_entries = [{"url": "https://sg.godaddy.com/zh/"},
        {"url": "https://www.rakuten.co.jp//"}, {"url": "http://diply.com/"},
        {"url": "https://www.nytimes.com/"}, {"url": "https://aws.amazon.com/cn/"},
        {"url": "https://vimeo.com/"}, {"url": "http://www.youth.cn/"},
        {"url": "http://www.espn.com/"},
        {"url": "http://www.nicovideo.jp/"},
        {"url": "https://www.salesforce.com/cn/?ir=1"},
        {"url": "https://www.bbc.co.uk/"}, {"url": "https://www.ask.com/"},
        {"url": "https://www.ebay.de/"},
        {"url": "https://www.booking.com/index.zh-cn.html?label=gen173rf-1BCAEoggJCAlhYSDNYA2gxiAEBmAEywgEKd2luZG93cyAxMMgBDNgBAegBAZICAXmiAhBhbGV4YS5jaGluYXouY29tqAID;sid=4af01d01b679f7df5a7327e30ddbe13f;sb_price_type=total&"},
        {"url": "http://soundcloud.com/"}, {"url": "http://terraclicks.com/"}
                          ]
        results = {}

        for url_ in urls:
            url = {'url': url_}
            threat_entries.append(url)

        reqbody = {
            'client': {
                'clientId': SB_CLIENT_ID,
                'clientVersion': SB_CLIENT_VER
            },
            'threatInfo': {
                'threatTypes': self.threat_types,
                'platformTypes': self.platform_types,
                'threatEntryTypes': self.threat_entry_types,
                'threatEntries': threat_entries
            }
        }

        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.apiurl,
                          data=json.dumps(reqbody),
                          headers=headers)
        #
        # need to include exceptions here
        #

        return r.json()


class UpdateAPI(object):
    def __init__(self, apikey):
        pass


