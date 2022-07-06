from collections import Counter
from datetime import datetime, timezone, timedelta

timezone_offset = -3.0
tzinfo = timezone(timedelta(hours=timezone_offset))
data = datetime.now(tzinfo)

class User():

    def __init__(self, id, nome, login, senha):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome

    def alterar_login(self, novo_login):
        self.login = novo_login
        return self.login

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha
        return self.senha

class Post():

    def __init__(self, postType, id, titulo, texto, tema, data = data):
        self.postType = postType
        self.id = id
        self.titulo = titulo
        self.tema = tema
        self.texto = texto
        self.data = data

class Ads():
    
    def __init__(self, postType, id, url, titulo, texto, tema, data = data):
        self.postType = postType
        self.id = id
        self.url = url
        self.titulo = titulo
        self.texto = texto
        self.tema = tema
        self.data = data
