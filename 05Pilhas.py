class Livro:
    def __init__(self, nome, num_paginas):
        self.nome = nome
        self.num_paginas = num_paginas

class PilhaLivros:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self):
        if not self.vazia():
            return self.livros.pop()
        else:
            return None

    def livro_topo(self):
        if not self.vazia():
            return self.livros[-1]
        else:
            return None

    def listar_livros(self):
        return self.livros

    def vazia(self):
        return len(self.livros) == 0

# Exemplo de uso
pilha = PilhaLivros()

# Adicionar livros na pilha
pilha.adicionar_livro(Livro("A Guerra dos Tronos", 694))
pilha.adicionar_livro(Livro("A Fúria dos Reis", 768))
pilha.adicionar_livro(Livro("A Tormenta de Espadas", 1177))

# Remover um livro da pilha
livro_removido = pilha.remover_livro()
if livro_removido:
    print("Livro removido:", livro_removido.nome)

# Mostrar o livro no topo da pilha
livro_topo = pilha.livro_topo()
if livro_topo:
    print("Livro no topo:", livro_topo.nome)

# Listar todos os livros da pilha
livros_na_pilha = pilha.listar_livros()
print("Livros na pilha:")
for livro in livros_na_pilha:
    print(livro.nome, "-", livro.num_paginas)
