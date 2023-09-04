import time
import pygetwindow as gw
import pyautogui
import pyperclip
import psutil


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


def get_running_applications():
    running_apps = []
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            app_name = process.info['name']
            running_apps.append(app_name)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return running_apps


while True:
    running_apps = get_running_applications()
    print("打开的应用程序列表:")
    for app in running_apps:
        if app == 'QQ.exe':
            print('QQ已启动')

    # 可以在这里执行你的其他操作

    # 休眠一段时间，然后再次检查应用程序列表
    time.sleep(5)  # 休眠时间可以根据需要进行调整
