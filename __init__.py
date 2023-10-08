# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DiscordRPC
                                 A QGIS plugin
 QGIS plugin that enables displaying a Rich Presence in Discord
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-05-27
        copyright            : (C) 2023 by Ahhj93
        email                : /
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = "Ahhj93"
__license__ = "GPL 2.0"

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DiscordRPC class from file DiscordRPC.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .discord_rpc import DiscordRPC
    return DiscordRPC(iface)
