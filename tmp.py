from pydantic import BaseModel


class DataTemp(BaseModel):
    name: str = None
    title: str = None
    description: str = None

s = "   type object 'DataTemp' has no attribute 'name'    "

d = DataTemp(
    name=s.strip().replace("'", "") + "new data",
    title="some",
    description="desc"

)
d.name = "other"
DataTemp.name = "Bob"
print(DataTemp.title)
res = d.json()
print(res)