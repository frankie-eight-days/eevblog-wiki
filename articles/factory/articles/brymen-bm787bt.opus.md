# brymen bm787bt

The Brymen BM787BT is a handheld digital multimeter in Brymen's 780 series, distinguished from the rest of the line by an integrated Bluetooth Low Energy link to a phone app.[TkmMitYnHUA] Mechanically and functionally it is the BM786 with Bluetooth added, and it is also sold in an EEVblog-branded version.[TkmMitYnHUA] The model exists as the delivered form of a design Brymen first committed to roughly five years before it shipped, the BM786 having been on sale since 2020 and the BM787BT arriving in 2025.[TkmMitYnHUA]

## Model numbering and the low-impedance function

The meter is not called the BM786BT because it is not simply a BM786 with a radio in it. A low-impedance measurement function, absent from the BM786, was added at Dave Jones's request during development, and Brymen took the position that a functional change of that kind required a new model number rather than a suffix on the old one.[TkmMitYnHUA] The result is the 787 designation, with the 788 and 789 occupying adjacent positions in the same family.[TkmMitYnHUA]

Bluetooth in this family is not new to the 787; the BM786 already carried Bluetooth hardware located in the rear of the case.[TkmMitYnHUA]

## Bluetooth module and firmware

The BLE radio is a discrete, physically replaceable module inside the meter rather than a soldered-down part of the main board, and it carries its own firmware revision independent of the meter's measurement firmware.[Q_RYG_5cQk8] During app development the module went from version 1.2 to version 1.3, and the fix was delivered as a new pre-programmed module swapped into an existing meter rather than as a field firmware update.[Q_RYG_5cQk8] This makes the radio firmware a separate variable when diagnosing app problems: an app fault may be a module revision issue rather than an application bug.[Q_RYG_5cQk8]

## Pairing and the app

The meter does not pair through the host operating system's normal Bluetooth settings; attempting to do so fails, and the connection is instead established from inside the app's own device scan.[ruxzp0OMicg] The scan lists discovered meters with a signal-level figure in dB, which tracks distance directly — around −55 with the meter on the bench, falling to about −78 with it placed underneath.[ruxzp0OMicg] Connecting then requires entering a connection password, for which there is a factory default.[ruxzp0OMicg]

Once connected, a device can be renamed and its stored pairing removed from the app.[Q_RYG_5cQk8] Multiple meters can be connected at the same time, given distinct names, and logged as separate channels in one session.[Q_RYG_5cQk8]

The app's chart-recorder mode plots the live reading and duplicates the numeric value above the trace, and a logging session can be exported as CSV.[ruxzp0OMicg] The device-selection step is a known rough edge: the app requires an explicit device selection even when only one meter is available, which should default to the sole candidate instead.[ruxzp0OMicg] For a chart recorder the display should also be able to flip orientation, since horizontal resolution is what matters when reading a trace.[ruxzp0OMicg]

## Pre-release hardware

Early units circulated as pilot production rather than prototypes — electrically representative, but without the finished cosmetic treatment: no blue silkscreen on the case and no blue overmoulded outer.[TkmMitYnHUA]
