# Game Admin API

一个使用 Python、FastAPI 和 JSON 开发的游戏角色管理后端接口项目。

项目支持角色查询、新增、修改和删除，并使用 Pydantic 进行请求体数据校验，通过 HTTPException 处理资源不存在和角色重名等情况。

## 项目功能

- 查询全部角色
- 按名字查询角色
- 添加新角色
- 修改角色等级和好感度
- 删除指定角色
- 角色重名检查
- 请求体类型校验
- 404 和 409 异常处理
- JSON 数据持久化
- Swagger 自动接口文档

## 使用技术

- Python
- FastAPI
- Pydantic
- JSON
- RESTful API
- GET / POST / PUT / DELETE
- Swagger / OpenAPI
- HTTPException

## 项目结构

```text
game_admin_api
├── main.py
├── characters.json
├── README.md
├── requirements.txt
└── resume_project_description.txt