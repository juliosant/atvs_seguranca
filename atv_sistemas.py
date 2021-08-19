# Julio Santiago

arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def cifra_cesar(text, key):
    cifra = ''
    aux = 0
    for i in text:
        #print(i)
        if i == ' ':
            cifra+=' '
        else:
            aux = arr.index(i)+ key
            if aux >= len(arr):
                while True:
                    more_than = aux - len(arr)
                    if more_than < len(arr):
                        cifra+=arr[more_than]
                        break
                    else:
                        aux = more_than
            else:
                cifra+=arr[arr.index(i)+key]

    return cifra

def descifra_cesar(text_encrypted, key):
        return cifra_cesar(text_encrypted, key*-1)

def brute_force(text_encrypted):
    for key in range(0, len(arr)):
        print(key+1, ': ',cifra_cesar(text_encrypted, key*-1))


text = input('Digite um texto: ').upper()

print('1 - Encriptar, \n2 - Decriptar, \n3 - Decriptar com força Bruta')
what_do = int(input("O que deseja fazer com esa frase?: " ))

# Encriptar
if what_do == 1:
    key = int(input('Digite a chave: '))
    print(cifra_cesar(text, key))
# Decriptar
if what_do == 2:
    key = int(input('Digite a chave: '))
    print(descifra_cesar(text, key))
# Força bruta
if what_do == 3:
    brute_force(text)



