from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()


#llm
llm = ChatOpenAI(
    model="Pro/zai-org/GLM-4.7",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL"),
)


if __name__ == "__main__":
    # 测试
    print(llm.invoke("你好，你是谁"))