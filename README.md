# Anki批量翻译机
主要是批量翻译Anki导出来的Decks，来源百度翻译

# 运行环境
需要有Python环境，推荐linux系统

# 文件说明
## translator.py
主程序脚本，直接运行本脚本即可批量翻译

```
python translator.py
```

## config.py
脚本配置文件，比如要把英语翻译成中文就需要配置src字段和dst字段，以下是所有字段的说明

- src 源语言，支持语言参考百度翻译API
- dst 目标语言，支持语言请参考百度翻译API
- origin 源decks路径
- out 输出的新decks路径
- srcIndex 源语言在字段中的索引，0开始
- dstIndex 目标语言字段索引，一般会被替换成翻译结果
- appid 百度翻译配置appid，由于额度问题请大家替换成自己的
- secretKey 百度翻译secretKey配置，由于额度问题请大家替换成自己的


## getfurigana.py

批量获取日语的注音，主要针对一些专有名词，原理是从日本雅虎抓取，成功率不是很高。

使用方法也非常简单，只需要输入：

```
python getfurigana.py fileName
```
> fileName 是可选参数，是读取源，utf-8编码，以换行符分隔，脚本将从这个文件中读取需要获取读音的词，默认文件为 list.txt，输出到 out-list.txt 文件。

---
# 参考
- [百度翻译API](http://api.fanyi.baidu.com/api/trans/product/apidoc)