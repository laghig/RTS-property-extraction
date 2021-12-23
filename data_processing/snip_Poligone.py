import sys
import os
# import geopandas as gpd
import glob
import shutil
import arcpy, arcinfo
import shapefile

print arcpy.CheckExtension("Spatial")
arcpy.CheckOutExtension("Spatial")


arcpy.env.workspace = r"D:\Data_WORK\processing\workspace"
arcpy.env.overwriteOutput=True
# os.environ['ESRI_SOFTWARE_CLASS']='Professional'



def snip_polygone(name, infolder, outfolder, shp_file):

    raster_file = glob.glob(infolder + "\\" + name + "\*_dem_cor_arcpy.tif")[0]
    print raster_file
    
    # raster_name = raster_file.split("\\")[-1][:-17]
    outraster_file = outfolder + "\\" + name + '_polygone.tif'
    print outraster_file
    # Check if files exists
    if not os.path.exists(raster_file) and not os.path.exists(raster_file):
        print 'Files do not exist'

    arcpy.Clip_management(raster_file, "#", outraster_file, shp_file,  "0", "ClippingGeometry")

    # outraster_file.save(shp_file[:-11] + outraster_file)

    # Read shapefile

def read_shp_file(shp_loc):
    """
    Function for reading shapefile without polygone features using pyshp
    Input:
        shp_loc(string): shapefile location
    Output:
        dictionary with elemets in shapefile
    """
    sf = shapefile.Reader(shp_selected)    
    fields = sf.fields[1:]
    field_names = [field[0] for field in fields]
    final_dict = dict(zip(field_names, [[] for i in range(len(fields))]))    
    for r in sf.shapeRecords():  
        new_dict = dict(zip(field_names, r.record))
        for key, value in new_dict.items():
            if key in new_dict and key in final_dict:
                final_dict[key].append(value)    
    return final_dict


if __name__ == '__main__':

    # input: Shapefile & DEM
    shp_file = r"D:\..."
    outfolder = r"D:\..."
    shp_selected = r"D:\..."

    shpData = read_shp_file(shp_selected)
    
    #print(shpData["name"])
    #print(shpData.keys())
    #folder_to_process = [u'SETSM_GE01_20090810_1050410001D80400_1050410001D70000_seg1_2m_v3.0', u'SETSM_W1W1_20140626_10200100309DB600_1020010030D4F000_seg1_2m_v3.0', u'SETSM_W1W1_20140626_102001002EB32300_102001003161BA00_seg1_2m_v3.0', u'SETSM_W1W1_20140520_102001002F05A900_102001002FCE4D00_seg4_2m_v3.0', u'SETSM_W1W1_20140519_102001002D004F00_102001002E071F00_seg1_2m_v3.0', u'SETSM_WV01_20090810_1020010009A0A000_1020010008227C00_seg1_2m_v3.0', u'SETSM_WV01_20110608_1020010014DB2400_10200100123AE500_seg1_2m_v3.0', u'SETSM_WV01_20130801_1020010024504700_10200100229DE400_seg1_2m_v3.0', u'SETSM_WV01_20140621_1020010031E54E00_102001003025DA00_seg1_2m_v3.0', u'SETSM_WV01_20140626_1020010030D4F000_102001002EB32300_seg1_2m_v3.0', u'SETSM_WV01_20140901_10200100329A2F00_10200100320BF100_seg1_2m_v3.0', u'SETSM_WV01_20140813_1020010034A1ED00_10200100319F9400_seg1_2m_v3.0', u'SETSM_WV01_20140808_1020010032147600_10200100323C6D00_seg2_2m_v3.0', u'SETSM_WV01_20140801_1020010031B97700_1020010031E05A00_seg3_2m_v3.0', u'SETSM_WV01_20140807_10200100333A5500_10200100359AEA00_seg1_2m_v3.0', u'SETSM_WV01_20140705_102001003161BA00_10200100309DB600_seg1_2m_v3.0', u'SETSM_WV01_20140506_102001002E458A00_102001002D13B400_seg1_2m_v3.0', u'SETSM_WV01_20140522_102001002F42C200_102001002F2F5500_seg1_2m_v3.0', u'SETSM_WV01_20140519_102001002E950E00_102001002D004F00_seg1_2m_v3.0', u'SETSM_WV01_20140527_102001002F6EF200_102001002FA79B00_seg2_2m_v3.0', u'SETSM_WV01_20140514_102001002F69B000_10200100302DD300_seg1_2m_v3.0', u'SETSM_WV01_20140524_1020010030B92E00_102001002DC00500_seg2_2m_v3.0', u'SETSM_WV01_20140528_102001002F05A900_102001002E873900_seg4_2m_v3.0', u'SETSM_WV01_20140523_102001002DB39200_102001002E071F00_seg1_2m_v3.0', u'SETSM_W1W2_20140801_1020010031B97700_10300100348BE800_seg3_2m_v3.0',  u'SETSM_WV02_20170325_103001006672F500_10300100674F9600_seg1_2m_v3.0', u'SETSM_WV02_20150418_1030010041A40900_1030010041753600_seg1_2m_v3.0', u'SETSM_WV02_20150414_10300100413F3700_10300100411B5D00_seg1_2m_v3.0', u'SETSM_WV02_20110602_103001000B3D3D00_103001000B28C600_seg1_2m_v3.0', u'SETSM_WV02_20110811_103001000D198300_103001000C5D4600_seg1_2m_v3.0', u'SETSM_WV02_20160402_1030010055555D00_1030010052BB9B00_seg1_2m_v3.0', u'SETSM_WV02_20120425_10300100187D2E00_10300100183C0000_seg1_2m_v3.0', u'SETSM_WV02_20120827_103001001B65D800_10300100192A7000_seg4_2m_v3.0', u'SETSM_WV02_20120814_103001001AA06400_103001001A755100_seg10_2m_v3.0', u'SETSM_WV02_20140919_103001003753EC00_1030010038647D00_seg1_2m_v3.0',  u'SETSM_WV02_20140924_1030010037097600_1030010037772B00_seg8_2m_v3.0', u'SETSM_WV02_20140809_10300100348BE800_103001003542D300_seg4_2m_v3.0', u'SETSM_WV02_20140704_10300100337F1400_10300100331F5500_seg1_2m_v3.0', u'SETSM_WV02_20140703_1030010033A84300_1030010032B54F00_seg1_2m_v3.0', u'SETSM_WV02_20140710_1030010033648600_1030010034D4DA00_seg1_2m_v3.0', u'SETSM_W2W2_20100702_1030010005D75A00_1030010006993F00_seg1_2m_v3.0', u'SETSM_W2W2_20110608_103001000B52B400_103001000B881900_seg1_2m_v3.0', u'SETSM_W2W2_20140919_1030010037772B00_1030010038647D00_seg3_2m_v3.0', u'SETSM_W2W2_20140919_1030010037772B00_1030010038647D00_seg1_2m_v3.0', u'SETSM_W2W2_20140703_10300100337F1400_1030010033A84300_seg1_2m_v3.0', u'SETSM_W2W2_20140703_1030010032B54F00_10300100337F1400_seg1_2m_v3.0', u'SETSM_WV03_20150418_104001000A283800_104001000AD3F300_seg1_2m_v3.0']
    folder_to_process = []
    # Download data using wget
    for name_ in shpData["name"]:
        folder_to_process.append(name_)

    #print(len(folder_to_process))

    folder_base = r"D:\ArcticDEM_Data_extracted"
    for foldername in folder_to_process:
         snip_polygone(foldername, folder_base, outfolder, shp_file)