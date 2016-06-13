'''
Created on 2016/06/14

@author: dk
'''
# -*- coding: utf-8 -*-

import unittest
from prawler.Page import Page

class Test(unittest.TestCase):

    def test_constructor(self):
        # 存在するページの場合
        page = Page("http://www.google.com")
        self.assertEqual(page.url, "http://www.google.com")
        
        # 存在しないページの場合
        page = Page("http://1qazxsw2.com/")
        self.assertEqual(page.url, "http://1qazxsw2.com/")
        
        pass

    def test_get_url(self):
        page = Page("http://www.google.com")
        self.assertEqual(page.get_url(), "http://www.google.com")
        pass

    def test_get_title(self):
        page = Page("http://www.google.com")
        self.assertEqual(page.get_title(), "Google")
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()