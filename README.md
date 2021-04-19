# Job Search Tool

## Setup

Create a Virtual Environment:

```bash
virtualenv venv
source venv/bin/activate
```

Download dependencies:

```bash
(venv) pip install -r requirements.txt
```

Create `.env` file in the website directory using template:

```bash
TESTING=True/False
DEBUG=True/False
SECRET_KEY=yoursecretlittlekey
SERVER=0.0.0.0
```

## Server

Lastly, run the webserver in the website directory:

```bash
python main.py
```


