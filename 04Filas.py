class Pedido:
    def __init__(self, prato, mesa):
        self.prato = prato
        self.mesa = mesa

class FilaPedidos:
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, prato, mesa):
        pedido = Pedido(prato, mesa)
        self.pedidos.append(pedido)

    def remover_pedido_entregue(self):
        if self.pedidos:
            pedido_entregue = self.pedidos.pop(0)
            return pedido_entregue
        else:
            return None

    def listar_pedidos(self):
        if self.pedidos:
            for pedido in self.pedidos:
                print(f"Prato: {pedido.prato} | Mesa: {pedido.mesa}")
        else:
            print("Não há pedidos na fila.")


# Exemplo de uso
fila = FilaPedidos()

# Adicionar novos pedidos na fila
fila.adicionar_pedido("Pizza", 1)
fila.adicionar_pedido("Hambúrguer", 2)
fila.adicionar_pedido("Salada", 3)

# Listar todos os pedidos na ordem em que foram feitos
print("Pedidos na fila:")
fila.listar_pedidos()

# Remover pedido entregue
pedido_entregue = fila.remover_pedido_entregue()
if pedido_entregue:
    print(f"Pedido entregue: Prato - {pedido_entregue.prato} | Mesa - {pedido_entregue.mesa}")
else:
    print("Não há pedidos para remover.")

# Listar pedidos restantes
print("Pedidos restantes:")
fila.listar_pedidos()
