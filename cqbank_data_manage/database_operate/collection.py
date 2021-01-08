#coding=utf-8
from database_operate.DBUitls import select
def collection_isexist(userid, collection_name):
    """查看用户是否创建收藏夹成功，查找有数据则创建成功"""
    sql = """SELECT * FROM collection WHERE
   user_id="{userid}" AND collection_name="{collection_name}" 
   AND is_delete=0;""".format(userid=userid,collection_name=collection_name)
    # print(sql)
    result = select(sql)
    # print(result)
    # print(len(result))
    if len(result)>0:
        # print("创建成功")
        return True
    else:
        # print("创建失败")
        return False
def delet_colletion(collection_userid, collection_name):
    """删除指定用户指定的收藏夹"""
    sql1 = """UPDATE collection set is_delete=1 
    WHERE user_id="{userid}" 
    AND collection_name="{collection_name}";""" .format(userid=collection_userid,collection_name=collection_name)

    # 验证用户是否成功删除收藏夹，若查找的数量大于0，则代表删除成功
    sql2 = """SELECT * FROM collection WHERE user_id= "{userid}" 
      AND collection_name="{collection_name}" 
      AND is_delete=1;""".format(userid=collection_userid,collection_name=collection_name)
    result = select(sql2)
    # print(result)
    if len(result)>0:
        return True
    else:
        return False

if __name__ == '__main__':
    collection_isexist(11217,"第一个收藏夹")
    # delet_colletion(11217,"第一个收藏夹")
