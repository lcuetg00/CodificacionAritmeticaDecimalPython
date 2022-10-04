import fractions
from decimal import *

getcontext().prec = 500

class CodificacionAritmetica:
    def __init__(self, simbolos, frecuencias):
        self.simbolos = simbolos
        self.frecuencias = frecuencias
        self.particionBase = []

    # def imprimirSimbolosParticionBase(self):
        # for i in (range(len(self.simbolos)):
            # print("Simbolo ' "+ self.simbolos[0] + "' Particion ")

    def calcularParticionBase(self, numFrecuenciaTotal):
        print("Calcular particion base")
        p1 = 0
        longSimbolos = len(self.simbolos)
        for i in (range(longSimbolos-1)):
            p2 = Decimal(self.frecuencias[i]) / Decimal(numFrecuenciaTotal)
            self.particionBase.append([p1,(p2+p1)])
            p1 = p1 + p2
        self.particionBase.append([p1,1])

    def decodificarLetra(self, num, longitud):
        print("Decodificando letra")
        fraseDecodificada = ""
        for i in range(longitud):
            indexIntervalo= 0
            encontrado = False
            for i in (range(len(self.particionBase))):
                num1 = num
                num2 = self.particionBase[i][1]
                if ((num1 < num2) and (encontrado == False)):
                    fraseDecodificada = fraseDecodificada + self.simbolos[i]
                    indexIntervalo = i
                    encontrado = True

            #Actualizo el dato num = num - Lj / Hj-Lj
            numerador1 = Decimal(num)
            numerador2 = Decimal(self.particionBase[indexIntervalo][0])
            numerador = numerador1 - numerador2
            denominador1 = Decimal(self.particionBase[indexIntervalo][1])
            denominador2 = Decimal(self.particionBase[indexIntervalo][0])
            denominador = denominador1 - denominador2
            num = numerador/denominador

        return fraseDecodificada

    def imprimirParticionesBase(self):
        stringParciones = ""
        for i in range(len(self.particionBase)):
            stringParciones = stringParciones + "Simbolo: " + str(self.simbolos[i] + " " + "Particion: [" + str(self.particionBase[i][0]) +"," + str(self.particionBase[i][1]) + "] \n" )
        print(stringParciones)