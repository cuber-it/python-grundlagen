text = "Hallo, Willi Watz! Wie geht es dir?"
text_size = len(text)
lfd_nr = -1

neu_text = ""

while lfd_nr >= -text_size:
    neu_text = neu_text + text[lfd_nr]
    lfd_nr -= 1

print(neu_text)


neu_text = "".join(reversed(text)) # macht das gleiche, aber wenn man mit py anfängt etwas schwerer verständlich, denke ich :-D
print(neu_text)