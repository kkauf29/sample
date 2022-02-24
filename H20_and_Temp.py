###
# Kim Kaufman
# This program will obtain user input for temperature and altitude and will calculate if water 
# is solid, liquid, or gas at that temperature and altitude

def main():
    
    print("Program to determine state of water at different temperatures and altitudes\n")
    
    try:  #obtain user input for temperature and altitude and convert to integer
    
        temp_input = float(input("Please enter a temperature in Fahrenheit (number only): ")) 
    
        altitude_input = float(input("Please enter your altitude in feet (number only): "))
    
    except ValueError: # informs users when input could not be converted to an integer
        
        print("Invalid input. Please enter a number")
    
    def altitude_adjustment(altitude):
        """Adjusts boiling point by lowering 1 degree Fahrenheit for every 500 feet of increased altitude
        @params altitude
        returns adjusted boiling point"""
        boiling_point = 212
        if altitude >= 500:
            boiling_point -= (altitude / 500)
        return round(boiling_point, 2)  
         
    
    def solid_liquid_gas(temperature, boiling_point):
        """Calculates if water will be solid, liquid, or gas at the provided temperature and boiling point
        @ params temperature and boiling_point
        returns a string which states whether the water is sold, liquid or gas"""
        if temperature < 32:
            state = "solid"
        elif temperature >= 32 and temperature < boiling_point:
            state = "liquid"
        else:
            state = "gas"
        return state
    
    # calls altitude_adjustment with the user input altitude_input and assigns value to boiling_p 
    boiling_p = altitude_adjustment(altitude_input)
    
    #calls sold_liquid_gas with user input temp_input and boiling_p and assigns value to state_of_water
    state_of_water = solid_liquid_gas(temp_input, boiling_p)
    
    
    print(f"At {temp_input} degrees F and {altitude_input} ft altitude, water is {state_of_water}")           
        
     
    
    
    
    
main()     
