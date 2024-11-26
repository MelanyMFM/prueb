from django.contrib import admin
from .models import User, Auditor, Control, Design, EncabezadoControl, Validacion, Observacion

admin.site.register(User)
admin.site.register(Auditor)
admin.site.register(Control)
admin.site.register(Design)
admin.site.register(EncabezadoControl)
admin.site.register(Validacion)
admin.site.register(Observacion)