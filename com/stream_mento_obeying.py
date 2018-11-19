import yy_libs.verification_Peter_Lynch as pl
import yy_libs.com_company_code as inputCode

# 대가들의 이론을 추출한 공식을 따라서 주식 종목을 판별하여
# 조건에 합당하면 별도로 파일 저장

# 대상 코드 추출
codeList = inputCode.getCompanyCodes('KOS')

#################################
# 피터린치
#################################

# 쓰기파일 오픈
resultFile = open("../data/ResultFile_Peter_Lynch.csv", "w+", encoding="euc-kr")
resultFile.write("종목코드"+","+"종목명"+","+"PER"+ "," +"3년 평균 PER"+","+"3년 매출액 성장률"+","+
                 "3년 재고자산 성장률"+","+"5년간 순이익 증가율"+","+"영업이익률"+","+"이자보상배율"+","+
                 "PER < 3년 평균 PER"+","+"3년간 매출액 성장률 > 10%"+","+"3년간 매출액 성장률 > 3년간 재고자산 성장률"+","+
                 "20% < 5년간 순이익 증가율 < 50%"+","+"영업이익률 > 10%"+","+"이자보상배율(배) > 2"+","+"조건충족 갯수"+"\n")

# 종목별 검증 후 파일 쓰기
for companyCode in codeList[:20]:
    try:
        # 뒤의 숫자는 만족하는 기준 갯수를 의미 함.
        resultDictionary = pl.verifyPL(companyCode['code'],3)
        if resultDictionary["PrintYn"]:
            resultFile.write("'"+resultDictionary["companyCode"]+","+
                             resultDictionary["companyName"]+","+
                             str(resultDictionary["per"])+","+
                             str(resultDictionary["year3AvePer"])+","+
                             str(resultDictionary["year3IncreaseRatioRevenue"])+","+
                             str(resultDictionary["year3IncreaseRatioInventory"])+","+
                             str(resultDictionary["year5IncreaseRatioIncome"])+","+
                             str(resultDictionary["roogtr"])+","+
                             str(resultDictionary["InrtCompMagni"])+","+
                             resultDictionary["Yn1"]+","+resultDictionary["Yn2"]+","+resultDictionary["Yn3"]+","+
                             resultDictionary["Yn4"]+","+resultDictionary["Yn5"]+","+resultDictionary["Yn6"]+","+
                             str(resultDictionary["meetNum"]) + "\n")
    except :
        print("error: "+companyCode['code'])

resultFile.close()
