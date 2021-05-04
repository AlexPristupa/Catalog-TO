import peewee
from models import *

if __name__ == '__main__':
    try:
        dbhandle.connect()
        Marks.create_table()
    except peewee.InternalError as px:
        print(str(px))
    try:
        Modifications.create_table()
    except peewee.InternalError as px:
        print(str(px))

    try:
        Models.create_table()
    except peewee.InternalError as px:
        print(str(px))

    try:
        Details.create_table()
    except peewee.InternalError as px:
        print(str(px))
