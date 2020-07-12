# sentiment_analyser
Used flairNlp library (link- https://github.com/flairNLP/flair) for out of the box sentiment analyser model, and built a rest API around it using django rest framework.
## Usage-

### Steps-
### 1. Cloning the repo and change directory into the repo
``` bash
git clone https://github.com/Sinha-Ujjawal/sentiment_analyser.git
cd sentiment_analyser
```
### Note- I have used python 3.7.6
### 2. Install dependencies
#### 2.1 Installing pytorch
##### If you have cuda 9.2
``` bash
pip install torch==1.5.1+cu92 torchvision==0.6.1+cu92 -f https://download.pytorch.org/whl/torch_stable.html
```
##### If you have cuda 10.1
``` bash
pip install torch==1.5.1+cu101 torchvision==0.6.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```
##### If you have cuda 10.2
``` bash
pip install torch===1.5.1 torchvision===0.6.1 -f https://download.pytorch.org/whl/torch_stable.html
```
##### If you dont have gpu or cuda
``` bash
pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```
#### 2.2 Installing remaining dependencies from requirements.txt
``` bash
pip install -r requirements.txt
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
