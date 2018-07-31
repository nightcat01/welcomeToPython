#-*- coding: utf-8 -*-
import os

for root, dirs, files, in os.walk('./') :
	print root # root 폴더 -> 현재 os.walk()로 가리키고 있는 폴더 ./ : 현재 폴더
	print dirs # root 내의 폴더 리스트
	print files # root 내의 파일 리스트
	for file in files :
		print file