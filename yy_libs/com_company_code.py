import requests
from bs4 import BeautifulSoup
# import psycopg2 as pg2
# import config.dbConfig as dbConfig
import config.db_connect as dbConnect
from datetime import datetime as dt

def getCompanyCodes(kind = ''):
    url = "http://bigdata-trader.com/itemcodehelp.jsp"
    pageCallResult = requests.get(url)
    bs_obj = BeautifulSoup(pageCallResult.content, "html.parser")

    # 종목코드와 종목명 존재하는 tag 찾기
    trs = bs_obj.find_all("tr")

    # return List
    resultCodes = []

    # code와 종목명 List에 담기
    for tr in trs:
        code = tr.find("a").text
        name = tr.find_all("td")[1].text
        sosok = tr.find_all("td")[2].text
        code_name = code+" "+name
        returnValue = {"code": code, "code_name": code_name, "sosok": sosok}

        if kind in sosok and name[-1] not in ['우', 'B']:
            resultCodes.append(returnValue)
    return resultCodes

def CodeDataToDB (codeLists):

    # DB Connect
    connection = dbConnect.dataBaseConnect()
    cursor = connection.cursor()

    # table clear
    cursor.execute("delete from company_code")
    cursor.execute('commit')

    # codeLists별 DB insert
    sql = "insert into company_code(code, name, kind, last_update_day)values (%s, %s, %s, %s);"
    for code in codeLists:
        try:
            cursor.execute(sql, (code['code'], code['code_name'][7:], code['sosok'], dt.now(),))
        except:
            print("error(com_company_code.CodeDataToDB): "+ code['code'], code['code_name'][7:], code['sosok'])
        finally:
            cursor.execute('commit')

    # DB종료, DB연결 해제
    connection.commit
    cursor.close
    connection.close


def getCompanyCodesFromDb (kind = ''):

    # DB Connect
    connection = dbConnect.dataBaseConnect()
    cursor = connection.cursor()

    # 리스트 조회
    sql = "select code, name, kind from company_code where kind like %s"
    cursor.execute(sql, ("%"+kind+"%",))
    result = cursor.fetchall()

    # DB종료, DB연결 해제
    cursor.close
    connection.close

    # return List
    resultCodes = []

    for data in result:
        code = data[0]
        name = data[1]
        sosok = data[2]
        code_name = code+" "+name
        returnValue = {"code": code, "code_name": code_name, "sosok": sosok}
        resultCodes.append(returnValue)

    return resultCodes
