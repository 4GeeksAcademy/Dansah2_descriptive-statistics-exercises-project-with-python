def calc_st_dev(data: list) -> float:
    """
    Calculates the standard deviation of a list of numbers

    Parameters: list of numbers

    Returns: floating point number

    Raises: Type error if a list of numbers is not passed to the function
    """

    if not isinstance(data, list):
        print("You must pass this fuction a list of numbers")

    if not all(isinstance(item, (int, float)) for item in data):
        print("The list contains non-number elements")

    # calculate the mean
    n = len(data)
    mean = sum(data)/n

    # calculate the variance
    var = sum ((x-mean)** 2 for x in data) / (n-1)

    # calculate the standard deviation
    st_dev = var ** 0.5

    return st_dev
