from student_code import find_path

def test_maze_path_dfs():
    maze = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    path = find_path(maze, start, end)
    assert path[0] == start
    assert path[-1] == end
    assert all(maze[r][c] == 0 for r, c in path)
