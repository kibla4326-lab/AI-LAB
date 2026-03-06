

class HeaterAgent:
    
    def __init__(self):
        # Initially heater is OFF
        self.previous_action = "OFF"
    
    def decide(self, temperature):
        
        # Rule 1: If temperature is less than 18, turn heater ON
        if temperature < 18:
            action = "ON"
        
        # Rule 2: If temperature is greater than 22, turn heater OFF
        elif temperature > 22:
            action = "OFF"
        
        # Rule 3: If temperature is between 18 and 22,
        
        else:
            action = self.previous_action
        
        # Save action as memory
        self.previous_action = action
        
        return action


agent = HeaterAgent()

# Sample temperatures (you can change these)
temperatures = [16, 19, 21, 23, 20, 17]

for temp in temperatures:
    result = agent.decide(temp)
    print("Temperature:", temp, "°C  -> Heater:", result)