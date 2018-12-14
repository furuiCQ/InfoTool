# -*- coding: UTF-8 -*-
from docx import Document


# 简历导入处理类

class Info:
    """简历导入处理类"""  # 类文档字符串

    def __init__(self, path):
        self.path = path

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
                            temp += (text.replace(" ", "") + "\n")  # 添加换行，方便抓取
        print temp
