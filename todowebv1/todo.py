import web
import model
import pdb

# routes: if path, then some code based on the METHOD

urls = (
    '/', 'Index',
    '/del/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit'
)


# sets up where the folder is ('templates')
# set a base templates where the pages will be rendered in
render = web.template.render('templates', base='base')


class Index:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            description="Enter a todo:"),
        web.form.Button('Add todo'),
    ) # form has the render method which prints html

    def GET(self):
        """ Show page """
        todos = model.get_todos() # returns an iterbetter object where u can iterate on it
        form = self.form() # returns a form object which prints html
        return render.index(todos, form) # print the index which contains todos and form

    def POST(self):
        """ Add new entry """
        form = self.form()
        if not form.validates(): # it is not validated
            todos = model.get_todos() # get the existing form
            return render.index(todos, form) # return the index page 
        model.new_todo(form.d.title) # if validated, add todo
        raise web.seeother('/') # 303 redirect back (so it refreshes)


class Edit:

    form = web.form.Form(
        web.form.Textbox('title', web.form.notnull, 
            description="Edit Todo:"),
        web.form.Button('Update'),
    )

    def GET(self, id):
        todo = model.get_todo(int(id))
        form = self.form()
        form.fill(todo)
        return render.edit(todo, form)


    def POST(self, id):
        form = self.form()
        todo = model.get_todo(int(id))
        if not form.validates():
            return render.edit(todo, form)
        model.update_todo(int(id), form.d.title)
        raise web.seeother('/')


class Delete:
    
    def POST(self, id):
        """ Delete based on ID """
        id = int(id)
        model.del_todo(id)
        raise web.seeother('/')

if __name__ == '__main__':
    app = web.application(urls, globals()) # set up application to delegate requests based on path and globals
    app.run()