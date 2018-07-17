from django.test import TestCase

from .base_62_converter import dehydrate, saturate
from .models import Url
from smallurl.settings import BASE_URL


class UrlTestCase(TestCase):
    def setUp(self):
        self.test_url = "https://httpstat.us/200"
        url = Url.objects.create(long=self.test_url)
        url.set_short()


    def test_dehydrate(self):
        """ID's should match alphabet"""
        self.assertEqual("a", dehydrate(0))
        self.assertEqual("z", dehydrate(25))
        self.assertEqual("A", dehydrate(26))
        self.assertEqual("Z", dehydrate(51))
        self.assertEqual("0", dehydrate(52))
        self.assertEqual("9", dehydrate(61))
        self.assertEqual("mS", dehydrate(788))


    def test_saturate(self):
        """Key's should match ID's"""
        self.assertEqual(0, saturate("a"))
        self.assertEqual(25, saturate("z"))
        self.assertEqual(26, saturate("A"))
        self.assertEqual(51, saturate("Z"))
        self.assertEqual(52, saturate("0"))
        self.assertEqual(61, saturate("9"))
        self.assertEqual(788, saturate("mS"))


    def test_shorten_url(self):
        """URL should be shortened"""
        url = Url.objects.get(long=self.test_url)
        self.assertEqual("{}{}".format(BASE_URL, dehydrate(url.id)), url.short)
