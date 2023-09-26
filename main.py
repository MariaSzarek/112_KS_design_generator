"""
program do wynaczania trasy kanalizacji podposadzkowej, oblicza zagłębienie długość tras,
punkt wyjscia KS musi znajduje się na osi x,
sprawdza czy dane z csv są prawidłowe (mieszczą się w obrysie budynku)

jak dalej można rozbudować program:
 - jedno wpięcie w węźle
 - wpięcia tylko pod kątem 45 st
- mam powielone liczenie trasy bo jest w klasie punkt i pipeline

Program ćwiczony na .csv
15, 10, dlugosc i szerokosc budynku
x, y
8, 0, wyjście z budynku musi być (x, 0)
10, 9
1, 5
3, 8
7, 4
1, 7
"""

from points import Point
from pipeline import find_route, depth
from drawing import draw_points, draw_coordinates, draw_building, offset

import csv
import turtle

scale = 30
x=0
y=0

with open("points.csv", "r") as file:
    reader = csv.reader(file)
    dimension = next(reader)
    next(reader)
    all_points = [Point(int(i[0]), int(i[1])) for i in reader]
    x = int(dimension[0])
    y = int(dimension[1])
    to_center = offset(x, y, scale)

if x > 0 and y > 0 and all_points[0].y == 0:
    print("The building dimensions and the last point of the sewage system are provided correctly")
for i in all_points:
    if i.x <= x and i.y <= y:
        pass
    else:
        raise ValueError("Invalid data in the csv file. Please provide correct details")
print("The connection points for the sewage system are specified correctly")


last_point = all_points[0]
first_route = []
start_point = None

routes_obj = {}
routes_str = {}

for the_point in all_points[1:]:
    route = find_route(the_point, last_point, x, y)
    if route and len(route) > len(first_route):
        first_route = route
        start_point = the_point
        print(f"The farthest point: {start_point.x, start_point.y}")

routes_obj[(start_point)] = [point for point in first_route]
routes_str[(start_point.x, start_point.y)] = [(point.x, point.y) for point in first_route]


for the_point in all_points[1:]:
    if the_point == start_point:
        continue
    other_route = first_route.copy()[:-1]
    for some_point in first_route[:-1]:
        route = find_route(the_point, some_point, x, y )
        if route and len(route) < len(other_route) and route[-1].y <= route[-2].y: #condition to connect pipes in good direction (final point on X-axis (y=0)
            other_route = route

    routes_obj[(the_point)] = [other_route]
    routes_str[(the_point.x, the_point.y)] = [(point.x, point.y) for point in other_route]

    draw_points(other_route, to_center, scale)

draw_building(x, y, scale)
draw_points(first_route, to_center, scale)
draw_coordinates(all_points, to_center, scale)


with open("routes_obj.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    for point_key, route in routes_obj.items():
        csv_writer.writerow([point_key, route])

with open("routes_str.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["First point", "Route"])
    for point_key, route in routes_str.items():
        csv_writer.writerow([point_key, route])


final_routes = {}
for k, i in routes_str.items():
    for g, j in routes_str.items():
        if i != j and len(i) >= len(j):
            while j[-1] in i and j[-2] in i:
                del j[-1]
                final_routes[g] = j
        else:
            final_routes[g] = j


pipe_lenght = 0
for i in final_routes.values():
    pipe_lenght += len(i)-1
print(f" Length of pipelines: {pipe_lenght} m")


longest_route = []
for i in final_routes.values():
    for j in final_routes.values():
        if i != j:
            end_point_i = i[-1]
            index_end_point_j = j.index(end_point_i) if end_point_i in j else None
            if index_end_point_j is not None:
                print(index_end_point_j)
                longest_route_len = (len(j) - index_end_point_j - 1 + len(i) - 1)
                if len(first_route) < longest_route_len:
                    longest_route = i[:-1] + j[index_end_point_j:]

longest_route_len = len(longest_route)
print(f"The longest route: {longest_route}")
print(f"Length of longest route: {longest_route_len}")
excavation_depth = depth(longest_route_len)
print(f"The last point is lowered by {excavation_depth}m from the bottom of the first point")


with open("routes_str.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Punkt Startowy", "Trasa"])
    for point_key, route in final_routes.items():
        csv_writer.writerow([point_key, route])
    csv_writer.writerow(["The longest route:"])
    csv_writer.writerow([longest_route])
    csv_writer.writerow(["Length of longest route:"])
    csv_writer.writerow([longest_route_len])
    csv_writer.writerow(["Przeglebienie"])
    csv_writer.writerow([excavation_depth])

turtle.exitonclick()