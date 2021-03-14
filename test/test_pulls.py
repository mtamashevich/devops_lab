from unittest import TestCase
from handlers import pulls


class TestPrime(TestCase):

    def setUp(self):
        """Init"""

    def test_status(self):

        list1 = {
            'num': 15,
            'title': 'Homework1: Maksimelyan Tamashevich',
            'link': 'https://github.com/alenaPy/devops_lab/pull/15'
        }

        list2 = {
            'num': 1,
            'title': 'Test PR',
            'link': 'https://github.com/alenaPy/devops_lab/pull/1'
        }
        self.assertEqual(pulls.get_pulls('open').count(list1), 1)
        self.assertNotEqual(pulls.get_pulls('closed').count(list1), 1)
        self.assertEqual(pulls.get_pulls('closed').count(list2), 1)
        self.assertNotEqual(pulls.get_pulls('open').count(list2), 1)

    def test_labels(self):
        self.assertEqual(pulls.get_pulls('accepted')[0]['num'], 101)
        self.assertEqual(pulls.get_pulls('needs work')[0]['num'], 102)

    def tearDown(self):
        """Finish"""
