from modal import Stub

stub = Stub()


@stub.function()
def foo():
    pass  # not actually used in test (servicer returns sum of square of all args)


def test_run_function(client):
    with stub.run(client=client):
        assert foo(2, 4) == 20


def test_map(client):
    stub = Stub()

    @stub.function
    def dummy():
        pass  # not actually used in test (servicer returns sum of square of all args)

    with stub.run(client=client):
        assert list(dummy.map([5, 2], [4, 3])) == [41, 13]


def test_map_none_values(client, servicer):
    stub = Stub()

    @stub.function
    @servicer.function_body
    def custom_function(x):
        if x % 2 == 0:
            return x

    with stub.run(client=client):
        assert list(custom_function.map(range(4))) == [0, None, 2, None]


def test_starmap(client):
    stub = Stub()

    @stub.function
    def dummy():
        pass  # not actually used in test (servicer returns sum of square of all args)

    with stub.run(client=client):
        assert list(dummy.starmap([[5, 2], [4, 3]])) == [29, 25]


def test_function_memory_request(client):
    stub = Stub()

    @stub.function(memory=2048)
    def f1():
        pass
