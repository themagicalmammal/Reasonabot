import re

def urlify(s):
    s = re.sub(r"\s+", '%20', s)

    return s

kam = input()
sam = str(kam)
nam = urlify(sam)
s ="#s="
msp = "https://www.mysmartprice.com/msp/search/search.php?search_type=full&typed_term=&s="
dip = msp+nam+s+nam
print(dip)