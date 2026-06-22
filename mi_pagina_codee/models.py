from django.db import models

# 1. Usuarios / Perfiles del Colegio
class UsuarioPerfil(models.Model):
    ROLES = [
        ('ADMIN', 'Administrador'),
        ('DOCENTE', 'Docente'),
        ('ALUMNO', 'Alumno'),
    ]
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='ALUMNO')

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.rol})"

# 2. Materias
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# 3. Cursos (ej. 1°A, 4° Informática)
class Curso(models.Model):
    anio = models.IntegerField(verbose_name="Año")
    division = models.CharField(max_length=10, verbose_name="División")
    turno = models.CharField(max_length=20, choices=[('MAÑANA', 'Mañana'), ('TARDE', 'Tarde'), ('VESPERTINO', 'Vespertino')])

    def __str__(self):
        return f"{self.anio}° {self.division} - Turno {self.turno}"

# 4. Horarios de Clase (Une Curso, Materia y Docente)
class HorarioClase(models.Model):
    DIAS = [
        ('LUN', 'Lunes'),
        ('MAR', 'Martes'),
        ('MIE', 'Miércoles'),
        ('JUE', 'Jueves'),
        ('VIE', 'Viernes'),
    ]
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='horarios')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    docente = models.ForeignKey(UsuarioPerfil, on_delete=models.SET_NULL, null=True, limit_choices_to={'rol': 'DOCENTE'})
    dia = models.CharField(max_length=3, choices=DIAS)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.curso} | {self.materia} - {self.dia} ({self.hora_inicio} a {self.hora_fin})"