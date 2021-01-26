from re import search

def arithmetic_arranger(problems: [str], results: bool = False) -> str:

    # Check for number of problems
    if len(problems) > 5: return "Error: Too many problems."

    line1, line2, line3, line4 = '', '', '', ''

    counter = 1
    
    for index, problem in enumerate(problems):

        # ------------------------------------------------
        # Split the string into a list 

        p = problem.split()

        # ------------------------------------------------
        # Error check based on the problem description

        if search('[^+-]', p[1]):
            return "Error: Operator must be '+' or '-'."

        if search('[^\d*]', p[0]) or search('[^\d*]', p[2]):
            return "Error: Numbers must only contain digits."

        if len(p[0]) > 4 or len(p[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        # ------------------------------------------------
        # Piecing it together

        emptySpace = len(max(p[0], p[2], key=len))

        line1 += ' ' + (' ' *  (emptySpace - len(p[0]) + 1 ) + p[0]) + '    '
        line2 += p[1] + (' ' *  (emptySpace - len(p[2]) + 1 ) + p[2]) + '    '
        line3 += ('-' * (emptySpace + 2)) + '    '
        
        if results:
            result = int(p[0]) + int(p[2]) if p[1] == '+' else int(p[0]) - int(p[2])
            fillerSpace = emptySpace - len(str(result)) + 2
            line4 += ' ' * fillerSpace + str(result) + '    '

    # --------------------
    # Remove last 4 spaces
    line1, line2, line3, line4 = line1[:-4], line2[:-4], line3[:-4], line4[:-4]

    # Concatenate results in single string
    arranged_problems = f"{line1}\n{line2}\n{line3}"

    if results:
        arranged_problems += f"\n{line4}"

    return arranged_problems



# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
# print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))

# print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))
print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"], True))



