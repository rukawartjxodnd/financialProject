# 필터링
def filteringData(sosok, financeInfoList):
    # 결과 리스트
    resultList = []

    # 반복통한 data 필터링
    for financeInfo in financeInfoList:
        companyCode = financeInfo["companyCode"]
        companyName = financeInfo["companyName"]
        presentPrice = financeInfo["presentPrice"]
        totalValue = financeInfo["totalValue"]
        per = financeInfo["per"]
        roe = financeInfo["roe"]

        # 조건설정
        if int(totalValue) < 0:
            continue
        if per == "N/A" or roe == "N/A":
            continue
        if float(per) < 0 or float(roe) < 0:
            continue
        else:
            resultList.append((sosok, companyCode, companyName,presentPrice,totalValue,float(per),float(roe)))
    return resultList