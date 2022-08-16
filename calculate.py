#Q1: Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.

lista = [4,5,7,2,3,50,60]
def calc_low(listA):
    listA.sort()
    return listA[0] + listA[1]
#esult = calc_low(lista)
#print(result)



#Q2: Given an array of integers.Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.


listb =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def SumOf(listc):
    FinalResult = []
    ResultofNeg = []
    ResultsofPos = []
    for x in listc:
        if x > 0:
            ResultsofPos.append(x)
        else:
            ResultofNeg.append(x)
    ResultsofPos = sum(ResultsofPos)
    ResultofNeg = sum(ResultofNeg)
    FinalResult.append(ResultsofPos)
    FinalResult.append(ResultofNeg)
    return FinalResult
FinalResults = SumOf(listb)

print(FinalResults)
             

