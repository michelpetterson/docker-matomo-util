# -*- coding: utf-8 -*-

####################################################################
# Program Name: Matomo Mass Creation
# Version: 1.0
# Description: Script para criar sites em massa no piwik
# Author: Michel Peterson
# Date: 29/06/2021
####################################################################

import os
import pycurl
import cStringIO
import xmltodict

TOKEN_AUTH = ''

MatomoUrl = 'https://matomo.dominio.com/'

def MatomoGetAllSites():

    MatomoApiGetSites = MatomoUrl \
            + 'index.php?module=API&method=SitesManager.getAllSites&filter_limit=-1&format=xml&token_auth=' \
            + TOKEN_AUTH

    response = cStringIO.StringIO()

    c = pycurl.Curl()
    c.setopt(pycurl.HTTPGET, 1)
    c.setopt(pycurl.URL, MatomoApiGetSites)
    c.setopt(pycurl.HTTPHEADER, ['Accept: application/xml'])
    c.setopt(c.WRITEFUNCTION, response.write)
    c.perform()
    c.close()

    with open('/tmp/allsites.xml', 'w') as f:
        f.write(response.getvalue())


def MatomoGetSite(SiteName):
    with open('/tmp/allsites.xml') as fd:
        doc = xmltodict.parse(fd.read())
        ObjectsList = doc['result']['row']

        SiteList = []
        for index in xrange(len(ObjectsList)):
            SiteList.append(ObjectsList[index]['name'])

        # print SiteName
        # print SiteList

        if SiteName.rstrip() in SiteList:
            return True
        else:
            return False

MatomoGetAllSites()

with open('/tmp/sitelist.txt', 'r') as sitelist:
    for SiteName in sitelist:
        print ('Verificando site:', SiteName)
        result = MatomoGetSite(SiteName)

        # print result

        if result == False:
            print ('Enviando site:', SiteName)
            Send2Matomo = []
            Send2Matomo.append(SiteName)
            Send2Matomo.append('https://' + SiteName)
            Send2Matomo.append('https://www.' + SiteName)
            Send2Matomo.append('http://www.' + SiteName)
            Send2Matomo.append('http://' + SiteName)

            MatomoApiAddSite = MatomoUrl \
                + 'index.php?module=API&method=SitesManager.addSite&siteName=' \
                + Send2Matomo[0].rstrip() + '&urls[0]=' \
                + Send2Matomo[1].rstrip() + '&urls[1]=' \
                + Send2Matomo[2].rstrip() + '&urls[2]=' \
                + Send2Matomo[3].rstrip() + '&urls[3]=' \
                + '&token_auth=' + TOKEN_AUTH

            c = pycurl.Curl()
            c.setopt(pycurl.HTTPGET, 1)
            c.setopt(c.VERBOSE, True)
            c.setopt(pycurl.URL, MatomoApiAddSite)
            c.setopt(pycurl.HTTPHEADER, ['Accept: text/html'])
            c.perform()

        else:
            print ('Site ja criado:', SiteName)

if os.path.exists("/tmp/allsites.xml"):
    os.remove("/tmp/allsites.xml")

MatomoGetAllSites()
