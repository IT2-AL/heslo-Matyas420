def overeni_hesla(heslo):
    if len(heslo) >= 8:
        print("Heslo je dostatečně silné")
    elif heslo.isalnum():
        return "Heslo musí obsahovat alespoň jeden znak"
    elif heslo.islower() or heslo.isupper():
        return "Heslo musí obsahovat velké i malé písmeno."
    elif not any(H.isdigit() for H in heslo):
        return "Heslo musí obsahovat číslo."
    else:
        print("Heslo je nedostatečně silné, jednoduše řečeno skill issue")
    
    return "Tvoje heslo je v pořádku"

heslo = input("Zadejte Heslo, které bude mít více než 8 znaků:")
print(overeni_hesla(heslo))

