import heapq

class AStarGrid:
    def __init__(self):
        self.grid_size = (5, 5)
        self.vertical_steps_per_unit = 3500 / 280  # steps per mm for vertical movement
        self.horizontal_steps_per_unit = 312.5 / 25  # steps per mm for horizontal movement
        self.horizontal_unit_mm = 25  # 25 mm
        self.vertical_unit_mm = 280  # 280 mm

    def heuristic(self, node, goal):
        # Manhattan distance heuristic
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    def astar(self, start, end):
        open_list = [(0, start)]
        came_from = {}
        g_score = {node: float('inf') for node in self.grid}  # Initialize g_score for all nodes
        g_score[start] = 0

        while open_list:
            current_cost, current_node = heapq.heappop(open_list)

            if current_node == end:
                path = []
                while current_node in came_from:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.append(start)
                return path[::-1]

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (current_node[0] + dx, current_node[1] + dy)
                if 0 <= neighbor[0] < self.grid_size[0] and 0 <= neighbor[1] < self.grid_size[1]:
                    if neighbor not in g_score:  # Check if neighbor node is not in g_score
                        g_score[neighbor] = float('inf')  # Initialize g_score for neighbor
                    tentative_g_score = g_score[current_node] + 1
                    if tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current_node
                        g_score[neighbor] = tentative_g_score
                        f_score = tentative_g_score + self.heuristic(neighbor, end)
                        heapq.heappush(open_list, (f_score, neighbor))

        return None

    def find_shortest_path(self, locations):
        # Sort locations based on (X, Y)
        locations.sort(key=lambda x: (x[0], x[1]))
        self.grid = set((x, y) for x, y, _ in locations)
        paths = []

        # Calculate shortest path from (0, 0) to the first point
        start = (0, 0)
        end = locations[0][:2]
        path = self.astar(start, end)
        if path:
            paths.extend(path)

        # Calculate shortest path between locations
        for i in range(len(locations) - 1):
            start = locations[i][:2]
            end = locations[i + 1][:2]
            path = self.astar(start, end)
            if path:
                if i == 0:
                    paths.extend(path)
                else:
                    paths.extend(path[1:])  # Exclude the starting point of the path

        # Calculate shortest path from the last point back to (0, 0)
        start = locations[-1][:2]
        end = (0, 0)
        path = self.astar(start, end)
        if path:
            paths.extend(path)

        # Set count for each point in the final path
        final_path = []
        encountered_points = set()  # To keep track of encountered points
        for point in paths:
            if len(point) == 2:  # If point doesn't have a count
                count = next((loc[2] for loc in locations if loc[:2] == point), 0)
                if point in encountered_points:
                    count = 0
                else:
                    encountered_points.add(point)
                final_path.append(point + (count,))
            else:
                final_path.append(point)

        return final_path

    def calculate_steps(self, path, locations):
        total_vertical_steps = 0
        total_horizontal_steps = 0
        steps_list = []

        for i in range(1, len(path)):
            x1, y1, count1 = path[i - 1]
            x2, y2, count2 = path[i]

            # Calculate the distance in mm for horizontal and vertical movement
            horizontal_distance_mm = abs(x2 - x1) * self.horizontal_unit_mm
            vertical_distance_mm = abs(y2 - y1) * self.vertical_unit_mm

            # Calculate the steps required for each movement
            horizontal_steps = horizontal_distance_mm * self.horizontal_steps_per_unit
            vertical_steps = vertical_distance_mm * self.vertical_steps_per_unit

            # Update total steps
            total_horizontal_steps += horizontal_steps if x2 > x1 else -horizontal_steps
            total_vertical_steps += vertical_steps if y2 > y1 else -vertical_steps

            # Only add significant locations (locations with items)
            if count2 > 0:  # Include only locations with items
                if len(steps_list) > 0:
                    v, h, c = steps_list[-1]
                    steps_list.append((round(total_vertical_steps - v, 2), round(total_horizontal_steps - h, 2), count2))
                else:
                    steps_list.append((round(total_vertical_steps, 2), round(total_horizontal_steps, 2), count2))

        # Return to (0, 0) with negative steps
        x3, y3 = locations[-1][:2]
        horizontal_distance_mm = abs(x3 - 0) * self.horizontal_unit_mm
        vertical_distance_mm = abs(y3 - 0) * self.vertical_unit_mm
        horizontal_steps = horizontal_distance_mm * self.horizontal_steps_per_unit
        vertical_steps = vertical_distance_mm * self.vertical_steps_per_unit
        total_horizontal_steps += horizontal_steps if 0 > x3 else -horizontal_steps
        total_vertical_steps += vertical_steps if 0 > y3 else -vertical_steps
        steps_list.append((round(total_vertical_steps, 2), round(total_horizontal_steps, 2), 0))

        return steps_list

    def process_input_list(self, input_list):
        locations = [(item['loc_x'], item['loc_y'], item['Count']) for item in input_list]
        return locations

    def find_steps_from_input(self, input_list):
        locations = self.process_input_list(input_list)
        shortest_path = self.find_shortest_path(locations)
        print("Shortest path:", shortest_path)
        steps = self.calculate_steps(shortest_path, locations)
        print("Steps required:", steps)
        return steps

# Example usage:
# input_list = [
#     {'Medicine_Name': 'a1 cream 100 gm', 'Count': 1, 'Price_Per_Count': 45.0, 'loc_x': 3, 'loc_y': 2},
#     {'Medicine_Name': 'abilaxine 10mg 5 adult supp.', 'Count': 1, 'Price_Per_Count': 4.0, 'loc_x': 1, 'loc_y': 3},
#     {'Medicine_Name': 'abilia 20mg 30 f.c.tabs.', 'Count': 1, 'Price_Per_Count': 120.0, 'loc_x': 1, 'loc_y': 2}
# ]
#
# astar_grid = AStarGrid()
# steps = astar_grid.find_steps_from_input(input_list)
