# News Python
This is a python package than fetches news from google news and speaks it for you . It is a cli tool that you can use . It is not published on PyPi Due to some reasonsbut will be soon.
You can choose language , location , topic and no of news you want to listen as per your convenience. Because it is a cli tool then it is easy for a linux user to access it .

## Features
* Easy to install
* Customizable
* Speaks out news for the user 
* Comes with a bunch of language supports.
* Text decoration
* Does'nt use argparse



## How to install ?
Clone the project

```bash
  git clone https://https://github.com/ZayedMalick/news-python-cli.git
```

Go to the project directory

```bash
  cd news-python-cli
```

Install Requirements

```bash
  pip install -r requirements.txt
```

Run Setup

```bash
  python setup.py install
```


## Why not on PyPi ?
I have'nt posted the project on PyPi because it still have some bugs and issues , one of those issues are the python-Levenshtein warning issue which is very annoying , after these issues and bugs are fixed then i will post it on PyPi

# Bug Fixes
This section will give you an idea of how to fix issues.

## Fixing python_Levenshtein issue
If you have installed this library and you just ran it then you must have got a warning like this :
```bash
warnings.warn('Using slow pure-python SequenceMatcher. Install python-Levenshtein to remove this warning')
```

If you are getting this warning then just install python-levenshtein in your machine by typing :
```python
pip install python-Levenshtein 
```
If you get a wheel error then goto [Unofficial Python Binaries](https://www.lfd.uci.edu/~gohlke/pythonlibs/) and install the wheel for python-Levenshtein.



