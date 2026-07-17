import json
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


app = FastAPI(
    title="Game Admin API",
    description="一个使用 FastAPI 和 JSON 实现的游戏角色管理后端接口项目",
    version="1.0.0"
)


class CharacterCreate(BaseModel):
    name: str
    rarity: str
    camp: str
    level: int
    favor: int
    skills: list[str]


class CharacterUpdate(BaseModel):
    level: int
    favor: int


def load_characters():
    with open("characters.json", "r", encoding="utf-8") as file:
        characters = json.load(file)

    return characters


def save_characters(characters):
    with open("characters.json", "w", encoding="utf-8") as file:
        json.dump(characters, file, ensure_ascii=False, indent=4)


@app.get("/")
def home():
    return {"message": "欢迎使用 Game Admin API"}


@app.get("/characters")
def get_characters():
    characters = load_characters()
    return characters


@app.post("/characters", status_code=status.HTTP_201_CREATED)
def create_character(character: CharacterCreate):
    characters = load_characters()

    for existing_character in characters:
        if existing_character["name"] == character.name:
            raise HTTPException(status_code=409, detail="这个角色已经存在")

    new_character = character.model_dump()

    characters.append(new_character)
    save_characters(characters)

    return {
        "message": "角色添加成功",
        "character": new_character
    }


@app.put("/characters/{name}")
def update_character(name: str, update_data: CharacterUpdate):
    characters = load_characters()

    for character in characters:
        if character["name"] == name:
            character["level"] = update_data.level
            character["favor"] = update_data.favor

            save_characters(characters)

            return {
                "message": "角色信息修改成功",
                "character": character
            }

    raise HTTPException(status_code=404, detail="没有找到这个角色")


@app.delete("/characters/{name}")
def delete_character(name: str):
    characters = load_characters()

    for character in characters:
        if character["name"] == name:
            characters.remove(character)
            save_characters(characters)

            return {
                "message": "角色删除成功",
                "character": character
            }

    raise HTTPException(status_code=404, detail="没有找到这个角色")


@app.get("/characters/{name}")
def get_character_by_name(name: str):
    characters = load_characters()

    for character in characters:
        if character["name"] == name:
            return character

    raise HTTPException(status_code=404, detail="没有找到这个角色")