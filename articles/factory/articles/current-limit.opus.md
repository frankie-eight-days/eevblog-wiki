# current limit

A current limit is the ceiling a power source imposes on the current it will deliver, enforced by folding back the output voltage once the load tries to draw more than the set value.[224][OOFoYVQ7kVo] On a bench supply it is the primary safety mechanism protecting an unknown or suspect circuit: a supply set for 24 V that hits a 0.1 A limit will simply sag to 15 V rather than deliver the power that would destroy the board under test.[1672] The limit is also the defining half of a bench supply's dual personality — below the threshold it behaves as a constant voltage source, above it as a constant current source — and a supply that cannot hold that limit under a short circuit is considered defective, since surviving a shorted output is the entire point of having the feature.[861][OOFoYVQ7kVo]

## Setting a limit before applying power

Standard practice on unknown hardware is to power it from an adjustable bench supply with the current limit deliberately set close to the expected draw, so that a fault cannot escalate.[357] The value is chosen from what the circuit ought to consume: 6 V at 100 mA for a keyboard controller that should never draw more than that, which then measured 4 mA in operation[1245]; 130 mA at 5 V for a prototype whose faults were still unknown, explicitly to protect the circuit if something went wrong[357]; 0.1 A at 24 V, only 2.4 W, on a repair where the goal was merely to see whether the display lit[1672]. Where the draw is genuinely unknown the limit is set generously — 7.2 V at 1 A on a camera teardown, 1.7 A on a laptop that turned out to draw 80 mA — on the reasoning that a wrong guess in the loose direction still bounds the damage.[625][1527] For higher-power work the same logic scales: 40 V with a 5 A limit gives a 200 W envelope, and 40 V at half an amp is used to bound the potential damage on a supply already known to have caught fire.[1036][1035]

The limit is also matched to the weakest component in the chain rather than to the supply's capability. An LM317L has a 100 mA internal limit, so the bench supply feeding it is set to the same 100 mA.[660]

## Reading the limit as a diagnostic

Because entering current limit is visible on the front panel, the limit doubles as a fault indicator. A circuit sitting at 197 mA against a 200 mA setting, with its LEDs at abnormal brightness, is not working — it is pinned against the limit, which is itself the diagnosis.[710] Unexpected limiting during a bring-up prompted a check that revealed the supply leads were reversed and the board's reverse-protection diode was conducting.[1520] The inverse error also occurs: apparent hiccupping on a PC repair was initially blamed on an insufficient 3.5 A limit before being traced to the unit's own internal supply.[1071][pKV_JiauAE4] A controller rated at 1.1 A that overloads and drops out even with a 1.5 A limit available points to a fault rather than a supply shortcoming.[1277]

## Choosing the value

The right value depends on what is being tested. For a finished product expected to work, the limit is set to the supply's full capability — 3 A on a converter needing about 1 A — because there is nothing to protect against.[895] For a design still under development, a limit just above the expected draw, such as 1.1 A per channel, is the safe choice.[895] Setting a low limit is not free, however: power-on surge currents can push a supply into limiting, collapsing the rail and upsetting the converter being powered, so a nominally safe setting can itself create the fault it was meant to prevent.[895]

Adjustable limits are also used as a fixed guard on shared equipment, set once by a pot so that an operator cannot damage an expensive device under test.[576] Sweeping the limit is a measurement technique in its own right — ramping from 0 A to 1 A in a hundred steps against a 10 V compliance produces a characteristic curve.[638]

## Implementation in supplies and regulators

In a discrete design the limit is set by comparing the drop across a sense resistor to an adjustable threshold. In one lab supply design the current-adjust pot develops 250 mV for a 250 mA limit, a direct 1 mV per mA correspondence that can be verified by probing the pot's wiper.[224] An LT3080-based topology uses two regulators, one for constant current and one for constant voltage, with the current set pin spanning 0 to 1 V to represent 0 to 1 A.[221] A two-transistor arrangement gives the current regulation and voltage regulation separate pass elements; when the supply is not in current limit the current pass transistor is effectively a short and the voltage element does the work.[1561]

Some monolithic parts expose the limit externally: a driver with a built-in 4.75 V reference and 31.6 k resistor sets its limit from the total resistance seen at a pin, or from a DAC, and the same part appears as an adjustable ±500 mA supply with adjustable current limit.[1701][1755] Higher up the scale, digital instruments set voltage and current limits per channel from multiplexed DACs.[1434] USB Power Delivery specifies an adjustable current limit alongside its 3.3 V to 48 V adjustable output, in 50 mA steps, though implementing it in a power brick is uncommon.[1749]

Fixed regulators generally carry an unadjustable internal limit whose purpose is self-preservation rather than load protection — a jelly bean regulator folds back to 30 mA into a short, and the concern is that the regulator survives a shorted load and recovers, not that the load is protected.[1147] Linear regulators in older instruments often combine both: an external current limit resistor at the output plus a limit inside the regulator chip, with an LM723-style device providing a dedicated current limit pin.[804]

## Output capacitance

Output capacitance directly undermines current limiting. When the limit engages, a large output capacitor dumps its stored charge into the load, delivering current well over the set value before the loop can respond, so a constant-current supply should carry the minimum possible output capacitance.[549][828] The requirement conflicts with noise performance and loop stability, since some capacitance is needed both to lower output noise and for the current limit loop itself, which makes the value a deliberate compromise rather than a free choice.[224]

## Setting and displaying the limit

Older supplies have no way to preview the setting: the traditional method is to short the output and adjust the pot until the meter reads the desired limit.[166][655] Better designs avoid this with a front-panel shorting switch, a dedicated set-current button, or a set-current display mode that shows the threshold without loading the output.[649][166][655] A single-turn pot is workable for current adjustment where a multi-turn is considered essential for voltage.[649] Failing to display the active limit at all is a design fault — a supply set to 100 mA that never shows the figure leaves the operator guessing.[1402] Interfaces that bury the setting compound the problem, since a limit left at an odd value by a previous user can be difficult to find and change.[8]

## Failure to limit

Supplies do fail at this. Repeatedly shorting a 30 V, 3 A channel with relay contacts destroyed it: instead of limiting cleanly at 3 A the series pass transistor failed, after which the channel could not drive even 10 mA.[861] The expectation is unambiguous — a supply must not exceed its set voltage and must not exceed its set current limit, on power-up or otherwise.[OOFoYVQ7kVo] Firmware faults appear too: one supply reported a spurious 30 to 40 mA with no load attached whenever the limit was set anywhere below 10 mA, later corrected in software.[512][549]

Limiting behaviour is also tested against active loads, where an electronic load's own control loop can interact with the supply's constant current loop; a well-behaved pair enters limit without oscillation even at 80 V.[1691] Universal programmers have been observed self-testing the feature by shorting their own programming rails to confirm the limit engages.[411]
