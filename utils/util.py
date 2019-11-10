import itertools


class Subsample:
    def __init__(self, set, subsize):
        self.set = set
        self.len = int(len(set)*subsize)

    def __iter__(self):
        return itertools.islice(self.set, self.len)

    def __len__(self):
        return self.len
