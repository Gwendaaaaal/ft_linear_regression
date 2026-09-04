# ft_linear_regression

A 42 introductory machine-learning project for implementing univariate linear regression from first principles.

## Objective

Estimate a car's price from its mileage using:

```text
estimated_price(mileage) = θ₀ + θ₁ × mileage
```

The parameters `θ₀` and `θ₁` must be learned from the supplied data with gradient descent rather than a library routine that performs the regression.

## Repository status

This snapshot contains only:

- `data.csv` — supplied training data
- `en.subject.pdf` — project requirements (version 4.1)
- `README.md` — this overview

No training or prediction program, saved parameters, tests, plots, or accuracy tool is currently implemented.

## Dataset

`data.csv` has 24 complete observations and two integer columns:

| Column | Meaning | Range |
| --- | --- | ---: |
| `km` | Car mileage in kilometres | 22,899–240,000 |
| `price` | Car price (currency unspecified) | 3,650–8,290 |

Rows are not sorted by mileage.

## Intended deliverables

A completed project should provide:

1. A training program that reads the dataset, learns `θ₀` and `θ₁` with gradient descent, and saves them.
2. A prediction program that accepts mileage, loads the saved parameters, and returns an estimated price; before training, both parameters default to zero.
3. Clear handling of invalid input and malformed data.

Optional extensions from the subject include plotting the data and fitted line, and reporting model precision. See [`en.subject.pdf`](en.subject.pdf) for authoritative requirements.
