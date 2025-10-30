def add(a, b):
    """计算两个数字的和"""
    return a + b

def multiply(a, b):
    """计算两个数字的乘积"""
    return a * b

# 测试代码
if __name__ == "__main__":
    print("工具模块测试:")
    print(f"3 + 4 = {add(3, 4)}")
    print(f"3 * 4 = {multiply(3, 4)}")