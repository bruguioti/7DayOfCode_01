class Produto:
    def __init__(self, nome, codigo_barra, preco, quantidade_estoque):
        self.nome = nome
        self.codigo_barra = codigo_barra
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
        self.proximo = None
        self.anterior = None

class ControleEstoque:
    def __init__(self):
        self.primeiro_produto = None
        self.ultimo_produto = None

    def adicionar_produto(self, nome, codigo_barra, preco, quantidade_estoque):
        novo_produto = Produto(nome, codigo_barra, preco, quantidade_estoque)
        if self.primeiro_produto is None:
            self.primeiro_produto = novo_produto
            self.ultimo_produto = novo_produto
        else:
            novo_produto.anterior = self.ultimo_produto
            self.ultimo_produto.proximo = novo_produto
            self.ultimo_produto = novo_produto

    def remover_produto(self, codigo_barra):
        atual = self.primeiro_produto
        while atual is not None:
            if atual.codigo_barra == codigo_barra:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.primeiro_produto = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.ultimo_produto = atual.anterior
                del atual
                break
            atual = atual.proximo

    def atualizar_estoque(self, codigo_barra, nova_quantidade):
        atual = self.primeiro_produto
        while atual is not None:
            if atual.codigo_barra == codigo_barra:
                atual.quantidade_estoque = nova_quantidade
                break
            atual = atual.proximo

    def listar_produtos(self):
        atual = self.primeiro_produto
        while atual is not None:
            print("Nome:", atual.nome)
            print("Código de Barra:", atual.codigo_barra)
            print("Preço:", atual.preco)
            print("Quantidade em Estoque:", atual.quantidade_estoque)
            print("------------------------")
            atual = atual.proximo

# Exemplo de uso
estoque = ControleEstoque()

# Adicionar produtos
estoque.adicionar_produto("Produto 1", "123456", 10.0, 5)
estoque.adicionar_produto("Produto 2", "789012", 20.0, 3)
estoque.adicionar_produto("Produto 3", "345678", 15.0, 7)

# Listar produtos
estoque.listar_produtos()

# Atualizar estoque
estoque.atualizar_estoque("789012", 2)

# Remover produto
estoque.remover_produto("345678")

# Listar produtos atualizados
estoque.listar_produtos()
