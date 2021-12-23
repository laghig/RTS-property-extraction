#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2.7 and arcpy

"""Module documentation goes here
   
"""
import sys
import os
import glob
import arcpy, arcinfo
from arcpy.sa import Plus


print arcpy.CheckExtension("Spatial")
arcpy.CheckOutExtension("Spatial")


arcpy.env.workspace = r"D:\Data_WORK\processing\workspace"
arcpy.env.overwriteOutput=True
# os.environ['ESRI_SOFTWARE_CLASS']='Professional'


def apply_correction_ArgGIS(folder):
    """
    Apply IceST correction to arcticDEM dems
    Input:
        folder(str): location of arcticDEM strip files
    """
    demLoc = glob.glob(folder + "\*dem.tif")[0]
    regLoc = glob.glob(folder + "\*reg.txt")[0]
    
    # Check if files exists
    if not os.path.exists(demLoc) and not os.path.exists(regLoc):
        print 'Files do not exist'

    regFile = open(regLoc,'r')
    for line in regFile.readlines():
        if line.startswith('Translation Vector (dz,dx,dy)(m)='):
            dz, dx, dy = [float(i.replace(',', '')) for i in line.split(" ")[-4:-1]]

    print 'Shift in dx, dy, dz: ', dx, dy, dz

    arcpy.Shift_management(demLoc, demLoc[:-4] + '_cor_tmp.tif', str(dx),\
                       str(dy)) # need to snap to raster?

    outPlus = Plus( demLoc[:-4] + '_cor_tmp.tif', dz)
    outPlus.save(demLoc[:-4] + '_cor_arcpy.tif')
    arcpy.Delete_management( demLoc[:-4] + '_cor_tmp.tif')




if __name__ == '__main__':
    #folder = r"D:\..."
   
    arcpy.Clip_management('#', '#', '#')

    sys.exit()
    folder_base = r"D:\..."
    DEM_data_folders = glob.glob(folder_base + "\*")
    print(DEM_data_folders)
    for folder in DEM_data_folders:
        apply_correction_ArgGIS(folder)

