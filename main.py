from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List
import uvicorn

from utils import orderMealPlans

app = FastAPI()

class Item(BaseModel):
    string: str
    array: List[List[int]]

@app.post("/getOrderMealPlans/", status_code=status.HTTP_201_CREATED)
async def process_item(item: Item):
    try:
        # The endpoint simply returns the array from the JSON payload

        res = orderMealPlans(item.string, item.array)

        return {"generatedMeals": res}
    except Exception as e:
        # If something goes wrong, return an HTTP 400 error
        raise HTTPException(status_code=400, detail=str(e))
