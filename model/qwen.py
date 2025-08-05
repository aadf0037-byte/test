from langchain_openai import ChatOpenAI

llm_qwen =  ChatOpenAI(
    model="qwen-plus-latest",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key="密钥",
    temperature=0,
)