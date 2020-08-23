# -*- coding: utf-8 -*-
"""
@author: Raymond F. Pauszek III, Ph.D. (2020)
Single-Molecule TIRF Viewer App
"""
from PyQt5.QtWidgets import QApplication, QSizePolicy
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

from smtirf import gui

# ==============================================================================
# MAIN APPLICATION
# ==============================================================================
class SMTirfViewerApp(gui.SMTirfMainWindow):

    def __init__(self, **kwargs):
        super().__init__(title="smTIRF Analysis", **kwargs)



# ==============================================================================
if __name__ == "__main__":
    app = QApplication(sys.argv) if not QApplication.instance() else QApplication.instance()
    win = SMTirfViewerApp()
    win.show()
    sys.exit(app.exec_())