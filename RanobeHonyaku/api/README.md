### /api/v1/series ###

GET
~~~~
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 230
Server: Werkzeug/0.11.11 Python/3.5.2
Date: Sat, 24 Sep 2016 17:50:12 GMT

[
    {
        "id": 2,
        "title": "Ore no Imouto"
    },
    {
        "id": 4,
        "title": "This is the newest update!"
    },
    {
        "id": 5,
        "title": "Meepah womp womp womp!"
    }
]
~~~~

POST
```echo '{"title": "Rawwwwrr2r!"}' | curl -i -d @- http://localhost:5000/api/v1/series --header "Content-Type:application/json"````


### /api/v1/series/(series_id) ###

GET
~~~~
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 59
Server: Werkzeug/0.11.11 Python/3.5.2
Date: Sat, 24 Sep 2016 17:23:54 GMT

{
    "chapters": [],
    "id": 2,
    "title": "OreImo"
}
~~~~

PUT
```echo '{"title": "Edit this plz!"}' | curl -i -X PUT -d @- http://localhost:5000/api/v1/series/4 --header "Content-Type:application/json"````

DELETE
```curl -X DELETE http://localhost:5000/api/v1/series/6 --header "Content-Type:application/json"```
