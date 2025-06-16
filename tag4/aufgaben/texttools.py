# Erstelle ein Modul texttools.py mit folgenden Funktionen:

# Einlesen eines Textes aus einer Datei
#   read_from_file(filename: str) -> str  
#   → Gibt den Inhalt der Datei als String zurück
#
#    count_words(text: str) -> int
#    → Gibt die Anzahl der Wörter zurück
#
#    count_lines(text: str) -> int
#    → Gibt die Anzahl der Zeilen zurück
#
#    most_common_word(text: str) -> str
#    → Gibt das am häufigsten vorkommende Wort zurück (ohne Groß-/Kleinschreibung)
#
#    longest_word(text: str) -> str
#    → Gibt das längste Wort zurück
#
#    word_frequency(text: str) -> dict
#    → Gibt ein Dictionary mit der Häufigkeit jedes Wortes zurück
#
#    character_frequency(text: str) -> dict
#    → Gibt ein Dictionary mit der Häufigkeit jedes Zeichens zurück
#
#    write_to_file(text: str, filename: str) -> None
#    → Schreibt den Text in eine Datei
#


def read_from_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def count_words(text: str) -> int:
    return len(text.split())

def count_lines(text: str) -> int:
    if text:
        return text.count('\n') + 1
    else:
        return 0

def most_common_word(text: str) -> str:
    words = text.lower().split()
    frequency = {}
    for word in words:
        word = word.strip('.,!?";:-')  # einfache Bereinigung
        frequency[word] = frequency.get(word, 0) + 1
    max_count = 0
    common = ''
    for word, count in frequency.items():
        if count > max_count:
            max_count = count
            common = word
    return common

def longest_word(text: str) -> str:
    words = text.split()
    longest = ''
    for word in words:
        clean_word = word.strip('.,!?";:-')
        if len(clean_word) > len(longest):
            longest = clean_word
    return longest

def word_frequency(text: str) -> dict:
    words = text.lower().split()
    freq = {}
    for word in words:
        word = word.strip('.,!?";:-')
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq

def character_frequency(text: str) -> dict:
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
    return freq

def write_to_file(text: str, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

#-- Spezialtools --------------------------------
def caesar(text: str, shift: int, decrypt: bool = False) -> str:
    if decrypt:
        shift = -shift

    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shifted = (ord(c) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += c
    return result

if __name__ == "__main__":
    # Beispieltest
    sample = "Hello world!\nHello again.\nWorld world world."

    print("Words:", count_words(sample))
    print("Lines:", count_lines(sample))
    print("Most common word:", most_common_word(sample))
    print("Longest word:", longest_word(sample))
    print("Word freq:", word_frequency(sample))
    print("Char freq:", character_frequency(sample))

    original = "Python macht Spass und lohnt sich zu lernen"
    encrypted = caesar(original, 5)
    decrypted = caesar(encrypted, 5, decrypt=True)

    print("Original:  ", original)
    print("Verschlüsselt:", encrypted)
    print("Entschlüsselt:", decrypted)