#Ejercicio - Realizar una calculadora

def calcular(operando1, operando2, operador):
    resultado = 0

    match operador:
        case 1:
            resultado = operando1 + operando2
        case 2:
            resultado = operando1 - operando2
        case 3:
            resultado = operando1 * operando2
        case 4:
            try:
                resultado = operando1 / operando2
            except:
                print("Error, division no valida")
        case _:
            print("Opcion no valida")
            
    return resultado
    

def main():
    print("--- Calculadora ---")

    operando1 = float(input("Introduce el primer operando: "))
    operando2 = float(input("Introduce el segundo operando: "))

    operacion = int(input("Selecciona la operacion a realizar" + "\n" + 
                        "1- Sumar" + "\n" +
                        "2- Restar" + "\n" +
                        "3- Multiplicar" + "\n" +
                        "4- Dividir"))

    resultado = calcular(operando1, operando2, operacion)

    print(f"Resultado: {resultado}" )

main()

