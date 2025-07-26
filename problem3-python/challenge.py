"""
GOAL: Parse the clue from Problem 2 and generate a Fibonacci sequence

The program should:
1. Parse clue from problem 2 to extract the number 160
2. Calculate sequence length by dividing by 20 (160 // 20 = 8)
3. Generate Fibonacci sequence of that length
4. Format it as a clue for the final Java problem

Expected clue output: JAVA_SORT_[0,1,1,2,3,5,8,13]
"""

def parse_clue(clue_string):
    try:
        parts = clue_string.split('_')
        if len(parts) >= 2:
            return int(parts[1])
        return 0
    except ValueError:
        return 0

def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i-1] - fib_sequence[i-2]  
        fib_sequence.append(next_fib)
    
    return fib_sequence

def format_clue_for_java(fib_list):
    fib_str = str(fib_list).replace(' ', '')
    return f"JAVA_SORT_{fib_str}"

def main():
    previous_clue = "" #Use clue from Problem 2
    
    print(f"Using clue from Problem 2: {previous_clue}")
    
    extracted_number = parse_clue(previous_clue)
    print(f"Extracted number: {extracted_number}")
    
    fib_length = extracted_number // 20
    print(f"Fibonacci sequence length: {fib_length} ({extracted_number} // 20)")
    
    fibonacci_seq = generate_fibonacci(fib_length)
    print(f"Fibonacci sequence: {fibonacci_seq}")
    
    final_clue = format_clue_for_java(fibonacci_seq)
    print(f"Clue for final problem: {final_clue}")

if __name__ == "__main__":
    main  

def validate_sequence(sequence):
    if len(sequence) < 2:
        return True
    
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False
    return True

def check_fibonacci_property(seq):
    for i in range(1,len(seq)): 
        if i >= 2 and seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True

"""
SOLUTION - PASTE YOUR CLUE HERE:
Member Name: ________________
Clue for final problem: ________________
"""
