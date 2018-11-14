from operator import itemgetter


# dataList: 입력 data set, orderBase: 정렬 기준 되는 인자, reverseYn: 내림차순 정렬 여부
def sortingListSimpleValue(dataGroupList, orderBase, reverseYn):

    # 전체 파일 리스트를 base 기준 sort
    sortedGrooupLists = sorted(dataGroupList, key=itemgetter(orderBase), reverse=reverseYn)

    # sort 결과에 순위 부여
    order = 0
    sortedListAndOrder = []
    for sortedGrooup in sortedGrooupLists:
        order = order + 1
        eachResult = []

        # 각 인자 저장 후 맨 끝에 순위 부여
        for value in sortedGrooup:
            eachResult.append(value)
        eachResult.append(order)

        sortedListAndOrder.append(eachResult)

    return sortedListAndOrder


# dataList: 입력 data set, orderBase: 정렬 기준 되는 인자, reverseYn: 내림차순 정렬 여부
def sortingListComplexValue(dataGroupList):
    # 결과 List
    middleResultList = []
    # 전체파일 리스트에서 per과 roe순위를 단순 합산
    for dataGroup in dataGroupList:

        eachResult = []
        for value in dataGroup:
            eachResult.append(value)
        eachResult.append(eachResult[7]+eachResult[8])

        middleResultList.append(eachResult)

    resultList = sortingListSimpleValue(middleResultList, 9, False)
    return resultList