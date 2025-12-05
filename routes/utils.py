# flight_app/utils.py

import heapq
from .models import Airport, FlightRoute 

def find_nth_node(start_airport_code, direction, n):
    """
    Traverses the route N times in the given direction.
    """
    current_airport = Airport.objects.filter(code=start_airport_code).first()
    if not current_airport:
        return "Start Airport not found"

    path = [current_airport.code]
    
    for i in range(n):
    
        route = FlightRoute.objects.filter(
            source=current_airport, 
            direction=direction.upper()
        ).first()
        
        if route:
            current_airport = route.destination
            path.append(current_airport.code)
        else:
            return f"Path ends after {i} steps. Last reached: {current_airport.code}"
            
    return current_airport

def get_longest_duration_route():
   
    longest_route = FlightRoute.objects.order_by('-duration_mins').first()
    if longest_route:
        return longest_route
    return None

def find_shortest_path(start_code, end_code):
    """
    Finds shortest path based on duration using Dijkstra's Algorithm.
    """

    queue = [(0, start_code, [])]
    visited = set()
    
    while queue:
        (cost, current_node, path) = heapq.heappop(queue)
        
        if current_node in visited:
            continue
        
        path = path + [current_node]
        visited.add(current_node)
        
        if current_node == end_code:
            return {"path": path, "total_duration": cost}
            
      
        routes = FlightRoute.objects.filter(source__code=current_node)
        
        for route in routes:
            if route.destination.code not in visited:
                heapq.heappush(queue, (cost + route.duration_mins, route.destination.code, path))
                
    return "No path found"