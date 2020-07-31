#-*- coding:utf-8 -*-
'''
@editor:Helexy22
@file:20190527.py
@time:2019-05-27 15:21:51
@Features:ʵ��tifӰ�����������lyr��������Ⱦ
'''
import arcpy
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

mxd_path="D:/181-0404/mxd֮��/"
path=r"C:\gd195\result_ex\bad"  #tif�ļ���

mxd=r"D:\181-0404\mxd֮��\�ޱ���.mxd"
mxd=unicode(mxd,'utf-8')

mxd = arcpy.mapping.MapDocument(mxd)
df = arcpy.mapping.ListDataFrames(mxd,'')[0]
for root,dirs,filenames in os.walk(path,topdown= True):
    for f in filenames:
        if ".tif" in f:
            JPG = os.path.join(path, f)
            arcpy.MakeRasterLayer_management(JPG,f)
            lyr = arcpy.mapping.Layer(f)
            arcpy.mapping.AddLayer(df, lyr)
            intype1_list = ["al.tif", "s.tif", "u.tif", "c.tif", "cals.tif", "bo.tif"]
            for intype in intype1_list:
                if intype in lyr.name:
                    lyrname=intype+".lyr"
                    slyrfile = 'F:/0-Master/�㶫191/ģ������20181227/lyr/�׵�lyr/' + '449-80_20180714_' + lyrname
                    lyrfile = arcpy.mapping.Layer(slyrfile)
                    arcpy.mapping.UpdateLayer(df, lyr, lyrfile, True)
    mxd.save()
    del mxd
