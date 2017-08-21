# -*- coding: utf-8 -*-
# Author: Alzemand

# Validadores de Fornecedor

Fornecedor.razao_social.requires = IS_NOT_EMPTY(error_message='Informe a Razão Social')
Fornecedor.nome.requires = IS_NOT_EMPTY(error_message='Informe o nome do Fornecedor')
Fornecedor.cnpj.requires = [IS_CNPJ(), IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'fornecedor.cnpj')]
Fornecedor.telefone.requires = IS_TELEFONE()

# # Validador de Pedido
#
# Fornecedor_Equipamento.valor.requires = E_DINHEIRO()
#
# # Validador de Almoxarife
#
# #Almoxarife.fornecedor.requires = IS_EMPTY_OR(IS_NOT_EMPTY(db, 'almoxarife.fornecedor'))
# Almoxarife.plataforma.requires = IS_IN_SET(['BASE', 'P-18', 'Outro'])
# Almoxarife.data_recebida.requires = IS_DATE(format=T('%d/%m/%Y') ,error_message='Data no formato dd/mm/aaaa')
