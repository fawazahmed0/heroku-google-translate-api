from fastapi import FastAPI, HTTPException, Request
from googletrans import Translator
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# https://fastapi.tiangolo.com/tutorial/cors/

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is only for testing out that heroku works


@app.get("/")
async def root():
    return {"message": "Hello World"}


# https://www.tutlinks.com/create-and-deploy-fastapi-app-to-heroku/
# https://fastapi.tiangolo.com/tutorial/first-steps/
@app.get("/translategettext/")
async def queryTranslateGetText(query=''):
    translator = Translator()
    # Return if query is empty
    if not query:
        return ''
    try:
        return translator.translate(query).text
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")


@app.get("/translategetfull/")
async def queryTranslateGetJSON(query=''):
    translator = Translator()
    # Return if query is empty
    if not query:
        return ''
    try:
        return translator.translate(query)
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")


@app.post("/translateposttext/")
async def queryTranslatePosttext(request: Request):
    req = await request.body()
    req = json.loads(req)

    translator = Translator()
    # Return if body is empty
    if not req:
        return ''
    try:
        return translator.translate(req).text
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")


@app.post("/translatepostfull/")
async def queryTranslatePostJSON(request: Request):
    req = await request.body()
    req = json.loads(req)

    translator = Translator()
    # Return if body is empty
    if not req:
        return ''
    try:
        return translator.translate(req)
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")
