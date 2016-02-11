### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def error():
    return dict()
def cursos():
   form = SQLFORM(db.cursos)
   grid = SQLFORM.smartgrid(db.cursos,onupdate=auth.archive,formname='web2py_grid')
   if form.process(formname='cursos').accepted:
       response.flash = 'Se ha registrado un nuevo curso'
   elif form.errors:
       response.flash = 'El formulario tiene errores'
   return dict(form=form, grid=grid)


