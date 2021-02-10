def get_data_by_run(run):
    """
    Función que retorna un diccionario con la información personal de un ciudadano Chileno según el RUN que recibe. El RUN debe estar formateado 11.111.111-1
    Requiere: requests, bs4 
    """
    import requests
    from bs4 import BeautifulSoup
    r = requests.post(
        'https://www.nombrerutyfirma.com/rut',
        data={
          'term': run
        }
    )
    contenido_web = BeautifulSoup(r.text, 'lxml')
    tabla = contenido_web.find('table').find('tbody')
    tds = tabla.findAll('td')
    nombre = tds[0].get_text()
    rut = tds[1].get_text()
    sexo = tds[2].get_text()
    direccion = tds[3].get_text()
    comuna = tds[4].get_text()
    response = {
        'nombre': nombre,
        'rut': rut,
        'sexo': sexo,
        'direccion': direccion,
        'comuna': comuna
    }
    return response

print(get_data_by_run('11.111.111-1'))
