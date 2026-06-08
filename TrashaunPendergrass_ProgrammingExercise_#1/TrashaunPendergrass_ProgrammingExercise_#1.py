# This program sells a limited number of tickets
# Each buyer can buy up to 4, no more than 20 can be sold
# The program prompts the user for desired tickets and displays how many are left
# Program repeats until all tickets are sold and displays total buyers

def get_ticket_amount(tickets_left, max_per_buyer):
    # Limits the buyer to 4 tickets or tickets remaining.
    max_tickets = min(max_per_buyer, tickets_left)

    # Gets the number of tickets the buyer wants.
    tickets = int(input(f"How many tickets to buy? (max 4): "))

    # Makes invalid purchases not count, have them retry.
    if tickets < 1 or tickets > max_tickets:
        print("Invalid tickets. Try again.")
        tickets = 0

    # Returns the ticket amount to the main function.
    return tickets


def main():
    # Stores the assignment limits.
    TOTAL_TICKETS = 10
    MAX_PER_BUYER = 4

    # Counts tickets left and counts buyers.
    tickets_left = TOTAL_TICKETS
    total_buyers = 0

    # Keeps selling tickets until all are sold.
    while tickets_left > 0:
        tickets_bought = get_ticket_amount(tickets_left, MAX_PER_BUYER)

        # Update totals only when the purchase is valid.
        if tickets_bought > 0:
            tickets_left = tickets_left - tickets_bought
            total_buyers = total_buyers + 1
            print(f"Tickets remaining: {tickets_left}")

    # Displays the total number of buyers.
    print("All tickets have been sold.")
    print(f"Total number of buyers: {total_buyers}")


# Starts the program.
main()