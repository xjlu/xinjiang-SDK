from unittest import TestCase

from lor_xlu import urls

class UrlsTests(TestCase):
    """Tests for urls"""

    def test_movie_url(self):
        self.assertEqual(
            urls.URLs.movie_url('1234'), "https://the-one-api.dev/v2/movie/1234"
        )

    def test_movie_quote_url(self):
        self.assertEqual(
            urls.URLs.movie_quote_url('1234'), "https://the-one-api.dev/v2/movie/1234/quote"
        )
