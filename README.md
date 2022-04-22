# HiraganaConversion

This python library allows for conversion of romaji to hiragana with the set of vocabulary provided by Japanese Test 4 You.
It converts romaji between the "(" and "):" strings on each row using a defined dictionary of romaji -> hiragana conversions

Special scenarios:
  Romaji "n'i" converts to hiragana "んい"
  Romaji " o " converts to "を"

Future iterations & updates:
  Improve documentation on the romaji -> hiragana conversion dictionary
  Implement hiragana -> romaji
  Alter program to include easier usability -> user interface or command line arguments allowing the user to specify:
    1. Characters to indicate conversion boundaries?
