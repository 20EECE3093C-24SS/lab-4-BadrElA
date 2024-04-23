import pytest
from course_grader import convert_to_letter_grade


# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_boundaries():
    assert convert_to_letter_grade(0) == 'F', "Score at 0 should be F"
    assert convert_to_letter_grade(59) == 'F', "Score at 59 should be F"
    assert convert_to_letter_grade(60) == 'D', "Score at 60 should be D"
    assert convert_to_letter_grade(69) == 'D', "Score at 69 should be D"
    assert convert_to_letter_grade(70) == 'C', "Score at 70 should be C"
    assert convert_to_letter_grade(79) == 'C', "Score at 79 should be C"
    assert convert_to_letter_grade(80) == 'B', "Score at 80 should be B"
    assert convert_to_letter_grade(89) == 'B', "Score at 89 should be B"
    assert convert_to_letter_grade(90) == 'A', "Score at 90 should be A"
    assert convert_to_letter_grade(100) == 'A', "Score at 100 should be A"


# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    with pytest.raises(ValueError) as e:
        convert_to_letter_grade(-1)
    assert str(e.value) == "Score must be between 0 and 100."
    
    with pytest.raises(ValueError) as e:
        convert_to_letter_grade(101)
    assert str(e.value) == "Score must be between 0 and 100."

# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_type():
    with pytest.raises(TypeError) as e:
        convert_to_letter_grade("eighty")
    assert str(e.value) == "Score must be a numeric value. (String input)"
    
    with pytest.raises(TypeError) as e:
        convert_to_letter_grade([90])
    assert str(e.value) == "Score must be a numeric value. (List input)"
    
    with pytest.raises(TypeError) as e:
        convert_to_letter_grade(None)
    assert str(e.value) == "Score must be a numeric value. (None Input)"