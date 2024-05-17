import tomllib

from src.app import assembler

# Database information. Does not make full use of TOML
# We need the DB to be able to read this without parsing TOML
with open("db_password", "rb") as f:
    configdata = tomllib.load(f)

# we update the dictionary with data from the default.toml file
# this uses the full TOML standard
with open("defaults.toml", "rb") as f:
    configdata.update(tomllib.load(f))

app = assembler(configdata)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)