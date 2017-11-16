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

Pedido.plataforma.requires = IS_IN_SET(["101.01.001 – IO – GERENTE DE CONTRATO",
                                                "101.01.003 – IO – OPERAÇÕES",
                                                "101.01.004 – IO – RH/DP",
                                                "101.01.006 – IO – FINANCEIRO",
                                                "101.01.008 – IO – PIPE SHOP",
                                                "101.01.009 – IO – T.I",
                                                "101.01.010 – IO – ADMINISTRAÇÃO CONTRATUAL",
                                                "101.01.011 – IO – SUPRIMENTOS",
                                                "101.01.014 – IO – QUALIDADE",
                                                "101.01.015 – IO – SEGURANÇA E MEIO AMBIENTE",
                                                "101.01.016 – IO – MEDICINA",
                                                "101.01.017 – IO – ENGENHARIA",
                                                "101.01.018 – IO – PLANEJAMENTO",
                                                "101.01.021 – IO – CONTABILIDADE/FISCAL",
                                                "101.01.023 – IO – INVESTIMENTO",
                                                "101.01.025 – IO – CARAPEBUS - OFFSHORE",
                                                "101.01.029 – IO – OPERAÇÃO ATPN",
                                                "101.01.030 – IO – PPM1 OFFSHORE",
                                                "101.01.031 – IO – PNA1 OFFSHORE",
                                                "101.01.032 – IO – PNA2 OFFSHORE - ATPN",
                                                "101.01.033 – IO – PCH2 OFFSHORE - ATPN",
                                                "101.01.034 – IO – P9 OFFSHORE - ATPN",
                                                "101.01.035 – IO – P12 OFFSHORE - ",
                                                "101.01.036 – IO – CAMPANHAS - ATIVO NORTE - PARADAS",
                                                "101.01.037 – IO – LOGISTICA DE MATERIAIS ",
                                                "101.01.038 – IO – MANUTENÇÃO",
                                                "101.01.039 – IO – UMS OFFSHORE ARARUAMA 02",
                                                "101.01.040 – IO – UMS OFFSHORE CABO FRIO",
                                                "101.01.041 – IO – ALMOXARIFADO DE FABRICAÇÃO E TERCEIROS",
                                                "101.01.042 – IO – PCH1 - ATPN"
                                                ])
