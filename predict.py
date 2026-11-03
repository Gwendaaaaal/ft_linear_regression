import math
from linear_regression import estimate_price, load_parameters, normalize_value

def main() -> None:
    theta0, theta1, minimum, maximum = load_parameters()

    try:
        mileage = float(input("Enter the mileage of the car : "))
    except ValueError:
        print("Please enter a valid float.")
        return
    except EOFError:
        print("\nNo mileage provided.")
        return

    if not math.isfinite(mileage):
        print("Mileage must be finite.")
        return
    if mileage < 0:
        print("Mileage must be positive.")
        return

    if minimum != maximum:
        mileage = normalize_value(mileage, minimum, maximum)
    price = estimate_price(theta0, theta1, mileage)
    print(f"Estimated price = {price:.0f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
