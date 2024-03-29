def arithmetic_arranger(lista_Operaciones, print_Resultados=False):
    
    if len(lista_Operaciones) > 5:
        return "Error: Too many problems."

    prueba = []
    lista = lista_Operaciones
    for i in range(0, len(lista)):
    
        dic2 = {}
        espacios = ""
        espacios =  lista[i].index(" ")
        
        primero = lista[i][0:espacios]
        dic2["primero"] = primero

        operador = lista[i][espacios+1:espacios+2]
        dic2["operador"] = operador

        if dic2["operador"] == "*" or dic2["operador"] == "/":
            return "Error: Operator must be '+' or '-'."

        segundo = lista[i][espacios+3:]
        dic2["segundo"] = segundo

        if (dic2["primero"].isdigit() and dic2["segundo"].isdigit()) == False:
            return "Error: Numbers must only contain digits."

        if (len(dic2["primero"]) and len(dic2["segundo"])) > 4:
            return "Error: Numbers cannot be more than four digits."

        if dic2["operador"] == "+":
            resultado = int(dic2["primero"]) + int(dic2["segundo"])
        else:
            resultado = int(dic2["primero"]) - int(dic2["segundo"])
        dic2["resultado"] = resultado

        if len(dic2["primero"]) > len(dic2["segundo"]):
            grande = dic2["primero"]
        else:
            grande = dic2["segundo"]

        ancho = len(grande) + 2

        barra = ""
        for i in range (ancho):
            barra += "-"
        dic2["barra"] = barra

        espacio1 = len(barra) - len(primero)
        espacios1 = ""
        for i in range(espacio1):
            espacios1 += " "
        dic2["espacio1"] = espacios1

        espacio2 = len(barra) - len(segundo) - 1
        espacios2 = ""
        for i in range(espacio2):
            espacios2 += " "
        dic2["espacio2"] = espacios2

        espacio3 = len(barra) - len(str(resultado))
        espacios3 = ""
        for i in range(espacio3):
            espacios3 += " "
        dic2["espacio3"] = espacios3

        prueba.append(dic2)

    lenDic = len(prueba)
    linea1 = ""
    linea2 = ""
    linea3 = ""
    linea4 = ""
    separacion = "    "

    for i in range(lenDic-1):
        linea1 += str(prueba[i]["espacio1"]) + str(prueba[i]["primero"]) + separacion
        linea2 += str(prueba[i]["operador"]) + str(prueba[i]["espacio2"]) + str(prueba[i]["segundo"]) + separacion
        linea3 += str(prueba[i]["barra"]) + separacion

    fin = 0
    while fin < 1:
        linea1 += str(prueba[lenDic-1]["espacio1"]) + str(prueba[lenDic-1]["primero"])
        linea2 += str(prueba[lenDic-1]["operador"]) + str(prueba[lenDic-1]["espacio2"]) + str(prueba[lenDic-1]["segundo"])
        linea3 += str(prueba[lenDic-1]["barra"]) 
        fin += 2

    fin = 0

    if print_Resultados == True:
        for i in range(lenDic-1):
            linea4 += str(prueba[i]["espacio3"]) +str(prueba[i]["resultado"]) + separacion
        
        while fin < 1:
            linea4 += str(prueba[lenDic-1]["espacio3"]) + str(prueba[lenDic-1]["resultado"]) 
            fin += 2

        junto = linea1+ "\n" + linea2  + "\n" + linea3  + "\n" +  linea4

    else:
        junto = linea1+ "\n" + linea2  + "\n" + linea3 
    
    return junto
