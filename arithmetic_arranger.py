def arithmetic_arranger(problems, show_result = False):

  if len(problems) > 5:
    return 'Error: Too many problems.'

  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  
  for p in problems:
    operator = p.split()[1]
    number1 = p.split()[0]
    number2 = p.split()[2]
    
    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."
    elif not number1.isdigit() or not number2.isdigit():
      return 'Error: Numbers must only contain digits.'
    elif len(str(number1)) > 4 or len(str(number2)) > 4:
      return 'Error: Numbers cannot be more than four digits.'
    else:
      longest = max(len(number1), len(number2))
      shortest = min(len(number1), len(number2))
      width = longest + 2

      line1 += f'{number1:>{width}}' + "    " 
      if len(number1) > len(number2):
        line2 += f'{operator}{" " * (width-shortest-1)}{number2}' + "    "    #number of spaces between operator and 2nd number if 1st number is longer than 2nd number
      elif len(number1) < len(number2):
        line2 += f'{operator}{" " * (width-longest-1)}{number2}' + "    "     #number of spaces between operator and 2nd number if 1st number is shorter than 2nd number
      else:
        line2 += f'{operator} {number2}' + "    "        #number of spaces between operator and 2nd number if numbers are same length
      line3 += f'{"-" * width}' + "    "
      all_lines = [line1.rstrip(), line2.rstrip(), line3.rstrip()]

      if show_result:                                    # only displayed if passed as arg
        if operator == '+':
          result = int(number1) + int(number2)
        else:
          result = int(number1) - int(number2)
          
        line4 += f'{result:>{width}}' + "    "
        all_lines = [line1.rstrip(), line2.rstrip(), line3.rstrip(), line4.rstrip()]
  
  arranged_problems = '\n'.join(all_lines)
    
  return arranged_problems