from datetime import date

# 文件路径
zb_path = 'zb.txt'
xj_path = 'xj.txt'
status_path = 'status.txt'

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except:
        return None

def main():
    today_str = date.today().isoformat()
    zb_info = read_file(zb_path)
    xj_info = read_file(xj_path)

    # 判断
    if zb_info == today_str or xj_info == today_str:
        new_status = '1'  # 休假或值班
    else:
        new_status = '0'  # 工作日

    # 写入status.txt
    with open(status_path, 'w') as f:
        f.write(new_status)

if __name__ == "__main__":
    main()
