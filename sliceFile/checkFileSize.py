#-*- coding: utf-8 -*-
import os

def sliceFile(fileName) :

	# 파일 읽기 종료 플래그
	isEnd = True

	# 원본 파일 크기 확인
	orgFileSize = os.path.getsize(fileName)
	# print orgFileSize, "Bytes"                           # 바이트 단위로 구하기
	# print orgFileSize / 1024, "KB"                       # 킬로바이트 단위로
	# print "%.2f MB" % (orgFileSize / (1024.0 * 1024.0))  # 메가바이트 단위로
	# print "%.2f GB" % (orgFileSize / (1024.0 * 1024.0 * 1024.0))  # 메가바이트 단위로

	# 원본 파일명(확장자 포함)
	basename = os.path.basename(fileName)
	# 확장자
	fileExtension = basename[basename.rindex('.'):len(basename)]
	# 원본 파일명(확장자 제거)
	orgFileName = basename[:basename.rindex('.')]
	# 파일 저장 할 폴더 생성
	os.mkdir('./' + orgFileName)

	# 원본 파일 열어 확인
	with open(fileName, 'r') as file :
		# 파일 번호
		index = 1
		# 새로 만들어질 파일명
		newFile = './' + orgFileName + '/' + orgFileName + '_' + str(index) + fileExtension
		exportFile = open(newFile, 'w')

		while isEnd :
			# 원본파일에서 읽어온 line
			line = file.readline()
			# 더이상 읽을 라인이 없을 경우 반복문 빠져나갈 수 있도록 체크
			if not line : isEnd = False
			# MB 단위로 용량 체크
			exportFileSize = os.path.getsize(newFile) / (1024.0 * 1024.0)
			# 원본 파일 -> 만들어진 파일 내용 복사
			exportFile.write(line)
			# 만들어진 파일 용량 체크
			if exportFileSize >= 25.0 :
				# 용량이 차면 이름 바꿔 새 파일 생성
				index += 1
				newFile = './' + orgFileName + '/' + orgFileName + '_' + str(index) + fileExtension
				exportFile = open(newFile, 'w')
			

