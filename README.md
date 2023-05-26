# CK3Translator

English | [简体中文](README.zh.md)

A python script to translate Crusader Kings 3 faster

You can quickly convert the contents of folders in localization, and support specifying source and target languages. The translation function is on hold because there is no good translation api.

## Configuration parameters
``` python
# Default Value
enable_translate = False         #Whether to enable translation
source_language = "english"      #Folder to be converted
target_language = "simp_chinese" #Convert the generated folder
```

## EXE Download address
There are files made by github action in the Release of the repository.
[localizator.exe](https://github.com/darnell8/CK3Translator/releases/latest/download/localizator.exe)

Just put it in the mod directory and run it directly.

## Effect Demo
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

## Note 
The program has integrated translation, but I only tested the free translation api, some large mods fail when translating due to too many requests. I was banned after two hours of trying to translate. maybe we should try using the paid api. or integrate the breakpoint pass function (which has been implemented initially).

## FAQ
#### How is the breakpoint transfer function implemented?
The program generates a `translate_progress.txt` file and maintains a list of localized files, which are then skipped the next time they are read.
