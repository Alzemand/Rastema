# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

# Conexão MYSQL
db = DAL('mysql://root:linux@127.0.0.1/rastema', bigint_id=True)

# Tabela Fornecedor

Fornecedor = db.define_table('fornecedor',
    Field('cnpj', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate'), label='CNPJ'),
    Field('razao_social', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate')),
    Field('nome', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate')),
    Field('endereco', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate')),
    Field('inscricao_estadual', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate'), label="Inscrição Estatual"),
    Field('email', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate', _type='email'), label="E-Mail"),
    Field('telefone', 'string', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate')),
    Field('servico', 'text'),
    primarykey=['cnpj'],
    format = "%(nome)s"
    )

# Tabela de Equipamento

Equipamento = db.define_table('equipamento',
    Field('descricao', 'string' , widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate'), label = 'Descrição'),
    Field('ax_cod', 'bigint' , widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate'), label='Código AX'),
    Field('tag', 'string' , widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate')),
    format = "%(descricao)s  | TAG: %(tag)s",
    # primarykey=['tag']
    )

# Tabela de vinculo de fornecedor e equipamento (Pedido)

Pedido = db.define_table('pedido',
    Field('fornecedor', 'reference fornecedor',  widget = lambda field, value:
    SQLFORM.widgets.options.widget(field, value, _class='input-field'), ondelete='SET NULL'),
    Field('equipamento', 'reference equipamento',  widget = lambda field, value:
    SQLFORM.widgets.options.widget(field, value, _class='input-field'), ondelete='SET NULL'),
    Field('valor', 'decimal(7,2)', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='validate')),
    Field('data_pedido', 'date', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='datepicker')),
    Field('data_prevista_fim', 'date', widget = lambda field, value:
    SQLFORM.widgets.string.widget(field, value, _class='datepicker')),
    # format = "%(equipamento_nome)s - %(fornecedor_nome)s"
    )
#
# # Tabela de recebimento de almoxarifado
#
# Almoxarife = db.define_table('almoxarife',
#     Field('tag', 'string', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('fornecedor_equipamento', 'reference fornecedor_equipamento',  widget = lambda field, value:
#     SQLFORM.widgets.options.widget(field, value, _class='browser-default'), ondelete='SET NULL'),
#     Field('fornecedor', 'bigint', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('equipamento', 'bigint', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('fornecedor_nome', 'string', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('equipamento_nome', 'string', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('plataforma', 'string', widget = lambda field, value:
#     SQLFORM.widgets.options.widget(field, value, _class='browser-default')),
#     Field('nf_entrada', 'integer', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('nf_embarque', 'integer', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('nf_saida', 'integer', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('valor', 'decimal(7,2)', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('data_recebida', 'date', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('data_devolucao', 'date', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('data_retirada', 'date', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('data_pedido', 'date', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='date')),
#     Field('data_prevista_fim', 'date', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='date')),
#     Field('status', 'string', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     format = "%(tag)s - %(equipamento_nome)s"
#     )
#
# # Atualização de valores
#
# Valor = db.define_table('valor',
#     Field('almoxarife', 'reference almoxarife',  widget = lambda field, value:
#     SQLFORM.widgets.options.widget(field, value, _class='browser-default'), ondelete='SET NULL'),
#     Field('valor', 'decimal(7,2)', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='validate')),
#     Field('data_atualizacao', 'date', widget = lambda field, value:
#     SQLFORM.widgets.string.widget(field, value, _class='date')),
#     )
