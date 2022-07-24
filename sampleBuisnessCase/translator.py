# This program will define a function translator
# Function accepts a string and convert every vowels to letter 'g'
# for example :  dog = dgg and cat = cgt

def translator(input):
    result = ""
    for letter in input:
        if letter in "AEIOUaeiou":
            letter = 'g'
        result += letter

    return result


statement = "The quick brown fox jump over a lazy frog"
print("------------Actual statement --------")
print(statement)
print("------------After translation (replacing vowels with letter 'g'-----------")
print(translator(statement))