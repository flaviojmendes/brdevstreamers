import os
from peewee import PostgresqlDatabase, CharField, IntegerField, Model

db = PostgresqlDatabase(
    config["DB_NAME"],
    user=config["DB_USER"],
    password=config["DB_PASS"],
    host=config["DB_HOST"],
    port=config["DB_PORT"],
)


class Reward(Model):
    id = CharField(null=False)
    description = CharField(null=False)
    price = IntegerField(null=False)
    quantity_available = IntegerField(null=False)

    class Meta:
        database = db
