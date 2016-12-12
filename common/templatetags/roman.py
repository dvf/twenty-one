# Credit to Gilgamesh for this sweet script:
# http://stackoverflow.com/questions/28777219/basic-python-program-to-convert-integer-to-roman-numerals
from collections import OrderedDict

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
def write_roman(num):
    num = num + 1

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return mark_safe("".join([a for a in roman_num(num)]))