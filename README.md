# doublePendulum
Code for a visualization of the motion of a double pendulum.
## Why a double pendulum?
A double pendulum is a very interesting mechanics problem as it posses a tough challange for solving its equation of motion using Newton's laws. Calculating the force of gravity on each mass is easy enough but the difficulty arises when attempting to come up with expressions for the forces of tension. The value and direction of these forces are interconnected with the current positions of the masses making it a mess. Instead this system is used as a prime example for Lagrangian mechanics. The Euler-Langrange equation is equivilant to the expression F=ma, but is in a form consisting of only scalars related to the energies of the system. Thus, with this method we would not have to worry about the internal forces of tension or vector expressions for coordinates. Instead we would only have to derive expressions for the gravitation potential energies, kinetic energies, and use only theta1 and theta2 to describe where our system is in space.
## Visualization
Once the equation of motion are solved for the two coordinate variables theta1 and theta2, a numerical integrator is used to solve and output the values into this visualization.

<a href="https://i.imgur.com/qzF5M8b.gif"><img src="https://i.imgur.com/qzF5M8b.gif" title="The Visualization"/></a>

## Chaos
Another interesting aspect of this system is its high sensitivity to initial conditions. Below are two idential double pendulums, with one having initial angles different by only one degree.

<a href="https://i.imgur.com/I0DDnDm.gif"><img src="https://i.imgur.com/I0DDnDm.gif" title="Chaos"/></a>

The two pendulums follow the same initial trajectories but soon after deviate and follow completely different paths. This is called chaos because this system seems to act irratically and hard to accuratly predict into the future without perfect accuracy of initial conditions. Mathematical weather predictions also have this property making them unreliable for long time scales.
