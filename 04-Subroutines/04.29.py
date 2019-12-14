def mediana():
    tablica.sort()
    
    import statistics
    return statistics.median(tablica)


def dominanta():
    import statistics
    return statistics.mode(tablica)
    


tablica = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]

print("mediana =", mediana())
print("dominanta =", dominanta())