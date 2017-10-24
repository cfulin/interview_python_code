#!/usr/bin/python
# -*- coding: utf-8 -*-


def analysis(inputList):
    num = 0
    temp = [inputList[0]]
    result = []
    while num < len(inputList):
        # first_index = num
        # temp.append(inputList[num])
        # if num != len(inputList) - 1:
        try:
            if inputList[num + 1] == inputList[num] + 1:
                temp.append(inputList[num + 1])
                num += 1
            else:
                result.append(temp)
                num += 1
                temp = [inputList[num]]
        except IndexError:
                result.append(temp)
                break
        # else:
        #     result.append(temp)
        #     break
    return result


def insert_number(outputList):
    for i in range(len(outputList)):
        outputList[i].insert(0, outputList[i][0] - 1)
        outputList[i].insert(0, outputList[i][0] - 1)
        outputList[i].append(outputList[i][len(outputList[i]) - 1] + 1)
        outputList[i].append(outputList[i][len(outputList[i]) - 1] + 1)
        outputList[i] = [i for i in outputList[i] if 0 <= i <= 400]
        # for j in range(len(result[i])):
        #     if result[i][j] < 0 | result[i][j] > 400:
        #         result[i].remove(j)
    return outputList


def main():
    inputList = [0, 3, 5, 6, 7, 9, 12, 13, 15, 16, 17, 19, 20, 21, 22, 25, 27, 29,
                 30, 32, 33, 36, 39, 40, 43, 44, 46, 47, 48, 53, 54, 57, 58, 60, 62,
                 64, 65, 66, 67, 72, 74, 75, 76, 77, 78, 80, 82, 84, 85, 86, 89, 95,
                 96, 97, 98, 103, 104, 107, 108, 110, 111, 114, 116, 117, 118, 120,
                 121, 122, 124, 127, 132, 135, 137, 138, 139, 140, 145, 146, 148, 149,
                 150, 151, 155, 156, 160, 161, 166, 167, 170, 171, 172, 175, 178,
                 179, 180, 181, 182, 183, 184, 186, 188, 189, 190, 193, 195, 196, 198,
                 202, 205, 208, 210, 211, 213, 214, 215, 217, 221, 226, 227, 228,
                 233, 234, 235, 240, 241, 246, 247, 249, 255, 257, 258, 261, 262, 263,
                 267, 268, 269, 270, 271, 272, 275, 278, 280, 282, 283, 284, 286,
                 287, 289, 291, 292, 295, 296, 298, 300, 302, 303, 304, 305, 306, 310,
                 315, 317, 319, 320, 321, 322, 323, 324, 325, 326, 328, 331, 336,
                 339, 341, 342, 344, 346, 349, 354, 355, 356, 362, 363, 365, 366, 367,
                 368, 371, 374, 376, 378, 382, 383, 388, 390, 393, 396, 399]

    result = analysis(inputList)
    outputList = insert_number(result)
    print(outputList)

if __name__ == '__main__':
    main()
