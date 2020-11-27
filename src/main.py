from fastapi import FastAPI, HTTPException, Request
from google_trans_new import google_translator  
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
    translator = google_translator()
    # Return if query is empty
    if not query:
        return ''
    try:
        return translator.translate(query,lang_tgt='en')
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")


@app.get("/translategetfull/")
async def queryTranslateGetJSON(query=''):
    translator = google_translator()
    # Return if query is empty
    if not query:
        return ''
    try:
        return translator.translate(query,lang_tgt='en')
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")


@app.post("/translateposttext/")
async def queryTranslatePosttext(request: Request):
    req = await request.body()
    req = json.loads(req)

    translator = google_translator()
    # Return if body is empty
    if not req:
        return ''
    try:
        return translator.translate(req,lang_tgt='en')
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")


@app.post("/translatepostfull/")
async def queryTranslatePostJSON(request: Request):
    req = await request.body()
    req = json.loads(req)

    translator = google_translator()
    # Return if body is empty
    if not req:
        return ''
    try:
        return translator.translate(req,lang_tgt='en')
    except:
        raise HTTPException(
            status_code=404, detail="translate api doesn't seem to work")
