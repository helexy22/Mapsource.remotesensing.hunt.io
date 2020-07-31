# -*- coding:utf-8 -*-

import arcpy
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

Jpath = 'F:/chutu/0_JPG/11广东中/'   
Mxdpath = r"F:\chutu\新建文件夹"

X_code=[1,1,1,1,1,1,1,1]  # Legend location

path = unicode(path,'utf-8')
typewater=["al", "s","u","ch","cals","bo"]

intype_list=["AlgalBloom","Turbidity","COD","Chlorophyll","Class","BlackOdorous"] 
sJpgname_list=["_20191108","_20191108","_20191108","_20191108","_20191108","_20191108","_20191108","_20191108","_20191108","_20191108","_20191108"]

for root, dirs, filenames in os.walk(Mxdpath,topdown=True):
        for f in filenames:          
            mxd_num=filenames.index(f)  
            mxdname=f[:-4]
            for intype in typewater:  
                smxd = os.path.join(path, f)
                mxd = arcpy.mapping.MapDocument(smxd)
                df = arcpy.mapping.ListDataFrames(mxd, '')[0]  
                lyers = arcpy.mapping.ListLayers(mxd)
                n = typewater.index(intype)  
                for lyer in lyers:
                    if "GD_ZF11_" + intype == lyer.name: 
                        lyer.visible = True

                elm = arcpy.mapping.ListLayoutElements(mxd, "PICTURE_ELEMENT", "u")[0]  

                if X_code[mxd_num] == 0:   #左下
                    elm.elementPositionX = df.elementPositionX + 0.1
                    elm.elementPositionY = df.elementPositionY + 0.1
                if X_code[mxd_num] == 1:   #右下
                    elm.elementPositionX = df.elementPositionX + df.elementWidth - elm.elementWidth - 0.1
                    elm.elementPositionY = df.elementPositionY + 0.1
                if X_code[mxd_num] == 2:   #左上
                    elm.elementPositionX = df.elementPositionX + 0.1
                    elm.elementPositionY = df.elementPositionY +df.elementHeight-elm.elementHeight- 0.1

                if f=="全省.mxd":
                    pixel=1200
                if f == "东江流域.mxd":
                    pixel = 1200
                if f == "东江流域.mxd":
                    pixel = 1200
                else:
                    pixel = 600

                intype = intype_list[n]
                arcpy.mapping.ExportToJPEG(mxd, Jpath + mxdname+sJpgname_list[mxd_num]+"_"+intype+ ".jpg",
                                           resolution=pixel)  # 全省的需要重新命名
										   
                print  mxdname+sJpgname_list[mxd_num]+"_"+intype+ ".jpg"

            del mxd
            print (mxd_num + 1)
            print mxdname + "所有参数完毕"
print "进程完整"