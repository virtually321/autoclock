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
        return ""

def main():
    today_str = date.today().isoformat()

    # 读取文件内容
    zb_content = read_file(zb_path)
    xj_content = read_file(xj_path)

    # 将内容拆分为列表
    zb_days = [day.strip() for day in zb_content.split(',') if day.strip()]
    xj_days = [day.strip() for day in xj_content.split(',') if day.strip()]

    # 判断今天是否在值班或休假列表
    is_bz_day = today_str in zb_days
    is_xj_day = today_str in xj_days

    # 优先判定休假（status=1）；否则值班（status=0）
    if is_xj_day:
        status = '1'
    elif is_bz_day:
        status = '0'
    else:
        status = '0'  # 可根据需要修改，默认为正常工作日

    # 保存状态
    with open(status_path, 'w') as f:
        f.write(status)

if __name__ == "__main__":
    main()
