def pig_it(text):
    words = text.split(' ')
    result = []
    for word in words:
        result.append(word[1:]+f"{word[0]}"+"ay")
    return " ".join(result)


assert pig_it('Pig latin is cool') == 'igPay atinlay siay oolcay'