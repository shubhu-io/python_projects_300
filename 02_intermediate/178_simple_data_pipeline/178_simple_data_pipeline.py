"""
Project 178: Simple Data Pipeline
Category: Database & Storage
Description: Cellular automaton grid simulation computing state evolution over discrete time steps.
"""

class LifeGridSimulator178:
    def __init__(self, rows=6, cols=10):
        self.rows = rows
        self.cols = cols
        self.grid = [[0]*cols for _ in range(rows)]
        # Seed glider pattern
        self.grid[1][2] = 1
        self.grid[2][3] = 1
        self.grid[3][1] = 1
        self.grid[3][2] = 1
        self.grid[3][3] = 1

    def count_neighbors(self, r, c):
        cnt = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0: continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    cnt += self.grid[nr][nc]
        return cnt

    def step(self):
        new_grid = [[0]*self.cols for _ in range(self.rows)]
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = sum(
                    self.grid[nr][nc]
                    for dr in [-1,0,1] for dc in [-1,0,1]
                    if (dr != 0 or dc != 0) and 0 <= (nr:=r+dr) < self.rows and 0 <= (nc:=c+dc) < self.cols
                )
                if self.grid[r][c] == 1 and neighbors in [2, 3]:
                    new_grid[r][c] = 1
                elif self.grid[r][c] == 0 and neighbors == 3:
                    new_grid[r][c] = 1
        self.grid = new_grid

    def render(self):
        lines = []
        for row in self.grid:
            lines.append(" ".join("█" if cell else "." for cell in row))
        return "\n".join(lines)

def run_project_178():
    print("=" * 45)
    print("   PYTHON PROJECT 178: SIMPLE DATA PIPELINE")
    print("=" * 45)
    
    sim = LifeGridSimulator178()
    print("Initial Grid State (Step 0):")
    print(sim.render())
    
    sim.step()
    print("\nEvolved Grid State (Step 1):")
    print(sim.render())
    return True

if __name__ == "__main__":
    run_project_178()
