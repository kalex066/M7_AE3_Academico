from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField (max_length= 100)
    email = models.EmailField (unique=True)

    def __str__(self):
        return  f"Estudiante: {self.nombre}"

class Profesor(models.Model):
    nombre= models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return  f"Profesor: {self.nombre}"

class Perfil(models.Model): #relacion uno a uno con estudiante
    estudiante = models.OneToOneField(
        Estudiante,
        on_delete = models.CASCADE,#si borro el estudiante borra su perfil tambien
        related_name = 'perfil'
    )
    biografia = models.CharField(max_length=200, blank=True, null=True)
    foto = models.TextField(max_length=20, blank=True, null=True)
    redes_sociales = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.estudiante.nombre}"

class Curso(models.Model): #relacion uno a muchos entre curso y profesor

    nombre = models.CharField(max_length=100) #DEFAULT CURRENT_TIMESTAMP
    descripcion = models.TextField()
    #clave primaria
    profesor = models.ForeignKey(
        Profesor, #Clase con la que me estoy relacionando
        on_delete = models.CASCADE, #Al borrar mi profesor se borran sus cursos
        related_name = 'cursos'
    )
    estudiante = models.ManyToManyField(Estudiante, through='Inscripciones', related_name='cursos') #n:m
    def __str__(self):
        return f"Curso: {self.id} - Profesor: {self.profesor.nombre}"


class Inscripciones(models.Model): #Tabla intermediaria
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE) #llave primaria de estudiante
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)#Llave primaria de cursos
    fecha_inscripcion = models.DateField(auto_now_add=True)
    estado = models.CharField(
        max_length=30,
        choices= [('activo', 'Activo'), ('finalizado', 'Finalizado')],
        default= 'activo'
    )
    nota_final= models.DecimalField(max_digits=3, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.estudiante.nombre} esta inscrito en el curso: {self.curso.nombre}"