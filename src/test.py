# -*- coding: UTF-8 -*-


from itchat.content import *
import requests
import json
import itchat


# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    print(info)  # 从好友发过来的消息
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'  # 图灵机器人网址
    data = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": info
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": "efe64759d5db4a19be08e63639249459",
            "userId": "2603f4a4eb089574"
        }
    }
    dat = json.dumps(data)  # 格式化为json
    result = requests.post(api_url, data=dat).json()  # 把data数据发
    print "状态码"
    print result['intent']['code']
    text = (result['results'])[0]['values']['text']
    print text  # 机器人回复给好友的消息
    return text


# 接收到的消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return tuling(msg.text)


# 处理群聊消息
@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:

        itchat.send(u'@%s\u2005: %s' % (msg['ActualNickName'], tuling(msg['Content'])), msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()
