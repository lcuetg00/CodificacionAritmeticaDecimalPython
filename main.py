import math as ma
import fuente as fuenteText
import arbol as arbol
import codificacionaritmetica as codArit
from decimal import *
import decodificacionbinarialineal as decodBinLin

#Recoger el fichero con el texto
def insertarTextoFichero(ruta):
    file = open(ruta, "r", encoding='utf8')
    texto = file.read()
    file.close()

    return texto

#ruta = "C:\\Users\\Luis-PC\\Desktop\\datos6.txt"
fuente = fuenteText.FuenteInformacion()
#texto = insertarTextoFichero(ruta)
texto= "Pensando en eso esta noche, con el corazón y el estó-\n" \
       "mago hechos papilla, me digo a fin de cuentas quizá\n" \
       "eso sea la vida: mucha desesperación pero también algunos\n" \
       "momentos de belleza donde el tiempo ya no es igual. Es\n" \
       "como si las notas musicales hicieran una suerte de parén-\n" \
       "tesis en el tiempo, una suspensión, otro lugar aquí mismo,\n" \
       "un siempre en el jamás.\n" \
       "(LA ELEGANCIA DEL ERIZO, Muriel Barbery)"

#Fuente del texto
print(texto)
fuente.insertarTexto(texto)
print("_______________")
print("Fuente de informacion sin ordenar:")
fuente.imprimirFuente()
print("_______________")
print("Frecuencias:")
fuente.imprimirFrecuencias()
print("_______________")
#print("Fuente de informacion ordenada de menor a mayor:")
#fuente.imprimirFuenteOrdenadaMayorAMenor()
#print("_______________")
entropia = fuente.calcularEntropia()
print("Entropia de la fuente: " + str(entropia))

#Huffman
arbol = arbol.ArbolHuffman()
arbol.crearArbol(fuente.listaSimbolos,fuente.listaFrecuencias,fuente.totalFrecuencias)
arbol.calcularCodificacion(arbol.nodos[0],'')
print("Codificacion de Huffman:")
arbol.imprimirCodificacionMenorMayor()
print("_______________")

fuente.imprimirAlfabeto()

print("Longitud binaria de la fuente (longitud media huffman):")
arbol.calcularLongitudMedia()
longitudMedia = arbol.calcularLongitudMedia()
print(longitudMedia)

eficacia = entropia / longitudMedia #entropia/(ma.log(q, 2) * longitudMedia)

print("Eficacia: " + str(eficacia))
print("_______________________________________________________________________________________")
codificacionArit = codArit.CodificacionAritmetica(fuente.listaSimbolos,fuente.listaFrecuencias)
codificacionArit.calcularParticionBase(fuente.totalFrecuencias)
numero= Decimal("0.938434993679600223922608511494132796026424143844362665527995868729657277")
fraseDecodificada = codificacionArit.decodificarLetra(numero, 57)
print("Frase decodificada:")
print(fraseDecodificada)
print("Particiones y simbolos:")
codificacionArit.imprimirParticionesBase()
print("_______________________________________________________________________________________")






print("________________________________________________________________________________________________________")
print("Decodificacion binaria lineal")
alf="aábcdeé AÁBCDEÉfghiíjklmnFGHIÍJKLMNoópqrstuúvwxyzOÓPQRSTUÚVWXYZ.,;¿?¡!"
mensaje=[0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,1,1,0,1,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1]

lista= [1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0]
generadora = [[1,1,0],[1,0,1],[0,1,1]]
dec = decodBinLin.DecodificacionBinariaLineal(alf, mensaje,generadora,0,3)
decLinPalabras = dec.decodificacionLineal()
mensajeFinal = dec.decodificacionFuente(decLinPalabras)
print(mensajeFinal)
print("________________________________________________________________________________________________________")



