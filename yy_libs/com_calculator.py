# 입력된 numList를 이용하여 계산 수행


# 합
def getSum(nums):
    sumVal = 0
    for element in nums:
        sumVal = sumVal + element
    return sumVal


# 평균
# option: 0->모두, 1->음수제외, 2->양수만
def getAvg(nums, option=0):
    # 합 및 제수 구하기
    devideNum = 0
    sumVal = 0

    if option not in [0, 1, 2]:
        print("option 값 오류(com_calculator.getAvg): ", option)
        raise ValueError

    for num in nums:
        if option == 0:
            devideNum = devideNum + 1
            sumVal = sumVal + num
        elif option == 1 and num >= 0:
            devideNum = devideNum + 1
            sumVal = sumVal + num
        elif option == 2 and num > 0:
            devideNum = devideNum + 1
            sumVal = sumVal + num

    try:
        avgVal = sumVal / devideNum
    except:
        avgVal = 0

    return avgVal


# 복리 증가율
def cmpIntstIncreaseRatio_old(firstYearValue, lastYearValue, years):
    figure = ''
    ratio = 0

    # 양수인 경우 정상 계산
    if firstYearValue >= 0 and lastYearValue >= 0:
        try:
            figure = '양수지속'
            ratio = (lastYearValue / firstYearValue) ** (1 / years) * 100 - 100
        except ZeroDivisionError:
            figure = '양수전환'
            ratio = 0
        except :
            figure = '계산오류'
            ratio = 0

    # 음수처리
    elif firstYearValue >= 0 and lastYearValue < 0:
        figure = '음수전환'
        ratio = 0
    elif firstYearValue < 0 and lastYearValue >= 0:
        figure = '양수전환'
        ratio = 0
    elif firstYearValue < 0 and lastYearValue < 0:
        figure = '음수지속'
        ratio = 0

    return {'figure': figure, 'ratio': ratio}


# 복리 증가율
def cmpIntstIncreaseRatio(yearValues):
    # 사용 되는 제수, 피제수 설정
    firstYearValue = yearValues[0]
    lastYearValue  = yearValues[0]
    years = 0

    for yearValue in yearValues[1:]:
        if yearValue != 0:
            lastYearValue = yearValue
            years = years +1

    # 0년 데이타 이면 계산 X
    if years == 0:
        figure = 'NO DATA'
        ratio = 0

    # 양수인 경우 정상 계산
    elif firstYearValue >= 0 and lastYearValue >= 0:
        try:
            figure = '양수지속'
            ratio = (lastYearValue / firstYearValue) ** (1 / years) * 100 - 100
        except ZeroDivisionError:
            figure = '양수전환'
            ratio = 0
        except :
            figure = '계산오류'
            ratio = 0

    # 음수처리
    elif firstYearValue >= 0 and lastYearValue < 0:
        figure = '음수전환'
        ratio = 0
    elif firstYearValue < 0 and lastYearValue >= 0:
        figure = '양수전환'
        ratio = 0
    elif firstYearValue < 0 and lastYearValue < 0:
        figure = '음수지속'
        ratio = 0

    return {'figure': figure, 'ratio': ratio}
