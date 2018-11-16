import yy_libs.crawler_finance_detail_information as detailInfo

# 종목코드를 입력 받아서 해당 종목의 기본정보 추출
def extractBasicFactor(compCode):
    inputObj = detailInfo.getDetailFinanceInfo(compCode)["basicInfoGroup"]
    companyCode = compCode
    companyName = inputObj.find("h1").text

    values = inputObj.find("div", {"class": "corp_group2", "id": "corp_group2"}).find_all("dd")
    closingPer = values[1].text
    m12Per = values[3].text
    industryPer = values[5].text
    closingPbr = values[7].text
    divYeild = values[9].text.replace("%", "")

    return {"companyCode": companyCode, "companyName": companyName, "closingPer": closingPer, "m12Per": m12Per, "industryPer": industryPer, "closingPbr": closingPbr, "divYeild": divYeild}


# 종목코드를 입력 받아서 해당 종목의 서브정보 추출
def extractSubFactor(compCode):
    inputObj = detailInfo.getDetailFinanceInfo(compCode)["subInfoGroup"]

    # 종가
    closingPrice = inputObj.find_all("tr")[0].find("td", {"class": "r"}).text.split("/")[0].replace(",", "")
    # 전일대비
    closingVariation = inputObj.find_all("tr")[0].find("td", {"class": "r"}).text.split("/")[1].replace(",", "")
    # 거래량
    dealMass = inputObj.find_all("tr")[0].find("td", {"class": "cle r"}).text.replace(",", "")
    # 52주 최고가
    week52Highist = inputObj.find_all("tr")[1].find("td", {"class": "r"}).text.split("/")[0].replace(",", "")
    # 52주 최저가
    week52Lowist = inputObj.find_all("tr")[1].find("td", {"class": "r"}).text.split("/")[1].replace(",", "")
    # 거래대금
    dealMoney = inputObj.find_all("tr")[1].find("td", {"class": "cle r"}).text.replace(",", "")+"00000000"
    # 외국인보유비중
    ForeignerRatio = inputObj.find_all("tr")[2].find("td", {"class": "cle r"}).text.replace(",", "")
    # 시가총액
    totalValue = inputObj.find_all("tr")[3].find("td", {"class": "r"}).text.replace(",", "")+"00000000"
    # 베타
    beta = inputObj.find_all("tr")[3].find("td", {"class": "cle r"}).text.replace(",", "")
    # 발행주식수(보통주)
    basicIssueStockQuentity = inputObj.find_all("tr")[4].find("td", {"class": "r"}).text.split("/")[0].replace(",", "")
    # 발행주식수(우선주)
    priorIssueStockQuentity = inputObj.find_all("tr")[4].find("td", {"class": "r"}).text.split("/")[1].replace(",", "")
    # 액면가
    faceValue = inputObj.find_all("tr")[4].find("td", {"class": "cle r"}).text.replace(",", "")
    # 유동주식수
    floatStock = inputObj.find_all("tr")[5].find("td", {"class": "r"}).text.replace(",", "")
    # 유동주식비율
    floatStockRatio = inputObj.find_all("tr")[5].find("td", {"class": "cle r"}).text.replace(",", "")

    return {"closingPrice": closingPrice, "closingVariation": closingVariation, "dealMass": dealMass
        , "week52Highist": week52Highist, "week52Lowist": week52Lowist, "dealMoney": dealMoney
        , "ForeignerRatio": ForeignerRatio, "totalValue": totalValue, "beta": beta
        , "basicIssueStockQuentity": basicIssueStockQuentity, "priorIssueStockQuentity": priorIssueStockQuentity
        , "faceValue": faceValue, "floatStock": floatStock, "floatStockRatio": floatStockRatio}

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

# 종목코드를 입력 받아서 해당 종목의 6개년도 정보 추출
# [-5년, -4년, -3년, -2년, -1년, 당해년] 순서로 리턴
def extractAnnualFactor(compCode):
    valuesInTrs = []
    inputObj = detailInfo.getDetailFinanceInfo(compCode)["annualInfoGroup"]
    trs = inputObj.find_all("tr")

    # 루프 돌면서 추출 (매출액, 영업이익, 영업이익률(%), ROA, ROE, EPS, BPS, DPS, PER, PBR, 배당수익률 만 추출: 추후 추가 가능함)
    # 해당 항목의 index는 전체 trs에서 0, 1, 13, 15, 16, 17, 18, 19, 20, 21, 23 임.
    index = 0

    for tr in trs:
        if index not in [0, 1, 13, 15, 16, 17, 18, 19, 20, 21, 23]:
            index = index + 1
            continue

        # 년도별 루핑
        tds = []
        for td in tr.find_all("td", {"class": "r"})[:6]:
            # 단위가 '억' 인 것 보정
            if index in [0, 1]:
                tds.append(td.text.replace(",", "")+'00000000')
            else:
                tds.append(td.text.replace(",", ""))

        valuesInTrs.append(tds)
        index = index + 1

    return {"revenue": valuesInTrs[0], "profit": valuesInTrs[1], "profitRatio": valuesInTrs[2],
            "roa": valuesInTrs[3], "roe": valuesInTrs[4],
            "eps": valuesInTrs[5], "bps": valuesInTrs[6], "dps": valuesInTrs[7],
            "per": valuesInTrs[8], "pbr": valuesInTrs[9],
            "divYeild": valuesInTrs[10]}