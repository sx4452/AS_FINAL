# -*- coding: utf-8 -*-
__auther__ = 'ben'

import time
import codecs
import copy

def TranslationRuleExtr(testch, testen, testalign):
    lengthCH = len(testalign)
    Trans = {}
    for i in xrange(1, lengthCH):
        for j in xrange(1, len(testalign[i])):
            index = testalign[i][j].split('-')
            index1 = int(index[0])
            index2 = int(index[1])
            strCH = testch[i][index1]
            strEN = testen[i][index2]
            if not Trans.has_key(strCH):
                Trans[strCH] = {}
            if Trans[strCH].has_key(strEN):
                Trans[strCH][strEN] += 1
            else:
                Trans[strCH][strEN] = 1
    Prob = copy.deepcopy(Trans)
    for strCH in Trans:
        allcnt = 0
        for strEN in Trans[strCH]:
            allcnt = allcnt + Trans[strCH][strEN]
        for strEN in Prob[strCH]:
            Prob[strCH][strEN] = float(Trans[strCH][strEN])/float(allcnt)
    OutputStr = ''
    for strCH in Prob:
        for strEN in Prob[strCH]:
            curStr = strCH + ' ||| '+ strEN + ' ||| ' + str(Trans[strCH][strEN]) + ' | ' + str(round(Prob[strCH][strEN], 2))
            OutputStr = OutputStr + curStr + '\r\n'
    return OutputStr

def InputData(fileName):
    Data = {}
    dataCnt = 0
    fileData = codecs.open(fileName, 'r', 'utf-8')
    isDone = 0
    while not isDone:
        line = fileData.readline()
        if not line:
            isDone = 1
        else:
            lineSplit = line.split(' ')
            lineSplit[-1] = lineSplit[-1][:-1]
            Data[dataCnt] = lineSplit
            dataCnt += 1
    fileData.close()
    return Data

def main():
    print 'do main'
    testch = InputData('test.ch.txt')
    testen = InputData('test.en.txt')
    testalign = InputData('test.align.txt')
    lengthCH = len(testch)
    lengthEN = len(testen)
    lengthALIGN = len(testalign)
    if lengthCH != lengthEN or lengthCH != lengthALIGN or lengthEN != lengthALIGN:
        print 'data size error!'
    output = TranslationRuleExtr(testch, testen, testalign)
    outputFile = open('output.txt', 'w')
    outputFile.write(output)
    outputFile.close()

if __name__ == '__main__':
    start = time.clock()
    main()
    end = time.clock()
    print 'elapsed time is'
    print end - start
