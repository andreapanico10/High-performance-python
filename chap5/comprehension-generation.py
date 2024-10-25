from iterator import fibonacci_gen

divisible_by_three = len([n for n in fibonacci_gen(100_000) if n % 3 == 0])
divisible_by_three = sum(1 for n in fibonacci_gen(100_000) if n % 3 == 0)

