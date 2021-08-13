print()
print("   OOOOOOOOOOOOOOOOOOOO")
print("  OO                  OO")
print("  OO    0         0   OO")
print("  OO   0 0       0 0  OO")
print("  OO    0         0   OO")
print("  OO                  OO")
print("   OOOOOOOOOOOOOOOOOOOO")

print()
print()
print("Esta es la versión 0.1 del calculador de instalaciones")
print("Escrito por Jose Angel Calvo")
print()
print()

#Preguntamos las alturas y manos del edificio
alturas = int(input("¿Cuantas alturas tiene el edificio?"))
manos = int(input("¿Cuantas manos tiene el edificio?"))
print()
print(f"El edificio tiene {alturas * manos} vecinos en el edificio")
print("Material a instalar:")

#Dependiendo de las alturas y las manos introducidas, calculamos las tomas necesarias para realizar la instalación
if alturas == 1:
    print(f"{1 * manos} Toma final")

if alturas == 2:
    print(f"{1 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final")

if alturas == 3:
    print(f"{1 * manos} Toma paso 15 db")
    print(f"{1 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final")

if alturas == 4:
    print(f"{1 * manos} Toma paso 20 db")
    print(f"{1 * manos} Toma paso 15 db")
    print(f"{1 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final")  

if alturas == 5:
    print(f"{1 * manos} Toma paso 20 db")
    print(f"{2 * manos} Toma paso 15 db")
    print(f"{1 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final") 

if alturas == 6:
    print(f"{2 * manos} Toma paso 20 db")
    print(f"{2 * manos} Toma paso 15 db")
    print(f"{1 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final") 

if alturas == 7:
    print(f"{2 * manos} Toma paso 20 db")
    print(f"{2 * manos} Toma paso 15 db")
    print(f"{2 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final") 

if alturas == 8:
    print(f"{3 * manos} Toma paso 20 db")
    print(f"{2 * manos} Toma paso 15 db")
    print(f"{2 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final") 

if alturas == 9:
    print(f"{3 * manos} Toma paso 20 db")
    print(f"{3 * manos} Toma paso 15 db")
    print(f"{2 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final") 

if alturas == 10:
    print(f"{3 * manos} Toma paso 20 db")
    print(f"{3 * manos} Toma paso 15 db")
    print(f"{3 * manos} Toma paso 10 db")
    print(f"{1 * manos} Toma final") 

if alturas > 10:
    print("Son muchas alturas")