
from datetime import date
ano = int(input("Qual ano você quer verificar?: "))
if ano == 0:
 ano = date.today().year
if ano % 4 == 0 :
    if ano % 100 != 0:
        if ano % 400 == 0:
            print("O ano de {}, é BISSEXTO.".format(ano))
        else: print("O ano de {}, NÃO é BISSEXTO.".format(ano))            
    else: print("O ano de {}, NÃO é BISSEXTO.".format(ano))          
else: print("O ano de {}, NÃO é BISSEXTO.".format(ano))            