from enum import Enum


class DataBaseName(str, Enum):
    """Database name enum
    
    Attributes:
        PSQL: PostgreSQL database name
        MONGODB: MongoDB database name
        MYSQL: MySQL database name
        REDIS: Redis database name
        MARIA_DB: MariaDB database name
    """

    PSQL = "psql"
    MONGODB = "mongodb"
    MYSQL = "mysql"
    REDIS = "redis"
    MARIA_DB = "maria_db"


class ColumnType(str, Enum):
    """Column type enum
    
    Attributes:
        STRING: String column type
        INTEGER: Integer column type
        FLOAT: Float column type
        BOOLEAN: Boolean column type
        DATE: Date column type
        DATETIME: DateTime column type
    """

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
