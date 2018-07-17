# smallurl
A Django URL shortening service with a simple GraphQL API.

This project assumes that you have `virtualenv` and `virtualenvwrapper` installed.

## Setup
1. `mkvirtualenv -p python3 smallurl` *NOTE: You will need python3 for this. Also the -p python3 command may vary with your OS*
2. While in your env: `pip install -r requirements.txt`

## Using the GraphQL API
To run the project: `python manage.py runserver` *NOTE: This project assumes that you are using the Django default localhost of `127.0.0.1:8000`. If you are using a different base URL, consider changing `BASE_URL` in the settings.py file.*.


The GraphQL API is available at `BASE_URL/graphql/`. Example mutation command:
```
mutation {
  createUrl(long: "https://www.youtube.com") {
    url {
      long
      short
    }
    ok
  }
}
```
If the response is `ok`, the response string in `url.short` will redirect to the given long URL.


The API also allows for queries:
```
query {
  allUrls {
    long
    short
  }
}
```
and
```
query {
  url(long: "https://www.youtube.com") {
    long
    short
  }
}
```