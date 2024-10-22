def generateMatrix(n):
    # 初始化⼀个 n x n 的⼆维数组，填充为0
    nums = [[0] * n for _ in range(n)]
    startx, starty = 0, 0 # 起始坐标
    loop, mid = n // 2, n // 2 # loop为螺旋次数，mid为矩阵中⼼点（仅当n为奇数时使⽤）
    count = 1 # ⽤于填充矩阵的计数器
    # 外层循环控制螺旋的层数
    for offset in range(1, loop + 1):
        # 从左到右填充
        for i in range(starty, n - offset):
            nums[startx][i] = count
            count += 1
        # 从上到下填充
        for i in range(startx, n - offset):
            nums[i][n - offset] = count
            count += 1  
        # 从右到左填充
        for i in range(n - offset, starty, -1):
            nums[n - offset][i] = count
            count += 1
        # 从下到上填充
        for i in range(n - offset, startx, -1):
            nums[i][starty] = count
            count += 1
        # 更新起始点，进⼊下⼀层螺旋
        startx += 1
        starty += 1
        # 如果n为奇数，填充中⼼点
    if n % 2 != 0:
        nums[mid][mid] = count
    return nums
# 创建⼀个⾜够⼤的数组
array1 = [0]*7569
# 读取名为'spiral'的⼆进制⽂件
fr = open('spiral', 'rb').read()
# ⽣成⼀个87x87的螺旋矩阵，并将其展开为⼀维列表
s = sum(generateMatrix(87), [])
# 根据螺旋矩阵中的索引顺序重新排列原始⽂件的数据
for i in range(len(s)):
    array1[i] = fr[s[i]-1]
# 将处理后的数据写⼊到新的ZIP⽂件中
fw = open('flag.zip', 'wb')
for i in array1:
    fw.write(bytes([i]))
# 关闭⽂件
fw.close()