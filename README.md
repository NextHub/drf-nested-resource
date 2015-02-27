# drf-nested-resource

This project is currently under heavy development and should not be used until this notice has been removed.

## Overview

The inspiration for this package was taken from [django-rest-framework-nested-resource](https://github.com/simpleenergy/django-rest-framework-nested-resource), and hence the problem that both these packages are trying 
to solve is the same. It's just that this package will address it in it's own way. 

## Requirements

* Python (2.7, 3.2, 3.3, 3.4)
* Django (1.6, 1.7)
* Django REST Framework (3.0+)

## Installation

Install using `pip`...

```bash
$ pip install drf-nested-resource
```

## Example

TODO: Write example.

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```


[build-status-image]: https://secure.travis-ci.org/NextHub/drf-nested-resource.png?branch=master
[travis]: http://travis-ci.org/NextHub/drf-nested-resource?branch=master
[pypi-version]: https://pypip.in/version/drf-nested-resource/badge.svg
[pypi]: https://pypi.python.org/pypi/drf-nested-resource
