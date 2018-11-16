import yy_libs.extract_stock_factor as stockFactor
import yy_libs.com_to_number as toNum
import yy_libs.com_calculator as cal


# 피터린치의 기준에 의한 종목 검증
# PER < 3년 평균 PER
# 3년간 매출액 성장률 > 10%
# 3년간 매출액 성장률 > 3년간 재고자산 성장률
# 20% < 5년간 순이익 증가율 < 50%
# 영업이익률 > 10%
# 이자보상배율(배) > 2
def verifyPL(companyCode):
    bsFactor = stockFactor.extractBasicFactor(companyCode)
    subFactor = stockFactor.extractSubFactor(companyCode)
    indFactor = stockFactor.extractIndustryFactor(companyCode)
    annFactor = stockFactor.extractAnnualFactor(companyCode)

    print(bsFactor)
    print(subFactor)
    print(indFactor)
    print(annFactor)

    # 기본정보
    print(bsFactor['companyCode'])
    print(bsFactor['companyName'])
    # PER
    print(bsFactor['m12Per'])
    # 3년 평균 PER
    year3PerIn = [annFactor['per'][3], annFactor['per'][4], annFactor['per'][5]]
    year3PerInNum = toNum.toNumber(year3PerIn)
    year3AvePer = cal.getAvg(year3PerInNum)
    print(year3AvePer)
    # 3년 매출액 성장률
    


    return -1

print(verifyPL("005930"))