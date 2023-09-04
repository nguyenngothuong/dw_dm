import pyodbc
from sqlalchemy import create_engine
import yaml


    # Đọc thông tin từ file YAML
file_path_config = r"G:\My Drive\HỌC TẬP DUE\NNT_năm 4 kì 1\DW & DM\config\config.yaml"
with open(file_path_config, 'r') as yaml_file:
    config = yaml.safe_load(yaml_file)

server = config['database']['server']
database = config['database']['database']
username = config['database']['username']
password = config['database']['password']



def connect_db():
    # Tạo chuỗi kết nối cho pyodbc
    conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};Database={database};UID={username};PWD={password}'

    # Tạo URL kết nối cho SQLAlchemy
    db_url = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"

    engine = create_engine(db_url)


    return conn_str, engine