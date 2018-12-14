# -*- coding: UTF-8 -*-

from Tkinter import *  # 导入 Tkinter 库
import tkFileDialog
import tkMessageBox
from userInfo import *


import docx
from docx import Document
from docxtpl import DocxTemplate
import re

root = Tk()  # 初始化Tk()

root.title("frame-test")  # 设置窗口标题
root.geometry("300x200")  # 设置窗口大小 注意：是x 不是*


def selectPath():
    path_ = tkFileDialog.askopenfilename(filetypes=[('all files', '.docx')])
    path.set(path_)


def showData():
    if path.get().strip() == '':
        tkMessageBox.showerror('提示', "请选择文件!")
        return
    if path.get().endswith('.doc'):
        tkMessageBox.showerror('提示', "将doc用word转成docx文件!")
        return
    print path.get()
    inf = Info(path.get())
    inf.decodeInfo()
    # 套模板
    # name = '寒冰'
    # template = "D:/pythonSpace/fristProject/src/asset/demo.docx"
    # doc = DocxTemplate(template)  # 对要操作的docx文档进行初始化
    # context = {
    #     'name': name}  # company_name 是存在于1.docx文档里面的变量，就像这样{{company_name}}，直接放在1.docx文件的明确位置就行
    # doc.render(context)  # 这里是有jinjia2的模板语言进行变量的替换，然后便可以在1.docx文档里面看到{{company_name}}变成了World company
    # doc.save("D:/pythonSpace/fristProject/src/asset/out.docx")  # 保存


path = StringVar()
Label(root, text="目标路径:").pack(side=TOP)
Entry(root, textvariable=path).pack(side=TOP, fill=X)
Button(root, text="路径选择", command=selectPath).pack(side=TOP)
Button(root, text="开始导出", command=showData).pack(side=TOP)

root.mainloop()  # 进入消息循环
