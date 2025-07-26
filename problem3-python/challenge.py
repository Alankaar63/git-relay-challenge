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
        next_fib = fib_sequence[i-1] + fib_sequence[i-2]  # Corrected here
        fib_sequence.append(next_fib)
    
    return fib_sequence

def format_clue_for_java(fib_list):
    fib_str = str(fib_list).replace(' ', '')
    return f"JAVA_SORT_{fib_str}"

def main():
    previous_clue = "CLUE_160"
    
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
    main()


def validate_sequence(sequence):
    if len(sequence) < 2:
        return True
    for i in range(2, len(sequence)):
        if sequence[i] != sequence[i-1] + sequence[i-2]:
            return False
    return True

def check_fibonacci_property(seq):
    for i in range(2, len(seq)):
        if seq[i] != seq[i-1] + seq[i-2]:
            return False
    return True