from filmoteca import inicializar_contadores, agregar_pelicula, mostrar_estadisticas


def test_filmoteca():
    inicializar_contadores()

    agregar_pelicula("1", 120, 1000000)  # Drama
    agregar_pelicula("2", 90, 800000)  # Comedia
    agregar_pelicula("3", 110, 750000)  # Terror
    agregar_pelicula("4", 130, 1200000)  # Ficción
    agregar_pelicula("1", 140, 900000)  # Drama

    mostrar_estadisticas()

    print("Todas las pruebas pasaron exitosamente.")


if __name__ == "__main__":
    test_filmoteca()
