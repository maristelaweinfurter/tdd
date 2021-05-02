class Restaurante:
    def __init__(self, nome, pedidos_na_fila=0):
        self.nome = nome
        if pedidos_na_fila >= 0:
            self.pedidos_na_fila = pedidos_na_fila
        else:
            raise ValueError(
                "A quantidade de pedidos na fila deve ser maior ou igual a zero"
            )

    def adiciona_pedido(self):
        self.pedidos_na_fila += 1

    def remove_pedido(self):
        if self.pedidos_na_fila > 0:
            self.pedidos_na_fila -= 1



# class Restaurante:
#     pass
#  primeiro código para fazer com que todos os testes criados falhem

#no segundo momento deixo de criar o pedidos_na_fila para falhar
# class Restaurante:
#     def __init__(self, nome):
#         self.nome = nome

#no segundo teste que falhou, ele não encontra o parâmetro pedidos_na_fila
# class Restaurante:
#     def __init__(self, nome):
#         self.nome = nome
#         self.pedidos_na_fila = 0

#no terceiro teste que falhou, ele não pode deixar pedidos na fila menores que zero
# class Restaurante:
#     def __init__(self, nome):
#         self.nome = nome
#         self.pedidos_na_fila = pedidos_na_fila

#no quarto teste falhou pq não tinha o método adiciona pedido
# class Restaurante:
#     def __init__(self, nome, pedidos_na_fila=0):
#         self.nome = nome
#         if pedidos_na_fila >= 0:
#             self.pedidos_na_fila = pedidos_na_fila
#         else:
#             raise ValueError(
#                 "A quantidade de pedidos na fila deve ser maior ou igual a zero"
#             )

# no quinto teste falhou pq não tinha o método remove pedido
# no sexto teste falhou pq eu não testava se o número de pedidos era maior que zero
