from peewee import *

dbname = 'catalog_to'
user = 'postgres'
password = '1'
host = 'localhost'


dbhandle = PostgresqlDatabase(
    dbname, user=user,
    password=password,
    host='localhost'
)


class BaseModel(Model):
    class Meta:
        database = dbhandle


class Marks(BaseModel):
    id = AutoField()  # PrimaryKeyField(sequence="marks_id_seq")
    name = CharField(max_length=200)
    img = BigBitField()

    class Meta:
        db_table = "marks"
        order_by = ("name",)


class Modifications(BaseModel):
    id = AutoField()  # PrimaryKeyField(sequence="modifications_id_seq")
    name = CharField(max_length=400)
    img = BigBitField()
    marka = ForeignKeyField(
        Marks, related_name="fk_marks_modifications", to_field="id", on_delete="cascade")

    class Meta:
        db_table = "modifications"
        order_by = ("name",)


class Models(BaseModel):
    id = AutoField()  # PrimaryKeyField(sequence="models_id_seq")
    name = CharField(max_length=400)
    power = CharField(max_length=100)
    fuel = CharField(max_length=200)
    year = CharField(max_length=100)
    modification = ForeignKeyField(
        Modifications, related_name="fk_modifications_models", to_field="id", on_delete="cascade")

    class Meta:
        db_table = "models"
        order_by = ("modification",)


class Details(BaseModel):
    id = AutoField()  # PrimaryKeyField(sequence="details_id_seq")
    name = CharField(max_length=500)
    code = CharField(max_length=200)
    comment = CharField(max_length=500)
    model = ForeignKeyField(
        Models, related_name="fk_models_details", to_field="id", on_delete="cascade")

    class Meta:
        db_table = "details"
        order_by = ("name",)
