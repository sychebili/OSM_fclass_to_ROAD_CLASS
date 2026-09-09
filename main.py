
'''
NOTE: Some ROAD_CLASS values do not match a corresponding road fclass and are ommited from this program

Missing ROAD_CLASS values:
5 (Roundabouts), 11 (Turning arcs), 13 (Escalator), 14 (Elevator), 15 (Pedestrian ramp), #64 (Transit), #128 (Sailing lines)
'''

roads_dict = {

    #Local roads
    "tertiary": 1,
    "residential": 1,
    "living_street": 1,
    "unclassified": 1,
    "service": 1,
    "track": 1,
    "track_grade1": 1,
    "track_grade2": 1,
    "track_grade3": 1,
    "track_grade4": 1,
    "track_grade5": 1,
    "busway": 1,

    # Highways
    "motorway": 2,
    "trunk": 2,

    # Ramps
    "motorway_link": 3,
    "trunk_link": 3,
    "primary_link": 3,
    "secondary_link": 3,
    "tertiary_link": 3,

    # Major roads
    "primary": 6,
    "secondary": 6,

    #Walkways
    "pedestrian": 10,
    "footway": 10,
    "path": 10,
    "cycleway": 10,
    "bridleway": 10,

    #Stairs
    "steps": 12,

    #Ferries
    "ferry": 4
}

def classify_road(fclass):
  return roads_dict.get(fclass, None)