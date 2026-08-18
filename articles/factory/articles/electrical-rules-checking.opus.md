# electrical rules checking

Electrical rules checking (ERC) is the automated verification step applied to a schematic document, in which a CAD package tests the drawn connectivity against a set of rules describing which pin types may legally connect to which.[953][1193] It is the schematic-side counterpart of design rule checking (DRC), which operates on the PCB: ERC is for schematics, DRC is for boards.[1193] Its value lies in catching connectivity errors at the cheapest possible point in the flow, because an error missed in the schematic propagates into the netlist, into the routed board, and into fabricated hardware — potentially weeks or months later, when the fault is finally found in a prototype that should never have been built.[953]

## Position in the design flow

Designing a board is a multi-step process: draw the schematic, run the ERC, lay out the PCB, run the DRC, generate manufacturing files, then have the board assembled.[1307] ERC therefore sits at the first gate, before any layout effort is committed.[1307][953] Running it should be a matter of course rather than an optional extra.[953]

The consequences of skipping it are concrete. A schematic drawn with a mismatched snap grid can leave a pin visually touching a wire without actually making an electrical connection; that missing connection never reaches the netlist, never reaches the PCB, and the pin simply goes unrouted, producing a board that does not work.[1129][953] Setting snap grids correctly before drawing is the first defence, and ERC is the check that catches what the grid discipline misses.[1129]

## What the check finds

The rule set is expressed as a connection matrix: every combination of pin types — input, output, open collector, power, tri-state, bus — is mapped to an outcome, and each outcome can be set independently to no report, warning, error, or fatal error.[953][255] This makes the tool tunable; a schematic generating a flood of nuisance warnings can have specific checks switched off deliberately.[255]

Errors typically caught include two output pins shorted together, an output pin connected to a power net such as ground, and inputs tied together with nothing driving them — the "no driving source" class of fault.[5eJorvyA708][953][253] In KiCad the same condition is reported as a type three error, a pin connected to some other pins but no pin to drive it.[253] Beyond raw connectivity, a capable package extends the checks to buses, code symbols, sub-parts of multi-part components, configurations, harnesses, and net-level issues.[953]

Warnings are not all equal. Hidden power pins on parts such as the 74HC series will generate hidden-net-added notices for VCC and ground that carry no real meaning and can be dismissed.[953][952]

## Invocation and reporting

In Altium Designer the ERC is reached either by compiling the individual schematic document or by compiling the entire PCB project; compiling the project is the recommended route.[953] The term "compile" is simply another name for running an electrical rules check, and the analogy is deliberate — the schematic has been drawn, and compilation reports whether something stupid has been done.[953] The check can also be bound into an output job so the report is generated alongside other outputs, as HTML or as a PDF suitable for circulation.[953]

Other packages present the same idea under their own names. DIPtrace places ERC on F9 with an electrical rule setup dialog structurally identical to Altium's, and runs effectively instantly.[255] KiCad exposes ERC alongside the netlist and BOM generators, and additionally places an ERC marker on the schematic as a graphical object, which is unusual — the markers must be erased from the page after the underlying errors are resolved.[253]

## Zero errors as a gate

The working goal is to drive all errors and warnings to zero before proceeding to PCB layout.[953][253] Many companies enforce this as a formal gate: demonstrating a clean ERC is a precondition for moving to the PCB step.[953] Serious organisations treat this rigorously — "once bitten, twice shy" — and an ERC is regarded as a genuinely powerful tool rather than a formality.[953]

In practice the zero-error target is often reached by fudging: suppressing or overriding errors the designer believes they understand.[953][253] This is legitimate when the designer genuinely does know what the errors are, but it is a judgment call, and ignoring errors requires actually knowing what one is doing.[253]

The same caveat applies to the check as a whole. A report showing no errors proves only that the schematic satisfies the rules that were configured; the meaningfulness of the result rests entirely on the constraints set up beforehand.[1193] A board can be riddled with problems and still produce a clean report — the appropriate response to a vendor's clean report is to ask to see the constraints.[1193]

## Dependence on library quality

The quality of an ERC is only as good as the quality of the component libraries feeding it.[953] The check reasons about pin types, so pins must be correctly declared as input, output, open collector, bus, power, and so on in the symbol; a data-out pin declared as something other than an output will not trigger the output-to-output rule.[953] Once pin types are corrected in the library and the change is pushed through, the corresponding errors disappear from the report.[953]

No rule check can detect a pin that has been mislabelled in the library — pin 20 entered as pin 19 will pass every electrical rule while being electrically wrong.[953] This is why companies invest in dedicated library designers and freeze verified libraries permanently once validated.[953] The principle is "Garbage in, garbage out."[953] Nor can the tool detect errors of intent: swapping two nets while rearranging a schematic for tidiness produces a perfectly legal circuit that does the wrong thing, and ERC in CAD programs is not magic — "They can't cater for fires up in the gray matter."[240] Knowing what an ERC is and is not capable of, given the information supplied to it, is part of using it.[953]

## The Altium 17 detection failure

A significant defect was identified in Altium Designer 17, in which deliberately introduced schematic faults went undetected.[5eJorvyA708] A test schematic containing two output pins shorted together, a floating input pair with no driving source, and a data output pin connected to ground was compiled; only the no-driving-source conditions were flagged.[5eJorvyA708] No warning or error was raised for the shorted outputs or for the output tied to a power net, despite the project's connection matrix explicitly configuring output-pin-to-output-pin as an error.[5eJorvyA708] The same omission occurred when the check was run from an output job.[5eJorvyA708]

The failure appears tied to compiling a single schematic document rather than the whole project; selecting the project produced correct results, which is why compiling the project is the recommended invocation.[y-NiyRvqfXc][953] The open question is where the document-level compile obtains its rules, since it is evidently not reading the project options.[5eJorvyA708]

The severity comes from the reporting path rather than the missed check alone: a PDF report showing a passed ERC can be handed to management as authorisation to proceed to layout while the schematic still contains gross faults capable of destroying the parts on power-up.[5eJorvyA708]
