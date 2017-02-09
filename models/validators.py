# -*- coding: utf-8 -*-
# Author: Alzemand

# Validadores de Fornecedor

Fornecedor.razao_social.requires = IS_NOT_EMPTY(error_message='Informe a Razão Social')
Fornecedor.nome.requires = IS_NOT_EMPTY(error_message='Informe o nome do Fornecedor')
Fornecedor.cnpj.requires = [IS_CNPJ(), IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'fornecedor.cnpj')]
Fornecedor.telefone.requires = IS_TELEFONE()

# Validador de Pedido

Fornecedor_Equipamento.valor.requires = E_DINHEIRO()
