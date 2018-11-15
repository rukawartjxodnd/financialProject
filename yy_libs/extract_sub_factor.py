import yy_libs.crawler_finance_detail_information as detailInfo

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
