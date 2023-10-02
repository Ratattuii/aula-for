for i in range(1, 21):
    print(i)

# --------------------------------------------------------------

for i in range(0, 102, 2):
    print(i)
    
# --------------------------------------------------------------

for i in range(1, 100, 2):
    print(i)
    
# --------------------------------------------------------------

numero_inteiro = int(input("Digite um número para gerar a tabuada: "))

tabuada = []

for i in range(1, 11):
    resultado = numero_inteiro * i
    tabuada.append(resultado)

print(tabuada)

# ----------------------------------------------------------------

numList = []

while i != 0.1:
    i = float(input("Insira quantos números você quiser (Digite '0.1' para parar): "))
    
    numList.append(i)

numList.pop()

numList.sort()

print(numList)

print(numList[-1])

print(numList[0])

soma = sum(numList)
print(soma)
