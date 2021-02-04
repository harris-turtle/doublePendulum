from vpython import *

#Initial conditions
theta1=90*pi/180
thetadot1=0
thetaddot1=0
theta2=30*pi/180
thetadot2=0
thetaddot2=0
l1=0.2
l2=0.2
g=9.8
m1=1
m2=1
t=0
dt=0.001

"""Initial conditions for secondary pendulum
ntheta1=91*pi/180
nthetadot1=0
nthetaddot1=0
ntheta2=31*pi/180
nthetadot2=0
nthetaddot2=0
"""

#Drawing the system
mass1=sphere(pos=vector(l1*sin(theta1), -l1*cos(theta1),0), radius=0.02, color=color.white, make_trail=False)
stick1=cylinder(pos=vector(0,0,0), axis=mass1.pos, radius=0.002)
mass2=sphere(pos=mass1.pos+vector(l2*sin(theta2), -l2*cos(theta2),0), radius=0.02, color=color.green, make_trail=True)
stick2=cylinder(pos=mass1.pos, axis=mass2.pos-mass1.pos, radius=0.002)

"""Drawing the secondary system
nmass1=sphere(pos=vector(l1*sin(ntheta1), -l1*cos(ntheta1),0), radius=0.02, color=color.white, make_trail=False)
nstick1=cylinder(pos=vector(0,0,0), axis=nmass1.pos, radius=0.002)
nmass2=sphere(pos=nmass1.pos+vector(l2*sin(ntheta2), -l2*cos(ntheta2),0), radius=0.02, color=color.blue, make_trail=True)
nstick2=cylinder(pos=nmass1.pos, axis=nmass2.pos-nmass1.pos, radius=0.002)
"""

while t<10:
  rate(1000)
  
  #Calculating new angles and updating to screen
  one1=m2*l2*thetaddot2*cos(theta1-theta2)
  two1=m1*l2*(thetadot2**2)*sin(theta1-theta2)
  three1=(m1+m2)*g*sin(theta1)
  one2=m2*l2*(thetadot1**2)*sin(theta1-theta2)
  two2=m2*l2*thetaddot1*cos(theta1-theta2)
  three2=m2*g*sin(theta2)
  thetaddot1=-(one1+two1+three1)/((m1+m2)*l1)
  thetadot1=thetadot1+thetaddot1*dt
  theta1=theta1+thetadot1*dt
  thetaddot2=(one2-two2-three2)/(m2*l2)
  thetadot2=thetadot2+thetaddot2*dt
  theta2=theta2+thetadot2*dt
  
  mass1.pos=vector(l1*sin(theta1), -l1*cos(theta1),0)
  stick1.axis=mass1.pos
  mass2.pos=mass1.pos+vector(l2*sin(theta2), -l2*cos(theta2),0)
  stick2.pos=mass2.pos
  stick2.axis=mass1.pos-mass2.pos
  
  """Calculating new angles and updating to screen for secondary system
  none1=m2*l2*nthetaddot2*cos(ntheta1-ntheta2)
  ntwo1=m1*l2*(nthetadot2**2)*sin(ntheta1-ntheta2)
  nthree1=(m1+m2)*g*sin(ntheta1)
  none2=m2*l2*(nthetadot1**2)*sin(ntheta1-ntheta2)
  ntwo2=m2*l2*nthetaddot1*cos(ntheta1-ntheta2)
  nthree2=m2*g*sin(ntheta2)
  nthetaddot1=-(none1+ntwo1+nthree1)/((m1+m2)*l1)
  nthetadot1=nthetadot1+nthetaddot1*dt
  ntheta1=ntheta1+nthetadot1*dt
  nthetaddot2=(none2-ntwo2-nthree2)/(m2*l2)
  nthetadot2=nthetadot2+nthetaddot2*dt
  ntheta2=ntheta2+nthetadot2*dt
 
  nmass1.pos=vector(l1*sin(ntheta1), -l1*cos(ntheta1),0)
  nstick1.axis=nmass1.pos
  nmass2.pos=nmass1.pos+vector(l2*sin(ntheta2), -l2*cos(ntheta2),0)
  nstick2.pos=nmass2.pos
  nstick2.axis=nmass1.pos-nmass2.pos
  """
  
  #Updating time
  t=t+dt
