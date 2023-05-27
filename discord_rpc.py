# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DiscordRPC
                                 A QGIS plugin
 Plugin for have Discord Rich Presence
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-05-27
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Ryse93
        email                : ryse93yt@outlook.fr
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QTimer
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .discord_rpc_dialog import DiscordRPCDialog
import os.path

from qgis.core import QgsProject
import qgis.core

import time
from pypresence import Presence

class DiscordRPC:
    def __init__(self, iface):
        self.iface = iface
        self.RPC = None
        self.timer = None
        self.start_time = int(time.time())  # Temps de début initial

    def initGui(self):
        # Initialisation de l'instance pypresence.Presence
        self.RPC = Presence('1112020776099516456')
        self.RPC.connect()

        # Démarrer le minuteur pour mettre à jour RPC toutes les 5 secondes
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_rpc)
        self.timer.start(5000)  # 5000 millisecondes = 5 secondes

    def unload(self):
        if self.RPC is not None:
            self.RPC.close()

        # Arrêter le minuteur lorsque le plugin est déchargé
        if self.timer is not None:
            self.timer.stop()


    def update_rpc(self):
        # Obtenez le nom du fichier en cours de modification
        project = QgsProject.instance()
        filename = os.path.basename(project.fileName())

        # Vérifier si le fichier a été modifié ou non
        if filename != "":
            state = f"Editing {filename}"
        else:
            state = "Not editing"

        # Mise à jour de RPC avec le nom du fichier dans l'état (state)
        self.RPC.update(
            details = f"QGIS Desktop {get_qgis_version()}",
            state = state,
            start = self.start_time,
            large_image = "logo",
            large_text = "QGIS",
        )

def get_qgis_version():
    return qgis.core.Qgis.QGIS_VERSION