#Brandon Estivenson Castro Contreras T00058678

from abc import ABC,abstractmethod#importamos metodo abstracto
class personajes():#clase padre
    def __int__(self):#se define la clase constructor para tener acceso a todas las instancias
        pass
class caracterizacion(personajes):#clase principal
    @abstractmethod#decorador 
    #creacion de datos para personajes
    def __init__(self,nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.poder = []
        self.habilidades =[]
        self.debilidades = []
        self.personalidad= []
    
    @abstractmethod#decorador
    def atacar(self, objetivo):
        pass
    
    @abstractmethod#decorador
    #declaramos los datos de personaje haciendo su llamado en la clase principal
    def getStatus(self):#definiendo nuevas funciones
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")
    
    def subirNivel(self):#definiendo nuevas funciones
        self.nivel += 1
        
    def MostraInventario(self):#definiendo nuevas funcione
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)
    
    def MostrarPoderes(self):#definiendo nuevas funcion
        print(f"Los poderes de {self.nombre} son: ")
        for objeto in self.poder:
            print(objeto)
            
    def MostrarHabilidades(self):#definiendo nuevas funcion
        print(f"Las habilidades de {self.nombre} son: ")
        for objeto in self.habilidades:
            print(objeto)
            
    def MostrarDebilidades(self):#definiendo nuevas funcion
        print(f"Las debilidades de {self.nombre} son: ")
        for objeto in self.debilidades:
            print(objeto)
        
        
        
class Humano(caracterizacion):#subclase
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 100
        self.armas = 18
        self.inventario = ["Pistola", "Cuchillo","Escudo","Grandas"]
        self.poder = ["Contruir cualquier cosa","Experto en armas","Maestro en las artes marciales y boxeo"]
        self.habilidades = ["Puede durar mas de 30 minutos debajo del agua"]
        self.debilidades = ["Sufre del colón","alergico al maní"]

              
    def getStatus(self):
        print(f"Humano")
        super().getStatus()
        
    def atacar(self, objetivo):
        objetivo.vida -= self.armas*0.6
        print(f"Vida : {objetivo.vida}")

class SuperHumano(caracterizacion):#subclase
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 300
        self.inventario = ["Chocolate", "Cargador","Fusil","Cuchillo"]
        self.poder = ["Super fuerza","Aprueba de balas","Puede llegar a dar saltos hasta de 7 kilometros"]
        self.habilidades = ["Conocimiento en medicina avanzada","ver en la oscuridad"]
        self.debilidades = ["debe comer chocolate dos veces al dia para no ser vurnerable"]

    
    def getStatus(self):
        print(f"SuperHumano")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza*0.8
        print(f"le queda {objetivo.vida} de vida")
              
class Artificiales(caracterizacion):#subclase
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 300
        self.invisibilidad = 95
        self.inventario = ["aumento de poder x2","Invisibilidad"]
        self.poder = ["Super inteligencia", "inmune a todo lo solido"]
        self.habilidades = ["Maestro en construcción"]
        self.debilidades = ["el agua"]


    def getStatus(self):
        print(f"Artificial")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.invisibilidad*0.9
        print(f"le queda {objetivo.vida} de vida")

class Aliens(caracterizacion):#subclase
    def __init__(self,nombre):
        super().__init__(nombre)
        self.vida = 500
        self.telequinesis = 90
        self.inventario =["Super armas"]
        self.poder = ["Puede volar","Regeneración", "vision laser"]
        self.habilidades = ["puede controlar las mentes de los demas"]
        self.debilidades = ["cuando controla la mente de alguien su cuerpo queda inmune hasta que este deje de controlar a la victuima"]

        
    def getStatus(self): 
        print(f"Aliens")
        super().getStatus()
    
    def atacar(self, objetivo):
        objetivo.vida -= self.telequinesis*0.4
        print(f"Le queda {objetivo.vida} de vida")
    


# In[52]:

#Asignación de personajes
humano = Humano('Brandon')
superhumano = SuperHumano('Brandoneltodopoderoso')
artificiales = Artificiales('brandonrakuten')
aliens = Aliens('el rojo')


#Datos
print("\n");
#LLamado a la función
humano.getStatus()
humano.MostraInventario()
humano.MostrarPoderes()
humano.MostrarHabilidades()
humano.MostrarDebilidades()

#Datos
print("\n");
#LLamado a la función
superhumano.getStatus()
superhumano.MostraInventario()
superhumano.MostrarPoderes()
superhumano.MostrarHabilidades()
superhumano.MostrarDebilidades()

#Datos
print("\n");
#LLamado a la función
artificiales.getStatus()
artificiales.MostraInventario()
artificiales.MostrarPoderes()
artificiales.MostrarHabilidades()
artificiales.MostrarDebilidades()

#Datos
print ("\n");
#LLamado a la función
aliens.getStatus()
aliens.MostraInventario()
aliens.MostrarPoderes()
aliens.MostrarHabilidades()
aliens.MostrarDebilidades()

#Datos
print ("\n");
print ("Humano: ");
humano.atacar(aliens)
print ("Superhumano: ");
superhumano.atacar(artificiales)
print ("Artificiales: ");
artificiales.atacar(humano)
print ("Aliens");
aliens.atacar(superhumano)
# In[ ]:



