from kanren import Relation, facts, run, conde, var, eq


# Verifica si x es padre de y
def padres(x, y):
    return conde([padre(x, y)], [madre(x, y)])


# Verifica si x es abuelo de y
def abuelo(x, y):
    temp = var()
    return conde((padres(x, temp), padres(temp, y)))


# Verifica si x, y y son hermanos
def hermano(x, y):
    temp = var()
    return conde((padres(temp, x), padres(temp, y)))


# Verifica si x es tio de y
def tio(x, y):
    temp = var()
    return conde((padre(temp, x), abuelo(temp, y)))


if __name__ == '__main__':

    padre = Relation()
    madre = Relation()

    facts(madre, ("Silvia", "Carlos"),
          ("Silvia", "David"),
          ("Silvia", "Andres"),
          ("Emilia", "Cristina"),
          ("Emilia", "Javier"),
          ("Olivia", "Maria"),
          ("Olivia", "Julia"),
          ("Olivia", "Ivan"),
          ("Olivia", "Angel"),
          ("Martha", "Sofia")
          )
    facts(padre, ("Juan", "Carlos"),
          ("Juan", "David"),
          ("Juan", "Andres"),
          ("Carlos", "Javier"),
          ("Carlos", "Cristina"),
          ("David", "Alejandro"),
          ("David", "Maria"),
          ("David", "Julia"),
          ("David", "Ivan"),
          ("David", "Angel"),
          ("Andres", "Sofia")
          )

    x = var()

    # Los hijos de Juan
    nombre = 'Juan'
    salida = run(0, x, padre(nombre, x))
    print("\nLista de hijos de " + nombre)
    for item in salida:
        print(item)

    # La madre de Carlos
    nombre = 'Carlos'
    salida = run(0, x, madre(x, nombre))[0]
    print("\nMadre de " + nombre + "\n" + salida)

    # Los padred de Andres
    nombre = 'Andres'
    salida = run(0, x, padres(x, nombre))
    print("\nLos padres de " + nombre)
    for item in salida:
        print(item)

    # Los abules de Alejandro
    nombre = 'Alejandro'
    salida = run(0, x, abuelo(x, nombre))
    print("\nLos abulelos de  " + nombre)
    for item in salida:
        print(item)

    # Los nietos de Silvia
    nombre = 'Silvia'
    salida = run(0, x, abuelo(nombre, x))
    print("\nLos nietos de " + nombre)
    for item in salida:
        print(item)

    # Los hermanos de David
    nombre = 'David'
    salida = run(0, x, hermano(x, nombre))
    hermano = [x for x in salida if x != nombre]
    print("\nLos hermanos de " + nombre)
    for item in hermano:
        print(item)

    #Los tios de Maria
    nombre = 'Maria'
    nombre_padre = run(0, x, padre(x, nombre))[0]
    salida = run(0, x, tio(x, nombre))
    salida = [x for x in salida if x != nombre_padre]
    print("\nLos tios de " + nombre)
    for item in salida:
        print(item)
