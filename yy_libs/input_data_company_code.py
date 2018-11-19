import requests
from bs4 import BeautifulSoup

def getCompanyCodes():
    url = "http://bigdata-trader.com/itemcodehelp.jsp"
    pageCallResult = requests.get(url)
    bs_obj = BeautifulSoup(pageCallResult.content, "html.parser")

    # 종목코드와 종목명 존재하는 tag 찾기
    trs = bs_obj.find_all("tr")

    # return List
    resultCodes = []

    # code와 종목명 List에 담기
    for tr in trs:
        code = tr.find("a").text
        name = tr.find_all("td")[1].text
        code_name = code+" "+name
        returnValue = {"code": code, "code_name": code_name}
        resultCodes.append(returnValue)

    return resultCodes
