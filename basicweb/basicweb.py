import web
import psycopg2

# look for templates in the templates directory
render = web.template.render("templates/")
db = web.database(dbn="postgres",pw="solozo13",user="kennyfrc", dbname="initialdb")

# url handling
urls = (
	'/', 'index',
	'/add', 'add'
)

# render index using web params
# class index:
# 	def GET(self):
# 		i = web.input(name=None)
# 		return render.index(i.name)


# render index
# class index:
# 	def GET(self):
# 		name = "Kenn"
# 		return render.index(name)

class index:
	def GET(self):
		todos = db.select('todo')
		return render.index(todos)

class add:
    def POST(self):
        i = web.input()
        n = db.insert('todo', title=i.title)
        raise web.seeother('/')


# basic index definition
# class index:
# 	def GET(self):
# 		return "Hello, World!"

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()