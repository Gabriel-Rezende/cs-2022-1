
class Contato:

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Agenda:

    def __init__(self, contatos):
        self.contatos = contatos

    def adicionar_contato(self, contato):
        self.contatos.append(contato)
    
    def buscar_contato(self, nome=None, email=None):
        for c in self.contatos:
            if c.nome == nome and nome:
                return c
            if c.email == email and email:
                return c
    
    def remover_contato(self, nome):
        for c in self.contatos:
            if c.nome == nome:
                self.contatos.remove(c)
    
    def listar_contatos(self):
        return self.contatos