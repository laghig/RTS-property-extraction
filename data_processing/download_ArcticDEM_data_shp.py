"""
python code for downloading ArcticDEM stripmap data
"""

import sys
import os
import geopandas as gpd
import wget
import glob
import tarfile


def download_DEMs_shp(shpFile_, saveLoc_):
    """
    Function for downloading ArcticDEM files specified in shaepfile
    Input:
        shpFile_ (string): Path to shapefile
        saveLoc_ (string): Path to download folder location 
    """
    # Make directory if it does not exists
    if not os.path.exists(saveLoc_):
        os.mkdir(saveLoc_)
    # change to directory
    os.chdir(saveLoc_)

    # Read shapefile
    shpData = gpd.read_file(shpFile)
    # Download data using wget
    for file in shpData["fileurl"]:
        print(file)
        wget.download(file)
        print(' ')

def unpacking(saveLoc_, DirExtract_):
    """
    Function for extract tar.gz files
    Input:
        saveLoc_ (string): Path to download folder location
        DirExtract_ (string): Path to folder where to extract the files 

    """
    # Make directory if it does not exists
    if not os.path.exists(DirExtract):
        os.mkdir(DirExtract)
    
    # get all files in folder
    DEMFiles = glob.glob(saveLoc_ + "\*.tar.gz") 

    # extract using tarfile
    for demfile in DEMFiles:
        # get identifier
        name = demfile.split("\\")[-1][:-7]
        print("Extracting: ", name)

        # make directory for extraction
        DirExtractFile = DirExtract_ + "\\" + name
        if not os.path.exists(DirExtractFile):
            os.mkdir(DirExtractFile)

        # open tar.gz file and extract
        with tarfile.open(demfile, 'r') as tar_ref:
            print("Extracting...")
            tar_ref.extractall(DirExtractFile)

# Define shapefile lcoation
shpFile = r"C:.."
saveLoc = r"D:.."
#download_DEMs_shp(shpFile, saveLoc)

# unpacking
DirExtract = r"D:.."
unpacking(saveLoc, DirExtract)

