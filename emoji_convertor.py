def Emojis2Words(message):
    words = message.split(' ')
    emojis={
        ":)":"😊",
        ":(":"😢",
        ":|)":"😁"
    }
    output=""
    for word in words:
        output+=emojis.get(word,word)+" "
    return output


message=input(">")
output=Emojis2Words(message)
print(output)
