# Funkce pro ověření síly hesla
def overeni_hesla(heslo):
    # Kontrola, zda je heslo alespoň 8 znaků dlouhé a pokud není vrátí se False
    if len(heslo) < 8:
        print("Heslo je příliš krátké (minimálně 8 znaků)")
        return False
    # Kontrola, zda heslo obsahuje alespoň jedno číslo
    if not any(h.isdigit() for h in heslo):
        print("Heslo musí obsahovat alespoň jedno číslo.")
        return False
     # Kontrola, zda heslo obsahuje alespoň jedno písmeno
    if not any(h.isalpha() for h in heslo):
        print("Heslo musí obsahovat alespoň jedno písmeno.")
        return False
    # Kontrola, zda heslo obsahuje alespoň jedno velké písmeno
    if heslo.islower():
        print("Heslo musí obsahovat alespoň jedno velké písmeno.")
        return False
    # Kontrola, zda heslo obsahuje alespoň jedno malé písmeno
    if heslo.isupper():
        print("Heslo musí obsahovat alespoň jedno malé písmeno.")
        return False
    # Kontrola, zda heslo není mezi běžně používanými hesly
    if heslo.lower() in heslo_:
        return "Heslo je příliš slabé, je mezi běžně používanými hesly."
    # Pokud heslo splňuje všechny podmínky, je dostatečně silné
    print("Heslo je dostatečně silné.")
    return True
# Seznam běžně používaných hesel
heslo_ = ["m1234578M?", ".?.?Aa?.?.", "Pavel_novák25", "HeslojeHeslo_78", "HesloneniHeslo1?", "1212Karel!"]
# Funkce pro kontrolu, zda se zadaná hesla shodují
def kontrola_hesla(heslo, heslo2):
    if heslo2 == heslo:
        print("Hesla jsou totožná.")
    else:
        print("Hesla se neshodují.")
# Funkce pro kontrolu, zda heslo odpovídá běžně používaným heslům
def kontrola_podle_jmen(heslo, heslo_):
    # Pokud heslo není v seznamu
    if not any(Heslo == heslo for Heslo in heslo_):
        print("Gratulujeme vaše heslo se neshoduje s běžně používanými hesly")
        return False
    else:
        # Pokud je heslo v seznamu
        print("Vaše heslo se shoduje s běžně používanými hesly, prosím změntě si jej")
        return True
    
# Požádáme uživatele o zadání hesla
heslo = input("Zadejte heslo, které bude mít více než 8 znaků: ")
# Opakovaně požadujeme heslo, dokud nesplní podmínky
while not overeni_hesla(heslo):
    heslo = input("Zadejte heslo, které bude mít více než 8 znaků: ")
# Pokud je heslo mezi běžně používanými, ukončíme program
if kontrola_podle_jmen(heslo, heslo_):
    exit()
# Požádáme uživatele o zopakování hesla pro ověření shody
heslo2 = input("Znovu zadejte své heslo pro kontrolu, jestli se hesla shodují: ")
# Ověříme, zda se hesla shodují
kontrola_hesla(heslo, heslo2)

