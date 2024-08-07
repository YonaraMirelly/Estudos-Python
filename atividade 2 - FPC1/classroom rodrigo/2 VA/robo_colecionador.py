class Robot:
    def __init__(self, arena, start_pos, start_dir):
        self.arena = arena
        self.pos = start_pos
        self.dir = start_dir
        self.figurines_collected = 0

    def move(self, instruction):
        if instruction == 'D':
            if self.dir == 'N':
                self.dir = 'L'
            elif self.dir == 'S':
                self.dir = 'O'
            elif self.dir == 'L':
                self.dir = 'S'
            elif self.dir == 'O':
                self.dir = 'N'
        elif instruction == 'E':
            if self.dir == 'N':
                self.dir = 'O'
            elif self.dir == 'S':
                self.dir = 'L'
            elif self.dir == 'L':
                self.dir = 'N'
            elif self.dir == 'O':
                self.dir = 'S'
        elif instruction == 'F':
            next_pos = self.get_next_position()
            if self.is_valid_move(next_pos):
                self.pos = next_pos
                if self.arena[self.pos[0]][self.pos[1]] == '*':
                    self.figurines_collected += 1

    def get_next_position(self):
        if self.dir == 'N':
            return (self.pos[0] - 1, self.pos[1])
        elif self.dir == 'S':
            return (self.pos[0] + 1, self.pos[1])
        elif self.dir == 'L':
            return (self.pos[0], self.pos[1] + 1)
        elif self.dir == 'O':
            return (self.pos[0], self.pos[1] - 1)

    def is_valid_move(self, next_pos):
        n, m = len(self.arena), len(self.arena[0])
        if next_pos[0] < 0 or next_pos[0] >= n or next_pos[1] < 0 or next_pos[1] >= m:
            return False
        if self.arena[next_pos[0]][next_pos[1]] == '#':
            return False
        return True

def collect_figurines():
    while True:
        n, m, s = map(int, input().split())
        if n == 0 and m == 0 and s == 0:
            break
        arena = []
        start_pos = None
        start_dir = None
        for i in range(n):
            row = input()
            arena.append(row)
            if 'N' in row:
                start_pos = (i, row.index('N'))
                start_dir = 'N'
            elif 'S' in row:
                start_pos = (i, row.index('S'))
                start_dir = 'S'
            elif 'L' in row:
                start_pos = (i, row.index('L'))
                start_dir = 'L'
            elif 'O' in row:
                start_pos = (i, row.index('O'))
                start_dir = 'O'
        instructions = input()
        robot = Robot(arena, start_pos, start_dir)
        for instruction in instructions:
            robot.move(instruction)
        print(robot.figurines_collected)

collect_figurines()