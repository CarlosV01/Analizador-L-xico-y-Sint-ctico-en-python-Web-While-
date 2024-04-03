import ply.yacc as yacc
from analizador_lexico import tokens

# resultado del analisis
resultado_gramatica = []



def p_expresion(p):
    '''
    expresion : WHILE PARIZQ IDENTIFICADOR MAYORQUE ENTERO PARDER LLAIZQ LLAIZQ
              | IDENTIFICADOR PARIZQ COMDOB IDENTIFICADOR COMDOB PARDER PUNTOCOMA PUNTOCOMA
              | LLADER LLADER
    '''
    if len(p) == 31:  # Regla para la primera expresión
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14], p[15], p[16], p[17], p[18], p[19], p[20], p[21], p[22], p[23], p[24], p[25], p[26], p[27], p[28], p[29], p[30])
        print("El for es correcto")
    elif len(p) == 15:  # Regla para la segunda expresión
        p[0] = (p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8], p[9], p[10], p[11], p[12], p[13], p[14],)
    else:  # Regla para la tercera expresión
        p[0] = (p[1],)




def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format(str(t.type), str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico: {}, CODE IS CORRECT".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sintáctico
parser = yacc.yacc()


def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica


if __name__ == '__main__':
    while True:
        try:
            s = input(''' while(a>1){
                          print("Compiladores");
                          } ''')
        except EOFError:
            continue
        if not s:
            continue

        prueba_sintactica(s)
