# Напишите функцию , которая будет возвращать переданное в качестве параметра n число словами

# Input -> 435467
# Output -> четыреста тридцать пять тысяч четыреста шестьдесят семь

 

def intToString(num: int, option: str = ''):   # Преобразовывает целое число до 999999 в число прописью
    res = ''
    one_nineteen = {'0': '',
                    '00': '',
                    '01': 'один',
                    '02': 'два',
                    '03': 'три',
                    '04': 'четыре',
                    '05': 'пять',
                    '06': 'шесть',
                    '07': 'семь',
                    '08': 'восемь',
                    '09': 'девять',
                    '10': 'десять',
                    '11': 'одиннадцать',
                    '12': 'двенадцать',
                    '13': 'тринадцать',
                    '14': 'четырнадцать',
                    '15': 'пятнадцать',
                    '16': 'шестнадцать',
                    '17': 'семнадцать',
                    '18': 'восемнадцать',
                    '19': 'девятнадцать',
                    }
    twenty_ninety = {'2': 'двадцать',
                     '3': 'тридцать',
                     '4': 'сорок',
                     '5': 'пятьдесят',
                     '6': 'шестьдесят',
                     '7': 'семьдесят',
                     '8': 'восемьдесят',
                     '9': 'девяносто',
                     }
    hundreds = {'0': '',
                '1': 'сто',
                '2': 'двести',
                '3': 'триста',
                '4': 'четыреста',
                '5': 'пятьсот',
                '6': 'шестьсот',
                '7': 'семьсот',
                '8': 'восемьсот',
                '9': 'девятьсот',
                }
    thousands = {'0': '',
                 '00': 'тысяч',
                 '01': 'одна тысяча',
                 '02': 'две тысячи',
                 '03': 'три тысячи',
                 '04': 'четыре тысячи',
                 '05': 'пять тысяч',
                 '06': 'шесть тысяч',
                 '07': 'семь тысяч',
                 '08': 'восемь тысяч',
                 '09': 'девять тысяч',
                 '10': 'десять тысяч',
                 '11': 'одиннадцать тысяч',
                 '12': 'двенадцать тысяч',
                 '13': 'тринадцать тысяч',
                 '14': 'четырнадцать тысяч',
                 '15': 'пятнадцать тысяч',
                 '16': 'шестнадцать тысяч',
                 '17': 'семнадцать тысяч',
                 '18': 'восемнадцать тысяч',
                 '19': 'девятнадцать тысяч',
                 }
    s = str(num)
    r = s[::-1]
    if len(r) > 3:
        t = r[3:6]
        t = t[::-1]
        res = intToString(int(t), 'thousands')
    digit = 0  # разряд
    for i in r:
        digit += 1
        if digit == 1:
            one = i
            if option == 'thousands':
                result = thousands['0'+i]
            else:
                result = one_nineteen['0'+i]
        elif digit == 2:
            if option == 'thousands':
                if int(i) > 1:
                    result = twenty_ninety[i] + ' ' + result
                elif int(i) <= 1:
                    result = thousands[i+one]
            else:
                if int(i) > 1:
                    result = twenty_ninety[i] + ' ' + result
                elif int(i) <= 1:
                    result = one_nineteen[i+one]
        elif digit == 3:
            if int(i) > 0:
                result = hundreds[i] + ' ' + result
    if res:
        res = res.capitalize()
        return(res+' '+result)
    else:
        result = result.capitalize()
        return(result)
if __name__ == '__main__':
    a = int(input("Введите число - "))
    print(intToString(a))

    # # -*- coding: utf-8 -*-
# '''
# Created on 13.03.2016 by Artem Tiumentcev
# @author: Sergey Prokhorov <me@seriyps.ru>
# '''
# import unittest

# from num2t4ru import num2text, decimal2text


# class TestStrToText(unittest.TestCase):

#     def test_units(self):
#         self.assertEqual(num2text(0), u'ноль')
#         self.assertEqual(num2text(1), u'один')
#         self.assertEqual(num2text(9), u'девять')

#     def test_gender(self):
#         self.assertEqual(num2text(1000), u'одна тысяча')
#         self.assertEqual(num2text(2000), u'две тысячи')
#         self.assertEqual(num2text(1000000), u'один миллион')
#         self.assertEqual(num2text(2000000), u'два миллиона')

#     def test_teens(self):
#         self.assertEqual(num2text(10), u'десять')
#         self.assertEqual(num2text(11), u'одиннадцать')
#         self.assertEqual(num2text(19), u'девятнадцать')

#     def test_tens(self):
#         self.assertEqual(num2text(20), u'двадцать')
#         self.assertEqual(num2text(90), u'девяносто')

#     def test_hundreeds(self):
#         self.assertEqual(num2text(100), u'сто')
#         self.assertEqual(num2text(900), u'девятьсот')

#     def test_orders(self):
#         self.assertEqual(num2text(1000), u'одна тысяча')
#         self.assertEqual(num2text(2000), u'две тысячи')
#         self.assertEqual(num2text(5000), u'пять тысяч')
#         self.assertEqual(num2text(1000000), u'один миллион')
#         self.assertEqual(num2text(2000000), u'два миллиона')
#         self.assertEqual(num2text(5000000), u'пять миллионов')
#         self.assertEqual(num2text(1000000000), u'один миллиард')
#         self.assertEqual(num2text(2000000000), u'два миллиарда')
#         self.assertEqual(num2text(5000000000), u'пять миллиардов')

#     def test_inter_oreders(self):
#         self.assertEqual(num2text(1100), u'одна тысяча сто')
#         self.assertEqual(num2text(2001), u'две тысячи один')
#         self.assertEqual(num2text(5011), u'пять тысяч одиннадцать')
#         self.assertEqual(num2text(1002000), u'один миллион две тысячи')
#         self.assertEqual(num2text(2020000), u'два миллиона двадцать тысяч')
#         self.assertEqual(num2text(5300600), u'пять миллионов триста тысяч шестьсот')
#         self.assertEqual(num2text(1002000000), u'один миллиард два миллиона')
#         self.assertEqual(num2text(2030000000), u'два миллиарда тридцать миллионов')
#         self.assertEqual(num2text(1234567891),
#                          u'один миллиард двести тридцать четыре миллиона '
#                          u'пятьсот шестьдесят семь тысяч '
#                          u'восемьсот девяносто один')

#     def test_main_units(self):
#         male_units = ((u'рубль', u'рубля', u'рублей'), 'm')
#         female_units = ((u'копейка', u'копейки', u'копеек'), 'f')
#         self.assertEqual(num2text(101, male_units), u'сто один рубль')
#         self.assertEqual(num2text(102, male_units), u'сто два рубля')
#         self.assertEqual(num2text(105, male_units), u'сто пять рублей')

#         self.assertEqual(num2text(101, female_units), u'сто одна копейка')
#         self.assertEqual(num2text(102, female_units), u'сто две копейки')
#         self.assertEqual(num2text(105, female_units), u'сто пять копеек')

#         self.assertEqual(num2text(0, male_units), u'ноль рублей')
#         self.assertEqual(num2text(0, female_units), u'ноль копеек')

#         self.assertEqual(num2text(3000, male_units), u'три тысячи рублей')

#     def test_decimal2text(self):
#         int_units = ((u'рубль', u'рубля', u'рублей'), 'm')
#         exp_units = ((u'копейка', u'копейки', u'копеек'), 'f')
#         self.assertEqual(
#             decimal2text(
#                 '105.245',
#                 int_units=int_units,
#                 exp_units=exp_units),
#             u'сто пять рублей двадцать четыре копейки')
#         self.assertEqual(
#             decimal2text(
#                 '101.26',
#                 int_units=int_units,
#                 exp_units=exp_units),
#             u'сто один рубль двадцать шесть копеек')
#         self.assertEqual(
#             decimal2text(
#                 '102.2450',
#                 places=4,
#                 int_units=int_units,
#                 exp_units=exp_units),
#             u'сто два рубля две тысячи четыреста пятьдесят копеек')  # xD
#         self.assertEqual(
#             decimal2text(
#                 '111',
#                 int_units=int_units,
#                 exp_units=exp_units),
#             u'сто одиннадцать рублей ноль копеек')
#         self.assertEqual(
#             decimal2text(
#                 '3000.00',
#                 int_units=int_units,
#                 exp_units=exp_units),
#             u'три тысячи рублей ноль копеек')

#     def test_negative(self):
#         self.assertEqual(num2text(-12345),
#                          u"минус двенадцать тысяч триста сорок пять")
#         self.assertEqual(
#             decimal2text('-123.45'),
#             u'минус сто двадцать три сорок пять')

# if __name__ == '__main__':
#     import sys
#     if len(sys.argv) > 1:
#         try:
#             num = sys.argv[1]
#             if '.' in num:
#                 print(decimal2text(
#                     num,
#                     int_units=((u'штука', u'штуки', u'штук'), 'f'),
#                     exp_units=((u'кусок', u'куска', u'кусков'), 'm')))
#             else:
#                 print(num2text(
#                     int(num),
#                     main_units=((u'штука', u'штуки', u'штук'), 'f')))
#         except ValueError:
#             print (sys.stderr, "Invalid argument {}".format(sys.argv[1]))
#         sys.exit()
#     unittest.main()