class morpion():

    def __init__(self,player,finished):
        # 0 si case vide, 1 si player 1, 2 si player 2. 3 = erreur
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.player = player
        self.finished = finished

    def get_grid(self):
        return self.grid

    def get_case(self, x, y):
        return self.grid[x][y]

    def set_case(self, x, y, player):
        self.grid[x][y] = player


    def print_grid(self):
        print("\n"+str(self.grid[0])+"\n"+str(self.grid[1])+"\n"+str(self.grid[2])+"\npl:"+str(self.player)+"fin:"+str(self.finished))