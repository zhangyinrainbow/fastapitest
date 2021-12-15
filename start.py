import uvicorn
from fastapi import FastAPI, HTTPException, Query

app = FastAPI()

people_id_str = {"1": "2"}
people_id_int = [1, 2, 3, 4, 5]


@app.post("/fastapi/{people_idone}")
async def postdate(
        people_idone: int,
        people_id_three: str = Query("1")
):
    if people_idone not in people_id_int:
        raise HTTPException(status_code=400, detail="people_idone不在范围里",headers={"nice":"what"})
        # 如果people_idone不在列表people_id_int里，那就报错400，并新增一个headers
    if people_id_three not in people_id_str:
        raise HTTPException(status_code=401, detail="people_id_three不在范围里")
        # 如果people_id_three不在people_id_str里，那就报错401
    return {"people_id": people_idone, "people_id_three": people_id_str[people_id_three]}


if __name__ == "__main__":
    uvicorn.run(app='start:app', host='0.0.0.0', port=8100, reload=True, debug=True)