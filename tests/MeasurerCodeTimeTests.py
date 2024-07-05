import unittest
import io
import time
from contextlib import redirect_stdout
from MeasurerCodeTime import MeasurerCodeTime


class MeasurerCodeTimeTests(unittest.TestCase):

    def test_without_code(self):
        expected_value = 0.0
        executed_value_stream = io.StringIO()

        with redirect_stdout(executed_value_stream):
            with MeasurerCodeTime():
                pass

        calculated_value = float(executed_value_stream.getvalue().split(" ")[2])
        self.assertEqual(expected_value, calculated_value)


    def test_sleep1(self):
        expected_value_min = 1000.0
        expected_value_max = 1002.0
        executed_value_stream = io.StringIO()

        with redirect_stdout(executed_value_stream):
            with MeasurerCodeTime():
                time.sleep(1)

        calculated_value= float(executed_value_stream.getvalue().split(" ")[2])
        calculated_value = round(calculated_value, 2)

        self.assertLess(calculated_value, expected_value_max)
        self.assertGreater(calculated_value, expected_value_min)


if __name__ == '__main__':
    unittest.main()
