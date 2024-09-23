import numpy as np
import pytest
from question2 import get_pos

def test_dh_table():
    student_pos = get_pos()

    assert np.allclose(student_pos, np.array([0.34082547, 0.34082547, 0.32]))
    
if __name__ == "__main__":
    pytest.main()