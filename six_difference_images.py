import sys
import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal, osr
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm
from mpl_toolkits.axes_grid1 import make_axes_locatable


# read some geotiff data
img1 = r"D:\..."
img2 = r"D:\..."
img3 = r"D:\..."
img4 = r"D:\..."
img5 = r"D:\..."
img6 = r"D:\..."

gdal_obj1 = gdal.Open(img1)
gdal_band1 = gdal_obj1.GetRasterBand(1)
gdal_arr1 = gdal_band1.ReadAsArray()

# get the existing coordinate system
old_cs= osr.SpatialReference()
old_cs.ImportFromWkt(gdal_obj1.GetProjectionRef())

# create the new coordinate system
wgs84_wkt = """
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.01745329251994328,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]"""
new_cs = osr.SpatialReference()
new_cs .ImportFromWkt(wgs84_wkt)

# create a transform object to convert between coordinate systems
transform = osr.CoordinateTransformation(old_cs,new_cs)

#get the point to transform, pixel (0,0) in this case
width = gdal_obj1.RasterXSize
height = gdal_obj1.RasterYSize
gt = gdal_obj1.GetGeoTransform()
minx = gt[0]
miny = gt[3] + width*gt[4] + height*gt[5] 

#get the coordinates in lat long
latlong = transform.TransformPoint(minx,miny)

latlong1 = transform.TransformPoint(gt[0], gt[3])


print(latlong)
print(latlong1)

gdal_obj2 = gdal.Open(img2)
gdal_band2 = gdal_obj2.GetRasterBand(1)
gdal_arr2 = gdal_band2.ReadAsArray()

gdal_obj3 = gdal.Open(img3)
gdal_band3 = gdal_obj3.GetRasterBand(1)
gdal_arr3 = gdal_band3.ReadAsArray()

gdal_obj4 = gdal.Open(img4)
gdal_band4 = gdal_obj4.GetRasterBand(1)
gdal_arr4 = gdal_band4.ReadAsArray()

gdal_obj5 = gdal.Open(img5)
gdal_band5 = gdal_obj5.GetRasterBand(1)
gdal_arr5 = gdal_band5.ReadAsArray()



gdal_obj6 = gdal.Open(img6)
gdal_band6 = gdal_obj6.GetRasterBand(1)
gdal_arr6 = gdal_band6.ReadAsArray()

old_cs6= osr.SpatialReference()
old_cs6.ImportFromWkt(gdal_obj6.GetProjectionRef())

# create the new coordinate system
wgs84_wkt = """
GEOGCS["WGS 84",
    DATUM["WGS_1984",
        SPHEROID["WGS 84",6378137,298.257223563,
            AUTHORITY["EPSG","7030"]],
        AUTHORITY["EPSG","6326"]],
    PRIMEM["Greenwich",0,
        AUTHORITY["EPSG","8901"]],
    UNIT["degree",0.01745329251994328,
        AUTHORITY["EPSG","9122"]],
    AUTHORITY["EPSG","4326"]]"""
new_cs6 = osr.SpatialReference()
new_cs6.ImportFromWkt(wgs84_wkt)

# create a transform object to convert between coordinate systems
transform6 = osr.CoordinateTransformation(old_cs6,new_cs6)

#get the point to transform, pixel (0,0) in this case
width6 = gdal_obj6.RasterXSize
height6 = gdal_obj6.RasterYSize
gt6 = gdal_obj6.GetGeoTransform()
minx6 = gt6[0]
miny6 = gt6[3] + width6*gt6[4] + height6*gt6[5] 

#get the coordinates in lat long
latlong5 = transform.TransformPoint(minx6,miny6)

latlong6 = transform6.TransformPoint(gt6[0], gt6[3])



# get geo transfrom
# geot1 = gdal_obj1.GetGeoTransform()
geot2 = gdal_obj2.GetGeoTransform()
geot3 = gdal_obj3.GetGeoTransform()
geot4 = gdal_obj4.GetGeoTransform()
geot5 = gdal_obj5.GetGeoTransform()
#geot6 = gdal_obj6.GetGeoTransform()


# get dimensions
[lat, lon] = gdal_arr1.shape
[lat6, lon6] = gdal_arr6.shape

#print(lon, lat)
#print(gt[0:10])


# generate array with lats lons
corner_lat = latlong1[1]
corner_lon = latlong1[0]
post_lat = float(2)/111320
post_lon = 0.002*np.cos(latlong[1])/360
lats = np.arange(corner_lat, corner_lat + post_lat * lat, step=post_lat)
lons = np.arange(corner_lon, corner_lon + post_lon * lon, step=post_lon)

corner_lat6 = latlong6[1]
corner_lon6 = latlong6[0]
post_lat = float(2)/111320
post_lon = 0.002*np.cos(latlong5[1])/360
lats6 = np.arange(corner_lat6, corner_lat6 + post_lat * lat6, step=post_lat)
lons6 = np.arange(corner_lon6, corner_lon6 + post_lon * lon6, step=post_lon)



# print(post_lat)
# print(post_lon)

cut_x1 =65
cut_x2 = 145
cut_y1 = 45
cut_y2 = 145

#print(lats[0:10])



cut1 = gdal_arr1[cut_x1:cut_x2, cut_y1:cut_y2]
cut2 = gdal_arr2[cut_x1:cut_x2, cut_y1:cut_y2]
cut3 = gdal_arr3[cut_x1:cut_x2, cut_y1:cut_y2]
cut4 = gdal_arr4[cut_x1:cut_x2, cut_y1:cut_y2]
cut5 = gdal_arr5[cut_x1:cut_x2, cut_y1:cut_y2]
cut6 = gdal_arr6[cut_x1:cut_x2, cut_y1:cut_y2]



#Plot the 4 images

font = {'family': 'sans-serif',
        'color':  'black',
        'weight': 600,
        'size': 8,
        }

colorbar =  "RdYlBu" #"RdYlGn" "jet"  "RdYlBu"


fig = plt.figure(figsize=(11,7))
ax = fig.add_subplot(111)    # The big subplot

ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

fig.subplots_adjust(wspace=0.4, hspace = 0)


# Turn off axis lines and ticks of the big subplot
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_color('none')
ax.tick_params(labelcolor='w', top=False, bottom=False, left=False, right=False)


axlist = [ax1,ax2,ax3,ax4, ax5, ax6]


# Suplot 1
first = ax1.imshow(cut1, vmin=-8,vmax=6, cmap= colorbar)

fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax1.transData,
                           10, '20 m', 'lower right', 
                           pad=0.2,
                           color='black',
                           frameon=False,
                           size_vertical=0.3,
                           fontproperties=fontprops)

ax1.add_artist(scalebar)
# Changing x ticks
x_ticks = ax1.get_xticks()
x_loc = []
for j in range(len(x_ticks)-1):
     x_loc.append(x_ticks[j+1])
     x_ticks[j+1] = round(lons[int(x_ticks[j+1])], 4)

ax1.set_xticks(x_loc[1:-1:2])
ax1.set_xticklabels(x_ticks[1:-1], fontdict=font)

# Changing y ticks
y_ticks = ax1.get_yticks()
y_loc = []
for j in range(len(y_ticks)-1):
     y_loc.append(y_ticks[j+1])
     y_ticks[j+1] = round(lats[int(y_ticks[j+1])], 4)

ax1.set_yticks(y_loc[1:-1:2])
ax1.set_yticklabels(y_ticks[1:-1], fontdict=font)


 # set labels
# ax1.set_xlabel('Longitude ', fontsize=10, weight='bold', labelpad=20)
# ax1.set_ylabel('Latitude ', fontsize=10, weight='bold', labelpad=20)
# ax1.set_title('ArcticDEM 2009-2011', fontsize=14, weight='bold')
ax1.set_title("ArcticDEM 2009-2010")



# Subplot 2
second = ax2.imshow(cut2, vmin=-8,vmax=6, cmap= colorbar)

fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax2.transData,
                           10, '20 m', 'lower right', 
                           pad=0.2,
                           color='black',
                           frameon=False,
                           size_vertical=0.3,
                           fontproperties=fontprops)

ax2.add_artist(scalebar)
# Changing x ticks
x_ticks = ax2.get_xticks()
x_loc = []
for j in range(len(x_ticks)-1):
     x_loc.append(x_ticks[j+1])
     x_ticks[j+1] = round(lons[int(x_ticks[j+1])], 4)

ax2.set_xticks(x_loc[1:-1:2])
ax2.set_xticklabels(x_ticks[1:-1], fontdict=font)

# Changing y ticks
y_ticks = ax2.get_yticks()
y_loc = []
for j in range(len(y_ticks)-1):
     y_loc.append(y_ticks[j+1])
     y_ticks[j+1] = round(lats[int(y_ticks[j+1])], 4)

ax2.set_yticks(y_loc[1:-1:2])
ax2.set_yticklabels(y_ticks[1:-1], fontdict=font)


 # set labels
# ax2.set_xlabel('Longitude ', fontsize=10, weight='bold', labelpad=10)
# ax2.set_ylabel('Latitude ', fontsize=10, weight='bold', labelpad=10)
# ax2.set_title('ArcticDEM 2009-2012', fontsize=14, weight='bold') 
ax2.set_title("ArcticDEM 2009-2011")

# Suplot 3
third = ax3.imshow(cut3, vmin=-8,vmax=6, cmap= colorbar)

fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax3.transData,
                           10, '20 m', 'lower right', 
                           pad=0.2,
                           color='black',
                           frameon=False,
                           size_vertical=0.3,
                           fontproperties=fontprops)

ax3.add_artist(scalebar)
# Changing x ticks
x_ticks = ax3.get_xticks()
x_loc = []
for j in range(len(x_ticks)-1):
     x_loc.append(x_ticks[j+1])
     x_ticks[j+1] = round(lons[int(x_ticks[j+1])], 4)

ax3.set_xticks(x_loc[1:-1:2])
ax3.set_xticklabels(x_ticks[1:-1], fontdict=font)

# Changing y ticks
y_ticks = ax3.get_yticks()
y_loc = []
for j in range(len(y_ticks)-1):
     y_loc.append(y_ticks[j+1])
     y_ticks[j+1] = round(lats[int(y_ticks[j+1])], 4)

ax3.set_yticks(y_loc[1:-1:2])
ax3.set_yticklabels(y_ticks[1:-1], fontdict=font)


 # set labels
# ax3.set_xlabel('Longitude ', fontsize=10, weight='bold', labelpad=20)
# ax3.set_ylabel('Latitude ', fontsize=10, weight='bold', labelpad=20)
# ax3.set_title('ArcticDEM 2009-2013', fontsize=14, weight='bold') 
ax3.set_title("ArcticDEM 2009-2012")


# Subplot 4
fourth = ax4.imshow(cut4, vmin=-8,vmax=6, cmap= colorbar)

fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax4.transData,
                           10, '20 m', 'lower right', 
                           pad=0.2,
                           color='black',
                           frameon=False,
                           size_vertical=0.3,
                           fontproperties=fontprops)

ax4.add_artist(scalebar)
# Changing x ticks
x_ticks = ax4.get_xticks()
x_loc = []
for j in range(len(x_ticks)-1):
     x_loc.append(x_ticks[j+1])
     x_ticks[j+1] = round(lons[int(x_ticks[j+1])], 4)

ax4.set_xticks(x_loc[1:-1:2])
ax4.set_xticklabels(x_ticks[1:-1], fontdict=font)

# Changing y ticks
y_ticks = ax4.get_yticks()
y_loc = []
for j in range(len(y_ticks)-1):
     y_loc.append(y_ticks[j+1])
     y_ticks[j+1] = round(lats[int(y_ticks[j+1])], 4)

ax4.set_yticks(y_loc[1:-1:2])
ax4.set_yticklabels(y_ticks[1:-1], fontdict=font) #, rotation='vertical'


 # set labels
# ax4.set_xlabel('Longitude ', fontsize=10, weight='bold', labelpad=20)
# ax4.set_ylabel('Latitude ', fontsize=10, weight='bold', labelpad=20)
# ax4.set_title('ArcticDEM 2009-2014', fontsize=14, weight='bold') 
ax4.set_title("ArcticDEM 2009-2013")


# Suplot 5
fifth = ax5.imshow(cut5, vmin=-8,vmax=6, cmap= colorbar)

fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax5.transData,
                           10, '20 m', 'lower right', 
                           pad=0.2,
                           color='black',
                           frameon=False,
                           size_vertical=0.3,
                           fontproperties=fontprops)

ax5.add_artist(scalebar)
# Changing x ticks
x_ticks = ax5.get_xticks()
x_loc = []
for j in range(len(x_ticks)-1):
     x_loc.append(x_ticks[j+1])
     x_ticks[j+1] = round(lons[int(x_ticks[j+1])], 4)

ax5.set_xticks(x_loc[1:-1:2])
ax5.set_xticklabels(x_ticks[1:-1], fontdict=font)

# Changing y ticks
y_ticks = ax5.get_yticks()
y_loc = []
for j in range(len(y_ticks)-1):
     y_loc.append(y_ticks[j+1])
     y_ticks[j+1] = round(lats[int(y_ticks[j+1])], 4)

ax5.set_yticks(y_loc[1:-1:2])
ax5.set_yticklabels(y_ticks[1:-1], fontdict=font)


 # set labels
# ax1.set_xlabel('Longitude ', fontsize=10, weight='bold', labelpad=20)
# ax1.set_ylabel('Latitude ', fontsize=10, weight='bold', labelpad=20)
# ax1.set_title('ArcticDEM 2009-2011', fontsize=14, weight='bold')
ax5.set_title("ArcticDEM 2009-2014")


# Suplot 6
sixth = ax6.imshow(cut6, vmin=-8,vmax=6, cmap= colorbar)

fontprops = fm.FontProperties(size=8)
scalebar = AnchoredSizeBar(ax6.transData,
                           10, '20 m', 'lower right', 
                           pad=0.2,
                           color='black',
                           frameon=False,
                           size_vertical=0.3,
                           fontproperties=fontprops)

ax6.add_artist(scalebar)
# Changing x ticks
x_ticks = ax6.get_xticks()
x_loc = []
for j in range(len(x_ticks)-1):
     x_loc.append(x_ticks[j+1])
     x_ticks[j+1] = round(lons6[int(x_ticks[j+1])], 4)

ax6.set_xticks(x_loc[1:-1:2])
ax6.set_xticklabels(x_ticks[1:-1], fontdict=font)

# Changing y ticks
y_ticks = ax6.get_yticks()
y_loc = []
for j in range(len(y_ticks)-1):
     y_loc.append(y_ticks[j+1])
     y_ticks[j+1] = round(lats6[int(y_ticks[j+1])], 4)

ax6.set_yticks(y_loc[1:-1:2])
ax6.set_yticklabels(y_ticks[1:-1], fontdict=font)


 # set labels
# ax1.set_xlabel('Longitude ', fontsize=10, weight='bold', labelpad=20)
# ax1.set_ylabel('Latitude ', fontsize=10, weight='bold', labelpad=20)
# ax1.set_title('ArcticDEM 2009-2011', fontsize=14, weight='bold')
ax6.set_title("Arc/TanDEM 2009-2017")


cbar= fig.colorbar(first, ax= axlist, fraction = 0.03)
cbar.set_label('Height difference', rotation=270, fontsize =14, labelpad = 15)

ax.set_title('RTS 14', fontsize=18, weight='bold')
fig.text(0.48, 0.1, 'Longitude', ha='center', va='center', fontsize=14, weight='bold')
fig.text(0.013, 0.5, 'Latitude', ha='center', va='center', rotation='vertical', fontsize=14, weight='bold')

#ax.set_xlabel('Longitude ', fontsize=10, weight='bold')
#ax.set_ylabel('Latitude ', fontsize=10, weight='bold')
#fig.tight_layout()
plt.savefig(r"D:\...")
plt.show()
