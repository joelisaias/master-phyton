class Persona:
    """
    nombres
    apellidos
    altura
    edad
    """
    def getNombres(self):
        return self.nombres
    def setNombres(self,nombres):
        self.nombres=nombres

    def getApellidos(self):
        return self.apellidos
    def setApellidos(self,apellidos):
        self.apellidos=apellidos

    def getAltura(self):
        return self.altura
    def setAltura(self,altura):
        self.altura=altura

    def getEdad(self):
        return self.edad
    def setEdad(self,edad):
        self.edad=edad

    def hablar(self):
        return "Bla Bla Bla"
    def caminar(self):
        return "Estoy caminando"
    def dormir(self):
        return "ZzZzzzzZZZZzzzzZZZzz"

class Informatico(Persona):
    """
    lenguajes
    experiencia
    """

    def __init__(self):
        super().__init__()#ejecuta el constructor de la clase padre
        self.lenguajes="java,php,javascript,phyton"
        self.experiencia=10
    
    def getLenguajes(self):
        return self.lenguajes
    def setLenguajes(self,lenguajes):
        self.lenguajes=lenguajes

    def getExperiencia(self):
        return self.experiencia
    def setExperiencia(self,experiencia):
        self.experiencia=experiencia


    def programar(self):
        return "Estoy programando"

    def soporte(self):
        return "Estoy dando soporte"