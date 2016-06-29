# -*- coding: utf-8 -*-
class Island():
    """Island :n*n grid where zero value indicates an unoccupied cell."""
    def __init__(self, n):
        self.gridSize = n
        self.grid = []
        for i in range(n):
            row = [0] * n
            self.grid.append(row)

    def __str__(self):
        """string represention for printing.(0,0)will be in the lower-left corner"""
        s = ""
        for j in range(self.gridSize - 1, -1 , -1): #print row size-1 first
            for i in range(self.gridSize):
                if not self.grid[i][j]:
                    #print a '.' for an empty space
                    s += "%-2s" %'.' + "  "
                else:
                    s += "%-2s" %(str(self.grid[i][j])) + "  "
            s += "\n"
        return s


