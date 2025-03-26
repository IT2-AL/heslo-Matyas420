def overeni_hesla(heslo):
    if len(heslo) < 8:
        print("Heslo je příliš krátké")
    if len(heslo) >= 8:
        print("Heslo je dostatečné")
    
    elif heslo.isalnum():
        return "Heslo musí obsahovat alespoň jeden znak"
    elif heslo.islower() or heslo.isupper():
        return "Heslo musí obsahovat velké i malé písmeno."
    elif not any(H.isdigit() for H in heslo):
        return "Heslo musí obsahovat číslo."
    else:
        print("Heslo je nedostatečně silné, jednoduše řečeno skill issue")
        
def kontrola_hesla(heslo, heslo2):
    if heslo2 == heslo:
        print("Hesla jsou totožné")
    else:
        print("Hesla se neshodují")
    

heslo = input("Zadejte Heslo, které bude mít více než 8 znaků:")
overeni_hesla(heslo)

heslo2 = input("Znovu zadejte své heslo pro kontrolu, jestli se hesla zhodují:")
kontrola_hesla(heslo, heslo2)
