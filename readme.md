![](icon.png) 
## *ImageLegend_widget*: A QGIS layer tree (Legend) widget for displaying image legend in a raster layer.

V1.4 - 26 November 2019

This widget works only on QGIS version >= 3.4.

This QGIS layer tree widget adds an "Image Legend" entry into the Legend tab of a raster layer properties.

![](wil2.jpg)

In order to work correctly this widget requires a specific <a href="https://en.wikipedia.org/wiki/Sidecar_file" target="_blank">sidecar</a> file (specially named file) for the selected raster. Two cases are dealt with: 1) one legend sidecar file per raster or 2) a common legend file for all rasters in the directory that do not have their own legend sidecar file.

**Case 1 - One legend sidecar file per raster file:**

* Legend file must be either a PNG or JPG image file. No other format accepted!
* Legend file must be named as `my_map.legend.png` or `my_map.legend.jpg` where `my_map` is the name as the original raster file, without extension, and `.legend.png` or `.legend.jpg` is sidecar identity.
* Legend file must be in same directory as raster file.

**Case 2 - Common legend file for rasters in folder:**

* Common legend file must be either a PNG or JPG image file. No other format accepted!
* Common legend file must be named as `pref.legendcommon.png` or `pref.legendcommon.jpg` where `pref` is a dummy name, and `.legendcommon.png` or `.legendcommon.jpg` must be as it is.
* Common legend file must be in same directory as raster files referencing it.
* One and only one `.legendcommon.png` or `.legendcommon.jpg` can exist in the given directory. If more than one file exists then the one displayed is undefined.

User manual [here](https://www.geoproc.com/be/image_legend_widget.htm)<br>
GeoProc.com plugins repository for QGIS [here](https://www.geoproc.com/be/plugins.xml)

Distributed under the GPL licence.
