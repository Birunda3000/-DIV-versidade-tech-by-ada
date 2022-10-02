import menu
import storage

db = storage.Storage()
me = menu.Menu()
me.run(db)