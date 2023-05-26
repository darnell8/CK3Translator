# CK3Translator

[English](README.md) | 简体中文

翻译Crusader Kings 3更快的Python脚本

可以快速转换localization里的文件夹内容，支持指定source和target语言。由于没有好的翻译api，翻译功能搁置。

## 配置参数
``` python
# 默认值
enable_translate = False         #是否启用翻译
source_language = "english"      #待转换文件夹
target_language = "simp_chinese" #转换生成文件夹
```

## EXE程序下载地址
仓库的Release里有github action制作的文件
[转换器.exe](https://github.com/darnell8/CK3Translator/releases/latest/download/localizator.exe)

放入mod目录直接运行即可。

## 效果演示
``` yml
# localization\english\abc_english.yml
l_english:

various_challenging_traits_add_decision:0 "Choose challenging ability traits"
various_challenging_traits_add_decision_desc:0 "Perhaps you want to try a different life? There are multiple traits to choose from (currently a total of 10), and you can choose to acquire one of them and gain a unique gaming experience with the support of that trait. The specific bonuses of traits can be viewed in the encyclopedia. (Note: Some traits may significantly increase/decrease the difficulty of the game)"

```

``` yml
# localization\simp_chinese\abc_simp_chinese.yml
l_simp_chinese:

various_challenging_traits_add_decision:0 "选择有挑战性的能力特质"
various_challenging_traits_add_decision_desc:0 "也许你想尝试一下不同的人生？以下多种特质可供你选择（目前总共10种），你可以选择获得其中一个特质，并在该特质加持下获得独特的游玩体验。特质的具体加成可以在百科查看。（注意：某些特质可能会大幅增加/降低游戏难度）"

```

## 笔记
程序已经集成了翻译功能，但是翻译api我只测试了免费的，有一些大型MOD在翻译时由于请求次数过多会导致失败。我在尝试翻译了两个小时后被封禁了ip。也许应该尝试一下使用付费api。或者集成断点续传功能（已初步实现）。

## 问答
#### 断点续传功能是如何实现的？
程序会生成一个`translate_progress.txt`文件并维护已经本地化的文件列表，然后下一次读取会跳过这些文件。
