from src.app import assembler

app = assembler()

if __name__ == "__main__":
    app = assembler()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)