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

def inspection_report(ship_name: str) -> dict[str, str | int]:
    report = observe_approaching_ships()
    for ship in report:
        if ship["name"] == ship_name:
            status = check_ship_permission(ship_name)
            ship["permission_status"] = status
            return ship 
            break
    else:
        return {"error": "Ship not found"}
   
    