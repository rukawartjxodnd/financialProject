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
def verifyPL(companyCode, printHuddle = 6):

    #################################
    # 각 페이지에서 데이터 크롤링
    #################################
    bsFactor = stockFactor.extractBasicFactor(companyCode)
    # subFactor = stockFactor.extractSubFactor(companyCode)
    # indFactor = stockFactor.extractIndustryFactor(companyCode)
    annFactor = stockFactor.extractAnnualFactor(companyCode)
    annFinFactor = stockFactor.extractAnnualFinanceFactor(companyCode)
    annIncomeFactor = stockFactor.extractAnnualIncomeStatFactor(companyCode)

    #################################
    # 개별 정보 추출
    #################################
    # 기본정보
    companyName = bsFactor['companyName']

    # PER
    per = toNum.toNumber(bsFactor['closingPer'])

    # 3년 평균 PER
    year3PerIn = [annFactor['per'][3], annFactor['per'][4], annFactor['per'][5]]
    year3PerInNum = toNum.toNumber(year3PerIn)
    year3AvePer = cal.getAvg(year3PerInNum,2)

    # 3년 매출액 성장률
    year3RevenueIn = [annFactor['revenue'][2], annFactor['revenue'][5]]
    year3RevenueInNum = toNum.toNumber(year3RevenueIn)
    year3IncreaseRatioRevenue = cal.cmpIntstIncreaseRatio(year3RevenueInNum[0], year3RevenueInNum[1], 3)

    # 3년 재고자산 성장률
    year3InventoryIn = [annFinFactor['inventory'][0], annFinFactor['inventory'][3]]
    year3InventoryInNum = toNum.toNumber(year3InventoryIn)
    year3IncreaseRatioInventory = cal.cmpIntstIncreaseRatio(year3InventoryInNum[0], year3InventoryInNum[1], 3)

    # 5년간 순이익 증가율
    year5IncomeIn = [annFactor['income'][0], annFactor['income'][5]]
    year5IncomeInNum = toNum.toNumber(year5IncomeIn)
    year5IncreaseRatioIncome = cal.cmpIntstIncreaseRatio(year5IncomeInNum[0], year5IncomeInNum[1], 3)

    # 영업이익률 (ratio of operating gain to revenue)
    roogtr = toNum.toNumber(annFactor['profitRatio'][5])

    # 이자보상배율 (영업이익/ 이자비용) (배)
    # 영업이익과 이자 비용 모두 0이 아닌 값 중 가장 최근 값 이용 한다.
    for index in range(3, -1, -1):
        opProfit = annIncomeFactor['opProfit'][index]
        interestCost = annIncomeFactor['interestCost'][index]
        if toNum.toNumber(opProfit) != 0 and toNum.toNumber(interestCost) != 0:
            break
    # 배율 구하되 0으로 나누는 경우 0배로 처리 함
    try:
        InrtCompMagni = toNum.toNumber(opProfit) / toNum.toNumber(interestCost)
    except(ZeroDivisionError):
        InrtCompMagni = 100


    #################################
    # 조건판별
    #################################
    Yn1 = 'N'
    Yn2 = 'N'
    Yn3 = 'N'
    Yn4 = 'N'
    Yn5 = 'N'
    Yn6 = 'N'
    meetNum = 0
    PrintYn = False

    # PER < 3년 평균 PER
    if per < year3AvePer:
        Yn1 = 'Y'
        meetNum = meetNum + 1

    # 3년간 매출액 성장률 > 10%
    if year3IncreaseRatioRevenue > 10:
        Yn2 = 'Y'
        meetNum = meetNum + 1

    # 3년간 매출액 성장률 > 3년간 재고자산 성장률
    if year3IncreaseRatioRevenue > year3IncreaseRatioInventory:
        Yn3 = 'Y'
        meetNum = meetNum + 1

    # 20% < 5년간 순이익 증가율 < 50%
    if year5IncreaseRatioIncome > 20 and year5IncreaseRatioIncome < 50:
        Yn4 = 'Y'
        meetNum = meetNum + 1

    # 영업이익률 > 10%
    if roogtr > 10:
        Yn5 = 'Y'
        meetNum = meetNum + 1

    # 이자보상배율(배) > 2
    if InrtCompMagni > 2:
        Yn6 = 'Y'
        meetNum = meetNum + 1

    if meetNum >= printHuddle:
        PrintYn = True

    #################################
    # return 설정
    #################################
    return {"companyCode": companyCode, "companyName": companyName,
            "per": per, "year3AvePer": year3AvePer,
            "year3IncreaseRatioRevenue": year3IncreaseRatioRevenue, "year3IncreaseRatioInventory": year3IncreaseRatioInventory,
            "year5IncreaseRatioIncome": year5IncreaseRatioIncome, "roogtr": roogtr, "InrtCompMagni": InrtCompMagni,
            "Yn1": Yn1, "Yn2": Yn2, "Yn3": Yn3, "Yn4": Yn4, "Yn5": Yn5, "Yn6": Yn6,"meetNum": meetNum,
            "PrintYn": PrintYn}
