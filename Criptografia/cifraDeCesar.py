#CIFRA DE CESAR EM PYTHON
#Antonio Miguel

alfabeto = 'abcdefghijklmnopqrstuvwxyz' #variavel que contem o alfabeto

#função de que cifrar ou decifrar o texto
def cipher(dir,chave,texto):
    cifra=''
    for l in texto: #Aqui será feito a cifragem ou decifragem de cada letra do texto
        if l in alfabeto: #Se a letra do texto tiver no alfabeto,
            indexL=alfabeto.index(l)  # ele paga o valor do indice do alfabeto
            cifra+=alfabeto[(indexL+(dir*chave))%len(alfabeto)] # Concate a letra ja cifrado ou decifrada 
        else: # Caso haja espaço no texto, ele simplesmente so add o espaço
            cifra+=l
    return cifra #retorna o texto ja cifrado ou decifrado

#para cifrar um texto ele manda um parametro 1 para o cipher() cifrar e -1 para decifrar
def decrypt(chave,texto):
    return cipher(-1,chave,texto) 

def encrypt(chave,texto):
    return cipher(1,chave,texto)

def descobrirChave(texto):
    for c in range(len(alfabeto)):
        print(cipher(1,c,texto),"chave: ",c)
    

def main():
    while True:
        opcao = int(input("\nDigite 1 - Cifragem\nDigite 2 - Decifragem\nDigite 3 - Descobrir chave\nOpção: "))
        if opcao == 1:
            chave = int(input("\nDigite a chave:"))
            texto = input("Digite o texto a ser cifrado:").lower()
            print(encrypt(chave,texto))
        elif opcao == 2:
            chave = int(input("\nDigite a chave:"))
            texto = input("Digite o texto a ser decifrado:").lower()
            print(decrypt(chave,texto))
        elif opcao == 3:
            cifra = input("\nDigite o texto a ser descoberto:").lower()
            descobrirChave(cifra)
        else:
            print("Opção invalida")

print("------CIFRA DE CESAR------")
print("--------------------------")
main()


            



