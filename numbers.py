# Write a function that converts letter numbers into difital numbers

def word_to_number(string_num):
    numbers = {
      "one": 1,
      "two": 2,
      "three": 3,
      "four": 4,
      "five": 5,
      "six": 6,
      "seven": 7,
      "eight": 8,
      "nine": 9,
      "ten": 10,
      "eleven": 11,
      "twelve": 12,
      "thirteen": 13,
      "fourteen": 14,
      "fifteen": 15,
      "sixteen": 16,
      "seventeen": 17,
      "eighteen": 18,
      "nineteen": 19,
      "twenty": 20,
      "thirty": 30,
      "fourty": 40,
      "fifty": 50,
      "sixty": 60,
      "seventy": 70,
      "eighty" : 80,
      "ninety": 90
    }
    # Dividing string
    millions = None
    thousands = None
    hundreds = None
    tens = None
    nothing = 'nothing'
    if 'million' in string_num:
        millions_pos = string_num.find('million')
        millions_end = string_num.find(' ',millions_pos)
        millions = string_num[:millions_end]
        string_num_new = string_num[millions_end+1:]
        if millions_end < 0:
            string_num_new = nothing #if there is only millions, ignore the rest of the code
    else:
        millions_pos = 0
        string_num_new = string_num
    if 'thousand' in string_num_new:
        thousands_pos = string_num_new.find('thousand')
        thousands_end = string_num_new.find(' ',thousands_pos)
        thousands = string_num_new[:thousands_end]
        string_num_new = string_num_new[thousands_end+1:]
        if thousands_end < 0:
            string_num_new = nothing
    else:
        thousands_pos = 0
    if 'hundred' in string_num_new:
        hundreds_pos = string_num_new.find('hundred')
        hundreds_end = string_num_new.find(' ',hundreds_pos)
        if hundreds_end < 0:
            hundreds = string_num_new
            tens = None
        else:
            hundreds = string_num_new[:hundreds_end]
            print hundreds_end
            tens = string_num_new[hundreds_end+1:]
    else:
        tens = string_num_new
    res = 0
    mil = 0
    thous = 0
    hund = 0
    ten = 0
# Converting words in each section to numbers
    if millions is not None:
        millions_list = millions.split()
#  case when we have 'hundred' in millions part
        if millions_list[1] == 'hundred':
            mil = mil + numbers[millions_list[0]]*100
            millions_list = millions_list[2:]
        for word in millions_list:
            if word in numbers.keys():
                mil = mil + numbers[word]
        mil = mil * 1000000
        print 'millions= ', mil
    else:
        millions = 0
#  case when we have 'hundred' in thousands part
    if thousands is not None:
        thousands_list = thousands.split()
        if thousands_list[1] == 'hundred':
            thous = thous + numbers[thousands_list[0]]*100
            thousands_list = thousands_list[2:]
        for word in thousands_list:
            if word in numbers.keys():
                thous = thous + numbers[word]
        thous = thous * 1000
        print 'thousands= ', thous
    else:
        thousands = 0
    if hundreds is not None:
        hundreds_list = hundreds.split()
        for word in hundreds_list:
            if word in numbers.keys():
                hund = hund + numbers[word]
        hund = hund * 100
        print 'hundreds= ', hund
    else:
        hundreds = 0
    if tens is not None:
        tens_list = tens.split()
        for word in tens_list:
            if word in numbers.keys():
                ten = ten + numbers[word]
        print 'tens= ', ten
    else:
        tens = 0
    res = mil + thous + hund + ten
    if string_num == 'zero':
        print 'The number <'+string_num+'> is', 0
    else:
        print 'The number <'+string_num+'> is', res
# end of function -------------------------------------------------------------
word_to_number("one hundred thirty five million two hundred eighty nine thousand three hundred sixty five")