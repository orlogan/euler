from euler import problemOne as p


def test_multiples(benchmark):
    benchmark(p.multiples, 1000)
    assert p.multiples(10) == 23
    assert p.multiples(1000) == 233168
