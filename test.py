#coding=utf8
try:
	print '开始测试'
	raise Exception('失败')
except Exception as e:
	print e
else:
	print '测试通过'
finally:
	print '我是最后调用'

f=open('1.txt','w')
print f.write('12121212')