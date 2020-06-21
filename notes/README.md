This notes are only meant for me, so I don't forget things, but if you want you can see it.

How to deploy python app to heroku

https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true
https://github.com/heroku/python-getting-started
https://github.com/Hedde/fastapi-heroku-test
https://github.com/fawazahmed0/google-translate-heroku
https://fastapi.tiangolo.com/tutorial/first-steps/
https://www.tutlinks.com/create-and-deploy-fastapi-app-to-heroku/

you only have to use 'heroku create' once in the new repo, then deploy the app with changes 'git push heroku master'
you can connect the app with github in apps settings (but don't enable auto deployment, the environment link will then show up in github, you did that by mistake just refer Remove enviroment from github repo.txt) (manually deploy everytime you update the code)
https://devcenter.heroku.com/articles/github-integration



To test app locally I can use(where main is the python file name containing code):
uvicorn --port 5000 --host 127.0.0.1 main:app --reload



Adding heroku deploy button:
https://devcenter.heroku.com/articles/heroku-button
