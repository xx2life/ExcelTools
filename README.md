# ExcelTools

使用FastAPI 提供接口，将`.xls`,`xlsx`格式的文件转换成python的字典返回JSON;
同时提供将MongoDB中的数据导出为`.xls`,`xlsx`格式的Excel格式文件。

## 项目结构
```text
├── READEME.md
├── app
│   ├── api
│   ├── config
│   ├── crud
│   ├── db
│   └── utils
├── main.py
└── requirements.txt
```


## 配置环境

```shell
pip install -r requirements.txt
```

## 快速开始

```shell
python main.py
```

## 文档
启动main.py之后，访问`127.0.0.1:8000/docs`文档地址。 
