import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的大小
    plt.figure(dpi=128,figsize=(10,6))

    #隐藏坐标轴,书上的存在问题，如下使用是可行的，注意代码需要在画图前
    current_axes = plt.axes()
    current_axes.xaxis.set_visible(False)
    current_axes.yaxis.set_visible(False)

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,s=1)

    plt.scatter(0,0,c='green',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)



    plt.show()

    keep_running = input("Make another walk (y/n):")
    if keep_running == 'n':
        break
