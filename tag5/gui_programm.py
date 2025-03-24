import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wxPython Menü-Grundgerüst", size=(700, 500))
        self.panel = wx.Panel(self)

        self.text = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE | wx.TE_READONLY)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text, 1, wx.EXPAND | wx.ALL, 5)
        self.panel.SetSizer(sizer)

        self.create_menu()
        self.Centre()
        self.Show()

    def create_menu(self):
        menubar = wx.MenuBar()

        # Datei-Menü
        file_menu = wx.Menu()
        open_item = file_menu.Append(wx.ID_OPEN, "&Öffnen\tCtrl+O", "Datei öffnen")
        exit_item = file_menu.Append(wx.ID_EXIT, "&Beenden\tCtrl+Q", "Programm beenden")
        menubar.Append(file_menu, "&Datei")

        # Edit-Menü
        edit_menu = wx.Menu()
        edit_menu.Append(wx.ID_UNDO, "Rückgängig\tCtrl+Z")
        edit_menu.Append(wx.ID_REDO, "Wiederholen\tCtrl+Y")
        menubar.Append(edit_menu, "&Edit")

        # Settings-Menü (nur Dummy)
        settings_menu = wx.Menu()
        settings_menu.Append(wx.ID_ANY, "Option 1")
        settings_menu.Append(wx.ID_ANY, "Option 2")
        menubar.Append(settings_menu, "&Settings")

        # Hilfe-Menü
        help_menu = wx.Menu()
        about_item = help_menu.Append(wx.ID_ABOUT, "&Über...\tF1")
        menubar.Append(help_menu, "&Hilfe")

        self.SetMenuBar(menubar)

        # Events
        self.Bind(wx.EVT_MENU, self.on_open, open_item)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)
        self.Bind(wx.EVT_MENU, self.on_about, about_item)

    def on_open(self, event):
        with wx.FileDialog(self, "Datei auswählen", wildcard="Textdateien (*.txt)|*.txt|Alle Dateien (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dialog:
            if dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = dialog.GetPath()
            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.text.SetValue(content)
            except Exception as e:
                wx.MessageBox(str(e), "Fehler", wx.ICON_ERROR)

    def on_exit(self, event):
        self.Close()

    def on_about(self, event):
        wx.MessageBox("Einfaches wxPython-Menü-Beispiel", "Über", wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    MainFrame()
    app.MainLoop()
