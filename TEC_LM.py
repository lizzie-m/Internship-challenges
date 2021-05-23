#!/usr/bin/env python
# coding: utf-8



from math import*
#This script it compares the buckling mass of the beam that is produced from the mass flow rate, to the mass produced from the
#aluminum and the steel I-shaped beams. The mass from the aluminium and the steel should be more than 
#the mass produced from the mass flowrate inorder to not buckle.
#For a mass flowrate of 2.5kg/s the mass from both materials do not buckle and aluminium calculated the lightest beam mass 
#that does not fail under the beam load.


# steel input parameters

velocity = 198.9
acceleration = 2
e1=200e9 #Young's modulus
rho1=8050 #density
uts1= 420e6
l1=300 #total length
w1=0.012 #beam depth
h1=0.020 #beam height

# Aluminium input parameters

e2= 70e9 #Young's modulus
rho2= 2700 #density
uts2= 310e6
l2=300 #total length
w2=0.012 #beam depth
h2=0.020 #beam height

# water pipe input parameters
rho_water = 1000
D_waterpipe = 0.005
d_waterpipe =0.0005
pipe_area = (pi*((D_waterpipe -(2*d_waterpipe))**2)/4) 


#A=(2*h*t2)+(t1*(w-(2*t2))) #beam cross sectional area

#force = mass x acceleration = mass flow rate x velocity
#mass_flow_rate = rho * A * velocity
#velocity = mass flow rate/ desnity * area
#force= mass flow rate^2 / density of water * area of pipe




def mab(mass_flow_rate):
    # 9.81 = acceleration due to gravity 
    #cross sectional area for pipe = a
      
    
    buckling_mass = ((mass_flow_rate**2)/ (rho_water*pipe_area)) /9.81
    
    return buckling_mass

mab(5)




#length of beam = l
#area of beam = total_area
#density of material = rho_beam
# e is the youngs modulus 
# w is the width

#length of beam = l
#area of beam = total_area
#density of material = rho_beam

#mass=rho*L*a #total mass


t2 = 3e-3
h= 20e-3
w = mab(2.5)*9.81
b1 =4e-3
d1 =6e-3
b2 =20e-3
d2 =3e-3
l = 300
youngs_modulus = 200

def mom(l,rho_beam,youngs_modulus):
#Derived equation for area please check notes
# area in terms of second moment of inertia
    total_area = (2*h*t2) + ((((l**2)/(3*2*youngs_modulus*w)) - ((b1*(d1**3))/12*2)) / (((b2*(d2**3))/12) + h**2))

    mass_of_material = rho_beam*total_area*l
    return(mass_of_material)





#Derived equation check notes
total_area = (2*h*t2) + ((((l**2)/(3*2*youngs_modulus*w)) - ((b1*(d1**3))/12*2)) / (((b2*(d2**3))/12) + h**2))
print(total_area)





mom(300,2700,70e9)#alu





mom(300,8050,200e9)#steel





def comparison(mass_flow_rate,l,rho_beam,youngs_modulus):
    x1 = mab(mass_flow_rate)
    x2 = mom(l,rho_beam,youngs_modulus)
    
    if x1 > x2:
         print("This should buckle because the mass of the material in kg, " + str(x2) +" ,is less than the resultant mass produced from the flowrate " + str(x1))  
    else:
         print("This should not buckle because the mass of the material in kg, " + str(x2) + " ,is higher than the resultant mass produced from the flowrate " + str(x1))

       




#Aluminium
comparison(2.5,300,2700,70e9)





#Steel
comparison(2.5,300,8050,200e9)





comparison(3.5,300,2700,70e9) # Aluminium buckles at a flow rate of 3.5kg/s



comparison(6,300,8050,200e9)# Steel  buckles at a flow rate of 6kg/s






