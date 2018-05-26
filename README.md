# Twitter Bot - Teleportche

Twitter Bot to reply tweets (@yourappname) identifying sentiments (Positive and Negative) and probabilities with FastText


### Step 1: Install dependencies

You need the follow dependencies in your development environment:

  [Python](https://www.python.org/downloads/)

  [Tweepy](http://www.tweepy.org/)

  [FastText](https://pypi.org/project/fasttext/)

### Step 2: Download the train dataset

  [Amazon Reviews for Sentiment Analysis:](https://www.kaggle.com/bittlingmayer/amazonreviews)

  Unzip the content inside the folder "./amazonreviews"

### Step 3: Create a Twitter app

https://apps.twitter.com/app/new

Pay attention to the filds:
Name: That will be the @name that your bot will the mentioned on Twitter
Website: If you don't have a website, it is possible to try http://127.0.0.1

### Step 4: Clone this repository

Please, clone this repo to your local development environment.
Replace the information in secrets.py with your keys and access tokens from the Twitter app you just created.


### Step 5: Excecute

Excecute the script twitterBot.py with the command line inside the project folder:

```
$ python twitterBot.py
```
The bot will only Reply tweets while the script will be executing.
