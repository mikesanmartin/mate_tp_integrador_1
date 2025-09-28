def operaciones_booleanas(valor1, valor2):
    # Operaciones logicas
    resultado_and = valor1 and valor2
    resultado_or = valor1 or valor2
    resultado_not_valor1 = not valor1
    resultado_not_valor2 = not valor2
    resultado_nand = not (valor1 and valor2)
    resultado_nor = not (valor1 or valor2)
    resultado_xor = (valor1 and not valor2) or (not valor1 and valor2)

    # Imprime resultados
    print(f"En base a los valores de verdad ingresados siendo el primer valor {valor1} y el segundo valor {valor2}, los resultados de las operaciones booleanas son los siguientes:")
    print(f"El resultado de la operacion AND es: {resultado_and}")
    print(f"El resultado de la operacion OR es: {resultado_or}")
    print(f"El resultado de la negacion (NOT) del primer valor es: {resultado_not_valor1} y del segundo valor es: {resultado_not_valor2}")
    print(f"El resultado de la operacion NAND es: {resultado_nand}")
    print(f"El resultado de la operacion NOR es: {resultado_nor}")
    print(f"El resultado de la operacion XOR es: {resultado_xor}")