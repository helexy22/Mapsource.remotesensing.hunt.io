#!/usr/bin/env python
# encoding: utf-8

import os
import getpass


class KindleExtract():
    def __init__(self):
        pass

    def kindle_check(self):
        """检测Kindle的Clippings文件"""
        username = getpass.getuser()
        kindle_path = ""
        try:
            if 'Kindle' in os.listdir("/media/"+username):
                kindle_path = "/media/"+username+"/Kindle"
                print u"检测到您的Kindle"
            else:
                print u"未检测到您的Kindle设备，请确认插入正确再运行本脚本"
                exit(1)
            if "My Clippings.txt" in os.listdir(kindle_path+"/documents"):
                kindle_path = kindle_path+"/documents/My Clippings.txt"
                print u"检测到标注信息所在文件"
            else:
                print u"未检测到标注信息文件"
                exit(2)
        except Exception, e:
            print e
        return kindle_path


    def get_data(self,kindle_path=None):
        result ={}
        book=[]
        item=[]
        with open(kindle_path) as f:
            for i,cont in enumerate(f.readlines()):
                cont = cont.strip()
                if "==========" == cont:
                    book.append(item)
                    item = []
                    continue
                # if cont != "":
                item.append(cont)

        caption = []
        for i in book:
            caption.append(i[0])
        caption = set(caption)

        tmp ={}
        for i in caption:
            tmp[i] = []

        for i in book:
            tmp[i[0]].append(i[3])

        for i in tmp:
            c = str(i).split(" ")
            title = c[0]
            print title
            author = " ".join(c[1:])
            with open(i.replace("/","·")+".md","w") as out_file:

                out_file.write("# 书名：《《"+title+"》》\n")
                out_file.write("> 作者：《《"+author+"\n")
                for id,item in enumerate(tmp[i]):
                    out_file.write("+ %s%s\n"%(id,item))
               
if __name__ == "__main__":
    ke = KindleExtract()
    ke.get_data(kindle_path="clip.txt")
    
# form http://www.cnblogs.com/taceywong/p/5460215.html
# Not original
