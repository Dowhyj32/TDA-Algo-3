def ruta_eficiente(E, cap, dist):
    estaciones = E + [dist]
    recorrido = []
    pos_actual = 0
    ult_parada = 0
    
    while ult_parada < len(estaciones) - 1:
        sig = ult_parada

        # Avanzar hasta la estación más lejana alcanzable con la capacidad
        while (sig + 1 < len(estaciones)) and (estaciones[sig + 1] - estaciones[pos_actual] <= cap):
            sig += 1

        # Si no se pudo avanzar, el viaje es imposible
        if sig == ult_parada:
            return None

        # Si aún no llegamos al destino, agregamos la parada
        if sig < len(estaciones) - 1:
            recorrido.append(estaciones[sig])

        # Actualizar posición y última parada
        pos_actual = sig
        ult_parada = sig

    return recorrido
    

estaciones = [0,77,120,132,160,186,197,230,245,260,275,300,310,320,330,380,400]
cap = int(input('Ingrese capacidad del tanque: '))
distancia = int(input('Ingrese distancia a recorrer: '))
paradas = ruta_eficiente(estaciones, cap, distancia)

if paradas is None:
    print("No se puede llegar al destino con la capacidad de tanque dada.")
else:
    print(f'Se paró {len(paradas)} veces, en las estaciones {paradas}')
