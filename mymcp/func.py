from account import mcp
from typing import Annotated
from pydantic import Field

# 查询接口
@mcp.tool(name="query", description="通过服务器id，查询服务器信息，返回服务器信息")
def query(server_id: Annotated[str, Field(description="服务器id", examples=["456"])]
          ) -> str:
    return query_account_info_impl(server_id)


def query_account_info_impl(server_id: str) -> str:
    return "123"