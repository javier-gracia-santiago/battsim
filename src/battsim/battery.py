class Battery:
    def __init__(self, initial_energy, nom_capacity):
        self.nom_capacity = nom_capacity * 3600
        self.current_energy = initial_energy * 3600

    @property
    def soc(self):
        return (self.current_energy/self.nom_capacity)*100

    def step(self, dt, power):
        # Current energy calculation
        self.current_energy = self.current_energy - dt*power
        if self.current_energy < 0:
            self.current_energy = 0
        elif self.current_energy> self.nom_capacity:
            self.current_energy = self.nom_capacity
        
