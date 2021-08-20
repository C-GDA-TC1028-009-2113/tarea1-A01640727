def main():
    #escribe tu código abajo de esta línea
    peso_in = float(input("Dame el peso inicial: "))
    peso_fin = float(input("Dame el peso final: "))
    meses = int(input("Dame la cantidad de meses: "))
    por_mes = (peso_in - peso_fin)/meses
    print("Lo que debes bajar por mes es:",por_mes)




if __name__ == '__main__':
    main()
