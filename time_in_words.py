h = int(input())
m = int(input())


def timeInWords(h, m):
    d = {'1': 'one',
         '2': 'two',
         '3': 'three',
         '4': 'four',
         '5': 'five',
         '6': 'six',
         '7': 'seven',
         '8': 'eight',
         '9': 'nine',
         '10': 'ten',
         '11': 'eleven',
         '12': 'twelve',
         '13': 'thirteen',
         '14': 'fourteen',
         '15': 'fifteen',
         '16': 'sixteen',
         '17': 'seventeen',
         '18': 'eighteen',
         '19': 'nineteen',
         '20': 'twenty',
         '21': 'twenty one',
         '22': 'twenty two',
         '23': 'twenty three',
         '24': 'twenty four',
         '25': 'twenty five',
         '26': 'twenty six',
         '27': 'twenty seven',
         '28': 'twenty eight',
         '29': 'twenty nine'
         }
    if m == 0:
        return (d[str(h)]+" o' clock")
    if m == 1:
        return (d[str(m)]+" minute past "+d[str(h)])
    if m > 1 and m < 30 and m != 15:
        return (d[str(m)]+" minutes past "+d[str(h)])
    if m == 15:
        return ("quarter past "+d[str(h)])
    if m == 30:
        return ('half past '+d[str(h)])
    if m > 30 and m != 45:
        return (d[str(60-m)]+' minutes to '+d[str(h+1)])
    if m == 45:
        return ('quarter to '+d[str(h+1)])


print(timeInWords(h, m))
