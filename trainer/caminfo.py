#!/usr/bin/env python3
import wx
import pyudev

class CameraSelectionDialog(wx.Dialog):
    def __init__(self, parent, cameras):
        super().__init__(parent, title="Kameraauswahl", size=(300, 150))
        self.cameras = cameras
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(panel, label="Wähle eine Kamera:")
        vbox.Add(label, flag=wx.ALL, border=10)
        choices = [
            f"{dev.device_node}: {dev.properties.get('ID_V4L_PRODUCT', 'Unbekannt')}"
            for dev in cameras
        ]
        self.choice = wx.Choice(panel, choices=choices)
        if choices:
            self.choice.SetSelection(0)
        vbox.Add(self.choice, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        ok_btn = wx.Button(panel, wx.ID_OK, label="OK")
        cancel_btn = wx.Button(panel, wx.ID_CANCEL, label="Abbrechen")
        hbox.Add(ok_btn, flag=wx.RIGHT, border=5)
        hbox.Add(cancel_btn, flag=wx.LEFT, border=5)
        vbox.Add(hbox, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.on_ok, ok_btn)

    def on_ok(self, event):
        if self.choice.GetSelection() == wx.NOT_FOUND:
            wx.MessageBox("Keine Kamera ausgewählt.", "Fehler", wx.OK | wx.ICON_ERROR)
        else:
            self.EndModal(wx.ID_OK)

    def GetSelectedCamera(self):
        idx = self.choice.GetSelection()
        if idx != wx.NOT_FOUND:
            return self.cameras[idx]
        return None

class CameraDetailsDialog(wx.Dialog):
    def __init__(self, parent, details):
        super().__init__(parent, title="Kameradetails", size=(500, 400))
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.text_ctrl = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.text_ctrl.SetValue(details)
        vbox.Add(self.text_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        close_btn = wx.Button(panel, wx.ID_OK, label="Schließen")
        vbox.Add(close_btn, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=10)
        panel.SetSizer(vbox)
        self.Bind(wx.EVT_BUTTON, self.on_close, close_btn)

    def on_close(self, event):
        self.EndModal(wx.ID_OK)

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected_device = None
        self.InitUI()

    def InitUI(self):
        self.SetTitle("Kamera Anwendung")
        self.SetSize((500, 400))
        self.CreateMenuBar()
        self.Show(True)

    def CreateMenuBar(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.ID_EXIT, "Beenden", "Programm beenden")
        menubar.Append(fileMenu, "&Datei")
        camMenu = wx.Menu()
        selectItem = camMenu.Append(wx.ID_ANY, "Kameraauswahl", "Kamera auswählen")
        propItem = camMenu.Append(wx.ID_ANY, "Eigenschaften", "Kameradetails anzeigen")
        menubar.Append(camMenu, "&Kamera")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        self.Bind(wx.EVT_MENU, self.OnSelectCamera, selectItem)
        self.Bind(wx.EVT_MENU, self.OnCameraProperties, propItem)

    def OnExit(self, event):
        self.Close()

    def OnSelectCamera(self, event):
        cameras = self.get_usb_cameras()
        if not cameras:
            wx.MessageBox("Keine USB-Kamera gefunden.", "Info", wx.OK | wx.ICON_INFORMATION)
            return
        sel_dlg = CameraSelectionDialog(self, cameras)
        if sel_dlg.ShowModal() == wx.ID_OK:
            device = sel_dlg.GetSelectedCamera()
            if device is not None:  # Verwende "is not None" statt "if device:" um den DeprecationWarning zu vermeiden.
                self.selected_device = device
                product = device.properties.get("ID_V4L_PRODUCT", "Unbekannt")
                self.SetTitle(f"Kamera Anwendung - {product}")
        sel_dlg.Destroy()

    def OnCameraProperties(self, event):
        if self.selected_device is None:
            wx.MessageBox("Keine Kamera ausgewählt. Bitte zuerst eine Kamera wählen.", 
                          "Info", wx.OK | wx.ICON_INFORMATION)
        else:
            details = self.get_camera_details(self.selected_device)
            details_dlg = CameraDetailsDialog(self, details)
            details_dlg.ShowModal()
            details_dlg.Destroy()

    def get_usb_cameras(self):
        context = pyudev.Context()
        devices = []
        for device in context.list_devices(subsystem='video4linux'):
            if device.properties.get("ID_BUS") == "usb":
                devices.append(device)
        return devices

    def get_camera_details(self, device):
        details = []
        details.append(f"Device Node: {device.device_node}")
        details.append(f"Product: {device.properties.get('ID_V4L_PRODUCT', 'Unbekannt')}")
        details.append("Alle Eigenschaften:")
        for key, value in device.properties.items():
            details.append(f"{key}: {value}")
        return "\n".join(details)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.SetTopWindow(self.frame)
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
