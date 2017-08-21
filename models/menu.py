# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

#response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
#                  _class="brand-logo",_href="http://www.web2py.com/",
#                  _id="web2py-logo")

response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Edilson Alzemand <edilson.alzemand@gmail.com>'
response.meta.description = 'Rastema'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'level'), [])
]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

def _():
    # shortcuts
    app = request.application
    ctr = request.controller
    # useful links to internal and external resources
    response.menu += [

          (T('Fornecedor'), False, '#', [
             (T('Cadastro'), True,
             URL('default', 'cadastro_fornecedor')),
             (T('Consulta'), True,
             URL('default', 'suporte')),
             ]),
        #   (T('Equipamentos'), False, '#', [
        #      (T('Cadastro Unitário'), True,
        #      URL('default', 'cadastro_equipamento')),
        #      (T('Consulta'), True,
        #      URL('default', 'ver_equipamento')),
        #      ]),
        #   (T('Pedidos'), False, '#', [
        #      (T('Locação'), True,
        #      URL('default', 'cadastro_pedido')),
        #      (T('Consulta'), True,
        #      URL('default', 'ver_locacao')),
        #      ]),
        #    (T('Almoxarifado'), False, '#', [
        #       (T('Consulta'), True,
        #       URL('default', 'ver_locacao')),
        #       (T('Receber'), True,
        #       URL('default', 'almoxarife')),
        #       (T('Devolução'), True,
        #       URL('default', 'suporte')),
        #       (T('Valores'), True,
        #       URL('default', 'ver_locacao')),
        #       ]),
        #    (T('Embarque'), False, '#', [
        #       (T('Locação'), True,
        #       URL('default', 'cadastro_pedido')),
        #       (T('Consulta'), True,
        #       URL('default', 'ver_locacao')),
        #       (T('Receber'), True,
        #       URL('default', 'almoxarife')),
        #       (T('Devolução'), True,
        #       URL('default', 'suporte')),
        #       ]),

          (T('Relatórios'), False,  URL('default', 'suporte'))]
if DEVELOPMENT_MENU: _()

if "auth" in locals(): auth.wikimenu()
