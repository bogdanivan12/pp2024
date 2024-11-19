text = input()
ls = [f"{caracter}p{caracter.lower()}" if caracter in "aeiouAEIOU" else caracter for caracter in text]
print("".join(ls))
