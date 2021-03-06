#!/usr/bin/python

import matplotlib as mpl
mpl.use('Agg')
import os, datetime, sys, glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.colors as colors
from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1 import ImageGrid
import matplotlib.font_manager as font_manager
from PIL import Image


def int2str(mm):
	if(mm == '01'): ms = 'January'
	if(mm == '02'): ms = 'February'
	if(mm == '03'): ms = 'March'
	if(mm == '04'): ms = 'April'
	if(mm == '05'): ms = 'May'
	if(mm == '06'): ms = 'June'
	if(mm == '07'): ms = 'July'
	if(mm == '08'): ms = 'August'
	if(mm == '09'): ms = 'September'
	if(mm == '10'): ms = 'October'
	if(mm == '11'): ms = 'November'
	if(mm == '12'): ms = 'December'
	return ms




fdate = sys.argv[1]   #(expects format like: 201301)
yyyy = fdate[0:4]
mm = fdate[4:]
ms = int2str(mm)
labeldate = ms+' '+yyyy

imgsize = sys.argv[2]  #(expects 620, 1000, DIY, )

path = '/usr/local/share/fonts/truetype/msttcorefonts/Trebuchet_MS.ttf'
propr = font_manager.FontProperties(fname=path)
path = '/usr/local/share/fonts/truetype/msttcorefonts/Trebuchet_MS_Bold.ttf'
propb = font_manager.FontProperties(fname=path)

if(imgsize == '620'):
	cbar_image = './ANOM.colorbar_620.png'
	cbar_x = 181
	cbar_y = 17.5
	figxsize = 8.62
	figysize = 0.719
	figdpi = 72
	fsiz1 = 12
	fsiz2 = 11
	t1x = 0.310; t1y = 0.678
	t2x = 0.654; t2y = 0.680
	t3x = 0.006; t3y = 0.77
	t4x = 0.910; t4y = 0.77
	t5x = 0.902; t5y = 0.55
	t6x = 0.278; t6y = 0.15
	t7x = 0.495; t7y = 0.15
	t8x = 0.700; t8y = 0.15
	pngfile = "temporary_cbar.png"

if(imgsize == '1000'):
	cbar_image = './ANOM.colorbar_620.png'
	cbar_x = 371
	cbar_y = 17.5
	figxsize = 13.89
	figysize = 0.719
	figdpi = 72
	fsiz1 = 12
	fsiz2 = 11
	t1x = 0.382; t1y = 0.678
	t2x = 0.596; t2y = 0.680
	t3x = 0.004; t3y = 0.77
	t4x = 0.946; t4y = 0.77
	t5x = 0.941; t5y = 0.55
	t6x = 0.363; t6y = 0.15
	t7x = 0.497; t7y = 0.15
	t8x = 0.623; t8y = 0.15
	pngfile = "temporary_cbar.png"

if(imgsize == 'DIY'):
	cbar_image = './ANOM.colorbar_620.png'
	cbar_x = 200
	cbar_y = 90
	figxsize = 8.89
	figysize = 2.44
	figdpi = 72
	fsiz1 = 12
	fsiz2 = 11
	t1x = 0.33; t1y = 0.665
	t2x = 0.67; t2y = 0.664
	t3x = 0.05; t3y = 0.82
	t4x = 0.85; t4y = 0.82
	t5x = 0.84; t5y = 0.63
	t6x = 0.300; t6y = 0.420
	t7x = 0.51; t7y = 0.420
	t8x = 0.71; t8y = 0.420
	pngfile = "temporary_cbar.eps"


fig = plt.figure(figsize=(figxsize,figysize))

# create an axes instance, leaving room for colorbar at bottom.
ax1 = fig.add_axes([0.0,0.0,1.0,1.0], axisbg='#F5F5F5')
ax1.set_frame_on(False)
ax1.set_xticks([])
ax1.set_xticklabels([])
ax1.set_yticks([])
ax1.set_yticklabels([])


#Add the colorbar
cbar_orig = Image.open(cbar_image)
bbox = (1,1,257,12)
cbar_orig = cbar_orig.crop(bbox)
old_size = cbar_orig.size
new_size = (old_size[0]+2,old_size[1]+2)
cbar_im = Image.new("RGB", new_size)
cbar_im.paste(cbar_orig, ((new_size[0]-old_size[0])/2,
                      (new_size[1]-old_size[1])/2))
#cbar_im = ImageOps.expand(cbar_orig,border=1,fill='#505050')
# We need a float array between 0-1, rather than
# a uint8 array between 0-255 for the logo
cbar_im = np.array(cbar_im).astype(np.float) / 255
fig.figimage(cbar_im, cbar_x, cbar_y)



dval = "Difference from average temperature"
plt.text(t1x, t1y, dval, fontproperties=propb, size=fsiz1, color='#333333')
plt.text(t2x, t2y, "($^\circ$F)", fontproperties=propr, size=fsiz1, color='#333333')

plt.text(t3x, t3y, labeldate, fontproperties=propr, size=fsiz2, color='#8D8D8D')
plt.text(t4x, t4y, 'NOAA EVL', fontproperties=propr, size=fsiz2, color='#8D8D8D')
plt.text(t5x, t5y, 'Data: NCDC', fontproperties=propr, size=fsiz2, color='#8D8D8D')

plt.text(t6x, t6y, "-11", fontproperties=propr, size=fsiz2, color='#333333')
plt.text(t7x, t8y, "0", fontproperties=propr, size=fsiz2, color='#333333')
plt.text(t8x, t8y, "11", fontproperties=propr, size=fsiz2, color='#333333')



if(imgsize != 'DIY'):
	plt.savefig(pngfile, dpi=figdpi, orientation='landscape', bbox_inches='tight', pad_inches=0.0)

if(imgsize == 'DIY'):
	plt.savefig(pngfile, dpi=figdpi, orientation='portrait', bbox_inches='tight', pad_inches=0.0)
