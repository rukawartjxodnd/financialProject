import yy_libs.crawler_finance_detail_information as detailInfo

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

