class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count = [colors.count('A'), colors.count('B')]
        players = [0, 0]
        for i in range(len(colors)-2):
            if (colors[i] == colors[i+1] == colors[i+2]):   
                players[colors[i] == 'B'] += 1
                # if there is more than a 270 piece gap then break -- used to beat 100% of python users on LeetCode :) but definitely cheating
                # if abs(count[colors[i] == 'B'] - count[colors[i] != 'B']) > 270:
                    # break
        return players[0] > players[1]
