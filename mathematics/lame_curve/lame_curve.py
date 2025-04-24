# 该程序解决如下问题:
# 闭合曲线C: x^{2n+2} + y^{2n+2} = 1, 对x, y进行弧长参数化(s), 取(1, 0)为起点, 逆时针方向为正方向.
# 求x(s), y(s)在s=0处的前m阶导数.

# 输入:
# n: C的参数, 当n=0时曲线退化为圆.
# m: 计算到前m阶导数(含第m阶). 值得注意的是, 如果要求x^{(n)}(0), 则必须求出x, y的所有前m-1阶s=0处导数.

# 输出:
# x, y的导数值列表, 从第零阶到第m阶.

import sympy as sp

def compute_derivatives(n, m):
    s = sp.symbols('s')
    x = sp.Function('x')(s)
    y = sp.Function('y')(s)
    
    # 定义隐式方程和弧长条件
    F = x**(2*n + 2) + y**(2*n + 2) - 1
    G = sp.diff(x, s)**2 + sp.diff(y, s)**2 - 1
    
    # 初始化导数值字典
    x_derivs = {0: 1}  # x(0) = 1
    y_derivs = {0: 0}  # y(0) = 0
    
    # 已知一阶导数（切向量模长为1）
    x_derivs[1] = 0
    y_derivs[1] = 1
    
    for k in range(2, m + 1):
        # 计算F的k阶导数并代入s=0
        F_k_expr = F.diff(s, k)
        F_k_at_0 = F_k_expr.subs(s, 0)
        
        # 代入已知的低阶导数值
        for var_derivs, var in [(x_derivs, x), (y_derivs, y)]:
            for d in range(0, k):
                deriv_expr = var.diff(s, d)
                value = var_derivs.get(d, 0)
                F_k_at_0 = F_k_at_0.subs(deriv_expr.subs(s, 0), value)
        
        # 计算G的(k-1)阶导数并代入s=0
        G_k_minus_1_expr = G.diff(s, k-1)
        G_k_minus_1_at_0 = G_k_minus_1_expr.subs(s, 0)
        
        # 代入已知的低阶导数值
        for var_derivs, var in [(x_derivs, x), (y_derivs, y)]:
            for d in range(0, k):
                deriv_expr = var.diff(s, d)
                value = var_derivs.get(d, 0)
                G_k_minus_1_at_0 = G_k_minus_1_at_0.subs(deriv_expr.subs(s, 0), value)
        
        # 定义当前求解的未知数（k阶导数在s=0处的值）
        unknowns = [
            x.diff(s, k).subs(s, 0),
            y.diff(s, k).subs(s, 0)
        ]
        
        # 解方程组
        try:
            sol = sp.solve([F_k_at_0, G_k_minus_1_at_0], unknowns)
        except:
            sol = None
        
        # 提取解的结果
        x_k_val = 0
        y_k_val = 0
        if sol:
            x_k_val = sol.get(unknowns[0], 0)
            y_k_val = sol.get(unknowns[1], 0)
        
        x_derivs[k] = x_k_val
        y_derivs[k] = y_k_val
    
    # 转换为整数列表
    result_x = [int(x_derivs.get(i, 0)) for i in range(m+1)]
    result_y = [int(y_derivs.get(i, 0)) for i in range(m+1)]
    
    return result_x, result_y

# 用户输入
n = int(input("请输入n的值："))
m = int(input("请输入m的值："))

x_derivatives, y_derivatives = compute_derivatives(n, m)

print("x的各阶导数值（从0阶到{}阶）：".format(m))
print(x_derivatives)
print("y的各阶导数值（从0阶到{}阶）：".format(m))
print(y_derivatives)