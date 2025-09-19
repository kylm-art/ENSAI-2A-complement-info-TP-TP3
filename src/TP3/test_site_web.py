from fastapi import FastAPI
import uvicorn

# Instantiate the web service
app = FastAPI()

# Create an endpoint that responds to the GET method at the address "/" and returns the message "Hello World".
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Launching the application on port 5000
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)