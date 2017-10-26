#coding:utf8

# 文件执行前需要先执行pip3 freeze >requirements/common.txt
import os
Config = {
	"dev":["ForgeryPy", "pygments", "certifi", "chardet", 
			"colorama", "httpie", "idna", "requests", "urllib3"],
	"produce":[]
}
current_dir = os.getcwd()
common_txt_path = current_dir + '/requirements/common.txt'
dev_txt_path = current_dir + '/requirements/dev.txt'
pro_txt_path = current_dir + '/requirements/produce.txt'
commonText, devText, proText = '', '-r common.txt\n', '-r common.txt\n'
if os.path.exists(common_txt_path):
	fp = open(common_txt_path, 'r+')
	allLines = fp.readlines()
	for line in allLines:
		isInDev, isInPro = False, False
		for devStr in Config.get('dev'):
			if devStr.lower() in line.lower():
				devText = devText + line
				isInDev = True
				break
		for proStr in Config.get('produce'):
			if proStr.lower() in line.lower():
				proText = proText + line
				isInPro = True
				break
		if isInDev == False and isInPro == False:
			commonText = commonText + line

def writeText(path, text):
	if os.path.exists(path) != True:
		os.mknod(path)
	fp = open(path, 'w')
	fp.write(text)
	fp.flush()
	fp.close()

writeText(common_txt_path, commonText)
writeText(dev_txt_path, devText)
writeText(pro_txt_path, proText)
