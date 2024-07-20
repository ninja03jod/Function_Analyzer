from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.llms import Ollama
import nest_asyncio
import uvicorn

nest_asyncio.apply()

app = FastAPI()

class FunctionInput(BaseModel):
    code: str
    language: str

llm = Ollama(model='llama3')

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI is working!"}

@app.post("/analyze_function")
async def analyze_function(input: FunctionInput):
    prompt = f"""
    {input.code}

    Analyze the function in programming language {input.language}
    Provide detailed information about it
    Identify any possible bugs and fix them
    Give me a list of global variables used in the function in list format
    Please provide test cases in array format to test this function. Each test case should be a dictionary containing 'input' and 'output'.
    At least 40 test cases
    
    """

    try:
        response = llm.invoke(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)