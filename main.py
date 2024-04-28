from utils import cleaned_tokenized

from fastapi import FastAPI
import uvicorn

app = FastAPI( debug = True)

@app.get('/predict/{rev}' , status_code=200)

def predict(rev : str):

    predict = cleaned_tokenized(rev)
    
    return {'prediction is' : predict}

    # Run through terminal
if __name__== '__main__' :
    uvicorn.run(app,host='127.0.0.1',port=8000)

