"""
功能简述：从网页中保存图片到本地文件夹
1. 读取配置文件
    - 如无配置，则需要用户输入，并保存到配置文件中
    - 如有配置，直接使用配置里的参数
2. 打开浏览器
3. 最小化浏览器窗口
4. 滚动网页判断页面是否完成加载
    - 完成加载，读取所有图片列表，保存至配置文件中
    - 未完成加载，继续滚动网页

使用方法：
    ``` python

    ```

@File           : main.py
@Author         : Elson.L
@Created        : 2025-07-06
@Last Modified  : 2025-07-06
@Version        :
"""


# 读取配置文件
def read_config():
    import yaml
    import os

    config_file = "lib/settings.yaml"
    if os.path.exists(config_file):
        with open(config_file, "r", encoding="utf-8") as f:
            print(f"[DEBUG] {config_file} 文件已经存在")
            return yaml.safe_load(f)
    else:
        print(f"[DEBUG] {config_file} 文件不存在")
        return None


if __name__ == "__main__":
    print(read_config())
