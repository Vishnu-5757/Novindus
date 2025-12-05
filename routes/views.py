from django.shortcuts import render, redirect
from .models import Airport, FlightRoute
from .forms import FlightRouteForm
from .utils import find_nth_node, get_longest_duration_route, find_shortest_path 


import json 

def dashboard(request):

    if request.method == 'POST' and 'add_route' in request.POST:
        form = FlightRouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('routes:dashboard')
    else:
        form = FlightRouteForm()

    nth_result = None
    if 'search_nth' in request.GET:
        start = request.GET.get('start_node')
        direction = request.GET.get('direction')
        n_steps = int(request.GET.get('n_steps', 1))
        nth_result = find_nth_node(start, direction, n_steps)

    shortest_path_result = None
    if 'search_path' in request.GET:
        start_p = request.GET.get('path_start')
        end_p = request.GET.get('path_end')
        shortest_path_result = find_shortest_path(start_p, end_p)

    longest_route = get_longest_duration_route()
    

    airports = Airport.objects.all()
    all_routes = FlightRoute.objects.all()

  
    nodes_data = []
    for airport in airports:
        nodes_data.append({
            'id': airport.code, 
            'label': f"Airport\n{airport.code}", 
            'shape': 'circle',
            'color': '#ffffff', 
            'font': {'multi': 'html'} 
        })

    # Create Edges (The Routes)
    edges_data = []
    for route in all_routes:
        edges_data.append({
            'from': route.source.code,
            'to': route.destination.code,
            'label': f"{route.direction}\n{route.distance_km} km", 
            'arrows': 'to',
            'font': {'align': 'middle'}
        })

    context = {
        'form': form,
        'nth_result': nth_result,
        'longest_route': longest_route,
        'shortest_path_result': shortest_path_result,
        'airports': airports,
        'all_routes': all_routes,
        'graph_nodes': json.dumps(nodes_data), 
        'graph_edges': json.dumps(edges_data),
    }
    return render(request, 'routes/dashboard.html', context)