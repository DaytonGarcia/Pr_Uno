### we prepend t_ to tablenames and f_ to fieldnames for disambiguity
db.define_table('cursos',
                Field('id', 'id'),
                Field('codigo', type='integer', label=T('CODIGO DEL CURSO')),
                Field('nombre', type='string', label=T('NOMBRE')),
                Field('creditos', type='integer', label=T('CREDITOS DEL CURSO')),
                format='%(nombre)s',
                migrate=False)

