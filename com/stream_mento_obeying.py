import yy_libs.verification_Peter_Lynch as pl
import yy_libs.com_company_code as inputCode
import config.db_connect as dbConnect
from datetime import datetime as dt

# 대가들의 이론을 추출한 공식을 따라서 주식 종목을 판별하여
# 조건에 합당하면 별도로 파일 저장

# 대상 코드 추출
codeList = inputCode.getCompanyCodes('KOS')[:30]
codeList = inputCode.getCompanyCodesFromDb('KOS')[:]

#################################
# 피터린치
#################################
def PeterLynchToFile(dataList, goalNun):
    # 쓰기파일 오픈
    resultFile = open("../data/ResultFile_Peter_Lynch.csv", "w+", encoding="euc-kr")
    resultFile.write("종목코드"+","+"종목명"+","+"PER"+ "," +"3년 평균 PER"+","+
                     "3년 매출액 추이"+","+"3년 매출액 성장률"+","+
                     "3년 재고자산 추이"+","+"3년 재고자산 성장률"+","+
                     "5년간 순이익 추이"+","+"5년간 순이익 증가율"+","+
                     "영업이익률"+","+"이자보상배율"+","+
                     "PER < 3년 평균 PER"+","+"3년간 매출액 성장률 > 10%"+","+"3년간 매출액 성장률 > 3년간 재고자산 성장률"+","+
                     "20% < 5년간 순이익 증가율 < 50%"+","+"영업이익률 > 10%"+","+"이자보상배율(배) > 2"+","+"조건충족 갯수"+"\n")

    # 종목별 검증 후 파일 쓰기
    for companyData in dataList:
        try:
            # 뒤의 숫자는 만족하는 기준 갯수를 의미 함.
            resultDictionary = pl.verifyPL(companyData['code'], goalNun)
            if resultDictionary["PrintYn"]:
                resultFile.write("'"+resultDictionary["companyCode"]+","+
                                 resultDictionary["companyName"]+","+
                                 str(resultDictionary["per"])+","+
                                 str(resultDictionary["year3AvePer"])+","+
                                 str(resultDictionary["year3IncreaseRatioRevenueFigure"]) + "," +
                                 str(resultDictionary["year3IncreaseRatioRevenueRatio"])+","+
                                 str(resultDictionary["year3IncreaseRatioInventoryFigure"]) + "," +
                                 str(resultDictionary["year3IncreaseRatioInventoryRatio"])+","+
                                 str(resultDictionary["year5IncreaseRatioIncomeFigure"]) + "," +
                                 str(resultDictionary["year5IncreaseRatioIncomeRatio"])+","+
                                 str(resultDictionary["roogtr"])+","+
                                 str(resultDictionary["InrtCompMagni"])+","+
                                 resultDictionary["Yn1"]+","+resultDictionary["Yn2"]+","+resultDictionary["Yn3"]+","+
                                 resultDictionary["Yn4"]+","+resultDictionary["Yn5"]+","+resultDictionary["Yn6"]+","+
                                 str(resultDictionary["meetNum"]) + "\n")
        except :
            print("error(stream_mento_obey.companyCode): ", companyData['code_name'])

    resultFile.close()

def PeterLynchToDB(dataList, goalNun):
    # DB
    connection = dbConnect.dataBaseConnect()
    cursor = connection.cursor()



    # DB종료, DB연결 해제
    connection.commit
    cursor.close
    connection.close

    # 당일
    nowDt = dt.today().strftime('%Y%m%d')
    nowDtTime = dt.now()

    # table clear
    sqlDel = "delete from stock_validation_Peter_Lynch where validate_day = %s;"
    cursor.execute(sqlDel, (nowDt,))
    cursor.execute('commit')

    # data별 DB insert
    sql = "insert into stock_validation_Peter_Lynch(" \
          "validate_day," \
          "code," \
          "name," \
          "per, " \
          "per_3avg, " \
          "revenue_3_increase_ment, " \
          "revenue_3_increase, " \
          "inventory_3_increase_ment, " \
          "inventory_3_increase, " \
          "income_5_increase_ment, " \
          "income_5_increase, " \
          "operation_margine, " \
          "In_comp_magn, " \
          "YN_per_3, " \
          "YN_revenue_3, " \
          "YN_revenue_inventory_3, " \
          "YN_revenue_income_5," \
          "YN_operation_margine," \
          "YN_in_comp_magn," \
          "meet_number, " \
          "last_update_day" \
          ")" \
          "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    for companyData in dataList:
        try:
            # 뒤의 숫자는 만족하는 기준 갯수를 의미 함.
            resultDictionary = pl.verifyPL(companyData['code'], goalNun)

            if resultDictionary["PrintYn"]:
                validate_day = nowDt
                code = resultDictionary['companyCode']
                name = resultDictionary['companyName']
                per = resultDictionary['per']
                per_3avg = resultDictionary['year3AvePer']
                revenue_3_increase_ment = resultDictionary['year3IncreaseRatioRevenueFigure']
                revenue_3_increase = resultDictionary['year3IncreaseRatioRevenueRatio']
                inventory_3_increase_ment = resultDictionary['year3IncreaseRatioInventoryFigure']
                inventory_3_increase = resultDictionary['year3IncreaseRatioInventoryRatio']
                income_5_increase_ment = resultDictionary['year5IncreaseRatioIncomeFigure']
                income_5_increase = resultDictionary['year5IncreaseRatioIncomeRatio']
                operation_margine = resultDictionary['roogtr']
                In_comp_magn = resultDictionary['InrtCompMagni']
                YN_per_3 = resultDictionary['Yn1']
                YN_revenue_3 = resultDictionary['Yn2']
                YN_revenue_inventory_3 = resultDictionary['Yn3']
                YN_revenue_income_5 = resultDictionary['Yn4']
                YN_operation_margine = resultDictionary['Yn5']
                YN_in_comp_magn = resultDictionary['Yn6']
                meet_number = resultDictionary['meetNum']
                last_update_day = nowDtTime

                cursor.execute(sql, (validate_day, code, name, per, per_3avg,
                                     revenue_3_increase_ment, revenue_3_increase,
                                     inventory_3_increase_ment, inventory_3_increase,
                                     income_5_increase_ment, income_5_increase,
                                     operation_margine, In_comp_magn,
                                     YN_per_3, YN_revenue_3, YN_revenue_inventory_3,
                                     YN_revenue_income_5, YN_operation_margine, YN_in_comp_magn,
                                     meet_number, last_update_day, ))
        except :
            print("error(stream_mento_obey.companyCode): ", companyData['code_name'])
        finally:
            cursor.execute('commit')

PeterLynchToFile(codeList, 0)