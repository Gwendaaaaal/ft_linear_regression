# ft_linear_regression

A 42 introductory machine-learning project implementing univariate linear regression from first principles.

## Objective

Estimate a car's price from its mileage using:

```text
estimated_price(mileage) = θ₀ + θ₁ × mileage
```

The parameters `θ₀` and `θ₁` are learned from the supplied dataset using gradient descent, without using a library routine to perform the regression.

## Setup

Clone the repository and enter it:

```bash
git clone https://github.com/Gwendaaaaal/ft_linear_regression.git
cd ft_linear_regression
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

To leave the virtual environment:

```bash
deactivate
```

When coming back to the project later, reactivate it with:

```bash
source .venv/bin/activate
```

## Usage

### Train the model

```bash
python train.py
```

The training program:

- reads the supplied dataset;
- normalizes mileage values;
- learns `θ₀` and `θ₁` using gradient descent;
- reports the final RMSE;
- saves the learned parameters and normalization values to `parameters.txt`.

### Predict a price

```bash
python predict.py
```

Enter a mileage when prompted. The program loads the saved parameters, normalizes the input using the same values used during training, and prints the estimated price.

Before the model has been trained, the prediction parameters default to zero.

## Dataset

`data.csv` contains 24 observations with two columns:

| Column | Meaning | Range |
| --- | --- | ---: |
| `km` | Car mileage in kilometres | 22,899–240,000 |
| `price` | Car price | 3,650–8,290 |

## Implementation

The project currently includes:

- CSV parsing;
- min-max normalization;
- gradient descent;
- parameter persistence;
- price prediction;
- cost tracking;
- RMSE evaluation;
- visualization of the dataset and fitted regression line.

The regression itself is implemented manually rather than through a machine-learning library.

## Project structure

```text
.
├── data.csv
├── en.subject.pdf
├── linear_regression.py
├── predict.py
├── train.py
├── requirements.txt
└── README.md
```

`parameters.txt` is generated after training.
