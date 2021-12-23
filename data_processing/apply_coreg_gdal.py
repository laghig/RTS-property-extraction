#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python3.7

"""Module documentation goes here
   
"""
import sys
import os
import gdal 
import glob
import subprocess
from copy import deepcopy



def coreg_gdal(folder):
    """
    apply correction of Icesat data to Arctic DEM dems
    Results are saved as ..._dem_cor.tif
    Input:
        folder(str): path to arcticDEM Folder
    Output:
        None
    """

    # Read files
    demLoc = glob.glob(folder + "\*dem.tif")[0]
    regLoc = glob.glob(folder + "\*reg.txt")[0]
    
    # Check if files exists
    if not os.path.exists(demLoc) and not os.path.exists(regLoc):
        print('File does not exists')
        sys.exit()

    regFile = open(regLoc,'r')
    for line in regFile.readlines():
        if line.startswith('Translation Vector (dz,dx,dy)(m)='):
            dx, dy, dz = [float(i.replace(',', '')) for i in line.split(" ")[-4:-1]]

    print('Shift in dx, dy, dz: ', dx, dy, dz)



    gdal.AllRegister()
        
    # open file
    gdal_obj = gdal.Open(demLoc)
    print('Reading geotiff...', demLoc)

    # Read band
    gdal_band = gdal_obj.GetRasterBand(1)

    # Read Geo transform and projection 
    gdal_geot = list(gdal_obj.GetGeoTransform())
    gdal_geop = gdal_obj.GetProjection()

    # extract array
    gdal_arr = gdal_band.ReadAsArray()

    # apply z-shift
    gdal_arr += dz

    # change geo transform
    gdal_geot[0] = gdal_geot[0] + dx
    gdal_geot[3] = gdal_geot[3] + dy

    print('Saving tif...')

    outfile = demLoc[:-4] + '_cor.tif'  # define save file
    print('Saving to: ', outfile)
    driver = gdal.GetDriverByName("GTiff")
    outdata = driver.Create(outfile, gdal_obj.RasterXSize, gdal_obj.RasterYSize, 1, gdal.GDT_Float32)  # gdt_float32 is the output type
    outdata.SetGeoTransform(tuple(gdal_geot))  # same as input
    outdata.SetProjection(gdal_geop)  # same as input
    outdata.GetRasterBand(1).WriteArray(gdal_arr)
    outdata.GetRasterBand(1).SetNoDataValue(-9999)
    outdata.FlushCache()  # save

    # close dataset
    gdal_obj = None


    # # using gdal_translate - not working?
    # xsize = gdal_obj.RasterXSize
    # ysize = gdal_obj.RasterYSize
    # minx = gdal_geot[0]
    # maxx = minx + xsize * gdal_geot[1]
    # maxy = gdal_geot[3]
    # miny = maxy + ysize * gdal_geot[5]
    # # [-projwin ulx uly lrx lry]
    # target_extent = "{} {} {} {}".format(minx, maxy, maxx, miny)
    # reg_vrt = demLoc[:-4] + ".vrt"
    # VRTdrv = gdal.GetDriverByName("VRT")
    # vds = VRTdrv.CreateCopy(reg_vrt,gdal_obj,0)
    # dgtf = (gdal_geot[0] + 20.,gdal_geot[1],gdal_geot[2],gdal_geot[0] + 20.,gdal_geot[4],gdal_geot[5])
    # vds.SetGeoTransform(dgtf)
    # temp_fp = demLoc[:-4]+"_cor_gdaltrans.tif"
    # # Possible improvements: -co COMPRESS=LZW -co TILED=YES
    # cmd = 'gdal_translate -projwin {} "{}" "{}"'.format(target_extent,reg_vrt,temp_fp)
    # subprocess.call(cmd,shell=True)


if __name__ == '__main__':
    folder = r"D:\Data_WORK\..."

    coreg_gdal(folder)
