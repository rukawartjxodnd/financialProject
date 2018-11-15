import yy_libs.crawler_finance_detail_information as detailInfo

# 종목코드를 입력 받아서 해당 종목의 기본정보 추출
def extractBasicFactor(compCode):
    inputObj = detailInfo.getDetailFinanceInfo(compCode)["basicInfoGroup"]
    companyCode = compCode
    companyName = inputObj.find("h1").text

    values = inputObj.find("div", {"class": "corp_group2", "id": "corp_group2"}).find_all("dd")
    closingRer = values[1].text
    m12Rer = values[3].text
    industryRer = values[5].text
    closingRbr = values[7].text
    divYeild = values[9].text.replace("%", "")

    return {"companyCode": companyCode, "companyName": companyName, "closingRer": closingRer, "m12Rer": m12Rer, "industryRer": industryRer, "closingRbr": closingRbr, "divYeild": divYeild}
