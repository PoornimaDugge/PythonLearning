
def translator(phrase):
    translation=""
    for letter in phrase:
        if letter in ('aeiouAEIOU'):
            translation=translation + 'g'
        else:
            translation= translation +letter
    return translation


print(translator(input("Enter the phrase")))
