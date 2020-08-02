from fastapi import FastAPI

app = FastAPI()

'''
基本のルーティングテスト
todo appと関係ない
'''


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("item/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
