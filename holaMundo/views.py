from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
 return HttpResponse(
 """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <header>
        <h1>Bienvenido a nuestro sitio</h1>
    </header>
    <nav>
        <ul>
            <li><a href="about/">Acerca de</a></li>
            <li><a href="contact/">Contacto</a></li>
        </ul>
    </nav>
    <main>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae commodo ligula. Integer nec eros in nulla sollicitudin venenatis.</p>
    </main>
    <footer>
        <p>&copy; 2024 Nuestro Sitio Web</p>
    </footer>
</body>
</html>
 """
 )
 
 
def about(request):
 return HttpResponse(
 """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <header>
        <h1>Sobre Nosotros</h1>
    </header>
    <main>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae commodo ligula. Integer nec eros in nulla sollicitudin venenatis.</p>
        <p>Proin ac convallis purus. Etiam interdum ligula ut tellus pulvinar, at eleifend velit pharetra.</p>
    </main>
    <footer>
        <p>&copy; 2024 Nuestro Sitio Web</p>
    </footer>
</body>
</html>
 """
 )
 
def contact(request):
 return HttpResponse(
 """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact</title>
</head>
<body>
    <header>
        <h1>Contacto</h1>
    </header>
    <main>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae commodo ligula. Integer nec eros in nulla sollicitudin venenatis.</p>
        <form action="/enviar" method="post">
            <label for="nombre">Nombre:</label><br>
            <input type="text" id="nombre" name="nombre" required><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email" required><br>
            <label for="mensaje">Mensaje:</label><br>
            <textarea id="mensaje" name="mensaje" rows="4" required></textarea><br>
            <button type="submit">Enviar mensaje</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2024 Nuestro Sitio Web</p>
    </footer>
</body>
</html>
 """
 )