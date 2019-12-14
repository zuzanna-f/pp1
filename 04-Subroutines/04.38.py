def wielkie_litery(x):
    import re
    litery = re.findall('[A-Z]', x)
    return ''.join(litery)
    
ciag_znakow = "AbcdEfghIjklmnOprstUwYz"
print(wielkie_litery(ciag_znakow))


