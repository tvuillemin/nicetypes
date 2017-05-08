# nicetypes

Advanced types for Python3: ImmutableDict and UniqList.

## Examples

### ImmutableDict

#### Usage

```python
from nicetypes import ImmutableDict
frozen_dict = ImmutableDict({"foo": 1, "bar": 2})
print(frozen_dict)
# ImmutableDict({'foo': 1, 'bar': 2})
frozen_dict["foo"] = 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'ImmutableDict' object does not support item assignment
```


### UniqList

#### Usage

```python
from nicetypes import UniqList
unql = UniqList([1, 2, 2, 2, 3, 2])
print(unql)
# UniqList([1, 2, 3])
unql.append(4)
unql.append(4)
print(unql)
# UniqList([1, 2, 3, 4])
```

## Usinge nicetypes

### Prerequisites

This module is developped on a Fedora 25 machine with Python 3.5.3, but it should theoretically run on **any system with a Python3 interpreter**. Don't hesitate to report any issues if it doesn't work on your platform. However, this module is not intented to work on Python2.

### Installation

#### Pip + Virtualenv (recommended)

First, make sure Pip is installed. Linux users should use their package manager. Alternatively, you can follow the [official site documentation](https://pip.pypa.io/en/stable/installing/). Then, make sure virtualenv is installed. Most linux distribution provide a virtualenvwrapper package that make virtualenvs easy-to-use. Otherwise, you might read [this documentation](https://virtualenv.pypa.io/en/stable/).

```bash
mkvirtualenv -p python3 foobar
workon foobar  # Should be automatically done by the previous command
pip install nicetypes
# Later, check for upgrades with
pip install -U nicetypes
```

#### Pip + admin rights

This method is similar to the previous one. First, get pip. Then, install nicetypes directly on your system with admin rights instead of installing it in a isolated virtualenv.

```bash
sudo pip3 install nicetypes
# Later, check for upgrades with
sudo pip3 install -U nicetypes
```

#### Sources download (avoid)

If you can't use Pip, then you could download the sources directly from Github. However, you should understand that you will need to handle updates and system integration all by yourself if you choose this method.

## Contributing

### Prerequisites

1. Make sure you have the following packages installed:
    - Python3,
    - Git,
    - Virtualenv.
2. Clone this Github repository and enter the repository.
3. Create a Python3 virtualenv and activate it.
4. Install the development dependencies with `pip install -r dev-requirements.txt`

### Style guide

Keep [PEP20](https://www.python.org/dev/peps/pep-0020/#the-zen-of-python) in mind, and use pylint to follow the coding style guide:

```
pylint --rcfile=.pylintrc src/nicetypes
```

### Unit tests

Make sure that all the code is covered by unit tests. Use a [Given-When-Then](https://github.com/cucumber/cucumber/wiki/Given-When-Then) structure to increase the tests readability. Avoid importing external libraries for the assertions, use the unittest methods instead. Run the tests and check the coverage with:

```
py.test --verbose --cov=src --cov-fail-under=100
```

### Continuous integration

This module use a [Travis pipeline](https://travis-ci.org/tvuillemin/nicetypes) for continuous integration. It performs the following actions when a Git branch is pushed on Github:
1. check the style guide,
2. run the unit tests and checking the coverage,
3. in case of tagged release, deploy to PyPI.

## Authors

- [Thibaut Vuillemin](https://github.com/tvuillemin/)

### Special thanks

- [Balthazar Rouberol](https://github.com/brouberol)
- [Guillaume Bouchard](https://github.com/guibou)

## License

This module is licensed under the MIT License - see the LICENSE file for details.
