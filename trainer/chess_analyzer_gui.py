import wx
import wx.grid
import chess
import chess.engine

# Panel zur Darstellung des Schachbretts
class BoardPanel(wx.Panel):
    def __init__(self, parent, board=None, size=400):
        super().__init__(parent, size=(size, size))
        self.board = board if board else chess.Board()
        self.size = size
        self.square_size = size // 8
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def set_board(self, board):
        self.board = board
        self.Refresh()

    def OnPaint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        # Zeichne Schachfelder
        for row in range(8):
            for col in range(8):
                x = col * self.square_size
                y = row * self.square_size
                color = wx.Colour(240, 217, 181) if (row + col) % 2 == 0 else wx.Colour(181, 136, 99)
                dc.SetBrush(wx.Brush(color))
                dc.DrawRectangle(x, y, self.square_size, self.square_size)
        # Zeichne Figuren
        font = wx.Font(self.square_size - 4, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        dc.SetFont(font)
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                file = chess.square_file(square)
                rank = chess.square_rank(square)
                # a8 oben links: Zeilenindex = 7 - rank
                row = 7 - rank
                col = file
                x = col * self.square_size
                y = row * self.square_size
                piece_char = self.get_piece_unicode(piece)
                tw, th = dc.GetTextExtent(piece_char)
                dc.DrawText(piece_char, x + (self.square_size - tw) // 2, y + (self.square_size - th) // 2)

    def get_piece_unicode(self, piece):
        mapping = {
            'K': u'\u2654', 'Q': u'\u2655', 'R': u'\u2656',
            'B': u'\u2657', 'N': u'\u2658', 'P': u'\u2659',
            'k': u'\u265A', 'q': u'\u265B', 'r': u'\u265C',
            'b': u'\u265D', 'n': u'\u265E', 'p': u'\u265F'
        }
        return mapping[piece.symbol()]

# Hauptfenster mit Menü, Brettanzeige und Bewertungstabelle
class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Schachbewertung", size=(420, 600))
        self.InitMenu()
        self.board = chess.Board()
        self.board_panel = BoardPanel(self, self.board, size=400)
        self.evaluation_grid = wx.grid.Grid(self)
        self.evaluation_grid.CreateGrid(3, 2)
        self.evaluation_grid.SetColLabelValue(0, "Parameter")
        self.evaluation_grid.SetColLabelValue(1, "Wert")
        self.evaluation_grid.SetCellValue(0, 0, "Mate")
        self.evaluation_grid.SetCellValue(1, 0, "Centipawn")
        self.evaluation_grid.SetCellValue(2, 0, "Status")
        self.evaluation_grid.Disable()
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.board_panel, 0, wx.ALL | wx.CENTER, 5)
        sizer.Add(self.evaluation_grid, 0, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(sizer)
        self.Centre()
        self.Show()

    def InitMenu(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        openItem = fileMenu.Append(wx.ID_OPEN, "&Öffnen")
        exitItem = fileMenu.Append(wx.ID_EXIT, "&Ende")
        menubar.Append(fileMenu, "&Datei")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.on_open, openItem)
        self.Bind(wx.EVT_MENU, self.on_exit, exitItem)

    def on_open(self, event):
        dlg = wx.FileDialog(self, "FEN-Datei öffnen", "", "", "Text files (*.txt)|*.txt", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            try:
                with open(path, "r") as f:
                    fen = f.read().strip()
            except Exception as e:
                wx.MessageBox(f"Fehler beim Lesen der Datei: {e}", "Error", wx.OK | wx.ICON_ERROR)
                return
            try:
                board = chess.Board(fen)
            except Exception as e:
                wx.MessageBox(f"Ungültiger FEN-String: {e}", "Error", wx.OK | wx.ICON_ERROR)
                return
            self.board = board
            self.board_panel.set_board(board)
            self.update_evaluation(board)
        dlg.Destroy()

    def on_exit(self, event):
        self.Close()

    def update_evaluation(self, board):
        engine_path = "stockfish"  # Pfad zum Stockfish-Engine
        try:
            engine = chess.engine.SimpleEngine.popen_uci(engine_path)
        except Exception as e:
            wx.MessageBox(f"Fehler beim Starten des Engines: {e}", "Error", wx.OK | wx.ICON_ERROR)
            return
        try:
            info = engine.analyse(board, chess.engine.Limit(time=1.0))
            score = info["score"]
            mate = "N/A"
            cp = "N/A"
            status = ""
            if score.is_mate():
                mate_val = score.mate()
                mate = str(mate_val) if mate_val is not None else "Unbekannt"
                if mate_val is None:
                    status = "Unbekanntes Matt"
                elif mate_val > 0:
                    status = f"Weiß gewinnt in {mate_val} Zügen (Matt)"
                else:
                    status = f"Schwarz gewinnt in {-mate_val} Zügen (Matt)"
            else:
                cp_val = score.white().score()
                cp = str(cp_val) if cp_val is not None else "N/A"
                if cp_val is None:
                    status = "Keine Bewertung"
                elif cp_val > 50:
                    status = "Weiß hat Vorteil"
                elif cp_val < -50:
                    status = "Schwarz hat Vorteil"
                else:
                    status = "Ausgeglichen"
        except Exception as e:
            wx.MessageBox(f"Analysefehler: {e}", "Error", wx.OK | wx.ICON_ERROR)
            engine.quit()
            return
        engine.quit()
        self.evaluation_grid.SetCellValue(0, 1, mate)
        self.evaluation_grid.SetCellValue(1, 1, cp)
        self.evaluation_grid.SetCellValue(2, 1, status)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
