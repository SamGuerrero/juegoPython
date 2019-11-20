def error(mensaje):
    print()
    for i in range(100):
        print ("/", end="")
        
    print("\n" + mensaje)
    
    for i in range(100):
        print ("/", end="")
        
    print()

def clase():
    return ["Fuego", "Planta", "Agua"]

def muestra_estadisticas(jugador):
    print(" Vida:", jugador["vida"],
      "\n Ataque:", jugador["ataque"],
      "\n Defensa:", jugador["defensa"],
      "\n Clase:", jugador["habilidad"])

def inicio():
    try:
        from random import randrange, choice

        jugador = {"vida": 0, "ataque": 0, "defensa": 0, "habilidad": 0}

        V = randrange(50, 100)
        A = randrange(30, 50)
        D = randrange(30, 50)
        H = choice(clase())

        jugador["vida"] = V
        jugador["ataque"] = (A-10, A)
        jugador["defensa"] = (D-20, D)
        jugador["habilidad"] = H

        return jugador
    
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en inicio")
    except IndentationError:
        error("Error de indentación en inicio")
    except NameError:
        error("Has llamado a algo no definido en inicio")
    except SyntaxError:
        error("Error de sintaxis en el método inicio")

def enemigo(jugador, poder):
    try:
        from random import choice

        enemigo = {"vida": 0, "ataque": 0, "defensa": 0, "habilidad": 0}

        enemigo["vida"] =  round(jugador["vida"]*poder)

        #Me aseguro de que el ataque del enemigo no tenga valores negativos
        a = round(jugador["ataque"][1]*poder)
        if (a-10 > 0):
            enemigo["ataque"] = (a-10, a)
        else:
            enemigo["ataque"] = (0, a)

        #Me aseguro de que la defensa del enemigo no tenga valores negativos
        d = round(jugador["defensa"][1]*poder)
        if (d - 20 > 0):
            enemigo["defensa"] = (d-20, d)
        else:
            enemigo["defensa"] = (0, d)
        enemigo["habilidad"] = choice(clase())

        return enemigo
    
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en enemigo")
    except IndentationError:
        error("Error de indentación en enemigo")
    except NameError:
        error("Has llamado a algo no definido en enemigo")
    except SyntaxError:
        error("Error de sintaxis en el método enemigo")

def trampa(jugador):
    try:
        from random import randrange
        #Hago constantes lo que le voy a quitar a cada uno
        AT = 0.1
        DE = 0.1
        VI = 0.2

        n = randrange(1, 4)
        print("\n¡Has caído en una trampa!", end=" ")
        if (n == 1):
            #Pierde 10% de ataque
            a = round(jugador["ataque"][1] - (jugador["ataque"][1] * AT))
            jugador["ataque"] = (a-10, a)
            print("Pierdes un",(AT*100),"% de ataque")

        elif (n == 2):
            #Pierde 10% de defensa
            d = round(jugador["defensa"][1] - (jugador["defensa"][1] * DE))
            jugador["defensa"] = (d-20, d)
            print("Pierdes un",(DE*100),"% de defensa")

        else:
            #Pierde 20% de vida
            v = round(jugador["vida"] - (jugador["vida"] * VI))
            jugador["vida"] = v
            print("Pierdes un",(VI*100),"% de vida")
            
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en trampa")
    except IndentationError:
        error("Error de indentación en trampa")
    except NameError:
        error("Has llamado a algo no definido en trampa")
    except SyntaxError:
        error("Error de sintaxis en el método trampa")
        

def recompensa(jugador):
    try:
        from random import randrange
        #Hago constantes lo que le voy a quitar a cada uno
        AT = 0.2
        DE = 0.2
        VI = 0.3

        n = randrange(1, 4)
        if (n == 1):
            #Pierde 10% de ataque
            a = round(jugador["ataque"][1] + (jugador["ataque"][1] * AT))
            jugador["ataque"] = (a-10, a)
            print("Recibes un",(AT*100),"% de ataque")

        elif (n == 2):
            #Pierde 10% de defensa
            d = round(jugador["defensa"][1] + (jugador["defensa"][1] * DE))
            jugador["defensa"] = (d-20, d)
            print("Recibes un",(DE*100),"% de defensa")

        else:
            #Pierde 20% de vida
            v = round(jugador["vida"] + (jugador["vida"] * VI))
            jugador["vida"] = v
            print("Recibes un",(VI*100),"% de vida")
    
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en recompensa")
    except IndentationError:
        error("Error de indentación en recompensa")
    except NameError:
        error("Has llamado a algo no definido en recompensa")
    except SyntaxError:
        error("Error de sintaxis en el método recompensa")

def combate(jugador, poder):
    try:
        enemi = enemigo(jugador, poder)

        print("\n¡Te encontraste con un enemigo!")
        muestra_estadisticas(enemi)

        #Atacamos primero
        ventaja(jugador, enemi)
        lucha(jugador, enemi, "enemigo")
        while (enemi["vida"] > 0) and (jugador["vida"] > 0): #Si el enemigo sigue vivo, nos ataca. Si hemos muerto, acaba
            lucha(enemi, jugador, "jugador")
            lucha(jugador, enemi, "enemigo")
            
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en combate")
    except IndentationError:
        error("Error de indentación en combate")
    except NameError:
        error("Has llamado a algo no definido en combate")
    except SyntaxError:
        error ("Error de sintaxis en el método combate")

def lucha(uno, dos, atacado):
    try:
        from random import randrange

        print("\n¡A luchar!")
        daño = randrange(uno["ataque"][0], uno["ataque"][1]) #El ataque aleatorio del atacante
        daño -= randrange(dos["defensa"][0], dos["defensa"][1]) #Menos la defensa aleatoria del atacado

        if (daño > 0):
            dos["vida"] -= daño
        else:
            daño = 0

        print("El", atacado ," recibe:", daño, "de daño")
        
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en lucha")
    except IndentationError:
        error("Error de indentación en lucha")
    except NameError:
        error("Has llamado a algo no definido en lucha")
    except SyntaxError:
        error("Error de sintaxis en el método lucha")

def ventaja(jugador, enemigo):
    try:
        VEN = 0.1

        clases = clase() #["Fuego", "Planta", "Agua"]
        c = clases.index(enemigo["habilidad"]) #Devuelve la posición dónde se encuentra su habilidad

        if ( clases[c-1] == jugador["habilidad"] ): #Si la habilidad del jugador se encuentra una posición anterior, significa que el jugador tiene ventaja
            print("Qué suerte, tienes ventaja sobre el enemigo")
            #Aumentamos el ataque del jugador
            a = round(jugador["ataque"][1] + jugador["ataque"][1]*VEN)
            jugador["ataque"] = (a-10, a)

        elif (enemigo["habilidad"] != jugador["habilidad"]): #Como son tres habilidades, si el jugador no vence y no son iguales: vence el enemigo
            print("Mala suerte, el enemigo tiene ventaja sobre ti")
             #Aumentamos el ataque del enemigo
            a = round(enemigo["ataque"][1] + enemigo["ataque"][1]*VEN)
            enemigo["ataque"] = (a-10, a)

        else:
            print("\nNadie tiene ventaja en el combate")
            
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en ventaja")
    except IndentationError:
        error("Error de indentación en ventaja")
    except NameError:
        error("Has llamado a algo no definido en ventaja")
    except SyntaxError:
        error("Error de sintaxis en el método ventaja")

def adivinanza(jugador):
    try:
        from random import randrange
        num = randrange(1, 10)

        print("\nTe has encontrando con EL PESADO")
        print("Buenas viajero, para seguir avanzando has de adivinar el número que estoy pensando.")
        print("Pero te advierto, alma mía: Cada vez que falles, te quitaré 5 puntos de vida")
        res = int(input("Introduce un número del 1 al 10: "))
        while ((jugador["vida"] > 0) and (num !=res)):
            jugador["vida"] -= 5
            res = int(input("Fallaste dame un número del 1 al 10: "))

        if (jugador["vida"] > 0):
            print("\nPuedes pasar")
        else:
            print("\nMala suerte, ahora vas a morir")
            
    except NameError:
        error("Has llamado a algo no definido en adivinanza")
    except TypeError:
        error("Estás haciendo operaciones tipo incorrecto en adivinanza")
    except IndentationError:
        error("Error de indentación en adivinanza")
    except SyntaxError:
        error("Error de sintaxis en el método adivinanza")

def eleccion(jugador):
    while(True):
        try:
            from random import choice

            print("Te encuentras con una señora mayor que necesita ayuda. ¿Qué haces?")
            res = int(input("1. La ayudas\n2. Pasas de ella\n3. La matas\n:"))

            while ((res < 1) or (res > 3)):
                print("Elige 1, 2 o 3. No es tan difícil chaval")
                res = int(input("1. La ayudas\n2. Pasas de ella\n3. La matas\n:"))

            if (res == 1): #Ayudas a la señora
                historia = choice(["Buena", "Mala"]) #Cuando te acercas, la señor apuede ser buena o mala

                if (historia == "Mala"):
                    print("\nJa ja, aún tengo dotes de seducción - La señora era una estafadora")
                    trampa(jugador)
                else:
                    print("\nHas sido muy amable, toma joven, esto para ti")
                    recompensa(jugador)

            elif (res == 2): #Pasas de la señora
                historia = choice(["Muerte", "Enfado"]) #Al pasar de la señora, esta puede morirse o enfadarse

                if (historia == "Muerte"): #Si se muere aparece su nieta y llora mucho
                    print("\nLa señora se muere delante de ti, podías haberla salvado. Ahora quedará para siempre en tu conciencia")
                    print("Oh no, parece que tenía nietos, una joven con una capa roja se acerca a su inerte cuerpo y rompe a llorar")
                    print("La niña de no más de 12 años llora desconsoladamente")
                    print("Llora mucho\nMuchísimo")
                    print("-Sin mi abuelita, mi hermano y yo nos moriremos de hambre")
                    print("Sigue llorando")
                    accion = input(("¿Te acercas a consolarla? (S/N): "))
                    while ((not accion == "S") and (not accion == "N")):
                        accion = input(("¿Te acercas a consolarla? (S/N): "))

                    if (accion == "S"): #Si la intentas consolar, resulta que eran estafadoras y te tienden una trampa
                        print("\nLa abuelita y la niña eran estafadoras")
                        trampa(jugador)
                    else: #Si pasas de ella, se piensa que la has matado tú, se convierte en loba y empezáis un combate
                        print("\n-Tú mataste a mi abuela, prepárate a morir.- La niña se convierte en loba")
                        combate(jugador, 0.6)

                else: #Si se enfada empezais un combate
                    print("\n¡Tienes que aprender a respetar a tus mayores niñato! ¡Joder, la vieja sabe karate!")
                    combate(jugador, 0.6)

            elif (res == 3): #Matas a la señora
                print("\nLa señora en su juventud había sido campeona de Kung Fu, lo tendrás complicado para matarla")
                combate(jugador, 0.6)

            break

        except TypeError:
            error("Has cometido un error de tipo en eleccion")
            break
        except ValueError:
            error("Tienes que introducir un número")
        except IndentationError:
            error("Error de indentación en eleccion")
            break
        except NameError:
            error("Has llamado a algo no definido en eleccion")
            break
        except SyntaxError:
            error("Error de sintaxis en el método prueba3")
            break

def comprobacion(jugador):
    try:
        if (jugador["vida"] <= 0):
            print("\nHas muerto :(")
            muestra_estadisticas(jugador)
            return False
        else:
            print("\nSigues vivo. Continúa :D")
            muestra_estadisticas(jugador)
            return True
        
    except IndentationError:
        error("Error de indentación en comprobacion")

def eligePuerta(puertas, cont):
    while (True):
        try:
            print()
            for i in range(100):
                print ("*", end="")
            print ("\nElige una puerta", puertas, " para la prueba", cont, end=": ")

            #Compruebo que mete una puerta correcta porque tiene que parecer que lo elige para algo
            p = int(input())
            while (p not in range(1, len(puertas) + 1)):
                print ("Elige una puerta", puertas, end=": ")
                p = int(input())
            break
        except ValueError:
            error("Debes introducir un número")
        except SyntaxError:
            error("Error de sintaxis en el método eligePuerta")
            break
        except NameError:
            error("Has llamado a algo que no existe en el método eligePuerta")

def prueba1(puertas):
    try:
        from random import randrange

        #Le doy a elegir una puerta por piedad, pero no le servirá de nada, porque es aleatorio todo
        eligePuerta(puertas, 1)
        print("\nHas entrado en la Jungla de lo desconocido")

        num = randrange(1, 4) #La aletoriedad
        if (num == 1):
            trampa(jugador) 
        elif (num == 2):
            combate(jugador, 0.4)
        else:
            adivinanza(jugador)

        if comprobacion(jugador):
            prueba2(puertas)
        else:
            print("\nDe todas formas no necesitabamos un fontanero")
        
    except IndentationError:
        error("Error de indentación en prueba1")
    except SyntaxError:
        error("Error de sintaxis en el método prueba1")
    except NameError:
        error("Has llamado a algo que no existe en el método prueba1")

def prueba2(puertas):
    try:
        #Le doy a elegir una puerta por piedad, pero no le servirá de nada, porque se va a cruzar con una señora y ya pues aleatorio
        eligePuerta(puertas, 2)

        eleccion(jugador)

        if comprobacion(jugador):
            prueba3(puertas)
        else:
            print("\nDe todas formas no necesitabamos un fontanero")
      
    except IndentationError:
        error("Error de indentación en prueba2")
    except SyntaxError:
        error("Error de sintaxis en el método prueba2")
    except NameError:
        error("Has llamado a algo que no existe en el método prueba2") 

def prueba3(puertas):
    try:
        from random import randrange

        #Le doy a elegir una puerta por piedad, pero no le servirá de nada, porque es aleatorio todo
        eligePuerta(puertas, 3)
        print("\nHas entrado en el templo maldito")

        num = randrange(1, 4) #La aletoriedad
        if (num == 1):
            print("Encontraste un cofre")
            recompensa(jugador) 
        elif (num == 2):
            print("He aquí el demonio de fuego")
            combate(jugador, 0.7)
        else:
            print("Este es el verdadero enemigo")
            adivinanza(jugador)

        if comprobacion(jugador):
            for i in range(100):
                print ("~", end="")
            print("\n¡Enhorabuena salvaste el reino!")
        else:
            print("\nDe todas formas no necesitabamos un fontanero")
            
    except IndentationError:
        error("Error de indentación en prueba3")        
    except SyntaxError:
        error("Error de sintaxis en el método prueba3")
    except NameError:
        error("Has llamado a algo que no existe en el método prueba3")

#Main
try:
    #Crea al jugador, le saluda y muestra sus estadísitcas
    jugador = inicio()
    print("Buenas jugador, el reino necesita tu ayuda.")
    muestra_estadisticas(jugador)
    
    puertas = [1, 2, 3]
    prueba1(puertas)
    
except IndentationError:
    error("Error de indentación en el Main")
except NameError:
    error("Has llamado a algo no definido en el Main")
except SyntaxError:
    error ("Error de sintaxis en el método Main")