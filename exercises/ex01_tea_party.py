"""Calculate cost of tea party based on number of guests."""

__author__: str = "730663103"


def main_planner(guests: int) -> None:  # Defining function to bring all together
    """Bringing all functions together to print what the result is"""  # Explaining
    print(
        "A Cozy Tea Party for " + str(guests) + " People!"
    )  # Printing word template while adding amt. of guests
    print(
        "Tea Bags: " + str(tea_bags(people=guests))
    )  # Printing Tea bag amt. template with amt. of tea bags needed
    print(
        "Treats: " + str(treats(people=guests))
    )  # Printing treat amt. template with amt. of treats needed
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )  # Printing cost amt. template with total cost by calling treats & tea_bags


def tea_bags(people: int) -> int:  # Define fn. to calculate amt. of tea bags needed
    """Function getting the total amt. of tea bags needed"""
    return people * 2  # Double amount of people


def treats(people: int) -> int:  # Define fn. to calculate amt. of treats needed
    """Function getting the total amt. of treats needed"""
    return int(tea_bags(people=people) * 1.5)  # Multiply amount of tea by 1.5


def cost(
    tea_count: int, treat_count: int
) -> float:  # Define fn. to calculate total costs of items
    """Function multiplying counts by their prices to get total cost"""
    return (treat_count * 0.75) + (
        tea_count * 0.5
    )  # Multiply amounts by their prices, and add them


if __name__ == "__main__":
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # Making it runnable
