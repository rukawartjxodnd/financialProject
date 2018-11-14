import requests
from bs4 import BeautifulSoup


# 개별 종목 정보에서 상세 값을 크롤링
def getDetailPrices(tr):
    tdTltle   = tr.find("a", {"class": "tltle"})
    tdsNumber = tr.find_all("td", {"class": "number"})

    companyCode  = tdTltle['href'].replace("/item/main.nhn?code=", "")
    companyName  = tdTltle.text
    presentPrice = tdsNumber[0].text.replace(",","")
    totalValue   = tdsNumber[4].text.replace(",","")
    per = tdsNumber[8].text.replace(",","")
    roe = tdsNumber[9].text.replace(",","")

    return {"companyCode":"'"+companyCode,"companyName":companyName,"presentPrice":presentPrice,"totalValue":totalValue,"per":per,"roe":roe}

# 종목 목록에서 종목정보 검색
# sosok: 0=>코스피, 1=>코스닥
# page : 네이버 조회 목록 페이지
def getPrices(sosok, page):
    url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok="+sosok+"&page="+page
    pageCallResult = requests.get(url)
    bs_obj = BeautifulSoup(pageCallResult.content,"html.parser")

    # 가격요소 table
    pricesFactorsTable = bs_obj.find("table", {"class": "type_2"})
    pricesFactorsbody  = pricesFactorsTable.find("tbody")
    pricesFactorsTrs   = pricesFactorsbody.find_all("tr", {"onmouseover": "mouseOver(this)"})

    # 결과 Set
    resultSet = []

    for tr in pricesFactorsTrs:
        try:
            resultSet.append(getDetailPrices(tr))
        except:
            print("error: "+tr)

    return resultSet