# autoclock
个人专属节假日加班调休判断；
0，on；
1，off
时间格式：2025-05-19

name: 智能打卡系统
on: 
  schedule: 
    - cron: '0 0,8 * * *'  # 每天早8点,16点自动运行（北京时间）
  push:                   # 文件修改实时生效

jobs:
  check:
    runs-on: ubuntu-latest
    env:
      TZ: Asia/Shanghai   # 中国时区
    steps:
    - uses: actions/checkout@v4
    
    - name: 生成状态
      run: |
        # 获取今日日期
        TODAY=$(date +"%Y-%m-%d")
        
        # 检查特殊日期（最高优先级）
        if grep -q "^$TODAY$" duty || grep -q "^$TODAY$" leave; then
          echo 1 > status
          exit 0
        fi

        # 调用节假日接口
        RESULT=$(curl -s "https://yasumi.neko7ina.com/")
        echo $RESULT > status  # 直接传递接口值

    - uses: stefanzweifel/git-auto-commit-action@v5
      with:
        commit_message: "系统自动更新"
