import wx

class FileViewer(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Datei anzeigen", size=(600, 400))
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.filename = wx.TextCtrl(panel)
        hbox.Add(self.filename, proportion=1, flag=wx.EXPAND|wx.RIGHT, border=5)

        open_btn = wx.Button(panel, label="Öffnen")
        open_btn.Bind(wx.EVT_BUTTON, self.on_open)
        hbox.Add(open_btn, flag=wx.EXPAND)

        vbox.Add(hbox, flag=wx.EXPAND|wx.ALL, border=10)

        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE|wx.TE_READONLY)
        vbox.Add(self.text, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=10)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def on_open(self, event):
        path = self.filename.GetValue()
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                self.text.SetValue(content)
        except Exception as e:
            wx.MessageBox(str(e), "Fehler", wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App()
    FileViewer()
    app.MainLoop()
