def convert_to_letter_grade(score):
    """Converts a numerical grade to a corresponding letter grade.

    Args:
        score (int or float): Score from 0 to 100 to be converted to a letter grade.

    Returns:
        str: Letter grade corresponding to the numeric score.

    Raises:
        TypeError: If the input is not an int or float.
        ValueError: If the score is outside the 0 to 100 range.
    """
    
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


