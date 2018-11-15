import yy_libs.crawler_finance_detail_information as detailInfo

# 종목코드를 입력 받아서 해당 종목의 6개년도 정보 추출
# [당사, 업종, 소속(코스피/코스닥)] 순서로 리턴
def extractAnnualFactor(compCode):
    valuesInTrs = []
    inputObj = detailInfo.getDetailFinanceInfo(compCode)["annualInfoGroup"]
    trs = inputObj.find_all("tr")

    # 루프 돌면서 추출 (매출액, 영업이익, ROA, ROE, EPS, BPS, DPS, PER, PBR, 배당수익률 만 추출: 추후 추가 가능함)
    for tr in trs:
        valuesInTds = []
        tds = tr.find_all("td")

        if tr.find("th",{"class": "clf"}).find("div").text not in ['매출액', '영업이익', 'ROA(%)', 'ROE(%)', 'EPS(원)', 'BPS(원)', 'DPS(원)', 'PER(배)', 'PBR(배)', '배당수익률(%)']:
            continue

        # for td in tds:
        #     valuesInTds.append(td.text)
        # valuesInTrs.append(valuesInTds)
        print(tr.find("th",{"class": "clf"}).find("div").text)
    # return {"totalValue": valuesInTrs[0], "revanue": valuesInTrs[1], "profit": valuesInTrs[2],
    #         "eps": valuesInTrs[3], "per": valuesInTrs[4], "evEbitda": valuesInTrs[5],
    #         "roe": valuesInTrs[6], "divYeild": valuesInTrs[7], "beta": valuesInTrs[8], }
    print(inputObj)
print(extractAnnualFactor("005930"))
