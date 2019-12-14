def rysujWykres(jezyki, wartosci):
    
    x=0
    for y in wartosci:
        print(f'{jezyki[x].rjust(10)}: {y*"#"}')
        x+=1
        
  
    
jezyki = ["Java", "Python", "JavaScript", "C++", "C#", "Ruby", "Perl", "PHP", "C", "Android"]
wartosci = [61, 47, 37, 32, 26, 18, 14, 14, 9, 7]

rysujWykres(jezyki, wartosci)
    