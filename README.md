# Phone-Handle
计算机网络课程项目——用Python开发的手机手柄
 
# 原理概述
虚拟游戏手柄主要分为电脑端主体程序以及网页部分的html5程序。首先，在电脑端用python创建一个服务端。在手机端用html5获取按键信息，然后通过websocket通道把信息传给电脑端的python。python通过获得的信息来模拟对应的按键。

# 运行方法
1.将手机与电脑连接同一WIFI，在cmd命令行里输入ipconfig查看自己的IPV4地址，将此代码中的IP地址改为你自己的IP地址。
2.先运行websocket.py，再运行inedx.py，再在手机浏览器中输入上述IP地址加端口号。
