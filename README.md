# Google Translate API using Heroku

**Note:** [google-trans-new](https://github.com/lushan88a/google_trans_new) package is broken, hence this will not work, Unless someone fixes it.

This is a free google translate api using [Heroku](https://github.com/heroku/python-getting-started "Heroku"), [FastAPI](https://fastapi.tiangolo.com/tutorial/first-steps/ "FastAPI") , [google-trans-new](https://github.com/lushan88a/google_trans_new)  

This api will auto detect the language and translate it into english(under the hood it uses [google-trans-new](https://github.com/lushan88a/google_trans_new)), if you want to manually assign the source and destination language, you will have to modify the code a little bit. Please refer the above links if you intend to add that functionality.

**Steps to setup:**
1. Click at [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)        
2. Signup and you will get a url something like: https://calm-boy-84008.herokuapp.com ,  note it down

**API Endpoints:**
- Use `/translategettext` endpoint if you have small text to translate and only want translated text
- Use `/translategetfull` endpoint if you have small text to translate and JSON response with other details
- Use `/translateposttext` endpoint if you have any length text to translate and only want translated text
- Use `/translatepostfull` endpoint if you have any length text to translate and JSON response with other details

**Below examples in JavaScript:**

**Example 1:**
```javascript
// Text to be translated
var text = 'لا أعرف لماذا'
// Use the url here which you got in step 2
 fetch('https://calm-boy-84008.herokuapp.com/translategettext/?query='+encodeURIComponent(text))
.then(response => response.text())
.then(data => console.log(data))
```

**Output in Console:**

`"I do not know why"`

**Example 2:**
```javascript
// Text to be translated
var text = 'لا أعرف لماذا'
// Use the url here which you got in step 2
 fetch('https://calm-boy-84008.herokuapp.com/translategetfull/?query='+encodeURIComponent(text))
.then(response => response.json())
.then(data => console.log(data))
```

**Output in Console:**
`"I do not know why"`

**Example 3:**
```javascript
// text to be translated
var text = 'لا أعرف لماذا'
// Use the url here which you got in step 2
 fetch('https://calm-boy-84008.herokuapp.com/translateposttext',{
  method: 'POST',
  body: JSON.stringify(text)
})
.then(response => response.text())
.then(data => console.log(data))
```

**Output in Console:**

`"I do not know why"`

**Example 4:**
```javascript
// text to be translated
var text = 'لا أعرف لماذا'
// Use the url here which you got in step 2
 fetch('https://calm-boy-84008.herokuapp.com/translatepostfull',{
  method: 'POST',
  body: JSON.stringify(text)
})
.then(response => response.json())
.then(data => console.log(data))
```


**Output in Console:**
`"I do not know why"`
