import peewee as pw

from samudra.conf.database import Database


class BaseTable(pw.Model):
    class Meta:
        database = Database.connection
        legacy_table_name = False
