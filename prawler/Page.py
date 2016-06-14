'''
Created on 2016/06/14

@author: dk
'''
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Page(object):
    '''
    classdocs
    '''

    def __init__(self, url):
        '''
        Constructor
        '''
        self.url  = url
        page = requests.get(url)
        self.page = page
        self.html = BeautifulSoup(page.text.encode(page.encoding))
        
    def get_url(self):
        return self.url
    
    def get_html(self):
        return self.html
    
    def get_title(self):
        return self.html.find("title").text
    
    def get_contents(self):
        return self.html.text