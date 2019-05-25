alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def crypter(dir):
    texto = input("Digite o texto a ser cifrado:").lower()
    print(texto)
    chave = int(input("Digite a chave:"))
    cifra=''
    for l in texto:
        if l in alfabeto:
            indexL=alfabeto.index(l)
            cifra+=alfabeto[(indexL+(dir*chave))%len(alfabeto)]
        else:
            cifra+=l
    print (cifra)

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

main()


            



