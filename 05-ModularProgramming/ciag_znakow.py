#05.13

def wspak(tekst):
    return tekst[::-1]
    

def rozs(tekst):
    return(" ".join(tekst))


def wielkie_litery(tekst):
    x=tekst.split()
    wyraz1=x[0]
    wyraz2=x[1]
    wyraz3=x[2]
    wyraz4=x[3]
    
    return(wyraz1.capitalize() + ' ' + wyraz2.capitalize() + ' ' + wyraz3 + ' ' + wyraz4.capitalize())


