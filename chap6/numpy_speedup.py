import numpy as np
from array import array

# python -m timeit -s "from numpy_speedup import norm_square_list; vector = list(range(1_000_000))" "norm_square_list(vector)"
def norm_square_list(vector):
    """
    >>> vector = list(range(1_000_000))
    >>> %timeit norm_square_list(vector)
    36.6 ms
    """
    norm = 0
    for v in vector:
        norm += v 

# python -m timeit -s "from numpy_speedup import norm_square_list_comprehension; vector = list(range(1_000_000))" "norm_square_list_comprehension(vector)"
def norm_square_list_comprehension(vector):
    """
    >>> vector = list(range(1_000_000))
    >>> %timeit norm_square_list_comprehension(vector)
    86.2 ms
    """
    return sum([v * v for v in vector])

# python -m timeit -s "from numpy_speedup import norm_square_array; from array import array; vector = array('l', range(1_000_000))" "norm_square_array(vector)"
def norm_square_array(vector):
    """
    >>> vector_array = array('l', range(1_000_000))
    >>> %timeit norm_square_array(vector_array)
    66.9 ms 
    """
    norm = 0
    for v in vector:
        norm += v * v
    return norm

# python -m timeit -s "from numpy_speedup import norm_square_numpy; import numpy as np; vector = np.arange(1_000_000)" "norm_square_numpy(vector)"
def norm_square_numpy(vector):
    """
    >>> vector_np = numpy.arange(1_000_000)
    >>> %timeit norm_square_numpy(vector_np)
    1.56 ms
    """
    return np.sum(vector * vector) 

# python -m timeit -s "from numpy_speedup import norm_square_numpy_dot; import numpy as np; vector = np.arange(1_000_000)" "norm_square_numpy_dot(vector)"
def norm_square_numpy_dot(vector):
    """
    >>> vector_np = numpy.arange(1_000_000)
    >>> %timeit norm_square_numpy_dot(vector_np)
    462 µs ± 41.1 µs
    """
    return np.dot(vector, vector) 