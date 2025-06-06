import codecs

def replace_m_c(text,i,o):
    trans_table=str.maketrans(i,o)
    return text.translate(trans_table)

intab=""
outtab=""

# read the code table file
with codecs.open("字库终版20240531 - 副本.txt", "r", "utf-8") as f:
    for line in f:
        code, char = line.strip().split("=")
        code=bytes.fromhex(code)
        try:
            intab+=code.decode("shift_jis")
            outtab+=char
        except:
            pass
            
        
# read the input text file
with codecs.open("tou.msbt.kup", "r", "utf-8",errors="ignore") as f:
    input_text = f.read()

# replace characters based on the code table
output_text = replace_m_c(input_text,outtab,intab)

# write the output text file
with codecs.open("output8.kup", "w", "utf-8") as f:
    f.write(output_text)
