from langchain_mcp_adapters.client import MultiServerMCPClient

async def create_mcp_stdio_client(name, params):
    config = {
        name: {
            "transport": "stdio",
            **params,
        }
    }

    print(config)
    client = MultiServerMCPClient(config)

    tools = await client.get_tools()

    return client, tools

async def get_stdio_account_tools():
    params = {
        "command": "python",
        "args": [
            "D:\\GOPATH\\src\\cc\\testpy\\test\\mymcp\\account.py",
        ]
    }

    client, tools = await create_mcp_stdio_client("account_tools", params)

    return tools