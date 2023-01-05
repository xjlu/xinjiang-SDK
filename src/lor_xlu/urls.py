ENDPOINT = "https://the-one-api.dev/v2"

class URLs:
    @staticmethod
    def movie_list_url():
        return ENDPOINT + '/movie'

    @staticmethod
    def movie_url(id):
        return ENDPOINT + '/movie/{}'.format(id)

    @staticmethod
    def movie_quote_url(id):
        return ENDPOINT + '/movie/{}/quote'.format(id)
