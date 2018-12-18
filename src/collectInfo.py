# -*- coding: UTF-8 -*-
from docx import Document
from workExperience import *
from honor import *


# 采集表导入处理类

class CollectInfo:
    """采集表导入处理类"""  # 类文档字符串

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
        self.major = ""  # 专业

        self.admissionTime = ""  # 入学时间
        self.graduationTime = ""  # 毕业时间
        self.project = ""  # 主修课程
        self.workExperience = []  # 实践经历
        self.schoolExperience = []  # 校园经历
        self.honors = []  # 荣誉
        self.majorSkill = ""  # 专业技能
        self.otherSkill = ""  # 其他技能和证书
        self.hobby = ""  # 兴趣爱好
        self.evaluation = ""  # 自我评价
        # 判断是否为浮点数

    def isNum2(self, value):
        try:
            x = float(value)  # 此处更改想判断的类型
        except TypeError:
            return False
        except ValueError:
            return False
        except Exception as e:
            return False
        else:
            return True

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
                            content = text.replace(" ", "") + "&\n"
                            temp += content  # 添加换行，方便抓取

        self.decodeData(temp)

    def decodeData(self, data):
        # print data
        self.getUserName(data)
        self.getUserNation(data)
        self.getUserBirth(data)
        self.getUserHeight(data)
        self.getUserPhone(data)
        self.getUserPolity(data)
        self.getUserEmail(data)
        self.getUserSchool(data)
        self.getUserAddress(data)
        self.getUserEdu(data)
        self.getUserMajor(data)
        self.getAdmissionTime(data)
        self.getGraduationTime(data)
        self.getPorjects(data)
        self.getWorkExp(data)
        self.getSchoolExp(data)
        self.getHonors(data)
        self.getMajorSkill(data)
        self.getHobby(data)
        self.getEvaluation(data)

    def getPropty(self, text, temp):
        text = text[text.find(temp):]
        if len(text.split('&')) >= 2:
            return text.split('&')[1]
        else:
            return ''

    def getUserName(self, text):
        if text.find('姓名') != -1:
            self.userName = self.getPropty(text, '姓名')

    def getUserNation(self, text):
        if text.find('民族') != -1:
            self.nation = self.getPropty(text, '民族')

    def getUserBirth(self, text):
        if text.find('出生日期') != -1:
            self.birth = self.getPropty(text, '出生日期')

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
        if text.find('email') != -1:
            self.email = self.getPropty(text, 'email')

    def getUserSchool(self, text):
        if text.find('毕业院校') != -1:
            self.school = self.getPropty(text, '毕业院校')

    def getUserAddress(self, text):
        if text.find('住址') != -1:
            self.address = self.getPropty(text, '住址')

    def getUserEdu(self, text):
        if text.find('教育背景') != -1:
            self.edu = self.getPropty(text, '教育背景')

    def getUserMajor(self, text):
        if text.find('专业') != -1:
            self.major = self.getPropty(text[text.find("教育背景"):], '专业')

    def getAdmissionTime(self, text):
        if text.find('入学时间') != -1:
            self.admissionTime = self.getPropty(text[text.find("教育背景"):], '入学时间')

    def getGraduationTime(self, text):
        if text.find('毕业时间') != -1:
            self.graduationTime = self.getPropty(text[text.find("教育背景"):], '毕业时间')

    def getPorjects(self, text):
        if text.find('核心课程') != -1:
            self.project = self.getPropty(text[text.find("教育背景"):], '核心课程')

    def getWorkContent(self, text, temp):
        text = text[text.find(temp) + 7:]
        return text.replace("&", "")

    def getWorkData(self, text, start, end):  # 截取工作经验
        return text[text.find(start):text.find(end)]

    def getWorkData2(self, end):
        if end.find('公司名称') != -1:
            return end[0:end.find('公司名称')]
        else:
            return end

    def getListNum(self, text):  # 循环抓取实践经历
        if text.strip() == '':
            return
        end = text[text.find('公司名称&') + 5:]
        temp = self.getWorkData2(end)
        temp = "公司名称&" + temp
        workExp = WorkExperience()
        workExp.time = self.getPropty(temp, '开始时间')
        workExp.time += self.getPropty(temp, '结束时间')
        workExp.title = self.getPropty(temp, '公司名称')
        workExp.type = self.getPropty(temp, '职位')
        workExp.content = self.getWorkContent(temp, '下面格内按条写')
        if '结束时间' in workExp.time and '职位' in workExp.title \
                and '开始时间' in workExp.type:
            return
        else:
            self.workExperience.append(workExp)
            self.getListNum(end)

    def getWorkExp(self, text):
        start = self.getWorkData(text, '实习经历', '五、校园经历')
        self.getListNum(start)

    def getSchoolData2(self, end):
        if end.find('组织名称') != -1:
            return end[0:end.find('组织名称')]
        else:
            return end

    def getSchoolListNum(self, text):  # 循环抓取实践经历
        if text.strip() == '':
            return
        end = text[text.find('组织名称&') + 5:]
        temp = self.getSchoolData2(end)
        temp = "组织名称&" + temp
        workExp = WorkExperience()
        workExp.time = self.getPropty(temp, '开始时间')
        workExp.time += self.getPropty(temp, '结束时间')
        workExp.title = self.getPropty(temp, '组织名称')
        workExp.type = self.getPropty(temp, '职位')
        workExp.content = self.getWorkContent(temp, '下面格内按条写')
        if '结束时间' in workExp.time and '职位' in workExp.title \
                and '开始时间' in workExp.type:
            return
        else:
            self.schoolExperience.append(workExp)
            self.getSchoolListNum(end)

    def getSchoolExp(self, text):
        start = self.getWorkData(text, '校园经历', '六、奖励及荣誉')
        self.getSchoolListNum(start)

    def getHonorData(self, end):
        # print "====="
        # print end
        if end.find('时间') != -1:
            return end[0:end.find('时间')]
        else:
            return end

    def getHonorListNumb(self, text):
        if text.strip() == '':
            return
        end = text[text.find('时间&') + 3:]
        temp = self.getHonorData(end)
        temp = "时间&" + temp
        honor = Honor()
        honor.time = self.getPropty(temp, '时间')
        honor.content = self.getPropty(temp, '获得荣誉')
        if '获得荣誉' in honor.time:
            return
        else:
            self.honors.append(honor)
            self.getHonorListNumb(end)

    def getHonors(self, text):
        start = self.getWorkData(text, '奖励及荣誉', '七、考取证书')
        self.getHonorListNumb(start)

    def getMajorSkill(self, text):
        start = self.getWorkData(text, '考取证书', '八、兴趣爱好')
        ct4 = self.getPropty(start, '英语四级分数')
        ct6 = self.getPropty(start, '英语六级分数')
        clevel = self.getPropty(start, '计算机级别')
        mj = self.getPropty(start, '职业资格')
        jz = self.getPropty(start, '驾照')
        pth = self.getPropty(start, '普通话')
        other = self.getPropty(start, '其他')
        temp = ""
        if self.isNum2(ct4):
            if int(ct4) > 425:
                temp += "英语四级证书"

        if self.isNum2(ct6):
            if int(ct6) > 425:
                temp += "英语六级证书,"

        if '无' not in clevel:
            temp += clevel + ","

        if '无' not in mj:
            temp += mj + ","

        if '无' not in jz:
            temp += jz + ","

        if '无' not in pth:
            temp += pth + ","

        if '无' not in other:
            temp += other + ","

        self.otherSkill = temp.replace('\n', '')

    def getHobby(self, text):
        start = self.getWorkData(text, '八、兴趣爱好', '九、自我评价')
        self.hobby = start.split("&")[2]
        # print self.hobby

    def getEvaluation(self, text):
        start = text[text.find('九、自我评价'):]
        self.evaluation = start.split("&")[1]
        # print self.evaluation
