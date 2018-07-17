## smallurl
A small Django url shortening API project using GraphQL.

This project assumes that you have `virtualenv` and `virtualenvwrapper` installed.

### Setup
1. `mkvirtualenv -p python3 smallurl` *NOTE: You will need python3 for this. Also the -p python3 command may vary with your OS*
2. While in your env: `pip install -r requirements.txt`
3. `pip freeze` will show the project dependencies

### Using the GraphQL API
To run the project: `python manage.py runserver` *NOTE: This project assumes that you are using the Django default localhost of 127.0.0.1:8000*.


The GraphQL API is available at `BASE_URL/graphql/`. A an example mutation command:
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
If the response is `ok`, the short URL will redirect to the given long URL.


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