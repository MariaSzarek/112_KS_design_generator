import heapq
from points import Point


def find_route(the_point, last_point, dim_x, dim_y):
    open_list = [(0, the_point)]
    closed_list = set()
    previous = {}
    costs = {the_point: 0}

    while open_list:
        cost, current_point = heapq.heappop(open_list)

        if current_point == last_point:
            route = [last_point]
            while route[-1] != the_point:
                route.append(previous[route[-1]])
            route.reverse()
            return route

        if current_point in closed_list:
            continue

        closed_list.add(current_point)

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                x, y = current_point.x, current_point.y
                nx, ny = x + dx, y + dy

                if 0 <= nx < dim_x and 0 <= ny < dim_y:
                    neighbor = Point(nx, ny)
                    new_cost = costs[current_point] + 1

                    if neighbor not in costs or new_cost < costs[neighbor]:
                        costs[neighbor] = new_cost
                        priority = new_cost + neighbor.distance(last_point)
                        previous[neighbor] = current_point
                        heapq.heappush(open_list, (priority, neighbor))

    return None


def depth(length):
    bottom = length / 100 * 2
    return bottom
