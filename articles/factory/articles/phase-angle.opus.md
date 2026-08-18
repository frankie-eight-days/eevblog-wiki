# phase angle

Phase angle is the angular displacement between two AC quantities of the same frequency — most often between the voltage across a circuit element and the current through it.[1729][1730] It is the term that separates AC circuit analysis from DC: once a circuit contains reactance, voltage and current no longer peak together, and every impedance, voltage and current has to be described by a magnitude *and* an angle.[1729][1660] The angle is what determines how much of the apparent power delivered to a load is actually converted to work, and it is the quantity an LCR meter, a power analyser and an oscilloscope phase measurement are all ultimately after.[1730][1473][1751]

## Notation and units

The angle is conventionally written as theta or phi; phi is typically used for the difference between a reference waveform and a second signal.[1469][1470] For a rotating phasor the instantaneous angle is theta = omega·t, where omega is angular frequency and t is time — the same omega that appears in reactance expressions, and not to be confused with the ohm symbol despite the shared glyph.[1469]

Angles may be expressed in radians, running from 0 to 2 pi, or in degrees, running from 0 to 360.[1469] In practice phase angle work in electronics is done in degrees, and a calculator left in radians or gradians mode is a standard source of wrong answers when evaluating cos theta or sin theta.[1730] Dave Jones's habit is to check the calculator — his "confuser" — is in degrees mode before every such evaluation.[1730]

## Phasor and complex representation

A sinusoid is generated physically by a coil rotating in a magnetic field, and the angle of the rotor as it sweeps is the phase angle that fixes where the waveform starts.[1469] Dropping that picture onto paper gives a phasor, and dropping two phasors onto an Argand diagram gives the complex plane: the horizontal axis carries real numbers, the vertical axis the imaginary component, with the vector magnitude setting peak amplitude and its angle setting phase.[1469][1470]

The J operator is a 90° rotation. A real value of three becomes J3 when rotated 90°; in polar form the same quantity is written three angle 90, and rotating the other way gives three angle minus 90.[1470] Anticlockwise rotation is positive.[1470]

Polar form makes multiplication and division trivial: magnitudes multiply while angles add. Multiplying 5 V RMS at 20° by 2 V RMS at 30° gives 10 at 50°; if the second angle is instead -30°, the result is 10 at -10°.[1470] Division subtracts the angles — 0° minus -82° yields a current of 1.32 A at a phase of 82.4°, which plots as a single phasor of that magnitude and angle.[1661] The same operation attempted in the time domain requires solving for an instant, whereas the phasor result is a steady-state answer.[1661]

## Resistors, inductors and capacitors

A pure resistor is completely linear and does not affect phase at all; the voltage and current stay together and the phase angle is zero.[1660][81] Zero phase angle is therefore the signature of a purely real, purely resistive impedance with no reactance whatsoever.[1473]

For an inductor, voltage leads current by 90°, giving a reactance of omega·L at angle 90°, or J·omega·L in complex notation.[1470] For a capacitor, current leads the voltage, and the reactance is 1/(omega·C) at angle minus 90 — 180° out of phase with the inductor.[1470] These ideal values assume a pure capacitor and a pure inductor.[1470] In measurement terms, a component whose current leads the test signal is inductive, one whose current lags is predominantly capacitive, and the residual series resistance shows up as a quality factor: with Q greater than one the part is predominantly inductive with a small amount of series resistance.[81]

Impedance in rectangular form is a real component plus an imaginary component, expressing a voltage-to-current relationship carrying a phase angle, and voltages likewise decompose into real and angular parts.[1729] When solving a network, the source is normally taken as the 0° reference against which all other angles are stated.[1729]

## Power, power factor and correction

In an AC circuit, real power is not simply V·I but V·I·cos theta, where theta is the phase angle between voltage and current.[1730] The power triangle sets real power along one axis, the apparent power S = V·I along the hypotenuse at angle theta, and reactive power as the vertical vector joining them — the imaginary component.[1730] Reactive power Q is V·I·sin theta.[1730] With zero phase angle, sin theta is zero and reactive power vanishes, while cos theta is one, so the real power equation collapses back to the DC form.[1730]

Power factor equals cos theta and can never exceed one, so a purely resistive load at unity power factor is the best case.[1730] Because domestic billing is for real power rather than apparent power, a poor power factor does not itself raise consumption; the penalty appears industrially, where the large circulating current demands heavier copper, and where a factory's electricity bill improves the closer the power factor gets to one.[o2NxHu5Bsnk][1730] Correction capacitors placed on the supply appear in parallel with the household's inductive loads, and the two cancel so that the voltage and current are brought back into phase and the installation looks resistive.[o2NxHu5Bsnk]

## Measuring phase on an oscilloscope

The direct method is a cursor measurement on the time display: take the delay between corresponding edges, divide by the period, and multiply by 360. A 95 µs offset on a 1 ms period gives 0.095, or 34.2° against a generator set to 33° — the discrepancy is cursor resolution rather than error in the method, and it is less precise than the scope's automated measurement.[1751]

Sign is relative and depends on which channel is source A. A generator set to positive 33° on channel two means channel two leads channel one, positive meaning it comes first; measuring the yellow channel minus channel two instead reports minus 33°, and swapping the source assignment (with rising edge to rising edge and falling to falling) restores the positive sign.[1751]

The XY display gives a second, independent method. Two sine waves offset in phase trace an ellipse: at zero phase the figure collapses to a straight angled line with both waveforms matching, at 90° it opens into a perfect circle, past 100° it rotates the opposite way, and at 180° it is a straight line again.[1751] The angle follows from the ellipse geometry — the Y-axis intercept divided by the maximum amplitude, then arcsine. Values of 1.062 V over 2.046 V give a ratio of 0.51, and 1.055 V over 2.102 V yields 30.12° against a 33° setting, the shortfall again being measurement resolution.[1751]

## Instruments that report phase angle

An LCR meter works by measuring both voltage and current at 0° and at 90° relative to the signal-generator reference waveform, decomposing the result into real and reactive parts.[1473] Bench and handheld units expose the angle directly: the HP 4263A can display impedance together with phase angle at a selected test frequency, reading close to -90° for a good capacitor and swinging positive for an inductor as the voltage leads instead of lags, and it will also report admittance with phase angle, or conductance with susceptance.[757] The BK Precision 879B offers phase angle on its secondary display alongside dissipation factor, quality factor and ESR.[137]

Phase angle also constrains in-circuit measurement. A resistance in parallel with the capacitor under test is a pure resistor and therefore does not change the phase angle at all, which is why such a shunt does not corrupt the angle-based part of the measurement even though it loads the source.[1474]

On the power side, the Voltech PM300 analyser measures voltage, current, phase angle, real power and apparent power together, plus inrush current.[589] The Uni-T UT71E displays VA with the phase angle of the current on its triple display, along with voltage, current and frequency.[712] Revenue metering demands the same capability with far tighter tolerances: the EDMI smart meter measures phase angle accurately across the full current range, with drift over a roughly 50 °C operating span held to the order of half a degree of error, likely by explicit temperature compensation.[409]
