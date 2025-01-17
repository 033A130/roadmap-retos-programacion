""" /*
 * EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con 
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
 */ """

#EJERCICIO

#Forma incorrecta

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        pass

    def send_email(self):
        pass

#Forma correcta

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserService:
    
    def save_to_database(self, user):
        pass

class EmailService:

    def send_email(self, email, message):
        pass

#DIFICULTAD EXTRA

class BookRegister:

    def __init__(self):
        self.books = []

    def new_book(self, title, author, book_copies: int):
        self.books.append({"Title": title, "Author": author, "Nº de copias": book_copies})


class UserManage:

    pass

class BookLoans:
    
    pass

book = BookRegister
book.new_book(self=None, title="Hola", author="Pepe", book_copies=12)
