from telegram import user
import sys
sys.path.append("./dbfolder")
from mysqlfunc import mysqldb
db = mysqldb()


class linkdb:
    def set(key, value):
        db.add_shortner(key,value)

    def get(key):
        return db.get_shortner(key)
