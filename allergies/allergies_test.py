import unittest

from allergies import New_Allergies


class AllergiesTests(unittest.TestCase):

    def test_no_allergies_means_not_allergic(self):
        allergies = New_Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_is_allergic_to_eggs(self):
        self.assertTrue(New_Allergies(1).is_allergic_to('eggs'))

    def test_has_the_right_allergies(self):
        allergies = New_Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_no_allergies_at_all(self):
        self.assertEqual([], New_Allergies(0).list)

    def test_allergic_to_just_peanuts(self):
        self.assertEqual(['peanuts'], New_Allergies(2).list)

    def test_allergic_to_everything(self):
        self.assertEqual(
            ('eggs peanuts shellfish strawberries tomatoes '
             'chocolate pollen cats').split(),
            New_Allergies(255).list)

    def test_ignore_non_allergen_score_parts(self):
        self.assertEqual(['eggs'], New_Allergies(257).list)


if __name__ == '__main__':
    unittest.main()
