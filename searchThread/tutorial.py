#-*- coding: utf-8 -*-
import searchThread

fileName = 'useatweb1.eaas.2018-04-30.log'
findText = 'userPwd'

threadNameList = []
threadNameList = searchThread.searchIncludedThreadInFile(fileName, findText)
searchThread.searchThreadInFile(fileName, threadNameList)