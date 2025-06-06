import codecs

with codecs.open("tou_10 - 副本T (1).txt", "r", "utf-8",errors="ignore") as f:
    input_text = f.read()

with codecs.open("output8.txt", "w", "shift_jis",errors="ignore") as f:
    f.write(input_text)
