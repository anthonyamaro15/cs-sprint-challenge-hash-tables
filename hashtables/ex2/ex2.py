#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    destinations = [None] * length

    destination_lookup = {}
    for ticket in tickets:

       # saving the source as key, and destination as value
        destination_lookup[ticket.source] = ticket.destination

   # get value for NONE
    next_destination = destination_lookup['NONE']

    for current_leg in range(0, length):

        destinations[current_leg] = next_destination
       # ['PDX', None, None]
       #  ['PDX', 'DCA', None]
       # ['PDX', 'DCA', 'NONE']
        # pushing none one index
        next_destination = destination_lookup[next_destination]

    return destinations


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

result = reconstruct_trip(tickets, 3)
print(result)
