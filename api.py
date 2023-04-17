from fastapi import FastAPI, Response, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, validator #Para crear un modelo de un dato y añadirle validaciones mediante FastAPI
import Clientes

class ModeloCliente(BaseModel):
    nombre: constr(min_length=2, max_length=20)
    apellido: constr(min_length=2, max_length=20)
    edad: constr(min_length=1, max_length=3)

class ModeloCrearCliente(ModeloCliente): #Para agregar validaciones en el modelo de entrada, apoyado del "BaseModel"
    @validator("edad")
    def validar_edad(cls, edad):
        if 18 < int(edad) < 140:
            return edad
        raise ValueError("La edad no puede ser menor a 18 ni mayor a 140")

headers = {"content-type": "charset=utf-8"}

#Al crear la API puedo pasarle campos para añadir en la documentación información
app = FastAPI(
    title="API del Gestor de clientes",
    description="Ofrece diferentes funciones para gestionar clientes"
)

@app.get("/")
async def mi_get():
    contenido = {"mensaje": "¡ Hola Irving con FastAPI ! ¬", "edad": "27"}
    return JSONResponse(content = contenido) #Por defecto es media_type="application/json"

@app.get("/html")
async def html():
    contenido = """
        <h1> Hola Irving </h1>
        <h2> Con un media_type diferente al por defecto, hay muchos tipos de media type ! </h2>
        """
    return Response(content = contenido, media_type = "text/html")

@app.get("/clientes", tags=["Clientes"])  #tags solo para el open api
async def clientes():
    #Transformo una lista en un diccionario con "comprensión de listas", es una lista de diccionarios
    #O en lugar del método poner "{ "nombre": self.nombre, "apellido": self.apellido, "edad": self.edad }", como destructuración de objetos
    contenido = [ cliente.a_diccionario() for cliente in Clientes.Clientes.obtener_clientes() ]
    return JSONResponse(content = contenido)

@app.get("/clientes/buscar/{edad}", tags=["Clientes"])
async def cliente_por_edad(edad: str): #Importante si es un string o entero el dato
    cliente = Clientes.Clientes.obtener_cliente_por_edad(edad)
    if not cliente:
        raise HTTPException(status_code = 404, detail = "No existe cliente con dicha edad")
    return JSONResponse(content = cliente.a_diccionario())


@app.post("/clientes/crear/", tags=["Clientes"])
async def crear_cliente(datos: ModeloCrearCliente): #FastApi permite usar el "BaseModel" para recuperar los datos de la API y/o crear otra clase apoyada del "BaseModel" para validar datos
    cliente = Clientes.Clientes.crear_cliente(datos.nombre, datos.apellido, datos.edad)
    if cliente:
        return JSONResponse(content=cliente.a_diccionario())
    raise HTTPException(status_code = 404, detail = "Cliente no creado")


@app.put("/clientes/actualizar", tags=["Clientes"])
async def actualizar_cliente(datos: ModeloCliente):
    if Clientes.Clientes.buscar_cliente(datos.edad):
        cliente = Clientes.Clientes.actualizar_cliente(datos.nombre, datos.apellido, datos.edad)
        if cliente:
            return JSONResponse(content=cliente.a_diccionario())
    raise HTTPException(status_code=404, detail="Cliente no encontrado en la lista")

@app.delete("/clientes/borrar/{edad}", tags=["Clientes"])
async def borrar_cliente(edad: str):
    if Clientes.Clientes.buscar_cliente(edad):
        cliente = Clientes.Clientes.eliminar_cliente(edad)
        if cliente:
            return JSONResponse(content=cliente.a_diccionario())
    raise HTTPException(status_code=404, detail="No se encontro la edad del cliente para eliminarlo")


print("Servidor de la API(Utilizo uvicorn como servidor para poder levantar la API).... 'pipenv run uvicorn api:app --reload'")
print("Si acceso a mi aplicación '/docs' me genera la documentación de openApi(swagger)")
print("'pipenv requirements' dira las depedencia que utilizamos en el proyecto")
