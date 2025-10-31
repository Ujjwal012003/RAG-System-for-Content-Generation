# Chapter 3: Current_Electricity

## 3.1 Introduction

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1AFQWm8raCtgBUVZHL-SrD3oM0FMKF9pq" alt="Illustration showing flow of electric charges as current, with arrows indicating conventional current direction and electron flow opposite it." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.1:</b> The flow of electric charge (electric current). The conventional current direction is from positive to negative, while electron flow is opposite.</i></figcaption>  
</figure>

Electric current is a foundational element in the study of electricity and forms the basis for all electrical and electronic devices. It is defined as the flow of electric charge through a conductor or any medium. Understanding electric current allows us to explore how electrical energy is transmitted and harnessed to perform work. This chapter provides a comprehensive examination of current electricity, starting from the microscopic origin of current due to charge movement and progressing towards practical aspects relevant for circuit analysis and device applications.

In metallic conductors such as copper or aluminum, the free electrons within the atomic lattice are the primary charge carriers responsible for current. These electrons move chaotically due to thermal energy, but when an external electric field is applied—such as by connecting a battery—a small average velocity called the drift velocity is established. Although slow compared to thermal speeds (drift velocity is typically in the order of millimeters or fractions of millimeters per second), this net movement of electrons constitutes a steady flow of charge that we call electric current.

The direction of electric current is defined conventionally as the direction positive charges would flow, which is opposite to the electrons’ actual movement in metals. This convention simplifies circuit analysis and is universally adopted in physics and engineering.

A critical parameter that describes electric current quantitatively is the current density, denoted by $\vec{J}$. Current density represents the current flowing per unit cross-sectional area of the conductor. It is a vector quantity pointing in the direction of positive charge flow. Understanding current density aids in analyzing current flow in complex conductor geometries and varying materials.

Mathematically, the electric current $I$ is expressed as

$$
I = \frac{q}{t}
$$

where $q$ is the charge flowing through a cross section in time $t$, with units of amperes (A), where 1 A = 1 coulomb/second.

Besides metallic conduction, current can also flow through electrolytes, where conduction happens due to movement of ions. This distinction expands the scope and applicability of current electricity in electrochemistry and industrial processes.

Applications of electric current permeate virtually every facet of modern life, powering everything from household lighting, electronic devices, and motors, to industrial machinery and power grids. Laboratory experiments involving measurement of current using ammeters and exploration of its properties form an essential part of physics education.

---

**Example 3.1:** (Conceptual) Understanding Current Flow in a Copper Wire  
A copper wire is connected to a battery, and the circuit is closed. Electrons in the wire begin to move under the influence of the battery's electric field. Although electrons move randomly at high speeds due to thermal energy, the battery-induced electric field causes them to acquire a small drift velocity towards the positive terminal. This tiny but uniform drift produces a net current that powers electrical devices. The current’s magnitude depends on charge carrier density, drift velocity, and cross-sectional area of the wire.

**Example 3.2:** (Conceptual) Difference Between Electron Flow and Conventional Current  
In circuits, conventional current is defined as flowing from the positive terminal to the negative terminal, whereas electrons physically flow in the opposite direction—from negative to positive. This historic convention facilitates consistent circuit analysis despite being opposite to actual electron motion. The bulb in a circuit lights up because electrons transfer energy to atoms of the filament as they flow, regardless of current direction convention.

---

### Applications

The concepts in this section are fundamental to electrical wiring, electronics design, and energy distribution systems. Knowledge of current flow and its microscopic basis helps in understanding circuit functioning, device behavior, and safety considerations such as current ratings of wires to prevent overheating.

---

### Physical Interpretation

Electric current captures the essence of electricity as dynamic flow of charges, moving beyond static electrostatics. The unusual but essential notion that current flows opposite electron motion arises from the sign conventions established historically. Drift velocity reconciles the presence of high-speed random electron motion with the relatively slow, orderly flow of electric current observed macroscopically.

---

## 3.2 Electric Current and Drift Velocity

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1omFgpTDqn4aolaiH6pRQDq1uu0-54i_s" alt="Diagram showing free electrons drifting through a metallic conductor under influence of electric field with average drift velocity opposite to field." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.2:</b> Electrons drifting through a metallic conductor under the influence of an electric field, showing average drift velocity opposite to the field direction.</i></figcaption>  
</figure>

Electric current $ I $ is the amount of charge $ q $ flowing through a conductor’s cross-section per unit time $ t $:

$$
I = \frac{q}{t}
$$

The standard unit is the ampere (A), where 1 ampere equals 1 coulomb of charge passing in 1 second.

In a metallic conductor, free electrons act as the charge carriers. Without an applied electric field, these electrons move randomly with very high thermal velocities (~10⁶ m/s) in all directions, resulting in no net charge flow. When an electric field is applied (for example, by connecting a battery), electrons experience an acceleration against the field and acquire a small average velocity called drift velocity $ v_d $, oriented opposite the field vector because electrons are negatively charged.

Considering a conductor of cross-sectional area $ A $, carrying current $ I $, and containing number density $ n $ of free electrons (number of electrons per unit volume), the drift velocity is derived from the relation:

$$
I = n e A v_d
$$

Rearranging,

$$
v_d = \frac{I}{n e A}
$$

where:  
- $ n $ ≈ $ 8.5 \times 10^{28} \, \text{electrons/m}^3 $ for copper  
- $ e = 1.6 \times 10^{-19} \, \text{C} $ (electronic charge)  
- $ A $ is cross-sectional area in $ m^2 $  
- $ I $ is current in amperes

Drift velocity is typically very small (on the order of $ 10^{-4} $ m/s), illustrating that although microscopic electrons move rapidly and randomly, their net directed velocity is modest and sufficient to produce steady current.

This microscopic understanding helps explain how electric signals propagate quickly (due to the electric field’s influence propagating at nearly the speed of light), even though electron drift is slow.

---

**Example 3.3:** Calculate the drift velocity of electrons in a copper wire of diameter 1 mm carrying a current of 3 A. Given $ n = 8.5 \times 10^{28} \, \text{m}^{-3} $.

*Solution:*  
Calculate area,

$$
A = \pi \left( \frac{d}{2} \right)^2 = \pi (0.5 \times 10^{-3})^2 = 7.85 \times 10^{-7} \, m^2
$$

Calculate drift velocity,

$$
v_d = \frac{I}{n e A} = \frac{3}{8.5 \times 10^{28} \times 1.6 \times 10^{-19} \times 7.85 \times 10^{-7}} \approx 2.8 \times 10^{-4} \, m/s
$$

Interpretation: Despite electron random motion at very high speeds, the net average velocity contributing to current is very small.

---

### Applications

Knowing drift velocity helps engineers design conductors with appropriate cross-section and material composition to handle expected current loads without overheating or failure.

---

### Physical Interpretation

The concept illustrates the link between macroscopic current and microscopic charge carrier movement, providing insight into conduction mechanisms and influencing material selection for electrical components.

---

## 3.3 Current Density

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1pOsC0vkHvGBIqMAthJfnezjMdN0iDvwT" alt="Vector representation of current density flowing through the cross-section of a conductor." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.3:</b> Current density (J) represented as a vector. It measures current per unit cross-sectional area.</i></figcaption>  
</figure>

Current density $ \vec{J} $ is defined as current $ I $ flowing per unit cross-sectional area $ A $ of a conductor, normal to the flow:

$$
J = \frac{I}{A}
$$

and as a vector:

$$
\vec{J} = J \hat{n}
$$

where $ \hat{n} $ is a unit vector in the direction of positive charge flow.

The SI unit of current density is ampere per square meter (A/m²).

In materials, current density relates directly to the electric field $ \vec{E} $ and conductivity $ \sigma $ by:

$$
\vec{J} = \sigma \vec{E}
$$

Here, conductivity $ \sigma $ has units $ S/m $ (siemens per meter). This expression is a microscopic form of Ohm’s law stating that current density is proportional to the applied electric field. This relation is linear for ohmic materials.

The inverse of conductivity is resistivity $ \rho $:

$$
\rho = \frac{1}{\sigma}
$$

essential for characterizing material properties.

---

**Example 3.4:** A wire of cross-sectional area $ 2 \times 10^{-6} \, m^2 $ carries a current of 4 A. Calculate the magnitude of the current density.

*Solution:*  
Using,

$$
J = \frac{I}{A} = \frac{4}{2 \times 10^{-6}} = 2 \times 10^{6} \, A/m^2
$$

---

### Applications

Current density is crucial in designing electrical wiring, electronics, and power cables, as excessive current density leads to heating and damage. It also aids in analyzing nonuniform current flow in complex conductor shapes.

---

### Physical Interpretation

Current density concept bridges microscopic charge carrier behavior to macroscopic observable current and guides material engineering to optimize conduction and thermal management.

---

## 3.4 Ohm’s Law and Electrical Resistance

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/15Y8mSsEpcnAyxFuWHxLxEQLHsHR9pRk4" alt="Graph showing linear relation between voltage and current, illustrating Ohm's law." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.4:</b> Voltage vs. Current graph demonstrating linear behavior consistent with Ohm’s law for an ohmic conductor.</i></figcaption>  
</figure>

Ohm’s law is a fundamental empirical relationship in current electricity, established by Georg Simon Ohm. It states that, for ohmic conductors, the voltage $ V $ across a conductor is directly proportional to the current $ I $ flowing through:

$$
V = IR
$$

where $ R $ is the resistance measured in ohms (Ω).

Resistance quantifies the opposition a material offers to the flow of electric current.

Resistance depends on the conductor’s geometry and nature of the material:

$$
R = \rho \frac{l}{A}
$$

where  
- $ \rho $ is resistivity of the material (Ω·m), an intrinsic property  
- $ l $ is length of the conductor (m)  
- $ A $ is cross-sectional area (m²)

Typical resistivity values are:  
- Copper: $ 1.68 \times 10^{-8} \, \Omega m $ (a good conductor)  
- Rubber: $ 10^{13} \, \Omega m $ (an insulator)

Ohm’s law is obeyed strictly by ohmic materials — metals at constant temperature. Certain materials and components (e.g., diodes, semiconductors) show nonlinear voltage-current characteristics.

---

**Example 3.5:** Calculate the resistance of a copper wire of length 2 m and diameter 0.5 mm. Resistivity of copper is $1.68 \times 10^{-8} \, \Omega m$.

*Solution:*  
Calculate cross-sectional area,

$$
A = \pi \left( \frac{d}{2} \right)^2 = \pi (0.25 \times 10^{-3})^2 = 1.96 \times 10^{-7} \, m^2
$$

Calculate resistance,

$$
R = \rho \frac{l}{A} = \frac{1.68 \times 10^{-8} \times 2}{1.96 \times 10^{-7}} = 0.171 \, \Omega
$$

---

### Applications

Ohm’s law forms the basis of circuit analysis, allowing calculation of voltages, currents, and resistances in electrical networks. It enables the design of resistors and selection of materials for wiring and devices.

---

### Physical Interpretation

Resistance arises due to collisions of moving electrons with atoms in the material lattice, dissipating electrical energy as heat and impeding current flow.

---

## 3.5 Temperature Dependence of Resistance

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1ok2dFaPbEV4L5nE_BVVmxUna_AhIN8-G" alt="Graph showing linear increase of resistance with temperature in metals." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.5:</b> Typical linear increase of resistance of metals with temperature.</i></figcaption>  
</figure>

The resistance of most conductors changes with temperature. For metals, resistance increases approximately linearly with temperature over ordinary temperature ranges:

$$
R_T = R_0 (1 + \alpha \Delta T)
$$

where,  
- $ R_T $ = resistance at temperature $ T $ (Ω)  
- $ R_0 $ = resistance at reference temperature (usually 20°C) (Ω)  
- $ \alpha $ = temperature coefficient of resistivity (per °C)  
- $ \Delta T = T - T_0 $ is temperature change (°C)

The parameter $ \alpha $ is positive for metals, typically around $ 0.004 , \text{per} ,  ^\circ \mathrm{C} $ for copper.

Semiconductors and insulators show different temperature behavior, but this is beyond current scope.

---

**Example 3.6:** The resistance of a copper wire at 20°C is 10 Ω. Calculate its resistance at 70°C. The temperature coefficient for copper is $ 0.004 \ \text{per} \ ^\circ C $.

*Solution:*  
Calculate temperature change $ \Delta T = 70 - 20 = 50^\circ C $,

Calculate resistance,

$$
R_{70} = 10 \times (1 + 0.004 \times 50) = 10 \times 1.2 = 12 \, \Omega
$$

---

### Applications

This temperature dependence is crucial for design and safety in electrical equipment. Resistance increases cause more heat, influencing material choice and current limits.

---

### Physical Interpretation

Increased lattice vibrations at higher temperatures cause more frequent electron collisions, increasing resistivity and resistance.

---

## 3.6 Combination of Resistors

### 3.6.1 Series Combination

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1gLNESD9Yo359ttzbyzl8yTjQfkWfUR56" alt="Three resistors connected in series with same current and voltage drops shown." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.1:</b> Resistors connected in series have the same current flowing through each. Equivalent resistance is sum of individual resistances.</i></figcaption>  
</figure>

In a series connection, resistors are connected end to end, so the same current $ I $ flows through each resistor. The total potential difference $ V $ across the series combination is the sum of voltage drops across individual resistors:

$$
V = V_1 + V_2 + \ldots = I(R_1 + R_2 + \ldots)
$$

The equivalent resistance is given by:

$$
R_{eq} = R_1 + R_2 + \ldots
$$

This additive nature makes series connections useful in achieving large resistance values.

---

### 3.6.2 Parallel Combination

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/14Oipq16rZ9JKfiY-xNw1xlku1SevgCpI" alt="Three resistors connected in parallel, voltage same across each; currents divide." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.6.2:</b> Resistors connected in parallel have the same voltage across each with total current as sum of branch currents.</i></figcaption>  
</figure>

In parallel, resistors are connected across the same voltage source, so voltage $ V $ across each resistor is identical. The total current $ I $ supplied divides among branches:

$$
I = I_1 + I_2 + \ldots
$$

Ohm’s law for each branch:

$$
I_i = \frac{V}{R_i}
$$

Equivalent resistance $ R_{eq} $ satisfies:

$$
\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \ldots
$$

The equivalent resistance is always less than the smallest individual resistance in the combination.

---

**Example 3.7:** Find equivalent resistance for resistors $ R_1 = 4 \, \Omega $ and $ R_2 = 6 \, \Omega $ connected in series and parallel.

*Solution:*  
Series,

$$
R_{series} = 4 + 6 = 10 \, \Omega
$$

Parallel,

$$
\frac{1}{R_{parallel}} = \frac{1}{4} + \frac{1}{6} = \frac{3}{12} + \frac{2}{12} = \frac{5}{12}
$$

So,

$$
R_{parallel} = \frac{12}{5} = 2.4 \, \Omega
$$

---

### Applications

Series and parallel resistor combinations form the building blocks of electrical circuit design, enabling precise control of resistance, current, and voltage distribution.

**Series Combinations:**

- **Voltage Dividers:** Creating specific voltage levels for biasing transistors and reference circuits. For example, two equal resistors in series across 12V provide 6V at the midpoint.

- **Current Limiting:** Protecting sensitive components like LEDs where a series resistor limits current to safe operating levels.

- **Custom Resistance Values:** Combining standard resistor values to achieve precise non-standard values (e.g., 47Ω + 33Ω = 80Ω).

**Parallel Combinations:**

- **Current Distribution:** Dividing load current among multiple paths for high-power applications, preventing overheating by sharing power dissipation.

- **House Wiring:** All electrical outlets and appliances connect in parallel, ensuring each device receives full voltage and operates independently.

- **Redundancy:** If one parallel path fails open, current continues through remaining paths, maintaining circuit operation.

- **Battery Banks:** Parallel batteries increase total current capacity while maintaining voltage, essential for high-current applications like electric vehicles.

Understanding these combinations enables effective circuit analysis and design for applications ranging from simple voltage dividers to complex electronic systems.

---

## 3.7 Cells, EMF and Internal Resistance

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1V6UyoWR5qeE0LbTicGp60a4ut9f-R2vN" alt="Symbolic representation of cell with EMF and internal resistance connected to external circuit." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.7:</b>Representation of cell with EMF and internal resistance connected to external circuit.</i></figcaption>  
</figure>


A cell or battery provides electrical energy through a chemical reaction, producing an electromotive force (EMF) $ \varepsilon $, measured in volts.

A real cell has internal resistance $ r $, which causes voltage drop inside the cell when current flows.

The terminal voltage $ V $ is given by:

$$
V = \varepsilon - Ir
$$

When current $ I $ drawn increases, terminal voltage decreases due to the internal resistance voltage drop.

---

**Example 3.8:** A cell of EMF 12 V and internal resistance 1 Ω is connected to a resistor of 5 Ω. Find the current in the circuit and terminal voltage.

*Solution:*  
Equivalent resistance,

$$
R_{total} = R + r = 5 + 1 = 6 \, \Omega
$$

Current,

$$
I = \frac{\varepsilon}{R_{total}} = \frac{12}{6} = 2 \, A
$$

Terminal voltage,

$$
V = \varepsilon - Ir = 12 - 2 \times 1 = 10 \, V
$$

---

### Applications

Understanding internal resistance is key to battery performance evaluation and efficiency in power delivery.

---

## 3.8 Kirchhoff's Laws

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1xCE_odag3O0htX1JgSmUhOq1z2lRgMxb" alt="Complex circuit illustrating Kirchhoff's junction and loop laws for current and voltage." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.8:</b> Application of Kirchhoff's junction and loop rules in circuit analysis.</i></figcaption>  
</figure>

Kirchhoff's laws, formulated by German physicist Gustav Kirchhoff in 1845, are fundamental principles for analyzing complex electrical circuits. These two laws extend Ohm's law to networks containing multiple loops and junctions, enabling systematic calculation of currents and voltages where simple series-parallel analysis fails. The laws are based on conservation of charge (current law) and conservation of energy (voltage law), making them universally applicable to any electrical circuit regardless of complexity.

These laws form the mathematical foundation for circuit simulation software and are essential tools in electrical engineering. They allow analysis of circuits with multiple current paths, multiple voltage sources, and complex interconnections that cannot be simplified using series and parallel combinations alone.

### 3.8.1 Kirchhoff's Current Law (KCL)

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1dRd_hdnCP7gIASvHFDZXNup6ySjboP2s" alt="Kirchhoff's Current Law." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.8.1:</b> Kirchhoff's Current Law.</i></figcaption>  
</figure>

Kirchhoff's Current Law states that the algebraic sum of all currents entering a junction must equal the sum of currents leaving that junction. This law follows directly from conservation of electric charge.

$$
\sum I_{in} = \sum I_{out}
$$

Or equivalently:

$$
\sum_{i=1}^{n} I_i = 0
$$

where currents entering are positive and leaving are negative.

**Physical Meaning:** Since charge cannot accumulate at a junction in steady-state conditions, all charge flowing in must flow out. If 3 A enters through two wires, exactly 3 A must exit through other connected wires.

**Conceptual Example:**

Think of a water pipe junction where three pipes meet. If 5 liters/second flows in through one pipe and 2 liters/second through another, then 7 liters/second must flow out through the third pipe. Water doesn't accumulate at the junction—similarly, electric charge cannot accumulate at a circuit node.

**Mathematical Example:**

**Problem:** At a junction, currents $I_1 = 3 \, A$, $I_2 = 2 \, A$ enter, while $I_3 = 1.5 \, A$ and $I_4$ leave. Find $I_4$.

**Solution:**

$$
I_1 + I_2 = I_3 + I_4
$$

$$
3 + 2 = 1.5 + I_4
$$

$$
I_4 = 3.5 \, A
$$

---

### 3.8.2 Kirchhoff's Voltage Law (KVL)

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1FJk336cpeG-SUo8Y45lJTzaleweYibb9" alt="Kirchhoff's Voltage Law." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.8.2:</b> Kirchhoff's Voltage Law.</i></figcaption>  
</figure>

Kirchhoff's Voltage Law states that the algebraic sum of all potential differences around any closed loop equals zero. This follows from conservation of energy.

$$
\sum V = 0
$$

**Sign Convention:**
- Voltage rise (moving through source from − to +): Positive
- Voltage drop (current through resistor): Negative (−IR)

**Physical Meaning:** Traveling around a closed loop and returning to the starting point, the net potential change must be zero. Energy gained from sources equals energy lost in resistors.

**Conceptual Example:**

Walking around a hilly path that returns to your starting point—if you climb 50 m up and descend 30 m and 20 m down different slopes, your net elevation change is zero. Similarly, voltage changes around a closed circuit loop sum to zero.

**Mathematical Example:**

**Problem:** A 12 V battery connects in series with resistors $R_1 = 2 \, \Omega$, $R_2 = 3 \, \Omega$, $R_3 = 1 \, \Omega$. Find the current.

**Solution:**

Applying KVL clockwise:

$$
12 - IR_1 - IR_2 - IR_3 = 0
$$

$$
12 - I(2 + 3 + 1) = 0
$$

$$
I = 2 \, A
$$

**Verification:** Voltage drops = $4 + 6 + 2 = 12 \, V$ 

---

### 3.8.3 Applying Kirchhoff's Laws to Complex Circuits

For circuits with multiple loops and junctions, we apply both KCL and KVL systematically following a step-by-step procedure.

**Step-by-Step Procedure:**

1. **Identify all junctions and loops** in the circuit
2. **Assign current directions** to each branch (if direction is wrong, solution will be negative)
3. **Apply KCL at junctions** to relate branch currents (write $n-1$ equations for $n$ junctions)
4. **Identify independent loops** and choose traversal direction for each loop
5. **Apply KVL to each loop**, carefully noting voltage rises and drops according to sign convention
6. **Solve the system of linear equations** to find unknown currents or voltages

**Important Notes:**

- Number of independent equations must equal number of unknowns for a solvable system
- Independent loops are chosen such that each includes at least one branch not in previous loops
- Consistent sign conventions are critical for correct results
- If assumed current direction is wrong, the calculated value will be negative but magnitude correct

**Example 3.8:** **Complex Circuit Analysis**

**Problem:** In a circuit with two batteries ($V_1 = 10 \, V$ and $V_2 = 6 \, V$) connected with three resistors ($R_1 = 2 \, \Omega$, $R_2 = 3 \, \Omega$, $R_3 = 1 \, \Omega$), find the current through each branch.

**Solution Approach:**

**Step 1:** Label currents $I_1$, $I_2$, $I_3$ in the three branches.

**Step 2:** Apply KCL at junction A:

$$
I_1 = I_2 + I_3
$$

**Step 3:** Apply KVL to Loop 1 (containing $V_1$, $R_1$, $R_2$):

$$
V_1 - I_1 R_1 - I_2 R_2 = 0
$$

$$
10 - 2I_1 - 3I_2 = 0
$$

**Step 4:** Apply KVL to Loop 2 (containing $V_2$, $R_2$, $R_3$):

$$
V_2 - I_2 R_2 + I_3 R_3 = 0
$$

$$
6 - 3I_2 + I_3 = 0
$$

**Step 5:** Solve the system of three equations simultaneously:

From KCL: $I_1 = I_2 + I_3$

Substituting into Loop 1 equation and solving with Loop 2 equation yields the three currents.

*(Complete numerical solution involves substitution or matrix methods)*

---

## 3.9 Wheatstone Bridge

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1xCE_odag3O0htX1JgSmUhOq1z2lRgMxb" alt="Wheatstone bridge circuit with resistors and galvanometer connected for balance measurement." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.9:</b> Wheatstone bridge setup used to measure unknown resistance.</i></figcaption>  
</figure>

The Wheatstone bridge is a fundamental electrical circuit used to measure unknown resistance with high precision. Invented by Samuel Hunter Christie in 1833 and popularized by Sir Charles Wheatstone in 1843, this bridge circuit operates on the principle of null deflection, where the circuit is balanced such that no current flows through the galvanometer. This method eliminates the need for precise measurement of current or voltage, making it highly accurate for determining unknown resistances.

The bridge consists of four resistors arranged in a diamond configuration with a galvanometer connected across one diagonal and a battery across the other diagonal. Three resistors have known values ($R_1$, $R_2$, $R_3$), while the fourth is the unknown resistance ($R_4$ or $R_x$) to be determined. By adjusting the variable resistor until the galvanometer shows zero deflection, the bridge reaches balance, and the unknown resistance can be calculated using a simple ratio relationship.

The Wheatstone bridge is widely used in laboratories for accurate resistance measurements, in strain gauges for measuring mechanical deformation, in temperature sensors, and in various instrumentation applications where precision matters. Its simplicity, accuracy, and versatility have made it an indispensable tool in electrical measurements and sensor technology.

### 3.9.1 Principle and Balance Condition

The Wheatstone bridge operates on the **null deflection principle**. When the bridge is balanced, no current flows through the galvanometer, indicating that the potential difference across its terminals is zero. This occurs when the voltage drop across $R_1$ equals the voltage drop across $R_3$, and similarly, the voltage drop across $R_2$ equals that across $R_4$.

At balance:

$$
\frac{R_1}{R_2} = \frac{R_3}{R_4}
$$

Rearranging to find the unknown resistance $R_4$:

$$
R_4 = R_3 \times \frac{R_2}{R_1}
$$

where:
- $R_1$ and $R_2$ are known resistances forming the ratio arm
- $R_3$ is a known standard resistance
- $R_4$ (or $R_x$) is the unknown resistance to be measured

**Derivation:**

When the galvanometer shows zero deflection ($I_g = 0$), currents $I_1$ flows through $R_1$ and $R_2$, while current $I_2$ flows through $R_3$ and $R_4$.

Since there's no current through the galvanometer, the potential at point B equals the potential at point D:

$$
V_B = V_D
$$

Therefore:

$$
I_1 R_1 = I_2 R_3 \quad \text{...(1)}
$$

Similarly:

$$
I_1 R_2 = I_2 R_4 \quad \text{...(2)}
$$

Dividing equation (1) by equation (2):

$$
\frac{R_1}{R_2} = \frac{R_3}{R_4}
$$

This is the **balance condition** of the Wheatstone bridge.

**Conceptual Example:**

Imagine a seesaw (teeter-totter) with two children on each side. The seesaw balances when the product of weight and distance on one side equals the product on the other side. Similarly, the Wheatstone bridge balances when the ratio of resistances on one arm matches the ratio on the opposite arm—achieving equilibrium where no current flows through the center (galvanometer).

**Mathematical Example:**

**Problem:** In a Wheatstone bridge, $R_1 = 10 \, \Omega$, $R_2 = 50 \, \Omega$, and $R_3 = 20 \, \Omega$. Find the unknown resistance $R_4$ when the bridge is balanced.

**Given:**
- $R_1 = 10 \, \Omega$
- $R_2 = 50 \, \Omega$
- $R_3 = 20 \, \Omega$
- $R_4 = ?$

**Solution:**

Using the balance condition:

$$
\frac{R_1}{R_2} = \frac{R_3}{R_4}
$$

$$
\frac{10}{50} = \frac{20}{R_4}
$$

$$
R_4 = 20 \times \frac{50}{10} = 100 \, \Omega
$$

**Answer:** The unknown resistance is $R_4 = 100 \, \Omega$.

---

### 3.9.2 Sensitivity and Accuracy

The **sensitivity** of a Wheatstone bridge refers to its ability to detect small changes in resistance. A more sensitive bridge produces larger galvanometer deflection for a given imbalance in resistance values.

Factors affecting sensitivity:

- **Galvanometer sensitivity:** A more sensitive galvanometer detects smaller currents, improving overall bridge sensitivity
- **Battery voltage:** Higher voltage increases current, making small imbalances more detectable
- **Resistance values:** Moderate resistance values (not too high or low) optimize sensitivity

**Advantages of Wheatstone Bridge:**

- High accuracy in resistance measurement (can measure to 0.1% accuracy)
- Null-detection method eliminates measurement errors from meter calibration
- Simple construction and easy to use
- Versatile for wide range of resistance values (1 Ω to several MΩ)

**Limitations:**

- Requires careful balancing for accurate measurements
- Not suitable for very low resistances (< 1 Ω) or very high resistances (> 10 MΩ)
- Sensitive to external factors like temperature changes and vibrations
- Time-consuming to achieve precise balance

---

### Applications

The Wheatstone bridge finds extensive applications in:

- **Resistance Measurement:** Precise determination of unknown resistances in laboratory and industrial settings
- **Strain Gauges:** Measuring mechanical strain and stress by detecting resistance changes in strain-sensitive wires
- **Temperature Sensors:** Resistance temperature detectors (RTDs) use Wheatstone bridges to measure temperature-dependent resistance changes
- **Pressure Sensors:** Detecting pressure through resistance changes in pressure-sensitive elements
- **Light Sensors:** Photoresistive devices in light-detection circuits
- **Quality Control:** Testing and calibrating resistors during manufacturing

The versatility and precision of the Wheatstone bridge make it fundamental in instrumentation, sensor technology, and metrology, enabling accurate measurements crucial for scientific research and industrial applications.

---

## 3.10 Meter Bridge

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1tY_cwvwuwADI2kSpKy1_vAhIgOAp7WFP" alt="Meter bridge setup showing uniform wire, resistances, and balancing length measurement." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.10:</b> Meter bridge apparatus based on Wheatstone bridge principle.</i></figcaption>  
</figure>

The meter bridge, also known as the slide wire bridge, is a practical application of the Wheatstone bridge principle used to determine unknown resistance with high accuracy in laboratory settings. The apparatus consists of a uniform resistance wire of exactly one meter length (typically made of constantan or manganin), stretched tightly between two metal strips mounted on a wooden base. The name "meter bridge" derives from the one-meter-long wire that forms the bridge.

Unlike the standard Wheatstone bridge with discrete resistors, the meter bridge uses a continuous uniform wire where resistance is directly proportional to length. This elegant design allows for fine adjustment of resistance ratios simply by moving a sliding contact (jockey) along the wire until balance is achieved. The null point—where the galvanometer shows zero deflection—indicates that the bridge is balanced, enabling calculation of the unknown resistance using the measured length and a known standard resistance.

The meter bridge is widely used in educational physics laboratories to teach principles of electrical measurements and in practical applications where accurate resistance determination is required. Its simplicity, portability, and reasonable accuracy make it an invaluable tool for students and researchers alike.

### 3.10.1 Principle and Working

The meter bridge operates on the **Wheatstone bridge principle** of null deflection. A uniform resistance wire AB of length 100 cm is stretched tightly. When the jockey touches the wire at point C, it divides the wire into two segments: AC of length $l_1$ and CB of length $l_2 = (100 - l_1)$ cm.

Since the wire is uniform (constant cross-sectional area $A$ and resistivity $\rho$), the resistance of each segment is proportional to its length:

$$
R_{\text{wire}} = \rho \frac{l}{A}
$$

For segment AC:

$$
P = \rho \frac{l_1}{A}
$$

For segment CB:

$$
Q = \rho \frac{l_2}{A} = \rho \frac{(100 - l_1)}{A}
$$

A known resistance $R$ is placed in one gap and unknown resistance $X$ in the other gap. When the bridge is balanced (galvanometer shows zero deflection):

$$
\frac{P}{Q} = \frac{R}{X}
$$

Substituting the expressions for $P$ and $Q$:

$$
\frac{\rho l_1 / A}{\rho (100 - l_1) / A} = \frac{R}{X}
$$

Simplifying:

$$
\frac{l_1}{100 - l_1} = \frac{R}{X}
$$

Solving for unknown resistance $X$:

$$
X = R \times \frac{100 - l_1}{l_1}
$$

Or equivalently:

$$
X = R \times \frac{l_2}{l_1}
$$

where:
- $X$ = unknown resistance to be determined (Ω)
- $R$ = known standard resistance (Ω)
- $l_1$ = balancing length from end A to null point C (cm)
- $l_2 = (100 - l_1)$ = remaining length from C to end B (cm)

**Conceptual Example:**

Imagine a see-saw with two children of different weights sitting at different distances from the fulcrum. Balance occurs when (weight₁ × distance₁) equals (weight₂ × distance₂). Similarly, the meter bridge balances when the ratio of wire lengths equals the ratio of the two resistances—achieving equilibrium where no current flows through the galvanometer.

**Mathematical Example:**

**Problem:** In a meter bridge experiment, a known resistance $R = 10 \, \Omega$ is connected in the left gap and an unknown resistance $X$ in the right gap. The null point is obtained at length $l_1 = 40 \, \text{cm}$ from end A. Find the unknown resistance $X$.

**Given:**
- Known resistance: $R = 10 \, \Omega$
- Balancing length: $l_1 = 40 \, \text{cm}$
- Remaining length: $l_2 = 100 - 40 = 60 \, \text{cm}$

**Solution:**

Using the meter bridge formula:

$$
X = R \times \frac{l_2}{l_1}
$$

$$
X = 10 \times \frac{60}{40}
$$

$$
X = 10 \times 1.5 = 15 \, \Omega
$$

**Answer:** The unknown resistance is $X = 15 \, \Omega$.

### Applications

The meter bridge finds applications in:

- **Laboratory Experiments:** Determining unknown resistance of conductors, measuring specific resistance of wire materials
- **Quality Control:** Testing resistor values during manufacturing and quality assurance
- **Educational Purposes:** Teaching Wheatstone bridge principle, resistance concepts, and experimental techniques
- **Material Testing:** Measuring resistivity of different materials and alloys
- **Calibration:** Verifying resistance values of standard resistors

The meter bridge's combination of simplicity, portability, and reasonable accuracy (typically 1-2% with care) makes it ideal for educational demonstrations and routine laboratory measurements where extremely high precision is not required.

---

## 3.11 Potentiometer: Principle and Applications

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/1ZnCvDxrQ-UZ5I8509pF6D3IOE9huOjOS" alt="Potentiomter." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.11:</b> Potentiometer setup used to measure voltage without drawing current from the circuit.</i></figcaption>  
</figure>


The potentiometer is a precision instrument used to measure voltage and electromotive force (EMF) using the **null deflection method**. Unlike ordinary voltmeters that draw current from the circuit being measured (thereby introducing errors), the potentiometer measures voltage by balancing it against a known potential difference, drawing zero current at the null point. This fundamental advantage makes it ideal for accurate measurements in laboratory settings and for calibrating other instruments.

The instrument consists of a long, uniform resistance wire (typically several meters of manganin or constantan wire) stretched tightly between two terminals, with a sliding contact (jockey) that can be moved along the wire to tap different potential differences. A steady current is maintained through the wire by a driver battery, establishing a uniform potential gradient along its length. The device operates on the principle that potential drop across any segment of uniform wire is directly proportional to its length when constant current flows through it.

Potentiometers are extensively used in physics laboratories for measuring EMF of cells, determining internal resistance, comparing voltages, and calibrating voltmeters and ammeters. Their high precision (typically 0.01% accuracy), combined with the advantage of not drawing current from the source during measurement, makes them invaluable for standards laboratories and precision electrical measurements.

### 3.11.1 Principle of Operation

The working principle of the potentiometer is based on the fundamental relationship between potential drop and wire length. For a uniform wire of length $L$ carrying constant current $I$, the potential drop $V$ across any length $l$ is:

$$
V = k \cdot l
$$

where $k$ is the **potential gradient** (voltage per unit length):

$$
k = \frac{V_0}{L}
$$

Here:
- $V_0$ = total voltage across the wire (from driver battery)
- $L$ = total length of potentiometer wire
- $l$ = balancing length (distance from one end to null point)
- $k$ = potential gradient (V/m or V/cm)

**Derivation:**

The resistance of uniform wire of length $l$ is:

$$
R_l = \rho \frac{l}{A}
$$

where $\rho$ = resistivity and $A$ = cross-sectional area.

The potential drop across length $l$ with current $I$ flowing:

$$
V_l = I R_l = I \rho \frac{l}{A}
$$

Since $I$, $\rho$, and $A$ are constants:

$$
V_l = \left(\frac{I \rho}{A}\right) l = k \cdot l
$$

This proves that **voltage is directly proportional to length** for uniform wire carrying constant current.

**Null Point Method:**

When an unknown EMF source (cell) is connected in the secondary circuit with a galvanometer, the jockey is moved along the wire until the galvanometer shows zero deflection (null point). At this point:

$$
\text{EMF of cell} = \text{Potential drop across length } l
$$

$$
E = k \cdot l = \frac{V_0}{L} \cdot l
$$

**Conceptual Example:**

Think of a potentiometer wire like a ruler for voltage. Just as you measure physical length by comparing it with standard markings on a ruler, you "measure" voltage by comparing it against the potential drop along a calibrated wire. The null point is like finding the exact matching mark where the unknown voltage equals the reference voltage—no current flows because there's perfect balance.

**Mathematical Example:**

**Problem:** A potentiometer wire of length $L = 10 \, \text{m}$ has a potential difference of $V_0 = 2 \, \text{V}$ across it. An unknown EMF cell is connected in the secondary circuit, and the null point is obtained at length $l = 3.5 \, \text{m}$. Find the EMF of the cell.

**Given:**
- Wire length: $L = 10 \, \text{m}$
- Total voltage: $V_0 = 2 \, \text{V}$
- Balancing length: $l = 3.5 \, \text{m}$

**Solution:**

First, calculate potential gradient:

$$
k = \frac{V_0}{L} = \frac{2}{10} = 0.2 \, \text{V/m}
$$

EMF of unknown cell:

$$
E = k \cdot l = 0.2 \times 3.5 = 0.7 \, \text{V}
$$

**Answer:** The EMF of the cell is $E = 0.7 \, \text{V}$.

---

### 3.11.2 Applications of Potentiometer

**1. Comparison of EMF of Two Cells**

To compare EMFs $E_1$ and $E_2$ of two cells, each is connected separately in the secondary circuit and balancing lengths $l_1$ and $l_2$ are measured:

$$
\frac{E_1}{E_2} = \frac{l_1}{l_2}
$$

This method provides accurate comparison without drawing current from either cell.

**2. Measurement of Internal Resistance**

The internal resistance $r$ of a cell can be determined by measuring balancing length $l_1$ with the cell in open circuit (EMF = $E$) and $l_2$ with external resistance $R$ connected (terminal voltage = $V$):

$$
E = k \cdot l_1
$$

$$
V = k \cdot l_2
$$

From $V = E - Ir$ and Ohm's law:

$$
r = R \left(\frac{l_1 - l_2}{l_2}\right)
$$

**3. Calibration of Voltmeters and Ammeters**

By comparing readings of voltmeters/ammeters against potentiometer measurements (which are highly accurate), these instruments can be calibrated to correct any errors.

**Mathematical Example: Internal Resistance**

**Problem:** In a potentiometer experiment, the balancing length for a cell in open circuit is $l_1 = 60 \, \text{cm}$. When a $10 \, \Omega$ resistor is connected across the cell, the balancing length becomes $l_2 = 50 \, \text{cm}$. Find the internal resistance of the cell.

**Given:**
- Open circuit length: $l_1 = 60 \, \text{cm}$
- With $R = 10 \, \Omega$: $l_2 = 50 \, \text{cm}$

**Solution:**

$$
r = R \left(\frac{l_1 - l_2}{l_2}\right)
$$

$$
r = 10 \times \frac{60 - 50}{50} = 10 \times \frac{10}{50} = 2 \, \Omega
$$

**Answer:** Internal resistance $r = 2 \, \Omega$.

---

### Advantages and Limitations

**Advantages:**

- **High Accuracy:** Provides measurements accurate to 0.01% or better
- **No Current Drawn:** At null point, zero current flows from measured source, preventing loading errors
- **Versatile:** Can measure EMF, voltage, internal resistance, and calibrate instruments
- **Direct Comparison:** Compares voltages directly without requiring calibrated meters

**Limitations:**

- **Time-Consuming:** Requires manual adjustment to find null point
- **Requires Stable Source:** Driver battery must provide constant voltage throughout measurement
- **Limited Range:** Cannot measure very high voltages (limited by wire length and insulation)
- **Sensitive to Temperature:** Wire resistance changes with temperature affect accuracy

---

## 3.12 Heating Effect of Current (Joule's Law)

<figure style="display: flex; flex-direction: column; align-items: center;">  
<img src="https://lh3.googleusercontent.com/d/10EbPYRDmX2SxgPjd3kbRgrFZmE_G3kqc" alt="Complex circuit illustrating Kirchhoff's junction and loop laws for current and voltage." style="max-width: 90%; height: auto;">  
<figcaption style="text-align: center; margin-top: 8px;"><i><b>Figure 3.12:</b> Heat produced in resistor due to current according to Joule's law.</i></figcaption>  
</figure>

When electric current flows through a conductor having resistance, electrical energy is converted into heat energy. This phenomenon, discovered by James Prescott Joule in 1840, is quantified by Joule's law of heating. The law states that heat produced in a resistor is directly proportional to the square of current, the resistance, and the time for which current flows.

The heat energy $H$ (or $Q$) produced when current $I$ flows through resistance $R$ for time $t$ is given by:

$$
H = I^2 R t
$$

where:
- $H$ = heat energy produced (joules, J)
- $I$ = current flowing through resistor (amperes, A)
- $R$ = resistance of conductor (ohms, Ω)
- $t$ = time duration (seconds, s)

Using Ohm's law ($V = IR$), this can be expressed in alternative forms:

$$
H = V I t = \frac{V^2}{R} t
$$

The first form ($I^2 R t$) is most useful when current is known, the second ($V I t$) when both voltage and current are known, and the third ($V^2 t / R$) when voltage is known and constant.

**Applications:** The heating effect of current has numerous practical applications:

- **Electric Heaters and Irons:** High-resistance coils convert electrical energy to heat for warming rooms or pressing clothes
- **Electric Kettles and Toasters:** Resistive heating elements rapidly heat water or toast bread
- **Incandescent Bulbs:** Tungsten filaments reach temperatures of 2500-3000°C, emitting visible light
- **Electric Fuses:** Thin wire melts when excessive current flows, breaking the circuit to prevent damage
- **Electric Furnaces:** Industrial furnaces use high-current heating for melting metals and manufacturing processes

**Mathematical Example:**

**Problem:** An electric iron has a resistance of $50 \, \Omega$ and operates at $220 \, \text{V}$ for 30 minutes. Calculate the heat energy produced.

**Given:**
- Resistance: $R = 50 \, \Omega$
- Voltage: $V = 220 \, \text{V}$
- Time: $t = 30 \times 60 = 1800 \, \text{s}$

**Solution:**

$$
H = \frac{V^2}{R} t = \frac{(220)^2}{50} \times 1800
$$

$$
H = \frac{48400}{50} \times 1800 = 968 \times 1800 = 1,742,400 \, \text{J}
$$

Converting to kilowatt-hours:

$$
H = \frac{1,742,400}{3.6 \times 10^6} = 0.484 \, \text{kWh}
$$

**Answer:** Heat produced is $1.74 \, \text{MJ}$ or $0.484 \, \text{kWh}$.

---

## 3.13 Carbon Resistors and Color Code

Carbon composition resistors are among the most widely used electronic components, providing fixed resistance values in circuits. Due to their small physical size, printing numerical values directly on them is impractical. Instead, a standardized **color code system** using colored bands painted on the resistor body indicates resistance value, multiplier, and tolerance, enabling quick identification.

A typical **four-band carbon resistor** has:

- **1st Band:** First significant digit
- **2nd Band:** Second significant digit  
- **3rd Band:** Multiplier (power of 10)
- **4th Band:** Tolerance (accuracy percentage)

**Color Code Table:**

| **Color** | **Digit** | **Multiplier** | **Tolerance** |
|----------|----------|----------------|---------------|
| Black | 0 | ×1 | — |
| Brown | 1 | ×10 | ±1% |
| Red | 2 | ×100 | ±2% |
| Orange | 3 | ×1,000 | — |
| Yellow | 4 | ×10,000 | — |
| Green | 5 | ×100,000 | ±0.5% |
| Blue | 6 | ×1,000,000 | ±0.25% |
| Violet | 7 | ×10,000,000 | ±0.1% |
| Grey | 8 | ×100,000,000 | — |
| White | 9 | ×1,000,000,000 | — |
| Gold | — | ×0.1 | ±5% |
| Silver | — | ×0.01 | ±10% |

**Reading Resistor Value:**

The resistance value is calculated as:

$$
R = (\text{Digit}_1 \, \text{Digit}_2) \times \text{Multiplier} \pm \text{Tolerance}
$$

**Mnemonic for Remembering Colors:**

"**B**lack **B**ears **R**un **O**ver **Y**our **G**arden **B**ack **V**ery **G**ood **W**eather"

(Black, Brown, Red, Orange, Yellow, Green, Blue, Violet, Grey, White)

**Example 1:** Resistor with bands **Brown (1), Black (0), Red (×100), Gold (±5%)**

$$
R = 10 \times 100 = 1,000 \, \Omega \pm 5\% = 1 \, k\Omega \pm 5\%
$$

**Example 2:** Resistor with bands **Yellow (4), Violet (7), Orange (×1,000), Gold (±5%)**

$$
R = 47 \times 1,000 = 47,000 \, \Omega \pm 5\% = 47 \, k\Omega \pm 5\%
$$

**Five-Band Resistors:** For higher precision, a five-band code includes three significant digits:

- Bands 1-3: Three digits
- Band 4: Multiplier  
- Band 5: Tolerance

**Example:** **Red (2), Violet (7), Black (0), Brown (×10), Brown (±1%)**

$$
R = 270 \times 10 = 2,700 \, \Omega \pm 1\% = 2.7 \, k\Omega \pm 1\%
$$

**Practical Tips:**

- Hold resistor with tolerance band (gold/silver) on the right side
- Read from left to right starting with the first colored band
- Tolerance band is usually spaced slightly apart from other bands
- If in doubt, measure with a multimeter to verify

Carbon resistors are essential in electronics for current limiting, voltage division, biasing transistors, and signal conditioning, making the color code system fundamental knowledge for anyone working with circuits.

---

## Summary

This chapter on Current Electricity provides a detailed exploration of the fundamental principles governing the flow of electric charge and their applications in practical circuits. Beginning with the microscopic origins of current in metallic conductors, it establishes that current arises from the drift motion of free electrons under an applied electric field, with conventional current direction defined oppositely to electron flow for analytic consistency.

The quantitative concept of current density introduces how current is distributed spatially across conductors and links macroscopic current with microscopic electric fields and material conductivity, reinforcing the microscopic foundation of Ohm’s law.

Ohm’s law characterizes linear relationships between voltage, current, and resistance in ohmic materials, guiding the calculation of current flow and potential differences across conductors. Resistance, an extrinsic property depending on length, cross-sectional area, and resistivity, encapsulates material opposition to current. The resistivity itself is temperature-dependent, rising linearly with temperature for metals due to enhanced lattice vibrations hindering electron motion.

The chapter extends these principles to explore combinations of resistors, both series and parallel, enabling calculation of equivalent resistance and serving as building blocks for complex circuit design. Cells and batteries are modeled including internal resistance, explaining terminal voltage variations under load, critical for battery performance understanding.

Kirchhoff’s circuit laws, encompassing the junction (current) and loop (voltage) rules, provide powerful tools for rigorous circuit analysis beyond simple series/parallel systems. The Wheatstone bridge and meter bridge apparatus employ these laws for precise resistance measurements, illustrating principles of circuit equilibrium and potentiometry.

The potentiometer is introduced as a precision device for voltage measurements, exploiting the concept of null deflection to avoid current draw and errors, essential in laboratory and experimental physics.

The heating effect of current, as described by Joule’s law, ties electrical parameters directly to thermal energy produced in conductors, a phenomenon leveraged in everyday appliances and an important safety consideration.

A practical understanding of carbon resistors and their color coding further integrates theoretical knowledge with hardware implementation, bridging physics and engineering.

Together, these topics elucidate a cohesive framework linking microscopic charge carrier dynamics with macroscopic electrical behavior, blending empirical laws with quantitative models. This foundation is critical not only for understanding electrical circuits but also for advancing in electronics, instrumentation, and power engineering.

---

## Practice Questions

1. Define electric current and state its SI unit.

2. What is drift velocity? Explain its physical significance in a metallic conductor.

3. Differentiate between conventional current and electron flow.

4. Derive the expression for drift velocity in terms of current and other relevant parameters.

5. Calculate the drift velocity of electrons in a copper wire of cross-sectional area $1 mm^2$ carrying a current of 2 A. (Given  $n = 8.5 \times 10^{28} \, m^{-3} $, $ e = 1.6 \times 10^{-19} \, C $).

6. Define current density and state its relation with electric field and conductivity.

7. A wire of length 100 m and cross-sectional area 1 mm\(^2\) has a resistance of 5 Ω. Calculate its resistivity.

8. State Ohm’s law. How does an ohmic conductor differ from a non-ohmic conductor?

9. Calculate the resistance of a wire of length 2 m and diameter 0.5 mm made of a material with resistivity $ 1.6 \times 10^{-8} \, \Omega m $.

10. Calculate the resistance of a copper wire at 70°C if its resistance at 20°C is 10 Ω. The temperature coefficient of resistivity for copper is $ 0.004 , ^\circ C^{-1} $.

11. Two resistors 6 Ω and 3 Ω are connected (a) in series, (b) in parallel. Find the equivalent resistance in both cases.

12. What happens to the resistance of a metal wire if (a) its length is doubled, (b) its diameter is doubled?

13. A cell of EMF 12 V and internal resistance 1 Ω is connected to an external resistor of 5 Ω. Find the current flowing and terminal voltage.

14. State Kirchhoff’s junction and loop rules.

15. In a Wheatstone bridge, if $ R_1 = 100 \, \Omega $, $ R_2 = 200 \, \Omega $, and $ R_3 = 150 \, \Omega $, find the value of $ R_4 $ at balance.

16. Define the function of a potentiometer. How does it measure emf accurately?

17. Calculate heat produced in a resistor of 10 Ω carrying 2 A current for 5 minutes.

18. Explain the significance of the temperature coefficient of resistance.

19. What is the color code of a resistor having bands: red, violet, yellow, gold?

20. Derive the expression for equivalent resistance of resistors connected in series.

21. Derive the expression for equivalent resistance of resistors connected in parallel.

22. Explain why current density is a vector quantity.

23. Explain the internal resistance of a cell with an example.

24. A wire of resistance 10 Ω is stretched to double its length. Calculate its new resistance.

25. Calculate the power dissipated in a resistor of 4 Ω carrying 3 A current.

26. Derive the relation between emf, internal resistance, and terminal voltage of a cell.

27. A copper wire of length 2 m and cross-sectional area $ 2 \times 10^{-6} \, m^2 $ carries a current of 3 A. Calculate drift velocity.

28. Explain Joule’s law of heating and its applications.

29. A cell of emf 6 V and internal resistance 0.5 Ω delivers 1.5 A current. Calculate terminal voltage.

30. How does combination of resistors in parallel affect equivalent resistance and current distribution?

---

# End of Chapter 3: Current_Electricity