from utils import add, multiply

def main():
    print("=== 我的Git实践项目 ===")
    
    # 使用工具函数进行计算
    num1 = 10
    num2 = 5
    
    result1 = add(num1, num2)
    result2 = multiply(num1, num2)
    
    print(f"{num1} + {num2} = {result1}")
    print(f"{num1} * {num2} = {result2}")
    print("程序执行完成！")

if __name__ == "__main__":
    main()