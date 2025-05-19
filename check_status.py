from datetime import date

# 文件路径
zb_path = 'zb.txt'  # 值班日期（当天在此文件表示值班 = 0）
xj_path = 'xj.txt'  # 休假日期（当天在此文件表示休假 = 1）
status_path = 'status.txt'  # 输出状态文件

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

    # 转换为列表
    zb_days = [day.strip() for day in zb_content.split(',') if day.strip()]
    xj_days = [day.strip() for day in xj_content.split(',') if day.strip()]

    # 判断
    is_bz_day = today_str in zb_days
    is_xj_day = today_str in xj_days

    # 设置默认状态
    status = '0'  # 默认为正常
    if is_xj_day:
        status = '1'  # 休假优先
    elif is_bz_day:
        status = '0'  # 值班（其实已是默认值）

    # 保存状态
    try:
        with open(status_path, 'w') as f:
            f.write(status)
    except Exception as e:
        print("写入状态文件失败：", e)

if __name__ == "__main__":
    main()
