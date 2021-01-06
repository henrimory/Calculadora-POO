from calculadora import Calculadora


numero1 = float(input("Digite o primeiro valor: "))
numero2 = float(input("Digite o segundo valor: "))
myCalc = Calculadora(numero1, numero2)

op = input("Digite a operação desejada(+ - * /) ")
if op == "+":
    myCalc.somar()
elif op == "-":
    myCalc.subtrair()
elif op == "*":
    myCalc.multiplicar()
elif op == "/":
    myCalc.divisao()
else:
    print("Opção inválida!")

if op == "+" or op == "-" or op == "*" or op == "/":
    print("O resultado é ", myCalc.resultado)