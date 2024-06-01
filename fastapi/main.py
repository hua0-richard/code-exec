import subprocess
import pandas
import scipy
import subprocess
from fastapi import FastAPI
from RestrictedPython import compile_restricted


app = FastAPI()


@app.get("/")
def read_root():
    result = subprocess.run(["pip", "list"], stdout=subprocess.PIPE, text=True)
    return result.stdout


@app.get("/run")
def exec():
    None
