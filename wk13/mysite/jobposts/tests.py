from unittest import TestCase

from .models import JobPost


class TestJobPosts(TestCase):

    @classmethod
    def setUpClass(cls):
        for i in xrange(100):
            JobPost.objects.create(
                title='Yo',
                years_experience=i
            )

    def setUp(self):
        self.jp = JobPost.objects.create(
            title='Yo',
            years_experience=1,
        )

    # def tearDown(self):
    #     JobPost.objects.all().delete()

    def test_increase_experience(self):
        self.assertEqual(self.jp.years_experience, 1)
        self.jp.increase_experience(5)
        self.assertEqual(self.jp.years_experience, 6)