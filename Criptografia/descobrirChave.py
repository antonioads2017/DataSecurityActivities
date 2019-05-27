
texto = input("Digite o texto a ser cifrado:").lower()
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
cifra=''
for k in range(27):
    for l in texto:
        if l in alfabeto:
            indexL=alfabeto.index(l)
            cifra+=alfabeto[(indexL-k)%len(alfabeto)]
        else:
            cifra+=l
    print(cifra)
    cifra=''
    print(k)
   