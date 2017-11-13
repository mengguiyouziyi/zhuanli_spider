import pymysql
import logging
import traceback
import multiprocessing

# 创建一个logger
logger = logging.getLogger('Patent_log')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('./lib/Patent.log')
# fh.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(process)d - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
# ---------↑↑↑↑↑↑↑定义日志↑↑↑↑↑↑↑↑-----------


buchang = 5000
# 批量插入的数据
insert_data = []
# 插入数据阈值
insert_num = 1
# 定义连接
connection = None


def openConn():
    db_host = '172.31.215.38'
    db_user = 'etl_m'
    db_password = 'innotree'
    db_port = 3306
    connection = pymysql.connect(host=db_host, user=db_user, password=db_password,
                                 port=db_port, charset='utf8', cursorclass=pymysql.cursors.SSCursor
                                 )
    return connection


def processAll(result, connection):
    global insert_data
    global insert_num
    words = ["纳米发电机", "纳米发电模组", "纳米传感器", "NEMS", "纳机电系统", "纳米发电薄膜", "纳米风力发电薄膜", "纳米风力发电", "纳米摩擦传感电缆", "纳米摩擦", "纳米传感电缆",
             "纳米摩擦电缆", "纳米传感带", "纳米自发电鞋", "纳米发电鞋", "压电传感器", "生理监测传感带", "生理信号采集传感带", "纳米自发电鞋",
             "自发光鞋", "智能计步鞋", "追踪鞋", "智能看护鞋", "足部理疗鞋", "自发电防伪", "高端酒防伪", "化妆品防伪", "物流防伪", "药品防伪", "纳米防伪", "微纳传感器",
             "微型能量收集", "石墨烯微型超级电容器", "石墨烯超级电容器", "石墨烯微型电容器", "石墨烯电容器", "压电传感电缆", "压电传感电缆", "纳米氧化锌", "紫外线传感器",
             "硅基紫外线传感器", "气流传感器", "气动传感（器）", "电子烟传感器", "雾化器传感器", "通用雾化器传感器", "医用雾化器传感器", "气体检测传感器", "智能睡眠传感器",
             "智能枕头传感器", "居家养老监护器", "智能床垫传感器", "智能坐垫传感器"]
    for one in result:
        if one[-1] != 'CN' or one[0].replace(' ', '').isalpha():
            continue
        intro = one[0] + one[1]
        for word in words:
            if word in intro:
                values = one[:-1] + (word,)
                insert_data.append(values)
                if len(insert_data) >= insert_num:
                    insertList(insert_data, connection)
                    insert_data.clear()
        word_1, word_2 = "可自发电+纳米".split('+')
        if word_1 in intro and word_2 in intro:
            values = one[:-1] + ('可自发电 + 纳米',)
            insert_data.append(values)
            if len(insert_data) >= insert_num:
                insertList(insert_data, connection)
                insert_data.clear()


def readSQL(st, ed):
    """
        从数据库读取所有 ID
    :return:
    """
    global connection
    global insert_data
    connection = openConn()
    with connection.cursor() as cursor:
        for i in range(st, ed):
            logger.info("处理第 {i} 张表".format(i=i))
            # 阈值
            start = 0
            while True:
                logger.info("处理 {buchang} 条".format(buchang=buchang))
                # print("处理 {buchang} 条".format(buchang=buchang))
                sql = """select title,abs,pubnumber,appdate,applicantname,appcoun from spider.patent_{num} limit {start},{buchang}""".format(
                    num=i, start=start, buchang=buchang)
                cursor.execute(sql)
                result = cursor.fetchall()
                if result.__len__() < buchang:
                    processAll(result, connection)
                    break
                start += buchang
                processAll(result, connection)
            if len(insert_data) > 0:
                insertList(insert_data, connection)
                insert_data.clear()


def insertList(many: list, connection):
    """
        插入多条数据
    :param many:
    :return:
    """
    sql = """insert into spider.patent_nami(title,abs,pubnumber,appdate,applicantname,guanjianzi) VALUES (%s,%s,%s,%s,%s,%s)"""
    with connection.cursor() as cursor:
        cursor.executemany(sql, many)
    logger.info(multiprocessing.current_process().name + " 插入数据 {num} 条".format(num=many.__len__()))
    connection.commit()


if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=2)
    readSQL(1, 3)
    print('程序运行结束。')
