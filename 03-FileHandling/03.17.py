import re

tekst = 'To be, or not to be, that is the question'
samogłoski = re.findall('[eyuioa]', tekst)

print(len(samogłoski))