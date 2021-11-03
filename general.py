

import math
import platform
import os
import time

os.system("clear")
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
BLANCO = '\033[37m'
RESET = '\033[39m'

print(BLUE+"                                            "+RED+"        ___  " )
print(BLUE+"  mmmmm mmmmm mmmmm mm mm  m   m m     mmmmm"+RED+"       l   l           ")
print(BLUE+"  m     m   m m   m m m m  m   m m     m   m"+RED+"      l     l     ")
print(BLUE+"  mmm   m   m mmmmm m   m  m   m m     m   m"+RED+"     l       l   ")
print(BLUE+"  m     m   m m  m  m   m  m   m m     mmmmm"+RED+"    l---------l    ")
print(BLUE+"  m     mmmmm m   m m   m  mmmmm mmmmm m   m"+YELLOW+"    l         l ")
print(BLUE+"                                            "+YELLOW+"    l      º  l  ")
print(BLUE+"  mmmmm mmmmm mmm m mmmmm mmmmm mmmmm m     "+YELLOW+"    l      º  l       ")
print(BLUE+"  m     m     m m m m     m   m m   m m     "+YELLOW+"    l      º  l          ")
print(BLUE+"  m mmm mmm   m m m mmm   mmmmm m   m m     "+YELLOW+"    l    _    l"+GREEN+"  _______    ")
print(BLUE+"  m   m m     m m m m     m  m  mmmmm m     "+YELLOW+"    l   l l   l"+GREEN+"  l    l_l   ")
print(BLUE+"  mmmmm mmmmm m mmm mmmmm m   m m   m mmmmm "+YELLOW+"    l___l_l___l"+GREEN+"  l- -- --l ")
print(BLANCO+"                 __________                                   "+GREEN+" º  º " )
print(BLANCO+"           -b ± √ b² - 4ac              " )
print("   X =          -----------                 " )
print("                   2a " )
print("                   " )
print("  nota:Recuerda ordenar correctamente tus valores de la forma: ax² + bx + c")
print("")
a = float(input(" ingresa el valor a:"))
print(" a es:",a)
b = float(input(" ingresa el valor b:"))
print(" b es:",b)
c = float(input(" ingresa el valor c:"))
print(" c es:",c)
print("")
print(" la estructura es:",a,"x² + ",b,"x + ",c)
print("\n  Iniciando calculo...")
time.sleep(3)
k = ((b ** 2)-(4*a*c))
print("\n comenzando paso 1: ",(-1*b),"± ✓(",k,")")
print("                      -------------------------")
print("                             ",(2*a))
h = (k ** 0.5)
print("\n comenzando paso 2: ",(-1*b),"± (",h,")")
print("                      -------------------------")
print("                             ",(2*a))
print("\n")
l = (2*a)
Y = ((-1*(b)) + (h)) / l
X = ((-1*(b)) - (h)) / l
print(YELLOW+" \n\n El resultado de X1 es: ",X)
print(GREEN+" \n El resultado de X2 es: ",Y)
print(BLANCO+" \n\n presiona cualquier tecla para salir...")
os.system("read")
os.system("clear")
os.system("exit")
