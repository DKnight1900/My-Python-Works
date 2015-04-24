
#download pics from http://wuqing.org
#ps:wuqing is a Chinese poet
import urllib,urllib2  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')  
import os,shutil
import BeautifulSoup,re
import threading

class getImgThread(threading.Thread):
	def __init__(self,imgUrl,fileName):
		threading.Thread.__init__(self)
		self.url=imgUrl
		self.fileName=fileName
	def run(self):
		mutex.acquire()
		#print self.url
		print 'getting...',self.url
		mutex.release()
		urllib.urlretrieve(self.url,self.fileName)
		print 'saving...',self.fileName
		
if __name__ == '__main__':

	purl =  'http://wuqing.org/wp-content/uploads/2013/'
	psavepath  = r'D:/mycode/Python/MyWorks/wuqingshi'
	headers = { 'Use-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }  
	
#	if os.path.isdir("wuqingshi"):  
#		shutil.rmtree("wuqingshi")      # delete dir 
	if not os.path.isdir('wuqingshi'):  
		os.makedirs('wuqingshi')        # make dir
		
	mutex = threading.Lock()
	threads = []
	
	for i in range(1,13):
		if i < 10:
			url = purl + '0' + str(i)
		else:
			url = purl + str(i)
		try:
			req = urllib2.Request(url, headers=headers)  
			content = urllib2.urlopen(req).read()  
			#content = BeautifulSoup.BeautifulSoup(content, from_encoding='GB18030')   # BeautifulSoup  
			content = BeautifulSoup.BeautifulSoup(content) 
		except Exception,e:
			pass
		
		file = content.findAll(href=re.compile(r'.jpg'))
		for ii in range(1,len(file)):
			picname = str(file[ii].text)
			picurl = url + '/' + picname
			filename = psavepath + r'/' + picname
			
			print 'getting...',picurl
			try:
				urllib.urlretrieve(picurl, filename)
			except Exception,e:
				pass
			print 'saving...',filename
#			try:
#				threads.append(getImgThread(picurl,filename))
#			except Exception,e:
#				pass
			
#	for t in threads:
#		t.start()
#	for t in threads:
#		t.join()
#	print 'End'
	print 'all downloading is done!'
