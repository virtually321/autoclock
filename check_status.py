import requests
from datetime import date

# 配置
zb_path = 'zb.txt'
xj_path = 'xj.txt'
status_url = 'https://raw.githubusercontent.com/你的用户名/autoclock/main/status.txt'

def read_file(filepath):
    try:
        with open(filepath, 'r') as f:
            return f.read().strip()
    except:
        return None

def get_status_from_api():
    try:
        r = requests.get(status_url)
        if r.status_code == 200:
            return int(r.text.strip())
    except:
        pass
    return None

def main():
    today_str = date.today().isoformat()
    zb_info = read_file(zb_path)
    xj_info = read_file(xj_path)

    # 判断当天是否有信息
    if zb_info == today_str or xj_info == today_str:
        # 有信息，代表值班或休假
        print(1)
    else:
        api_status = get_status_from_api()
        if api_status is not None:
            print(api_status)
        else:
            # 默认：工作日 计算自己需求
            print(0)

if __name__ == "__main__":
    main()
