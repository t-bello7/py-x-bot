# How To Create a Python Bot That auto schdeules trained tweets 

In this walkthrough I would be writing on how I created a python bot that tweets from a trained gemini model based on my google keep notes.


## Presquites
- Python 
- Git 
- Github Account
- Twitter Developer Account
- Google Developer Account 


## Step One: Setup a python project

Setting up a python project requires planning how to manage dependencies and environment variables. We would be making used of the following python packages to do that 

    - pipenv: Python Package for creating virtualenv
    - python_dotenv: Python Package for loading environemt variables 

In the project directory run the following command to install pipenv:
```
pip3 install pipenv
```
After installing pipenv, we can now create a virtual environment and install our project packages. In the terminal, run the command to activate your virtual envrionment of the project
```
pipenv shell
```
Now we can install the python dotenv package with the command
```
pipenv install python_dotenv
```
Now let's export the packages to requirements.txt file so we can install them on the github actions runner. We use the command

```
pip freeze > requirements.txt
```

The project file structure should look like this 
```
|-- Pipfile
|-- Pipfile.lock
```

## STEP TWO: Setup github actions 
To run github actions we need to create a schedule-tweet workflow in the github actions workflows file structure. Run the command to create the workflow
```
mkdir .github && mkdir workflows && touch .github/workflows/schedule-tweet.yml
```
In the schedule-tweet.yml file paste the follwing command that runs the python job every 1 minute. 

P. S: We won't be tweeting every one minute. This is just for testing purposes.
```
name: Schedule Tweet

on:
    schedule:
        - cron: "1 * * * *"  # Run Job every one minute

jobs:
    tweet:
        runs-on: unbuntu-latest
        steps:
            - name: Install python Packages
              run: pip install -r requirements.txt
```
The next thing to do if initialize git and push our code github. You can checkout this blog

