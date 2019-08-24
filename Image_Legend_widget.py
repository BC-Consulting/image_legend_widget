# -*- coding: utf-8 -*-
"""QGIS Toggle Labels Widget

.. note:: This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

__author__ = '(C) 2019 by GeoProc.com'
__date__ = '24/08/2019'
__copyright__ = 'Copyright 2019, GeoProc.com'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os
import webbrowser
from PIL import Image
from qgis.PyQt.QtCore import (
    QTranslator,
    QCoreApplication,
    QSize
)
from qgis.PyQt.QtGui import (
    QPixmap,
    QIcon
)
from qgis.PyQt.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy
)
from qgis.core import (
    QgsApplication,
    QgsMapLayer
)
from qgis.gui import (
    QgisInterface,
    QgsGui,
    QgsLayerTreeEmbeddedWidgetProvider
)

VERSION = '1.0.0'

class LayerTreeToggleLabelsWidget(QWidget):
    """
    Layer tree widget for displaying image legend in a raster layer
    """

    def __init__(self, layer):
        super().__init__()
        self.layer = layer
        self.my_img = os.path.splitext(layer.source())[0] + '.legend.png'
        if not os.path.exists(self.my_img):
            return

        im = Image.open(self.my_img)
        w, h = im.size
        
        self.setAutoFillBackground(False)
        self.my_pix = QPixmap(self.my_img)
        self.imgleg = QPushButton()
        self.imgleg.setIcon(QIcon(self.my_pix))
        self.imgleg.setCheckable(False)
        self.imgleg.setFlat(True)
        if w >= h:
            self.imgleg.setIconSize(QSize(200,int(200*h/w)))
        else:
            self.imgleg.setIconSize(QSize(int(200*w/h),200))
        self.imgleg.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)

        layout = QHBoxLayout()
        spacer = QSpacerItem(1, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        layout.addWidget(self.imgleg)
        layout.addItem(spacer)
        self.setLayout(layout)

        if self.layer.type() == QgsMapLayer.RasterLayer:
            self.imgleg.clicked.connect(self.showLegend)

    def showLegend(self, active):
        """
        Triggered when the image legend is clicked.
        """
        webbrowser.open('file:///' + self.my_img)
#=========================================================================================

class ImageLegendProvider(QgsLayerTreeEmbeddedWidgetProvider):
    """
    Layer tree provider for Image Legend widgets
    """

    def id(self):  # pylint: disable=missing-docstring
        return 'image_legend'

    def name(self):  # pylint: disable=missing-docstring
        return QCoreApplication.translate('ImageLegendWidget', 'Image Legend')

    def createWidget(self, layer, _):  # pylint: disable=missing-docstring
        return LayerTreeToggleLabelsWidget(layer)

    def supportsLayer(self, layer):  # pylint: disable=missing-docstring
        return layer.type() == QgsMapLayer.RasterLayer
#=========================================================================================

class ImageLegendWidgetPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface: QgisInterface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        super().__init__()
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QgsApplication.locale()
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            '{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        self.provider = None

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        self.provider = ImageLegendProvider()
        QgsGui.layerTreeEmbeddedWidgetRegistry().addProvider(self.provider)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        QgsGui.layerTreeEmbeddedWidgetRegistry().removeProvider(self.provider.id())
        self.provider = None
#=========================================================================================