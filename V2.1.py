import sys
from collections import defaultdict

def main():
    # 读取所有输入行
    data = sys.stdin.read().splitlines()
    
    codes = []
    for line in data:
        # 去除首尾空格及花括号后，再过滤空行
        code = line.strip().lstrip('{').rstrip('}').strip()
        if code:
            codes.append(code)
    
    # 统计兑换码出现次数
    count = defaultdict(int)
    for code in codes:
        count[code] += 1
    
    # 提取重复项
    duplicates = {code: cnt for code, cnt in count.items() if cnt > 1}
    
    # 输出结果
    if duplicates:
        print("发现以下重复的兑换码：")
        for code, cnt in duplicates.items():
            print(f"{code} （出现次数：{cnt}）")
    else:
        print("没有发现重复的兑换码。")

if __name__ == "__main__":
    main()