# -*- coding: UTF-8 -*-
import httplib
import md5
import urllib
import random
import demjson
import sys
import config
reload(sys)  
sys.setdefaultencoding('utf8')

def translate_baidu(q):
	'从百度获取翻译'
	appid = config.appid
	secretKey = config.secretKey
	httpClient = None
	myurl = '/api/trans/vip/translate'
	fromLang = config.src
	toLang = config.dst
	salt = random.randint(32768, 65536)

	sign = appid+q+str(salt)+secretKey
	m1 = md5.new()
	m1.update(sign)
	sign = m1.hexdigest()
	myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
	 
	try:
	    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
	    httpClient.request('GET', myurl)
	 
	    #response是HTTPResponse对象
	    response = httpClient.getresponse()
	    return demjson.decode(response.read())['trans_result'][0]['dst']
	except Exception, e:
	    print e
	finally:
	    if httpClient:
	        httpClient.close()
	pass

def getDecks(fileNanme='origin.txt'):
	'从文件读取字段'
	f=open(fileNanme)
	tmp=f.read()
	f.close()
	decks=tmp.splitlines()
	for i in range(len(decks)):
		tmp=decks[i].split('\t')
		#print tmp
		decks[i]=tmp
	return decks

def writeDecks(data,fileNanme='out.txt'):
	'写入记忆库'
	print '开始写入文件 %s '%fileNanme
	try:
		f=open(fileNanme,'w')
		f.write(data)
	except:
		print '写入文件 %s 失败'%fileNanme
	else:
		print '写入文件 %s 成功'%fileNanme
	f.close()

#执行代码
res=getDecks(config.origin)
print '读取到文件 %s 中的 %d 条数据'%(config.origin,len(res))
for i in range(len(res)):
	src=res[i][config.srcIndex]
	dst=translate_baidu(src)
	res[i][config.dstIndex]=dst
	print '翻译 %s 到 %s'%(src,dst)
	res[i]= '\t'.join(res[i])
res='\n'.join(res)
writeDecks(res,config.out)