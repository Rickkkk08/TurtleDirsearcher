# webDirsearcher

龟速目录扫描器 慎用！！ 

# 1.编写目的

练手项目


# 2.功能

- 自定义URL进行目录扫描
- 可自定义字典
- 可开启`async`模式
- 随机UA

# 3.使用方法

```
-u 指定目标URL
-d 指定字典地址(默认dict.txt)
-c 设置cookie
-a 1 开启协程模式(需要添加参数 1)
```

​	字典默认目录： `/db/xxx.txt`

# 4.结语

## 开发周期	

​	开发周期为三天，第一天编写了总体架构，第二天实现了基本的扫描功能，顺便学习了`async`，第三天完成了async的开发，并对一些细节进行处理

## 困难	

​	开发的时候，被类与类之间的传递，self什么的搞得很懵，但是一次一次的调试过后，对其理解更加深刻了。

​	注意，读取字典的时候需要使用strip()去掉行尾的回车符，否则无法迭代。


# 参考

[1]  https://github.com/maurosoria/dirsearch

[2]  https://github.com/xiaoyaovo/yyzscanner

[3] https://www.bilibili.com/video/BV1Ke411W71L?from=search&seid=15733674525522533428

[4] https://blog.csdn.net/weixin_30770783/article/details/98879140?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control&dist_request_id=1332041.603.16191838166735179&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-2.control

[5]https://blog.csdn.net/weixin_46622106/article/details/111855778
