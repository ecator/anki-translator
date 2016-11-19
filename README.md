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

- src 源语言
- dst 目标语言
- origin 源decks路径
- out 输出的新decks路径
- srcIndex 源语言在字段中的索引，0开始
- dstIndex 目标语言字段索引，一般会被替换成翻译结果
- appid 百度翻译配置appid，由于额度问题请大家替换成自己的
- secretKey 百度翻译secretKey配置，由于额度问题请大家替换成自己的

---
# 参考
- [百度翻译API](http://api.fanyi.baidu.com/api/trans/product/apidoc)