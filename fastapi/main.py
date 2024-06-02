import subprocess
import pandas
import scipy
import subprocess
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import mysql.connector
import time

time.sleep(15)

connection = mysql.connector.connect(
    host="database",
    user="exampleuser",
    password="examplepassword",
    database="exampledb",
)

cursor = connection.cursor()
cursor.execute("SELECT VERSION();")
data = cursor.fetchone()
print("Database version:", data)
create_table_query = "CREATE TABLE source (code TEXT(65535), output TEXT(65535));"
cursor.execute(create_table_query)
connection.commit()

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    result = subprocess.run(["pip", "list"], stdout=subprocess.PIPE, text=True)
    return result.stdout


@app.post("/test")
async def execute(request: Request):
    source_code = await request.json()
    try:
        result = subprocess.run(
            ["python", "-c", source_code["code"]], capture_output=True, text=True
        )
        if result.stderr != "":
            return {'error': True, 'logs': result.stderr}
        else:
            return {'error': False, 'logs': result.stdout}
    except Exception as e:
        return {'error': False, 'logs': result.stderr}

def escape_single_quotes(input_string):
    return input_string.replace("'", "''")

@app.post("/submit")
async def submit(request: Request):
    source_code = await request.json()
    print(source_code["code"])
    try:
        result = subprocess.run(
            ["python", "-c", source_code["code"]], capture_output=True, text=True
        )
        if result.stderr != "":
            return {'error': True, 'logs': result.stderr}
        else:
            data = result.stdout
            if (result.stdout == ''):
                data = "None"
            source_code['code'] = escape_single_quotes(source_code['code'])
            data = escape_single_quotes(data)
            query_1 = f"INSERT INTO source (code, output) VALUES ('{source_code['code']}', '{data}')";
            cursor.execute(query_1)
            connection.commit()


            return {'error': False, 'logs': result.stdout}
    except Exception as e:
        print(e)
        return result.stderr
