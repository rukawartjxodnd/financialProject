import requests
from bs4 import BeautifulSoup

# 개별 종목정보 값을 입력 받아서 계산에 필요한 정보를 획득
def getDetailFinanceInfo(companyCode):

    # main page호출
    url = "http://comp.fnguide.com/SVO2/ASP/SVD_main.asp?pGB=1&gicode=A"+companyCode+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701"
    pageCallResult = requests.get(url)
    bs_obj = BeautifulSoup(pageCallResult.content,"html.parser")

    # 기본 정보 영역 추출
    basicInfoGroup = bs_obj.find("div", {"class": "section ul_corpinfo"})
    # 서브 정보 영역 추출
    subInfoGroup = bs_obj.find("table",{"class": "us_table_ty1 table-hb thbg_g h_fix zigbg_no"}).find("tbody")
    # 업계비교정보 추출
    industryInfoGroup = bs_obj.find("div", {"class": "ul_wrap","id": "div9"}).find("table", {"class": "us_table_ty1 h_fix zigbg_no th_topbdno"}).find("tbody")
    # 변도별 상세 정보 테이블 추출
    annualInfoGroup = bs_obj.find("div", {"class": "um_table", "id": "highlight_D_Y"}).find("tbody")

    # finance page호출
    url = "http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A"+companyCode+"&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701"
    pageCallResult = requests.get(url)
    bs_obj = BeautifulSoup(pageCallResult.content,"html.parser")

    # 연도별 대차대조표 정보 테이블 추출
    annualFinanceInfoGroup = bs_obj.find("div", {"class": "um_table", "id": "divDaechaY"}).find("tbody")

    # 연도별 손익계산서 정보 테이블 추출
    annualIncomeStatInfoGroup = bs_obj.find("div", {"class": "um_table", "id": "divSonikY"}).find("tbody")

    return {"basicInfoGroup": basicInfoGroup,
            "subInfoGroup": subInfoGroup,
            "industryInfoGroup": industryInfoGroup,
            "annualInfoGroup": annualInfoGroup,
            "annualFinanceInfoGroup": annualFinanceInfoGroup,
            "annualIncomeStatInfoGroup": annualIncomeStatInfoGroup}


