This SDK is designed to be a simple wrapper for the LoR API without overabstraction.

The lightweight abstration is only for the url generation, which is decoupled from the business logic handling api call and data handling.

Some further abstration can be done regarding the authenticaiton module if it's more complex than the current requirement. For example, one common way for separation of concerns between api, common, and core functionality, where api handles network communication, common is for shared stuff such as URLs, constants, etc, and core functioality deals with the business logic mapping.

Depending on how the API is typically assumed, a common and popular abstraction is mapping RESTful resources to objects such as Movie. Particularly for access patterns such as ORM. For example:
```
>>> movie = client.get_movie({movie_id})
>>> quotes = movie.quotes()
```

The design is mainly motivated by the main use cases, and it comes with typical trade-off. For example, in many use cases, the data is consumed and manipulated, then pass it down to another service. the ORM approach doesn't add much value in many of these scenarios.
