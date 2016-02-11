response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Especializacion'),URL('default','especializacion')==URL(),URL('default','especializacion'),[]),
(T('Catedratico'),URL('default','catedratico')==URL(),URL('default','catedratico'),[]),
]
