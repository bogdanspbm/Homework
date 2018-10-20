def encrypt(offset, text):
    
    strcaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    strsmall = 'abcdefghijklmnopqrstuvwxyz'

    strcaps2 = strcaps[offset:] + strcaps[:offset]
    strsmall2 = strsmall[offset:] + strsmall[:offset]

    encrypter = {' ':' '}

    result = ''

    for i in range(len(strcaps)):
        encrypter[strcaps[i]] = strcaps2[i]
        encrypter[strsmall[i]] = strsmall2[i]

    for i in range(len(text)):
        result += encrypter[text[i]]

    return result


def decrypt(offset, text):

    strcaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    strsmall = 'abcdefghijklmnopqrstuvwxyz'

    strcaps2 = strcaps[offset:] + strcaps[:offset]
    strsmall2 = strsmall[offset:] + strsmall[:offset]

    encrypter = {' ': ' '}

    result = ''

    for i in range(len(strcaps)):
        encrypter[strcaps2[i]] = strcaps[i]
        encrypter[strsmall2[i]] = strsmall[i]

    for i in range(len(text)):
        result += encrypter[text[i]]

    return result
