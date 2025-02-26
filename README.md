# README

## Nombres
Sara Castrillón Sánchez, Isabel Acevedo Acosta

## Numero de clase
 Clase SI2002-2 (7309) clase del miercoles

## Desarrollo

- **Sistema Operativo:**: macOS 13
- **Lenguaje:** Phyton 3.x
- **Herramientas utilizadas:** 
  - Visual Studio Code
  - Interprete de Python 3.x

## Instrucciones de Ejecución
Primera forma:
1. Descargar o clonar
2. tener instalado Python 3
3. Ejecutar, y abrir la terminal donde está el archivo `"minimize_dfa.py"
4. Poner la entrada

Segunda forma:
1. Poner la entrada en el archivo input.txt
2. Abrir la terminal
3. POner en esta el comando python3 minimize_dfa.py < input.txt


## Explicacion del algoritmo
Este codigo minimiza un DFA encontrando pares de estados equivalentes, estados que para cualquier cadena de entrada se comportan igual (aceptan o rechazan). 
## Explicación General del Algoritmo

El algoritmo implementado se utiliza para minimizar un autómata finito determinista (DFA) mediante la identificación de estados equivalentes. 
Se recogen los datos de entrada (número de estados, alfabeeto, estados finales y tabla de transiciones) para estructurarlos y que el programa pueda trabajar con ellos

Se hace una tabla para comparar todos los pares de estados. inicialmente se marcan aquellos pares en los que uno de los estados es final y el otro no, ya que estos estados son diferentes. Despues el algoritmo revisa cada par de estados no marcados y examina sus transiciones para cada símbolo del alfabeto, si para alguna transición los dos estados llevan a un par que ya se marco como diferente, entonces se marca el par actual como distinguible.

Ya para acabarr los pares que permanecen sin marcar son considerados equivalentes, ya que no existe ninguna entrada que permita diferenciarlos,esos son los estados que pueden juntarse para obtener un DFA minimizado.


