---
title: "Electric_Charges_and_Fields"
author: "Class 12 Physics"
date: 2024-06
subject: Physics
chapter: 1
language: en
---

# Chapter 1: Electric_Charges_and_Fields

## Table of Contents

1. [1.1 Introduction](#11-introduction)  
2. [1.2 Electric Charges](#12-electric-charges)  
3. [1.3 Conservation of Charge](#13-conservation-of-charge)  
4. [1.4 Coulomb’s Law](#14-coulombs-law)  
5. [1.5 Force Between Multiple Charges; Superposition Principle](#15-force-between-multiple-charges-superposition-principle)  
   - [1.5.1 Superposition Principle](#151-superposition-principle)  
6. [1.6 Electric Field, Definition](#16-electric-field-definition)  
7. [1.7 Electric Field Due to a Point Charge](#17-electric-field-due-to-a-point-charge)  
8. [1.8 Electric Field Lines](#18-electric-field-lines)  
9. [1.9 Electric Dipole](#19-electric-dipole)  
   - [1.9.1 Electric Dipole Moment](#191-electric-dipole-moment)  
   - [1.9.2 Electric Field Due to an Electric Dipole](#192-electric-field-due-to-an-electric-dipole)  
10. [1.10 Torque on an Electric Dipole in a Uniform Electric Field](#110-torque-on-an-electric-dipole-in-a-uniform-electric-field)  
11. [1.11 Electric Flux](#111-electric-flux)  
12. [1.12 Gauss’s Law and Its Applications](#112-gausss-law-and-its-applications)  
    - [1.12.1 Gauss’s Law Statement and Mathematical Form](#1121-gausss-law-statement-and-mathematical-form)  
    - [1.12.2 Applications](#1122-applications)  

[Summary](#summary) [Practice Questions](#practice-questions)

---

## 1.1 Introduction

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1vOKkkw7Ap0h26XWPu80GsJPTyYBX3NAE" alt="Illustration of static cling and spark discharge caused by electric charges" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.1:</b> Representation of static electricity causing cling and spark discharge</i></figcaption>
</figure>

Electric charge forms the foundation of electrostatics, a branch of physics concerned with stationary charges and the forces and fields they produce. This chapter begins by introducing the nature, types, and fundamental behavior of electric charges, illustrating how these concepts explain everyday phenomena such as static cling and spark discharges. Understanding the basic properties of electric charge is crucial to grasping more advanced concepts of electric fields and forces that govern electromagnetic interactions.

Charges are of two types: positive and negative, which exert forces on each other - like charges repel, unlike charges attract. This was first systematically investigated through Coulomb’s torsion balance experiment, which measured the electrostatic force quantitatively. At the atomic level, protons carry positive charge and electrons negative charge, giving substance to the macroscopic effects we observe.

The emergence of the electric field concept, describing how charges influence the space around them, marks a significant leap in understanding. Instead of action at a distance, fields describe local force interactions, enabling analysis of complex charge systems through superposition. This insight is fundamental to all of electromagnetism.

Mathematically, Coulomb’s law quantifies the force between two stationary charges as proportional to the product of the charges and inversely proportional to the square of their separation, mediated by the permittivity of space.

The principles elaborated in this introductory section form the basis for multiple practical applications, including electric circuits, capacitors, and even biomedical devices. Recognizing the role of charge and field concepts facilitates a deeper comprehension of technology and natural phenomena rooted in electrostatics.

### Conceptual Example:

Imagine rubbing a balloon on your hair. Electrons transfer to the balloon, imparting it a negative charge. When brought close to small pieces of paper, they are attracted and stick to the balloon, illustrating charge transfer and the action of forces via electric fields.

### Mathematical Example:

**Problem:** A charged balloon attracts bits of paper placed nearby. If a test charge of $q_0 = 2 \times 10^{-6} \, C$ placed near the balloon experiences a force of $F = 6 \times 10^{-3} \, N$, find the electric field at that point.

**Solution:**

By definition,

$$
E = \frac{F}{q_0} = \frac{6 \times 10^{-3}}{2 \times 10^{-6}} = 3000\, \mathrm{N/C}.
$$

Thus, the electric field due to the charged balloon at that location is \(3000 \, \mathrm{N/C}\).

---

## 1.2 Electric Charges

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1QJvgUteS-GfNoRo3ovmj4jCqjJ4107S3" alt="Diagram showing conduction and induction methods of charging" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.2:</b> Methods of charging by conduction and induction</i></figcaption>
</figure>

Electric charge is a fundamental property of matter responsible for electric forces and fields. At the microscopic scale, atoms contain protons, which bear positive charge, and electrons, which carry negative charge. An electrically neutral object has an equal number of these, but if an imbalance occurs, the object becomes charged.

Charges are discrete and quantized, existing as integer multiples of the elementary charge $ e = 1.6 \times 10^{-19} \, C $. Two types of charges are identified: positive and negative. The law of electrostatics states that like charges repel, and unlike charges attract, forming the basis of all electrostatic phenomena.

Materials are categorized based on their ability to allow charge flow: conductors permit free movement of electrons, facilitating charge redistribution; insulators inhibit free flow, causing charge to remain localized. These properties determine how objects respond to charging processes such as conduction and induction.

Charging by conduction involves direct physical contact where electrons transfer between bodies. For example, rubbing a glass rod with silk removes electrons from the rod, charging it positively. Charging by induction, on the other hand, rearranges charges without contact. When a charged body is near a neutral conductor, it induces charge separation inside it. By grounding the conductor while the charged object is nearby, electrons either enter or leave the conductor, resulting in a net charge once the ground and inducing charge are removed.

Charges add algebraically; the total charge in a system is the sum of individual charges considering their sign. The coulomb (C) is the SI unit of charge, though microcoulombs and nanocoulombs are commonly more practical for everyday magnitudes.

Understanding these charging mechanics underpins many technologies, from electrostatic precipitators to capacitors, and explains natural effects like lightning and static cling.

### Conceptual Example:

Rubbing a balloon against wool transfers electrons to the balloon, making it negatively charged by conduction. The balloon then attracts neutral paper pieces, demonstrating how charged bodies influence each other electrically even without contact.

### Mathematical Example:

**Problem:** Two spheres, initially uncharged, are touched by a charged rod losing $4 \times 10^{-7} \, C$ of electrons in the process. Calculate the charge gained by the rod.

**Solution:**

Electrons have negative charge, so losing electrons means the rod gains positive charge of magnitude:

$$
Q = 4 \times 10^{-7} \, C.
$$

Hence, the rod acquires a positive charge of $4 \times 10^{-7} \, C$.

---

## 1.3 Conservation of Charge

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1vnG7EYqeuVQCX1uEd7ogzE8dd1tvoOR2" alt="Illustration of isolated system showing charge conservation before and after interaction" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.3:</b> Conservation of charge in an isolated system during charge transfer</i></figcaption>
</figure>

The law of conservation of charge asserts that the total electric charge in an isolated system remains unchanged regardless of any internal processes. Charges cannot be created or destroyed but can only be transferred from one object to another.

This fundamental principle is validated experimentally and applies universally in electrostatics, electric circuits, and particle physics. For instance, when two conductors touch and charges redistribute, the sum of charges before and after contact remains constant.

Charges are quantized, meaning measured charges are always integer multiples of the elementary charge $e = 1.6 \times 10^{-19} \, C$. Millikan’s oil drop experiment provided definitive evidence for this quantization by observing discrete changes in charge on tiny oil droplets.

This conservation principle ensures reliable charge accounting in electrical engineering and underpins fundamental laws of physics relating to charge and matter.

Understanding and applying charge conservation is critical when analyzing charge movement in circuits, chemical reactions involving ions, and in the behavior of subatomic particles.

### Conceptual Example:

Consider two metal spheres: one positively charged and one neutral. When touched, charge redistributes between them, but the total charge combined remains equal to the initial charge on the charged sphere, illustrating conservation.

### Mathematical Example:

**Problem:** A charged sphere with $+6 \, \mu C$ charge touches an identical neutral sphere. Find the charge on each sphere after separation.

**Solution:**

Total charge conserved: $+6 \, \mu C$. Charges distribute equally due to identical spheres:

$$
Q_{each} = \frac{6 \, \mu C}{2} = +3 \, \mu C.
$$

Each sphere ends up with $+3 \, \mu C$.

---

## 1.4 Coulomb’s Law

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1cRK55U2iyBLgsP4G1ly7ve0HJ4U42BF7" alt=" demonstrating force between two point charges" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.4:</b> Coulomb’s law (force between point charges)</i></figcaption>
</figure>

Coulomb’s law provides the quantitative expression for the electrostatic force between two point charges. It states that the magnitude of the force between charges is directly proportional to the product of the absolute values of the charges and inversely proportional to the square of the distance separating them. The force acts along the straight line joining the charges.

The mathematical form is

$$
\mathbf{F} = k \frac{|q_1 q_2|}{r^2} \hat{r},
$$

where:

- $ \mathbf{F} $ = electrostatic force vector (N)  
- $ q_1, q_2 $ = magnitudes of the two charges (C)  
- $ r $ = distance between charges (m)  
- $ k = \frac{1}{4\pi \varepsilon_0} \approx 8.99 \times 10^9 \, \mathrm{N\, m^2/C^2} $  
- $ \hat{r} $ = unit vector from one charge to the other, direction depending on repulsion or attraction

Charles-Augustin de Coulomb verified this inverse square relationship using a torsion balance experiment in the late 18th century, establishing the law’s accuracy for point charges separated by a vacuum or air.

The vector nature indicates that forces have both magnitude and direction, with like charges repelling and unlike charges attracting.

Coulomb’s law not only explains forces between charged particles but also guides the design of electronic equipment, understanding molecular bonds, and studies in atomic physics.

### Conceptual Example:

Imagine two similarly charged balloons pushed close. Coulomb’s law explains the repulsive force pushing them apart, which weakens as they move farther away due to the inverse square dependence.

### Mathematical Example:

**Problem:** Calculate the force between two charges $q_1 = 5 \times 10^{-6} \, C$ and $q_2 = -3 \times 10^{-6} \, C$ separated by 0.2 m in air.

**Solution:**

$$
F = k \frac{|q_1 q_2|}{r^2} = 9 \times 10^9 \times \frac{5 \times 10^{-6} \times 3 \times 10^{-6}}{(0.2)^2} = 3.375 \, N.
$$

The force is attractive (charges opposite) with magnitude 3.375 N along the line joining them.

---

## 1.5 Force Between Multiple Charges; Superposition Principle

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1cjZvnUEwRd6OIOJfwgebf_6rSFHGnMkm" alt="Vector addition of forces from multiple charges on a charge at the origin" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.5:</b> Superposition principle showing vector sum of forces from multiple charges</i></figcaption>
</figure>

Charges in realistic situations seldom exist alone. A charge may be influenced simultaneously by several other charges located around it. The superposition principle simplifies the analysis by stating that the net force on a charge due to multiple other charges is the vector sum of the forces exerted independently by each charge.

This is critical because Coulomb’s law describes forces accurately only between two point charges at a time. By treating each pairwise interaction separately and combining the results, complex charge configurations can be analyzed efficiently.

The forces add as vectors, meaning their directions and magnitudes must be considered. Forces can partially cancel or reinforce each other depending on relative positions and signs of charges.

Applications range from understanding molecular forces in chemistry, electrostatics in materials, to engineering designs involving multiple charged bodies.

### Conceptual Example:

A test charge in a room with multiple other charged bodies experiences pushes and pulls in various directions. Its motion depends on the combined effect – a net force found by vector addition of all individual forces.

### Mathematical Example:

**Problem:** Find the net force on a charge $q = 2 \, \mu C$ located at origin, due to two charges: $q_1 = 3 \, \mu C$ at (2 m, 0) and $q_2 = -1 \, \mu C$ at (0, 3 m).

**Solution:**

Calculate forces $\mathbf{F_1}$ and $\mathbf{F_2}$ due to $q_1$ and $q_2$:

$$
F_1 = k \frac{|q q_1|}{r_1^2} = 9 \times 10^9 \times \frac{2 \times 10^{-6} \times 3 \times 10^{-6}}{2^2} = 13.5 \times 10^{-3} \, N
$$

Direction: along +x-axis (repulsive since both positive).

$$
F_2 = k \frac{|q q_2|}{r_2^2} = 9 \times 10^9 \times \frac{2 \times 10^{-6} \times 1 \times 10^{-6}}{3^2} = 2 \times 10^{-3} \, N
$$

Direction: attractive towards $q_2$ at (0,3), along -y axis.

Net force components:

$$
F_{x} = 0.0135 \, N, \quad F_{y} = -0.002\, N
$$

Magnitude:

$$
F_{net} = \sqrt{(0.0135)^2 + (-0.002)^2} \approx 0.0137\, N
$$

Direction:

$$
\theta = \tan^{-1}\left(\frac{|F_y|}{F_x}\right) = \tan^{-1}\left(\frac{0.002}{0.0135}\right) \approx 8.5^\circ \text{ below } +x.
$$

---

### 1.5.1 Superposition Principle

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1ZnxmgjoO3FQ5qIlKZO8M-rbJOsCziXpG" alt="Two forces acting at angles and their vector sum visualization" style="max-width: 90%; height: auto;">
<figcaption><i><b>Figure 1.5.1:</b> Vector addition of forces illustrating superposition</i></figcaption>
</figure>

The superposition principle rigorously states that the electric force experienced by any charge in a system is the vector sum of the forces due to each other charge considered separately. This allows breaking complex interactions down into simple two-charge calculations, which are then combined.

Mathematically, the net force on a charge $q$ is

$$
\mathbf{F}_{net} = \sum_i \mathbf{F}_i = \sum_i k \frac{q q_i}{r_i^2} \hat{r}_i
$$

Variables:

- $ q_i $ = $i^{th}$ source charge  
- $ r_i $ = distance from source charge to $ q $  
- $ \hat{r}_i $ = unit vector directed from $ q_i $ to $ q $  

This vector addition respects both magnitude and direction, meaning forces can reinforce, oppose, or partially cancel.

---

**Conceptual Example:**

Imagine two kids pushing a sled from different sides, with different strength and directions. The sled’s acceleration depends on the combined vector sum of these pushes, not just their numbers.

---

**Mathematical Example:**

**Problem:** Three charges $q_1=2 \, \mu C$ at origin, $q_2=-3 \, \mu C$ at 2 m right, and $q_3=1 \, \mu C$ at 3 m left. Find net force on $q_1$.

**Solution:**

Force by $q_2$:

$$
F_{12} = 9 \times 10^9 \times \frac{2 \times 10^{-6} \times 3 \times 10^{-6}}{(2)^2} = 13.5 \times 10^{-3} \, N
$$

Direction: attractive, so to right.

Force by $q_3$:

$$
F_{13} = 9 \times 10^9 \times \frac{2 \times 10^{-6} \times 1 \times 10^{-6}}{(3)^2} = 2 \times 10^{-3} \, N
$$

Direction: repulsive, also to right.

Net force:

$$
F_{net} = 15.5 \times 10^{-3} \, N = 0.0155 \, N
$$

Direction: toward right along line.

---

## 1.6 Electric Field, Definition

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1xj7bBB-YObow-wK6TApgfw0xH7GThNsz" alt="Vector field representation around a positive charge" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.6:</b> Electric field vectors radiating from a point charge</i></figcaption>
</figure>

Electric field is a vector quantity that describes the influence a charge exerts on the space around it. Formally, at a point in space, the electric field is defined as the force experienced per unit positive test charge placed at that point, independent of the test charge's magnitude.

This concept moves beyond the notion of "action at a distance," instead describing local interactions mediated through the field. A positive source charge produces field lines radiating outward, whereas a negative charge produces inward-directed field lines.

Mathematically,

$$
\mathbf{E} = \frac{\mathbf{F}}{q_0}
$$

where:

- $ \mathbf{E} $ = electric field vector (N/C)  
- $ \mathbf{F} $ = force on the test charge (N)  
- $ q_0 $ = positive test charge magnitude (C)  

The field is independent of $ q_0 $, making it an intrinsic property of the charge distribution. The direction of $ \mathbf{E} $ is the direction of the force on a positive charge.

Electric fields explain forces experienced by charges in a region and extend to describe energy, potential, and dynamics of charges.

### Conceptual Example:

Consider electric field as invisible "force lines" that push or pull a small test charge placed anywhere around a source charge. This "wind" shows how the charge affects the surroundings, similar to how a fan creates airflow.

### Mathematical Example:

**Problem:** A test charge $5 \times 10^{-6} \, C$ experiences a force $1 \times 10^{-3}\, N$. Find the electric field at that point.

**Solution:**

$$
E = \frac{F}{q_0} = \frac{1 \times 10^{-3}}{5 \times 10^{-6}} = 200 \, \mathrm{N/C}.
$$

Therefore, the electric field at the point is $200 \, \mathrm{N/C}$.

---

## 1.7 Electric Field Due to a Point Charge

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1GVAC8JnjDTgVlO2srh8AhRvNQbER8iRT" alt="Radial electric field vectors from a point charge" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.7:</b> Radial electric field lines emanating from a positive point charge</i></figcaption>
</figure>

For a point charge $ Q $, the electric field at any point located at a distance $ r $ from it is radially directed and has magnitude given by

$$
\mathbf{E} = k \frac{Q}{r^2} \hat{r},
$$

where:

- $ k = \frac{1}{4 \pi \varepsilon_0} $  
- $ r $ = distance from charge (m)  
- $ \hat{r} $ = unit vector from charge to point of interest

The field points radially outward if $ Q $ is positive and inward if $ Q $ is negative. This dependence implies the field strength decreases as the inverse square of distance, analogous to gravitational fields.

This precise formula is derived from Coulomb’s law, dividing force by test charge to get field.

Electric fields due to point charges form the basis for understanding more complex charge distributions, as more complex fields can be thought of as sums of point charge fields.

### Conceptual Example:

Visualize the space around a positively charged point as filled with radially outward "lines of force," which become sparser as you move farther, illustrating decreasing field strength.

### Mathematical Example:

**Problem:** Calculate electric field 5 cm from a point charge of $2 \, \mu C$.

**Solution:**

Convert distance:

$$
r = 5 \, \text{cm} = 0.05 \, m.
$$

Calculate field:

$$
E = 9 \times 10^9 \times \frac{2 \times 10^{-6}}{(0.05)^2} = 7.2 \times 10^6 \, N/C.
$$

The electric field is $7.2 \times 10^6 \, N/C$ directed radially outward.

---

## 1.8 Electric Field Lines

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/16Gbp3YOUuRLjK7JxmL6RJdHQC8kFM2Hw" alt="Electric field lines of point charges and dipole" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.8:</b> Electric field lines of single charges and a dipole, showing direction and density</i></figcaption>
</figure>

Electric field lines provide a visual representation of electric fields allowing qualitative understanding of their direction and strength. Lines originate from positive charges and terminate on negative charges. The number of lines per unit area perpendicular to the direction of the field corresponds to the field's magnitude.

Key properties include:

- Lines never cross.  
- Line density correlates with field strength — denser lines imply stronger fields.  
- At infinity, field lines may extend without termination if charges are isolated.  

Field lines around single positive and negative charges radiate outward and inward, respectively. A dipole shows lines originating on the positive charge and terminating on the negative with characteristic curved paths.

This visual method aids in understanding interactions and designing electronic equipment.

### Conceptual Example:

Sketching field lines around charges, we observe that lines cluster near the charges where the field is strongest, spreading out as we move away, illustrating the inverse square nature of the field.

---

## 1.9 Electric Dipole

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1ZaX2CWif6tyVbOMUNN06yajh8tPccGne" alt="Electric dipole showing charges and dipole moment vector" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.9:</b> Schematic of an electric dipole with charges and dipole moment vector</i></figcaption>
</figure>

An electric dipole consists of two equal and opposite charges separated by a distance \( 2a \). It represents a system with an overall neutral charge but with distinct positive and negative poles.

Dipoles are fundamental in molecular physics and electrostatics because of their unique interaction behavior with external fields.

---

### 1.9.1 Electric Dipole Moment

The electric dipole moment \( \mathbf{p} \) is a vector quantity defined as

$$
\mathbf{p} = q \times 2a,
$$

where $ q $ is the charge magnitude and $ 2a $ the separation between charges. Its direction is from the negative charge to the positive charge.

The dipole moment measures the strength and orientation of the dipole and determines its interaction with external fields.

### Conceptual Example:

A water molecule, with uneven charge distribution, behaves like a dipole with a defined dipole moment, explaining many of water’s physical properties.

### Mathematical Example:

**Problem:** Calculate dipole moment for charges $\pm 1 \times 10^{-6} \, C$ separated by 4 cm.

**Solution:**

$$
p = q \times 2a = 1 \times 10^{-6} \times 0.04 = 4 \times 10^{-8} \, C \cdot m.
$$

---

### 1.9.2 Electric Field Due to an Electric Dipole

The electric field of a dipole depends on the position relative to the dipole axis.

- **On the axial line** (along dipole axis):

$$
E_{axial} = \frac{1}{4 \pi \varepsilon_0}\frac{2p}{r^3}
$$

- **On the equatorial line** (perpendicular bisector):

$$
E_{equatorial} = \frac{1}{4 \pi \varepsilon_0}\frac{p}{r^3}
$$

The equatorial field points opposite to the axial line direction, decreasing faster with distance than single charges.

This dependence shows the distinct spatial characteristics of dipole fields.

### Conceptual Example:

A dipole placed near another charge exerts forces different in magnitude and direction depending whether the charge lies along axial or equatorial lines.

### Mathematical Example:

**Problem:** Calculate the field at 0.1 m on the axial line of a dipole with $ p = 4 \times 10^{-8} \, C.m $.

**Solution:**

$$
E = 9 \times 10^9 \times \frac{2 \times 4 \times 10^{-8}}{(0.1)^3} = 7.2 \times 10^{5} \, N/C.
$$

---

## 1.10 Torque on an Electric Dipole in a Uniform Electric Field

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1utkJfRt2j-1cCUedW9OKYxFVs5vkdoqI" alt="Dipole in uniform electric field with forces and torque directions indicated" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.10:</b> Torque on dipole due to uniform electric field</i></figcaption>
</figure>

A dipole placed in an external uniform electric field experiences forces on its charges resulting in a torque tending to align the dipole with the field.

The magnitude of torque $ \tau $ is

$$
\tau = p E \sin \theta,
$$

where:

- $ p $ = dipole moment (C.m)  
- $ E $ = magnitude of uniform field (N/C)  
- $ \theta $ = angle between dipole moment and electric field vectors

The torque direction tends to rotate the dipole to align along the field, minimizing potential energy.

Potential energy of the dipole in the field is

$$
U = -p E \cos \theta,
$$

lowest when dipole aligns with the field.

This behavior is fundamental in molecular physics and electric devices sensing dipole orientations.

### Conceptual Example:

A water molecule in an electric field experiences torque aligning its dipole moment with the field, influencing physical behavior such as dielectric polarization.

### Mathematical Example:

**Problem:** Calculate torque on a dipole of $p = 3 \times 10^{-8}\, C.m$ in $E = 5 \times 10^4\, N/C$ when $ \theta = 60^\circ $.

**Solution:**

$$
\tau = 3 \times 10^{-8} \times 5 \times 10^4 \times \sin 60^\circ = 1.3 \times 10^{-3} \, Nm.
$$

---

## 1.11 Electric Flux

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1gfrBl8lMb-YRpNzG1T7aQjVcMDsEpB4k" alt="Surface with electric field lines illustrating flux calculation" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.11:</b> Electric flux concept with field lines passing through a surface</i></figcaption>
</figure>

Electric flux $ \Phi_E $ measures the quantity of electric field lines passing through a given surface. It quantifies how the field permeates the surface and is defined by the surface integral

$$
\Phi_E = \int \mathbf{E} \cdot d \mathbf{A},
$$

where $ d\mathbf{A} $ is an infinitesimal area element vector normal to the surface.

For uniform fields and flat surfaces at angle $ \theta $ to the field,

$$
\Phi_E = E A \cos \theta.
$$

Electric flux is a scalar quantity, yet directionality is embedded in the dot product, associating positive or negative values based on field orientation.

This concept is pivotal for Gauss’s law and aids in visualizing and calculating field behavior through surfaces.

### Conceptual Example:

Imagine wind blowing through a screen at an angle; the “amount” of wind passing through is akin to electric flux, depending on wind strength, screen area, and angle relative to wind.

### Mathematical Example:

**Problem:** Find electric flux through 0.2 m² surface inclined at $60^\circ$ to a uniform field $E = 500 \, N/C$.

**Solution:**

$$
\Phi_E = E A \cos \theta = 500 \times 0.2 \times \cos 60^\circ = 500 \times 0.2 \times 0.5 = 50 \, \mathrm{N\, m^2/C}.
$$

---

## 1.12 Gauss’s Law and Its Applications

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://lh3.googleusercontent.com/d/1NHE0OHVAxK4wfzHMnek392q9TLyrjUc3" alt="Gaussian surfaces used in applications of Gauss's law" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 1.12:</b> Gauss's law</i></figcaption>
</figure>

Gauss's law is a fundamental theorem connecting electric flux through a closed surface to the charge enclosed within that surface. This relationship simplifies field calculations for systems with high symmetry.

---

### 1.12.1 Gauss’s Law Statement and Mathematical Form

The law states:

$$
\Phi_E = \oint \mathbf{E} \cdot d\mathbf{A} = \frac{Q_{enc}}{\varepsilon_0},
$$

where:

- $ \Phi_E $ = total electric flux through closed surface  
- $ Q_{enc} $ = net charge enclosed  
- $ \varepsilon_0 = 8.854 \times 10^{-12} \, C^2/(N\,m^2) $ permittivity of free space

The surface integral accounts for field contribution over the entire closed surface.

---

**Conceptual Example:**

Imagine field lines flowing through a spherical surface enclosing a charge; the total number of lines (flux) is proportional to the enclosed charge and independent of surface shape.

---

### 1.12.2 Applications

Gauss’s law lends to calculating fields of symmetric charge distributions where direct Coulombian summation is complicated.

Examples:

- **Charged sphere:**  
  Outside:

  $$
  E = \frac{1}{4 \pi \varepsilon_0} \frac{Q}{r^2}
  $$

  Inside (for uniformly charged sphere radius \(R\)):

  $$
  E = \frac{1}{4 \pi \varepsilon_0} \frac{Q r}{R^3}
  $$

- **Infinite line charge (linear density $\lambda$)**

$$
E = \frac{\lambda}{2 \pi \varepsilon_0 r}
$$

- **Infinite charged plane (surface charge density $\sigma$)**

$$
E = \frac{\sigma}{2 \varepsilon_0}
$$

These simplified formulas arise via appropriate Gaussian surfaces exploiting symmetry.

### Conceptual Example:

To find the field around a charged sphere, choose a concentric spherical Gaussian surface and apply Gauss’s law to relate enclosed charge and flux, leading to elegant expressions.

### Mathematical Examples:

1. **Find $E$ inside a uniformly charged sphere at $r=0.05 \, m$, $R=0.1 \, m$, total charge $Q=4 \, \mu C$.**

$$
E = \frac{1}{4 \pi \varepsilon_0} \frac{Q r}{R^3} = 9 \times 10^9 \times \frac{4 \times 10^{-6} \times 0.05}{(0.1)^3} = 1.8 \times 10^{6} \, N/C.
$$

2. **Field near infinite charged plane with \(\sigma = 5 \times 10^{-6} \, C/m^2\).**

$$
E = \frac{\sigma}{2\varepsilon_0} = \frac{5 \times 10^{-6}}{2 \times 8.854 \times 10^{-12}} = 2.82 \times 10^{5} \, N/C.
$$

---

## Summary

Chapter 1 explores electric charges and fields, starting from fundamental properties and proceeding to advanced concepts with applications. Electric charge, a discrete and conserved property of matter, forms the basis of electrostatics. Charges exist as positive or negative, with forces between them governed quantitatively by Coulomb’s law, which states that the electrostatic force magnitude is proportional to the product of charges and inversely proportional to the distance squared.

The superposition principle extends this understanding to multiple charge configurations, allowing forces and fields to be summed vectorially. Transitioning from forces to fields introduces the concept of the electric field as a vector field describing force per unit charge at every point in space, independent of test charge magnitude. Field lines provide intuitive visualization, showing direction and relative strength.

An electric dipole, composed of equal and opposite charges separated by a fixed distance, features prominently due to its torque interaction with external uniform fields. This leads to orientation phenomena central to molecular behavior and device physics. Torque and potential energy expressions quantify this behavior precisely.

Electric flux measures the quantity of field passing through a surface and serves as a gateway to Gauss’s law, a powerful theorem connecting net electric flux to enclosed electric charge. Gauss's law allows efficient calculation of fields for charge distributions with high symmetry, including spheres, lines, and planes, providing elegant field expressions consistent with Coulomb’s law.

Throughout the chapter, core formulas like Coulomb’s law, electric field definitions, dipole moment, torque equation, electric flux, and Gauss’s law unify the conceptual framework. Examples contextualize these theories numerically and conceptually, reinforcing understanding.

Practically, these concepts underpin technologies such as capacitors, electrostatics-based pollution control, particle accelerators, and biological sensors. Experimental verifications such as Coulomb’s torsion balance and Millikan’s oil drop reinforce the reliability of these laws.

The chapter also connects to later topics on electric potential, capacitance, and electromagnetic induction, providing a foundational base for advanced physics and engineering studies.

---

## Practice Questions

1. Define electric charge and state its units.  
2. Distinguish between conductors and insulators in terms of charge mobility.  
3. Explain why charges are quantized and what is meant by the elementary charge.  
4. State the law of conservation of charge and describe an experiment that verifies it.  
5. Write the mathematical statement of Coulomb’s law and explain the significance of each symbol.  
6. Calculate the force between two charges of $3 \times 10^{-6} \, C$ and $-4 \times 10^{-6} \, C$ placed 0.5 m apart in vacuum.  
7. What is the superposition principle in electrostatics? Give an example.  
8. A charge $q$ experiences two forces $ \mathbf{F}_1 = 5 \hat{i} \, N$ and $ \mathbf{F}_2 = 3 \hat{j} \, N$. Find the magnitude and direction of the net force.  
9. Define electric field and write its relation to force and test charge.  
10. Calculate electric field at 10 cm from a charge of $1 \, \mu C$.  
11. Sketch electric field lines for (a) single positive charge, (b) dipole.  
12. Define electric dipole moment and state its direction.  
13. Calculate the dipole moment for a dipole consisting of charges $\pm 2 \times 10^{-6} \, C$ separated by 6 cm.  
14. Derive expression for electric field at a point on the axial line of a dipole.  
15. Calculate the torque on a dipole of moment $3 \times 10^{-8} \, C.m$ in a field $10^{5} \, N/C$ making angle $30^\circ$ with the field.  
16. What is electric flux? Write expression for flux through a surface area placed in uniform electric field.  
17. Using Gauss’s law, derive the expression for electric field outside a charged conducting sphere.  
18. Find electric field inside a uniformly charged sphere of radius 10 cm with total charge $5 \times 10^{-6} \, C$ at radius 5 cm.  
19. Calculate the electric field due to an infinite line charge with linear charge density $2 \times 10^{-6} \, C/m$ at 0.1 m distance.  
20. An infinite charged plane has surface charge density $4 \times 10^{-6} \, C/m^2$. Find field near its surface.  
21. Show that electric field lines never cross.  
22. If two charges of equal magnitude and opposite signs are separated by 5 cm, calculate the magnitude of the dipole moment.  
23. A test charge experiences two forces: one 4 N east and another 3 N south. Find the net force magnitude and direction.  
24. Derive expression for potential energy of an electric dipole in uniform electric field.  
25. Explain the difference between electric field and electric potential.

---

# End of Chapter 1: Electric_Charges_and_Fields