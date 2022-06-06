def decode(roman):
    roman_dict = {
      "M": 1000,
      "D": 500,
      "C": 100,
      "L": 50,
      "X": 10,
      "V": 5,
      "I": 1
    }
    
    if len(roman) == 1:
      return roman_dict[roman[0]]
    
    digit = 0
    i = 0
    j = 1
    # fast and slow pointer algorithm
    while i < j and j <= len(roman)-1:
      if roman_dict[roman[i]] < roman_dict[roman[j]]:
          digit += (roman_dict[roman[j]] - roman_dict[roman[i]])
          i = j + 1
          j += 2
      elif roman_dict[roman[i]] == roman_dict[roman[j]]:
          digit += (roman_dict[roman[j]] + roman_dict[roman[i]])
          if len(roman) == 3:
            digit += (roman_dict[roman[j+1]])
            break
          i = j + 1
          j += 2
      else:
          digit += roman_dict[roman[i]]
          i += 1
          j += 1
    return digit
  
  
  
  
  
  
