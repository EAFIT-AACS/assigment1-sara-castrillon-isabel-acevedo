

def parse_input():
    cases = []
    
    line = input().strip()
    c = int(line)  
    
    for _ in range(c):
        n = int(input().strip()) 
        
        
        alphabet = input().strip().split()
        final_states = set(map(int, input().strip().split()))
        
        transition_table = [None] * n
        for _ in range(n):
            row = input().strip().split()
            if len(row) != len(alphabet) + 1:
                raise ValueError("Error: la fila de transiciones no coincide con el tamaño del alfabeto + 1.")
            
            state_id = int(row[0])
            destinations = list(map(int, row[1:]))
            transition_table[state_id] = destinations
        
        cases.append((n, alphabet, final_states, transition_table))
    
    return cases

def initialize_mark_table(n, final_states):
    table = [[False] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if (i in final_states) != (j in final_states):
                table[i][j] = True
    return table
def fill_mark_table(n, alphabet, transition_table, table):
    changed = True
    while changed:
        changed = False
        for i in range(n):
            for j in range(i + 1, n):
                if not table[i][j]:
                    
                    for symbol_index in range(len(alphabet)):
                        next_i = transition_table[i][symbol_index]
                        next_j = transition_table[j][symbol_index]
                        
                       
                        if next_i > next_j:
                            next_i, next_j = next_j, next_i
                        
                        
                        if next_i != next_j and table[next_i][next_j]:
                            table[i][j] = True
                            changed = True
                            break

def get_equivalent_pairs(n, table):
    equivalent_pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if not table[i][j]:
                equivalent_pairs.append((i, j))
    return equivalent_pairs

def main():
    
    cases = parse_input()
    
    
    results = []
    for n, alphabet, final_states, transition_table in cases:
        table = initialize_mark_table(n, final_states)
        
        fill_mark_table(n, alphabet, transition_table, table)
        
        eq_pairs = get_equivalent_pairs(n, table)
        if eq_pairs:
            line = " ".join(f"({i}, {j})" for i, j in eq_pairs)
        else:
            line = ""
        
        results.append(line)
    
    
    for line in results:
        print(line)

if __name__ == "__main__":
    main()
