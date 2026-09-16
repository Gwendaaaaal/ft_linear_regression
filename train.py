from linear_regression import estimate_price, normalize_value, save_parameters, compute_rmse
import matplotlib.pyplot as plt


def parse_csv() -> tuple[list[float], list[float]]:
    mileages = []
    prices = []
    with open("data.csv", "r") as file:
        next(file)
        for line in file:
            split = line.split(",")
            mileages.append(float(split[0]))
            prices.append(float(split[1]))

    return (mileages, prices)

def train(mileages: list[float], prices: list[float]) -> tuple[float, float, float, float]:
    theta0 = 0.0
    theta1 = 0.0
    learning_rate = 0.1
    iterations = 5000
    maximum = max(mileages)
    minimum = min(mileages)

    for _ in range(iterations):
        gradient_theta0 = 0.0
        gradient_theta1 = 0.0

        for mileage, price in zip(mileages, prices):
            mileage = normalize_value(mileage, minimum, maximum)
            estimate = estimate_price(theta0, theta1, mileage)
            error = estimate - price
            gradient_theta0 += error
            gradient_theta1 += error * mileage


        gradient_theta0 /= len(mileages)
        gradient_theta1 /= len(mileages)
        theta0 -= learning_rate * gradient_theta0
        theta1 -= learning_rate * gradient_theta1

    return (theta0, theta1, minimum, maximum)

def plot_regression(mileages: list[float], prices: list[float], theta0: float, theta1: float, minimum: float, maximum: float) -> None:
    sorted_mileages = sorted(mileages)
    predicted_prices = []

    for mileage in sorted_mileages:
        normalized_mileage = normalize_value(
            mileage,
            minimum,
            maximum,
        )

        predicted_prices.append(
            estimate_price(
                theta0,
                theta1,
                normalized_mileage,
            )
        )

    plt.scatter(mileages, prices)
    plt.plot(sorted_mileages, predicted_prices)

    plt.xlabel("Mileage")
    plt.ylabel("Price")
    plt.title("Linear Regression")

    plt.savefig("regression.png", dpi=150, bbox_inches="tight")

def main() -> None:
    mileages, prices = parse_csv()
    theta0, theta1, minimum, maximum = train(mileages, prices)
    save_parameters(theta0, theta1, minimum, maximum)
    rmse = compute_rmse(mileages, prices, theta0, theta1, minimum, maximum)
    plot_regression(mileages, prices, theta0, theta1, minimum, maximum)

    print(f"RMSE: {rmse:.2f} €")

if __name__ == "__main__":
    main()
