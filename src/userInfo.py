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
                            content = text.replace(" ", "") + "\n"

                            self.getUserName(content)
                            self.getUserNation(content)
                            self.getUserBirth(content)
                            self.getUserHeight(content)
                            self.getUserPhone(content)
                            self.getUserPolity(content)
                            self.getUserEmail(content)
                            self.getUserSchool(content)
                            self.getUserAddress(content)
                            self.getUserEdu(content)

                            temp += content  # 添加换行，方便抓取

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

    def getUserPhone(self, text):
        if text.find('电话') != -1:
            self.phone = self.getPropty(text, '电话')

    def getUserPolity(self, text):
        if text.find('政治面貌') != -1:
            self.polity = self.getPropty(text, '政治面貌')

    def getUserEmail(self, text):
        if text.find('邮箱') != -1:
            self.email = self.getPropty(text, '邮箱')

    def getUserSchool(self, text):
        if text.find('毕业院校') != -1:
            self.school = self.getPropty(text, '毕业院校')

    def getUserAddress(self, text):
        if text.find('住址') != -1:
            self.address = self.getPropty(text, '住址')

    def getUserEdu(self, text):
        if text.find('学历') != -1:
            self.edu = self.getPropty(text, '学历')
