def check_duplicate_codes(file_path):
    # 读取文件内容
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    code_dict = {}
    # 遍历每一行并记录原始行号
    for line_num, line in enumerate(lines, start=1):
        stripped_line = line.strip()
        if stripped_line:  # 忽略空行
            if stripped_line in code_dict:
                code_dict[stripped_line].append(line_num)
            else:
                code_dict[stripped_line] = [line_num]
    
    # 筛选出重复的兑换码
    duplicates = {code: line_nums for code, line_nums in code_dict.items() if len(line_nums) > 1}
    
    # 输出结果
    if duplicates:
        print("发现以下重复的兑换码：")
        for code, line_nums in duplicates.items():
            print(f"兑换码: {code}")
            print(f"重复行号: {', '.join(map(str, line_nums))}\n")
    else:
        print("未发现重复的兑换码。")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("使用方法: python check_codes.py <文件路径>")
    else:
        check_duplicate_codes(sys.argv[1])