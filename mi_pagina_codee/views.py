from django.shortcuts import render

# Vista para la página principal (index.html)
def inicio(request):
    return render(request, 'index.html')

# Vista para la página de Docentes
def ver_docentes(request):
    return render(request, 'docentees.html')

# Vista para la página de Materias
def ver_materias(request):
    return render(request, 'materias.html')

# Vista para la página de Administración
def ver_administrador(request):
    return render(request, 'adminnistrador.html')