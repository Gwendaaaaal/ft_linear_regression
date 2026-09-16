def load_parameters() -> tuple[float, float, float, float]:
    try:
        with open("parameters.txt", "r") as file:
            parameters = file.readline().split(",")
            theta0 = float(parameters[0])
            theta1 = float(parameters[1])
            minimum = float(parameters[2])
            maximum = float(parameters[3])
            return (theta0, theta1, minimum, maximum)
    except (FileNotFoundError, PermissionError):
        return (0.0, 0.0, 0.0, 0.0)

def save_parameters(theta0: float, theta1: float, minimum: float, maximum: float) -> None:
    with open("parameters.txt", "w") as file:
       file.write(str(theta0) + "," + str(theta1) + "," + str(minimum) + "," + str(maximum))

def normalize_value(mileage: float, minimum: float, maximum: float) -> float:
    return (mileage - minimum) / (maximum - minimum)

def estimate_price(theta0: float, theta1: float, mileage: float) -> float:
    return theta0 + theta1 * mileage

def compute_rmse(mileages: list[float], prices: list[float], theta0: float, theta1: float, minimum: float, maximum: float) -> float:
    squared_errors = 0.0

    for mileage, price in zip(mileages, prices):
        normalized_mileage = normalize_value(mileage, minimum, maximum)
        estimate = estimate_price(theta0, theta1, normalized_mileage)
        squared_errors += (estimate - price) ** 2

    return (squared_errors / len(mileages)) ** 0.5
