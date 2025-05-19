from datetime import date

# 文件路径（请确保在同一目录或调整路径）
zb_path = 'zb.txt'    # 休假/值班日期列表
xj_path = 'xj.txt'    # 其他休假/值班日期
status_path = 'status.txt'  # 状态输出文件

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except:
        return ""

def main():
    today_str = date.today().isoformat()

    zb_content = read_file(zb_path)
    xj_content = read_file(xj_path)

    # 将内容按逗号分割，去除空白
    zb_days = [day.strip() for day in zb_content.split(',') if day.strip()]
    xj_days = [day.strip() for day in xj_content.split(',') if day.strip()]

    # 判断当天是否在任何休假或值班日期内
    if today_str in zb_days or today_str in xj_days:
        status = '1'   # 休假/值班
    else:
        status = '0'   # 工作日

    # 写入状态文件
    with open(status_path, 'w') as f:
        f.write(status)

if __name__ == "__main__":
    main()
