# brewer #
### brew your own! ###
barebone flask app for a tasty, delightfully smooth start  
what it does:
- customizable webapp with minimum boilerplate
- can be easily deployed to heroku
- supports various environments configs (add your own, too!)
- sqlalchemy and migrations included
- manager included   

### set up! ###
note: ```APP_SETTINGS``` is a environment variable which needs to be set depending on your enviroment:   
- ```cd``` to directory of choice
- clone this repo
- create a venv and activate it
- ```pip install -r requirements.txt```
- ```export APP_SETTINGS="config.[chosen_config]"```   
...and you're good to go!   
   
to automate these (and the activation of your venv of choice) i suggest using [autoenv](https://github.com/kennethreitz/autoenv)

