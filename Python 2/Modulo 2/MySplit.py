

def mysplit(phrase):
    word = ''
    list_of_words = []
    for ch in phrase:
        if(ch != " "):
            word = word + ch
        else: 
            if(word != ""): # meter la palabra siempre y cuando no sea vacia
                list_of_words.append(word)
                word = ''
    if(word != ""):
        list_of_words.append(word) # Para el final de frase
    return list_of_words

print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("Ser o no ser, esa es la cuestión"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
