### we prepend t_ to tablenames and f_ to fieldnames for disambiguity
db.define_table('Especializacion',
                Field('id', 'id'),
                Field('Detalle', type='string', label=T('NOMBRE')),
                format='%(Detalle)s',
                migrate=False)

## agregando string tabla catedratico
db.define_table('Catedratico',
                Field('Nombre', type='string', label=T('Nombre'),notnull=True),
                Field('Dpi', type='string', label=T('DPI'),notnull=True,unique=True),
                Field('Telefono', type='integer', label=T('TELEFONO'),notnull=True),
                Field('Especializacion', 'reference Especializacion', label=T('ESPECIALIZACION'),notnull=False),
                migrate=False)
