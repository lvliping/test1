#coding=utf-8
import pymysql
import traceback
ip = "188.131.183.182"
port = 3306
user = "root"
password = "12345678x"
database = "hahu2"
def insert_delete_update(sql):
    cur = None
    conn = None
    try:
        conn = pymysql.Connect(host=ip,user=user,password=password,database=database,charset='UTF8')
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
    except:
        print(traceback.format_exc())
    finally:
        try:
            if cur:
                cur.close()
        except:
            print('运行错误')
        finally:
            if conn:
                conn.close()
def select(sql):
    cur = None
    conn = None
    try:
        conn = pymysql.Connect(host=ip,user=user,password=password,database=database,charset='UTF8')
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        # print(data)
        return data

    except:
        print(traceback.format_exc())
    finally:
        try:
            if cur:
                cur.close()
        except:
            print('错误')
        finally:
            if conn:
                conn.close()
if __name__ == '__main__':
    sql = """SELECT * FROM collection WHERE
               user_id=11217 AND collection_name="第一个收藏夹" 
               AND is_delete=0;"""
    select(sql)
    # insert_delete_update('insert into student_llp values("0019","wang","yuwen",90);')