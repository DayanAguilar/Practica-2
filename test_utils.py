import pytest
from utils import traduction_move

class TestUtils():

    def test_traduction_move_valid(self):
        assert(traduction_move("D1 SE"), (0, 3, 'SE'))

    def test_traduction_move_invalid_length(self):
        assert(traduction_move("D1SE"), "El movimiento debe contener una posición y una dirección (ej. 'D1 SE').")

   