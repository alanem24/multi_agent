import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm import llm
from langchain_core.prompts import ChatPromptTemplate
import json
from tools.collect_tools import collect_hot_store


prompt = ChatPromptTemplate.from_messages(
        [
        ("system","""请分析以下用户咨询的意图，从以下类别中选择最合适的：
            [热点咨询收集, 实时商品收集, 用户评价收集, 发货情况, 订单状态, 商品价格收集, 其他]
            用户咨询：{input}
            请返回JSON格式:{{"classification": "类别", "confidence": 置信度0-1, "key_points": ["关键点1", "关键点2"]}}"""),
        ("human","{input}")
        ]
)

if __name__ == "__main__":

    chain = prompt | llm
    res = chain.invoke({"input": "帮我收集一下微博实时热点"})
    print(res)


    # 处理预测结果
    final_ouput = res.content.split("```")[1].strip("json")
    # print(final_ouput)
    json1= json.loads(final_ouput)
    input = json1.get("classification")
    print

    bind_tool = llm.bind_tools([collect_hot_store])
    refinal = bind_tool.invoke(input)
    print(refinal)
