from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import webbrowser
import pyautogui
import os
import sys

# 获取临时解压路径（PyInstaller运行时）
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

while True:
    try:
        url = input("请输入：")
        if not url:
            break
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)  # 解析查询参数
        query_params['contentType'] = ['x_url']
        query_params['catalogType'] = ['elecedu']

        new_query = urlencode(query_params, doseq=True)  # doseq=True 处理多值参数
        # 4. 重新组合 URL
        new_url = urlunparse((
            parsed_url.scheme,    # https
            parsed_url.netloc,    # basic.smartedu.cn
            parsed_url.path,      # /tchMaterial/detail
            parsed_url.params,    # 通常为空
            new_query,            # 新的查询参数
            parsed_url.fragment   # 锚点（通常为空）
        ))
        webbrowser.open(new_url)
        button_pos = pyautogui.locateOnScreen(resource_path('kebenxiazai\dianji.png'), confidence=0.8, minSearchTime=10)
        if button_pos:
            x, y = pyautogui.center(button_pos)
            pyautogui.moveTo(x, y, duration=0.5)
            pyautogui.click()
            print('成功!')
    except Exception as e:
        print("错误：", e)

