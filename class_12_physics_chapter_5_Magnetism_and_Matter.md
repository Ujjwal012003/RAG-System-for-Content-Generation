---
title: "Magnetism_and_Matter"
author: "Class 12 Physics"
date: 2024-06
subject: Physics
chapter: 5
language: en
---

# Chapter 5: Magnetism_and_Matter

## Table of Contents

1. [5.1 Introduction](#51-introduction)  
2. [5.2 Magnetic Field and Magnetic Forces](#52-magnetic-field-and-magnetic-forces)  
   - [5.2.1 Magnetic Field Lines and Their Properties](#521-magnetic-field-lines-and-their-properties)  
   - [5.2.2 Force on a Moving Charge in a Magnetic Field](#522-force-on-a-moving-charge-in-a-magnetic-field)  
3. [5.3 Magnetic Dipole and Magnetic Moment](#53-magnetic-dipole-and-magnetic-moment)  
   - [5.3.1 Torque on a Magnetic Dipole](#531-torque-on-a-magnetic-dipole)  
   - [5.3.2 Potential Energy of a Magnetic Dipole](#532-potential-energy-of-a-magnetic-dipole)  
4. [5.4 Magnetisation and Magnetic Intensity](#54-magnetisation-and-magnetic-intensity)  
5. [5.5 Magnetic Susceptibility and Permeability](#55-magnetic-susceptibility-and-permeability)  
6. [5.6 Types of Magnetic Materials](#56-types-of-magnetic-materials)  
   - [5.6.1 Diamagnetic Materials](#561-diamagnetic-materials)  
   - [5.6.2 Paramagnetic Materials](#562-paramagnetic-materials)  
   - [5.6.3 Ferromagnetic Materials](#563-ferromagnetic-materials)  
   - [5.6.4 Superconductors](#564-superconductors)  
7. [5.7 Magnetic Properties of Materials](#57-magnetic-properties-of-materials)  
8. [5.8 Biot-Savart Law](#58-biot-savart-law)  
9. [5.9 Ampere's Circuital Law](#59-amperes-circuital-law)  
10. [5.10 Gauss's Law for Magnetism](#510-gausss-law-for-magnetism)  
11. [5.11 Electromagnetic Induction and Magnetism](#511-electromagnetic-induction-and-magnetism)  

[Summary](#summary)  
[Practice Questions](#practice-questions)

---

## 5.1 Introduction

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/3/38/Magnetic_field_lines_around_a_bar_magnet.png" alt="Magnetic field lines around a bar magnet showing dipole nature" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.1:</b> Magnetic field lines around a bar magnet representing the dipole nature of magnetism</i></figcaption> 
</figure>

Magnetism is a fundamental physical phenomenon resulting from the motion of electric charges and the intrinsic magnetic moments associated with elementary particles such as electrons. It manifests itself as forces between magnets, currents, and magnetic materials. Unlike electrostatics, where charges at rest produce electric fields, magnetic fields arise only from moving charges or changing electric fields, reflecting the deep interplay between electricity and magnetism encapsulated in Maxwell’s equations.

Historically, magnetism was first noted through the properties of natural lodestones, which have the ability to attract iron and align themselves along Earth’s magnetic field. This led to the discovery that magnetism can be described by a vector field $\mathbf{B}$—the magnetic field—which permeates space around magnets and current-carrying conductors. The direction of $\mathbf{B}$ at any point assigns the direction of the force it exerts on moving charges or magnetic dipoles.

The fundamental unit of magnetism is the magnetic dipole moment, a vector quantity characterizing the strength and orientation of a magnet or current loop. Magnetic fields exert forces and torques on these dipoles, leading to energy changes that form the basis for many technologies such as electric motors and generators.

Mathematically, the magnetic flux density $\mathbf{B}$ relates to the magnetic field intensity $\mathbf{H}$ and the magnetisation vector $\mathbf{M}$ of a material by:
$$
\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M}) = \mu \mathbf{H}
$$
where $\mu_0$ denotes the permeability of free space, and the permeability of the material $\mu$ is defined as $\mu = \mu_0 (1 + \chi)$, $\chi$ being the magnetic susceptibility.

Materials respond differently to magnetic fields based on their electronic structures, classified primarily as diamagnetic, paramagnetic, or ferromagnetic, determined by their susceptibility $\chi$. Diamagnetic materials are repelled weakly, paramagnetic materials are weakly attracted, while ferromagnets show strong attraction and retain magnetization even without an external field.

Exploring magnetism provides insights into atomic physics—especially electron spin and orbital angular momentum—and facilitates numerous practical applications spanning from medical imaging technologies to maglev transportation. Understanding magnetic forces is also crucial to fundamental physics experiments and modern electric devices.

**Conceptual Example:**  
Consider a compass needle, which behaves as a small magnetic dipole. When placed near a bar magnet, the needle aligns with the magnetic field lines due to the torque exerted on its magnetic moment by the external magnetic field. This simple experiment demonstrates how magnetic dipoles tend to orient along the direction of $\mathbf{B}$, revealing the vector nature of the magnetic field and introducing the concept of torque in magnetic phenomena.

**Mathematical Example:**  
**Problem:** A magnetic dipole of moment $m = 3 \times 10^{-3}$ A·m$^2$ is placed in a uniform magnetic field $B = 0.6$ T. Calculate the torque on the dipole when it makes an angle of $45^\circ$ with the magnetic field.

**Given:**  
- $m = 3 \times 10^{-3}$ A·m$^2$  
- $B = 0.6$ T  
- $\theta = 45^\circ$  

**Solution:**  
Torque on magnetic dipole is given by:  
$$
\tau = m B \sin \theta
$$  
Calculate $\sin 45^\circ$:  
$$
\sin 45^\circ = \frac{\sqrt{2}}{2} \approx 0.707
$$  
Substitute values:  
$$
\tau = (3 \times 10^{-3}) \times 0.6 \times 0.707 = 1.27 \times 10^{-3} \text{ N·m}
$$  

**Answer:** The torque acting on the dipole is approximately $1.27 \times 10^{-3}$ newton meter.

---

## 5.2 Magnetic Field and Magnetic Forces

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/c/c4/Right-Hand-Rule.svg" alt="Right hand rule for magnetic force" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.2:</b> Right hand rule to determine direction of magnetic force on a moving charge</i></figcaption> 
</figure>

Magnetic fields arise around moving electric charges and current-carrying conductors. The magnetic field is a vector field $\mathbf{B}$ defined so that it exerts a force on moving charged particles and magnetic dipoles. The SI unit of magnetic field is the tesla (T), where $1~\mathrm{T} = 1~\mathrm{N/(A \cdot m)}$.

### 5.2.1 Magnetic Field Lines and Their Properties

Magnetic field lines are continuous closed curves with no beginning or end, illustrating the nature of magnetic fields. These lines emerge from the north pole of a magnet and enter the south pole, forming loops outside the magnet and continuing through it. The density of field lines indicates the magnetic field strength. Unlike electric field lines that start and end on charges, magnetic field lines never terminate, implying the absence of magnetic monopoles.

Key properties of magnetic field lines are: they never intersect, they form closed loops, and the tangent to a line at any point gives the field direction there. Observation of iron filings around a magnet reveals the pattern of these lines visually.

### 5.2.2 Force on a Moving Charge in a Magnetic Field

A charged particle with charge $q$ moving with velocity $\mathbf{v}$ in a magnetic field $\mathbf{B}$ experiences a force called the Lorentz force, given by:
$$
\mathbf{F} = q(\mathbf{v} \times \mathbf{B})
$$
This force acts perpendicular to both the velocity and the magnetic field, changing the direction of the particle’s motion without doing work (no change in kinetic energy).

The magnitude of the force is:
$$
F = qvB \sin \theta
$$
where $\theta$ is the angle between $\mathbf{v}$ and $\mathbf{B}$. If $\mathbf{v}$ is parallel or antiparallel to $\mathbf{B}$, the magnetic force is zero.

The direction of the force is determined by the right hand rule: pointing the fingers in the direction of $\mathbf{v}$ and curling them towards $\mathbf{B}$, the thumb points in the direction of $\mathbf{F}$ for a positive charge; for negative charges, force direction is opposite.

**Conceptual Example:**  
An electron moving horizontally eastward enters a magnetic field directed vertically downward. Applying the right hand rule (reversed for electron), the force acts perpendicularly to both directions, causing the electron to move in a circular path. This explains the bending of electron beams in cathode ray tubes.

**Mathematical Example:**  
**Problem:** A proton with charge $1.6 \times 10^{-19}$ C moves with velocity $5 \times 10^6$ m/s perpendicular to a uniform magnetic field of strength $0.2$ T. Find the magnitude of the force experienced by the proton.

**Solution:**  
Given,  
$q = 1.6 \times 10^{-19}$ C,  
$v = 5 \times 10^6$ m/s,  
$B = 0.2$ T,  
$\theta = 90^\circ$, so $\sin \theta = 1$.

Force magnitude:  
$$
F = q v B \sin \theta = 1.6 \times 10^{-19} \times 5 \times 10^6 \times 0.2 \times 1 = 1.6 \times 10^{-13} \text{ N}
$$  

**Answer:** The proton experiences a force of $1.6 \times 10^{-13}$ newtons perpendicular to its velocity and the magnetic field.

---

## 5.3 Magnetic Dipole and Magnetic Moment

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Magnet_dipole.svg" alt="Magnetic dipole and moment representation" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.3:</b> Magnetic dipole moment direction and notation</i></figcaption> 
</figure>

A magnetic dipole consists of two equal and opposite magnetic poles separated by a distance. The magnetic dipole moment $\mathbf{m}$ characterizes the strength and orientation of a dipole and is a vector quantity defined as:
$$
\mathbf{m} = I \mathbf{A}
$$
where $I$ is the current and $\mathbf{A}$ is the area vector of a current loop.

Magnetic dipoles behave like tiny bar magnets. When placed in an external magnetic field, they experience torque and potential energy changes which affect their orientation.

### 5.3.1 Torque on a Magnetic Dipole

If a magnetic dipole $\mathbf{m}$ is placed in an external magnetic field $\mathbf{B}$, it experiences a torque $\boldsymbol{\tau}$ given by:
$$
\boldsymbol{\tau} = \mathbf{m} \times \mathbf{B}
$$
The magnitude of this torque is:
$$
\tau = m B \sin \theta
$$
where $\theta$ is the angle between $\mathbf{m}$ and $\mathbf{B}$. This torque tends to align the magnetic dipole moment along the magnetic field direction.

### 5.3.2 Potential Energy of a Magnetic Dipole

The potential energy $U$ of a magnetic dipole in a magnetic field depends on its orientation:
$$
U = -\mathbf{m} \cdot \mathbf{B} = -m B \cos \theta
$$
The minimum energy occurs when $\mathbf{m}$ aligns parallel to $\mathbf{B}$ ($\theta = 0^\circ$), and the maximum when anti-parallel ($\theta = 180^\circ$).

**Conceptual Example:**  
A tiny current loop suspended in a magnetic field oscillates when displaced from an equilibrium orientation because of the restoring torque produced by the field on its magnetic dipole moment. This principle is exploited in galvanometers.

**Mathematical Example:**  
**Problem:** A circular current loop of radius $5$ cm carries a current of $2$ A in a uniform magnetic field of $0.1$ T. Calculate the torque on the loop if the plane of the loop makes an angle of $60^\circ$ with the magnetic field.

**Solution:**  
The magnetic moment magnitude:  
$$
m = I A = I \pi r^2 = 2 \times \pi \times (0.05)^2 = 2 \times \pi \times 0.0025 = 0.0157 \text{ A·m}^2
$$  
Torque magnitude:  
$$
\tau = m B \sin \theta = 0.0157 \times 0.1 \times \sin 60^\circ = 0.0157 \times 0.1 \times 0.866 = 0.00136 \text{ N·m}
$$  

**Answer:** The torque acting on the loop is $1.36 \times 10^{-3}$ newton meter.

---

## 5.4 Magnetisation and Magnetic Intensity

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Magnetization.svg/480px-Magnetization.svg.png" alt="Magnetisation vector in material" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.4:</b> Magnetisation vector $\mathbf{M}$ representing magnetic dipole moments per unit volume</i></figcaption> 
</figure>

Magnetisation $\mathbf{M}$ of a material is the vector quantity that gives the net magnetic dipole moment per unit volume within the material:
$$
\mathbf{M} = \frac{\text{Net magnetic moment}}{\text{Volume}}
$$

When a material is placed in an external magnetic field $\mathbf{H}$ (magnetic field intensity), its atomic or molecular dipoles tend to align, producing magnetisation. The magnetic flux density $\mathbf{B}$ in the material relates to $\mathbf{H}$ and $\mathbf{M}$ via:
$$
\mathbf{B} = \mu_0 (\mathbf{H} + \mathbf{M})
$$

The intensity of magnetisation depends on the nature of the material and the strength of the applied magnetic field. In vacuum or air, magnetisation is zero, and $\mathbf{B} = \mu_0 \mathbf{H}$.

**Conceptual Example:**  
Consider iron filings sprinkled over a magnet; the filings align themselves along magnetic field lines, thus reflecting magnetisation of individual particles and producing a visible pattern indicating $\mathbf{M}$.

**Mathematical Example:**  
**Problem:** A sample of a magnetic material of volume $10^{-4}$ m$^3$ has a net magnetic moment of $2 \times 10^{-3}$ A·m$^2$. Find its magnetisation.

**Solution:**
$$
M = \frac{\text{Magnetic moment}}{\text{Volume}} = \frac{2 \times 10^{-3}}{10^{-4}} = 20 \text{ A/m}
$$

**Answer:** The magnetisation of the material is $20$ A/m.

---

## 5.5 Magnetic Susceptibility and Permeability

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/0/02/Permeability_and_susceptibility.png" alt="Graph of magnetic susceptibility and relative permeability" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.5:</b> Relative permeability and magnetic susceptibility in magnetic materials</i></figcaption> 
</figure>

Magnetic susceptibility $\chi$ is a dimensionless quantity that measures the degree to which a material is magnetised in response to an applied magnetic intensity $\mathbf{H}$:
$$
\mathbf{M} = \chi \mathbf{H}
$$
Susceptibility can be positive or negative depending on the material.

Magnetic permeability $\mu$ is a measure of the material’s ability to support the formation of a magnetic field within it. The relation is:
$$
\mathbf{B} = \mu \mathbf{H}
$$
where
$$
\mu = \mu_0 (1 + \chi)
$$

Materials with $\chi > 0$ are paramagnetic or ferromagnetic, and those with $\chi < 0$ are diamagnetic.

**Conceptual Example:**  
A paramagnetic salt placed in a magnetic field becomes weakly magnetised, increasing the field inside the material slightly due to $\chi > 0$.

**Mathematical Example:**  
**Problem:** A material has a magnetic susceptibility of $0.005$. Calculate its permeability given that $\mu_0 = 4\pi \times 10^{-7}$ T·m/A.

**Solution:**
$$
\mu = \mu_0 (1 + \chi) = 4\pi \times 10^{-7} \times (1 + 0.005) = 4\pi \times 10^{-7} \times 1.005 \approx 1.26 \times 10^{-6} \text{ T·m/A}
$$  

**Answer:** The permeability $\mu$ is approximately $1.26 \times 10^{-6}$ T·m/A.

---

## 5.6 Types of Magnetic Materials

### 5.6.1 Diamagnetic Materials

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Diamagnetic_magnetic_fields.svg" alt="Diamagnetic materials magnetic response illustration" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.6.1:</b> Diamagnetic material repelling magnetic field lines</i></figcaption> 
</figure>

Diamagnetic materials create an induced magnetic moment in a direction opposite to the applied magnetic field. This weak repulsion occurs in all materials but is dominant when other types of magnetism are absent. Their susceptibility $\chi$ is small and negative.

Common diamagnetic materials include copper, silver, gold, and bismuth.

**Mathematical Example:**  
**Problem:** If a diamagnetic material has $\chi = -1.2 \times 10^{-5}$ and is placed in a magnetic field of $10^4$ A/m, find the magnetisation.

**Solution:**
$$
M = \chi H = -1.2 \times 10^{-5} \times 10^4 = -0.12 \text{ A/m}
$$  

**Answer:** The magnetisation is $-0.12$ A/m, indicating a weak opposing magnetic moment.

---

### 5.6.2 Paramagnetic Materials

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Paramagnetic.svg" alt="Paramagnetic material magnetic alignment" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.6.2:</b> Paramagnetic material aligning weakly with magnetic field</i></figcaption> 
</figure>

Paramagnetic materials have permanent atomic magnetic moments due to unpaired electrons but no net magnetisation without an external field. When a field is applied, these moments align partially in the same direction, resulting in a small positive susceptibility.

Examples include aluminum and platinum.

---

### 5.6.3 Ferromagnetic Materials

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/f/f8/Ferromagnetism_domain_walls.svg" alt="Ferromagnetic domain structure" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.6.3:</b> Ferromagnetic domains and domain walls inside a ferromagnet</i></figcaption> 
</figure>

Ferromagnetic materials exhibit spontaneous magnetisation even without an external magnetic field due to parallel alignment of atomic moments in domains. They have large positive susceptibilities and can retain magnetisation after the external field is removed (hysteresis).

Common ferromagnets are iron, cobalt, and nickel.

---

### 5.6.4 Superconductors

Superconductors are materials that below a critical temperature exhibit zero electrical resistance and perfect diamagnetism (Meissner effect), expelling magnetic fields completely.

---

## 5.7 Magnetic Properties of Materials

The magnetic properties determine how materials respond to magnetic fields—characterised chiefly by susceptibility $\chi$ and permeability $\mu$. These properties influence the design of transformers, inductors, and recording media. The temperature dependence of $\chi$ is crucial, exemplified by the Curie-Weiss law in ferromagnets.

---

## 5.8 Biot-Savart Law

<figure style="display: flex; flex-direction: column; align-items: center;"> 
<img src="https://upload.wikimedia.org/wikipedia/commons/5/52/Biot-Savart_law.svg" alt="Biot-Savart law geometry" style="max-width: 90%; height: auto;"> 
<figcaption style="text-align: center; margin-top: 8px;">
<i><b>Figure 5.8:</b> Geometry defining Biot-Savart law</i></figcaption> 
</figure>

Biot-Savart law relates the magnetic field $\mathbf{B}$ at a point due to a small current element $I d\mathbf{l}$:
$$
d\mathbf{B} = \frac{\mu_0}{4\pi} \frac{I d\mathbf{l} \times \mathbf{\hat{r}}}{r^2}
$$
where $\mathbf{\hat{r}}$ is the unit vector from the current element to the point, and $r$ is the distance.

Using integration, the magnetic field of arbitrary current configurations can be found.

**Mathematical Example:**  
The magnetic field at the center of circular coil of radius $R$ carrying current $I$ is:
$$
B = \frac{\mu_0 I}{2R}
$$

---

## 5.9 Ampere's Circuital Law

Ampere’s law states that the line integral of the magnetic field around a closed path equals $\mu_0$ times the net current enclosed:
$$
\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{\text{enclosed}}
$$

It is used to find magnetic fields with high symmetry, like inside solenoids and toroids.

---

## 5.10 Gauss's Law for Magnetism

Gauss's law in magnetism states that the net magnetic flux through any closed surface is zero:
$$
\oint \mathbf{B} \cdot d\mathbf{A} = 0
$$
This implies there are no magnetic monopoles; magnetic field lines always form closed loops.

---

## 5.11 Electromagnetic Induction and Magnetism

Changing magnetic fields can induce electric currents in conductors, a phenomenon described by Faraday’s law of electromagnetic induction. This underlines the dynamic relationship between electric and magnetic fields.

---

## Summary

The chapter “Magnetism and Matter” builds a comprehensive framework elucidating the origins, properties, and applications of magnetic phenomena. Beginning with the fundamental notion that magnetism emerges from moving electric charges and intrinsic magnetic moments, the chapter establishes the magnetic field $\mathbf{B}$ as a vector field that mediates forces on charged particles and magnetic dipoles. The concept of magnetic dipole moment forms a central theme, quantifying magnetic strength and direction and introducing the physical reality that dipoles experience torques and potential energy variations in magnetic fields. These foundational topics provide the groundwork to understand the behavior of magnetic materials and the basis for electromagnetic devices.

The magnetic force on a moving charge demonstrates the interplay between velocity and magnetic fields, producing a Lorentz force perpendicular to particle motion. Magnetic field lines illustrate the nature of magnetic fields as closed continuous loops, offering visual insight into field strength and direction. Biot-Savart law and Ampere’s circuital law provide essential tools for calculating magnetic fields from different current configurations, showing how currents generate magnetic fields in space. Ampere’s law complements these by simplifying field calculations in symmetric systems like solenoids, while Gauss’s law for magnetism highlights the absence of magnetic monopoles, an intrinsic symmetry of magnetic fields.

Magnetisation and magnetic intensity describe how materials respond to applied magnetic fields via induced or aligned atomic dipoles. This leads to the introduction of magnetic susceptibility $\chi$ and permeability $\mu$, which quantify how easily materials become magnetised and influence the resultant magnetic flux density. Understanding these concepts is vital in classifying materials as diamagnetic, paramagnetic, or ferromagnetic based on their intrinsic electron structures and resultant magnetic responses. The unique behavior of superconductors, showing perfect diamagnetism, emphasizes the diverse material responses under different conditions.

Conceptual and mathematical examples throughout the chapter ground theory in practical scenarios, reinforcing the significance of magnetic torque on current loops and dipoles, forces on moving charges, and calculations of magnetic fields around conductors. These examples bridge theory and experiment, illustrating the principles that underpin devices such as galvanometers, electric motors, MRI machines, and maglev trains.

In practical applications, the principles of magnetism unlock technologies critical to modern life–from electric power generation and electronic storage to medical imaging and transportation. Experimentally, mapping magnetic fields with iron filings or quantifying force on moving charges has provided empirical validation of theoretical models. Furthermore, the chapter’s treatment opens a pathway to advanced topics in electromagnetism, preparing students for the intricate connection between electric and magnetic fields explored in subsequent chapters.

Overall, the chapter delivers a coherent study of magnetism, interconnecting physical laws with material properties and technological applications. Its coverage offers students a robust understanding of how magnets influence the physical world and enables innovations that drive scientific progress.

---

## Practice Questions

1. Define magnetic dipole moment. How is it related to current and area?

2. Explain why magnetic field lines never intersect.

3. State and explain the right hand rule for determining the direction of magnetic force on a moving charge.

4. Calculate the force on an electron moving with velocity $2 \times 10^6$ m/s perpendicular to a magnetic field of strength $0.3$ T.

5. Two magnetic dipoles $m_1 = 5 \times 10^{-3}$ A·m$^2$ and $m_2 = 8 \times 10^{-3}$ A·m$^2$ are placed in a uniform magnetic field $0.4$ T at angles 60° and 45°, respectively. Calculate the torque acting on each dipole.

6. What is magnetisation? How does it differ from magnetic intensity?

7. Calculate the magnetisation of a material having net magnetic moment $0.01$ A·m$^2$ occupying volume $5 \times 10^{-5}$ m$^3$.

8. Define magnetic susceptibility and permeability. How are they related?

9. A material has $\chi = -2 \times 10^{-5}$. Identify the type of magnetic material and explain its behavior in a magnetic field.

10. Describe the difference in magnetic behaviour between paramagnetic and ferromagnetic materials.

11. Using Biot-Savart law, derive the expression for magnetic field at the center of a circular current-carrying loop.

12. Find the magnetic field at the center of a circular coil of radius $20$ cm carrying $5$ A current.

13. State Ampere’s circuital law and use it to find the magnetic field inside a long solenoid having $1000$ turns per meter carrying current $2$ A.

14. Explain Gauss’s law for magnetism. What does it imply about magnetic monopoles?

15. Calculate the torque acting on a rectangular loop of dimensions $0.1$ m by $0.2$ m carrying current $3$ A in a magnetic field of 0.5 T when the plane of the loop is at 30° to the field.

16. A proton moves with speed $4 \times 10^6$ m/s parallel to a magnetic field of strength $0.1$ T. Calculate the magnetic force on the proton.

17. Discuss the phenomenon of electromagnetic induction and its relation to magnetic field changes.

18. Explain the Meissner effect in superconductors.

19. Derive expression for potential energy of a magnetic dipole in a magnetic field.

20. Calculate the magnetic flux density inside a material having magnetic intensity $1000$ A/m and susceptibility $0.003$.

21. A magnetic dipole experiences a torque of $2 \times 10^{-4}$ N·m in a magnetic field of strength $0.2$ T. Find the magnetic moment if torque is maximum.

22. Explain hysteresis in ferromagnetic materials and its significance.

23. Determine the force on a charged particle moving at an angle of $60^\circ$ to the magnetic field.

24. Calculate the number of turns per unit length of a solenoid if the magnetic field inside for a current of 3 A is $7.54 \times 10^{-3}$ T.

25. Discuss how magnetic materials are used in data storage devices.

26. A copper rod moves with velocity $10$ m/s perpendicular to a magnetic field of $0.2$ T. Calculate the emf induced between ends if the length of rod is $0.5$ m.

27. Explain why work done by magnetic force on a charged particle is zero.

28. Calculate the relative permeability of a material with susceptibility $0.02$.

29. A magnetic dipole is oriented at $90^\circ$ to a magnetic field of $0.1$ T. If torque on it is $4 \times 10^{-3}$ N·m, find the magnetic moment.

30. Describe the use of magnetic fields in magnetic resonance imaging (MRI).

---

# End of Chapter 5: Magnetism_and_Matter