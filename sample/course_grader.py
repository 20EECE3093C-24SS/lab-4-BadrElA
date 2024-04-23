# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    """Converts number grade to letter grade

    Takes input of a grade number (int or float), between 0 and 100,
    and converts it the corresponding letter grade

    Args:
        score: int or float from 0 to 100

    Returns:
        Letter string corresponding to letter grade.
        For example:
            A: 90 to 100
            B: 80 to 89
            C: 70 to 79
            D: 60 to 69
            F: Below 60

        Return will always be a single, capital letter string.  If the
        input is not an int/float or if the value is no within bounds (<0 or >100),
        an error will be raised.

    Raises:
        TyperError: An error occurred due to inproper type (not an int or float).
        ValueError: An error occuered due to the entered number being outside the 0 to 100 range
    """
    
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
    

    