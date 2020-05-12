## 0x01 简介
​		autotest 是一款基于 Selenium 的 web UI 自动化测试框架，具有良好的自定义性和可扩展性。编程语言选用强大且便捷的 Python。框架采用自动化测试中广受推崇的 Page Object 设计模式，测试人员可以基于此框架进行二次开发，帮助完成自动化测试的工作。

​		框架基于 Python3 开发，针对 Selenium 中常用的定位元素等后续操作进行符合逻辑的封装，使得测试人员专心于测试逻辑上。



## 0x02 目录结构

- 测试代码以羊驼cms后台功能测试为例 : 

```
.
├── README.MD
├── config.ini 	
├── core
│   ├── driver_handler.py
│   ├── logger.py
│   └── utils.py
├── data
│   └── img
│       └── 95.jpg
├── logs
└── main
    ├── run.py
    ├── ytcms_layout.py
    ├── ytcms_link.py
    ├── ytcms_logout.py
    ├── ytcms_page.py
    ├── ytcms_profile.py
    ├── ytcms_site.py
    └── ytcms_tag.py
```

- config.ini : 存放浏览器的选择，测试 domain，是否开启静默模式等选项
- core : 存放框架核心部分 ：
  - driver_handler.py  : 实现 webdriver 的初始化和配置等
  - logger.py : 实现基于 logging 库的日志
  - utils.py ：封装自动化测试常见的操作，可由开发者进行扩展
- data : 存放一些静态资源
- logs : 存放测试文件日志
- main : 存放测试部分主文件 ：
  - run.py ：测试主文件
  - 其他 ：测试页面类文件

## 0x03 框架依赖

- 整个框架的主体基于 Selenium，我们需要下载第三方库 :

```
pip install selenium

- 也可以使用镜像源加速下载
pip install -i https://pypi.douban.com/simple selenium

- 注意: pip 是 python3 对应的 pip，有些操作系统中装了多版本 python，对应的 pip 是 pip3
```

- 需要下载测试浏览器对应版本的 webdriver 驱动程序, 下面提供一个镜像源：

```
http://npm.taobao.org/mirrors/chromedriver

- geckodriver 和 ie 浏览器对应的 webdriver 也可以在里面寻找下载
```

- 下载完后，需要在 config.ini 里面配置下载驱动程序的位置 :

```
eg : Path = /usr/bin/chromedriver
```

## 0x04 其他说明

- 为了统一寻找元素标准，框架代码中寻找特定单个元素的时候，大多使用 xpath 语法进行寻找。
- 每个页面构建一个类，里面的继承关系完全由开发者决定。
- 框架中 data 目录可根据需求存放测试数据
- 代码参考 : https://github.com/StrawberryFlavor/Selenium-Framework 感谢作者开源精神







 