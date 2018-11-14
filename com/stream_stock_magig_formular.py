import yy_libs.crawler_finance_infomation as financeInfo
import yy_libs.filtering_finance_information as filteringInfo
import yy_libs.sorting_finance_information as sortingInfo

# 쓰기파일 오픈
resultFile = open("../data/perRoeResultFile.csv", "w+", encoding="euc-kr")
resultFile.write("소속"+","+"종목코드"+","+"종목명"+","+"현재가"+ "," +"시가총액(억)"+","+"PER"+","+"ROE"+","+"PER순위"+","+"ROE순위"+","+"순위합산"+","+"종합순위"+","+"종목그래프"+"\n")

# 전체 data 취합 및 필터링
totalDataList = []
# 코스피(1, 31+1)
for pageNum in range(15,17+1):
    financeInfoList = financeInfo.getPrices("0", str(pageNum))
    totalDataList = totalDataList + filteringInfo.filteringData("KOSPI", financeInfoList)
# 코스닥(1, 26+1)
for pageNum in range(15,17+1):
    financeInfoList = financeInfo.getPrices("1", str(pageNum))
    totalDataList = totalDataList + filteringInfo.filteringData("KOSDAQ", financeInfoList)

# 전체 파일 리스트를 per 기준 sort
sortForPer = sortingInfo.sortingListSimpleValue(totalDataList, 5, False)
# 전체 파일 리스트를 roe 기준 sort
sortForPerAndRoe = sortingInfo.sortingListSimpleValue(sortForPer, 6, True)
# per 및 roe 순위 합산 후 sort
sortForPerAndRoeComplex = sortingInfo.sortingListComplexValue(sortForPerAndRoe)

# 파일쓰기
for eachGroup in sortForPerAndRoeComplex:
    for eachValue in eachGroup:
        resultFile.write(str(eachValue))
        resultFile.write(',')
    resultFile.write('https://finance.naver.com/item/main.nhn?code='+eachGroup[1].replace("'",""))
    resultFile.write('\n')

