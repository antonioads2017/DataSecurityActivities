import numpy as np

#Algoritmo de Cifragem e Decifragem em RC4 em Python, RC4 é uma criptografia simétrica
#bastante usada em rede WEP E SSL.
#Feito por Antonio Miguel


def KSA(key): #função para permutação de todos os 8-bit possíveis (256 elementos) que forma o conjunto S
    tam_key = len(key) #pega o tamanho da chave 
    S = list(range(256))#cria uma lista com numeros de 0 a 255
    j = 0
    for i in range (256):
        j = (j + S[i]+key[i%tam_key])%256 #É somado o valor de j, o valor de S apontado por i e o valor de K (chave) apontado por i e armazenado na variável j.
        S[i],S[j] = S[j], S[i] #swap dos valores S[i] e S[j]
    return S

def PRGA(S, n): #função para gerar a keystream
    i = 0
    j = 0
    key=[]
    while n>0:
        n-=1 #n é o tamanho da mensagem
        i = (i + 1) % 256 #incrementa +1 em i e faz a modal 256
        j = (j + S[i]) % 256 #adiciona o valor de S apontado por i com j e armazena o resultado em j em modal de 256.
        S[i],S[j] = S[j], S[i] #swap dos valores S[i] e S[j]
        K = S[(S[i] + S[j]) % 256] # soma os valores de  S[i] e S[j] em modal 256
        key.append(K) #adiciona o valor de K a chave
    return key

def preparing_key_array(s):
    return [ord(c) for c in s] #converte o s em array

def array_for_string(array): #função para converter o array de string para string 
    text=""
    for c in range(len(array)):
        text+=array[c]
    return text

def encrypt(message,keystream): #função de cifragem
        message = np.array([ord(c) for c in message]) #mensagem é convertida em np.array 
        encryption = keystream ^ message #XOR entre a keystream e a mensagem
        print("\ncifragem: ",encryption)
        return encryption
        

def createKeystream(key, message): #função para criar a keystream em array
    S = KSA(key) 
    keystream = np.array(PRGA(S, len(message))) #keystream é convertida em np.array
    print("\nkeystream: ",keystream)
    return keystream

def decrypt(encryption, keystream): #função para decifragem
    decrypterUni =  keystream ^ encryption #XOR entre a cifra e a keystream
    decrypter = [chr(c) for c in decrypterUni]
    # return decrypter.replace("'","").replace(", ","")
    return array_for_string(decrypter)


def main ():
    print("----------------------------")
    print("Cifragem e decifragem em RC4")
    print("----------------------------")
    while True:
        key = input("Digite a chave: ")
        message = input("Digite a mensagem: ")
        keyArray = preparing_key_array(key)
        keystream = createKeystream(keyArray,message)
        encryption = encrypt(message,keystream)
        encryptionHex=(encryption.astype(np.uint8).data.hex()) #cifra em hexadecimal
        print("\nhexa da cifragem: ",encryptionHex)
        decifrar=""
        while decifrar!=key:
                decifrar = input("\nDigite a chave para decifrar: ")
                if decifrar==key:
                        print("\ndecriptada:", decrypt(encryption,keystream))
                else:
                        print("\nChave invalida, tente de novo!")
        print("\n--------------------------\nBora de novo!\n")
main()






