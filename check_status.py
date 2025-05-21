import os
from datetime import date
import tempfile

# 基础路径，按需调整
base_dir = os.path.dirname(os.path.abspath(__file__))
zb_path = os.path.join(base_dir, 'zb.txt')
xj_path = os.path.join(base_dir, 'xj.txt')
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
    先写入临时文件，再重命名为目标文件，提高写入原子性和安全性。
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
    today_str = date.today().isoformat()
    print(f"开始检测日期：{today_str}")

    zb_content = read_file(zb_path)
    xj_content = read_file(xj_path)

    zb_days = [d.strip() for d in zb_content.split(',') if d.strip()] if zb_content else []
    xj_days = [d.strip() for d in xj_content.split(',') if d.strip()] if xj_content else []

    # 日志提示
    if not zb_days:
        print("警告：值班日期列表为空或未读取到有效内容！")
    if not xj_days:
        print("提示：休假日期列表为空或未读取到有效内容！")

    print(f"值班日期：{zb_days}")
    print(f"休假日期：{xj_days}")

    is_bz_day = today_str in zb_days
    is_xj_day = today_str in xj_days

    if is_xj_day:
        status = '1'  # 休假优先
    elif is_bz_day:
        status = '0'  # 值班
    else:
        status = '2'  # 非值班非休假，节假日接口判断

    print(f"今日状态为：{status}")

    atomic_write(index_path, status)

if __name__ == '__main__':
    main()
