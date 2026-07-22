from enum import StrEnum


class DataBaseName(StrEnum):
    """Supported database engines."""

    PSQL = "psql"
    MONGODB = "mongodb"
    MYSQL = "mysql"
    REDIS = "redis"
    MARIA_DB = "maria_db"
    SQLITE = "sqlite"
    SQL_SERVER = "sql_server"
    ORACLE = "oracle"
    COCKROACHDB = "cockroachdb"


class ColumnType(StrEnum):
    """Supported database column types."""

    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    TIME = "time"
    TIMESTAMP = "timestamp"
    UUID = "uuid"
    TEXT = "text"
    CHAR = "char"
    VARCHAR = "varchar"
    SMALLINT = "smallint"
    BIGINT = "bigint"
    DECIMAL = "decimal"
    NUMERIC = "numeric"
    DOUBLE = "double"
    JSON = "json"
    JSONB = "jsonb"
    BINARY = "binary"
    BLOB = "blob"
    ENUM = "enum"
    ARRAY = "array"
    GEOMETRY = "geometry"
    CUSTOM = "custom"


class IndexType(StrEnum):
    """Kinds of indexes represented by a diagram."""

    INDEX = "index"
    UNIQUE = "unique"
    PRIMARY = "primary"
    FULLTEXT = "fulltext"


class SortOrder(StrEnum):
    """Column ordering inside an index."""

    ASC = "asc"
    DESC = "desc"


class ReferentialAction(StrEnum):
    """Actions supported by SQL foreign keys."""

    NO_ACTION = "no_action"
    RESTRICT = "restrict"
    CASCADE = "cascade"
    SET_NULL = "set_null"
    SET_DEFAULT = "set_default"


class RelationshipCardinality(StrEnum):
    """Cardinality displayed at one end of a relationship."""

    ZERO_OR_ONE = "zero_or_one"
    EXACTLY_ONE = "exactly_one"
    ZERO_OR_MANY = "zero_or_many"
    ONE_OR_MANY = "one_or_many"
