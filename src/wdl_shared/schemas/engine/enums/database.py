from enum import StrEnum


class DataBaseName(StrEnum):
    """Supported database engines."""

    PSQL = "psql"
    MONGODB = "mongodb"
    MYSQL = "mysql"
    REDIS = "redis"
    MARIA_DB = "maria_db"


class ColumnType(StrEnum):
    """Supported database column types."""

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
