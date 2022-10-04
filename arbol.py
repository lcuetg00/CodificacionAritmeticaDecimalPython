import math as ma
import decimal
import fractions

class Nodo:
    def __init__(self, simbolo, frecuencia, nodoIzquierdo = None, nodoDerecho = None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.nodoIzquierdo = nodoIzquierdo
        self.nodoDerecho = nodoDerecho

class ArbolHuffman:
    def __init__(self):
        self.nodos = []

    def crearArbol(self,simbolos, frecuencias, totalFrecuencias):
        self.totalFrecuencias = totalFrecuencias
        for i in range(len(simbolos)):
            self.nodos.append(Nodo(simbolos[i],frecuencias[i]))

        while len(self.nodos) > 1:
            #Ordeno de menor a mayor todos los nodos en cada iteracion
            self.nodos = sorted(self.nodos, key=lambda x: x.frecuencia)

            #Recojo los nodos que voy a juntar
            nodoDerecho = self.nodos[0]
            nodoIzquierdo = self.nodos[1]
            sumaFrec = nodoIzquierdo.frecuencia + nodoDerecho.frecuencia
            sumaSimb = nodoIzquierdo.simbolo + nodoDerecho.simbolo
            nodoCombinado = Nodo(sumaSimb,sumaFrec, nodoIzquierdo, nodoDerecho)

            self.nodos.remove(nodoIzquierdo)
            self.nodos.remove(nodoDerecho)

            #Lo inserto al final de la lista
            #No importa en que posicion este ya que se ordenara en la siguiente iteracion
            self.nodos.append(nodoCombinado)

    codificacion = []
    simbolos = []
    frecuencias = []
    def calcularCodificacion(self, nodo, codigo):
        if(nodo.nodoIzquierdo):
            codRamaIz = codigo + '0'
            self.calcularCodificacion(nodo.nodoIzquierdo, codRamaIz)
        if(nodo.nodoDerecho):
            codRamaDer = codigo + '1'
            self.calcularCodificacion(nodo.nodoDerecho, codRamaDer)
        #Llegamos a una hoja del arbol, donde tenemos la letra
        if(not nodo.nodoIzquierdo and not nodo.nodoDerecho):
            self.simbolos.append(nodo.simbolo)
            self.frecuencias.append(nodo.frecuencia)
            self.codificacion.append(codigo)

    def imprimirCodificacionMenorMayor(self):
        zipped = zip(self.codificacion, self.simbolos)
        zipSorted = sorted(zipped, key=lambda x: len(x[0]))
        for i in range(len(zipSorted)):
            print("Simbolo: '" + zipSorted[i][1] + "' Codificacion: " + str(zipSorted[i][0]))

    def calcularLongitudMedia(self):
        long=0
        for i in range(len(self.simbolos)):
            #long = long + ((self.frecuencias[i] / self.totalFrecuencias) * len(self.codificacion[i]))
            long = long + fractions.Fraction(self.frecuencias[i],self.totalFrecuencias)*len(self.codificacion[i])
        return long

    def calcularEficacia(self, entropia, longitudMedia):
        eficacia = entropia/(ma.log(2, 2) * longitudMedia)
        return eficacia