import re #libreria de expresiones regulares

path = 'Ciclos_Alumnos.java'

try: 
  #lectura del archivo, pasandolo a una variable
  archivo = open(path, 'r')
except:
  print ('El archivo que intentas abrir no existe')
  quit()

texto = ''

#lectura de lineas del archivo para ser pasados a una variable vacia.
for linea in archivo:
  texto += linea



patron = r"[a-zA-Z][\w\d]*"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
for i in result:
    if(i!="console" and i!="log" and i!="let" and i!="var" and i!="const" and i!="push" and i!="pop" and i!="unshift" and i!="shift" and i!="slice" and i!="splice" and i!="reverse" and i!="split" and i!="join" and i!="sort" and i!="indexOf" and i!="findIndex" and i!="find" and i!="new" and i!="Set"
    and i!="of" and i!="forEach" and i!="some" and i!="every" and i!="lenght" and i!="map" and i!="filter" and i!="reduce" and i!="toFixed" and i!="parseInt" and i!="parseFloat"
    and i!="Math.random" and i!="this" and i!="delete" and i!="Object.getPrototypeOf" and i!="Object.assign" and i!="String.prototype" and i!="hasOwnProperty" and i!="legs" and i!="lastIndex" and i!="includes" and i!="startsWith" and i!="endsWith"
    and i!="replace" and i!="substr" and i!="return" and i!="prompt" and i!="alert" and i!="Array" and i!="break" and i!="case" and i!="catch" and i!="class" and i!="default" and i!="do" and i!="else" and i!="elseif"
    and i!="endsswitch" and i!="eval" and i!="extends" and i!="for" and i!="function" and i!="if" and i!="implements" and i!="include" and i!="instanceof" and i!="interface" and  i!="print"
    and i!="private" and i!="protected" and i!="public" and i!="require" and i!="static" and i!="switch" and i!="throw" and i!="try" and i!="use" and i!="while" and i!="true" and i!="false"):
        print ("\n Ejercicio 1- Variables validas: " +i)

patron = r"([\d]+[.]?[\d])"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 2- Enteros y decimales","\n",result)

patron = r"([+-]|[\/]|[*]|[%])"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 3- Operadores aritm�ticos ","\n",result)

patron = r"<|<=|>=|=|==|!="
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejercicio 4- Operadores relacionales","\n",result)

patron = r"\bint|\babstract|\bassert|\bboolean|\bbreak|\bbyte|\bcase|\bcatch|\bchar|\bclass|\bconst|\bcontinue|\bdefault|\bdo|\bdouble|\belse|\benum|\bextends|\bfinal|\bfinally|\bfloat|\bfor|\bgoto|\bif|\bimplements|\bimport|\binstanceof|\binterface|\blong|\bnative|\bnew|\bpackage|\bprivate|\bprotected|\bpublic|\breturn|\bshort|\bstatic|\bstrictfp|\bsuper|\bswitch|\bsynchronized|\bthis|\bthrow|\bthrows|\btransient|\btry|\bvoid|\bvolatile|\bwhile"
result = re.findall(patron, texto) #busca las coincidencias y devuelve un arreglo
print ("\n Ejericio 5-Palabras reservadas","\n",result)



