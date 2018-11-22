# 입력된 단일 str 또는 strList를 숫자로 변환

# 개별요소 변환
def convertToNumber(str):
    # 천자리 콤마 제거
    str = str.replace(",", "")

    # 소숫점을 가지고 있으면 소수형 변환
    # 오류 발생시 0 반환
    if "." in str:
        try:
            numValue = float(str)
        except:
            numValue = 0
    else:
        try:
            numValue = int(str)
        except:
            numValue = 0

    return numValue

# List요소 변환
def convertListToNumber(strList):

    # 개별 숫자별로 숫자 변환
    # 오류 발생시 0 반환
    numValueList = []
    for str in strList:
        numValue = convertToNumber(str)
        numValueList.append(numValue)

    return numValueList

# List 여부 판별후 적용
def toNumber(inputValue):
    if isinstance(inputValue, list):
        resultValue = convertListToNumber(inputValue)
    else:
        resultValue = convertToNumber(inputValue)
    return resultValue
