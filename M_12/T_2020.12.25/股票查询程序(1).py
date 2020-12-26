import re


stock_data = {
    # 'SH601778':['SH601778',N晶科,6.29,+1.92,+43.94%,+43.94%,259.66万,1625.52万,0.44%,22.32,-,173.95亿]
    # 'SH688566': [SH688566,吉贝尔,52.66,+6.96,+15.23%,+122.29%,1626.58万,8.09亿,42.29%,89.34,-,98.44亿]
}

f = open("stock_data.txt",encoding='UTF-8')
headers = f.readline().strip().split(",") # 表头存下来
for line in f:
    line = line.strip().split(",")
    stock_data[line[0]] = line

valid_filter_columns = ["当前价","涨跌幅","换手率"] #

while True:
    cmd = input("输入要查询的股票>").strip()
    if not cmd: continue
    # 先进行模糊查询
    print(headers)
    match_count = 0 # 计数器
    for sid,s_data in stock_data.items():
        s_name = s_data[1] # 拿到股票 名
        if cmd in s_name: # 如果成立，代表匹配上了
            print(s_data)
            match_count += 1


    # 进行公式查询 ， 当前价>50
    # step 1 把语法拆开， 折成2个值 。
    # step 2 ,验证每个变量的合法性，
    # step 3 ，取到要查询列的索引，然后真正的去循环dict的每行，
    # step 4, 拿到每行，要查询的列的值 ，进行>,or <判断。
    syntax_parser = re.split("[<>]",cmd) # 当前价>50
    if len(syntax_parser) == 2: # 代表语法基本合格, step1
        filter_col,filter_val = syntax_parser   # ['当前价', '50t']
        if filter_col in valid_filter_columns:  # step 2 ， 列名合法
            try:
                filter_val = float(filter_val) # '50t', 有可能报错。 。。。
                filter_column_index = headers.index(filter_col) # step 3 ,取到索引值
                for sid,s_data in stock_data.items():
                    real_col_val = float(s_data[filter_column_index].strip("%")) # step 4 , 拿到每行，要查询的列的值
                    if ">" in cmd: # 当前价>50
                        if real_col_val > filter_val: # 成立了， 代表匹配了
                            print(s_data)
                            match_count += 1
                    if "<" in cmd: # 当前价<50
                        if real_col_val < filter_val: # 成立了， 匹配
                            print(s_data)
                            match_count += 1
            except Exception as e:
                print("出错啦,",e)
    print(f"匹配到了\033[31;1m{match_count}\033[0m条数据.")






