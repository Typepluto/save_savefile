import types


def add_count(count=0):
    while True:
        yield count
        count += 1


def coded_gen(fuc):
    while True:
        if isinstance(fuc, types.GeneratorType):
            yield from fuc
        else:
            yield fuc
