#-*- coding: utf-8 -*-

# In File

# 파일 전체에서 찾을 문구를 포함한 스레드 찾아 리스트 형태로 리턴(전자출결 전용)
def searchIncludedThreadInFile(fileName, findText) :

	threadNameList = []
	# 파일 open 
	# r : 읽기 모드
	# w : 쓰기 모드
	# a : 추가 모드 - 파일 마지막에 새로운 내용 추가
	with open(fileName, 'r') as file_object :
		# threadName = ''
		trigger = True	
		
		# 읽은 파일 라인 별로 읽어오는 반복문
		while trigger :
			line = file_object.readline()	
			if not line : trigger = False
			
			# 검색할 문자 확인 and
			# 검색한 문자의 스레드가 빈값인지 체크 - 처음 잡힌 스레드만 확인하기 위해 확인
			# if line.find(findText) > 0 and threadName is '' :
			# 	# 스레드명 검색
			# 	startIndex = line.index('[')
			# 	endIndex = line.index(']')
			# 	threadName = line[startIndex:endIndex + 1]	
			
			# 검색할 문자 확인
			if line.find(findText) > 0 :
			 	# 스레드명 검색
				startIndex = line.index('[')
				endIndex = line.index(']')
				threadName = line[startIndex:endIndex + 1]	
				
				# 검색 할 스레드에 추가
				if threadName not in threadNameList :
					threadNameList.append(threadName)
	print(threadNameList)
	return threadNameList

# 파일 전체에서 문구 리스트를 포함한 행을 찾을 경우
def searchTextListInFile(fileName, findTextList) :
	# 새로 출력할 파일
	exportFileName = open('newFile_findThread.txt', 'w')

	with open(fileName, 'r') as file_object :
		trigger = True

		# 읽은 파일 라인 별로 읽어오는 반복문
		while trigger :
			line = file_object.readline()	
			if not line : trigger = False
			
			# 검색할 문자 확인 and
			# 검색한 문자의 스레드가 빈값인지 체크 - 처음 잡힌 스레드만 확인하기 위해 확인
			# if line.find(findText) > 0 and threadName is '' :
			# 	# 스레드명 검색
			# 	startIndex = line.index('[')
			# 	endIndex = line.index(']')
			# 	threadName = line[startIndex:endIndex + 1]	
			
			# 스레드명 체크
			for i in findTextList :
				if i in line :
					exportFileName.write(line)
	# 쓴 파일 close
	exportFileName.close()

# 파일 전체에서 문구가 포함 된 행을 찾을 경우
def searchTextInFile(fileName, findText) :
	# 새로 출력할 파일
	exportFileName = open('newFile_' + findText + '.txt', 'w')

	with open(fileName, 'r') as file_object :
		trigger = True

		# 읽은 파일 라인 별로 읽어오는 반복문
		while trigger :
			line = file_object.readline()	
			if not line : trigger = False
			
			# 찾을 텍스트 체크가 line 안에 있을 경우
			if findText in line :
				exportFileName.write(line)
	# 쓴 파일 close
	exportFileName.close()

# 파일 전체에서 여러 문구가 전부 포함 된 행을 찾을 경우
def searchTextListAtAllInFile(fileName, findTextList) :
	# 새로 출력할 파일
	exportFileName = open('newFile_findTextList.txt', 'w')

	with open(fileName, 'r') as file_object :
		trigger = True

		# 읽은 파일 라인 별로 읽어오는 반복문
		while trigger :
			line = file_object.readline()	
			if not line : trigger = False

			# 모든 문구가 확인 될 때 텍스트 파일에 쓴다.
			if isTextListAtAllInSingleLine(line, findTextList) :
				exportFileName.write(line)
	# 쓴 파일 close
	exportFileName.close()	

# In Single Line

# 파일 전체에서 여러 문구가 전부 포함 된 행을 찾을 경우
def searchComplexTextListInFile(fileName, findTextList, findText) :
	# 새로 출력할 파일
	exportFileName = open('newFile_findTextList.txt', 'w')

	with open(fileName, 'r') as file_object :
		trigger = True

		# 읽은 파일 라인 별로 읽어오는 반복문
		while trigger :
			line = file_object.readline()	
			if not line : trigger = False

			isInAll = isTextListAtAllInSingleLine(line, findTextList)
			isInLine = isTextInSingleLine(line, findText)

			# 모든 문구가 확인 될 때 텍스트 파일에 쓴다.
			if isInAll or isInLine :
				exportFileName.write(line)
	# 쓴 파일 close
	exportFileName.close()

# 여러 문구가 전부 포함 된 행을 찾을 경우
def isTextListAtAllInSingleLine(line, findTextList) :
	#결과값
	result = False

	# 찾을 텍스트 리스트 체크
	for i in findTextList :
		result = True
		if i not in line :
			result = False
	
	return result

# 리스트 내의 문구가 포함 된 행을 찾을 경우
def isTextListInSingleLine(line, findTextList) :

	#결과값
	result = False

	# 찾을 텍스트 리스트 체크
	for i in findTextList :
		if i in line :
			result = True
			break
	
	return result

# 문구가 포함 된 행을 찾을 경우
def isTextInSingleLine(line, findText) :

	#결과값
	result = False

	# 찾을 텍스트 체크
	if findText in line :
		result = True
	
	return result	
		
# print('===========================================================================================================')
# data = open(filename, 'r')
# lines = data.read()
# print(lines)
# data.close()
