from die import Die
import pygal

die_1 = Die()
die_2 = Die()

list_range=[]

for i in list(range(1,7)):
    for j in list(range(1,7)):
        if(i*j) not in list_range:
            list_range.append(i*j)

#掷几次骰子，并且把结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)


frequencies = []
for value in list_range:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(len(results))
print(frequencies)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of mutiling two D6 1000 times."
hist.x_labels = list_range
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6',frequencies)
hist.render_to_file('mutil_dice_visual.svg')