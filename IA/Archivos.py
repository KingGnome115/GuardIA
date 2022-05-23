import json 

class Usuario:
    def to_JSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def guardar_json(usuarios):
    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def leer_json():
    try:
        with open('usuarios.json', 'r') as archivo:
            usuarios = json.load(archivo)
            return usuarios
    except:
        return []

user1 = Usuario()
user1.nombre = 'Juan'
user1.contrasena = '123'
user2 = Usuario()
user2.nombre = 'Pedro'
user2.contrasena = '456'

#guardar en el archivo json
#usuarios = [user1, user2]
#guardar_json(usuarios)

#leer datos
usuarios = leer_json()
print(usuarios)
for usuario in usuarios:
    print(usuario['nombre'])
