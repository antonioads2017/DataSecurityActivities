#CIFRA DE CESAR EM PYTHON
#Antonio Miguel

alfabeto = 'abcdefghijklmnopqrstuvwxyz' #variavel que contem o alfabeto

#função de que cifrar ou decifrar o texto
def crypter(dir):
    texto = input("Digite o texto a ser cifrado:").lower()
    print(texto)
    chave = int(input("Digite a chave:"))
    cifra=''
    for l in texto: #Aqui será feito a cifragem ou decifragem de cada letra do texto
        if l in alfabeto: #Se a letra do texto tiver no alfabeto,
            indexL=alfabeto.index(l)  # ele paga o valor do indice do alfabeto
            cifra+=alfabeto[(indexL+(dir*chave))%len(alfabeto)] # Concate a letra ja cifrado ou decifrada 
        else: # Caso haja espaço no texto, ele simplesmente so add o espaço
            cifra+=l
    print (cifra) #Imprime o texto ja cifrado ou decifrado

#para cifrar um texto ele manda um parametro 1 para o crypter() cifrar e -1 para decifrar
def decrypt():
    return crypter(-1) 

def encrypt():
    return crypter(1)
    

def main():
    while True:
        opcao = int(input("Digite 1 para cifrar ou 2 para decrifar:"))
        if opcao == 1:
            encrypt()
        elif opcao == 2:
            decrypt()
        else:
            print("Opção invalida")

print("------CIFRA DE CESAR------")
print("--------------------------")
main()


            



