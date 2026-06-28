from pytest import approx
from battsim.battery import Battery

# Helpers
def prepare_battery(initial_energy, nom_capacity): 
    battery = Battery(initial_energy, nom_capacity) # Wh, Wh
    return battery


def test_soc_100_to_50():
    battery = prepare_battery(100000,100000)
    dt=0.1
    time_it = 1800/dt
    for _ in range(int(time_it)):
        battery.step(dt=dt, power= 100000) 
    assert battery.soc == approx(50)

def test_clamp_battery_discharge():
    battery = prepare_battery(100000,100000)
    dt=0.1
    time_it = 3650/dt
    for _ in range(int(time_it)):
        battery.step(dt=dt, power= 100000) 
    assert battery.soc == approx(0)

def test_clamp_battery_charge():
    battery = prepare_battery(100000,100000)
    dt=0.1
    time_it = 3650/dt
    for _ in range(int(time_it)):
        battery.step(dt=dt, power= -100000) 
    assert battery.soc == approx(100)