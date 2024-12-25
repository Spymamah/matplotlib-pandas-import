import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y) 
plt.xlabel('Angle')
plt.ylabel('Sin Value')
plt.title('Sine wave')
plt.show()

x = np.linspace(0, 10,)
# fig = plt.figure()

# Add a custom axis to the figure
# [left, bottom, width, height] in relative figure dimensions (0 to 1)
# ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
# languages = ["french", "english", "portuguese", "german", "igbo"]
# people = [100, 10, 50, 120, 70]
# ax.bar(languages, people)
# plt.xlabel("languages")
# plt.ylabel("people")
# plt.title("I am not sure what i am doing")
# plt.show()

fig = plt.figure()

#Add a custom axis to the figure
#[left, bottom, width, height] in relative figure dimensions (0 to 1)
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
languages = ["french", "english", "portuguese", "german", "igbo"]
people = [100, 10, 50, 120, 70]

ax.pie(people, labels=languages, autopct='%1.1f%%', startangle=90, explode=[0, 0, 0.1, 0, 0] )
plt.show()
