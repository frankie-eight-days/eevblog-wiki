# truth table

A truth table is a tabulation of every possible combination of a logic circuit's inputs alongside the output each combination produces.[7bVnsXHO6Uw] It is the primary description of what a digital function does, and it is the starting point from which both the algebraic expression and the gate-level circuit are derived.[rfaCFEqk05M] Because arbitrarily large digital systems reduce to combinations of the same handful of elementary functions, analysis of a circuit containing hundreds or thousands of gates is nothing more than repeated application of the basic truth tables — there is no additional mechanism beyond them.[7bVnsXHO6Uw]

## Construction

The table is drawn with the inputs on one side and the output on the other, and then filled out with all of the possible combinations of the inputs.[7bVnsXHO6Uw] For two inputs labelled A and B with an output C, the four rows are 0 0, 0 1, 1 0 and 1 1.[7bVnsXHO6Uw] The row count is set by the number of inputs: three inputs give eight distinct binary states, and therefore eight output entries.[lJ3q9RHIatU] Gates are not restricted to two inputs, and the table for a wider gate need not be memorised separately — a three-input AND gate's table follows by adding a further input column and enumerating the extended set of combinations.[7bVnsXHO6Uw]

The tables for the elementary gates are treated as material to be known outright rather than looked up, and they are largely self-describing: the gate names state the function, with exclusive-OR the one that does not read off quite so directly.[7bVnsXHO6Uw] The AND table follows from the rule that the output is true only when both inputs are true; each row is settled by asking whether both A and B are 1.[7bVnsXHO6Uw]

## Inverted-output gates

The tables for NAND, NOR and XNOR do not have to be learned as separate facts. Each of these gates is the corresponding AND, OR or XOR with an inverter added on the output, so its table is the base table with the output column complemented.[7bVnsXHO6Uw] The inputs are unchanged; only the output entries flip, so a NAND's output column reads 1, 1, 1, 0 where AND's reads 0, 0, 0, 1.[7bVnsXHO6Uw] The same reasoning explains gate substitutions: tying the two inputs of a NAND gate together turns it into an inverter, which is verified directly against the NAND table, and this in turn allows a NOR gate to be built from NAND gates and a NAND gate from NOR gates.[hFvqEfZfMtA]

## Deriving timing behaviour

A truth table is combinatorial — it says nothing about time on its own — but it fully determines the output waveform once input waveforms are given.[7bVnsXHO6Uw] Working left to right along a timing diagram, each instant is looked up as a row of the table: with an AND function the output stays at 0 while the inputs are 1 and 0, transitions to 1 at the moment both inputs are high, and drops back when the A input falls low.[7bVnsXHO6Uw] Where the overlap between two high inputs is brief, the output pulse is correspondingly brief.[7bVnsXHO6Uw]

## From table to circuit

Converting a desired truth table into gates is the design step that Boolean algebra alone does not supply.[rfaCFEqk05M] The standard route is the sum of products method: the rows whose output is 1 are located, each such row is realised with an AND gate driven by the appropriate input polarities, and the AND outputs are combined.[rfaCFEqk05M] Rows with a 0 output require no term — the circuit is designed around the 1 cases and the remaining input combinations fall out of the design automatically.[rfaCFEqk05M] When a second row in the table carries a 1 on the output, the existing circuit is left untouched and an additional AND gate is added to generate that term.[rfaCFEqk05M]

The method scales badly in raw form. Inputs A through F alone produce a very large table, and the resulting expression can become enormous; multiple outputs, each with its own output column and its own expression, are also permitted.[rfaCFEqk05M] This is why simplification matters: reducing a design from a large gate count to a smaller one saves chip count and silicon area.[7bVnsXHO6Uw] Boolean and De Morgan's theorems are one route to that simplification.[hFvqEfZfMtA] The Karnaugh map is the other, a visual method devised in the 1960s that requires no algebraic manipulation at all; the map is drawn with the same number of squares as there are elements in the truth table, so that the table's contents transfer square for square.[lJ3q9RHIatU]

## In datasheets

Logic device datasheets carry the truth table as the functional description of the part, and it matches the table derived from first principles for the gate in question.[sr1DOHnJi8I] The convention extends to sequential parts, where the table encodes clocking behaviour: a counter whose clock input is marked with the inversion bubble counts on the negative clock edge, and the table records this by showing the count occurring on the negative-going transition and no change on the positive one.[1208] That distinction can determine whether a given circuit configuration works as intended.[1208] Truth tables are also standard content in introductory electronics reference material, presented alongside the gate symbols themselves.[1163]
