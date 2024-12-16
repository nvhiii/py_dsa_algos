# Define the stations and the states they cover
stations = {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}

# Define the set of all states we need to cover
states_needed = {"wa", "id", "nv", "ut", "or", "ca", "az", "mt"}

# Initialize the final set of selected stations
final_stations = set()

# Iterate until all needed states are covered
# while states_needed:
#     best_station = None
#     states_covered = set()
    
#     for station, states in stations.items():
#         # Find the intersection between states needed and states covered by the station
#         covered = states_needed & states
#         if len(covered) > len(states_covered):
#             best_station = station
#             states_covered = covered

#     # Update the states needed by removing those covered by the best station found
#     states_needed -= states_covered
#     # Add the best station to the final selection
#     if best_station:
#         final_stations.add(best_station)

# print("Selected stations:", final_stations)

while states_needed:
    # best station is set to None
    best_station = None
    states_covered = set() # empty state

    # every iteration, we iterate all stations and states
    for station, states in stations.items():
        # find intersection
        covered = states_needed & states
        if len(covered) > len(states_covered):
            states_covered = covered
            best_station = station

    states_needed -= states_covered

    if best_station: # valid if not None
        final_stations.add(best_station)
