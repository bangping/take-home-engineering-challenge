import pytest
from script.get_nearest_trunks import get_nearest_trucks

trucks = [
  dict(Applicant=f"App{i}", Address=f"Addr{i}", FacilityType="Truck", Latitude=f"{i}.0", Longitude=f"-{i}.0")
  for i in range(10)
]

def test_nearest_5():
  results = get_nearest_trucks(trucks, 3.1, -3.1, 5)
  assert [i["Applicant"] for i in results] == ["App3", "App4", "App2", "App5", "App1"]
