# -*- coding: UTF-8 -*-
from docx import Document


# 简历导入处理类

class Info:
    """简历导入处理类"""  # 类文档字符串

    def __init__(self, path):
        self.path = path
        self.userName = ""  # 姓名
        self.nation = ""  # 民族
        self.phone = ""  # 电话
        self.email = ""  # 邮箱
        self.address = ""  # 地址
        self.birth = ""  # 出生年月
        self.height = ""  # 身    高
        self.polity = ""  # 政治面貌
        self.school = ""  # 毕业院校
        self.edu = ""  # 学    历

    def decodeInfo(self):
        temp = ""
        lastRow = ""
        doc = Document(self.path)
        for t in doc.tables:
            for r in t.rows:
                for c in r.cells:
                    text = c.text.replace("\t", "")  # 去掉\t 换行不去掉方便抓取关键信息
                    if len(text) > 0:  # 去掉空数据
                        if text != lastRow:
                            lastRow = text
                            self.getUserName(text.replace(" ", "") + "\n")
                            self.getUserNation(text.replace(" ", "") + "\n")
                            temp += (text.replace(" ", "") + "\n")  # 添加换行，方便抓取

    # print temp
    def getPropty(self, text, temp):
        text = text[text.find(temp):]
        return text[text.find(temp):text.find('\n')].replace(temp, "").replace(":", "").replace("：", "")

    def getUserName(self, text):
        if text.find('姓名') != -1:
            self.userName = self.getPropty(text, '姓名')

    def getUserNation(self, text):
        if text.find('民族') != -1:
            self.nation = self.getPropty(text, '民族')

    def getUserBirth(self, text):
        if text.find('出生年月') != -1:
            self.birth = self.getPropty(text, '出生年月')

    def getUserHeight(self, text):
        if text.find('身高') != -1:
            self.height = self.getPropty(text, '身高')
