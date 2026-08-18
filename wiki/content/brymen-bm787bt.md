---
title: brymen bm787bt
tags:
  - tool-equipment
writer: opus
---

<aside class="ib"><div class="ib-h">brymen bm787bt</div><table><tbody><tr><td>Videos</td><td>4</td></tr><tr><td>Mentions</td><td>52</td></tr><tr><td>Explained in</td><td>45</td></tr><tr><td>Sources cited</td><td>3</td></tr><tr><td>Type</td><td>tool-equipment</td></tr></tbody></table></aside>


The Brymen BM787BT is a handheld [[digital-multimeter|digital multimeter]] in Brymen's 780 series, distinguished from the rest of the line by an integrated [[bluetooth|Bluetooth]] Low Energy link to a phone app.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup> Mechanically and functionally it is the BM786 with Bluetooth added, and it is also sold in an EEVblog-branded version.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup> The model exists as the delivered form of a design Brymen first committed to roughly five years before it shipped, the BM786 having been on sale since 2020 and the BM787BT arriving in 2025.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup>

## Model numbering and the low-impedance function

The meter is not called the BM786BT because it is not simply a BM786 with a radio in it. A low-[[impedance]] measurement function, absent from the BM786, was added at Dave Jones's request during development, and Brymen took the position that a functional change of that kind required a new model number rather than a suffix on the old one.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup> The result is the 787 designation, with the 788 and 789 occupying adjacent positions in the same family.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup>

Bluetooth in this family is not new to the 787; the BM786 already carried Bluetooth hardware located in the rear of the case.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup>

## Bluetooth module and firmware

The BLE radio is a discrete, physically replaceable module inside the meter rather than a soldered-down part of the main board, and it carries its own [[firmware]] revision independent of the meter's measurement firmware.<sup class="cite"><a href="#src-Q_RYG_5cQk8" title="Brymen BM787BT BLE Module Replacement">•</a></sup> During app development the module went from version 1.2 to version 1.3, and the fix was delivered as a new pre-programmed module swapped into an existing meter rather than as a [[firmware-update|field firmware update]].<sup class="cite"><a href="#src-Q_RYG_5cQk8" title="Brymen BM787BT BLE Module Replacement">•</a></sup> This makes the radio firmware a separate variable when diagnosing app problems: an app fault may be a module revision issue rather than an application bug.<sup class="cite"><a href="#src-Q_RYG_5cQk8" title="Brymen BM787BT BLE Module Replacement">•</a></sup>

## Pairing and the app

The meter does not pair through the host operating system's normal Bluetooth settings; attempting to do so fails, and the connection is instead established from inside the app's own device scan.<sup class="cite"><a href="#src-ruxzp0OMicg" title="Brymen BM787BT Bluetooth App First Impressions">•</a></sup> The scan lists discovered meters with a signal-level figure in dB, which tracks distance directly — around −55 with the meter on the bench, falling to about −78 with it placed underneath.<sup class="cite"><a href="#src-ruxzp0OMicg" title="Brymen BM787BT Bluetooth App First Impressions">•</a></sup> Connecting then requires entering a connection password, for which there is a factory default.<sup class="cite"><a href="#src-ruxzp0OMicg" title="Brymen BM787BT Bluetooth App First Impressions">•</a></sup>

Once connected, a device can be renamed and its stored pairing removed from the app.<sup class="cite"><a href="#src-Q_RYG_5cQk8" title="Brymen BM787BT BLE Module Replacement">•</a></sup> Multiple meters can be connected at the same time, given distinct names, and logged as separate channels in one session.<sup class="cite"><a href="#src-Q_RYG_5cQk8" title="Brymen BM787BT BLE Module Replacement">•</a></sup>

The app's chart-recorder mode plots the live reading and duplicates the numeric value above the trace, and a logging session can be exported as CSV.<sup class="cite"><a href="#src-ruxzp0OMicg" title="Brymen BM787BT Bluetooth App First Impressions">•</a></sup> The device-selection step is a known rough edge: the app requires an explicit device selection even when only one meter is available, which should default to the sole candidate instead.<sup class="cite"><a href="#src-ruxzp0OMicg" title="Brymen BM787BT Bluetooth App First Impressions">•</a></sup> For a chart recorder the display should also be able to flip orientation, since horizontal resolution is what matters when reading a trace.<sup class="cite"><a href="#src-ruxzp0OMicg" title="Brymen BM787BT Bluetooth App First Impressions">•</a></sup>

## Pre-release hardware

Early units circulated as pilot production rather than prototypes — electrically representative, but without the finished cosmetic treatment: no blue [[silkscreen]] on the case and no blue overmoulded outer.<sup class="cite"><a href="#src-TkmMitYnHUA" title="New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)">•</a></sup>


## Sources

<table class="srcs"><tbody>
<tr id="src-TkmMitYnHUA"><td class="n">&mdash;</td><td><a href="/transcripts/t/TkmMitYnHUA#p195">New Brymen BM787BT Bluetooth Multimeter Teardown (Live Recorded)</a></td><td class="y"><a href="https://www.youtube.com/watch?v=TkmMitYnHUA&amp;t=2032s" target="_blank" rel="noopener">watch</a></td></tr>
<tr id="src-Q_RYG_5cQk8"><td class="n">&mdash;</td><td><a href="/transcripts/t/Q_RYG_5cQk8#p46">Brymen BM787BT BLE Module Replacement</a></td><td class="y"><a href="https://www.youtube.com/watch?v=Q_RYG_5cQk8&amp;t=663s" target="_blank" rel="noopener">watch</a></td></tr>
<tr id="src-ruxzp0OMicg"><td class="n">&mdash;</td><td><a href="/transcripts/t/ruxzp0OMicg#p0">Brymen BM787BT Bluetooth App First Impressions</a></td><td class="y"><a href="https://www.youtube.com/watch?v=ruxzp0OMicg&amp;t=0s" target="_blank" rel="noopener">watch</a></td></tr>
</tbody></table>
