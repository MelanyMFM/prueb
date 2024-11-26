from django.db import models

# User
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.username


# Auditor
class Auditor(models.Model):
    class CargoChoices(models.TextChoices):
        AUDITOR = 'Auditor', 'Auditor'

    id_auditor = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.CharField(
        max_length=100,
        choices=CargoChoices.choices,
        default=CargoChoices.AUDITOR,
    )

    def __str__(self):
        return f"{self.user.name} ({self.cargo})"


# Control
class Control(models.Model):
    class EstadoChoices(models.TextChoices):
        PENDIENTE = 'Pendiente', 'Pendiente'
        EN_PROCESO = 'En Proceso', 'En Proceso'
        TERMINADO = 'Terminado', 'Terminado'

    year = models.IntegerField()
    testing = models.IntegerField(choices=[(1, 'Semestre 1'), (2, 'Semestre 2')])
    nombre_control = models.CharField(max_length=100)
    codigo_control = models.CharField(max_length=50, unique=True)
    estado = models.CharField(
        max_length=50,
        choices=EstadoChoices.choices,
        default=EstadoChoices.PENDIENTE,
    )

    def get_estado_css_class(self):
        """Convierte el estado en una clase CSS adecuada."""
        return {
            self.EstadoChoices.PENDIENTE: "pendiente",
            self.EstadoChoices.EN_PROCESO: "en-proceso",
            self.EstadoChoices.TERMINADO: "terminado",
        }.get(self.estado, "default")

    ciclo = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    auditor = models.ForeignKey(Auditor, on_delete=models.CASCADE, related_name="controles")

    def __str__(self):
        return f"{self.nombre_control} ({self.year}, Testing {self.testing})"


# Design
class Design(models.Model):
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name="designs")
    nombre = models.CharField(max_length=100)
    last_date = models.DateField()
    nombre_prueba = models.CharField(max_length=100)
    comentarios = models.TextField(blank=True)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


# EncabezadoControl
class EncabezadoControl(models.Model):
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name="encabezados")
    explicacion = models.TextField()
    estado = models.CharField(max_length=50)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    recursos = models.TextField(blank=True)

    def __str__(self):
        return f"Encabezado de {self.control.nombre_control}"


# Validacion
class Validacion(models.Model):
    control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name="validaciones")
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"Validación de {self.control.nombre_control} ({self.estado})"


# Observacion
class Observacion(models.Model):
    validacion = models.ForeignKey(Validacion, on_delete=models.CASCADE, related_name="observaciones")
    explicacion = models.TextField()

    def __str__(self):
        return f"Observación: {self.explicacion[:50]}..."
