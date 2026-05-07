import math


def minimax(depth, nodeIndex, maximizingPlayer, values, alpha=-math.inf, beta=math.inf):
    
    
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = -math.inf

        
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        
        for i in range(2):
            val = minimax(depth + 1, nodeIndex * 2 + i,
                          True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

        
            if beta <= alpha:
                break

        return best
result = minimax(0, 0, True, values)

print("Optimal value:", result)