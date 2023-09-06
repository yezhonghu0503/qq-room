import time
import pygetwindow as gw
import pyautogui
import pyperclip
import psutil
import time


def check_link(is_check):
    # 记录当前活动窗口的标题
    current_window_title = None
    while is_check:
        try:
            # 获取当前活动窗口
            active_window = gw.getActiveWindow()

            # 检查是否有新窗口被激活
            if active_window is not None and active_window.title != current_window_title:
                current_window_title = active_window.title

                # 检查标题中是否包含浏览器名称（这里以Chrome为例）
                if "Chrome" in active_window.title:
                    # 在此处执行你的操作，例如获取浏览器链接
                    pyautogui.hotkey("ctrl", "l")  # Ctrl+L 快捷键用于选中浏览器地址栏
                    time.sleep(0.5)  # 等待浏览器地址栏被选中
                    pyautogui.hotkey("ctrl", "c")  # Ctrl+C 快捷键用于复制链接
                    clipboard_content = pyperclip.paste()  # 使用 pyperclip 获取剪贴板内容
                    print("打开的链接:", clipboard_content)

            time.sleep(1)  # 每秒检查一次活动窗口
        except KeyboardInterrupt:
            break


# 指定要监听的程序名称
target_program_name = "notepad.exe"  # 请根据你要监听的程序名称进行修改


def is_window_focused(program_name):
    # 获取所有窗口
    all_windows = gw.getWindowsWithTitle(program_name)

    # 检查是否有新窗口被激活
    if all_windows:
        return all_windows[0].isVisible
    else:
        return False


while True:
    # 检查指定程序的窗口是否置于最前端
    if is_window_focused(target_program_name):
        print(f"{target_program_name} 的窗口在最前端")

    # 可以在这里执行你的其他操作

    time.sleep(5)  # 休眠时间可以根据需要进行调整


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
