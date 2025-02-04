import chess
import chess.engine
import sys

def main():
    # Lese FEN-String entweder als Argument oder per Eingabe
    fen = sys.argv[1] if len(sys.argv) > 1 else input("FEN-String eingeben: ")
    try:
        board = chess.Board(fen)
    except Exception as e:
        print(f"Ungültiger FEN-String: {e}")
        sys.exit(1)

    # Pfad zur Stockfish-Engine anpassen (Engine muss im PATH sein oder vollständigen Pfad angeben)
    engine_path = "stockfish"
    try:
        engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    except Exception as e:
        print(f"Fehler beim Starten des Engines: {e}")
        sys.exit(1)

    try:
        info = engine.analyse(board, chess.engine.Limit(time=1.0))
    except Exception as e:
        print(f"Analysefehler: {e}")
        engine.quit()
        sys.exit(1)

    score = info["score"]
    if score.is_mate():
        mate_in = score.mate()
        if mate_in is None:
            status = "Unbekanntes Matt"
        elif mate_in > 0:
            status = f"Weiß gewinnt in {mate_in} Zügen (Matt)"
        else:
            status = f"Schwarz gewinnt in {-mate_in} Zügen (Matt)"
    else:
        cp = score.white().score()
        if cp is None:
            status = "Keine Bewertung verfügbar"
        elif cp > 50:
            status = "Weiß hat Vorteil"
        elif cp < -50:
            status = "Schwarz hat Vorteil"
        else:
            status = "Ausgeglichen"

    print("Bewertung:", status)
    engine.quit()

if __name__ == "__main__":
    main()
