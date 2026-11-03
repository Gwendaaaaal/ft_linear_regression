from linear_regression import estimate_price, load_parameters, normalize_value

def main() -> None:
    theta0, theta1, minimum, maximum = load_parameters()
    try:
        mileage = float(input("Enter the mileage of the car : "))
    except:
        print("Please enter a valid float.")
        return(None)

    if minimum != maximum:
        mileage = normalize_value(mileage, minimum, maximum)
    
    price = estimate_price(theta0, theta1, mileage)

    print(f"Estimated price = {price}")

if __name__ == "__main__":
    main()
