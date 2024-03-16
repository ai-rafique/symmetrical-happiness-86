# symmetrical-happiness-86
Learning how to implement a simple Retreival Augmented Generation code using LangChains, ChromaDB, OpenAI, and Python

### Inspiration and learnt from
https://www.youtube.com/watch?v=tcqEUSNCn8I

### Howto get started

Install dependencies.
```python
pip install -r requirements.txt
```

Create the local Chroma DB.
```python
python create_database.py
```

Query the local Chroma DB.
```python
python query_data.py "Who is the bloodstained queen and what is their real name??"
```

### Changes to original implementation

The original code has been modified and the following has been done

- Used proper langchain-community library to make the code run
- Using Asato Asato's novel series Eighty Six as the input data (no I will not upload a copy here)
- Uses PDF instead of markdown, thouhgh to use markdown, just change the glob in load_documents() function of create_database.py to ".md" and install specified python package via pip.
- Added a .env file in project and loaded the environment variable in the code, user should just replace the openapi key with their own

