# -*- coding: UTF-8 -*-
# http://fanyi.baidu.com/gettts?lan=jp&text=%25E7%25A7%2581%25E3%2581%25AF%25E5%2590%259B%25E3%2581%25AE%25E3%2581%2593%25E3%2581%25A8%25E3%2581%258C%25E5%25A5%25BD%25E3%2581%258D%25E3%2581%25A7%25E3%2581%2599&source=web
import urllib
jp=raw_input('请输入日语：')
url = 'http://fanyi.baidu.com/gettts?lan=jp&text='+urllib.quote(urllib.quote(jp))+'&source=web'

res=urllib.urlopen(url)
data=res.read()
f=open(jp+'.mp3','wb')
f.write(data)
#print data
f.close()
