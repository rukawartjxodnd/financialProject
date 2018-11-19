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
        print("option 값 오류: ", option)
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
def cmpIntstIncreaseRatio(firstYearValue, lastYearValue, years):
    try:
        returnValue = (lastYearValue / firstYearValue) ** (1 / years) * 100 - 100
    except:
        returnValue = 0
    return returnValue
