from media import Media

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda a nota: "))

minhamedia = Media(nota1, nota2)
result = minhamedia.calcmedia()
print(result)

print("Sua maior nota foi", minhamedia.maiornota())
