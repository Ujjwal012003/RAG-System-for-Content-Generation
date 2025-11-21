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

<img src="https://i.imgur.com/magnetic-force-overview.png" alt="Overview of Magnetic Force on Moving Charges" style="width:450px; display:block; margin:auto" />

The fascinating connection between electricity and magnetism extends beyond stationary charges to moving charges. When a charged particle moves through a magnetic field, it experiences a force that was first comprehensively described by Dutch physicist **Hendrik Lorentz** in the late 19th century, building upon the experimental work of André-Marie Ampère and Michael Faraday. This force, now known as the **Lorentz force**, is fundamental to understanding the behavior of charged particles in electromagnetic fields and forms the basis for numerous technologies from particle accelerators to cathode ray tubes.

The magnetic force on a moving charge exhibits unique properties that distinguish it from electric forces. Unlike electric forces that act along the direction of the field, magnetic forces act perpendicular to both the velocity of the charge and the magnetic field direction. This perpendicular nature leads to circular or helical motion rather than linear acceleration, making magnetic fields ideal for steering and confining charged particle beams without changing their kinetic energy.

Understanding the Lorentz force is essential for explaining phenomena ranging from cosmic ray deflection by Earth's magnetic field to the operation of mass spectrometers in analytical chemistry. The mathematical formulation combines both electric and magnetic field effects, providing a unified description of electromagnetic forces on charges. This principle underpins technologies like magnetic resonance imaging (MRI), particle accelerators used in cancer treatment, and even the auroras that light up polar skies.

In this section, we will explore the Lorentz force law and its mathematical expression, examine the unique properties of magnetic forces including why they do no work on moving charges, and investigate the wide-ranging applications of this fundamental principle in modern science and technology. We'll analyze how the direction of the force is determined using the right-hand rule and understand how these forces affect particle trajectories in uniform and non-uniform magnetic fields.

### 4.2.1 Lorentz Force on Moving Charges

<img src="https://i.imgur.com/sTMzZ1R.png" alt="Lorentz Force Vector Diagram" style="width:450px; display:block; margin:auto" />

A fundamental force experienced by a charged particle moving in combined electric and magnetic fields is known as the **Lorentz force**. This force was mathematically formulated by Hendrik Lorentz in 1895 as part of his electron theory, which explained how electromagnetic fields interact with matter at the microscopic level. The Lorentz force equation represents one of the most important relationships in electromagnetism, bridging classical mechanics with electromagnetic field theory.

When a charged particle with charge $q$ moves with velocity $\mathbf{v}$ through a region containing both an electric field $\mathbf{E}$ and a magnetic field $\mathbf{B}$, it experiences a combined force given by the complete Lorentz force equation:

$$
\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B})
$$

where:
- $\mathbf{F}$ = total Lorentz force vector acting on the charged particle (Newtons, N)
- $q$ = electric charge of the particle (Coulombs, C); positive for protons, negative for electrons
- $\mathbf{E}$ = electric field vector (Newtons per Coulomb, N/C or Volts per meter, V/m)
- $\mathbf{v}$ = velocity vector of the charged particle (meters per second, m/s)
- $\mathbf{B}$ = magnetic field vector (Tesla, T or Weber per square meter, Wb/m²)
- $\times$ = cross product operator (produces a vector perpendicular to both operands)

When only magnetic fields are present (which is often the case in particle deflection experiments), the electric field term vanishes and the force simplifies to:

$$
\mathbf{F} = q(\mathbf{v} \times \mathbf{B})
$$

This magnetic component of the Lorentz force is perpendicular to both the velocity $\mathbf{v}$ of the charge and the magnetic field $\mathbf{B}$. The magnitude of this force depends on the angle between the velocity and field vectors:

$$
F = q v B \sin \theta
$$

where:
- $F$ = magnitude of the magnetic force (Newtons, N)
- $v$ = speed of the charged particle (meters per second, m/s)
- $B$ = magnitude of the magnetic field (Tesla, T)
- $\theta$ = angle between the velocity vector and magnetic field vector (degrees or radians)

**Conceptual Understanding: The Perpendicular Push**

Imagine pushing a merry-go-round at a playground. If you push directly toward the center (radially inward), the merry-go-round doesn't spin—your force is ineffective. But if you push perpendicular to the radius (tangentially), it rotates smoothly. Magnetic force works on a similar principle—it only acts when a charge moves with a velocity component perpendicular to the magnetic field lines.

Think of electrons in an old cathode ray tube television. They shoot straight from the electron gun at the back of the tube, but strategically placed magnets around the tube deflect them left-right and up-down to "paint" the image on the screen. The faster the electrons move, the stronger the deflection force—that's why $F$ is directly proportional to velocity $v$. 

This perpendicular nature is why magnetic fields can steer particles in circular paths without changing their speed—they only change direction of motion, not the magnitude of velocity. This principle is exploited in particle accelerators like cyclotrons and in Earth's magnetosphere, where charged particles from the solar wind are trapped in Van Allen radiation belts, spiraling along magnetic field lines.

**Direction of Magnetic Force: The Right-Hand Rule**

The direction of the magnetic force $\mathbf{F}$ is determined by the **right-hand rule** (also called Fleming's left-hand rule for motors):

1. Point your **fingers** in the direction of the velocity vector $\mathbf{v}$
2. **Curl** your fingers toward the direction of the magnetic field $\mathbf{B}$
3. Your extended **thumb** points in the direction of the force $\mathbf{F}$ for a **positive** charge

For a **negative** charge (like an electron), the force direction is **opposite** to what the right-hand rule indicates for the same velocity and field directions. This is because the charge $q$ in the equation $\mathbf{F} = q(\mathbf{v} \times \mathbf{B})$ is negative, reversing the force direction.

**Mathematical Example:**

**Problem:** An electron is moving at a velocity of $2 \times 10^6 \, \text{m/s}$ perpendicular to a uniform magnetic field of magnitude $0.01 \, \text{T}$. Calculate the magnitude of the magnetic force acting on the electron.

**Given:**
- Charge of electron: $q = -1.6 \times 10^{-19} \, \text{C}$ (we use magnitude for force calculation)
- Velocity: $v = 2 \times 10^6 \, \text{m/s}$
- Magnetic field: $B = 0.01 \, \text{T}$
- Angle: $\theta = 90°$ (perpendicular motion, so $\sin 90° = 1$)

**To Find:** Magnitude of magnetic force $F$

**Solution:**

Step 1: Apply the magnetic force formula for perpendicular motion:

$$
F = |q| v B \sin \theta
$$

Step 2: Substitute the given values (using magnitude of charge):

$$
F = (1.6 \times 10^{-19}) \times (2 \times 10^{6}) \times (0.01) \times \sin 90°
$$

Step 3: Simplify (since $\sin 90° = 1$):

$$
F = 1.6 \times 10^{-19} \times 2 \times 10^{6} \times 0.01
$$

$$
F = 3.2 \times 10^{-15} \, \text{N}
$$

**Answer:** The magnitude of the magnetic force acting on the electron is $3.2 \times 10^{-15} \, \text{N}$.

**Physical Interpretation:** Although this force appears extremely small, it is significant for subatomic particles like electrons due to their tiny mass ($9.1 \times 10^{-31} \, \text{kg}$). This force produces an acceleration of approximately $3.5 \times 10^{15} \, \text{m/s}^2$—sufficient to dramatically alter the electron's trajectory in devices like cathode ray tubes, electron microscopes, and particle accelerators.

### 4.2.2 Properties of Magnetic Force on Moving Charges

<img src="https://i.imgur.com/ULRz2GT.png" alt="Trajectory of Charged Particle in Magnetic Field" style="width:450px; display:block; margin:auto" />

The magnetic force on moving charges exhibits several unique and remarkable properties that distinguish it from other fundamental forces in nature. Understanding these properties is crucial for explaining particle behavior in electromagnetic fields and designing devices that manipulate charged particle beams.

**1. Perpendicularity of Force**

The magnetic force is **always perpendicular** to both the instantaneous velocity of the charge and the magnetic field direction. Mathematically, this arises from the cross product $\mathbf{v} \times \mathbf{B}$ in the Lorentz force equation. The cross product of two vectors produces a third vector perpendicular to the plane containing the original two vectors.

This perpendicularity has profound consequences: since the force acts perpendicular to velocity, it cannot change the **speed** of the particle—only its **direction** of motion. The particle's kinetic energy $KE = \frac{1}{2}mv^2$ remains constant because speed $v$ is unchanged. The magnetic force continuously redirects the particle's velocity vector, causing it to follow a curved path.

**2. Magnetic Force Does No Work**

Work done by a force is defined as $W = \mathbf{F} \cdot \mathbf{d}$, where $\mathbf{d}$ is the displacement. Since the magnetic force is perpendicular to the velocity (and hence perpendicular to the displacement $\mathbf{d} = \mathbf{v} \Delta t$), the dot product $\mathbf{F} \cdot \mathbf{d} = 0$. Therefore:

$$
W_{\text{magnetic}} = 0
$$

This means magnetic fields cannot increase or decrease the kinetic energy of charged particles—they can only redirect them. This property is exploited in particle accelerators where magnetic fields steer particles while electric fields accelerate them.

**3. Dependence on Velocity**

Unlike gravitational or electrostatic forces (which act on charges or masses regardless of motion), the magnetic force exists **only when the charge is moving** relative to the magnetic field. A stationary charge in a magnetic field experiences zero magnetic force:

$$
\text{If } \mathbf{v} = 0, \text{ then } \mathbf{F} = q(\mathbf{v} \times \mathbf{B}) = 0
$$

Additionally, the force is **maximum** when the velocity is perpendicular to the field ($\theta = 90°$, $\sin \theta = 1$) and **zero** when velocity is parallel or antiparallel to the field ($\theta = 0°$ or $180°$, $\sin \theta = 0$).

**4. Effect on Particle Trajectory**

The perpendicular force produces different types of motion depending on the initial velocity direction relative to the magnetic field:

- **Circular Motion:** When $\mathbf{v} \perp \mathbf{B}$ (velocity completely perpendicular to field), the particle moves in a circular path in the plane perpendicular to $\mathbf{B}$

- **Helical Motion:** When velocity has both perpendicular ($v_\perp$) and parallel ($v_\parallel$) components relative to $\mathbf{B}$, the particle follows a helical (spiral) trajectory—circular motion in the plane perpendicular to $\mathbf{B}$ combined with uniform motion along $\mathbf{B}$

- **Straight-Line Motion:** When $\mathbf{v} \parallel \mathbf{B}$ (velocity parallel to field), no magnetic force acts, and the particle continues in a straight line with constant velocity

**Conceptual Understanding: The Helical Path**

Imagine a quarterback throwing a spiral football. The ball has two types of motion: it spins around its axis (circular motion) while simultaneously moving forward through the air (linear motion). Similarly, when a charged particle enters a magnetic field at an angle, it exhibits helical motion—it circles around the magnetic field lines while drifting along them.

This helical motion is beautifully demonstrated in nature by auroras (Northern and Southern Lights). Charged particles from the solar wind spiral along Earth's magnetic field lines, eventually funneling toward the magnetic poles. As they collide with atmospheric molecules, they create the spectacular light displays we observe near the Arctic and Antarctic regions.

**Mathematical Example:**

**Problem:** An electron is moving with velocity components $v_\perp = 3 \times 10^6 \, \text{m/s}$ perpendicular to a magnetic field and $v_\parallel = 4 \times 10^6 \, \text{m/s}$ parallel to the field. The magnetic field strength is $B = 0.02 \, \text{T}$. Describe the motion and calculate the magnetic force.

**Given:**
- Perpendicular velocity component: $v_\perp = 3 \times 10^6 \, \text{m/s}$
- Parallel velocity component: $v_\parallel = 4 \times 10^6 \, \text{m/s}$
- Electron charge magnitude: $|q| = 1.6 \times 10^{-19} \, \text{C}$
- Magnetic field: $B = 0.02 \, \text{T}$

**To Find:** Type of motion and magnitude of magnetic force

**Solution:**

Step 1: Identify the type of motion. Since the electron has both perpendicular and parallel velocity components, it will undergo **helical motion**—circular motion in the plane perpendicular to $\mathbf{B}$ combined with constant velocity along $\mathbf{B}$.

Step 2: Calculate the magnetic force. The magnetic force acts only on the perpendicular velocity component:

$$
F = |q| v_\perp B
$$

Step 3: Substitute values:

$$
F = (1.6 \times 10^{-19}) \times (3 \times 10^{6}) \times (0.02)
$$

$$
F = 9.6 \times 10^{-15} \, \text{N}
$$

Step 4: Note that the parallel velocity component $v_\parallel$ experiences **no magnetic force** and remains constant throughout the motion.

**Answer:** The electron undergoes helical motion with a magnetic force magnitude of $9.6 \times 10^{-15} \, \text{N}$ acting on the perpendicular velocity component. The parallel velocity component remains unaffected at $4 \times 10^6 \, \text{m/s}$, causing the electron to drift along the field lines while circling around them.

**Physical Significance:** This property is fundamental to understanding charged particle behavior in astrophysical environments (cosmic ray propagation), laboratory plasma confinement (fusion reactors), and particle beam transport in accelerators.

### 4.2.3 Applications of Magnetic Force on Moving Charges

<img src="https://i.imgur.com/applications-lorentz.png" alt="Applications of Magnetic Force" style="width:450px; display:block; margin:auto" />

The Lorentz force principle finds extensive applications across multiple fields of science, technology, and medicine, revolutionizing our capabilities in particle manipulation, medical imaging, materials analysis, and fundamental research.

**Laboratory and Research Applications:**

**Mass Spectrometry:** One of the most powerful analytical techniques in chemistry and biology, mass spectrometers use magnetic fields to separate ions based on their mass-to-charge ratio ($m/q$). Charged particles are deflected into circular paths with radius $r = \frac{mv}{qB}$, allowing identification of different isotopes and molecular fragments. Modern mass spectrometers achieve parts-per-trillion sensitivity, enabling detection of trace substances in environmental samples, drug testing, and proteomics research.

**Particle Accelerators:** Facilities like cyclotrons, synchrotrons, and the Large Hadron Collider (LHC) use powerful magnetic fields to guide and focus particle beams. The LHC employs superconducting magnets producing fields of 8.3 Tesla to bend 7 TeV proton beams around its 27-kilometer circumference. These accelerators have led to groundbreaking discoveries including the Higgs boson and are used for fundamental physics research, materials science, and medical isotope production.

**Velocity Selectors:** In experimental physics, crossed electric and magnetic fields create regions where only particles with specific velocities can pass undeflected. When $qE = qvB$, the electric and magnetic forces balance, allowing selection of particles with $v = E/B$. This technique is crucial for creating monoenergetic particle beams in electron microscopy and ion implantation.

**Medical Technology Applications:**

**Magnetic Resonance Imaging (MRI):** Modern MRI scanners use strong static magnetic fields (1.5 to 3 Tesla for clinical machines, up to 10.5 Tesla for research) to align hydrogen nuclei in body tissues. Radio frequency pulses perturb this alignment, and the resulting signals create detailed three-dimensional images of internal anatomy. MRI provides superior soft-tissue contrast compared to X-rays or CT scans without using ionizing radiation, making it invaluable for diagnosing neurological disorders, joint injuries, and soft-tissue tumors.

**Radiation Therapy:** Proton beam therapy uses magnetic fields to precisely steer high-energy proton beams to target cancerous tumors while minimizing damage to surrounding healthy tissue. The magnetic force allows fine control over beam position and shape, enabling treatment of tumors near critical structures like the brain stem or optic nerves.

**Consumer Electronics Applications:**

**Cathode Ray Tubes (CRTs):** Though largely replaced by LCD and LED displays, CRT technology dominated television and computer monitors for decades. Electron beams generated by thermionic emission were magnetically deflected to scan across a phosphorescent screen at rates up to 85 Hz, creating images through persistence of vision. The precise magnetic deflection system allowed high-resolution displays and vector graphics.

**Magnetic Data Storage:** Hard disk drives (HDDs) use magnetic read/write heads to store digital information on rapidly spinning platters. Modern HDDs achieve areal densities exceeding 1 terabit per square inch using perpendicular magnetic recording and sophisticated magnetic field manipulation at the nanoscale.

**Astrophysical and Space Physics Applications:**

**Earth's Magnetosphere:** The planet's magnetic field (approximately 0.00005 Tesla at the surface) deflects charged particles from the solar wind, protecting life from harmful radiation. Particles spiral along magnetic field lines toward the poles, where collisions with atmospheric molecules (oxygen and nitrogen) produce auroras—the Northern Lights (Aurora Borealis) and Southern Lights (Aurora Australis)—at altitudes of 100-400 kilometers.

**Cosmic Ray Deflection:** High-energy charged particles from supernovae and other cosmic sources are bent by interstellar and galactic magnetic fields. The magnetic force constrains their propagation, affecting the cosmic ray flux observed at Earth and influencing star formation rates in galaxies through pressure on interstellar gas.

**Plasma Confinement:** Experimental fusion reactors like tokamaks use toroidal magnetic fields to confine hot plasma (temperatures exceeding 100 million Kelvin) away from material walls. The Lorentz force keeps charged particles spiraling along magnetic field lines, enabling sustained fusion reactions that may provide clean, abundant energy in the future.

**Industrial Applications:**

**Electromagnetic Flow Meters:** Used in chemical processing and water treatment, these devices measure the flow rate of conductive fluids by detecting the voltage induced when the fluid moves through a magnetic field. The Lorentz force on charge carriers in the moving fluid creates a measurable potential difference proportional to flow velocity.

**Isotope Separation:** Magnetic separation of uranium isotopes (U-235 and U-238) was historically used in nuclear fuel enrichment. Ionized uranium atoms with different masses are deflected by different amounts in a magnetic field, enabling collection of the lighter, fissile U-235 isotope.

Understanding the Lorentz force and its applications demonstrates the profound connection between fundamental physics and practical technology, illustrating how a mathematical relationship discovered in the 19th century continues to enable 21st-century innovations in medicine, communications, energy, and scientific research.

---

## 4.3 Motion of Charged Particles in a Magnetic Field

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/motion-overview-magnetic.png" alt="Overview of Charged Particle Motion in Magnetic Fields" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.3:</b> Types of motion experienced by charged particles in uniform magnetic fields depending on velocity direction relative to field.</i></figcaption>
</figure>

The motion of charged particles in magnetic fields is determined by the relationship between the particle's velocity and the magnetic field direction. When physicist Hendrik Lorentz first analyzed this problem, he discovered that particles follow distinct trajectories—circular paths when moving perpendicular to the field, and helical (spiral) paths when moving at an angle. This principle became the foundation for designing particle accelerators, from Rutherford's early experiments to modern cyclotrons and synchrotrons that explore the fundamental structure of matter.

The fascinating aspect of magnetic deflection is that the particle's speed remains constant (magnetic force does no work), yet the trajectory becomes curved. This property makes magnetic fields uniquely suited for manipulating charged particles without changing their kinetic energy, a principle exploited in devices ranging from electron microscopes to plasma confinement reactors. Understanding these motion patterns requires analyzing how the magnetic force balances with the requirements of circular motion, leading to remarkable results where the period of revolution becomes independent of particle speed.

In this section, we examine two primary types of motion: circular motion when velocity is perpendicular to the magnetic field, and helical motion when velocity has components both parallel and perpendicular to the field. We'll derive the key relationships governing radius, period, and frequency of revolution, and explore how these principles apply to real-world technologies and natural phenomena.

### 4.3.1 Circular Motion of Charged Particles

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/q7yDsDp.png" alt="Circular Motion of Charged Particle in Magnetic Field" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.3.1:</b> A charged particle moving perpendicular to a uniform magnetic field experiences a centripetal magnetic force, resulting in uniform circular motion.</i></figcaption>
</figure>

When a charged particle enters a uniform magnetic field with velocity perpendicular to the field direction, the magnetic force acts perpendicular to the velocity. This force continuously changes the direction of motion while maintaining constant speed, resulting in uniform circular motion. This is one of the most elegant applications of the perpendicular nature of magnetic force.

The magnetic force provides exactly the centripetal force needed for circular motion. Equating the two forces gives us a fundamental relationship:

$$
q v B = \frac{m v^2}{r}
$$

where:
- $q$ = magnitude of the charge (Coulombs, C)
- $v$ = speed of the particle (meters per second, m/s)
- $B$ = magnitude of the magnetic field (Tesla, T)
- $m$ = mass of the particle (kilograms, kg)
- $r$ = radius of the circular path (meters, m)

**Solving for the radius of the circular path:**

$$
r = \frac{m v}{q B}
$$

This equation reveals several important insights: the radius increases with particle mass and speed, but decreases with greater charge and stronger magnetic field. Heavier particles follow larger circles, while more highly charged particles follow tighter curves.

**Period of Revolution - The Remarkable Independence:**

The time required for one complete circular orbit is:

$$
T = \frac{2\pi r}{v} = \frac{2\pi m}{q B}
$$

where:
- $T$ = time period of one complete revolution (seconds, s)
- $\pi$ = mathematical constant (≈ 3.14159...)

The remarkable feature of this equation is that **the period is independent of velocity and radius**—it depends only on the particle's mass, charge, and the magnetic field strength. Whether a particle moves slowly or rapidly, if it has the same $m/q$ ratio and faces the same magnetic field, it takes the same time to complete one orbit.

**Frequency of Revolution (Cyclotron Frequency):**

The number of complete revolutions per unit time is:

$$
f = \frac{1}{T} = \frac{q B}{2\pi m}
$$

where:
- $f$ = frequency of revolution (Hertz, Hz or revolutions per second)

This frequency is also called the **cyclotron frequency** or **Larmor frequency**, and its independence from velocity is the principle underlying cyclotron operation.

**Conceptual Understanding: The Steady Dance**

Imagine a merry-go-round with no friction. If you throw a ball toward it perpendicular to its edge, the ball curves and eventually orbits around the platform. Faster-thrown balls orbit in larger circles with the same speed, but all balls (of the same mass) take the same time to complete an orbit if the deflecting force is constant. Similarly, charged particles in a magnetic field orbit in paths whose size depends on speed, but the orbital period remains constant—making magnetic fields perfect for accelerating particles at regular intervals, which is exactly how cyclotrons work.

**Mathematical Example:**

**Problem:** An electron is accelerated through a potential difference and enters a region with a uniform magnetic field of $0.1 \, \text{T}$, moving perpendicular to the field. Calculate the radius of its circular path and the time period for one revolution.

**Given:**
- Electron mass: $m = 9.1 \times 10^{-31} \, \text{kg}$
- Electron charge magnitude: $|q| = 1.6 \times 10^{-19} \, \text{C}$
- Electron velocity: $v = 3 \times 10^7 \, \text{m/s}$
- Magnetic field: $B = 0.1 \, \text{T}$
- Motion is perpendicular to field ($\theta = 90°$)

**To Find:** 
- Radius of circular path $(r)$
- Time period of revolution $(T)$

**Solution:**

Step 1: Calculate the radius using $r = \frac{mv}{qB}$:

$$
r = \frac{(9.1 \times 10^{-31}) \times (3 \times 10^{7})}{(1.6 \times 10^{-19}) \times (0.1)}
$$

Step 2: Simplify the numerator and denominator:

$$
r = \frac{2.73 \times 10^{-23}}{1.6 \times 10^{-20}} = 1.706 \times 10^{-3} \, \text{m} = 1.706 \, \text{mm}
$$

Step 3: Calculate the period using $T = \frac{2\pi m}{qB}$:

$$
T = \frac{2\pi \times (9.1 \times 10^{-31})}{(1.6 \times 10^{-19}) \times (0.1)}
$$

Step 4: Simplify:

$$
T = \frac{5.71 \times 10^{-30}}{1.6 \times 10^{-20}} = 3.57 \times 10^{-10} \, \text{s} \approx 0.357 \, \text{ns}
$$

**Answer:** The electron follows a circular path with radius approximately **1.71 mm**, completing one revolution in approximately **0.357 nanoseconds**. Notice that the period is extremely small—billions of revolutions occur each second—making precise timing critical in cyclotrons.

**Physical Significance:** This rapid orbital motion at the atomic scale demonstrates why electromagnetic deflection is so effective. Electrons in cathode ray tubes follow such tight, rapid circles that precise beam steering is possible. The same principle allows mass spectrometers to separate isotopes and particle accelerators to achieve relativistic energies.

### 4.3.2 Helical Motion of Charged Particles

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/wPV638A.png" alt="Helical Path of Charged Particle in Magnetic Field" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.3.2:</b> When a charged particle enters a magnetic field at an angle, it follows a helical (spiral) trajectory combining circular motion perpendicular to the field with linear motion parallel to it.</i></figcaption>
</figure>

In many practical situations, charged particles enter magnetic fields at angles other than 90 degrees. When this occurs, the velocity vector can be decomposed into two components: perpendicular and parallel to the magnetic field. Each component experiences different effects, resulting in a combined helical motion.

**Decomposing the Velocity:**

When a particle with total velocity $v$ enters at angle $\theta$ to the magnetic field:

$$
v_{\perp} = v \sin \theta \quad \text{(perpendicular component)}
$$

$$
v_{\parallel} = v \cos \theta \quad \text{(parallel component)}
$$

where:
- $v_{\perp}$ = velocity component perpendicular to magnetic field (m/s)
- $v_{\parallel}$ = velocity component parallel to magnetic field (m/s)
- $\theta$ = angle between velocity and magnetic field (degrees or radians)

**Circular Motion from Perpendicular Component:**

The perpendicular component $v_{\perp}$ causes circular motion in the plane perpendicular to $\mathbf{B}$, with radius:

$$
r = \frac{m v_{\perp}}{q B} = \frac{m v \sin \theta}{q B}
$$

**Linear Motion from Parallel Component:**

The parallel component $v_{\parallel}$ is unaffected by the magnetic field (since $\sin 0° = 0$ and $\sin 180° = 0$). Therefore, the particle moves with constant velocity $v_{\parallel}$ along the magnetic field lines throughout its motion.

**Pitch of the Helix - The Advance Per Revolution:**

The **pitch** is the distance the particle advances along the magnetic field direction in one complete revolution:

$$
p = v_{\parallel} \times T = v \cos \theta \times \frac{2\pi m}{q B}
$$

where:
- $p$ = pitch of helical path (meters, m)
- $T$ = period of one revolution (seconds, s)

The pitch determines how tightly or loosely the helix is wound. If $v_{\parallel} = 0$ (purely perpendicular motion), pitch is zero and motion becomes purely circular. If $v_{\perp} = 0$ (purely parallel motion), there is no circular component and the particle travels straight along the field.

**Conceptual Understanding: The Spiral Staircase**

Imagine a spiral staircase or a DNA double helix. As you climb the staircase, you move both upward (parallel to the central axis) and in circles (around the axis). A charged particle in an angled magnetic field does the same—it circles around the magnetic field lines while advancing along them, creating a spiral trajectory. On Earth, solar wind particles follow such helical paths along magnetic field lines, eventually funneling toward the poles where they collide with atmospheric molecules to create auroras.

**Mathematical Example:**

**Problem:** A proton enters a uniform magnetic field of strength $0.1 \, \text{T}$ with velocity $3 \times 10^6 \, \text{m/s}$ at an angle of $30°$ to the field. Calculate the radius of the helical path, the pitch, and the time period.

**Given:**
- Proton mass: $m = 1.67 \times 10^{-27} \, \text{kg}$
- Proton charge: $q = 1.6 \times 10^{-19} \, \text{C}$
- Total velocity: $v = 3 \times 10^6 \, \text{m/s}$
- Angle to field: $\theta = 30°$
- Magnetic field: $B = 0.1 \, \text{T}$

**To Find:** Radius $(r)$, pitch $(p)$, and period $(T)$

**Solution:**

Step 1: Calculate velocity components:

$$
v_{\perp} = v \sin 30° = 3 \times 10^6 \times 0.5 = 1.5 \times 10^6 \, \text{m/s}
$$

$$
v_{\parallel} = v \cos 30° = 3 \times 10^6 \times 0.866 = 2.598 \times 10^6 \, \text{m/s}
$$

Step 2: Calculate radius of circular motion (using perpendicular component):

$$
r = \frac{m v_{\perp}}{q B} = \frac{(1.67 \times 10^{-27}) \times (1.5 \times 10^6)}{(1.6 \times 10^{-19}) \times (0.1)}
$$

$$
r = \frac{2.505 \times 10^{-21}}{1.6 \times 10^{-20}} = 0.157 \, \text{m}
$$

Step 3: Calculate period (note: period is independent of velocity):

$$
T = \frac{2\pi m}{q B} = \frac{2\pi \times (1.67 \times 10^{-27})}{(1.6 \times 10^{-19}) \times (0.1)}
$$

$$
T = \frac{1.049 \times 10^{-26}}{1.6 \times 10^{-20}} = 6.56 \times 10^{-7} \, \text{s}
$$

Step 4: Calculate pitch (distance advanced per revolution):

$$
p = v_{\parallel} \times T = (2.598 \times 10^6) \times (6.56 \times 10^{-7})
$$

$$
p = 1.703 \, \text{m}
$$

**Answer:** The proton follows a helical path with:
- **Radius:** $0.157 \, \text{m}$ (circular component in perpendicular plane)
- **Pitch:** $1.703 \, \text{m}$ (advance along field per revolution)
- **Period:** $6.56 \times 10^{-7} \, \text{s}$ (time for one complete loop)

**Physical Interpretation:** In each revolution (~0.66 microseconds), the proton advances about 1.7 meters along the magnetic field while circling in a radius of 15.7 centimeters. This creates a spiral trajectory approximately as wide as a person's height but advancing over a meter per loop.

### 4.3.3 Applications in Natural Phenomena and Technology

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/particle-applications.png" alt="Applications of Charged Particle Motion" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.3.3:</b> Charged particles from cosmic rays and solar wind follow helical paths along Earth's magnetic field, concentrating toward the polar regions.</i></figcaption>
</figure>

The principles of circular and helical motion find critical applications across multiple domains:

**Natural Phenomena:**

**Aurora Formation:** Solar wind particles (protons and electrons) spiral along Earth's magnetic field lines toward the polar regions. As they collide with nitrogen and oxygen molecules in the upper atmosphere (100-400 km altitude), they excite these molecules, causing them to emit light as the Northern Lights (Aurora Borealis) or Southern Lights (Aurora Australis). The magnetic field effectively funnels particles from the equator toward the poles, concentrating these spectacular light shows in polar regions.

**Cosmic Ray Deflection:** High-energy cosmic rays from supernovae and other sources are deflected by galactic and interstellar magnetic fields. This deflection extends their paths through space and affects which particles reach Earth, influencing cosmic ray flux measurements and providing clues about distant cosmic events.

**Technology Applications:**

**Cyclotrons and Particle Accelerators:** Rely on the velocity-independent period to accelerate particles. Protons or other charged particles are repeatedly accelerated across a gap in synchronization with an oscillating electric field. Each time they cross, they gain energy and move in a larger circle, eventually spiraling outward and exiting with high energy. Modern cyclotrons accelerate particles to energies of 10-30 MeV, used for medical isotope production and radiation therapy.

**Mass Spectrometry:** Different isotopes have different mass-to-charge ratios, causing them to follow different circular paths when accelerated through the same potential and deflected by the same magnetic field. This separation allows identification and analysis of molecular and isotopic composition of samples.

**Electron Microscopes:** Magnetic coils act as lenses, focusing electron beams onto samples. The circular motion of electrons in these magnetic fields enables magnifications exceeding 1 million times, revealing cellular and subcellular structures invisible to optical microscopes.

**Plasma Confinement:** In fusion reactors like tokamaks, strong magnetic fields confine hot plasma by forcing ions and electrons into helical trajectories that prevent them from touching the reactor walls. This magnetic confinement is essential for reaching the extreme temperatures (>100 million Kelvin) needed for controlled fusion reactions.

---

## 4.4 Force on a Current-Carrying Conductor in a Magnetic Field

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/AN5cMle.png" alt="Force on Current-Carrying Wire in Magnetic Field" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.4:</b> A current-carrying conductor placed in a magnetic field experiences a force due to the interaction between moving charges and the magnetic field.</i></figcaption>
</figure>

The relationship between electric current and magnetic fields provides the foundation for countless practical devices, from electric motors to magnetic brakes. When electrical charges move through a conductor in the presence of a magnetic field, they experience the Lorentz force, which manifests as a macroscopic force on the conductor itself. This principle, systematically explored by André-Marie Ampère in the early 19th century, unified the understanding of electromagnetism and enabled the development of electromagnetic machines.

A current-carrying conductor represents numerous charge carriers moving with drift velocity. Each individual charge experiences a magnetic force $\mathbf{F} = q(\mathbf{v} \times \mathbf{B})$. Since all charge carriers in a wire move in the same direction with the same drift velocity, these individual forces add up constructively, producing a significant macroscopic force on the entire conductor. This cumulative effect is why magnetic fields can push or pull conductors with considerable force, enabling motor operation and electromagnetic machinery.

In this section, we derive expressions for the force on current-carrying conductors, analyze how this force depends on conductor orientation, and examine the torque produced on current loops. We also explore the connection to magnetic dipole moment and applications ranging from electric motors to electromagnetic switches and relays.

### 4.4.1 Magnetic Force on a Straight Current-Carrying Conductor

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/force-straight-wire.png" alt="Force on Straight Current-Carrying Wire" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.4.1:</b> Force direction on a current-carrying conductor determined by Fleming's left-hand rule, showing relationship between current, field, and force directions.</i></figcaption>
</figure>

When a straight conductor of length $L$ carrying current $I$ is placed in a uniform magnetic field $\mathbf{B}$, the conductor experiences a force. The magnitude of this force depends on three factors: the strength of the current, the length of the conductor, the magnetic field strength, and critically, the angle between the conductor and the field direction.

**Mathematical Expression:**

$$
F = I L B \sin \theta
$$

where:
- $F$ = magnitude of magnetic force on conductor (Newtons, N)
- $I$ = electric current flowing through conductor (Amperes, A)
- $L$ = length of conductor in the magnetic field (meters, m)
- $B$ = magnitude of magnetic field (Tesla, T)
- $\theta$ = angle between conductor direction and magnetic field direction (degrees or radians)

**Vector Form:**

The complete vector expression for magnetic force is:

$$
\mathbf{F} = I \mathbf{L} \times \mathbf{B}
$$

where:
- $\mathbf{F}$ = magnetic force vector (Newtons, N)
- $I$ = current magnitude (Amperes, A)
- $\mathbf{L}$ = length vector pointing in direction of current flow (meters, m)
- $\mathbf{B}$ = magnetic field vector (Tesla, T)
- $\times$ = cross product operator producing perpendicular resultant

**Special Cases:**

When $\theta = 0°$ (conductor parallel to field): $\sin 0° = 0$, so $F = 0$ (no force)

When $\theta = 90°$ (conductor perpendicular to field): $\sin 90° = 1$, so $F_{\max} = IBL$ (maximum force)

**Direction of Force - Fleming's Left-Hand Rule:**

The direction is determined by **Fleming's left-hand rule**:
1. Point your **thumb** in direction of **current** ($I$)
2. Point your **index finger** in direction of **magnetic field** ($\mathbf{B}$)
3. Your **middle finger** points in direction of **force** ($\mathbf{F}$)

This rule helps visualize force direction without calculating cross products, making it invaluable in circuit design and motor engineering.

**Conceptual Understanding: The Pushing Effect**

Imagine water flowing through a pipe that crosses a region of strong wind (magnetic field). The flowing water (current) experiences a sideways push from the wind. Similarly, current-carrying conductors in magnetic fields experience perpendicular forces. The stronger the water flow (more current) and the wider the pipe (longer conductor), the greater the total push. But if the pipe runs parallel to wind direction, the wind has no perpendicular component, so no force acts. When perpendicular, the force is maximum—exactly like our conductor and field.

**Mathematical Example:**

**Problem:** A straight wire of length $0.5 \, \text{m}$ carrying a current of $4 \, \text{A}$ is placed perpendicular to a uniform magnetic field of $0.3 \, \text{T}$. Calculate the magnetic force on the wire.

**Given:**
- Length of conductor: $L = 0.5 \, \text{m}$
- Current: $I = 4 \, \text{A}$
- Magnetic field: $B = 0.3 \, \text{T}$
- Angle: $\theta = 90°$ (perpendicular placement)

**To Find:** Magnetic force $F$

**Solution:**

Step 1: Apply the force formula with $\sin 90° = 1$:

$$
F = I L B \sin \theta = 4 \times 0.5 \times 0.3 \times 1
$$

Step 2: Calculate:

$$
F = 0.6 \, \text{N}
$$

Step 3: Determine direction using Fleming's left-hand rule: If current flows to the right and field points downward, force points toward you (out of the page).

**Answer:** The magnetic force on the wire is **0.6 Newtons**, pointing perpendicular to both current and field directions according to Fleming's left-hand rule.

**Physical Significance:** This 0.6 N force can lift a 60-gram mass against gravity, demonstrating how electromagnetic forces manipulate conductors in practical devices like loudspeakers and electromagnetic actuators.

### 4.4.2 Torque on a Current Loop and Magnetic Dipole Moment

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/torque-loop-magnetic.png" alt="Torque on Current Loop in Magnetic Field" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.4.2:</b> A rectangular current loop in a magnetic field experiences a net torque that tends to align the loop with the field, demonstrating the principle of electric motors.</i></figcaption>
</figure>

When a current loop (typically rectangular) is placed in a uniform magnetic field at an angle to the field direction, opposite sides of the loop experience forces in opposite directions. These forces don't cancel—instead, they produce a net **torque** that rotates the loop. This principle is fundamental to electric motor operation.

**Torque Formula:**

For a rectangular loop of area $A$ carrying current $I$ in a uniform magnetic field $B$:

$$
\tau = I A B \sin \theta
$$

where:
- $\tau$ = torque (tau) on the loop (Newton-meters, N·m)
- $I$ = current through loop (Amperes, A)
- $A$ = area enclosed by loop (square meters, m²)
- $B$ = magnitude of magnetic field (Tesla, T)
- $\theta$ = angle between normal to loop and magnetic field (degrees or radians)

**Magnetic Dipole Moment:**

The product $m = IA$ defines the **magnetic dipole moment**:

$$
m = I A
$$

where:
- $m$ = magnetic dipole moment (Ampere-square meters, A·m²)
- The direction of $m$ is perpendicular to the loop plane, given by right-hand rule

Using this definition, the torque can be elegantly rewritten as:

$$
\tau = m B \sin \theta
$$

This form shows that torque depends on the magnetic moment—a fundamental property of any current loop or magnetic material.

**Special Cases:**

When $\theta = 0°$ (loop normal parallel to field): Torque is zero (stable equilibrium—loop aligned with field)

When $\theta = 90°$ (loop normal perpendicular to field): Torque is maximum, $\tau_{\max} = mB$ (unstable position)

**Conceptual Understanding: The Spinning Door**

Imagine a door hanging perpendicular to a strong wind (magnetic field). Wind forces on the top and bottom edges push in opposite directions, creating rotational motion around the hinges. The wider the door and stronger the wind, the greater the spinning effect. Similarly, a current loop in a magnetic field experiences opposite forces on opposite sides, producing torque that spins the loop toward alignment with the field.

**Mathematical Example:**

**Problem:** A rectangular current loop has dimensions $0.3 \, \text{m} \times 0.2 \, \text{m}$ and carries a current of $2.5 \, \text{A}$. The loop is placed in a $0.5 \, \text{T}$ magnetic field at an angle of $60°$ to the field. Calculate the torque on the loop and the magnetic dipole moment.

**Given:**
- Loop dimensions: $0.3 \, \text{m} \times 0.2 \, \text{m}$
- Current: $I = 2.5 \, \text{A}$
- Magnetic field: $B = 0.5 \, \text{T}$
- Angle: $\theta = 60°$

**To Find:** Torque $(\tau)$ and magnetic dipole moment $(m)$

**Solution:**

Step 1: Calculate loop area:

$$
A = 0.3 \times 0.2 = 0.06 \, \text{m}^2
$$

Step 2: Calculate magnetic dipole moment:

$$
m = I A = 2.5 \times 0.06 = 0.15 \, \text{A·m}^2
$$

Step 3: Calculate torque with $\sin 60° = 0.866$:

$$
\tau = m B \sin \theta = 0.15 \times 0.5 \times 0.866 = 0.065 \, \text{N·m}
$$

**Answer:** The magnetic dipole moment is **0.15 A·m²** and the torque on the loop is **0.065 N·m**, causing the loop to rotate toward alignment with the magnetic field.

**Physical Interpretation:** This torque value (about 0.065 N·m) can rotate the loop quite noticeably if it's free to move, demonstrating the significant rotational forces available from electromagnetic interactions. This is the exact principle used in electric motors, where rapidly switching magnetic fields continuously rotate coils to produce mechanical motion.

### 4.4.3 Applications in Motors and Electromagnetic Devices

The principles of force on current-carrying conductors and torque on loops form the foundation of numerous practical devices:

**Electric Motors:** The fundamental operating principle relies on the continuous rotation of current-carrying coils in magnetic fields. Permanent magnets or electromagnets create the magnetic field, while rotating commutators ensure the current direction changes as the coil rotates, maintaining continuous torque. DC motors, AC induction motors, and brushless motors all exploit this same underlying physics.

**Electromagnetic Relays:** These devices use the force on a current-carrying conductor to mechanically switch electrical circuits on or off. When sufficient current flows through a coil, the resulting magnetic force pulls an armature, opening or closing contacts. Relays enable remote control of high-power circuits using low-power control signals.

**Magnetic Brakes:** Eddy currents induced in a conductor moving through a magnetic field create forces opposing the motion (Lenz's law), converting kinetic energy to heat. This electromagnetic braking is used in emergency stops, regenerative braking in electric vehicles, and precision positioning systems.

**Loudspeakers:** A voice coil (small current-carrying conductor) attached to a cone-shaped diaphragm sits in a strong magnetic field. When audio signals pass through the coil, varying magnetic forces push and pull the diaphragm, creating sound waves.

**Electromagnetic Actuators:** Industrial applications use controlled electromagnetic forces to move components precisely, from automated assembly lines to medical devices requiring exact positioning.

---

## 4.5 Biot–Savart Law

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/x5uif7n.png" alt="Biot-Savart Law Setup" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.5:</b> Biot-Savart law determines the magnetic field contribution from an infinitesimal current element at distance r from observation point P.</i></figcaption>
</figure>

The Biot–Savart law, formulated independently by French physicists Jean-Baptiste Biot and Félix Savart in 1820, provides a fundamental method for calculating magnetic fields produced by current distributions. This law serves as the magnetic analog to Coulomb's law in electrostatics—just as Coulomb's law calculates electric fields from static charges, the Biot–Savart law calculates magnetic fields from moving charges (currents). The law emerged from experimental observations and has proven to be one of the most powerful tools in electromagnetics for analyzing magnetic fields in systems with complex geometries.

The Biot–Savart law establishes that magnetic fields are produced locally by current elements and can be superposed by integration. Unlike Coulomb's law, which gives the field from a point charge directly, the Biot–Savart law works with infinitesimal current elements and requires integration over the entire current distribution. This differential approach reveals the deep connection between current direction, geometry, and the resulting magnetic field configuration, making it indispensable for understanding electromagnet design, transformer operation, and magnetic field mapping in complex systems.

In this section, we explore the mathematical expression of the Biot–Savart law, its physical interpretation, and its application to calculate magnetic fields for various current geometries. We'll derive expressions for common configurations including straight wires, circular loops, and solenoids, demonstrating how this fundamental law unifies the description of magnetic fields across diverse practical applications.

### 4.5.1 Statement and Mathematical Expression

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/biot-savart-elements.png" alt="Current Element and Field Contribution" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.5.1:</b> An infinitesimal current element Idl at point O produces a magnetic field contribution dB at observation point P.</i></figcaption>
</figure>

The Biot–Savart law states that the magnetic field $d\mathbf{B}$ produced by a small current element at a point in space is proportional to the current, the length of the element, and the sine of the angle between the element and the line connecting the element to the observation point. Crucially, this field contribution is inversely proportional to the square of the distance.

**Mathematical Statement:**

The magnetic field contribution from an infinitesimal current element $I d\mathbf{l}$ at distance $r$ from observation point $P$ is:

$$
d\mathbf{B} = \frac{\mu_0}{4\pi} \frac{I d\mathbf{l} \times \hat{\mathbf{r}}}{r^2}
$$

where:
- $d\mathbf{B}$ = magnetic field contribution from current element (Tesla, T)
- $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$ = permeability of free space (Tesla-meter per Ampere)
- $I$ = current flowing through conductor (Amperes, A)
- $d\mathbf{l}$ = length vector of current element pointing in current direction (meters, m)
- $\hat{\mathbf{r}}$ = unit vector pointing from current element to observation point (dimensionless)
- $r$ = distance from current element to observation point (meters, m)
- $\times$ = cross product operator (produces perpendicular vector)

**Scalar Form - When Perpendicular:**

When the current element is perpendicular to the line connecting it to point $P$ (i.e., $\theta = 90°$):

$$
dB = \frac{\mu_0}{4\pi} \frac{I \, dl}{r^2}
$$

**General Scalar Form - Any Angle:**

When the current element makes angle $\theta$ with the radial direction:

$$
dB = \frac{\mu_0}{4\pi} \frac{I \, dl \sin \theta}{r^2}
$$

**Total Magnetic Field - Integration:**

To find the total magnetic field at point $P$ from an extended current distribution, integrate contributions from all current elements:

$$
\mathbf{B} = \int d\mathbf{B} = \frac{\mu_0}{4\pi} \int \frac{I d\mathbf{l} \times \hat{\mathbf{r}}}{r^2}
$$

**Physical Interpretation:**

The Biot–Savart law reveals several fundamental principles:

1. **Inverse square relationship:** Magnetic field decreases as $1/r^2$, same as electric field from point charges
2. **Directional dependence:** The cross product $d\mathbf{l} \times \hat{\mathbf{r}}$ ensures field is perpendicular to both current direction and radial direction
3. **Superposition principle:** Total field is vector sum of contributions from all current elements
4. **Current dependence:** Stronger currents produce stronger fields

**Conceptual Understanding: The Ripple Pattern**

Imagine tapping a ripple source in a pond—each tap creates circular ripples radiating outward. The ripple amplitude (analogous to magnetic field) is strongest near the source and weakens as $1/\text{distance}^2$. A steady current is like continuous tapping—creating a continuous magnetic field pattern around the wire. Magnetic field lines form concentric circles around the wire (right-hand rule), with spacing increasing as you move away, exactly representing the $1/r^2$ behavior.

**Mathematical Example:**

**Problem:** Calculate the magnetic field at point $P$ located at perpendicular distance $r = 0.2 \, \text{m}$ from a very small current element of length $dl = 0.01 \, \text{m}$ carrying current $I = 5 \, \text{A}$, where the current element is perpendicular to the line from element to $P$.

**Given:**
- Permeability of free space: $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$
- Current: $I = 5 \, \text{A}$
- Element length: $dl = 0.01 \, \text{m}$
- Distance to point P: $r = 0.2 \, \text{m}$
- Angle: $\theta = 90°$ (perpendicular)

**To Find:** Magnetic field contribution $dB$

**Solution:**

Step 1: Apply scalar form for perpendicular element:

$$
dB = \frac{\mu_0}{4\pi} \frac{I \, dl}{r^2}
$$

Step 2: Substitute values:

$$
dB = \frac{4\pi \times 10^{-7}}{4\pi} \times \frac{5 \times 0.01}{(0.2)^2}
$$

Step 3: Simplify:

$$
dB = 10^{-7} \times \frac{0.05}{0.04} = 10^{-7} \times 1.25 = 1.25 \times 10^{-7} \, \text{T}
$$

**Answer:** The magnetic field contribution from this small current element is **1.25 × 10⁻⁷ Tesla** or **125 nanotesla**, directed perpendicular to both the current element and the radial direction (by right-hand rule).

### 4.5.2 Applications of Biot–Savart Law

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/biot-savart-applications.png" alt="Applications of Biot-Savart Law" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.5.2:</b> Magnetic field configurations for different current geometries: (a) straight infinite wire, (b) finite straight wire, (c) circular loop, (d) solenoid.</i></figcaption>
</figure>

The Biot–Savart law can be integrated over various current geometries to derive useful expressions for magnetic fields. Here are the most important applications:

**Magnetic Field of Infinite Straight Wire:**

For a long straight conductor carrying current $I$, the magnetic field at perpendicular distance $r$ is:

$$
B = \frac{\mu_0 I}{2\pi r}
$$

where:
- $B$ = magnetic field magnitude at distance $r$ (Tesla, T)
- All other symbols have previous definitions

The field circles the wire according to the right-hand rule—thumb in current direction, fingers curl in field direction. Field strength decreases inversely with distance.

**Magnetic Field at Center of Circular Loop:**

For a circular loop of radius $R$ carrying current $I$, the magnetic field at the center is:

$$
B = \frac{\mu_0 I}{2 R}
$$

This uniform expression shows that field magnitude depends only on current and loop radius, independent of the loop's position in space (translation symmetry). The field points perpendicular to the loop plane, direction given by right-hand rule (fingers along current, thumb points in field direction).

**Magnetic Field on Axis of Circular Loop:**

At distance $z$ from the loop center along the axis:

$$
B = \frac{\mu_0 I R^2}{2(R^2 + z^2)^{3/2}}
$$

At the center ($z = 0$), this reduces to the center formula. Far from the loop ($z \gg R$), the field weakens as $1/z^3$, characteristic of a magnetic dipole.

**Magnetic Field Inside a Solenoid:**

A solenoid with $N$ turns over length $l$ carrying current $I$ produces uniform field inside:

$$
B = \mu_0 \frac{N}{l} I = \mu_0 n I
$$

where $n = N/l$ is the number of turns per unit length. Outside an ideal infinite solenoid, the field is zero.

**Conceptual Understanding: Building Magnetic Architecture**

The Biot–Savart law is like an architect's blueprint for constructing magnetic fields. Want a circular pattern? Use a circular wire—integrate the law around the circle. Want a uniform field? Use a solenoid—integrate contributions from parallel turns. Each geometry creates a characteristic field pattern determined by the current distribution geometry.

**Mathematical Example:**

**Problem:** Calculate the magnetic field at perpendicular distance $0.05 \, \text{m}$ (5 cm) from a long straight wire carrying current $2 \, \text{A}$.

**Given:**
- Permeability: $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$
- Current: $I = 2 \, \text{A}$
- Distance: $r = 0.05 \, \text{m}$

**To Find:** Magnetic field $B$

**Solution:**

Step 1: Apply straight wire formula:

$$
B = \frac{\mu_0 I}{2\pi r} = \frac{4\pi \times 10^{-7} \times 2}{2\pi \times 0.05}
$$

Step 2: Simplify:

$$
B = \frac{8\pi \times 10^{-7}}{0.1\pi} = \frac{8 \times 10^{-7}}{0.1} = 8 \times 10^{-6} \, \text{T}
$$

**Answer:** The magnetic field at 5 cm from the wire is **8 × 10⁻⁶ Tesla** or **8 microTesla**, directed perpendicular to the plane containing the wire and observation point.

**Physical Comparison:** This field (8 μT) is comparable to Earth's magnetic field (~25-65 μT), showing that ordinary wires with modest currents produce significant magnetic effects. This principle is exploited in electromagnets, transformers, and electromagnetic switches used throughout electrical devices.

### 4.5.3 Relationship to Ampère's Law

The Biot–Savart law and Ampère's circuital law are complementary approaches to calculating magnetic fields. While Biot–Savart works for any current configuration through integration, Ampère's law is simpler for highly symmetric systems. For a long straight wire:

- **Biot–Savart approach:** Integrate contributions from each element along the infinite wire
- **Ampère's approach:** Use the symmetry to simplify the line integral

Both methods yield identical results: $B = \frac{\mu_0 I}{2\pi r}$. The choice between them depends on the geometry and symmetry of the specific problem—Biot–Savart for complex shapes, Ampère's law for symmetric configurations.

---

## 4.6 Ampère's Circuital Law

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/bnfDFK6.png" alt="Ampere's Law Closed Path" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.6:</b> Ampère's circuital law relates the line integral of magnetic field around a closed path to the enclosed current.</i></figcaption>
</figure>

Ampère's circuital law, formulated by French physicist André-Marie Ampère in 1826, represents one of the cornerstones of magnetostatics. This law establishes a fundamental relationship between the magnetic field circulating around a closed path and the electric current passing through that path. Unlike the Biot–Savart law which requires integration over the entire current distribution, Ampère's law leverages symmetry to provide elegant solutions for magnetic fields in highly symmetric configurations. When combined with Gauss's law, Faraday's law, and the continuity equation, it forms part of Maxwell's equations—the complete description of electromagnetic phenomena.

The beauty of Ampère's circuital law lies in its simplicity for symmetric systems. When a current distribution possesses cylindrical, planar, or toroidal symmetry, Ampère's law transforms a difficult integral into a simple algebraic calculation. This makes it invaluable in designing electromagnets, transformers, and inductors used in power transmission and electronics. The law embodies a deep principle: magnetic fields are generated by currents and circulate around them in a manner quantitatively related to the current magnitude.

In this section, we present the mathematical statement and physical meaning of Ampère's circuital law, explore its application to symmetric current geometries (infinite wires, solenoids, toroids), and demonstrate how it complements the Biot–Savart law. We'll examine practical examples where symmetry enables rapid magnetic field calculation and discuss the limitations of the law for non-symmetric configurations.

### 4.6.1 Statement and Mathematical Form

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/ampere-law-concept.png" alt="Amperian Loop Concept" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.6.1:</b> An Amperian closed loop enclosing current I, illustrating how the line integral of B around the loop relates to enclosed current.</i></figcaption>
</figure>

Ampère's circuital law states that the line integral of the magnetic field $\mathbf{B}$ around any closed path (called an Amperian loop) equals the permeability of free space multiplied by the total electric current enclosed by that path.

**Mathematical Statement:**

$$
\oint \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_{\text{enc}}
$$

where:
- $\oint$ = line integral around a closed path (contour integral)
- $\mathbf{B}$ = magnetic field vector at points on the path (Tesla, T)
- $d\mathbf{l}$ = infinitesimal length vector tangent to the path (meters, m)
- $\mathbf{B} \cdot d\mathbf{l}$ = dot product (scalar multiplication of magnitudes when parallel)
- $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$ = permeability of free space
- $I_{\text{enc}}$ = total current passing through the surface bounded by the path (Amperes, A)

**Physical Interpretation:**

The line integral $\oint \mathbf{B} \cdot d\mathbf{l}$ represents the total "circulation" of the magnetic field around the closed path. It measures how much the magnetic field aligns with the path direction. When $\mathbf{B}$ and $d\mathbf{l}$ point in the same direction, the dot product is positive; when opposite, it's negative.

**Sign Convention for Current:**

Using the right-hand rule: curl your right hand's fingers in the direction of the path integration, and your thumb points in the positive current direction. Currents flowing in this direction are counted as positive; those in the opposite direction are negative.

**For Highly Symmetric Cases:**

When the magnetic field has constant magnitude and is tangent to a circular Amperian loop:

$$
B \oint dl = B(2\pi r) = \mu_0 I_{\text{enc}}
$$

Therefore:

$$
B = \frac{\mu_0 I_{\text{enc}}}{2\pi r}
$$

**Conceptual Understanding: The Swirling Water Analogy**

Imagine water swirling around a drain (current flowing downward). The faster the water swirls and the closer you are to the drain, the stronger the circulation. If you draw any closed loop around the drain and measure the water's tangential velocity (analogous to $\mathbf{B}$) all around the loop, the total circulation (analogous to $\oint \mathbf{B} \cdot d\mathbf{l}$) is proportional to the drain flow rate (analogous to $I_{\text{enc}}$). Change the loop shape but keep the same drain—the total circulation remains constant!

**Mathematical Example:**

**Problem:** A long straight wire carries current $I = 3 \, \text{A}$. Calculate the magnetic field at distance $r = 0.1 \, \text{m}$ from the wire using Ampère's law.

**Given:**
- Current: $I = 3 \, \text{A}$
- Distance: $r = 0.1 \, \text{m}$
- Permeability: $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$

**To Find:** Magnetic field $B$

**Solution:**

Step 1: Choose an Amperian loop—a circle of radius $r$ centered on the wire, in a plane perpendicular to it.

Step 2: By symmetry, $\mathbf{B}$ is constant in magnitude and tangent to the circle:

$$
\oint \mathbf{B} \cdot d\mathbf{l} = \oint B \, dl = B \oint dl = B(2\pi r)
$$

Step 3: Apply Ampère's law. The enclosed current is $I_{\text{enc}} = I = 3 \, \text{A}$:

$$
B(2\pi r) = \mu_0 I
$$

Step 4: Solve for $B$:

$$
B = \frac{\mu_0 I}{2\pi r} = \frac{4\pi \times 10^{-7} \times 3}{2\pi \times 0.1}
$$

Step 5: Simplify:

$$
B = \frac{4\pi \times 10^{-7} \times 3}{0.2\pi} = \frac{12 \times 10^{-7}}{0.2} = 6 \times 10^{-6} \, \text{T}
$$

**Answer:** The magnetic field at 10 cm from the wire is **6 × 10⁻⁶ Tesla** or **6 microTesla**, directed tangentially according to the right-hand rule (thumb in current direction, fingers point in field direction).

### 4.6.2 Applications of Ampère's Law

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/ampere-applications.png" alt="Applications of Ampere's Law" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.6.2:</b> Field configurations for different symmetric geometries: (a) infinite straight wire with concentric field circles, (b) long solenoid with uniform interior field, (c) toroid with field only inside the ring.</i></figcaption>
</figure>

Ampère's law simplifies dramatically for symmetric current distributions. Here are the most important applications:

**Magnetic Field of Infinite Straight Wire:**

For a long straight conductor carrying current $I$, the magnetic field at perpendicular distance $r$ is:

$$
B = \frac{\mu_0 I}{2\pi r}
$$

where:
- $B$ = magnetic field magnitude (Tesla, T)
- All symbols have previous definitions

The magnetic field forms concentric circles around the wire, following the right-hand rule. Field strength decreases as $1/r$, which is faster than the $1/r^2$ decrease for electric fields (due to the circulation nature of magnetic fields).

**Magnetic Field Inside a Long Solenoid:**

A solenoid consists of $N$ closely spaced turns of wire wrapped helically around a cylindrical form, carrying current $I$ through length $l$. Inside an ideal (infinitely long) solenoid, the field is uniform:

$$
B = \mu_0 n I = \mu_0 \frac{N}{l} I
$$

where:
- $n = N/l$ = number of turns per unit length (turns per meter, m⁻¹)
- Field is parallel to the solenoid axis
- Field outside an ideal solenoid is zero

The uniformity of the interior field makes solenoids invaluable for creating controlled magnetic fields in laboratories and MRI machines. The field magnitude depends only on current and turn density, not on solenoid radius or length.

**Magnetic Field Inside a Toroid:**

A toroid is a solenoid bent into a doughnut shape with $N$ turns. The magnetic field exists only inside the toroid (in the "doughnut hole"), and at distance $r$ from the central axis:

$$
B = \frac{\mu_0 N I}{2\pi r}
$$

where:
- $N$ = total number of turns
- $r$ = distance from central axis to the point of interest
- Field is tangential, forming circles around the central axis
- Outside the toroid: $B = 0$

The $1/r$ dependence means field strength varies around the toroid—stronger near the inner edge, weaker near the outer edge.

**Conceptual Understanding: Building Symmetric Fields**

Ampère's law reveals that symmetric current geometries create symmetric field patterns. A wire wrapped helically (solenoid) creates a uniform field inside—useful for uniform deflection of particle beams. Bending that solenoid into a toroid confines the field to the ring region—useful for plasma confinement in fusion reactors. Each geometry's symmetry is the key to rapid field calculation.

**Mathematical Example:**

**Problem:** A solenoid has length $L = 0.5 \, \text{m}$, contains $N = 1000$ turns, and carries current $I = 2 \, \text{A}$. Calculate the magnetic field inside the solenoid.

**Given:**
- Length: $L = 0.5 \, \text{m}$
- Number of turns: $N = 1000$
- Current: $I = 2 \, \text{A}$
- Permeability: $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$

**To Find:** Magnetic field inside solenoid $B$

**Solution:**

Step 1: Calculate the turn density:

$$
n = \frac{N}{L} = \frac{1000}{0.5} = 2000 \, \text{turns/m}
$$

Step 2: Apply the solenoid formula:

$$
B = \mu_0 n I = 4\pi \times 10^{-7} \times 2000 \times 2
$$

Step 3: Calculate:

$$
B = 4\pi \times 10^{-7} \times 4000 = 1.6\pi \times 10^{-3} \, \text{T}
$$

$$
B = 5.03 \times 10^{-3} \, \text{T} = 5.03 \, \text{mT}
$$

**Answer:** The magnetic field inside the solenoid is **5.03 millitesla**, directed parallel to the solenoid axis. This field is uniform throughout the interior and independent of position within the solenoid.

**Physical Significance:** A field of 5 mT is significant for practical applications. MRI machines use fields of 1.5-3 Tesla (achieved with superconducting solenoids), while this modest electromagnet produces 5 millitesla—sufficient for numerous laboratory experiments, magnetic deflection, and educational demonstrations.

### 4.6.3 Ampère's Law vs Biot–Savart Law

Both laws describe the same magnetic fields but are applied differently:

| Aspect | Ampère's Law | Biot–Savart Law |
|--------|-------------|-----------------|
| **Best for** | Symmetric current distributions | Any current geometry |
| **Calculation** | Line integral around chosen path | Integration over all current elements |
| **Effort** | Simple for symmetric cases | Requires full integration |
| **Limitations** | Needs high symmetry to simplify | Always works but often lengthy |
| **Example strength** | Infinite wires, solenoids, toroids | Finite wires, irregular loops |

For a long straight wire, both yield $B = \frac{\mu_0 I}{2\pi r}$. Choose the method based on the problem's geometry and symmetry.

---

## 4.7 Force Between Two Parallel Currents

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/LPHqkd8.png" alt="Force Between Two Parallel Current-Carrying Wires" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.7:</b> Two parallel current-carrying wires exert magnetic forces on each other—attractive when currents flow in the same direction, repulsive when in opposite directions.</i></figcaption>
</figure>

The electromagnetic interaction between parallel current-carrying conductors demonstrates a fundamental principle: currents produce magnetic fields, and these fields exert forces on other current-carrying conductors. This phenomenon, systematically studied by Ampère in the 1820s, provides a direct method to measure electric current through the magnetic force it generates. The interaction between parallel currents is particularly important in electrical engineering—excess forces between power transmission lines during fault conditions can cause mechanical damage, while precise force calculations are essential for motor design and current measurement.

When two long parallel conductors carry electric currents, they create magnetic fields that interact with each other's currents through the Lorentz force mechanism. If currents flow in the same direction, the magnetic field of one wire pulls the other toward it—the wires attract. If currents oppose, the wires repel. This attraction or repulsion occurs regardless of wire material, depending only on the currents and separation. This principle uniquely defined the ampere unit: one ampere is the current producing a specific force between two wires—a definition that endured for over a century before being superseded by a definition based on elementary charge.

In this section, we derive the force per unit length between parallel currents, explain the origin of attractive and repulsive forces, present the fundamental definition of the ampere, and explore applications in current measurement and electrical engineering. We'll examine how this simple formula enables predictions about forces in real electrical systems and demonstrates the vector nature of magnetic field interactions.

### 4.7.1 Derivation of Force Between Parallel Currents

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/parallel-wires-force.png" alt="Force Derivation Between Two Parallel Wires" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.7.1:</b> Wire 1 creates magnetic field B₁ at the location of wire 2; this field exerts force F on the current-carrying wire 2.</i></figcaption>
</figure>

To find the force between two parallel current-carrying conductors, we apply Ampère's law to find the magnetic field from one wire, then calculate the force this field exerts on the other wire using the Lorentz force law for currents.

**Step 1: Magnetic Field from Wire 1**

Using Ampère's law, the magnetic field produced by wire 1 carrying current $I_1$ at distance $d$ (the separation between wires) is:

$$
B_1 = \frac{\mu_0 I_1}{2\pi d}
$$

where:
- $B_1$ = magnetic field from wire 1 at wire 2's location (Tesla, T)
- $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$ = permeability of free space
- $I_1$ = current in wire 1 (Amperes, A)
- $d$ = perpendicular distance between wires (meters, m)

**Step 2: Force on Wire 2**

Wire 2, carrying current $I_2$, experiences force in the magnetic field $B_1$. For a wire segment of length $L$:

$$
F = I_2 L B_1 = I_2 L \times \frac{\mu_0 I_1}{2\pi d}
$$

**Step 3: Force Per Unit Length**

Dividing by length $L$ gives the force per unit length:

$$
\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}
$$

where:
- $F/L$ = force per unit length (Newtons per meter, N/m)
- $I_1, I_2$ = currents in the two wires (Amperes, A)
- $d$ = separation between wires (meters, m)

**By Newton's Third Law**, wire 2 exerts an equal and opposite force on wire 1, so both wires experience the same magnitude force per unit length.

**Direction of Force - Same Current or Opposite:**

- **Same direction currents:** The magnetic field from wire 1 circles it according to the right-hand rule. At wire 2's location, this field points in a direction such that it pushes wire 2 toward wire 1—the wires **attract**

- **Opposite direction currents:** The magnetic field from wire 1 at wire 2's location now points in the opposite direction, pushing wire 2 away—the wires **repel**

**Conceptual Understanding: The Magnetic Tango**

Two dancers moving in the same direction down a dance floor find themselves drawn together by invisible forces—like two parallel currents attracting. But dancers moving in opposite directions find themselves being pushed apart. This isn't about collision; it's about how their "magnetic presence" (field) affects each other when they're in motion. The stronger the motion (current) and the closer they dance (smaller separation), the stronger the effect.

**Mathematical Example:**

**Problem:** Two long parallel wires are separated by distance $d = 0.2 \, \text{m}$ and carry currents $I_1 = 2 \, \text{A}$ and $I_2 = 3 \, \text{A}$ in the same direction. Calculate the force per unit length between them.

**Given:**
- Separation: $d = 0.2 \, \text{m}$
- Current 1: $I_1 = 2 \, \text{A}$
- Current 2: $I_2 = 3 \, \text{A}$
- Permeability: $\mu_0 = 4\pi \times 10^{-7} \, \text{T·m/A}$
- Currents in same direction (attractive force)

**To Find:** Force per unit length $F/L$

**Solution:**

Step 1: Apply the force per unit length formula:

$$
\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi d}
$$

Step 2: Substitute values:

$$
\frac{F}{L} = \frac{4\pi \times 10^{-7} \times 2 \times 3}{2\pi \times 0.2}
$$

Step 3: Simplify:

$$
\frac{F}{L} = \frac{24\pi \times 10^{-7}}{0.4\pi} = \frac{24 \times 10^{-7}}{0.4} = 60 \times 10^{-7} \, \text{N/m}
$$

$$
\frac{F}{L} = 6 \times 10^{-6} \, \text{N/m}
$$

**Answer:** The force per unit length is **6 × 10⁻⁶ N/m** or **6 microNewtons per meter**, directed **toward each other** (attractive) since currents flow in the same direction.

**Physical Interpretation:** Over a 1-meter length of these wires, the total force would be 6 microNewtons—tiny but measurable with sensitive equipment. This demonstrates why electromagnetic force measurement devices must be extremely precise.

### 4.7.2 Definition of the Ampere and SI Units

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/ampere-definition.png" alt="Definition of the Ampere" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.7.2:</b> The classical definition of the ampere was based on the magnetic force between two parallel conductors separated by one meter.</i></figcaption>
</figure>

Historically, the definition of electric current has been fundamental to the SI system of units. Before the 2019 SI redefinition, the ampere was defined operationally through the magnetic force between parallel conductors.

**Classical Definition (Pre-2019):**

"The ampere is that constant current which, if maintained in two straight parallel conductors of infinite length and negligible circular cross-section, placed one metre apart in vacuum, would produce between these conductors a force equal to $2 \times 10^{-7}$ newton per metre of length."

**Mathematical Basis:**

From the force formula with $d = 1 \, \text{m}$, $I_1 = I_2 = 1 \, \text{A}$:

$$
\frac{F}{L} = \frac{\mu_0 \times 1 \times 1}{2\pi \times 1} = \frac{\mu_0}{2\pi} = \frac{4\pi \times 10^{-7}}{2\pi} = 2 \times 10^{-7} \, \text{N/m}
$$

This elegant relationship directly connects the definition of current to measurable electromagnetic forces, making it experimentally verifiable.

**Modern Definition (2019 Onward):**

The SI redefined the ampere in terms of elementary charge: "The ampere is the electric current corresponding to the flow of 1/(1.602176634 × 10⁻¹⁹) elementary charges per second." This definition, based on quantum physics rather than macroscopic forces, provides greater precision and universal applicability.

**Why This Matters:**

The force-based definition demonstrates that electric current fundamentally relates to magnetic phenomena. The new definition preserves this relationship while providing numerical stability through fixed physical constants.

### 4.7.3 Applications in Electrical Engineering and Measurement

**Power Transmission Line Design:**

Long-distance power transmission lines carry thousands of amperes. During normal operation, parallel transmission lines running near each other experience mutual forces. These forces must be considered in tower design to prevent mechanical failure. Paradoxically, during three-phase AC operation (where currents in different phases differ in time), the net force averages to zero if lines are symmetrically arranged, minimizing mechanical stress.

**Current Measurement - Current Balance Methods:**

The precise force relationship enables indirect current measurement. By measuring the magnetic force between conductors carrying known and unknown currents over a known distance, the unknown current can be determined. This principle underlies various electromagnetic instruments used before digital ammeters became prevalent.

**Magnetic Force in Motors and Actuators:**

Electric motors exploit forces between parallel current paths. Conductors on opposite sides of a motor coil carry currents in opposite directions, experiencing repulsive forces that create torque. The magnitude of this torque directly relates to the mutual force between these antiparallel currents.

**Electromagnetic Rail Guns (Research Applications):**

Rail guns accelerate projectiles using the magnetic force between parallel current paths. Two parallel conducting rails separated by distance $d$ carry enormous currents ($I$ in tens of thousands of amperes) through a projectile (armature) resting across them. The resulting repulsive force can accelerate projectiles to hypersonic speeds (exceeding 2 km/s) in laboratory experiments.

**Fusion Reactor Plasma Control:**

In plasma physics, conducting plasma channels experience forces similar to parallel current conductors. Understanding these forces is crucial for plasma stability in tokamak fusion reactors, where 20 million ampere-equivalent plasma currents can produce forces strong enough to damage reactor structures if not carefully controlled through magnetic field shaping.

**Superconductor Stability:**

Superconducting coils used in magnets experience mechanical stress from mutual forces between current paths. Proper mechanical support structures must be designed accounting for these electromagnetic forces to prevent coil damage during cool-down or fault conditions.

---

## 4.8 Cyclotron

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/N8zZuvH.png" alt="Cyclotron Device Diagram" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.8:</b> Schematic diagram of a cyclotron showing the two D-shaped dees, the accelerating gap, the magnetic field region, and the particle extraction mechanism.</i></figcaption>
</figure>

The cyclotron, invented by American physicist Ernest O. Lawrence in 1930, revolutionized nuclear and particle physics by enabling acceleration of charged particles to high energies in a compact device. Lawrence's innovation earned him the Nobel Prize in Physics in 1939, recognizing the profound impact cyclotrons had on scientific research. The key insight was exploiting the velocity-independent cyclotron frequency—the period of revolution remains constant regardless of particle speed, allowing the same accelerating gap to be used repeatedly. This elegant principle transformed particle acceleration from a challenging engineering problem into a practical laboratory instrument.

The cyclotron operates on the principle that a charged particle moving perpendicular to a magnetic field experiences a Lorentz force causing circular motion, while an appropriately timed oscillating electric field repeatedly accelerates the particle. With each acceleration, the particle gains kinetic energy and its circular path expands to a larger radius, creating a spiral trajectory. Eventually, when the radius reaches the cyclotron's boundary, the particle exits with high energy—often in the MeV range (millions of electron volts). Modern medical cyclotrons produce radioisotopes for positron emission tomography (PET) scans and deliver proton beams for cancer therapy, while research cyclotrons explore nuclear structure and particle interactions.

In this section, we examine the principle underlying cyclotron operation, describe its construction in detail, derive the cyclotron frequency, analyze energy gain and limitations, and explore applications ranging from medical isotope production to fundamental nuclear research. We'll understand why relativistic effects ultimately limit cyclotron energy and how this limitation led to the development of more advanced accelerators.

### 4.8.1 Principle and Basic Concept

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/cyclotron-principle.png" alt="Cyclotron Operation Principle" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.8.1:</b> The cyclotron principle: velocity-independent cyclotron frequency allows synchronization of oscillating electric field with particle motion regardless of energy.</i></figcaption>
</figure>

The fundamental principle of the cyclotron rests on a remarkable property of charged particle motion in magnetic fields: **the period of revolution is independent of the particle's speed and radius**. This property enables a single radiofrequency oscillator to continuously accelerate particles without requiring frequency adjustment as they gain energy.

When a charged particle moves perpendicular to a uniform magnetic field, it follows a circular path with radius and period determined by:

$$
r = \frac{m v}{q B}
$$

$$
T = \frac{2\pi m}{q B}
$$

Notice that the period $T$ depends only on the particle's charge-to-mass ratio $(q/m)$, the magnetic field strength $B$, and fundamental constants—it is **completely independent** of velocity $v$ and radius $r$.

**The Cyclotron Frequency:**

The frequency at which the particle completes one revolution is:

$$
f_c = \frac{1}{T} = \frac{q B}{2\pi m}
$$

where:
- $f_c$ = cyclotron frequency (Hertz, Hz)
- $q$ = charge of particle (Coulombs, C)
- $B$ = magnetic field strength (Tesla, T)
- $m$ = mass of particle (kilograms, kg)

This frequency is called the **Larmor frequency** or **cyclotron frequency** and remains constant as the particle gains energy and spirals outward. By matching an oscillating electric field to this frequency, the particle encounters an accelerating electric field each time it crosses the gap, regardless of its current energy.

**Conceptual Understanding: The Perfectly Timed Dance**

Imagine a dancer performing a spiral pattern on a stage, starting close to center and spiraling outward. A coach stands at one edge, and each time the dancer passes nearby, the coach gives them a push (acceleration). If the coach times pushes to match the dancer's orbital frequency (independent of spiral radius), the dancer accelerates efficiently. Similarly, a cyclotron's oscillating electric field "pushes" particles at the cyclotron frequency, maintaining synchronization even as particles spiral outward and gain energy.

**Mathematical Example:**

**Problem:** A proton cyclotron operates with a magnetic field of $B = 1.5 \, \text{T}$. Calculate the cyclotron frequency.

**Given:**
- Magnetic field: $B = 1.5 \, \text{T}$
- Proton charge: $q = 1.6 \times 10^{-19} \, \text{C}$
- Proton mass: $m = 1.67 \times 10^{-27} \, \text{kg}$

**To Find:** Cyclotron frequency $f_c$

**Solution:**

Step 1: Apply the cyclotron frequency formula:

$$
f_c = \frac{q B}{2\pi m}
$$

Step 2: Substitute values:

$$
f_c = \frac{(1.6 \times 10^{-19}) \times 1.5}{2\pi \times (1.67 \times 10^{-27})}
$$

Step 3: Calculate numerator and denominator:

$$
f_c = \frac{2.4 \times 10^{-19}}{1.05 \times 10^{-26}} = 2.29 \times 10^{7} \, \text{Hz} = 22.9 \, \text{MHz}
$$

**Answer:** The proton cyclotron frequency is **22.9 MHz** (megahertz). The radiofrequency oscillator must operate at this frequency to keep protons synchronized with the accelerating electric field.

### 4.8.2 Construction and Working

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/cyclotron-construction.png" alt="Cyclotron Construction Details" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.8.2:</b> Cross-sectional view of cyclotron construction showing D1, D2, gap, ion source, magnetic field region, and extraction magnet.</i></figcaption>
</figure>

The cyclotron consists of several essential components, each playing a critical role in particle acceleration:

**Main Components:**

**D-Shaped Dees (Dees):** Two hollow, semi-cylindrical metal containers, typically made of copper or aluminum, called "dees" because of their D-shaped profile when viewed from above. The two dees (D₁ and D₂) face each other across a narrow gap of a few centimeters. Inside each dee, particles are shielded from the electric field—the magnetic field maintains their circular motion. The dees are electrically connected to an RF oscillator that alternates their polarity at the cyclotron frequency.

**Vacuum Chamber:** The entire apparatus sits in a vacuum chamber (pressure typically 10⁻⁶ torr or lower) to prevent particles from colliding with gas molecules, which would scatter them from their intended paths.

**Magnetic Field Region:** A strong uniform magnetic field, typically 1-2 Tesla for medical cyclotrons and up to 5-8 Tesla for research machines, is applied perpendicular to the plane of the dees using large electromagnets or permanent magnets. Modern superconducting cyclotrons achieve fields exceeding 10 Tesla.

**Ion Source:** Located at the center between the two dees, the ion source produces a thin beam of charged particles (protons, deuterons, or heavier ions). In medical cyclotrons, protons are typically produced by accelerating hydrogen ions.

**Radiofrequency (RF) Oscillator:** An RF generator produces an alternating voltage at the cyclotron frequency, applied between the dees. Modern cyclotrons use frequencies between 10-100 MHz, with voltages typically 10,000-50,000 volts.

**Extraction System:** When particles reach the edge of the dees (after many accelerations), a weak deflecting magnetic field nudges them out of the cyclotron orbit and onto the target or beamline.

**Step-by-Step Working Principle:**

**Initial Acceleration:** A positively charged particle (e.g., proton) starts at rest in the center near the ion source. When D₂ is positive and D₁ is negative, the proton is accelerated across the gap, gaining energy $\Delta KE = qV_{\text{gap}}$.

**First Revolution:** The proton enters D₁ (now positive, shielding it from the electric field) and moves in a semicircle due to the magnetic force, with radius $r_1 = \frac{mv_1}{qB}$.

**Repeated Acceleration:** By the time the proton exits D₁ and re-enters the gap, the RF oscillator has reversed polarity—D₁ is now positive and D₂ is negative. The proton again accelerates, gaining another $\Delta KE = qV_{\text{gap}}$ and entering D₂ with higher velocity.

**Spiral Motion:** With each crossing of the accelerating gap, the proton gains energy and follows a semicircular path of slightly larger radius. After hundreds of orbits, the spiral radius grows from millimeters (near center) to tens of centimeters (near exit).

**Extraction:** When the proton's orbit radius reaches the cyclotron boundary (determined by dee radius), an extraction magnet deflects it out of the orbit onto a target or into a beamline.

**Conceptual Understanding: The Accelerating Spiral**

Picture a spiraling ramp in a parking garage. A car starts at the center with low speed, accelerating at each ramp turn. As it gains speed, it moves to higher spiral levels. After many turns, it exits at the top with high speed. A cyclotron works similarly—particles spiral outward, getting pushed at each gap crossing, until they exit the outer edge with high energy.

**Important Notes:**

- **Isochronism:** The time to complete each semicircle remains constant ($T/2 = \frac{\pi m}{qB}$), even though the path length increases. This is the enabling principle of the cyclotron.

- **Synchronization Requirement:** The RF frequency must precisely match the cyclotron frequency. If even slightly mismatched, particles gradually slip out of phase and stop accelerating efficiently.

- **Vacuum Requirement:** The vacuum prevents collisions that would scatter particles. Even one gas collision can deflect a particle off its designed spiral path.

### 4.8.3 Cyclotron Frequency Derivation

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/cyclotron-frequency-derivation.png" alt="Cyclotron Frequency Derivation" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.8.3:</b> Geometric derivation of cyclotron frequency from circular motion in magnetic field.</i></figcaption>
</figure>

The cyclotron frequency emerges naturally from the physics of circular motion in magnetic fields:

**Step 1: Centripetal Force Balance**

A particle moving perpendicular to a magnetic field experiences perpendicular magnetic force that acts as centripetal force:

$$
F_{\text{magnetic}} = F_{\text{centripetal}}
$$

$$
q v B = \frac{m v^2}{r}
$$

**Step 2: Solve for Radius**

$$
r = \frac{m v}{q B}
$$

**Step 3: Relate Radius to Period**

For circular motion, the particle travels distance $2\pi r$ in time period $T$:

$$
v = \frac{2\pi r}{T}
$$

**Step 4: Substitute Radius Expression**

$$
v = \frac{2\pi}{T} \times \frac{m v}{q B}
$$

**Step 5: Cancel Velocity**

Dividing both sides by $v$:

$$
1 = \frac{2\pi m}{T q B}
$$

**Step 6: Solve for Period**

$$
T = \frac{2\pi m}{q B}
$$

**Step 7: Express as Frequency**

$$
f = \frac{1}{T} = \frac{q B}{2\pi m}
$$

**Physical Insight:** The derivation reveals why frequency is independent of velocity—$v$ cancels out completely! This cancellation occurs because both the radius and speed increase proportionally with energy, preserving the revolution time.

### 4.8.4 Maximum Energy and Limitations

<figure style="display: flex; flex-direction: column; align-items: center;">
<img src="https://i.imgur.com/cyclotron-limitations.png" alt="Cyclotron Limitations" style="max-width: 90%; height: auto;">
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 4.8.4:</b> Maximum particle energy is limited by dee radius and relativistic mass increase.</i></figcaption>
</figure>

The maximum energy a cyclotron can impart depends on two factors: the physical size of the dees and relativistic effects:

**Maximum Energy from Dee Radius:**

When the particle's orbit expands to the dee radius $R_{\text{dee}}$, it must exit. Using $r = \frac{mv}{qB} = R_{\text{dee}}$:

$$
v_{\text{max}} = \frac{q B R_{\text{dee}}}{m}
$$

The maximum kinetic energy is:

$$
K.E._{\max} = \frac{1}{2} m v_{\max}^2 = \frac{1}{2} m \left(\frac{q B R_{\text{dee}}}{m}\right)^2
$$

$$
K.E._{\max} = \frac{q^2 B^2 R_{\text{dee}}^2}{2m}
$$

where:
- $q$ = particle charge (Coulombs, C)
- $B$ = magnetic field strength (Tesla, T)
- $R_{\text{dee}}$ = radius of cyclotron dees (meters, m)
- $m$ = particle mass (kilograms, kg)

**Relativistic Limitations - The Fundamental Problem:**

At very high energies, particles approach the speed of light and relativistic effects become important. The particle's relativistic mass increases:

$$
m_{\text{rel}} = \frac{m_0}{\sqrt{1 - v^2/c^2}} = \gamma m_0
$$

where $\gamma$ is the Lorentz factor and increases dramatically as $v \to c$.

The problem: the cyclotron frequency depends on rest mass $m_0$:

$$
f = \frac{q B}{2\pi m}
$$

When relativistic mass is used, this becomes:

$$
f_{\text{rel}} = \frac{q B}{2\pi \gamma m_0}
$$

The frequency **decreases** as particles gain energy! This means the oscillating electric field falls out of synchronization—it oscillates faster than the relativistic particles revolve. Particles gradually slip out of phase, arriving at the gap at the wrong time (when the field accelerates in the wrong direction), and stop gaining energy.

**Practical Energy Limits:**

- **Light particles (electrons):** Relativistic effects begin at energies around 1-2 MeV
- **Protons:** Classical cyclotrons reach ~30 MeV before synchronization loss becomes severe
- **Heavier ions:** Correspondingly higher energies possible before relativistic effects dominate

**Solutions to Overcome Limitations:**

**Synchrocyclotron:** Varies the RF frequency as particles gain energy to maintain synchronization. However, this requires accelerating bunches sequentially, reducing beam intensity.

**Synchrotron:** Uses a different approach—the magnetic field strength increases with particle energy to maintain constant orbit radius. The particle orbits in a fixed ring, eliminating the spiral motion limitation.

**Fixed-Field Alternating Gradient (FFAG) Accelerators:** Use specially designed magnetic field patterns to maintain synchronization without frequency modulation or field increase, achieving high intensity and high energy.

**Mathematical Example:**

**Problem:** Calculate the maximum kinetic energy of protons in a cyclotron with dee radius $R = 0.6 \, \text{m}$ and magnetic field $B = 1.5 \, \text{T}$.

**Given:**
- Dee radius: $R_{\text{dee}} = 0.6 \, \text{m}$
- Magnetic field: $B = 1.5 \, \text{T}$
- Proton charge: $q = 1.6 \times 10^{-19} \, \text{C}$
- Proton mass: $m = 1.67 \times 10^{-27} \, \text{kg}$

**To Find:** Maximum kinetic energy $K.E._{\max}$

**Solution:**

Step 1: Apply maximum energy formula:

$$
K.E._{\max} = \frac{q^2 B^2 R_{\text{dee}}^2}{2m}
$$

Step 2: Calculate $q^2 B^2 R^2$:

$$
q^2 B^2 R^2 = (1.6 \times 10^{-19})^2 \times (1.5)^2 \times (0.6)^2
$$

$$
= 2.56 \times 10^{-38} \times 2.25 \times 0.36 = 2.07 \times 10^{-38}
$$

Step 3: Divide by $2m$:

$$
K.E._{\max} = \frac{2.07 \times 10^{-38}}{2 \times 1.67 \times 10^{-27}} = \frac{2.07 \times 10^{-38}}{3.34 \times 10^{-27}}
$$

$$
= 6.2 \times 10^{-12} \, \text{J}
$$

Step 4: Convert to electron volts (1 eV = 1.6 × 10⁻¹⁹ J):

$$
K.E._{\max} = \frac{6.2 \times 10^{-12}}{1.6 \times 10^{-19}} = 3.9 \times 10^{7} \, \text{eV} = 39 \, \text{MeV}
$$

**Answer:** The maximum proton kinetic energy is approximately **39 MeV** (megaelectron volts), typical for medical cyclotrons before relativistic effects become severe.

### 4.8.5 Applications of Cyclotron

**Medical Isotope Production:**

Modern medical cyclotrons produce radioisotopes for positron emission tomography (PET) scanning. For example, a cyclotron bombards a nitrogen target with protons to produce fluorine-18, which attaches to glucose molecules (FDG). Patients receive FDG injections, and the positrons emitted during decay are detected to create detailed metabolic images of tumors and brain disorders. Medical cyclotrons operate at 10-25 MeV, producing radioisotopes with 110-minute half-lives, requiring rapid transport to hospitals.

**Proton Beam Therapy:**

Cyclotrons accelerate protons to 50-250 MeV for cancer radiotherapy. Proton beams deposit most of their energy at a specific depth (the Bragg peak), minimizing damage to healthy tissue before or behind the tumor. This enables treatment of tumors near critical structures—eye cancers, brain tumors, pediatric cancers—with significantly reduced side effects compared to X-ray therapy.

**Nuclear and Particle Physics Research:**

Research cyclotrons and synchrocyclotrons accelerate various ions (protons, deuterons, helium nuclei, heavier ions) to study nuclear structure, cross sections for nuclear reactions, and fundamental interactions. CERN's cyclotrons contributed to early particle physics discoveries before being superseded by larger accelerators.

**Neutron Production:**

Cyclotron-accelerated protons striking targets produce neutrons via nuclear reactions. These neutrons are used for neutron activation analysis (determining elemental composition of materials), neutron therapy, and creating intense neutron beams for materials science research.

**Industrial Applications:**

- **Sterilization:** Electron beams from cyclotrons sterilize medical equipment and pharmaceuticals
- **Materials modification:** Ion beams modify semiconductor properties and create specialized materials
- **Activation analysis:** Neutrons from cyclotrons enable non-destructive chemical analysis

**Radioisotope Tracer Production:**

Beyond PET isotopes, cyclotrons produce many tracers used in nuclear medicine: technetium-99m for bone scans, iodine-123 for thyroid studies, and numerous other diagnostic radioisotopes essential to modern healthcare.

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