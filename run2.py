import sys
import collections

keys_char = [chr(i) for i in range(ord('a'), ord('z') + 1)]
doors_char = [k.upper() for k in keys_char]

def get_input():
    """Чтение данных из стандартного ввода."""
    return [list(line.strip()) for line in sys.stdin]

def solve(data):
    rows = len(data)
    cols = len(data[0])
    robot_positions = []
    key_positions = {}
    
    
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == '@':
                robot_positions.append((r, c))
            elif data[r][c] in keys_char:
                key_positions[data[r][c]] = (r, c)

    num_robots = len(robot_positions)
    all_keys = len(key_positions)
    
    
    queue = collections.deque()
    visited_cell = set()
    

    queue.append((robot_positions, 0, 0))  
    visited_cell.add((tuple(robot_positions), 0))

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_robots, keys_doors, steps = queue.popleft()

         
        if keys_doors == (1 << all_keys) - 1:
            return steps

        for i in range(num_robots):
            r, c = current_robots[i]
            
            for dr, dc in direction:   
                nr = r + dr
                nc = c + dc
                
                 
                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue
                
                if data[nr][nc] == '#':
                    continue   

                new_keys_doors = keys_doors
                
                if data[nr][nc] in keys_char:
                    new_keys_doors |= (1 << keys_char.index(data[nr][nc]))   
                elif data[nr][nc] in doors_char:
                     
                    if not (keys_doors & (1 << keys_char.index(data[nr][nc].lower()))):
                        continue

                 
                new_robot_positions = list(current_robots)
                new_robot_positions[i] = (nr, nc)
                new_robot_positions_tuple = tuple(new_robot_positions)

                 
                if (new_robot_positions_tuple, new_keys_doors) not in visited_cell:
                    visited_cell.add((new_robot_positions_tuple, new_keys_doors))
                    queue.append((new_robot_positions, new_keys_doors, steps + 1))

    return -5  # Если не удалось собрать все ключи

def main():
    data = get_input()
    result = solve(data)
    print(result)

if __name__ == '__main__':
    main()
