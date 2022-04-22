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
        outputline = "";
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
                        if line[index].lower() == 'n':
                            outputline = 'ん' + outputline
                            index -= 1
                        else:
                            outputline = 'っ' + outputline
                            index -= 1
        outputfile.write(outputline)


hiraganaDict = {
    'a': 'あ',
    'i': 'い',
    'u': 'う',
    'e': 'え',
    'o': 'お',
    'ka': 'か',
    'ki': 'き',
    'ku': 'く',
    'ke': 'け',
    'ko': 'こ',
    'sa': 'さ',
    'shi': 'し',
    'su': 'す',
    'se': 'せ',
    'so': 'そ',
    'ta': 'た',
    'chi': 'ち',
    'tsu': 'つ',
    'te': 'て',
    'to': 'と',
    'ma': 'ま',
    'mi': 'み',
    'mu': 'む',
    'me': 'め',
    'mo': 'も',
    'ra': 'ら',
    'ri': 'り',
    'ru': 'る',
    're': 'れ',
    'ro': 'ろ',
    'ha': 'は',
    'hi': 'ひ',
    'fu': 'ふ',
    'he': 'へ',
    'ho': 'ほ',
    'na': 'な',
    'ni': 'に',
    'nu': 'ぬ',
    'ne': 'ね',
    'no': 'の',
    'ya': 'や',
    'yu': 'ゆ',
    'yo': 'よ',
    'wa': 'わ',
    'wo/o': 'を',
    'n': 'ん',
    'ga': 'が',
    'gi': 'ぎ',
    'gu': 'ぐ',
    'ge': 'げ',
    'go': 'ご',
    'za': 'ざ',
    'ji': 'じ',
    'zu': 'ず',
    'ze': 'ぜ',
    'zo': 'ぞ',
    'da': 'だ',
    'dzi': 'ぢ',
    'dzu': 'づ',
    'de': 'で',
    'do': 'ど',
    'ba': 'ば',
    'bi': 'び',
    'bu': 'ぶ',
    'be': 'べ',
    'bo': 'ぼ',
    'pa': 'ぱ',
    'pi': 'ぴ',
    'pu': 'ぷ',
    'pe': 'ぺ',
    'po': 'ぽ',
    'kya': 'きゃ',
    'kyu': 'きゅ',
    'kyo': 'きょ',
    'sha': 'しゃ',
    'shu': 'しゅ',
    'sho': 'しょ',
    'cha': 'ちゃ',
    'chu': 'ちゅ',
    'cho': 'ちょ',
    'nya': 'にゃ',
    'nyu': 'にゅ',
    'nyo': 'にょ',
    'hya': 'ひゃ',
    'hyu': 'ひゅ',
    'hyo': 'ひょ',
    'mya': 'みゃ',
    'myu': 'みゅ',
    'myo': 'みょ',
    'rya': 'りゃ',
    'ryu': 'りゅ',
    'ryo': 'りょ',
    'gya': 'ぎゃ',
    'gyu': 'ぎゅ',
    'gyo': 'ぎょ',
    'ja': 'じゃ',
    'ju': 'じゅ',
    'jo': 'じょ',
    'bya': 'びゃ',
    'byu': 'びゅ',
    'byo': 'びょ',
    'pya': 'ぴゃ',
    'pyu': 'ぴゅ',
    'pyo': 'ぴょ'
}
