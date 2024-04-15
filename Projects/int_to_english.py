# Integer to English Words
# https://leetcode.com/problems/integer-to-english-words/

class Solution:
    def __init__(self):
        self.singles = {
            1  : "One",
            2  : "Two",
            3  : "Three",
            4  : "Four",
            5  : "Five",
            6  : "Six",
            7  : "Seven",
            8  : "Eight",
            9  : "Nine",
            10 : "Ten",
            11 : "Eleven",
            12 : "Twelve",
            13 : "Thirteen",
            14 : "Fourteen",
            15 : "Fifteen",
            16 : "Sixteen",
            17 : "Seventeen",
            18 : "Eighteen",
            19 : "Nineteen",
            20 : "Twenty",
            30 : "Thirty",
            40 : "Forty",
            50 : "Fifty",
            60 : "Sixty",
            70 : "Seventy",
            80 : "Eighty",
            90 : "Ninety"
        }

        self.billion = 1000000000
        self.million = 1000000
        self.thousand = 1000
        self.hundred = 100
        self.tens = 10



    def processTriple(self, num: int) -> str:
        result = []
        remainder = 0

        if num >= self.hundred:
            result.append(self.singles[num // self.hundred] + ' Hundred')
            num = num % self.hundred

        if num >= self.tens:
            if num in self.singles.keys():
                result.append(self.singles[num])
                num -= num
            else:
                result.append(self.singles[num // self.tens * self.tens])
                num = num % self.tens

        if num > 0:
            result.append(self.singles[num])

        return ' '.join(result)
        '''
        if num in self.singles.keys():
            return self.singles[num]

        if num > 99:
            result = result + f'{self.singles[num // 100]} Hundred'

        remainder = num % 100

        if remainder > 0:
            if remainder in self.singles:
                addSpace = ' ' if len(result) else ''
                result = result + addSpace + self.singles[remainder]
            else:
                tens = self.singles[(remainder // 10) * 10]
                ones = self.singles[remainder % 10]
                if tens != 'Zero':
                    addSpace = ' ' if len(result) else ''
                    result = result + addSpace + tens
                if ones != 'Zero':
                    addSpace = ' ' if len(result) else ''
                    result = result + addSpace + ones

        return result
        '''

    def numberToWords(self, num: int) -> str:
        print(f'Value provided: {num}')

        if num == 0:
            return 'Zero'

        output = []

        if num >= self.billion:
            output.append(self.processTriple(num // self.billion) + ' Billion')
            num = num % self.billion

        if num >= self.million:
            output.append(self.processTriple(num // self.million) + ' Million')
            num = num % self.million

        if num >= self.thousand:
            output.append(self.processTriple(num // self.thousand) + ' Thousand')
            num = num % self.thousand

        if num > 0:
            output.append(self.processTriple(int(num)))

        return ' '.join(output)

        # self.places = {
        #     0  : "",
        #     1  : "Thousand",
        #     2  : "Million",
        #     3  : "Billion",
        #     4  : "Trillion",
        #     5  : "Quadrillion",
        #     6  : "Quintillion",
        #     7  : "Sextillion",
        #     8  : "Septillion",
        #     9  : "Octillion",
        #     10 : "Nonillion",
        #     11 : "Decillion",
        #     12 : "Undecillion",
        #     13 : "Duodecillion",
        #     14 : "Tredecillion",
        #     15 : "Quattuordecillion",
        #     16 : "Quindecillion",
        #     17 : "Sexdecillion",
        #     18 : "Septendecillion",
        #     19 : "Octodecillion",
        #     20 : "Novemdecillion",
        #     21 : "Vigintillion",
        #     22 : "Unvigintillion",
        #     23 : "Duovigintillion",
        #     24 : "Trevigintillion",
        #     25 : "Quattuorvigintillion",
        #     26 : "Quinvigintillion",
        #     27 : "Sexvigintillion",
        #     28 : "Septenvigintillion",
        #     29 : "Octovigintillion",
        #     30 : "Nonvigintillion",
        #     31 : "Trigintillion",
        #     32 : "Untrigintillion",
        #     33 : "Duotrigintillion",
        #     34 : "Ten-duotrigintillion",
        #     35 : "Skewer's Number",
        #     36 : "Centillion",
        #     37 : "Googolplex"
        # }

        # print(f'Value provided: {num}')

        # if num == 0:
        #     return 'Zero'

        # output = []

        # num = str(num)

        # triples = []

        # counter = 0
        # triple = ""
        # for x, v in enumerate(reversed(num)):
        #     counter += 1
        #     triple = v + triple

        #     if counter > 2 or x == len(num) - 1:
        #         counter = 0
        #         triples.insert(0, int(triple))
        #         triple = ""
        #         continue

        # for t, v in enumerate(triples):
        #     pos = (len(triples) - 1) - t
        #     group = self.processTriple(v)

        #     if group and group != 'Zero':
        #         output.append(group)

        #         thousands = self.places[pos]
        #         if thousands:
        #             output.append(f'{thousands}')

        # return ' '.join(output)

a = Solution()
print(a.numberToWords(1000))
