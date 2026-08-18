# temperature control

Temperature control is the closed-loop regulation of a heated or cooled body against a setpoint: a sensor reads the actual temperature, a control algorithm compares it to the target, and the loop modulates the heating element or the cooling airflow to close the error.[1059][1058][257] It is the defining feature that separates a usable soldering tool from a mains-connected heating element,[729][596] and it appears again wherever electronics must hold a stable operating point — fan-cooled instruments, ovenised crystal oscillators, calibration laboratories, and spacecraft.[1753][1049][424][r7LbLwnYVZE]

## The loop

The minimum implementation is a heater, a temperature sensor, and a controller that cycles the element on and off. In a hot air rework station the sensor sits in the handle alongside the element and serves both the regulation loop and the stand-detection that drops the tool into sleep mode.[1058] The controller does not simply switch the element on or off at a fixed rate: driving a mains element, it decides on a cycle-by-cycle basis how much to pass, so a single-shot capture of the element drive can show one and a half mains cycles conducting, or only a half cycle, depending on what the loop needs to hold the setpoint.[1059] Airflow is part of that calculation, since forced air is a load on the loop and raising the flow rate changes the duty the element must deliver.[1059]

The quality of the algorithm shows up in the step response. A well-behaved loop ramps to the setpoint and holds it without overshooting;[257] a controller without a PID algorithm exhibits visible overshoot at the start and continuing oscillation around the target.[174] A poorly behaved instrument may ramp to roughly 250 degrees and then fall back with what appears to be large overshoot, with the displayed temperature jumping around erratically.[hVIo7vmIExw] Regulation quality also varies between nominally similar cheap stations: two units both set to 250 °C behave differently, one showing a steady on/off heating indicator and the other flickering in a way that suggests oscillation in the heating element drive.[596]

Not every controller needs a processor. A heater controller can be built entirely from a 555 timer and 4000-series CMOS logic, reading the temperature, controlling the ramp, and driving a motor, with the ramp profile set by discrete analog elements.[hVIo7vmIExw]

## Sensing and accuracy

Loop accuracy is bounded by the measurement. A soldering station built around a claim of accurate temperature control without user calibration uses a Microchip TC500, a 17-bit analog-to-digital converter, to acquire the tip temperature — a deliberate expenditure of resolution to support that claim.[1106]

Factory calibration on cheap stations is not to be assumed: a station set to 250 °C may sit at around 235 °C, correctable by adjusting the front-panel potentiometer.[596] The practical consequence is that the number on the dial is a station-specific quantity rather than an absolute one. A low-thermal-capacity station has to be dialled to 400 °C to flow a particular joint quickly, where a high-capacity cartridge iron does the same joint at 270 °C on the dial.[596] Comparing setpoints between stations is therefore meaningless without also comparing their thermal capacity.

## Soldering and rework

An iron with no temperature control is wired straight from the mains to the element and runs wherever it settles.[729] Such irons can reach around 500 °C, and the direct consequence of that uncontrolled overshoot is lifted pads.[1113] The corresponding failure at the low end is a fixed low-power iron — 8 W with no adjustment — that cannot raise a ground-plane-connected pad to the melting point no matter how much solder is blobbed on for thermal coupling.[1110][913] A temperature-controlled station, even the cheapest one on the market, is the minimum acceptable tool.[596]

Working setpoints follow the job. A desoldering station spans 160 °C to 480 °C, with most bulk desoldering done at 300 °C and the displayed temperature barely sagging under load on a heat-sunk multilayer board — a thermal capacity result, not a setpoint result.[542] Hot air rework starts at a 100 °C minimum, which is useful for heat shrink typically rated around 125 °C,[167] and runs above 400 °C for stubborn joints, with 410 °C and an airflow setting around six used to lift a BGA.[167] Board quality bounds the top end; a high-temperature FR5 board tolerates it, and balancing temperature against airflow is a matter of technique rather than a fixed recipe.[167] For reflowing a stencilled board with a hot air gun, the target peak is around 220 °C, so the gun is set roughly 40–50 °C above that — about 250 °C, and not above 250–260 °C, because temperature-sensitive components such as LEDs do not survive higher.[415]

Standby behaviour is part of the control scheme. A stand sensor — magnets and a detector in the handle — drops the tool into sleep, and a hot air station keeps the fan running after the element switches off, cutting the fan only when the tool falls to 100 °C.[167][1058] A sleeping iron sits at around 225 °C and is specified to recover to working temperature in two or three seconds.[1064] The same idle-and-recover logic can be implemented in firmware on a portable iron, where the microcontroller manages a slower duty cycle to lower the temperature in standby, alongside battery low-voltage cutout and the on/off switch.[znYVJGfHj9Q] Power display makes the loop visible: a station showing drive power reads 100% while recovering and falls back as the tip reaches setpoint,[1064] and a USB-powered iron that peaks at 82 W idles at roughly 10–15 W simply holding temperature.[1646]

## Setpoint interfaces

How the setpoint is entered is a recurring source of friction. Locking out temperature adjustment while the tool is on the stand — whether during cool-down on a hot air station, or behind an interlock on a cartridge iron that demands the tool be held before the temperature can be changed — is a design fault, as is hiding the set temperature until the tool is lifted.[1058][1106] Coarse adjustment is a related problem: desoldering tweezers that step in 50 °C increments, offering settings as low as 50 °C, give less useful control than finer steps would.[1650] Single-degree increments are the better behaviour.[OvGdE5hC1Ro]

A portable iron may omit on-tool adjustment entirely, setting temperature over a USB serial port from a computer and retaining the last setpoint for field use.[1646] This is a genuine trade rather than a defect: an iron that cannot be adjusted in the field is the wrong iron for someone who needs field adjustment, and the right one for someone who does not want a screen and buttons on the handle.[5vbg8QEZXfY]

## Thermal management of equipment

The same loop applied in reverse — modulating cooling rather than heating — is standard in instruments and computers. Fans are run under thermal control so they idle nearly stationary and spin up only under load, which requires the thermal design to be integrated with the case styling and assembly rather than added at the end.[1396] A battery analyser ramps its fan without any user action, driven purely by internal temperature.[1434] Desktop PC cooling is thermally controlled and cycles through modes,[1280][1279] and a small fan in a cramped chassis makes for poor thermals regardless of the control loop.[1279]

Cooling control can also serve precision rather than survival. An isolated oscilloscope front end has an internal temperature sensor and regulates fan speed to hold the enclosure at 40 °C, so that the analog electronics sit at a constant temperature and do not drift.[1753] The same reasoning drives the oven-controlled oscillator: crystals are inherently stable when held at a fixed temperature, so even a ten-cent crystal can perform well provided its temperature and drive voltage are held constant.[1049]

## Controlled environments

Where the loop encloses a whole workspace, the specifications tighten. A portable calibration laboratory is an insulated, environmentally controlled box whose air conditioning is sized to remove the heat generated by the equipment inside; it holds 23 °C ± 5 °C and 5–80% relative humidity, the humidity floor being the hard part in a dry climate.[424] SAR testing is stricter still: the ambient must be between 18 °C and 25 °C, and once a test begins it may not drift by more than ±1 °C, because the dielectric parameters of the tissue-simulant liquid change with temperature and a few degrees of drift between morning and afternoon invalidates the calculated result.[201]

Thermal cycling equipment inverts the problem, needing both heating and cooling under precise control; a practical implementation uses a standard PC liquid-cooling system extended with custom aluminium blocks.[203]

## Extreme environments

On a Mars rover, surface temperatures at the equator can be pleasant at midday in summer and fall below −100 °C on a winter night, which makes thermal control a first-order design problem. The intuitive concern — keeping the vehicle warm — is not the binding constraint; the harder job is keeping it cool enough, because a multi-mission radioisotope thermoelectric generator mounted on the rover is a continuous heat source.[r7LbLwnYVZE]
