import tomllib

from src.app import assembler

with open("db_password", "rb") as f:
    configdata = tomllib.load(f)

app = assembler(**configdata)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)