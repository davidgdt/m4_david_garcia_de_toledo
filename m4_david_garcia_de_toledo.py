import pandas as pd

def ejercicio1():
    print("Los primeros 5 elementos de los titulos son: \n")
    titulos = pd.read_csv('imdb_titulos.csv')
    print(titulos.head())   #los 5 primeros se muestran con head(), si quiero mostrar otros primeros, pongo el numero entre parentesis
    
    print("\n\n")
    print("Los primeros 5 elementos del elenco son: \n")
    elenco = pd.read_csv('imdb_elenco.csv')
    print(elenco.head())
    
    print("\n\n")
    #Mostrar el número de registros del dataframe de títulos
    print("El numero de registros de titulos es: ")
    print(titulos.shape[0])  #shape[0] contar el numero de filas

    print("\n\n")
    #Mostrar el número de registros del dataframe de elenco
    print("El numero de registros de elenco es: ")
    print(elenco.shape[0])

    print("\n\n")
    #Mostrar las 5 peliculas más antiguas del listado de titulos
    print("Las 5 peliculas mas antiguas del listado de títulos son:")
    print(titulos.sort_values(by='year').head())  #sort_values(by='year') ordenar por año, head() para mostrar los 5 primeros

    print("\n\n")
    #Mostrar las peliculas que en el titulo tienen la palabra "Dracula". 
    #También mostrar el número total de peliculas que coincidan con este requisito.
    print("Las peliculas que en el titulo tienen la palabra Dracula son: ")
    print(titulos[titulos['title'].str.contains('Dracula')])  #str.contains('Dracula') para buscar la palabra
    print("El numero total de peliculas que coinciden con este requisito es: ")
    print(titulos[titulos['title'].str.contains('Dracula')].shape[0])  #para contar el numero de peliculas que coinciden con el requisito
    
    print("\n\n")
    #Mostrar los 10 titulos más comunes (que más se repiten) en el listado de titulos
    print("Los 10 titulos mas comunes son:")
    print(titulos['title'].value_counts().head(10))  #value_counts() para contar los titulos, head(10) para mostrar los 10 primeros

    print("\n\n")
    #Mostrar cual fue la primera pelicula hecha titulada "Romeo and Juliet"
    print("La primera pelicula hecha titulada Romeo and Juliet es:")
    print(titulos[titulos['title'] == 'Romeo and Juliet'].sort_values(by='year').head(1))  #sort_values(by='year') ordenar por año, head(1) para mostrar el primero

    print("\n\n")
    #Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
    print("Las peliculas que contienen la palabra Exorcist ordenadas de la mas vieja a la mas reciente son:")
    print(titulos[titulos['title'].str.contains('Exorcist')].sort_values(by='year'))  #str.contains('Exorcist') para buscar la palabra, sort_values(by='year') ordenar por año

    print("\n\n")
    #Mostrar cuantas peliculas fueron hechas en el año 1950
    print("El numero de peliculas hechas en el año 1950 es:")
    print(titulos[titulos['year'] == 1950].shape[0])  

    print("\n\n")
    #Mostrar cuantas peliculas fueron hechas de 1950 a 1959
    print("El numero de peliculas hechas de 1950 a 1959 es:")
    print(titulos[(titulos['year'] >= 1950) & (titulos['year'] <= 1959)].shape[0])  #& para buscar entre 1950 y 1959

    print("\n\n")
    #Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
    print("Los roles o papeles que hubo en la pelicula The Godfather son:")
    print(elenco[elenco['title'] == 'The Godfather'])  #category para mostrar los roles
    print("El numero total de coincidencias es:")
    print(elenco[elenco['title'] == 'The Godfather'].shape[0])  #para contar el numero de coincidencias

    print("\n\n")
    #Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
    print("El elenco completo ordenado por la clasificacion n de la pelicula Dracula de 1958 es:")
    print(elenco[(elenco['title'] == 'Dracula') & (elenco['year'] == 1958)].sort_values(by='n'))  #sort_values(by='n') ordenar por n

    print("\n\n")
    #Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
    print("El numero de papeles de Bruce Wayne que han sido hechos en la historia de las peliculas son:")
    print(elenco[elenco['character'] == 'Bruce Wayne'].shape[0])  #para contar el numero de papeles de Bruce Wayne

    print("\n\n")
    #Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
    print("El numero de papeles que ha hecho Robert De Niro en su carrera son:")
    print(elenco[elenco['name'] == 'Robert De Niro'].shape[0])  #para contar el numero de papeles de Robert De Niro

    print("\n\n")
    #Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
    print("El listado de papeles como protagonista que tuvo el actor Charlton Heston en la decada de los 60's es:")
    print(elenco[(elenco['name'] == 'Charlton Heston') & (elenco['n'] == 1) & (elenco['year'] >= 1960) & (elenco['year'] <= 1969)].sort_values(by='year', ascending=False))  #sort_values(by='year', ascending=False) ordenar por año de forma descendente, elenco['n'] == 1 para mostrar los papeles como protagonista
    
    print("\n\n")
    #Mostrar cuantos papeles para actores hubo en la década de los 50's
    print("El numero de papeles para actores que hubo en la decada de los 50's es:")
    print(elenco[(elenco['type'] == 'actor') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)].shape[0])  #para contar el numero de papeles para actores en la decada de los 50's

    print("\n\n")
    #Mostrar cuantos papeles para actrices hubo en la década de los 50's
    print("El numero de papeles para actrices que hubo en la decada de los 50's es:")
    print(elenco[(elenco['type'] == 'actress') & (elenco['year'] >= 1950) & (elenco['year'] <= 1959)].shape[0])  #para contar el numero de papeles para actrices en la decada de los 50's

ejercicio1()

