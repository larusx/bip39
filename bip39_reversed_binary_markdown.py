def int_to_reversed_bin(index, bits=11):
    # 将索引转为11位二进制，并反转低位→高位
    bin_str = format(index, f'0{bits}b')
    reversed_bin = bin_str[::-1]  # 反转字符串
    return reversed_bin

# 加载BIP-39词表（需提前下载english.txt）
with open("english.txt", "r") as f:
    words = f.read().splitlines()

# 生成Markdown表格
with open("bip39_reversed_binary_markdown_table.txt", "w") as f:
    # 写入Markdown表格的表头
    f.write("| 索引  | 反转二进制值（图形化）       | 单词     |\n")
    f.write("|-------|------------------------------|----------|\n")
    
    # 生成词表（索引0~2047）
    for index in range(2048):
        reversed_bin = int_to_reversed_bin(index)
        
        # 将1替换为●，0替换为○
        graphic_bin = ''.join(['●' if bit == '1' else '○' for bit in reversed_bin])
        
        word = words[index]
        
        # 写入每一行数据
        f.write(f"| {index:04} | {graphic_bin} | {word} |\n")
