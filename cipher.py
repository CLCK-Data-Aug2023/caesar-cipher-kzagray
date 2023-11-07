cipher = {
            "a":"f",
            "b":"g",
            "c":"h",
            "d":"i",
            "e":"j",
            "f":"k",
            "g":"l",
            "h":"m",
            "i":"n",
            "j":"o",
            "k":"p",
            "l":"q",
            "m":"r",
            "n":"s",
            "o":"t",
            "p":"u",
            "q":"v",
            "r":"w",
            "s":"x",
            "t":"y",
            "u":"z",
            "v":"a",
            "w":"b",
            "x":"c",
            "y":"d",
            "z":"e"
}

sentence = input("Please enter a sentence:")
sentence = sentence.lower()

secret_sentence = ""

for char in sentence: 
    if char in cipher: 
        char = cipher[char]
    secret_sentence += char
print(secret_sentence) 
