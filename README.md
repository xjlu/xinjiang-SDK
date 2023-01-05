# The Lord of Rings API

This is a simple SDK to help explore https://the-one-api.dev/.


# Getting Started

To get started, install the library with pip:

`pip install lor-xlu`

Example of usage:

```
>>> from lor_xlu import api
>>> client = api.Client(YOUR_ACCESS_KEY)
>>> c.get_movie("5cd95395de30eff6ebccde56")
{'_id': '5cd95395de30eff6ebccde56', 'name': 'The Lord of the Rings Series', 'runtimeInMinutes': 558, 'budgetInMillions': 281, 'boxOfficeRevenueInMillions': 2917, 'academyAwardNominations': 30, 'academyAwardWins': 17, 'rottenTomatoesScore': 94}
```
