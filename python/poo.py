def espacios():
    print(
        "___________________________________________________________________________________"
    )


class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"Estas haciendo una llamada desde un {self.modelo}")

    def cortar(self):
        print(f"Cortaste la llamada de tu {self.modelo}")


celular1 = Celular("Apple", "Iphone 15 pro max", "15Mp")
celular2 = Celular("Samsung", "S3 ultra", "50Mp")
celular3 = Celular("Xiaomi", "C13", "100Mp")


celular1.llamar()
celular1.cortar()
espacios()


class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    def saludar(self):
        print(
            f"Hola mi nombre es {self.nombre} y tengo {self.edad} años y mi número de teléfono es {self.telefono}"
        )


persona1 = Persona("William", 28, "3500001010")
persona1.saludar()

persona2 = Persona("Isabel", 50, "3109991010")
persona2.saludar()

espacios()


class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"Hola soy {self.nombre} soy {self.nacionalidad}")


class Estudiante(Persona):

    def __init__(self, nombre, edad, nacionalidad, grado):
        super().__init__(nombre, edad, nacionalidad)
        self.grado = grado

    def estudiar(self):
        print(f"Hola soy estudiante y voy a estudiar estudiando")


class Empleado(Persona):

    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario


# nombre = input("Ingrese nombre: ")
# edad = input("Ingrese edad: ")
# nacionalidad = input("Ingrese nacionalidad: ")
# grado = input("Ingrese grado: ")
# trabajo = input("Ingrese trabajo: ")
# salario = input("Ingrese salario: ")
# estudiante = Estudiante(nombre, edad, nacionalidad, grado)
# empleado = Empleado(nombre, edad, nacionalidad, trabajo, salario)
# estudiante.hablar()
# estudiante.estudiar()
# empleado.hablar()


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"Hi!, my name is {self.name} and make {self.sound}")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Guaaaaf")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Miaaaau")


dog = Dog("Rex")
cat = Cat("Pelusa")

cat.make_sound()
dog.make_sound()
