
class DecodificacionMonoalfabetica:
    def __init__(self, alfabeto, mensajeCifrado, cifradoA, cifradoB):
        self.alfabeto = alfabeto
        self.mensajeCifrado = mensajeCifrado
        self.modulo = len(alfabeto)
        self.cifradoA = cifradoA
        self.cifradoB = cifradoB
        self.descifradoA = pow(cifradoA,-1,self.modulo)
        self.descifradoB = ((-self.descifradoA) + self.cifradoB) % self.modulo


    @property
    def descifrarMensaje(self):
        mensajeDescifrado = ""
        clave = 1
        for i in range(len(self.mensajeCifrado)):
            posicion = self.alfabeto.find(self.mensajeCifrado[i])
            claveA=self.descifradoA % self.modulo
            claveB=self.descifradoB % self.modulo
            index = (posicion * claveA) + claveB
            index = index%self.modulo
            mensajeDescifrado = mensajeDescifrado + self.alfabeto[index]
            if(i>0 and self.mensajeCifrado[i] == self.mensajeCifrado[i-1] and self.alfabeto[index] == " "):
                clave=clave+1
                self.a = pow(self.cifradoA,clave,self.modulo)
                self.b = (self.cifradoB * clave) %self.modulo
                self.descifradoA = pow(self.a, -1, self.modulo)
                self.descifradoB = ((-self.descifradoA) * self.b) % self.modulo

        return mensajeDescifrado

