import http.server
import socketserver
import socket
import webbrowser
import os

# 设置端口
PORT = 8000

# 切换到HTML文件所在的目录
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 创建HTTP请求处理器
Handler = http.server.SimpleHTTPRequestHandler

# 获取本机IP地址
def get_local_ip():
    try:
        # 创建一个套接字连接到外部服务器但不发送数据
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

# 启动服务器
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    local_ip = get_local_ip()
    
    print("=" * 60)
    print("圣诞树动画网页服务器已启动!")
    print("=" * 60)
    print(f"本地访问: http://localhost:{PORT}")
    print(f"局域网访问: http://{local_ip}:{PORT}")
    print("=" * 60)
    print("重要提示:")
    print("1. 确保防火墙允许端口8000")
    print("2. 同一网络下的设备可以通过局域网IP访问")
    print("3. 按 Ctrl+C 停止服务器")
    print("=" * 60)
    
    # 自动在浏览器中打开页面
    webbrowser.open(f"http://localhost:{PORT}")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")