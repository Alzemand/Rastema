# -*- coding: utf-8 -*-
# Author: Alzemand



# Validador Fornecedor

Fornecedor.razao_social.requires = [IS_NOT_EMPTY(error_message='Informe a Razão Social'), IS_UPPER()]
Fornecedor.nome.requires = IS_NOT_EMPTY(error_message='Informe o nome do Fornecedor')
Fornecedor.cnpj.requires = [IS_CNPJ(), IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'fornecedor.cnpj')]
Fornecedor.telefone.requires = IS_TELEFONE()
Fornecedor.email.requires = IS_EMAIL()


# Validador Equipamento

Equipamento.tag.requires = [IS_TAG(), IS_NOT_IN_DB(db, 'equipamento.tag')]
Equipamento.descricao.requires = [IS_NOT_EMPTY(error_message='Informe o nome do equipamento'), IS_UPPER()]
