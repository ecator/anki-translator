#coding=utf8
#获取专有日语名称的读法，来源:https://kotobank.jp/word/
#https://search.yahoo.co.jp/search?p=%E6%96%87%E8%8F%AF%E7%A7%80%E9%BA%97%E9%9B%86&aq=-1&oq=&ei=UTF-8&fr=top_ga1_sa&x=wrt

import httplib
import urllib
import re
import time
import sys
import random

reload(sys)  
sys.setdefaultencoding('utf8')
fileName='list.txt'
if len(sys.argv)>1: fileName=sys.argv[1]
def getContent(word):
    '获取雅虎搜索源码'
    httpClient = None
    host='search.yahoo.co.jp'
    url='/search?p='+urllib.quote(word)+'&aq=-1&oq=&ei=UTF-8&fr=top_ga1_sa&x=wrt'
    try:
        httpClient = httplib.HTTPConnection(host, 80, timeout=30)
        httpClient.request('GET', url,'',randHeader())
     
        #response是HTTPResponse对象
        response = httpClient.getresponse()
        if response.status!=200:raise Exception('访问被限制，请稍后再试')
        #print response.reason
        content=response.read()
        return content
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
def randHeader():
    '返回一个随机的Header'
    head_connection = ['Keep-Alive','close']
    head_accept = ['text/html, application/xhtml+xml, */*']
    head_accept_language = ['zh-CN,fr-FR;q=0.5','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
    head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
    
    
    header = {
        'Connection': head_connection[0],
        'Accept': head_accept[0],
        'Accept-Language': head_accept_language[1],
        'User-Agent': head_user_agent[random.randrange(0,len(head_user_agent))]
    }
    return header
def readTest():
    '读取一段测试文本来测试匹配'
    f=open('test.html')
    return f.read()
    f.close()
    pass
patt=ur'</b>[(（](.*?)[）)]'
#print patt
prog=re.compile(patt,re.M)
def getfurigana(word):
    '获取读音'
    #<b>文華秀麗集</b>(ぶんかしゅうれいしゅう)とは - コトバン
    content=getContent(word)
    #content=readTest()
    #print content
    furigana=None
    if content: furigana=prog.search(content)
    if furigana:
        #print furigana.group()
        return furigana.group(1)
def getList(fileName='list.txt'):
    '读取需要获取读音的单词列表'
    try:
        f=open(fileName)
        List=f.read()
    except Exception as e:
        print '打开 %s 失败'%fileName
    else:
        print '读取 %s 成功'%fileName
        return List.splitlines()
    finally:
        f.close()
def writeData(fileName,data):
    '写入数据'
    try:
        f=open(fileName,'w')
        f.write(data)
    except Exception as e:
        print '写入文件 %s 失败'%fileName
    else:
        print '写入文件 %s 成功'%fileName
    finally:
        f.close()
begin=time.time()
words=getList(fileName)
for i in range(0,len(words)):
    #time.sleep(random.randint(5,10))
    word=words[i]
    print '开始抓取 %s 的读音'%word
    furigana=getfurigana(word)
    if furigana:
        print '%s 的读音为：%s'%(word,furigana)
    else:
        print '%s 的读音抓取失败'%word
        furigana=''
    words[i]+='\t'+str(furigana)
data='\n'.join(words)
print '所有列表抓取完成，开始更新文件 %s'%fileName
writeData('out-'+fileName,data)
begin=time.time()-begin
print '处理 %d 条数据，耗时：%f秒'%(len(words),begin)
