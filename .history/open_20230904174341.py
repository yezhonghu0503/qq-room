import time
import pygetwindow as gw
import pyautogui

# 记录当前活动窗口的标题
current_window_title = None

while True:
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
                clipboard_content = pyautogui.paste()
                print("打开的链接:", clipboard_content)

        time.sleep(1)  # 每秒检查一次活动窗口
    except KeyboardInterrupt:
        break
