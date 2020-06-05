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
    # set up route list with slots
    route = [None] * length

    route_find = {}

    # store the ticket
    for ticket in tickets:
        route_find[ticket.source] = ticket.destination

    # Start with None
    next_route = route_find["NONE"]

    # look up each next route and stop when next route is NONE
    for current in range(0, length):

        # store next route
        route[current] = next_route

        # recall next route
        next_route = route_find[next_route]

    return route
