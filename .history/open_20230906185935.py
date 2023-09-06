import win32gui
import time
import pygetwindow as gw
import time
import win32con


import time
import pygetwindow as gw
import pyperclip

# 指定要监听的程序名称
target_program_name = "QQ"  # 请根据你要监听的程序名称进行修改


def check_link():
    # 获取当前活动窗口的标题
    current_window_title = gw.getActiveWindow().title

    # 获取剪贴板内容
    clipboard_content = pyperclip.paste()

    # 检查标题或剪贴板内容是否包含链接信息
    if "http://" in current_window_title or "https://" in current_window_title:
        print("在窗口标题中发现链接:", current_window_title)
    elif "http://" in clipboard_content or "https://" in clipboard_content:
        print("在剪贴板中发现链接:", clipboard_content)


while True:
    # 检查指定程序是否处于活动状态
    active_window = gw.getWindowsWithTitle(target_program_name)

    if active_window:
        check_link()

    # 可以在这里执行你的其他操作

    time.sleep(5)  # 休眠时间可以根据需要进行调整


# # 指定要监听的程序名称
# target_program_name = "QQ"  # 请根据你要监听的程序名称进行修改


# def is_window_focused(program_name):
#     # 获取所有窗口
#     all_windows = gw.getAllTitles()

#     # 检查是否有新窗口被激活
#     if program_name in all_windows:
#         active_window = gw.getWindowsWithTitle(program_name)[0]
#         hwnd = win32gui.FindWindow(None, active_window.title)

#         # 获取窗口的状态
#         placement = win32gui.GetWindowPlacement(hwnd)

#         # placement[1] == win32con.SW_SHOWMINIMIZED 表示窗口最小化
#         if placement[1] != win32con.SW_SHOWNORMAL:
#             return False

#         return active_window.isActive
#     else:
#         return False


# while True:
#     # 检查指定程序的窗口是否处于最前端
#     if is_window_focused(target_program_name):
#         print(f"{target_program_name} 的窗口在最前端")

#     # 可以在这里执行你的其他操作

#     time.sleep(5)  # 休眠时间可以根据需要进行调整

# 指定要监听的程序名称
# target_program_name = "QQ.exe"
# target_program_short = "QQ"


# def is_program_open_and_focused(program_name, program_short):
#     current_window_title = gw.getActiveWindow().title
#     return program_short in current_window_title and is_process_running(program_name)


# def is_process_running(process_name):
#     for process in psutil.process_iter(attrs=['pid', 'name']):
#         try:
#             if process.info['name'] == process_name:
#                 return True
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#     return False


# time_sleep = 2
# while True:
#     if is_program_open_and_focused(target_program_name, target_program_short):
#         time_sleep = 10
#         print(f"{target_program_name} 正在打开且位于窗口界面")

#     time.sleep(time_sleep)
