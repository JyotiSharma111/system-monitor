from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from psutil import cpu_percent, virtual_memory, disk_usage

app=FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return  FileResponse("static/index.html")

@app.get("/info")
def info():
    return {"message":"Your app info is good"}

@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/metrics")
def metrics():
    return{
        "cpu":{"usage_percent": cpu_percent(interval=1)},
        "memory":{
            "total_gb": round(virtual_memory().total/(1024**3)),
            "available_gb": round(virtual_memory().available/(1024**3)),
            "percent_used": virtual_memory().percent

        }
                  ,
        "disk":{
            "total_gb": round(disk_usage("/").total/(1024**3)),
            "available_gb": round(disk_usage("/").free/(1024**3)),
            "percent_used":disk_usage("/").percent

        }
    }