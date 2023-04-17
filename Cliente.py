class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido} tiene {self.edad} años"
    
    def a_diccionario(self):
        return { "nombre": self.nombre, "apellido": self.apellido, "edad": self.edad }