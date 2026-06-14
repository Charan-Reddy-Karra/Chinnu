from engines.rs.score import calculate_rs_score

tests = [
    (10, 5),
    (20, 10),
    (35, 5),
    (5, 10)
]

for stock, benchmark in tests:

    score = calculate_rs_score(
        stock,
        benchmark
    )

    print(
        stock,
        benchmark,
        score
    )
