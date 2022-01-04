import unittest

def sum(a,b):
    return a + b

def setup(self):
    self.a = 10
    self.b = 20

class dont_test (unittest.TestCase):
    def test_dont_test1(self):
        #arange

        #act
        result = sum(self.a,self.b)
        #assert
        self.assertEqual(result, self.a + self.b)


class new_deck (unittest.TestCase):
    def test_new_deck(self):
        pass


class dont_test2 (unittest.TestCase):
    def test_dont_test2(self):
        pass



class new_deck2 (unittest.TestCase):
    def test_new_deck2(self):
        pass



class draw_card (unittest.TestCase):
    def test_draw_card(self):
        pass



class dont_test3 (unittest.TestCase):
    def test_dont_test3(self):
        pass



class return_card (unittest.TestCase):
    def test_return_card(self):
        pass


class dont_test4 (unittest.TestCase):
    def test_dont_test4(self):
        pass


class verify_card (unittest.TestCase):
    def test_verify_card(self):
        pass


class dont_test5 (unittest.TestCase):
    def test_dont_test5(self):
        pass


if __name__ == '__main__':
    unittest.main()
