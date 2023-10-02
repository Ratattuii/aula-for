texto = "LOrem Ipsu dolor"

#for variavel in range(começo, final, quanto espaços ele vai pular):
for i in range(0, len(texto), 2): 
    print(texto[i]) #acessa a posição em que o i está na variavel
    
#------------------------------------------------------------------------

for item in range(9, 0, -1): # -1 printa em ordem decrescente
    print(item)