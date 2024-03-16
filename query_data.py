import os
import argparse
from dotenv import load_dotenv

from langchain.vectorstores.chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


CHROMA_PATH = "chroma"

load_dotenv()
OPEN_API_KEY = os.getenv('OPENAI_API_KEY')

PROMPT_TEMPLATE = """
The context is the following:

{context}

---

Answer the question based on the above context: {question}
"""


def main():
    # Create the command line arguments

    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")

    args = parser.parse_args()
    query_text = args.query_text

    # Prepare the DB.
    embedding_function = OpenAIEmbeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=5)
    if len(results) == 0 or results[0][1] < 0.7:  # adjust till reasonable answers come up. 0.9 for instance was
        # terrible
        print(f"Unable to discern answer")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    model = ChatOpenAI()
    response_text = model.invoke(prompt)

    print(f"LeBot: {response_text}")


if __name__ == "__main__":
    main()
