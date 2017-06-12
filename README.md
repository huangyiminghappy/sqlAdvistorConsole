# sqlAdvistorConsole

sqlAdvistor只有一个linux下命令后查询方式，通过在命令行下执行./sqladvisor -h xx  -P xx  -u xx -p 'xx' -d xx -q "sql" -v 1得到sql的优化建议，sqlAdvistorConsole通过python提供http服务，通过html界面的方式输入数据连接等信息，对sql语句进行分析，将展示结果展示在界面上。本项目是sqlAdvistor官方群内第一个公布的界面版工具，效果如图：
![image](https://github.com/huangyiminghappy/sqlAdvistorConsole/blob/master/static/sqladvistor.png)
操作步骤：<br/>
1.根据https://github.com/Meituan-Dianping/SQLAdvisor/blob/master/README.md 配置的
步骤在lunux服务器上安装部署sqladvistor。<br/>

2.在该服务器上安装python环境，目前代码是基于python2.7编写的，设定虚拟环境，切换到2.7并安装pipe，安装request和flask包。<br/>

3.启动server_sqlAdvisor.py脚本即可，注意脚本中有指定端口，默认是9999端口。<br/>
