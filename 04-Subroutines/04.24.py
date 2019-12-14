def miesiąc(n):
    miesiące = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień", "październik", "listopad", "grudzień"]
    return miesiące[n-1]

tablica = [miesiąc(7), miesiąc(9)]
print(tablica)