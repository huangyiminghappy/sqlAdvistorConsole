#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-13 16:51:26
# @Author  : huangyiming (huangyiming@globalegrowejob2016)
# @Link    : ${link}
# @Version : $Id$

import os
from flask import Flask, request, Response,jsonify
from werkzeug.datastructures import Headers

class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        if 'mimetype' not in kwargs and 'contenttype' not in kwargs:
            if response.startswith('<?xml'):
                kwargs['mimetype'] = 'application/xml'
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制 
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods])
        kwargs['headers'] = headers
        return super(MyResponse, self).__init__(response, **kwargs)


app = Flask(__name__,static_url_path='')
app.response_class = MyResponse

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/sqladvisor', methods=['GET'])
def sqladvisor():
    user = request.args.get('user')
    pwd = request.args.get('pwd')
    host = request.args.get('host')
    port = request.args.get('port')
    dbname = request.args.get('dbname')
    sqls = "'"+request.args.get('sqls')+"'"
    print sqls
    logs = '/usr/local/res.log'
#    cmd = '/usr/local/sqladvistor/SQLAdvisor/sqladvisor/sqladvisor -h '+host+' -P '+port+' -u '+user+' -p '+pwd+' -d '+dbname+' -q '+sqls+'-v 1 2>'+logs
#    cmd = '/usr/local/sqladvistor/SQLAdvisor/sqladvisor/sqladvisor -h 10.40.6.187 -P 3306 -u root -p 123456 -d test_xumin -q select+*+from+sbtest1 -v 1 2>/usr/local/res.log'
    cmd = "/usr/local/sqladvistor/SQLAdvisor/sqladvisor/sqladvisor -h "+host+" -P "+ port+" -u "+user+" -p "+pwd+" -d "+dbname+" -q "+sqls +" -v 1 2>"+logs 
    os.popen(cmd).read()
    res = open(logs).read().replace('\n','\r\n')
    return responseto(data=res)

def responseto(message=None, error=None, data=None, **kwargs):
    """ 封装 json 响应
    """
    # 如果提供了 data，那么不理任何其他参数，直接响应 data
    if not data:
        data = kwargs
        data['error'] = error
        if message:
            # 除非显示提供 error 的值，否则默认为 True
            # 意思是提供了 message 就代表有 error
            data['message'] = message
            if error is None:
                data['error'] = True
        else:
            # 除非显示提供 error 的值，否则默认为 False
            # 意思是没有提供 message 就代表没有 error
            if error is None:
                data['error'] = False
    # if not isinstance(data, dict):
    #     data = {'error':True, 'message':'data 必须是一个 dict！'}
    resp = jsonify(data)
    # 跨域设置
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)
