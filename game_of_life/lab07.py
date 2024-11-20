import time
from typing import List, Tuple, Generator

class Life:
    state: List[List[bool]]
    m: int
    n: int

    def __init__(self, m: int, n: int):
        self.state = [[False for _ in range(n)] for _ in range(m)]  # Using list comprehension
        self.m = m
        self.n = n

    def __repr__(self) -> str:
        return str(self.state)

    def neighbours(self, i: int, j: int) -> Generator[Tuple[int, int], None, None]:
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if 0 <= x < self.m and 0 <= y < self.n and (x, y) != (i, j):
                    yield (x, y)

    def nextstate(self) -> None:
        next_state = [[False for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                live_neighbors = sum(self.state[x][y] for x, y in self.neighbours(i, j))
                if self.state[i][j]:
                    if live_neighbors in (2, 3):
                        next_state[i][j] = True
                else:
                    if live_neighbors == 3:
                        next_state[i][j] = True
        self.state = next_state

    def addfigure(self, i: int, j: int, figure: List[str]) -> None:
        if i < 0 or j < 0:
            raise ValueError("Invalid position")
        for k, row in enumerate(figure):
            for l, cell in enumerate(row):
                if k + i >= self.m or l + j >= self.n:
                    raise ValueError("Figure out of bounds")
                self.state[k + i][l + j] = cell != ' ' and cell != '.'

    def __str__(self) -> str:
        return '\n'.join(''.join('#' if cell else '.' for cell in row) for row in self.state)

def tester():
    lf = Life(4, 5)
    for pnt in lf.neighbours(2, 3):
        print(pnt)

def start():
    toad = [".###",
            "###."]
    blinker = ["###"]
    block = ["..##..",
             "..##.."]
    glidergun = ["...................................#............",
                 ".................................#.#............",
                 ".......................##......##............##.",
                 "......................#...#....##............##.",
                 "...........##........#.....#...##...............",
                 "...........##........#...#.##....#.#............",
                 ".....................#.....#.......#............",
                 "......................#...#.....................",
                 ".......................##......................." ]
    lf = Life(50, 80)
    lf.addfigure(10, 10, glidergun)
    lf.addfigure(30, 10, toad)
    lf.addfigure(40, 15, blinker)

    while True:
        print(lf)
        print("Press Ctrl-C to stop")
        lf.nextstate()
        time.sleep(0.25)

if __name__ == "__main__":
    start()