def min_watering_points(grid_size, plant_positions):
    from collections import defaultdict, deque
    
    M, N = grid_size
    plant_positions_set = set(plant_positions)
    
    # A function to find neighbors (adjacent plants)
    def get_neighbors(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and (nx, ny) in plant_positions_set:
                neighbors.append((nx, ny))
        return neighbors
    
    # Use BFS to cover all plants
    def bfs_cover():
        visited = set()
        cover_count = 0
        
        for plant in plant_positions:
            if plant not in visited:
                cover_count += 1
                queue = deque([plant])
                while queue:
                    px, py = queue.popleft()
                    if (px, py) in visited:
                        continue
                    visited.add((px, py))
                    for neighbor in get_neighbors(px, py):
                        if neighbor not in visited:
                            queue.append(neighbor)
        
        return cover_count
    
    return bfs_cover()

# Read input
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        M = int(data[idx])
        N = int(data[idx + 1])
        K = int(data[idx + 2])
        idx += 3
        
        plant_positions = []
        for _ in range(K):
            x = int(data[idx])
            y = int(data[idx + 1])
            plant_positions.append((x, y))
            idx += 2
        
        result = min_watering_points((M, N), plant_positions)
        results.append(result)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()