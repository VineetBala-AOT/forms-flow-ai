"""This module initializes the supported databases and the client to interact with them."""
from .database_factory import DatabaseFactory
from .postgres import PostgresConnect
from .dbms_enum import Databse
from .db_client import DatabaseClient

factory = DatabaseFactory()
factory.register_database(Databse["POSTGRES"].value, PostgresConnect)

client = DatabaseClient(factory)
