import yy_libs.crawler_finance_detail_information as detailInfo

# 종목코드를 입력 받아서 해당 종목의 해당업종과의 비교정보 추출
# [당사, 업종, 소속(코스피/코스닥)] 순서로 리턴
def extractIndustryFactor(compCode):
    valuesInTrs = []
    inputObj = detailInfo.getDetailFinanceInfo(compCode)["industryInfoGroup"]
    trs = inputObj.find_all("tr")

    # 루프 돌면서 추출
    for tr in trs:
        valuesInTds = []
        tds = tr.find_all("td")
        for td in tds:
            valuesInTds.append(td.text)
        valuesInTrs.append(valuesInTds)

    return {"totalValue": valuesInTrs[0], "revenue": valuesInTrs[1], "profit": valuesInTrs[2],
            "eps": valuesInTrs[3], "per": valuesInTrs[4], "evEbitda": valuesInTrs[5],
            "roe": valuesInTrs[6], "divYeild": valuesInTrs[7], "beta": valuesInTrs[8], }

