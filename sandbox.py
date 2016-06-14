'''
Created on 2016/06/14

@author: dk
'''
# -*- coding: utf-8 -*-
import sys

from prawler.Page import Page

if __name__ == '__main__':
    param = sys.argv

    page = Page(param[1])
    # print(page.get_title())
    
    print(page.get_contents())
    
    pass
