import unittest
# import subprocess
import shell_seq


class ShellCheck(unittest.TestCase):

    def setUp(self) -> None:
        self.data_0 = None
        self.data_1 = []
        self.data_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        self.data_3 = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        self.data_4 = ['Hello', 'world']
        self.data_5 = ['@', '#', '$', '^', '&']
        self.data_6 = [-1, -2, -3, -4, -5]

    def test_1(self):
        self.assertRaises(TypeError, shell_seq.shell_sort(self.data_0))

    def test_2(self):
        shell_seq.shell_sort(self.data_1)
        self.assertIsNotNone(self.data_1)

    def test_3(self):
        shell_seq.shell_sort(self.data_2)
        self.assertIsNotNone(self.data_2)

    def test_4(self):
        shell_seq.shell_sort(self.data_3)
        self.assertIsNotNone(self.data_3)

    def test_5(self):
        shell_seq.shell_sort(self.data_4)
        self.assertIsNotNone(self.data_4)

    def test_6(self):
        shell_seq.shell_sort(self.data_5)
        self.assertIsNotNone(self.data_5)

    def test_7(self):
        shell_seq.shell_sort(self.data_6)
        self.assertIsNotNone(self.data_6)

        # run = subprocess.Popen('python D:/RND/credit_robot-ru/tests/test_integration/shell_seq.py',
        #                        stdout=subprocess.PIPE, shell=True)
        # output = run.stdout.read()
        # print(output)
        # # self.assertIsNotNone(output)


if __name__ == "__main__":
    unittest.main()
