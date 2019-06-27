import web
import psycopg2

db = web.database(dbn='postgres', dbname='todo', user='kennyfrc',pw='solozo13')

def get_todos():
    return db.select('todo', order='id')

def new_todo(text):
    db.insert('todo', title=text)

def del_todo(id):
    db.delete('todo', where="id=$id", vars=locals())

# def update_todo(id, text):
# 	db.update('todo', where="id=$id", vars=locals(), title=text)