import codecs
# coding: utf8


def check_vowel(char):
    return char == 'a' or char == 'i' or char == 'u' or char == 'e' or char == 'o'


def can_convert(substr):
    return hiraganaDict.__contains__(substr)


def convert(substr):
    return hiraganaDict.get(substr)


class UnconvertedSubstringException(Exception):
    def __init__(self, substr):
        """Unexpected character sequence""" + substr


def convert_hiragana(inputfilearg):
    inputfile = codecs.open(inputfilearg, mode="r", encoding='utf-8')
    outputfile = codecs.open("conversion.txt", mode="w", encoding="utf-8")

    hiraganaconversion = False

    for line in inputfile:
        # Start from the end index, continue until we have processed index 0
        outputline = ""
        index = len(line) - 1
        while index >= 0:
            if not hiraganaconversion:
                if line[index - 1: index + 1] == "):":
                    hiraganaconversion = True
                    outputline = ']:' + outputline
                    index -= 2
                else:
                    outputline = line[index] + outputline
                    index -= 1
            else:
                if line[index].lower() == '(':
                    outputline = '[' + outputline
                    hiraganaconversion = False
                    index -= 1
                else:
                    # Check if the current character is a vowel
                    isvowel = check_vowel(line[index].lower())
                    if isvowel:
                        # First, prioritize 3 letter combinations
                        if can_convert(line[index - 2: index + 1]):
                            outputline = convert(line[index - 2: index + 1]) + outputline
                            index -= 3
                        # Then prioritize 2 letter combinations
                        elif can_convert(line[index - 1: index + 1]):
                            outputline = convert(line[index - 1: index + 1]) + outputline
                            index -= 2
                        # Then prioritize Single Chars
                        elif can_convert(line[index: index + 1]):
                            outputline = convert(line[index: index + 1]) + outputline
                            index -= 1
                        # Unexpected character sequence, except
                        else:
                            raise UnconvertedSubstringException(line[index - 2: index + 1])
                    else:
                        # TO:DO :: Both the 'n' and " o " special cases could be included as conversions in the dict
                        # This solution would require a new check vowel (?) function that would pick those scenarios up.
                        if line[index].lower() == 'n':
                            outputline = '???' + outputline
                            index -= 1
                        elif index >= 2 and line[index - 2: index + 1] == " o ":
                            outputline = '???' + outputline
                            index -= 3
                        else:
                            outputline = '???' + outputline
                            index -= 1
        outputfile.write(outputline)


hiraganaDict = {
    'a': '???',
    'i': '???',
    'u': '???',
    'e': '???',
    'o': '???',
    'ka': '???',
    'ki': '???',
    'ku': '???',
    'ke': '???',
    'ko': '???',
    'sa': '???',
    'shi': '???',
    'su': '???',
    'se': '???',
    'so': '???',
    'ta': '???',
    'chi': '???',
    'tsu': '???',
    'te': '???',
    'to': '???',
    'ma': '???',
    'mi': '???',
    'mu': '???',
    'me': '???',
    'mo': '???',
    'ra': '???',
    'ri': '???',
    'ru': '???',
    're': '???',
    'ro': '???',
    'ha': '???',
    'hi': '???',
    'fu': '???',
    'he': '???',
    'ho': '???',
    'na': '???',
    'ni': '???',
    'nu': '???',
    'ne': '???',
    'no': '???',
    'ya': '???',
    'yu': '???',
    'yo': '???',
    'wa': '???',
    'n': '???',
    'ga': '???',
    'gi': '???',
    'gu': '???',
    'ge': '???',
    'go': '???',
    'za': '???',
    'ji': '???',
    'zu': '???',
    'ze': '???',
    'zo': '???',
    'da': '???',
    'dzi': '???',
    'dzu': '???',
    'de': '???',
    'do': '???',
    'ba': '???',
    'bi': '???',
    'bu': '???',
    'be': '???',
    'bo': '???',
    'pa': '???',
    'pi': '???',
    'pu': '???',
    'pe': '???',
    'po': '???',
    'kya': '??????',
    'kyu': '??????',
    'kyo': '??????',
    'sha': '??????',
    'shu': '??????',
    'sho': '??????',
    'cha': '??????',
    'chu': '??????',
    'cho': '??????',
    'nya': '??????',
    'nyu': '??????',
    'nyo': '??????',
    'hya': '??????',
    'hyu': '??????',
    'hyo': '??????',
    'mya': '??????',
    'myu': '??????',
    'myo': '??????',
    'rya': '??????',
    'ryu': '??????',
    'ryo': '??????',
    'gya': '??????',
    'gyu': '??????',
    'gyo': '??????',
    'ja': '??????',
    'ju': '??????',
    'jo': '??????',
    'bya': '??????',
    'byu': '??????',
    'byo': '??????',
    'pya': '??????',
    'pyu': '??????',
    'pyo': '??????',
    'n???i': '??????'
}
