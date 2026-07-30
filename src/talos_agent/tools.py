def observe_approaching_ships() -> list[dict[str, str | int]]:
    return [
        {
            "name": "Argo",
            "origin": "Iolcos",
            "distance_km": 12
        },
        {
            "name": "Merchant Vessel",
            "origin": "Athens",
            "distance_km": 25
        },
    ]
def check_ship_permission(ship_name)->str:
    permission_registry={
        "Argo": "approved",
        "Black Sail": "denied",
    }
    status=permission_registry.get(ship_name,"unknown")
    return status