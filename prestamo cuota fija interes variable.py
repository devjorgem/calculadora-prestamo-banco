saldo=int(input("ponga aqui valor a prestar: "))   
cuotas=int(input("cantidad a tiempo: "))
saldo1=saldo
for i in range(1,cuotas+1):
    interes=0.02
    abonoacapital=(saldo1/cuotas)
    interesapagar=saldo*interes
    a=abonoacapital+interesapagar
    print(f"su cuota N{i} pagara {int(a)} abonando a capital todos los meses cuotas fijas de {int(abonoacapital)} y de interes {int(interesapagar) } en este mes")
    saldo-=abonoacapital