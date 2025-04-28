notaDoAluno = int(input("Digite sua nota: "))

if notaDoAluno >= 90 and notaDoAluno <= 100:
    print("Parabéns, você tirou A!")

elif notaDoAluno >= 80 and notaDoAluno <= 89:
    print("Muito bem, você tirou B.")

elif notaDoAluno >= 70 and notaDoAluno <= 79:
    print("Bom trabalho, você tirou C.")

elif notaDoAluno >= 60 and notaDoAluno <= 69:
    print("Fique atento, você tirou D.")

else:
    print("Estude um pouco mais, você tirou F.")