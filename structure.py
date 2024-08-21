from fastapi import FastAPI
app=FastAPI()
main= [
    {"hello Adhrit all good 2"}
]
@app.get("/")
async def aditi():
    return main