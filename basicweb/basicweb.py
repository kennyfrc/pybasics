# look for templates in the templates directory
render = web.template.render("templates/")

import web

# url handling
urls = (
	'/', 'index'
)

# render index using web params
class index:
	def GET(self):
		i = web.input(name=None)
		return render.index(i.name)


# render index
# class index:
# 	def GET(self):
# 		name = "Kenn"
# 		return render.index(name)


# basic index definition
# class index:
# 	def GET(self):
# 		return "Hello, World!"

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()