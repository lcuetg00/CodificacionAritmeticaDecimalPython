import math as ma

class DecodificacionBinariaLineal:
    def __init__(self, alfabeto, mensaje, generadora, posIdentidad, longitudIdentidad):
        self.alfabeto = alfabeto
        self.mensaje = mensaje
        self.generadora = generadora
        #posIdentidad tendra 2 valores:
        #0 si la identidad esta a la izquierda
        #1 si la identidad esta a la derecha
        self.posIdentidad = posIdentidad
        #self.base = base

        self.longitudBloque = ma.ceil(ma.log(len(alfabeto), 2)) #longitud minima de cada letra

        #longitudPalabraCodigo = el tamanyo que utilizaremos para dividir el mensaje para la decodificacion lineal
        self.longitudPalabraCodigo = len(generadora[0])+longitudIdentidad #columnas de la matriz
        self.numColumnas = len(generadora[0]) #columnas de la matriz
        self.numFilas = len(generadora) #filas de la matriz (numero de letras como (a,b,c,...) que utilizare

    def devolverCodificacionPosicionAlfabeto(self, binario):
        index = int(binario,2)
        letra = self.alfabeto[index]
        return letra

    def decodificacionLineal(self):
        numIteraciones = ma.floor(len(self.mensaje)/self.longitudPalabraCodigo)

        #Compruebo si la ultima columna no tiene la longitud de la palabra entera
        if(len(self.mensaje) % self.longitudPalabraCodigo != 0):
            numIteraciones = numIteraciones + 1

        listaPalabras = []
        #Troceamos el mensaje
        for i in (range(numIteraciones)):
            palabras = self.mensaje[:self.longitudPalabraCodigo]
            self.mensaje = self.mensaje[self.longitudPalabraCodigo:len(self.mensaje)]
            listaPalabras.append(palabras)


        #Ahora lo vuelvo a trocear, utilizando las propiedades que tiene la matriz generadora y su identidad
        if(self.posIdentidad == 0):
            for i in (range(numIteraciones)):
                if(len(listaPalabras[i]) == self.longitudPalabraCodigo):
                    listaPalabras[i] = listaPalabras[i][:self.numFilas] #Cortamos hasta la posicion que necesitamos por la izquierda
        else:
            negativo = -(self.numFilas)
            for i in (range(numIteraciones)):
                if(len(listaPalabras[i]) == self.longitudPalabraCodigo):
                    listaPalabras[i] = listaPalabras[i][:negativo] #Cortamos hasta la posicion que necesitamos para conseguir la parte del final

        stringPalabras=''
        #Combino la lista en un String:
        for i in (range(len(listaPalabras))):
            stringPalabras = stringPalabras + ''.join(map(str,listaPalabras[i]))

        return stringPalabras

    def decodificacionFuente(self, stringPalabras):
        #troceamos la codificacion lineal por el tamanyo que tengan las palabras del alfabeto (longitudBloque)
        numPalabras = len(stringPalabras)
        numIteraciones = numPalabras / self.longitudBloque
        numIteraciones = int(numIteraciones)


        listaPalabras = []
        # Troceamos el mensaje con la longitudBloque
        for i in (range(numIteraciones)):
            palabras = stringPalabras[:self.longitudBloque]
            stringPalabras = stringPalabras[self.longitudBloque:len(stringPalabras)]
            listaPalabras.append(palabras)

        mensajeDescodificado = ''
        i=0
        for i in (range(len(listaPalabras))):
            letra = self.devolverCodificacionPosicionAlfabeto(listaPalabras[i])
            mensajeDescodificado = mensajeDescodificado + '' + letra

        return mensajeDescodificado