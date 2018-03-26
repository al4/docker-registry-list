docker-registry-list
====================

Simple script to list the available tags for a given image name

Usage
-----

```
./docker-registry-list.py -h
usage: docker-registry-list.py [-h] [-t TOKEN] [-i INDEX_URL] [-a AUTH_URL]
                               name

positional arguments:
  name                  Name of image to list versions of

optional arguments:
  -h, --help            show this help message and exit
  -t TOKEN, --token TOKEN
                        Auth token to use (automatically fetched if not
                        specified)
  -i INDEX_URL, --index-url INDEX_URL
  -a AUTH_URL, --auth-url AUTH_URL
```

Example
-------
```
./docker-registry-list.py alpine
{
  "name": "library/alpine",
  "tags": [
    "2.6",
    "2.7",
    "3.1",
    "3.2",
    "3.3",
    "3.4",
    "3.5",
    "3.6",
    "3.7",
    "edge",
    "latest"
  ]
}
```