from logger import get_logger

logger = get_logger("calculator")


def calculate() -> None:
    """Perform a basic arithmetic calculation.

    Prompts the user for two numbers and an operator (+, -, *, /).
    Validates input and handles division by zero. Logs each step
    of the calculation process.
    """
    logger.debug("Calculation started")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                logger.warning("Division by zero attempted")
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            logger.warning(f"Invalid operator entered: {op}")
            print("Invalid operator.")
            return

        logger.info(f"Calculation completed: {num1} {op} {num2} = {result}")
        print(f"Result: {result}")
    except ValueError:
        logger.warning("Invalid number input during calculation")
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        logger.critical(f"Unexpected application failure during calculation: {e}")
        print("An unexpected error occurred during calculation.")
