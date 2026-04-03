from langchain.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
import pandas as pd

# 数据收集工具类
"""
    1.热搜数据收集
    2.商品数据收集
        2.1 
    3.用户数据收集
        3.1 用户基本信息
        3.2 用户购物车数据
        3.3 用户订单数据
"""



'''热搜数据工具及提示词'''
def collect_hot_store(input: str) -> str:
    """
    收集热搜数据
    """
    # 从hot_search.xlsx读取数据，并且转化成json格式
    df = pd.read_excel("hot_search.xlsx")
    return f"{input}:{df}，共{len(df)}条"




