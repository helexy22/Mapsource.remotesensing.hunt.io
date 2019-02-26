import tarfile
import arcpy
import numpy as np 

# # 数数据预处理

tragzfile.extract(file,unzipedfolder) 
# 从压缩文件 tragzfile 中把解压出的文件 file 放到文件夹 unzipedfolder

arcpy.Rename_management(name_fr,name_to)
# 从将文件 name_fr 重命名 name_to

arcpy.gp.CellStatistics_sa(in,out,"MINMUM"；"DATA")
# 获取所有输入图层的最小值

arcpy.gp.Con_sa(in,1,out,"","Value>0")
# 剔除外围的黑边，裁剪出最小的重叠区域

# #云噪声去除

arcpy.gp.CellStatistics_sa(in,out,"MEDIAN"；"DATA")
# 获取所有图层的中值，后面需要采用中值滤去除云噪声
