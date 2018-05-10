# Phone-Handle
计算机网络课程项目——用Python开发的手机手柄

 ![Alt text](https://github.com/Wu-Jiaxin/Phone-Handle/UI_Image/1.png)
# 原理概述
虚拟游戏手柄主要分为电脑端主体程序以及网页部分的html5程序。首先，在电脑端用python创建一个服务端。在手机端用html5获取按键信息，然后通过websocket通道把信息传给电脑端的python。python通过获得的信息来模拟对应的按键。
