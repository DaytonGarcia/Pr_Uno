# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

@auth.requires_login()
def especializacion():
   form = SQLFORM(db.Especializacion)
   grid = SQLFORM.smartgrid(db.Especializacion,onupdate=auth.archive,formname='web2py_grid')
   if form.process(formname='registro').accepted:
       response.flash = 'Se ha registrado una nueva especializacion'
   elif form.errors:
       response.flash = 'El formulario tiene errores'
   return dict(form=form, grid=grid)

#agregando la definicion del modulo catedratico
@auth.requires_login()
def catedratico():
   form = SQLFORM(db.Catedratico)
   grid = SQLFORM.smartgrid(db.Catedratico,formname='web2py_grid')
   if form.process(formname='registro').accepted:
       response.flash = 'Se ha registrado una nueva especializacion'
   elif form.errors:
       response.flash = 'El formulario tiene errores'
   return dict(form=form, grid=grid)

def error():
    return dict()
