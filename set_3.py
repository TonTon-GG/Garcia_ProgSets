def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]['following']:
        if from_member in social_graph[to_member]['following']:
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph[to_member]['following']:
        return "followed by"
    else:
        return "no relationship"

def tic_tac_toe(board):
    size = len(board)
    for row in board:
        if all(symbol == row[0] and symbol != '' for symbol in row):
            return row[0]
    for col in range(size):
        if all(board[row][col] == board[0][col] and board[row][col] != '' for row in range(size)):
            return board[0][col]
    if all(board[i][i] == board[0][0] and board[i][i] != '' for i in range(size)):
        return board[0][0]
    if all(board[i][size - 1 - i] == board[0][size - 1] and board[i][size - 1 - i] != '' for i in range(size)):
        return board[0][size - 1]
    return "NO WINNER"

def eta(first_stop, second_stop, route_map):
    time_taken = 0
    current_stop = first_stop
    while True:
        for (start, end), leg in route_map.items():
            if start == current_stop:
                time_taken += leg['travel_time_mins']
                current_stop = end
                break
        if current_stop == second_stop:
            return time_taken