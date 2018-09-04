def knight_tour_backtracking(n):
    def backtracking_helper(board,x,y,move_i,moves):
        if move_i == len(board)*len(board):
            print(board)
            return True
        valid_positions = []
        max_id = len(board)
        for (delta_x,delta_y) in moves:
            if x+delta_x >= 0 and x+delta_x < max_id and y+delta_y >= 0 and y+delta_y < max_id:
                valid_positions.append((x+delta_x,y+delta_y))
        for (next_x,next_y) in valid_positions:
            if board[next_x][next_y] != -1:
                continue
            board[next_x][next_y] = move_i
            if backtracking_helper(board,next_x,next_y,move_i+1,moves):
                return True
            else:
                board[next_x][next_y] = -1
        return False
        

    board = []
    moves = [(1,2),(2,1),(-2,-1),(-1,-2),(2,-1),(1,-2),(-1,2),(-2,1)]
    for _ in range(n):
        board.append([-1]*n)
    board[0][0] = 0
    print(backtracking_helper(board,0,0,1,moves))

#knight_tour_backtracking(5)

# Choose the next position by the mininum number of possible plays in that new position
def knight_tour_Warnsdorff(n):
    def number_of_moves_from(x,y,board,moves):
        valid_positions = []
        max_id = len(board)
        for (delta_x,delta_y) in moves:
            if x+delta_x >= 0 and x+delta_x < max_id and y+delta_y >= 0 and y+delta_y < max_id:
                if board[x+delta_x][y+delta_y] == -1:
                    valid_positions.append((x+delta_x,y+delta_y))
        return len(valid_positions)

    board = []
    moves = [(1,2),(2,1),(-2,-1),(-1,-2),(2,-1),(1,-2),(-1,2),(-2,1)]
    for _ in range(n):
        board.append([-1]*n)
    board[0][0] = 0
    x = 0
    y = 0
    move_id = 1
    while move_id < n*n:
        next_pos = (-1,-1)
        number_moves_from_next = 9
        for (delta_x,delta_y) in moves:
            if x+delta_x >= 0 and x+delta_x < n and y+delta_y >= 0 and y+delta_y < n and board[x+delta_x][y+delta_y] == -1:
                n_moves = number_of_moves_from(x+delta_x,y+delta_y,board,moves)
                if n_moves < number_moves_from_next:
                    number_moves_from_next = n_moves
                    next_pos = (x+delta_x,y+delta_y)
        print(move_id,next_pos,board)
        if next_pos[0] != -1:
            x = next_pos[0]
            y = next_pos[1]
            board[x][y] = move_id
            move_id += 1
        else:
            print("No solution")
            return
    print(move_id)
    print(board)

knight_tour_Warnsdorff(5)