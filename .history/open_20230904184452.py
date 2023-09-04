import time
import pygetwindow as gw
import pyautogui
import pyperclip
import psutil
import time

# 记录当前活动窗口的标题
current_window_title = None

# while True:
#     try:
#         # 获取当前活动窗口
#         active_window = gw.getActiveWindow()

#         # 检查是否有新窗口被激活
#         if active_window is not None and active_window.title != current_window_title:
#             current_window_title = active_window.title

#             # 检查标题中是否包含浏览器名称（这里以Chrome为例）
#             if "Chrome" in active_window.title:
#                 # 在此处执行你的操作，例如获取浏览器链接
#                 pyautogui.hotkey("ctrl", "l")  # Ctrl+L 快捷键用于选中浏览器地址栏
#                 time.sleep(0.5)  # 等待浏览器地址栏被选中
#                 pyautogui.hotkey("ctrl", "c")  # Ctrl+C 快捷键用于复制链接
#                 clipboard_content = pyperclip.paste()  # 使用 pyperclip 获取剪贴板内容
#                 print("打开的链接:", clipboard_content)

#         time.sleep(1)  # 每秒检查一次活动窗口
#     except KeyboardInterrupt:
#         break

# 指定要监听的浏览器名称
target_browser_name = "QQ.exe"  # 请根据你的浏览器名称进行修改

# 定义函数来检查指定进程是否打开浏览器链接


def is_browser_opening_link(process):
    try:
        # 获取进程的命令行参数
        cmdline = process.cmdline()
        # 检查命令行参数中是否包含浏览器名称以及"http"或"https"
        if target_browser_name in cmdline and any("http" in arg for arg in cmdline):
            return True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
    return False


while True:
    # 获取所有正在运行的进程
    running_processes = psutil.process_iter(attrs=['pid', 'name', 'cmdline'])

    # 遍历进程并检查是否有浏览器打开链接
    for process in running_processes:
        if is_browser_opening_link(process):
            print(f"{target_browser_name} 正在打开链接")

    # 休眠一段时间，然后再次检查
    time.sleep(5)  # 调整休眠时间根据需要
