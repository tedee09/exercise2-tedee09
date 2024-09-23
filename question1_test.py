import numpy as np
import pytest
from question1 import get_DH_table


def test_dh_table():
    dh_table = get_DH_table()
    assert np.allclose(dh_table, np.load('dh_table.npz')['dh_table'])
    
if __name__ == "__main__":
    pytest.main()