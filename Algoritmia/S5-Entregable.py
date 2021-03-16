def pedirDatos(nombre, ApellidoPaterno, ApellidoMaterno, clave, salon):
    Datos = {'nombre': 'Luis A.',
            'ApellidoPaterno':'Sixtos',
            'ApellidoMaterno':'Muro',
            'clave':'181949', 
            'salon': '400'
    }
    print(Datos['ApellidoPaterno'], Datos['ApellidoMaterno'], Datos['nombre']) # Nombre Completo: Juan Perez Prado
    print('Mi clave es:', Datos['clave'], end='\n\n') # Clave: 150545
    return Datos
    

datos1 = pedirDatos('Sixtos', 'Muro', 'Luis A.', 181949, 400,)
print(datos1)



