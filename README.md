<div align="center">  

# Tunic文字生成器

<img alt="LOGO" src="https://github.com/passerbyzhao/TunicCharacterGenerator/blob/f63b5fea3c09def001d0d7a7d1a456bb3f1e0b2e/icon.png" width=108 height=185/>

把英文单词转换成TUNIC文字
</div>

<div align="left">  

# 简介
虽然我没玩过TUNIC，是看的大仙的视频云的游戏，但是我还是很喜欢小狐狸。  

本程序是一个简单的英文原文到转TUNIC中狐狸文字的转换程序。
使用turtle库绘图，eng_to_ipa库获取单词音标。
输入为英文单词或句子，输出为TUNIC文字的图片。
只支持单向转换，想读懂输出的符号请学习TUNIC文字。
可以去看 [旭日之记忆](https://space.bilibili.com/12994) 
的[教学视频](https://www.bilibili.com/video/BV1n541117Pi?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=31639fcfc39fb9a40438489d06a52319) 。


需要额外安装[eng_to_ipa](https://github.com/mphilli/English-to-IPA/tree/master)
和[ghostscript](https://pypi.org/project/python3-ghostscript/ )。

每次运行都会弹出turtle绘图窗口，~~忍受巨慢的绘图过程~~欣赏文字书写的过程。  
目前无UI，只能用命令行运行。  
有时候输出图片右侧会有黑边。正在排查。

## 依赖
[eng_to_ipa](https://github.com/mphilli/English-to-IPA/tree/master)  
[ghostscript](https://pypi.org/project/python3-ghostscript/ )  

## 效果
> - 原文：banana
> - 输入：`python main.py --sentence banana`
> - 输出：  
> ![image](https://github.com/passerbyzhao/TunicCharacterGenerator/blob/2a2ffe82b32658e098b76e15e0428572839aa581/img/banana.jpg)

> - 原文：Hello world!
> - 输入：`python main.py --sentence "Hello World!" --fontsize 20 -c blue`
> - 输出：  
> ![image](https://github.com/passerbyzhao/TunicCharacterGenerator/blob/2a2ffe82b32658e098b76e15e0428572839aa581/img/HelloWorld.jpg)

> - 原文：How are you? Fine, thank you. And you? I'm fine too.
> - 输入：`python main.py --sentence "How are you? Fine, thank you. And you? I'm fine too." --mode handwriting`
> - 输出：  
> ![image](https://github.com/passerbyzhao/TunicCharacterGenerator/blob/2a2ffe82b32658e098b76e15e0428572839aa581/img/HowAreYou.jpg)
 
> - 原文：Tunic Character Generator
> - 输入：` python main.py --sentence "Tunic Character Generator" --fontsize 13`
> - 输出：  
> ![image](https://github.com/passerbyzhao/TunicCharacterGenerator/blob/2a2ffe82b32658e098b76e15e0428572839aa581/img/TunicCharacterGenerator.jpg)

## *注意*
- 原文中如果有空格的话需要用英文双引号将原文括起来。  
- <font color=Yellow>**不支持**</font>除了26个字母、英文逗号、句号、
感叹号、问号、单引号和空格之外的字符！（数字也不支持）  
- 能转换的单词取决于eng_to_ipa模块能否返回输入单词的音标。  

## 可用参数
`--sentence`  想要翻译的原文 有空格的话请用英文双引号括起来  
`-p --path`   输出图片保存路径 默认为根目录  
`-n --name`   输出图片的名称 默认为result  
`--fontsize`  输出符号的大小 默认为15  
`--pensize`   输出符号的笔画粗细 默认为4   
`-m --mode`   输出模式 默认为`formal` 可选`handwriting`和`original` 
三种模式的差别请看[教学视频](https://www.bilibili.com/video/BV1n541117Pi?spm_id_from=333.1007.top_right_bar_window_default_collection.content.click&vd_source=31639fcfc39fb9a40438489d06a52319)   
`-s --save`   是否保存结果图片 默认为保存  


###### <font color=Black>Tunic Character Generator v0.2</font>
</div>
