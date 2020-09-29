import datetime
import time

def conversor(hours):
    h,m,s = hours.split(':')
    seconds = int(datetime.timedelta(
                                     hours=int(h),
                                     minutes=int(m),
                                     seconds=int(s)).total_seconds())
    print(f"{hours} em segundos é: {seconds}")

tempo = input("Informe hora no formato hh:mm:ss ")
conversor(tempo)
