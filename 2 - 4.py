def signs(day, month):
    if day > 31 or day <= 0:
        return print("Dia inválida")
    if month > 12 or month <= 0:
        return print("Mês inválido")
    if day>=22 and day<=31 and month==12 or day>=1 and day<=20 and month==1:
      print ("Capricornio")

    if day>=21 and day<=31 and month==1 or day>=1 and day<=18 and month==2:
      print ("Aquario")

    if day>=19 and day<=29 and month==2 or day>=1 and day<=19 and month==3:
      print ("Peixes")

    if day>=20 and day<=31 and month==3 or day>=1 and day<=20 and  month==4:
       print ("Aries")

    if day>=21 and day<=30 and month==4 or day>=1 and day<=20 and month==5:
       print ("Touro")

    if day>=21 and day<=31 and month==5 or day>=1 and day<=20 and month==6:
       print ("Gemeos")

    if day>=21 and day<=30 and month==6 or day>=1 and day<=21 and month==7:
       print ("Cancer")

    if day>=22 and day<=31 and month==7 or day>=1 and day<=22 and month==8:
       print ("Leao")

    if day>=22 and day<=31 and month==8 or day>=1 and day<=22 and month==9:
       print ("Virgem")

    if day>=22 and day<=30 and month==9 or day>=1 and day<=22 and month==10:
       print ("Libra")

    if day>=23 and dia <=31 and month==10 or day>=1 and day<=21 and month==11:
       print ("Escorpiao")

    if day>=22 and day<=30 and month==11 or day>=1 and day<=21 and month==12:
       print ("Sagitario")


dia = int(input("Informe o dia de nascimento: "))
mes = int(input("Informe o mês de nascimento: "))
signs(dia, mes)
