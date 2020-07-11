# sentiment_analyser

## Usage-

### Steps-
### 1. Cloning the repo and change directory into the repo
``` bash
git clone https://github.com/kingZthefirst-cypher/sentiment_analyser.git
cd sentiment_analyser
```
### Note- I have used python 3.7.6
### 2. Install dependencies
``` bash
pip install requirements.txt
```
### 3. Change directory django project
``` bash
cd src
```
### 4. Run manage.py to host the server
``` bash
python manage.py runserver
```
### This will host the django backend on localhost:8000
### 5. Hit http://localhost:8000/sentiment with post json data in the form-
``` python
{"text": "your text"}
```
### 6. Response structure is-
``` python
{"text": "your text", "sentiment": 60 # values are between [-100, 100]}
```

### Repo for the React-UI- https://github.com/raj-saumya/sentiment-analysis