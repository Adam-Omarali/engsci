import numpy as np


# Printing matrices using NumPy:

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
print(M)




#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)        

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]

# To obtain a list of lists from the array M, we use .tolist()
M_listoflists = M.tolist() 

print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

def print_matrix(M_lol):
    print(np.array(M_lol, dtype=float))

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

def get_row_to_swap(M, start_i):
    min_lead_idx = get_lead_ind(M[start_i])
    row_to_swap = start_i
    lead_idx_at_swap = min_lead_idx
    for row in range(start_i + 1, len(M)):
        curr_lead_idx = get_lead_ind(M[row])
        #if the leading zero of this row is smaller
        #(more to the left), then swap it
        if curr_lead_idx < lead_idx_at_swap:
            row_to_swap = row
            lead_idx_at_swap = curr_lead_idx
    
    return row_to_swap

def add_rows_coefs(r1, c1, r2, c2):
    ret = [0] * len(r1)
    for i in range(len(r1)):
        ret[i] = r1[i] * c1 + r2[i] * c2
    return ret
        
def eliminate(M, row_to_sub, best_lead_ind):
    val = M[row_to_sub][best_lead_ind]
    for i in range(row_to_sub + 1, len(M[0]) - 1):
        #val * x + to_elim = 0
        #x = -to_elim / val
        row_value_to_elimintate = M[i][best_lead_ind]
        c =  - row_value_to_elimintate / val
        print("Adding ", c, "* row", row_to_sub)
        new_row = add_rows_coefs(M[row_to_sub], c, M[i], 1)
        M[i] = new_row
    
    return M

def eliminate_backward(M, row_to_sub, best_lead_ind):
    val = M[row_to_sub][best_lead_ind]
    for i in range(row_to_sub - 1, -1, -1):
        row_value_to_elimintate = M[i][best_lead_ind]
        c =  - row_value_to_elimintate / val
        print("Adding ", c, "* row", row_to_sub)
        new_row = add_rows_coefs(M[row_to_sub], c, M[i], 1)
        M[i] = new_row
    
    return M

def divide_by_lead(M):
    for i in range(len(M)):
        lead_idx = M[i][get_lead_ind(M[i])]
        if (lead_idx != 0):
            for col in range(len(M[0])):
                M[i][col] /= lead_idx
    return M
        
def forward_step(M):
    for row in range(len(M)):
        row_to_swap = get_row_to_swap(M, row)
        print("Swapping row:", row, "with", row_to_swap)
        M[row], M[row_to_swap] = M[row_to_swap], M[row]
        M = eliminate(M, row, get_lead_ind(M[row]))
        print_matrix(M)
        #put into upper triangular matrix

    
    return M

def backward_step(M):
    for row in range(len(M) - 1, 0, -1):
        M = eliminate_backward(M, row, get_lead_ind(M[row]))
        print_matrix(M)
    
    return M

def solve(M, b):
    M = M.tolist()
    matrix = [0] * len(b)
    for i in range(len(M)):
        row = M[i]
        row.append(b[i])
        matrix[i] = row
    
    matrix = forward_step(matrix)
    matrix = backward_step(matrix)
    matrix = divide_by_lead(matrix)
    return matrix
        


print_matrix(M_listoflists)
print(get_lead_ind(M_listoflists[0])) #0

M = [[5, 6, 7, 8],
[0, 0, 0, 1],
[0, 0, 5, 2],
[0, 1, 0, 0]]
print(get_row_to_swap(M, 1)) #3
print(add_rows_coefs([1, 2], 1, [1, 2], 1)) #2, 4
M = [[5, 6, 7, 8],
[0,0, 1, 1],
[0, 0, 5, 2],
[0, 0, 7, 0]]
print_matrix(eliminate(M, 1, 2))

M = [[ 0, 0, 1, 0, 2],
[ 1, 0, 2, 3, 4],
[ 3, 0, 4, 2, 1],
[ 1, 0, 1, 1, 2]]

forward_step(M)

M = [[ 1, -2, 3, 22],
[ 3, 10, 1, 314],
[ 1, 5, 3, 92]]
M = forward_step(M)
print("backward step")
M = backward_step(M)
M = divide_by_lead(M)
print_matrix(M)
print("Test Solve")
#Compute M*x for matrix M and vector x by using
#dot. To do that, we need to obtain arrays
#M and x
M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
x = np.array([75,10,-11])
b = np.matmul(M,x)        

print(M)
#[[ 1 -2  3]
# [ 3 10  1]
# [ 1  5  3]]
print_matrix(solve(M, b))