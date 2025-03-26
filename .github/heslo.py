def overeni_hesla(heslo):
    if len(heslo) < 8:
        print("Heslo je příliš krátké (minimálně 8 znaků)")
        return False
    
    if not any(h.isdigit() for h in heslo):
        print("Heslo musí obsahovat alespoň jedno číslo.")
        return False
    
    if not any(h.isalpha() for h in heslo):
        print("Heslo musí obsahovat alespoň jedno písmeno.")
        return False
    
    if heslo.islower():
        print("Heslo musí obsahovat alespoň jedno velké písmeno.")
        return False
    
    if heslo.isupper():
        print("Heslo musí obsahovat alespoň jedno malé písmeno.")
        return False
    
    print("Heslo je dostatečně silné.")
    return True

def kontrola_hesla(heslo, heslo2):
    if heslo2 == heslo:
        print("Hesla jsou totožná.")
    else:
        print("Hesla se neshodují.")

heslo = input("Zadejte heslo, které bude mít více než 8 znaků: ")

while not overeni_hesla(heslo):
    heslo = input("Zadejte heslo, které bude mít více než 8 znaků: ")
heslo2 = input("Znovu zadejte své heslo pro kontrolu, jestli se hesla zhodují: ")
kontrola_hesla(heslo, heslo2)
