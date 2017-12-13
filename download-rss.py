# -*- coding: utf-8 -*- 
# coding: UTF-8

import urllib.request
from bs4 import BeautifulSoup
import MySQLdb
from models import CrawlSiteList

def insert_record(title, link, posted_datetime):
    conn = MySQLdb.connect(
        user='username',
        passwd='userpassword',
        host='172.17.0.2',
        db='ff14rssdata',
        charset="utf8"
    )

    sql = "insert into rss_history (title, link) values (%s, %s)"
    var = (title, link)
    cur = conn.cursor()
    ret = cur.execute( sql, var )
    ret = cur.execute( "commit" )

    cur.execute("select * from rss_history")
    for row in cur.fetchall():
        print(row)

def getRss(url):
    res = urllib.request.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")
    for item in soup.find_all("item"):
        title = item.find("title").string
        link  = item.attrs['rdf:about']
        dt    = item.find("dc:date").string
        insert_record(title, link, dt )
    print(url)

crawlSiteList = CrawlSiteList.CrawlSiteList()
siteList      = crawlSiteList.getSiteList()

for site in siteList:
    getRss(site[1])


