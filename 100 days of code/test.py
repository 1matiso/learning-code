def consoantes(palavra):
    cons = 0
    for letra in palavra:
        if letra not in "aeiou":
            cons += 1
    print(f"essa palavra tem {cons} consoantes")


consoantes("matheus")


