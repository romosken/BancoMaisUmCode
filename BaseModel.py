import peewee


class BaseModel(peewee.Model):

    class Meta:
        database = peewee.SqliteDatabase('banco_maisumcode.db')

    # CRUD  - Create Read Update Delete
