from dagster import resource, Field, String, Int
import sqlalchemy

class PostgresDBConnection:
    def __init__(self, host:str='localhost', port:int=5432, user:str='root', password:str='', database:str=''):
        self.__host =  host
        self.__port = port
        self.__user = user
        self.__pwd = password
        self.__db = database
    
    def connect(self) -> sqlalchemy.engine.Engine:
        return sqlalchemy.create_engine(f'postgresql://{self.__user}:{self.__pwd}@{self.__host}:{self.__port}/{self.__db}')

@resource(
    config_schema={
        'host': Field(String, description="Postgresql database server host"),
        'port': Field(Int, description="Postgresql database server port"),
        'username': Field(String, description="Postgresql database username"),
        'password': Field(String, description="Postgresql database user password"),
        'database': Field(String, description="Postgresql database name"),
    }
)
def dwh_connection(init_context):
    return PostgresDBConnection(
        host=init_context.resource_config['host'],
        port=init_context.resource_config['port'],
        user=init_context.resource_config['username'],
        password=init_context.resource_config['password'],
        database=init_context.resource_config['database']
    )