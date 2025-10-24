from academico.models import Profesor, Estudiante, Perfil, Curso, Inscripciones
#Crear al menos dos profesores y asignarles varios cursos.
#Creo tres profesores
profe1 = Profesor.objects.create(nombre="Carlos Suarez", email="carlos@skillnest.com")
profe2 = Profesor.objects.create(nombre="Marta Morales", email="marta@skillnest.com")
profe3 = Profesor.objects.create(nombre="Eduardo Yedro", email="eduardo@skillnest.com")
#Creo cinco cursos y los asigno a los profesores
curso1 = Curso.objects.create(nombre="Fundamentos de la Web", descripcion="HTML, CSS, JS", profesor=profe1)
curso2 = Curso.objects.create(nombre="Fullstack Python", descripcion="Python, POO, Django", profesor=profe2)
curso3 = Curso.objects.create(nombre="Fullstack Java", descripcion="Java, POO, SpringBoot", profesor=profe3)
curso4 = Curso.objects.create(nombre="Inteligencia Artificial", descripcion="Gemini, Copilot, Chatgpt", profesor=profe1)
curso5 = Curso.objects.create(nombre="Analisis de Datos", descripcion="MySQl, SQLlite, Workbench", profesor=profe2)
curso6 = Curso.objects.create(nombre="Frameworks de python", descripcion="Django, Flask", profesor=profe2)

# Crear estudiantes e inscribirlos en diferentes cursos.
#Creo 5 estudiantes
estudiante1 = Estudiante.objects.create(nombre="Macarena Monntesinos", email="macarena@skillnest.com")
estudiante2 = Estudiante.objects.create(nombre="Pamela Figueroa", email="pamela@skillnest.com")
estudiante3 = Estudiante.objects.create(nombre="Carolina Brown", email="carolina@skillnest.com")
estudiante4 = Estudiante.objects.create(nombre="Violeta Isnulza", email="violeta@skillnest.com")
estudiante5 = Estudiante.objects.create(nombre="Valentina Mooreno", email="valen@skillnest.com")

#nota_ cuando ya he creado los estudiantes y salgo del shell y vuelvo a entrar debo llamarlos primero de esta forma antes de realizar las inscripciones
curso1 = Curso.objects.get(id=1) #Fundamentos
curso2 = Curso.objects.get(id=2) #Python
curso3 = Curso.objects.get(id=3) #Java
curso4 = Curso.objects.get(id=4) #IA
curso5 = Curso.objects.get(id=5) #Analisis de Datos
curso6 = Curso.objects.get(id=6)# Frameworks

# Obtengo los estudiantes
estudiante1 = Estudiante.objects.get(id=1) #Macarena
estudiante2 = Estudiante.objects.get(id=2) #Pamela
estudiante3 = Estudiante.objects.get(id=3) #Carolina
estudiante4 = Estudiante.objects.get(id=4) #Violeta
estudiante5 = Estudiante.objects.get(id=5) #Valentina

# inscribo a Macarena en el curos de Fundamentos y Python
Inscripciones.objects.create(estudiante=estudiante1, curso=curso1, nota_final=6.1, estado='FIN')
Inscripciones.objects.create(estudiante=estudiante1, curso=curso2)

#inscribo a Pamela en los curoso de Java, IA y Fundamentos de la web
Inscripciones.objects.create(estudiante=estudiante2, curso=curso1, nota_final=6.5, estado='FIN')
Inscripciones.objects.create(estudiante=estudiante2, curso=curso3, nota_final=5.8, estado='FIN')
Inscripciones.objects.create(estudiante=estudiante2, curso=curso4)

# inscribo a Violeta en todos los cursos
Inscripciones.objects.create(estudiante=estudiante4, curso=curso1, nota_final=5.9, estado='FIN')
Inscripciones.objects.create(estudiante=estudiante4, curso=curso2)
Inscripciones.objects.create(estudiante=estudiante4, curso=curso3, nota_final=6.7, estado='FIN')
Inscripciones.objects.create(estudiante=estudiante4, curso=curso4)
Inscripciones.objects.create(estudiante=estudiante4, curso=curso5)

# Modificar estados de inscripciones y agregar notas finales.
inscripcion2 = Inscripciones.objects.get(id=2)
inscripcion2.estado = 'FIN'
inscripcion2.nota_final = 7.0
inscripcion2.save()

inscripcion7 = Inscripciones.objects.get(id=7)
inscripcion7.estado = 'FIN'
inscripcion7.nota_final = 6.5
inscripcion7.save()


# Crear perfiles para los estudiantes.
Perfil.objects.create(estudiante=estudiante1, biografia="Amante de lo aesthetic, le gusta el diseño de páginas web")
Perfil.objects.create(estudiante=estudiante2, biografia="Bailarina de ballet, le gusta pintar y pasear al aire libre")
Perfil.objects.create(estudiante=estudiante3, biografia="Mama de dos, ingeniera de profesion y mama de corazòn")
Perfil.objects.create(estudiante=estudiante4, biografia="Tecnico en mantenimiento con especializacion en refrigeracion")
Perfil.objects.create(estudiante=estudiante5, biografia="Pequeño jugador de ajedrez, amante de los videojuegos y de tocar el violin")

# Comprobar que el borrado en cascada funciona correctamente, borrare al estudiante 3 Macarena
estudiante1.delete()