import pyodbc
import pandas as pd
import sys
sys.path.append(r"G:/My Drive/HỌC TẬP DUE/NNT_năm 4 kì 1/DW & DM/config")
import mdl_db_connection

conn_str, engine = mdl_db_connection.connect_db()

def get_foreign_key_relationships():
    conx = pyodbc.connect(conn_str)
    cursor = conx.cursor()

    # Truy vấn để lấy thông tin về ràng buộc khóa ngoại
    query = """
            SELECT 
                OBJECT_NAME(parent_object_id) AS parent_table,
                col.name AS parent_column,
                OBJECT_NAME(referenced_object_id) AS referenced_table,
                col_ref.name AS referenced_column
            FROM sys.foreign_key_columns fkc
            INNER JOIN sys.columns col
                ON fkc.parent_object_id = col.object_id
                AND fkc.parent_column_id = col.column_id
            INNER JOIN sys.columns col_ref
                ON fkc.referenced_object_id = col_ref.object_id
                AND fkc.referenced_column_id = col_ref.column_id
            WHERE OBJECT_NAME(referenced_object_id) IS NOT NULL
            """
    cursor.execute(query)

    # In ra thông tin mối quan hệ giữa các bảng
    for row in cursor.fetchall():
        parent_table, parent_column, referenced_table, referenced_column = row
        print(f"Table: {parent_table} ({parent_column}) -> Table: {referenced_table} ({referenced_column})")
    conx.close()

def print_query(query):
    # global conn_str  # Khai báo rằng bạn muốn sử dụng biến conn_str toàn cục
    # print("CÂU TRUY VẤN")
    # print("---")
    # # print(query)
    # print("---")

    # Kết nối đến cơ sở dữ liệu
    conx = pyodbc.connect(conn_str) 
    
    # Đọc dữ liệu từ truy vấn và tạo DataFrame
    df = pd.read_sql(query, conx)
    conx.commit()
    # Đóng kết nối pyodbc
    conx.close()

    # Hiển thị DataFrame
    return df

def create_tbl_query(query, table_name):
    # global conn_str  # Khai báo rằng bạn muốn sử dụng biến conn_str toàn cục
    # print("CÂU TRUY VẤN")
    # print("---")
    # # print(query)
    # print("---")
    
    try:
        # Kết nối đến cơ sở dữ liệu
        conx = pyodbc.connect(conn_str)

        # Thực hiện truy vấn và tạo bảng
        cursor = conx.cursor()
        cursor.execute(query)

        # Xác nhận thay đổi
        conx.commit()
        print(cursor.rowcount)
        if cursor.rowcount == -1:
            print("Đã tạo bảng thành công")
            print("="*30)
        else:
            print(f"Đã chèn {cursor.rowcount} dòng vào bảng {table_name}")
            print("="*30)


    except Exception as e:
        print("Đã xảy ra lỗi:\n", e)

    finally:
        # Đóng kết nối pyodbc
        conx.close()