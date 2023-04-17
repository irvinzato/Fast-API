from Cliente import Cliente

lista = [Cliente("Irving", "Rivera", "27"), Cliente("Mauricio", "Silva", "28"), Cliente("Angeles", "Lopez", "51")]

class Clientes:

    def obtener_clientes():
        return lista
    
    def obtener_cliente_por_edad(edad):
        for cliente in lista:
            if cliente.edad == edad:
                print("Cliente encontrado")
                return cliente
            
    def crear_cliente(nombre, apellido, edad):
        cliente = Cliente(nombre, apellido, edad)
        lista.append(cliente)
        return cliente
    
    def buscar_cliente(edad):
        for cliente in lista:
            if edad == cliente.edad:
                print("********** Encontre a un cliente ", cliente)
                return cliente
            
    def actualizar_cliente(nombre, apellido, edad):
        for indice,cliente in enumerate(lista):
            if edad == cliente.edad:
                print("--------- Tengo indice y cliente", indice, cliente)
                print(lista[indice])
                lista[indice].nombre = nombre 
                lista[indice].apellido = apellido 
                lista[indice].edad = edad 
                return lista[indice]
            
    def eliminar_cliente(edad):
        for indice,cliente in enumerate(lista):
            if edad == cliente.edad:
                cliente = lista.pop(indice)
                return cliente

if __name__ == "__main__":
    Clientes.obtener_cliente_por_edad("27")