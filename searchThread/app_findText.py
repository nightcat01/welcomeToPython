#-*- coding: utf-8 -*-
import searchThread

fileName = 'useatweb1.eaas.2018-04-30.log'
findTextList = {'Decrypt header', 'deviceUuid', 'A001'}
findText = 'eaas.common.ApiEncDecUtil - body : {"userPwd"'

searchThread.searchComplexTextListInFile(fileName, findTextList, findText)