import os
from datetime import date

# 绝对路径示例，请根据实际路径修改
base_dir = os.path.dirname(os.path.abspath(__file__))
zb_path = os.path.join(base_dir, 'zb.txt')
xj_path = os.path.join(base_dir, 'xj.txt')
index_path = os.path.join(base_dir, 'index.html')  # 直接写入 index.html

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except Exception as e:
        print(f"读取文件{filepath}失败：{e}")
        return ""

def write_to_index(content):
    try:
        with open(index_path, 'w') as f:
            f.write(content)
        print(f"内容写入成功：{index_path}")
    except Exception as e:
        print(f"写入内容失败：{e}")

def main():
    today_str = date.today().isoformat()
    print(f"开始检测日期：{today_str}")

    zb_content = read_file(zb_path)
    xj_content = read_file(xj_path)

    zb_days = [day.strip() for day in zb_content.split(',') if day.strip()]
    xj_days = [day.strip() for day in xj_content.split(',') if day.strip()]

    print(f"值班日期：{zb_days}")
    print(f"休假日期：{xj_days}")

    is_bz_day = today_str in zb_days
    is_xj_day = today_str in xj_days

    status = '0'  # 默认值班/正常
    if is_xj_day:
        status = '1'  # 休假优先

    print(f"今日状态为：{status}")

    # 将状态值写入 index.html
    write_to_index(status)

if __name__ == '__main__':
    main()
