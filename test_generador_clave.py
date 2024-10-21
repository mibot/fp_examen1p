from generador_clave import obtener_consonantes, generar_clave
import re


def test_generador_clave():
    assert obtener_consonantes("animo") == "nm"
    assert obtener_consonantes("ELEFANTE") == "LFNT"
    assert obtener_consonantes("programacion") == "prgrmcn"

    clave = generar_clave("animo", "elefante", "programacion")

    assert re.match(r'^[A-Z]+(?:1[0-9]|2[0-9]|3[0-9]|4[0-9]|50)$', clave)

    assert len(clave) >= 2, f"Clave demasiado corta: {clave}"

    assert clave[:-2].isupper(), f"No todas las letras están en mayúsculas: {clave}"

    assert not any(letra in "AEIOU" for letra in clave[:-2]), f"La clave contiene vocales: {clave}"

    clave2 = generar_clave("animo", "elefante", "programacion")
    assert clave != clave2, "Las claves generadas no son únicas"

    clave_vocales = generar_clave("aeiou", "AEIOU", "AeIoU")
    assert len(clave_vocales) == 2  # f"Clave incorrecta para palabras con solo vocales: {clave_vocales}"

    print("Todas las pruebas pasaron exitosamente.")


# Ejecutar las pruebas
if __name__ == "__main__":
    test_generador_clave()
