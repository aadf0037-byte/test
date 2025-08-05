import sys
from mcp.server.fastmcp import FastMCP




dir = "D:\\GOPATH\\src\\cc\\testpy\\test\\mymcp"
sys.path.append(dir)

mcp = FastMCP()




if __name__ == '__main__':
    mcp.run(transport="stdio")
