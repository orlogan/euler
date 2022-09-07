from euler import problemTwo as p


def test_evenFib(benchmark):
    total = benchmark(p.evenFib, 4000000)
    assert total == 4613732
