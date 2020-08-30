class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = (-2) ** 31
        INT_MAX = 2**31 - 1
        flag = False
        int_num = i= 0
        sign = ""
        dt = {"0": 0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

        if not str:
            return 0

        while i < len(str) and str[i] == ' ':
            i += 1
        print(i)
        if i == len(str):
            return 0

        if str[i] == "-":
            sign = '-'
            i += 1
        elif str[i] == "+":
            i += 1

        start = i
        while i < len(str) and str[i].isdigit():
            i += 1

        num = str[start:i]
        if sign:
            num = "-" + num
        print("num:", num)

        for digit in num:
            if digit == "-":
                flag = True
            else:
                int_num = int_num * 10 + dt[digit]

        if flag: 
            int_num = - int_num
        print("int_num:", int_num)
        if int_num < INT_MIN:
            return INT_MIN
        elif int_num > INT_MAX:
            return INT_MAX
        else:
            return int_num

