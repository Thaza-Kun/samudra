from peewee import BlobField, TextField, ForeignKeyField

from .base import BaseTable
from .konsep import Konsep


class Cakupan(BaseTable):
    """
    Dalam konteks apakah istilah tersebut digunakan untuk konsep yang diberikan.
    """
    nama = TextField(null=False, unique=True)
    keterangan = BlobField(null=True)


class PadananCakupanKeKonsep(BaseTable):
    cakupan = ForeignKeyField(model=Cakupan, field=Cakupan.id, backref='konsep', on_delete='cascade')
    konsep = ForeignKeyField(model=Konsep, field=Konsep.id, backref='cakupan', on_delete='cascade')
