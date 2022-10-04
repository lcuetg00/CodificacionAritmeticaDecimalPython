import math as ma

class FuenteInformacion:
    def __init__(self):
        self.listaSimbolos = []
        self.listaFrecuencias = []
        self.totalFrecuencias = 0

    def insertar(self, simbolo):
        if simbolo in self.listaSimbolos:
            index = self.listaSimbolos.index(simbolo)
            self.listaFrecuencias[index] = self.listaFrecuencias[index] + 1
            self.totalFrecuencias = self.totalFrecuencias + 1

        # Si el caracter es un salto de linea, hay que insertarlo como 2 espacios
        elif simbolo == "\n":
            # Si el espacio ya estaba insertado, actualizamos su frecuencia +2
            if " " in self.listaSimbolos:
                index = self.listaSimbolos.index(" ")
                self.listaFrecuencias[index] = self.listaFrecuencias[index] + 2
            # Si el espacio no estaba insertamos, lo insertamos y ponemos su frecuencia a 2
            else:
                self.listaSimbolos.append(" ")
                self.listaFrecuencias.append(2)
            self.totalFrecuencias = self.totalFrecuencias + 2

        else:
            self.listaSimbolos.append(simbolo)
            self.listaFrecuencias.append(1)
            self.totalFrecuencias = self.totalFrecuencias + 1

    def imprimirFuente(self):
        print("Fuente de Informacion")
        for i in range(len(self.listaSimbolos)):
            print("Simbolo " + str(self.listaSimbolos[i]) + " Frecuencia " + str(self.listaFrecuencias[i]))

    def imprimirFrecuencias(self):
        print("Frecuencias: ")
        frecuencias = "["
        for i in range(len(self.listaFrecuencias)):
            frecuencias = frecuencias + str(self.listaFrecuencias[i]) + ","
        frecuencias = frecuencias + "]"
        print(frecuencias)

    def imprimirAlfabeto(self):
        print("Alfabeto:")
        alfabeto = ""
        for i in range(len(self.listaSimbolos)):
            alfabeto = alfabeto + str(self.listaSimbolos[i])
        print(str(alfabeto))

    def insertarTexto(self, texto):
        for i in range(len(texto)):
            simbolo = texto[0]
            texto = texto[1:len(texto)]
            self.insertar(simbolo)

    def calcularEntropia(self):
        sumatorio = 0
        for i in self.listaFrecuencias:
            sumatorio = sumatorio + (i * ma.log(i, 2))
        entropia = ma.log(self.totalFrecuencias, 2) - 1 / self.totalFrecuencias * sumatorio
        return entropia

    def imprimirFuenteOrdenadaMayorAMenor(self):
        zipped = zip(self.listaFrecuencias, self.listaSimbolos)
        zipSorted = sorted(zipped, reverse=True)
        for i in range(len(zipSorted)):
            print("Simbolo: '" + zipSorted[i][1] + "' Frecuencia: " + str(zipSorted[i][0]))