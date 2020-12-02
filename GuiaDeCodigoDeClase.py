# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 09:03:12 2020

@author: Lucia
"""
# Clase 1
#%%

print("Hola Mundo")

#%%

x= 3
nombre = "juan"
print(x)
print(nombre)

#%%

x = 3
print(type(x))

#%%

x = "juan"
print(type(x))

#%%

PI = 3.14
IVA = 21

#%%

nombre = input("Ingrese su nombre")
print("Bievenido",nombre)

#%%

edad = int(input("ingrese su edad"))
print("tu edad es:", edad)
edad2 = edad + 1
print("Tu proxima edad es", edad2)

#%%

año = int(input("año de nacimiento"))
edad = 2020 - año
print("Su edad es:", edad)

#%% Tarea clase 1

nombre = input("Ingrese su nombre")
print("Bievenido",nombre, "¿como estas?")

#%% tarea clase 1
a = int(input("inserte un numero"))
b = int(input("inserte el segundo numero"))

sol = a*b
print(sol)
 #%% tarea clase 1

B = int(input("Valor de la base del rectangulo"))
A = int(input("valor de la altura del rectangulo"))

perimetro = 2*(A+B)
altura = A*B

print("la altura es: ",altura,",y el pereimetro es: ", perimetro)
#%%
o = int(input("ingrese numero N°1 "))
p = int(input("ingrese el segundo numero N°2 "))
 # el int te pasa de str a int, es como que te lo pasa a que te lo lea como un numero o unidad sino este codigo no lo leeria
suma = o+p
resta1 = o-p 
resta2 = p-o
multiplicacion = o*p
division1 = o/p
division2 =p/o 

print("la suma es: ",suma) 
print("la resta del N°1-N°2 es: ", resta1)
print("la resta del N°2-N°1 es: ",resta2)
print("la multiplicacion es: ", multiplicacion)
print("la division de N°1/N°2 es: ", division1)
print("la division de N°2/N°1 es: ", division2)

#%%
# Clase 2

print("hola como estan")
'''mensajes latgos
tipo asi
'''
#las variable son contenedores de informacion
#apellido es una variables tipo string o cadena
apellido=input("ingrese apellido")
#el valor quiero que sea un entero y asi agrego int
valor=int(input("ingrese un valor positivo"))
#tambien esta el long y float 
#print e input da valores
#float es para numero con coma, y mas valores que el entero
#si el float no lee la coma uso punto porque los invierte

print("el valor ingresado por el usuario es:", valor)
print(" el apellido ingresado por el usuario es:", apellido)
print("fin del programa")
#%% Desiciones if else

#tabulacion el espacio que queda con el if es todo lo que contiene el if
#tabulacion es el espacio abajo de un codigo
parcial1 =int(input("ingrese nota del primer parcial: "))
parcial2 = int(input("ingrese nota del segundo parcial: "))

if(parcial1 >=4 and parcial2 >=4 ):
    print("el alumno  aprobo")
    #num = int((input("ingrese un valor dentro del if")))
    print("felicidades!")
# no pones tabulacion despues del num por ahora 1 sola tabulacion    
else:
    print("el alumno no aprobo")
    #num = int((input("ingrese un valor dentro del else")))
    print("la proxima es la vencida!")

print("Buenas vacaciones")

#%% intento de agregar unidades
print("ingrese una velocidad valida:")
speed = float(input())
print(speed," km/h ")

#%% agregar unidades

velocidad=input("introduce the speed module ")
unidad=input("introduce the unit ")

#%% expresiones booleanas 
''' x==y esto es dos iguales para una condicion igual
x<y, x<=y, x!=y distinto '''

# conectores and(une), or(o uno u otro) a not (not)

x = int(input("ingrese un numero:"))
if x>0:
    print("numero positivo")
    x=-x
if x<0:
    print("numero no positivo")
    
''' ESTO ESTA MAL'''#y lo sabias :3, diosa!
#%%
    
x = int(input("ingrese un numero:"))
if x>0:
    print("numero positivo")
else:
    if x==0:
        print("igual a 0")
    else:
        print("numero negativo")
    
    

#%%

nota =int(input("ingrese nota del primer parcial "))
if (nota>=7):
    print("Promocionaste")
else:
    if (nota>=4):
       print("aprobe la materia")
    else: 
        print("debes recursar la materia")
        
#servia 2 else
#%% Tarea clase 2

#ingreso de datos
numero = int(input("ingrese el numero entre 1 y 7 inclusive: "))
# proceso de seleccion
if (numero==1):
    print("Lunes")
elif(numero==2):
    print("Martes")
elif(numero==3):
    print("Miercoles")
elif(numero==4):
    print("Jueves")
elif(numero==5):
    print("Viernes")
elif(numero==6):
    print("Sabado")
elif(numero==7):
    print("Domingo")
# y si nada funciona
else:
    print("Fuera de rango, intente nuevamente")
    
#%% EJERCICIO 1
    
A = int(input("ingrese un numero entero: "))
B = int(input("ingrese otro un numero entero: "))   
C = int(input("ingrese otro un numero entero: "))   
D = int(input("ingrese otro un numero entero: "))       
E = int(input("ingrese el un numero entero: "))   
         
print("El maximo es: ",max(A,B,C,D,E)," y el minimo es: ", min(A,B,C,D,E))
#%%

A = int(input("ingrese un numero entero: "))
B = int(input("ingrese otro un numero entero: "))   
C = int(input("ingrese otro un numero entero: "))   
D = int(input("ingrese otro un numero entero: "))       
E = int(input("ingrese el un numero entero: "))

if ( A==B or B==C or C==D or D==E or A==C or A==E or A==D or B==D or B==E or C==E):
    if (A==B):
        print(A,"y",B, "Son duplicados")
    elif(B==C):
         print(B,"y",C,"son duplicados" )
    elif(C==D):
         print(C,"y",D,"son duplicados" )
    elif(D==E):
         print(D,"y",E,"son duplicados" )      
    elif(A==C):
         print(A,"y",C,"son duplicados" )     
    elif(A==E):
         print(A,"y",E,"son duplicados" )     
    elif(A==D):
         print(A,"y",D,"son duplicados" )    
    elif(B==D):
         print(B,"y",D,"son duplicados" )     
    elif(B==E):
         print(B,"y",E,"son duplicados" )    
    elif(C==E):
         print(C,"y",E,"son duplicados" )   
    print("hay duplicados")    
else:
    print("Son todos distintos:", A, B, C, D, E)

#%% elif(va a dejar la estructura en la primera condicion verdadera)
#%% Clase 3 for y range
for i in range(7):
    print(i, end=',')
#%% sin for no vez las componentes
secuencia=range(7)
print(secuencia)
for i in range(7):
     print(i)
#por si sola da secuencias de 1 numero por renglon
#range(start, stop, step): no olvidar los :
     
#%%
     
for i in range(1, 10,2):
    print(i)


#%%tarea me piden 1o numeros y quiero la suma


A = int(input("ingrese un numero entero: "))
B = int(input("ingrese otro un numero entero: "))   
C = int(input("ingrese otro un numero entero: "))   
D = int(input("ingrese otro un numero entero: ")) 
E = int(input("ingrese otro un numero entero: "))   
F = int(input("ingrese otro un numero entero: "))   
G = int(input("ingrese otro un numero entero: "))       
H = int(input("ingrese otro un numero entero: "))  
j = int(input("ingrese otro un numero entero: "))
K = int(input("ingrese el un numero entero: "))   

print(A+B+C+D+E+F+G+H+j+K)

# yo haria asi la tarea
#%%
#como se hace
acumulador = 0
for i in range(10):
   numero = int(input('Ingrese un numero:'))
   #acumulador = acumulador + numero
   acumulador += numero # me va acumulando
print(acumulador)

#%% variante profe i se puede llamar posicion
acumulador = 0
for i in range(1,11):
   numero = int(input('Ingrese el numero ubicado en la posicion %i:' %(i))) #ayuda a saber que numero esta poniendo
   #acumulador = acumulador + numero
   acumulador += numero # me va acumulando
print(acumulador)

#%%while
nota = 5 # solo hace que se cumpla la condicion
while nota <=9:
      nota = int(input("ingrese su nota:"))
print('sali')

# con 10 recien salis de esta permanencia

#%%
gato = 0
respuesta =input("¿Quiere agregar otro gato? ")
while (respuesta=="si"):
    gato+= 1 # suma lo de al lado
    respuesta=input("¿quiere agregar otro gato?")
print("cantidad de gatos:",gato)

#%%
cantidad_de_gatos=int(input("ingresa la cantidad de gatos viky"))
cantidad_de_gatos_final=0
while cantidad_de_gatos!="0":
    cantidad_de_gatos_final+= cantidad_de_gatos
    cantidad_de_gatos=int(input("ingresa la cantidad de gatos viky"))
print("la sed de venganza esta saceada")
print("Viki lanzo", cantidad_de_gatos_final, "gatos")
# no me gusta tanto
#%%

vocales = 'aeiouAEIOU'

while True:
    v=input("ingrese una vocal: ")
    if v in vocales:
        break
    print("no es una vocal. ingrese nuevamente!")
print("gracias")

#no les gusta
#%%
#estesi

vocales = 'aeiouAEIOU'
letra = input("ingrese una vocal")
while letra not in vocales:
    print("no es una vocal. ingrese nuevamente!")
    letra =input("ingrese una vocal")
print("gracias")

#%%algo mal
nombre=input("ingrese su nombre:")
altura =int(input("ingrese su altura en centimetros= "))
if((altura > 170)  and (altura<190)):
   print("aprobado")
else:
    print("rechazado")


#%%
    
año = int(input("ingrese año: "))
if (año%4==0 and año % 100 != 0 or año % 400==0): # el año%4==0 me dice que el año lo divido por 4 y quiero resto 0
    print("Año bisiesto")
else:
    print("Año no bisiesto")

#%%
#print() 
#print  en dos espacios deja el lugar
#%% tarea del molesto de martin ):<
    
numero= int(input("Inserte el numero que desee: "))
fact = 1

for i in range(2,numero+1):
    fact = fact * i


print(fact)


#%% Factorial con while
numero = int(input("ingrese un numero entero: "))

if numero < 0:
    print("numero positivo porfitas")
elif numero == 0 or numero == 1:
    print(1)
else:
    nu = 1
    while numero > 1:
        nu = nu*numero
        numero = numero - 1 #variable de control: romper la condicion de while
    
              
print(nu)

"""
1er iteracion(numero = 5):
    nu = 1(nu) * 5(numero)
    
2da iteracion(numero = 4):
    nu = 5(nu anterior) * 4(numero restado)
"""

while n < 20 and n > 5:
#%% funciona peo me da un error feo

#texto = "Primer intento"
#print(texto)
#texto2=texto.replace("Primer","Segundo")# sin el igual no funca
#print(texto2)
#%%
nombre= "lucia"
edad="22" 
print(f"{nombre} tiene {edad} años")
#%%
lista= ["juan","dos","piedras"]
print("--".join(lista))# une la lista de arriba

#%%
text = "juancito come panchos"
print(text.split()) #si text.split("o") devuelve el texto sin o
#%%
lista=[4,3,5,2,6,8,9]
lista=sorted(lista) #igualar sino no andaesta lista.sort() que ordena
print(lista)
#%%
matriz=[[1,2,3],[2,3,4],[1,-1,1]]
print(matriz)
for i in matriz:
    print(i) #hace mas matriz
#%%
megalista=[[4,2,5],[1,2],[1,8,2,]]
for i in range(len(megalista)):
    for j in range(len(megalista[i])):
        print(megalista[i][j]) #muestra e orden los elementos en vertical
        print("i vale",i)
        print("j vale",j)# te dice que lugar ocupa de la matriz
#%%
def fun_nono():
    print("soy una funcion")
#%% funciones
def fun_nosi():
    Nombre = input("Ingrese su nombre su nombre: ")
    return(Nombre)
Nomb = fun_nosi()
print("buenos dias", Nomb)
#%%
def fun_sisi(nomb):
    print("buenos dias", nomb)
    apell= input(nomb+", cual es tu apellido")
    return(apell)

nombre=input("ingrese su nombre:" )
#%% funcion factorial
def fun_factorial (k):
    fac = 1
    if(k>1):
        for i in range (k,1,-1):
            fac *= i
    return fac
m= int(input("ingrese M: "))
n= int(input("ingrese n<m: "))

fac_m = fun_factorial(m)
fac_n = fun_factorial(n)
fac_mn = fun_factorial(m-n)
comb = fac_m/(fac_n*fac_mn)
print("combinaciones de %2d tomados de %2d es = %5d" % (m,n,comb))

#%% def de la funcion combinatoria
def fun_combinatoria (a,b,c):
    combina = a/(b*c)
    return combina
m= int(input("ingrese M: "))
n= int(input("ingrese n<m: "))

fac_m = fun_factorial(m)
fac_n = fun_factorial(n)
fac_mn = fun_factorial(m-n)
comb = fun_combinatoria(fac_m,fac_n,fac_mn)      
print("combinaciones de %2d tomados de %2d es = %5d" % (m,n,comb))   

#%%
def fun_prueba(a,b):
    print("llegue a la funcion")
    print("valores recibidos del programa:", a ,b)
    a*= 3
    B+= 7
    print("valores modificados de la funcion:", a,b)# si a y b los llamo igual van a sgeuir siendo distintas porque ocupan lugares distintos en el programa
    print("salgo de la funcion")

M = int(input("ingrese m:"))
N = int(input("ingrese N:"))
print( "estoy en el programa")
print(" valores del porograma:", M, N)

fun_prueba(M,N):
    
    
    
#%% funcion repulsiva
def fun_factorial(K):
    if(K<2):
        fac = 1
    else:
        fac = K* fun_factorial(K-1)
    return fac
m= int(input("ingrese M: "))
n= int(input("ingrese n<m: "))

fac_m = fun_factorial(m)
fac_n = fun_factorial(n)
fac_mn = fun_factorial(m-n)
comb = fac_m/(fac_n*fac_mn)
print("combinaciones de %2d tomados de %2d es = %5d" % (m,n,comb))
#%% repaso de lista
lista = [77024,"lucia","costa"]
#        0    1        2 
print("catidad de elementos",len(lista)) #len me diice la cantidad de elementos recorda va de 0 a n-1
 # recorrer los elementos
for elemento in lista:
    print(elemento)
# recorre los lugares de elemento es decir de 0 a 3
for i in range(4):
    print(i)
for i in range (len(lista)):#igual al primer for
        print(lista[i])
        
lista.append(10)# agrega
print(lista)
print(len(lista))

lista.pop(1)# saca un elemento
print(lista)

#encuentra el indice de lo que buscas
print("indice: ",lista.index("lucia"))
# saco un elemento sin saber donde esta porque se su indice
buscar= input(" que queres buscar ")
if buscar in lista:
    print("indice: ",lista.index(buscar))
else:
    print("No esta en la lista")    

print(lista)
#%% lista de listas
puntos= [[2,4],[3,5],[8,8]]
punto=[4,1]
puntos.append(punto) # agrega punto al final
print(puntos)

for puntito in (puntos):
    print(puntito)
for i in range(len(puntos)): # sin lend no anda( aca estas inicando ana hasta la suma de tyodosos lso elementos de punto)
    print(puntos[i])
#LEND ES EL LARGO DE LA LIST CUENTA LOS ELEMENTOS DE LA LITA
#%%
'''1º Ejercicio a resolver:
Crear un programa que permita generar un tablero de
nxn en el cual que la diagonal se muestre con “#” mientras
que el resto de las casillas deben mostrar “*”.
Pedir al usuario que ingrese una coordenada (fila y columna).
Si el casillero tiene un “*” cambiarlo a “#”.
Si tiene un “#” mostrar un mensaje que diga “la diagonal es del alfil”
Si elige el mismo casillero más de una vez mostrar un mensaje que diga
“¿¿¿Pero que estas haciendo???”'''

# un chico hizo este
def casillero():
    tablero=[["#","*","*"],["*","#","*"],["*","*","#"]]
    #el usuario tiene eque ingresar la coordenada, es decir una fila y una columna
    fil=int(input("ingrese el numero de la fila: "))
    col=int(input("ingrese el numero de la columna: "))

    valor=tablero[fil][col]
    if valor =="#": #si el valor esta en la diagonal imprime este mensaje
        print("La diagonal es del alfil ")


    elif valor=="*":
        #cambia el 2 "*" `por un "#" porque el valor no esta en la
#%% misma tarea
# yo hice este
def tablero():
n = int(input("Ingrese el numero de fila y columnas: \n"))
for i in range(n):
    for j in range(n):
        if i==j:
            print("#")
        else:
            print("*")
print(tablero) # no me salio :()
#%% profes
tablero = []
ingresadas = []
tamanio = int(input("Ingrese el tamaño del tablero (n): "))
for i in range(tamanio):
#    print("i = ",i)
    fila = []
    for j in range(tamanio):
#        print("j = ",j)
        if i == j:
            fila.append("#")
        else:
            fila.append("*")
#    print("Agrego fila",i)
    tablero.append(fila)
#print(tablero)
corte = 's'
while corte != 'n':
    print(" ",end =" ")
    for i in range(len(tablero)):
        print(f"   {i+1}",end=" ")
    print()
    for fila in range(len(tablero)):
        print(f"{fila+1} {tablero[fila]}")
    fila = int(input("Ingrese fila: "))-1
    columna = int(input("Ingrese columna: "))-1
    if [fila,columna] in ingresadas:
        print("Que haces????")
    else:
        if tablero[fila][columna] == "*":
          tablero[fila][columna] = "#"
        elif tablero[fila][columna] == "#":
            print("La diagonal es del alfil")
    ingresadas.append([fila,columna])
    corte = input("Seguir? s/n: ")
#%% tarea con martin
# 1. (Con funciones) Cree un programa que permita al usuario elegir entre
# las siguientes opciones:
# Agregar un alumno: debe solicitarse nombre,padron y nota.
# Consultar aprobados: debe mostrar los alumnos con nota
# mayor a 4.
# Cantidad de alumnos totales y promedio general.
# Quitar a un  alumno.
# Salir
# 2. Crear un programa que permita ingresar una cadena
# de caracteres como “******A**” con una longitud de
# caracteres múltiplo de 3.
# El programa debe devolver una cadena de caracteres
# en la cual cada “*” es reemplazado por la inicial de un color.
# Deben usarse todos los colores y no pueden haber más de dos caracteres vecinos
# del mismo color.
# Colores: 1azul (“A”), verde(“V”), rojo(“R”)
#%%
'''A)Haga  un  programa carga tres  valores.  El  programa poseeuna función 
querecibe3  valores  y  devuelveel  mayor.  El  programamuestra por pantalla 
el mayor.(NOsepuedeusar la función max )'''  
#el usuario ingresa 3 valores no decimales no negativos para poder ejecutar la funcion
a=int(input("ingrese un valor: "))
b=int(input("ingrese un valor: "))
c=int(input("ingrese un valor: "))
#ahora buscamos definir una funcion que solo me muestre el maximo de los 3 valores pedidos
def funcion_maxima(a,b,c):
   # vengo a encontrar las condiciones
    if a<b and c<b:
        maximo=b
        print("el maximo es: ",maximo)
    elif b<a and c< a:
        maximo1=a
        print("el maximo es: ",maximo1)
    else:
        maximo2=c
        print("el maximo es: ",maximo2)
        
funcion_maxima(a,b,c)

#%%otro intento
# estoy tratando de pedir los 3 valores ahorrando espacio
#flagIngreso = 1
#for i in range(0,3):
#   ingrese=int(input("ingrese un valor: "))
    
flagIngreso = 0
i = 0
ingresoMax = 0

while(i < 3):   
    ingreso = int(input("Ingrese un valor: "))
            
    if (ingreso > ingresoMax or flagIngreso == 0):
        
        ingresoMax = ingreso
        flagIngreso = 1
        
    i = i + 1   

print("Valor maximo ingresado ", ingresoMax)
    
#%%e
'''E)Haga un programa carga un valor que es un ángulo expresado en radianes. El programa poseeuna 
función querecibeeste dato y lo muestra  expresado en grados,  minutos  y  segundos(a° b’c’’).
La función muestra el resultado. (Puedenusar la función math.pi)'''
import math
angulo=  float(input("ingrese un valor de angulo: "))

angulo = angulo * math.pi

print(angulo)

def funcion_grados(angulo):
            
    grados= angulo * (180/math.pi)
    print(int(angulo))
    decimales = abs(grados - int(grados)) #
    minutos= decimales * 60
    decimalesmin = abs(minutos - int(minutos))
    segundos= decimalesmin * 60
        
    print(grados,"°",minutos,"'",segundos,"''")
    

funcion_grados(angulo)
#%%
'''B) Haga un programa carga cuatro valores. El programa posee una función que hace la sumatoria de los mismos y
 devuelve la suma. El programa muestra por pantalla el resultado.'''
def sumaNumeros():
    
    acumulador = 0
    for i in range(0,4):
        ingrese=int(input("ingrese un valor: "))
        
        acumulador = ingrese + acumulador #Acumulador: variable que permite "acumular" un valor sea resultado de una operacion o de una concatenacion de caracteres
    print(acumulador)

sumaNumeros()
#%% como usar la funcion

a = int(input("ingrese num1: "))
b = int(input("ingrese num2: "))


def comparacion(a,b):
    suma = a + b
    
    print(suma)


comparacion(a,b)
#%% Clase 6
''' mi intento de hacer el epromedio de 10 valoes'''

def promedio():
    
    acumulador = 0
    for i in range(0,10):
        ingrese=int(input("ingrese un valor: "))
        
        acumulador = ingrese + acumulador
    
    resultado = acumulador/10
    print(resultado)
promedio()
#%%
''' Se quiere conocer el promedio y la nota mas alta de un curso de computacion para el cual el usuaurio
para  lo cual el usuario ingrese el nro de padron y nota del alumno'''

def usuario():
    alumno = 1
    acumulador = 0
  
    ingresenota=float(input(" ingrese nota del pibe: "))
    ingresepadron=int(input("ingrese el padron del alumno: "))
    maximo=ingresenota
    flagmaximo=0
    
    while (ingresenota>=0 and ingresenota<=10):
        alumno = alumno + 1
        acumulador = ingresenota + acumulador
        
        if ingresenota>maximo or flagmaximo==0:
            maximo=ingresenota
            flagmaximo = 1
            padronmaximo = ingresepadron
        ingresenota=float(input(" ingrese nota del pibe: "))
        ingresepadron=int(input("ingrese el padron del alumno: "))
        


    print("maxima nota del curso desastre: ", maximo, "y su padron es: ", padronmaximo)    
    print("cantidad de alumnos: ", alumno-1)
    promedio = acumulador/ (alumno-1)
    print("promedio del curso desastroso:", promedio)
usuario()
        
    
    
    
# la idea seria tomar la primera nota como maximo y luego ir comparando con las siguientes notas
#, si es mas grande lo cambias si es mas chico lo descartas
#%%
''' se tiene cuatro cursos con n alumos en cada uno (condicion de corte cuando el alumno es nombre* y nota es -1)'''
'''a, promedio de notas c/curso.. b nota mas baja de cada curso( es unica), indicar el alumno. c) promediogeneral. d) promedio mas alto a que curso pertenece'''
def curso():

sumaprom = 0
promM = 0
cursoM = 0
for i in range (1,5):
    print ()
    curso = "Curso " + str(i)
    print ("Usted está en el ", curso)
    print ("Ingrese alumno: '*' y nota: -1 para salir de este curso")
    alumno = input("Ingrese el padrón o el nombre del alumno: ")
    nota = int(input("Ingrese la nota del alumno: "))
    alumnos = 0
    notaB = nota
    alumnoB = alumno
    suma = 0
    while (alumno != "*" and nota != -1):
        if (nota < notaB):
            notaB = nota
            alumnoB = alumno
        suma += + nota
        alumnos += 1
        print ()
        print ("Ingrese alumno: '*' y nota: -1 para salir de este curso")
        alumno = input("Ingrese el padrón o el nombre del alumno: ")
        nota = int(input("Ingrese la nota del alumno: "))
    prom = suma/alumnos
    sumaprom += prom
    if (prom > promM):
        promM = prom
        cursoM = "Curso " + str(i)
    print ()
    print ("El promedio del ",curso," es: ", prom)
    print ("La nota más baja es: ", notaB, ", del alumno: ", alumnoB)
promgral = sumaprom/4
print ()
print ("El promedio general de los 4 cursos es: ", promgral)
print ()
print ("El curso con mayor promedio es el ", cursoM, "con un promedio de: ", promM)

#%% 
'''hacer la tabla del 1 al 10'''
for i in range (0,11):
    for j in range (0,11):
        
        valor= j*i
        print(j," x",i,"=", valor)
#%% ver si es par  o impar el i en la tabla del 2
for i in range (0,11):
    if  i % 2==0:
        print(i,"es par")
    else:
        print(i,"es impar")
        
    valor= 2*i
    print("2 x",i,"=", valor)
#%%
''' cree un programa que permita al usuario elegir entre las sisguientres opciones:
1) agregar un alumno: debe solicitar nombre padron y nota
2) consultar aprobados: debe mostrar los alumnos con nota mayor a 4
3) cantidad de alumnos totales y promedio general
4) indicar cual es la nota maxima, elpadron y el nombre del alumno
5) quitar a un alumno
6) salir'''
#necesito una funcion agrega alumnos y saca alumnos, una funcion que muestre aprobados y una funcion total(main) 
#1)
listaalum=[]
    
def agrega(listaalum):
    
    alumnos = []
    nombre = input("Ingrese el nombre del pendejo: ")
    padron = int(input("Ingrese padron del pendex: "))
    nota = float(input("Ingrese nota del wachinchin: "))
    
    alumnos.append(nombre)
    alumnos.append(padron)
    alumnos.append(nota)
    listaalum.append(alumnos)
    
#2)    
def consultarAprobados():
    for alumnos in listaalum:
        if alumno[2] > 4:
            print("Alumno: ", alumnos[0], " Padron: ", alumnos[1], " Nota: ", alumnos[2])
           
            

def quitar(listaalum, padron):
    
    for alumnos in listaalum:
        if(alumnos[1] == padron):
            listaalumn.remove(alumnos)
        else:
            print("Alumno no existente")
            
    print("Alumno removido exitosamente")
        
def cantAlumnos(listaalum):
    x = len(listaalum)
    print("Cantidad de alumnos: ")          


def notaMax(listaalum):
    notasMayores = []
    for alumnos in listaalum:
    
        notasMayores.append(alumno[2])    
    notaMax = max(notasMayores)
    
    for alumnos in listaalum:
        if (alumnos[2] == notaMax):
            print("Nota maxima: ", notaMax, " pertece a: ", alumnos[0])
            
    

def promedioGral(listaalum):
    suma = 0
    for alumnos in listaalum:
        suma = alumnos[2] + suma
    
    promedio = suma / cantAlumnos(listaalum) 
    return promedio

def menu():
    print("---Bienvenido al menu xdddd---")
    print("")
    print("1-- Ingresar alumno")
    print("2-- Mostrar aprobados")
    print("3-- Cantidad de alumnos")
    print("4-- Promedio general")
    print("5-- Lista de notas maximas")
    print("6-- Quitar alumno")
    print("0-- Salir del programa")
    print("------------------------------")
    
    opcion = int(input("Ingrese una opcion"))
    while opcion < 0 and opcion > 6:
        
        opcion = int(input("Ingrese una opcion"))
                     
    return opcion

def seleccion():
    opcion = 1
    while opcion > 0 and opcion < 7:
        opcion = menu()
        if opcion == 1:
            agrega(listaalum)
        elif opcion == 2:
            consultarAprobados(listaalum)
        elif opcion == 3:
            cantAlumnos(listaalum)
        elif opcion == 4:
            promedioGral(listaalum)
        elif opcion == 5:            
            notaMax(listaalum)
        else:
            padron = int(input("Ingrese el padron de alumno a remover: "))
            quitar(listaalum, padron)           
        op = menu()
                
        
                 
    
def main():
    listaalum = []
    salir = False
    seleccion()
    
    
    
    print("Terminated")
    
    return 1
    
main()
#%% ejercicio parcial
'''3) Dada la pandemia mundial que nos atraviesa, Presidencia de la Nación nos solicita armar un sistema para poder
controlar la evolución de contagios y fallecimientos a causa del COVID-19 en cada una de las provincias que integran
la República Argentina.
Para ello el sistema deberá permitir, a demanda del usuario, ingresar la provincia, la cantidad de infectados, la cantidad
de fallecidos, la población total y la cantidad de testeos realizados.
Luego el programa deberá permitir emitir los siguientes reportes:
a) La cantidad total de fallecidos a nivel país en provincias que tengan más de 100 contagiados
b) Provincia con mayor cantidad de testeos
c) Provincia con menor tasa de contagio por habitante
d) Cantidad de provincias con Testeos mayor al testeo promedio por provincia.'''

    
listacontagios = []    

def ingresar(listacontagios):
    continuar = True
    while continuar:    
        contagios=[]
        provincia=input("ingrese nombre de provincia: " )
        infectados=int(input("ingrese la cantidad de infectados: "))
        fallecidos=int(input("ingrese numero de fallecidos: "))
        poblacion=int(input("ingrese la poblacion de provincia: "))
        testeos=int(input("ingrese la cantidad de testeos hechos: "))
    
        contagios.append(provincia)#0
        contagios.append(infectados)
        contagios.append(fallecidos)
        contagios.append(poblacion)
        contagios.append(testeos)
        listacontagios.append(contagios)
        opcion= input("desea agregar mas provincias s/n: ")
        if opcion=="n":
            continuar= False
    
ingresar(listacontagios)

#def canfallecidos(listacontagios):    
    
    
    
    
def maxdetesteo(listacontagios):
    testeomax=[]
    for contagios in listacontagios:
        
        testeomax.append(contagios[4])        
    maxtesteo = max(testeomax)    
        
    for contagios in listacontagios:
        if(contagios[4]==maxtesteo):
            print("testeos maximos hechos: ",maxtesteo,"y corresponde a la provincia ", contagios[0])
        
maxdetesteo(listacontagios)
    
   
#def contagiosxhabi


def totalfallecidos(listacontagios):
    if len(listacontagios) >0:
        cant=0
        for contagios in listacontagios:
            cant+= contagios[2]
            print("la cantidad de falelcidos son: ", cant)
        else:
             print("falta agregar datos")
totalfallecidos(listacontagios)






#%% .lower te deja todo en minuscula, y split ()cada palabra nos la va a separar como un elelemenyo de la lista
#%%
''' ejericio 4 parcial 1  Realizar un programa que le solicite una frase al usuario y luego un término para buscar. El sistema deberá imprimir
por pantalla las palabras de la frase que comienzan con el término que el usuario buscó.
Ej: ‘mi capacidad para resolver parciales es interminable’
Luego el usuario puede buscar el término: par
El sistema deberá imprimir por pantalla las palabras: para parciales'''

def ingresar():
    lista_palabras = []
    
    for i in range(5):
        print("Ingrese palabra ", i + 1, ":")
        palabra = input().lower()
        lista_palabras.append(palabra)
        
    return lista_palabras

def buscador(lista_palabras, palabra_clave):
    
    for palabra in lista_palabras:
        letras_encontradas = []
            
        for letra in palabra:
            if(letra in palabra_clave and letra not in letras_encontradas):
                letras_encontradas.append(letra)
        if(len(letras_encontradas) == len(palabra_clave)):
            print(palabra)
                
    
def main():
    
    palabra_inicial = input("Ingrese una palabra inicial: ").lower()
    lista_palabras = ingresar()
    buscador(lista_palabras, palabra_inicial)
        
    
main()   
    
    #%%
''' ejercicio c practica de funciones enunciado: Haga un programa carga dos
 valores. El mismo posee una función que recibe los valores,
 si el primero es mayor que el segundo hace la suma caso contrario 
 realiza el producto. El programa muestra por pantalla el resultado.'''
 
a = int(input(" ingrese el primer valor: "))
b = int(input(" ingrese el segundo valor: "))

def prueba():

    if a > b:
        resultado= a+b
        print("la suma es: ",resultado)
    else:
        c= a * b
        print("El producto es: ",c)
prueba()
#%%
'''d. Haga un programa carga cinco valores. El programa posee una función
 que recibe los cinco valores y devuelve el menor. El programa muestra por
 pantalla el mayor. (NO se puede usar la función max)'''
    
i=0 
ingresomin = 0
while(i<5):
    valores=float(input("Ingrese un valor: "))
    
    if valores > ingresomin:
        ingresomin= valores
    i= i+1
print("El valor minimo es: ", ingresomin)

#%%
''' f). Haga un programa carga un valor que es un ángulo expresado en
 grados, minutos y segundos (a° b’ c’’). El programa posee una función que 
 recibe los tres valores y lo pasa a radianes. El programa muestra el
 resultado. (Pueden usar la función math.pi)'''
 
import math
grados= float(input(" ingrese el valor del grado:  "))
minutos= float(input(" ingrese el valor del minuto:  "))
segundos= float(input(" ingrese el valor del segundo:  "))

def funcion_radianes(grados, minutos, segundos):
   gradoentero = grados +(minutos/60)+(segundos/3600)
   radianes=(gradoentero*math.pi)/180
   print(gradoentero)
   print(radianes)
funcion_radianes(grados, minutos, segundos)
#%%
'''g). Haga un programa carga los dos catetos de un triángulo rectángulo. 
El programa posee una función que recibe los catetos y calcula la hipotenusa
 y uno de sus ángulos. La función muestra por pantalla La hipotenusa y 
el ángulo calculado en ° ‘ “. (Pueden usar las funciones math.atan(),
 math.sqrt, math.pow)'''
# math.sqrt es la raiz 
#math.pow(x,y) y es x elevado a la y
 
def triangulo(a,b):
    a=float(input(" ingrese el lado a del triangulo: "))
    b= float(input("ingrese el lado b del triangulo: "))
    hipotenusa= math.sqrt((a**2)+(b**2))
    angulo= math.atan(b/a)# no estoy segura
    decimales = abs(angulo - int(angulo))                                    '''duda'''
    minutos= decimales * 60
    decimalesmin = abs(minutos - int(minutos))
    segundos= decimalesmin * 60
    
    print("el largo de la hipotenusa es: ", hipotenusa)
    print("y el angulo es: ",angulo,"°",minutos,"'",segundos,"''")
    
triangulo(a,b)
#revisar puede dar en radianes
#%%
''' o. Haga un programa que recibe n valores positivos. La carga la hace el 
programa y arma una lista, finaliza cuando ingresa un 0 (cero).
La lista pasa a una función que calcula el máximo y la posición.
 La función pasa la lista a una segunda función que calcula el prmedio,
 el cual devuelve a la primera. La primera devuelve máximo, posición y 
 promedio al programa. El programa muestra los resultados por pantalla. 
 (NO se puede usar funciones de Python)'''


def maxi():
    respuesta=int(input(" ingrese el primer valor positivo: "))
    valormax =0
    contador =0
    while respuesta != 0:
        respuesta=int(input("ingrese el siguiente valor: "))                 '''duda'''
        if respuesta > valormax:
            valormax = respuesta
            contador = contador + 1
        
        print("valor maximo es: ",valormax, "la posicion es: ", contador)
maxi()
            
    
def promedio():
   promedio = 0
   promedio+= respuesta
   contador+=1
   prom= promedio/ contador
   print("el promedio es: ", prom)
promedio()
      
#%%

'''h) Haga un programa carga un número complejo expresado como un binomio (a + bi) 
a y b son reales. El programa posee una función que recibe los dos valores y 
pasa el complejo de la forma binomial a la polar (ρ, ω). La función los
 muestra el resultado por pantalla. (Pueden usar las funciones math.atan(), 
 math.sqrt, math.pow)'''

                                                         #duda
import math
def funcion_compleja():
    a= float(input("ingreseel valor a de a+bi: "))
    b=float(input("igrese el valor b de a+bi: "))               

    modulo= math.sqrt((a**2+b**2))
    angulo = math.atan(b/a)
    print("La forma polar es:",modulo, "e^", angulo,".i")
funcion_compleja()
#%%









































































