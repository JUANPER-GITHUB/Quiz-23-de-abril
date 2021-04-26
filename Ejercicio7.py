cuenta = input("Solo se acepta para su suscripción una cuenta de Gmail, ingresela a continuación: ")
def comprobar(cuenta):
    if cuenta.find('@gmail.com') >= 0:     # Se busca en la cuenta ingresada que haya un "@gmail.com"
        print("Cuenta Válida")
    else:
        print("Cuenta no Válida")
comprobar(cuenta)