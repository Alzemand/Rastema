# -*- coding: utf-8 -*-
# Author: Alzemand



# Validador Fornecedor

Fornecedor.razao_social.requires = [IS_NOT_EMPTY(error_message='Informe a Razão Social'), IS_UPPER()]
Fornecedor.nome.requires = IS_NOT_EMPTY(error_message='Informe o nome do Fornecedor')
Fornecedor.cnpj.requires = [IS_CNPJ(), IS_NOT_EMPTY(), IS_NOT_IN_DB(db, 'fornecedor.cnpj',
                                                    error_message="CNPJ já cadastrado")]
Fornecedor.telefone.requires = IS_TELEFONE()
Fornecedor.email.requires = IS_EMAIL()


# Validador Equipamento

# Equipamento.fornecedor.requires = [IS_IN_DB(db, db.fornecedor.cnpj, '%s' % (db.fornecedor.cnpj))]
Equipamento.tag.requires = [IS_TAG(), IS_NOT_IN_DB(db, 'equipamento.tag')]
Equipamento.descricao.requires = [IS_NOT_EMPTY(error_message='Informe o nome do equipamento'), IS_UPPER()]

# Validador Equipamento

# dbset = db(db.tabela.ativo=='sim')
#
# db.objeto.tipo.requires = IS_IN_DB(dbset, Tipo.id, '%(descricao)s')

# fornecedor_selecionado está
dbset = db(db.equipamento.fornecedor == 1)

Pedido.equipamento.requires = IS_IN_DB(dbset, 'equipamento.id', "%(descricao)s")
Pedido.data_prevista_fim.requires = IS_DATE(format=T('%d/%m/%Y') ,error_message='Data no formato dd/mm/aaaa')
Pedido.valor.requires = E_DINHEIRO()
Pedido.plataforma.requires = IS_IN_SET(["101.01.001 – GERENTE DE CONTRATO",
                                                "101.01.003 – OPERAÇÕES",
                                                "101.01.004 – RH/DP",
                                                "101.01.006 – FINANCEIRO",
                                                "101.01.008 – PIPE SHOP",
                                                "101.01.009 – T.I",
                                                "101.01.010 – ADMINISTRAÇÃO CONTRATUAL",
                                                "101.01.011 – SUPRIMENTOS",
                                                "101.01.014 – QUALIDADE",
                                                "101.01.015 – SEGURANÇA E MEIO AMBIENTE",
                                                "101.01.016 – MEDICINA",
                                                "101.01.017 – ENGENHARIA",
                                                "101.01.018 – PLANEJAMENTO",
                                                "101.01.021 – CONTABILIDADE/FISCAL",
                                                "101.01.023 – INVESTIMENTO",
                                                "101.01.025 – CARAPEBUS - OFFSHORE",
                                                "101.01.029 – OPERAÇÃO ATPN",
                                                "101.01.030 – PPM1 OFFSHORE",
                                                "101.01.031 – PNA1 OFFSHORE",
                                                "101.01.032 – PNA2 OFFSHORE - ATPN",
                                                "101.01.033 – PCH2 OFFSHORE - ATPN",
                                                "101.01.034 – P9 OFFSHORE - ATPN",
                                                "101.01.035 – P12 OFFSHORE - ",
                                                "101.01.036 – CAMPANHAS - ATIVO NORTE - PARADAS",
                                                "101.01.037 – LOGISTICA DE MATERIAIS ",
                                                "101.01.038 – MANUTENÇÃO",
                                                "101.01.039 – UMS OFFSHORE ARARUAMA 02",
                                                "101.01.040 – UMS OFFSHORE CABO FRIO",
                                                "101.01.041 – ALMOXARIFADO DE FABRICAÇÃO E TERCEIROS",
                                                "101.01.042 – PCH1 - ATPN"
                                                ])
