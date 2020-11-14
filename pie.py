"""
Relevant pie chart generator.
"""
import matplotlib.pyplot as plt

win_wins = .66
mac_wins = .3
lin_wins = 1 - win_wins - mac_wins

plt.pie(
    [win_wins, mac_wins, lin_wins, 0],
    labels=['Windows', 'Mac', 'Linux', 'You'],
    colors=['cornflowerblue', 'salmon', 'palegreen', 'gold'],
)
plt.title("Winning Players")
plt.legend(bbox_to_anchor=(1, 1))
plt.show()
