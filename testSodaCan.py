###
# Kim Kaufman
# Imports the SodaCan class to create an object. It obtains user input for can_radius and can_heights 
# that will be used as the canHeight and canRadius attributes in the SodaCan object. The getSurfaceArea
# and getVolume methods from the SodaCan class are used to get the surface area and volume of the can 

from SodaCanClass import SodaCan

def main():
    
    
    while True:
    
        try: #obtains can radius and can height from user input
            can_radius = float(input("Please enter the radius of a can in centimeters (digits only): "))
            can_height = float(input("please enter the height of a can in centimeters (digits only): "))
            
            #checks if number is positive
            if can_radius < 0 or can_height < 0:
                print("Please enter positive numbers")  
            else:
                break
            
        # prints message if user input cannot be converted to a float and continues loop to obtain user input again             
        except ValueError:
            print("Invalid input. Please try again")
            print()
                
    can_radius = round(can_radius, 2)
    can_height = round(can_height, 2)                            
    
    #creates SodaCan object with the user input        
    can1 = SodaCan(can_height, can_radius) 
    
    #uses the getSurfaceArea method to get the surface area for can1
    can_surface_area = can1.getSurfaceArea()
    
    #uses the getVolume method to get the volume for can1
    can_volume = can1.getVolume()
    
    print(f"The surface area of this can is {can_surface_area}")
    
    print(f"The volume of this can is {can_volume}")
    
    
if __name__ == "__main__":
    main()    
    
       
