#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QDialog, QVBoxLayout, QComboBox,
    QPushButton, QHBoxLayout, QPlainTextEdit
)
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder
import pyudev

def get_camera_details(device_node):
    context = pyudev.Context()
    for device in context.list_devices(subsystem='video4linux'):
        if device.device_node == device_node:
            details = []
            details.append(f"Device Node: {device.device_node}")
            details.append(f"Product: {device.properties.get('ID_V4L_PRODUCT', 'Unbekannt')}")
            details.append("Alle Eigenschaften:")
            for key, value in device.properties.items():
                details.append(f"{key}: {value}")
            return "\n".join(details)
    return "Keine Details gefunden."

class CameraSelectionDialog(QDialog):
    def __init__(self, cameras, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kameraauswahl")
        layout = QVBoxLayout(self)
        self.combo = QComboBox(self)
        for cam in cameras:
            self.combo.addItem(cam.description(), cam)
        layout.addWidget(self.combo)
        btnLayout = QHBoxLayout()
        okBtn = QPushButton("OK", self)
        cancelBtn = QPushButton("Abbrechen", self)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)
        layout.addLayout(btnLayout)
    
    def getSelectedCamera(self):
        return self.combo.currentData()

class CameraDetailsDialog(QDialog):
    def __init__(self, details, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kameradetails")
        self.resize(500, 400)
        layout = QVBoxLayout(self)
        self.text_edit = QPlainTextEdit(self)
        self.text_edit.setPlainText(details)
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)
        close_btn = QPushButton("Schließen", self)
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Kamera Anwendung")
        self.viewfinder = QCameraViewfinder(self)
        self.setCentralWidget(self.viewfinder)
        self.camera = None
        self.currentCameraInfo = None
        self.createMenu()
    
    def createMenu(self):
        menuBar = self.menuBar()
        camMenu = menuBar.addMenu("Kamera")
        
        selectAction = QAction("Kameraauswahl", self)
        selectAction.triggered.connect(self.selectCamera)
        camMenu.addAction(selectAction)
        
        detailsAction = QAction("Eigenschaften", self)
        detailsAction.triggered.connect(self.showDetails)
        camMenu.addAction(detailsAction)
        
        exitAction = QAction("Beenden", self)
        exitAction.triggered.connect(self.close)
        menuBar.addAction(exitAction)
    
    def selectCamera(self):
        cams = QCameraInfo.availableCameras()
        if not cams:
            return
        dlg = CameraSelectionDialog(cams, self)
        if dlg.exec_() == QDialog.Accepted:
            camInfo = dlg.getSelectedCamera()
            self.currentCameraInfo = camInfo
            self.setWindowTitle(f"Qt Kamera Anwendung - {camInfo.description()}")
            if self.camera:
                self.camera.stop()
            self.camera = QCamera(camInfo)
            self.camera.setViewfinder(self.viewfinder)
            self.camera.start()
    
    def showDetails(self):
        if self.currentCameraInfo is None:
            return
        # Verwende deviceName() als Device Node (z.B. "/dev/video0")
        device_node = self.currentCameraInfo.deviceName()
        details = get_camera_details(device_node)
        dlg = CameraDetailsDialog(details, self)
        dlg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(640, 480)
    win.show()
    sys.exit(app.exec_())
