import os
from datetime import date
import tempfile

# 基础路径，确保和脚本在同一目录
base_dir = os.path.dirname(os.path.abspath(__file__))

zb_path = os.path.join(base_dir, 'zb.txt')       # 值班日期文件
xj_path = os.path.join(base_dir, 'xj.txt')       # 休假日期文件
index_path = os.path.join(base_dir, 'index.html')  # 输出状态文件

def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if not content:
                print(f"警告：文件 {filepath} 内容为空！")
            return content
    except Exception as e:
        print(f"读取文件 {filepath} 失败：{e}")
        return ""

def atomic_write(filepath, content):
    """
    先写入临时文件，再原子替换目标文件，
    避免写入时文件损坏或读取异常。
    """
    dir_name = os.path.dirname(filepath)
    try:
        with tempfile.NamedTemporaryFile('w', encoding='utf-8', dir=dir_name, delete=False) as tmp_f:
            tmp_f.write(content)
            temp_name = tmp_f.name
        os.replace(temp_name, filepath)
        print(f"成功写入状态文件：{filepath} 内容：{content}")
    except Exception as e:
        print(f"写入文件 {filepath} 失败：{e}")

def main():
    # 当前日期字符串
    today_str = date.today().isoformat()
    print(f"开始检测日期：{today_str}")

    # 读取两份日期文件
    zb_content = read_file(zb_path)
    xj_content = read_file(xj_path)

    print(f"zb.txt 原始内容：'{zb_content}'")
    print(f"xj.txt 原始内容：'{xj_content}'")

    # 分割并清理日期列表（以逗号分隔）
    zb_days = [d.strip() for d in zb_content.split(',') if d.strip()] if zb_content else []
    xj_days = [d.strip() for d in xj_content.split(',') if d.strip()] if xj_content else []

    print(f"解析得到的值班日期列表: {zb_days}")
    print(f"解析得到的休假日期列表: {xj_days}")

    # 判断状态
    is_bz_day = today_str in zb_days
    is_xj_day = today_str in xj_days

    print(f"是否值班日？{is_bz_day}")
    print(f"是否休假日？{is_xj_day}")

    if is_xj_day:
        status = '1'  # 休假优先
    elif is_bz_day:
        status = '0'  # 值班
    else:
        status = '2'  # 其他（非值班非休假）

    print(f"今日状态为：{status}")

    # 原子写入状态文件
    atomic_write(index_path, status)

if __name__ == '__main__':
    main()
