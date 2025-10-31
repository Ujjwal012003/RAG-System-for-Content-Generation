---
title: "Moving_Charges_and_Magnetism"
author: "Class 12 Physics"
date: 2024-06
subject: Physics
chapter: 4
language: en
---

# Chapter 4: Moving_Charges_and_Magnetism

## Table of Contents

1. [4.1 Introduction to Moving Charges and Magnetism](#41-introduction-to-moving-charges-and-magnetism)  
2. [4.2 Magnetic Force on a Moving Charge](#42-magnetic-force-on-a-moving-charge)  
   - [4.2.1 Lorentz Force on Moving Charges](#421-lorentz-force-on-moving-charges)  
   - [4.2.2 Properties of Magnetic Force on Moving Charges](#422-properties-of-magnetic-force-on-moving-charges)  
3. [4.3 Motion of Charged Particles in a Magnetic Field](#43-motion-of-charged-particles-in-a-magnetic-field)  
   - [4.3.1 Circular Motion of Charged Particles](#431-circular-motion-of-charged-particles)  
   - [4.3.2 Helical Motion of Charged Particles](#432-helical-motion-of-charged-particles)  
4. [4.4 Force on a Current-Carrying Conductor in a Magnetic Field](#44-force-on-a-current-carrying-conductor-in-a-magnetic-field)  
5. [4.5 Biot–Savart Law](#45-biot–savart-law)  
   - [4.5.1 Statement and Mathematical Expression](#451-statement-and-mathematical-expression)  
   - [4.5.2 Applications of Biot–Savart Law](#452-applications-of-biot–savart-law)  
6. [4.6 Ampère’s Circuital Law](#46-ampères-circuital-law)  
   - [4.6.1 Statement and Mathematical Form](#461-statement-and-mathematical-form)  
   - [4.6.2 Applications of Ampere’s Law](#462-applications-of-amperes-law)  
7. [4.7 Force Between Two Parallel Currents](#47-force-between-two-parallel-currents)  
8. [4.8 Cyclotron](#48-cyclotron)  
   - [4.8.1 Principle and Basic Concept](#481-principle-and-basic-concept)  
   - [4.8.2 Construction and Working](#482-construction-and-working)  
   - [4.8.3 Cyclotron Frequency Derivation](#483-cyclotron-frequency-derivation)  
   - [4.8.4 Maximum Energy and Limitations](#484-maximum-energy-and-limitations)  
   - [4.8.5 Applications of Cyclotron](#485-applications-of-cyclotron)  
9. [4.9 Moving Coil Galvanometer](#49-moving-coil-galvanometer)  
   - [4.9.1 Principle](#491-principle)  
   - [4.9.2 Construction](#492-construction)  
   - [4.9.3 Theory and Derivation](#493-theory-and-derivation)  
   - [4.9.4 Current Sensitivity](#494-current-sensitivity)  
   - [4.9.5 Voltage Sensitivity](#495-voltage-sensitivity)  
   - [4.9.6 Conversion to Ammeter](#496-conversion-to-ammeter)  
   - [4.9.7 Conversion to Voltmeter](#497-conversion-to-voltmeter)  

[Summary](#summary) [Practice Questions](#practice-questions)  

---

## 4.1 Introduction to Moving Charges and Magnetism

<img src="https://i.imgur.com/s9R843X.png" alt="Oersted's Experiment" style="width:450px; display:block; margin:auto" />

The fascinating connection between electricity and magnetism was first experimentally discovered in 1820 by Hans Christian Oersted. He noticed that a compass needle placed near a current-carrying wire experienced a deflection, which demonstrated that an electric current produces a magnetic field surrounding the conductor.

A magnetic field is a vector field denoted by $\mathbf{B}$ that exists around magnets and moving electric charges. While electric fields ($\mathbf{E}$) originate from static charges, magnetic fields exist only because of moving charges or changing electric fields.

The magnetic interaction between currents and magnets forms the basis of electromagnetism, a fundamental branch of physics that has been unified with electricity under Maxwell's equations.

Magnetism can be understood from both a microscopic viewpoint, involving moving electrons inside atoms, and then macroscopically as the field created by current-carrying conductors. The direction of the magnetic field lines around a conductor is given by the right-hand thumb rule: if the thumb points in direction of current, the fingers curl in direction of magnetic field.

Understanding magnetic forces on moving charges helps explain the operation of devices such as cathode ray tubes, electric motors, and particle accelerators. It also forms the foundation of electromagnetic induction, where changing magnetic flux induces current in coils.

Oersted's discovery opened the path for great innovators like Ampère, Faraday, and Maxwell to explore the electromagnetic relationship, which today enables a myriad of technologies from MRI machines to wireless communications.

---

## 4.2 Magnetic Force on a Moving Charge

### 4.2.1 Lorentz Force on Moving Charges

<img src="https://i.imgur.com/sTMzZ1R.png" alt="Lorentz Force Vector Diagram" style="width:450px; display:block; margin:auto" />

A fundamental force experienced by a charged particle moving in combined electric and magnetic fields is known as the Lorentz force. The force $\mathbf{F}$ acting on a charge $q$ moving with velocity $\mathbf{v}$ in electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$ is expressed as:

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
$$

When only magnetic fields are present, the force simplifies to:

$$
\mathbf{F} = q(\mathbf{v} \times \mathbf{B})
$$

This force is perpendicular both to the velocity $\mathbf{v}$ of the charge and the magnetic field $\mathbf{B}$. The magnitude is:

$$
F = q v B \sin \theta
$$

where $\theta$ is the angle between $\mathbf{v}$ and $\mathbf{B}$.

The direction of $\mathbf{F}$ is given by the right-hand rule: Point your fingers in direction of $\mathbf{v}$, curl them towards $\mathbf{B}$, and your thumb points in direction of force for a positive charge.

**Example:** Calculate the magnetic force on an electron moving at $2 \times 10^6\, m/s$ perpendicular to a magnetic field of $0.01\, T$.

Given $q = 1.6 \times 10^{-19} C$,  
$F = q v B = 1.6 \times 10^{-19} \times 2 \times 10^{6} \times 0.01 = 3.2 \times 10^{-15}\, N$

This tiny force can significantly alter the electron's trajectory, as observed in cathode ray tubes.

**Applications:** Magnetic force is exploited in mass spectrometers, cyclotrons, and magnetic storage devices to manipulate charged particle paths precisely.

### 4.2.2 Properties of Magnetic Force on Moving Charges

<img src="https://i.imgur.com/ULRz2GT.png" alt="Trajectory of Charged Particle in Magnetic Field" style="width:450px; display:block; margin:auto" />

Key properties of the magnetic force include:

- **Perpendicularity:** The magnetic force is always perpendicular to the instantaneous velocity. Therefore, the magnetic field does not change the speed of the charge, only its direction.
  
- **No work done:** Since force is perpendicular to velocity, magnetic force cannot do work on the charge; it cannot change kinetic energy.

- **Effect on Trajectory:** The perpendicular force produces circular or helical motion depending on components of velocity relative to the magnetic field.

When velocity has a component along the magnetic field, the particle moves in a helical path with constant speed along the field and circular motion perpendicular, combining into a screw-like trajectory.

**Example:** An electron moving with velocity having components $v_\perp$ and $v_\parallel$ in a magnetic field experiences force only due to $v_\perp$. The component $v_\parallel$ remains unaffected, causing helical motion.

This property is fundamental to understanding particle trajectories in magnetic fields in applications like cyclotrons and astrophysical phenomena.

---

## 4.3 Motion of Charged Particles in a Magnetic Field

### 4.3.1 Circular Motion of Charged Particles

<img src="https://i.imgur.com/q7yDsDp.png" alt="Circular Motion of Charged Particle" style="width:450px; display:block; margin:auto" />

When a charged particle moves perpendicular to a uniform magnetic field, the magnetic force acts as centripetal force causing circular motion.

Equating magnetic force to centripetal force:

$$
q v B = \frac{m v^2}{r}
$$

Solving for radius $r$ of circular path:

$$
r = \frac{m v}{q B}
$$

The time period of revolution is:

$$
T = \frac{2\pi r}{v} = \frac{2\pi m}{q B}
$$

Frequency of revolution (cyclotron frequency):

$$
f = \frac{1}{T} = \frac{q B}{2\pi m}
$$

**Example:** Calculate radius of path for electron ($m=9.1 \times 10^{-31} kg$, $q=1.6 \times 10^{-19} C$) moving at $3 \times 10^7 m/s$ in magnetic field $6 \times 10^{-4} T$.

$$
r = \frac{9.1 \times 10^{-31} \times 3 \times 10^{7}}{1.6 \times 10^{-19} \times 6 \times 10^{-4}} = 0.284 \, m
$$

Such calculation confirms the feasibility of bending electron beams by magnetic fields.

**Applications:** This principle is used in cyclotrons and synchrotrons for particle acceleration.

### 4.3.2 Helical Motion of Charged Particles

<img src="https://i.imgur.com/wPV638A.png" alt="Helical Path of Charged Particle" style="width:450px; display:block; margin:auto" />

For particles entering the magnetic field at an angle other than $90^\circ$, velocity $\mathbf{v}$ has components:

$$
v_{\perp} = v \sin \theta, \quad v_{\parallel} = v \cos \theta
$$

The perpendicular component causes circular motion of radius:

$$
r = \frac{m v_{\perp}}{q B}
$$

Meanwhile, the parallel component moves the particle along the magnetic field, resulting in a helical trajectory. The pitch $p$ is the distance moved parallel to the field in one revolution:

$$
p = v_{\parallel} T = v \cos \theta \times \frac{2\pi m}{q B}
$$

**Example:** If $v = 3 \times 10^6 m/s$, $\theta = 30^\circ$, $B=0.1 T$ for a proton, find radius and pitch.

Radius:

$$
r = \frac{m v \sin \theta}{q B} = \frac{1.67 \times 10^{-27} \times 3 \times 10^6 \times 0.5}{1.6 \times 10^{-19} \times 0.1} \approx 0.157 \, m
$$

Pitch:

$$
p = v \cos \theta \times \frac{2\pi m}{qB} = 3 \times 10^{6} \times 0.866 \times \frac{2\pi \times 1.67 \times 10^{-27}}{1.6 \times 10^{-19} \times 0.1} \approx 0.341 \, m
$$

Such motion is critical to understanding cosmic ray trajectories and designing particle beam paths.

---

## 4.4 Force on a Current-Carrying Conductor in a Magnetic Field

<img src="https://i.imgur.com/AN5cMle.png" alt="Force on Current-Carrying Wire" style="width:450px; display:block; margin:auto" />

A current-carrying conductor placed in a magnetic field experiences a force due to the magnetic field acting on the moving charges in the conductor.

The force magnitude on a wire segment of length $L$ carrying current $I$ in magnetic field $\mathbf{B}$ is:

$$
F = I L B \sin \theta
$$

where $\theta$ is the angle between the wire and the magnetic field.

**Vectorially:**

$$
\mathbf{F} = I \mathbf{L} \times \mathbf{B}
$$

This force is the cumulative effect of Lorentz force on all charge carriers.

**Magnetic Torque on Current Loop:**

For a rectangular current loop of area $A$ placed in uniform magnetic field,

$$
\tau = I A B \sin \theta = m B \sin \theta
$$

where $m = I A$ is the magnetic dipole moment.

**Example 1:** Calculate force on a 1.5 m wire carrying 3 A current in a 0.2 T magnetic field perpendicular to wire.

$$
F = I L B = 3 \times 1.5 \times 0.2 = 0.9 \, N
$$

**Example 2:** Calculate torque on a rectangular loop of dimensions $0.2 m \times 0.1 m$ carrying current 2 A in 0.3 T magnetic field at $45^\circ$.

Area $A = 0.02\, m^2$,  
$$
\tau = I A B \sin 45^\circ = 2 \times 0.02 \times 0.3 \times \frac{\sqrt{2}}{2} = 0.0085 \, Nm
$$

**Applications:** Operating principle in electric motors is based on this magnetic force and torque on current-carrying conductors.

---

## 4.5 Biot–Savart Law

### 4.5.1 Statement and Mathematical Expression

<img src="https://i.imgur.com/x5uif7n.png" alt="Biot-Savart setup" style="width:450px; display:block; margin:auto" />

Biot–Savart law gives the magnetic field $\mathbf{B}$ at point $P$ due to a small current element $I d\mathbf{l}$:

$$
d\mathbf{B} = \frac{\mu_0}{4\pi} \frac{I d\mathbf{l} \times \hat{\mathbf{r}}}{r^2}
$$

Here:

- $\mu_0 = 4\pi \times 10^{-7} \,T \cdot m/A$ is the permeability of free space.  
- $d\mathbf{l}$: infinitesimal length vector of the current element.  
- $\hat{\mathbf{r}}$: unit vector from current element to point $P$.  
- $r$: distance from current element to point $P$.

This law is the magnetic analog of Coulomb’s law in electrostatics and can be integrated over the conductor to find the net field.

**Example:** Calculate magnetic field at point $P$ due to small segment of wire carrying current 5 A at distance 0.1 m.

For infinitely small element directed perpendicular to $\hat{\mathbf{r}}$:

$$
dB = \frac{\mu_0}{4 \pi} \frac{I dl \sin \theta}{r^2}
$$

Using appropriate geometry yields exact value after integrating.

### 4.5.2 Applications of Biot–Savart Law

Common applications are calculating fields due to:

- **Long straight wire** at distance $r$:

$$
B = \frac{\mu_0 I}{2 \pi r}
$$

- **Circular current loop** at center:

$$
B = \frac{\mu_0 I}{2 R}
$$

where $R$ is loop radius.

- **On axis of loop and solenoid:** extend integration using Biot–Savart law.

**Example:** Field at 5 cm from 2 A wire:

$$
B = \frac{4\pi \times 10^{-7} \times 2}{2 \pi \times 0.05} = 4 \times 10^{-6} T
$$

**Applications:** Precise magnetic field estimations in cables and electrical machines.

---

## 4.6 Ampère’s Circuital Law

### 4.6.1 Statement and Mathematical Form

<img src="https://i.imgur.com/bnfDFK6.png" alt="Ampere's Law Path" style="width:450px; display:block; margin:auto" />

Ampere’s circuital law relates the magnetic field in space to the electric current producing it:

$$
\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{\text{enc}}
$$

This states that the line integral of $\mathbf{B}$ around a closed path equals $\mu_0$ times the net current $I_{\text{enc}}$ enclosed.

Used to calculate magnetic fields when symmetries simplify integration.

### 4.6.2 Applications of Ampere’s Law

- **Infinite straight wire:** Field at distance $r$,

$$
B = \frac{\mu_0 I}{2 \pi r}
$$

- **Long solenoid:** Inside field is uniform,

$$
B = \mu_0 n I
$$

where $n$ is number of turns per unit length.

- **Toroid:** Circular field lines with,

$$
B = \frac{\mu_0 N I}{2 \pi r}
$$

with $N$ turns and radius $r$.

**Example:** Calculate field inside solenoid of length 0.5 m with 1000 turns carrying 2 A.

$$
n = \frac{1000}{0.5} = 2000 \, turns/m
$$

$$
B = 4\pi \times 10^{-7} \times 2000 \times 2 = 5.03 \times 10^{-3} T
$$

**Applications:** Designing electromagnets, MRI machines, inductors.

---

## 4.7 Force Between Two Parallel Currents

<img src="https://i.imgur.com/LPHqkd8.png" alt="Force between Two Wires" style="width:450px; display:block; margin:auto" />

Two parallel long currents $I_1$ and $I_2$ separated by distance $d$ exert magnetic forces on each other.

Force per unit length on each wire is:

$$
\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2 \pi d}
$$

- If currents flow in same direction, wires attract.  
- If opposite, they repel.

This principle defines the **ampere** as the current which produces a force of $2 \times 10^{-7} N/m$ between two wires one meter apart.

**Example:** Two wires 0.2 m apart carry currents 2 A and 3 A. Calculate force per meter.

$$
F/L = \frac{4 \pi \times 10^{-7} \times 2 \times 3}{2 \pi \times 0.2} = 6 \times 10^{-6} N/m
$$

Direction follows right-hand rule.

**Applications:** Used in current measuring techniques and industrial setup of power lines.

---

## 4.8 Cyclotron

### 4.8.1 Principle and Basic Concept

<img src="https://i.imgur.com/N8zZuvH.png" alt="Cyclotron Diagram" style="width:450px; display:block; margin:auto" />

A cyclotron is a device used to accelerate charged particles using a constant magnetic field and an alternating electric field.

Charged particles move in circular paths within a uniform magnetic field according to:

$$
f = \frac{q B}{2 \pi m}
$$

This frequency is independent of speed, allowing synchronization with oscillating electric field for acceleration.

### 4.8.2 Construction and Working

- Two D-shaped hollow conductors (“dees”) placed between poles of a magnet.  
- Particles are injected at center and accelerated across gap by RF electric field.  
- Magnetic field bends particles in semicircular trajectories inside dees.

Particles gain kinetic energy each pass until exiting with high velocity.

### 4.8.3 Cyclotron Frequency Derivation

Using the centripetal force equality for circular motion:

$$
q v B = \frac{m v^2}{r}
$$

Time period independent of radius:

$$
T = \frac{2 \pi m}{q B}
$$

Frequency is:

$$
f = \frac{1}{T} = \frac{q B}{2 \pi m}
$$

### 4.8.4 Maximum Energy and Limitations

Maximum kinetic energy:

$$
K.E_{\max} = \frac{1}{2} m v_{\max}^2 = \frac{1}{2} m (r q B / m)^2 = \frac{q^2 B^2 r^2}{2 m}
$$

Limitations arise when particles approach relativistic speeds; mass increases causing frequency mismatch.

### 4.8.5 Applications of Cyclotron

Used in nuclear physics research, isotope production for medicine, and particle physics.

---

## 4.9 Moving Coil Galvanometer

### 4.9.1 Principle

<img src="https://i.imgur.com/B52bGHZ.png" alt="Moving Coil Galvanometer" style="width:450px; display:block; margin:auto" />

A moving coil galvanometer works on the torque produced when a current-carrying coil is placed in a magnetic field. The coil experiences a torque causing rotation, which moves a pointer over a calibrated scale.

Torque on coil:

$$
\tau = N I A B \sin \theta
$$

where $N$ = number of turns, $I$ = current, $A$ = area of coil, $B$ = magnetic field, $\theta$ = angle between coil plane and magnetic field (usually $90^\circ$).

### 4.9.2 Construction

Consists of:

- Rectangular coil suspended by thin wire with known torsion constant.  
- Permanent magnets produce radial magnetic field ensuring uniform torque.  
- Pointer attached to coil moves over scale.  
- Suspension wire provides restoring torque.

### 4.9.3 Theory and Derivation

At equilibrium:

$$
\tau_{\text{magnetic}} = \tau_{\text{restoring}} \implies N I A B = k \theta
$$

where $k$ is torsion coefficient.

Deflection $\theta$ proportional to current $I$, allowing measurement.

### 4.9.4 Current Sensitivity

Current sensitivity $S_I$ defined as deflection per unit current:

$$
S_I = \frac{\theta}{I} = \frac{N A B}{k}
$$

Enhancing $S_I$ improves galvanometer's sensitivity.

### 4.9.5 Voltage Sensitivity

Voltage sensitivity $S_V$ defined as deflection per unit voltage:

$$
S_V = \frac{\theta}{V} = \frac{N A B}{k R}
$$

where $R$ is coil resistance.

### 4.9.6 Conversion to Ammeter

Adding a low resistance (shunt) $S$ in parallel enables the galvanometer to measure large currents:

$$
S = \frac{I_g G}{I - I_g}
$$

where $I_g$ is galvanometer current, $G$ its resistance, and $I$ the full current.

### 4.9.7 Conversion to Voltmeter

Adding a high resistance $R$ in series converts galvanometer to voltmeter:

$$
R = \frac{V}{I_g} - G
$$

Allows measurement of voltage by limiting current through galvanometer.

---

## Summary

Chapter 4, *Moving Charges and Magnetism*, elucidates the profound interplay between electric currents, moving charges, and magnetism—fundamental pillars of electromagnetism. Beginning with Oersted’s historic discovery linking currents to magnetic fields, the chapter builds up a comprehensive understanding of how magnetic forces arise from moving charges and how these forces dictate particle and conductor behavior.

The Lorentz force law encapsulates the combined effects of electric and magnetic fields acting on a charge, showing the magnetic force as perpendicular to both velocity and field, altering direction but not speed. The concept of trajectories—circular and helical—emerges naturally from this force law, with formulae for the radius of curvature and pitch providing precise quantitative descriptions of charged particle motion in uniform magnetic fields. These motions underpin practical devices like cyclotrons that accelerate particles using synchronized magnetic and electric fields.

Passage from microscopic forces on charges to macroscopic forces on current-carrying conductors is bridged elegantly by the relation $F = I L B \sin \theta$, highlighting physical reality that moving charges inside a conductor collectively experience the magnetic force leading to phenomena such as torque on current loops—forming the principle behind electric motors.

The Biot–Savart law extends Coulomb’s analogy to magnetism, providing the fundamental expression to calculate magnetic fields due to currents in varied geometries. Complementarily, Ampère’s circuital law offers an integral form relating total magnetic field circulation to enclosed current, particularly effective in highly symmetric situations.

Interactions between parallel current-carrying wires reveal magnetic forces that are foundational not only for theoretical constructs but also for defining the ampere—an SI unit—and for practical wiring and industrial current measurement.

In exploring instruments, the chapter details the moving coil galvanometer's construction and quantitative working, delineating sensitivity parameters and conversion to ammeters and voltmeters that are crucial for precise current and voltage measurements.

Applications permeate the chapter’s scope: from fundamental physics experiments in accelerators to ubiquitous electric motors and contemporary medical technology like MRI, showcasing the omnipresence of electromagnetism in science and engineering.

Experimentally verified principles, intuitive right and left hand rules, and rigorous derivations come together to provide students a robust, interconnected understanding empowering both conceptual grasp and practical problem-solving. Thus, the chapter serves as a critical foundation connecting to subsequent studies in electromagnetic induction, alternating currents, and quantum applications.

---

## Practice Questions

1. Define magnetic field and explain its origin around a current-carrying conductor.  
2. State and explain Oersted’s experiment and its significance.  
3. What is the Lorentz force? Write its expression and discuss the direction of force for a positively charged particle.  
4. Why does the magnetic force do no work on a moving charged particle?  
5. A proton moves perpendicular to a magnetic field of 0.5 T with velocity $1 \times 10^6 m/s$. Calculate the radius of its circular path.  
6. Explain the difference between circular and helical motion of charged particles in magnetic fields with examples.  
7. Derive the expression for force on a current-carrying conductor placed in a magnetic field.  
8. A wire 1 m long carrying a current of 3 A is placed perpendicularly in a magnetic field of 0.4 T. Calculate the force on the wire.  
9. State Biot–Savart law. How is it used to find the magnetic field due to a current element?  
10. Calculate the magnetic field at 0.1 m from a straight wire carrying 5 A current.  
11. Using Ampere’s circuital law, find the magnetic field inside a long solenoid of length 0.4 m with 800 turns carrying 2 A.  
12. Two parallel conductors 0.3 m apart carry currents of 4 A and 6 A in opposite directions. Find the force per unit length between the conductors.  
13. Explain the principle and working of a cyclotron. Derive the expression for cyclotron frequency.  
14. What limits the maximum energy of particles in a cyclotron?  
15. Describe the construction and working of a moving coil galvanometer.  
16. Derive the expression for current sensitivity of a moving coil galvanometer.  
17. How is a galvanometer converted into an ammeter? Write the formula for the shunt resistance required.  
18. Explain the procedure to convert a galvanometer into a voltmeter with the relevant formula.  
19. A galvanometer with resistance 50 Ω and current sensitivity 5°/μA is converted into an ammeter to measure 1 A full scale. Calculate the shunt resistance required.  
20. A proton moves at $2 \times 10^6 m/s$ in a magnetic field 0.02 T at an angle of 60°. Calculate radius and pitch of the helical path.  
21. Explain the role of earth’s magnetic field in the motion of charged particles in the atmosphere.  
22. How can you find the direction of the magnetic field due to a straight current carrying wire?  
23. Calculate magnetic torque on a rectangular coil of 0.3 m by 0.4 m carrying 3 A current placed at 30° in a 0.2 T magnetic field.  
24. A charged particle moves with velocity $3 \times 10^6 m/s$ perpendicular to magnetic field 0.05 T. What is the time period of circular motion if particle mass is $9.1 \times 10^{-31} kg$ and charge is $1.6 \times 10^{-19} C$?  
25. Explain the significance of the force between two parallel current carrying conductors in defining the ampere.  
26. Describe one real-world application each for the Lorentz force, cyclotron, and moving coil galvanometer.  
27. A wire carries current of 10 A and is subjected to a uniform magnetic field of 0.3 T at 90°. What is the force acting on 2 meters of this wire?  
28. Derive the relationship between pitch of helical motion and velocity components along a uniform magnetic field.  
29. Why is the magnetic field inside a toroid confined largely within the core?  
30. Explain how the Biot–Savart law and Ampere’s law complement each other in magnetic field calculations.

---

# End of Chapter 4: Moving_Charges_and_Magnetism