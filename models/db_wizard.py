### we prepend t_ to tablenames and f_ to fieldnames for disambiguity
db.define_table('Especializacion',
                Field('id', 'id'),
                Field('Detalle', type='string', label=T('NOMBRE')),
                format='%(Detalle)s',
                migrate=False)
