#-*- coding:utf-8 -*-
'''
Reclsss by Value  base on arcpy spatial
message is content
@Application : Reclass Raster layer
@Para: tif_path,outTif_root
'''
import os
import sys
import arcpy
from arcpy import env
from arcpy.sa import *


def ReclassCls(Cls_Tif,Root):
    arcpy.CheckOutExtension("spatial")
    outReclass= Reclassify(Cls_Tif, "Value",RemapRange([[1, 19, 1], [20, 29, 2], [30, 39, 3],[40, 49, 4], [50, 59, 5], [60, 69, 6]]),"NODATA")
    outReclass.save(os.path.join(Root, "Cls.tif"))
    

def ReclassBo(Uco_Tif,Root):
    arcpy.CheckOutExtension("spatial")
    outReclass= Reclassify(Uco_Tif, "Value",RemapRange([[-1, 12, 0], [12, 14, 1], [14, 500, 2]]),"NODATA")
    outReclass.save(os.path.join(Root, "Bo.tif"))
    

def ReclassWater(Al_Tif,Root):
    arcpy.CheckOutExtension("spatial")
    outReclass= Reclassify(Al_Tif, "Value",RemapRange([[-1, 500, 1]]),"NODATA")
    outReclass.save(os.path.join(Root, "WaterAear.tif"))
    

def ReclassUTIF(Uco_Tif,Root,name):
    arcpy.CheckOutExtension("spatial")
    outReclass= Reclassify(Uco_Tif, "Value",RemapRange([[-50, 0,]]))
    outReclass.save(os.path.join(Root, name))
