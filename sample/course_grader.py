# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.” for input scores outside the 0 to 100 range.")
    elif type(score) != int or type(score) != float:
        raise TypeError("Score must be a numeric value.")

    if score < 60: 
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    else:
        return "A"
    

    