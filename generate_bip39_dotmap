def int_to_reversed_bin(index, bits=11):
    # 将索引转为11位二进制，并反转低位→高位
    bin_str = format(index, f'0{bits}b')
    reversed_bin = bin_str[::-1]  # 反转字符串
    return reversed_bin

# 加载BIP-39词表（需提前下载english.txt）
with open("english.txt", "r") as f:
    words = f.read().splitlines()

# 生成词表（索引0~2047）
with open("bip39_reversed_binary.txt", "w") as f:
    for index in range(2048):
        reversed_bin = int_to_reversed_bin(index)
        word = words[index]
        f.write(f"{index:04} {reversed_bin} {word}\n")
