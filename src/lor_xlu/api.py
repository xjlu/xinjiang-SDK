import requests
from .urls import URLs

class Client:
    def __init__(self, access_key):
        self._access_key = access_key
        self._headers = {
            "Authorization": "Bearer " + self._access_key
        }

    @property
    def access_key(self):
        return self._access_key


    # this end point returns 500, rather than the standard 404, 
    # thus impossible to differentiate "not found" from "server side error"
    # the result seems to be a simple filtered collection from a mongodb style query; here it's mapped
    # to a more RESTful style single resource 
    def get_movie(self, id):
        """Return a specific movie's information

            >>> client.get_movie('5cd95395de30eff6ebccde56')
            >>> {'_id': '5cd95395de30eff6ebccde56', 'name': 'The Lord of the Rings Series', 'runtimeInMinutes': 558, 'budgetInMillions': 281, 'boxOfficeRevenueInMillions': 2917, 'academyAwardNominations': 30, 'academyAwardWins': 17, 'rottenTomatoesScore': 94}
        """
        try:
            res = requests.get(URLs.movie_url(id), headers=self._headers)
            res.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(e, file=sys.stderr)
            print("Please ensure that a valid access key is provided")
        except requests.exceptions.RequestException as e:
            print(e, file=sys.stderr)

        data = res.json()['docs'][0]
        return data
