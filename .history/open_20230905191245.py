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
target_program_name = "QQ"  # 请根据你要监听的程序名称进行修改


def is_window_focused(program_name):
    # 获取所有窗口
    windows = gw.getWindowsWithTitle(program_name)
    print(windows[0].isActive)
    # 检查窗口是否存在并且最前端
    if windows:
        return windows[0].isActive
    else:
        return False


is_window_focused(target_program_name)
# while True:
#     # 检查指定程序的窗口是否置于最前端
#     if is_window_focused(target_program_name):
#         print(f"{target_program_name} 的窗口在最前端")

#     # 可以在这里执行你的其他操作

#     time.sleep(5)  # 休眠时间可以根据需要进行调整
