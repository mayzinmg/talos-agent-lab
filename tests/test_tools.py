from talos_agent.tools import inspection_report


def test_argo_has_approved_permission():
    result = inspection_report("Argo")

    assert result["name"] == "Argo"
    assert result["permission_status"] == "approved"

def test_missing_ship_returns_error():
    result = inspection_report("Ship That Is Not Approaching")

    assert result["error"] == "Ship not found"

def test_ship_with_unknown_permission():
    result = inspection_report("Merchant Vessel")

    assert result["name"] == "Merchant Vessel"
    assert result["permission_status"] == "unknown"
