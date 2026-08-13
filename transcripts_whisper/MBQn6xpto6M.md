---
video_id: MBQn6xpto6M
title: EEVblog #273 - Power Factor Correction with the MC34262
url: https://www.youtube.com/watch?v=MBQn6xpto6M
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 33, "2": 57, "3": 76, "4": 93, "5": 111, "6": 130, "7": 151, "8": 169, "9": 181, "10": 207, "11": 226, "12": 245, "13": 265, "14": 291, "15": 313, "16": 331, "17": 347, "18": 369, "19": 390, "20": 400, "21": 419, "22": 444, "23": 455, "24": 475, "25": 498, "26": 519, "27": 537, "28": 556}
---

**Dave Jones:** And let's take a look at the Motorola Slash-On Semiconductor. Sorry, still keeps calling the Motorola every time I see the old Motorola prefix of MC, but the MC34262 Power Factor controller. It's just an 8-pin DIP package, comes in SO as well. It's got a 2% internal

**Dave Jones:** bandgap reference, zero current detectors, quadrant multipliers and various other stuff. So let's take a look at the internal simplified block diagram here. As you can see, not a huge amount of circuitry in there. There's an internal bandgap voltage reference. That's an over-voltage comparator which comes from the voltage feedback which goes into an error

**Dave Jones:** amplifier. There's a compensation pin. The input for the multiplier is here. There's the output driver and there's a current sense input as well with the zero current detect input because it has to know when there's zero current. And we'll take a look at that

**Dave Jones:** and there's a power pin and that's pretty much it. There's not much else, but we'll see if we scroll down here and we go to typical configurations, we can actually have a look at, it's well worth reading this, it's got introduction and how a Power Factor correction

**Dave Jones:** system actually works. And we'll have a look at what happens if you don't have a Power Factor correction circuit. You've got the basic AC mains coming in here, full wave bridge rectifier as we saw in the schematic, and if the Power Factor correction circuitry wasn't

**Dave Jones:** there you've got the bulk storage capacitor. So full wave bridge rectifier straight into the storage capacitor generating a high voltage DC which then goes into your DC to DC converter which then powers your load. Now the problem with that is that looking at the waveforms

**Dave Jones:** here, you can see the AC line waveform here which is the dashed, the outer dashed one there, that's the ideal 50 hertz or 60 hertz mains input. And because the energy is stored in the bulk capacitors here, the voltage peak, you're only going to draw a current spike.

**Dave Jones:** So this waveform here, this spiky one here, is the current drawn during the peak period of the waveform. And that's quite, it's going to be a large current draw, so you're actually going to drag down the line voltage, the mains voltage, just a little bit, and it's going

**Dave Jones:** to sag as they say, as they call that line sag. And so you're going to get these current pulses at the positive and negative peaks at the mains input. And that's not very good at all for getting a Power Factor correction of one.

**Dave Jones:** And in fact they tell you here that this configuration can give you commonly a Power Factor ratio of 0.5 to 0.7, and that's not great at all. Now I don't think this is the place to actually get into a detailed discussion on how a Power Factor correction pre-converter works, a current mode one like

**Dave Jones:** we've got here. If you want to get the details of this, by all means download the data sheet, it'll be linked in in the notes there. So, but this is basically what we've got. We've added a PFC, Power Factor correction, pre-converter between the bridge rectifier and the bulk

**Dave Jones:** storage capacitor we had before, and the rest of the DC to DC converters are all the same. And of course you've got the high frequency bypass capacitor in here, and you would have noted that on the schematic for this model as well. But we're looking at the MC34362

**Dave Jones:** Power Factor correction pre-converter, and there's basically a series inductor here with a MOSFET pulling that down to ground, and an output diode. And you'll note that that is basically a boost converter. That's basically, that's exactly the same configuration as you get for a boost DC to DC converter.

**Dave Jones:** But the whole basic concept of it is, it's going to switch the MOSFET down here so that you get a half sinusoidal average current, basically drawn from your inductor current. So that's a series inductor, a series current through your inductor. You're going to have these peak values, but they're going to average

**Dave Jones:** out and smooth out over your AC mains, or half of your AC mains waveform like that. So instead of having just one big spike here like you would get without this Power Factor correction circuit in here, you get multiple spikes spread out over half of the sinusoidal

**Dave Jones:** waveform. And that averages out, and that improves your Power Factor correction. And if you take a look at the rest of it here, it tells you all about the different functional block diagrams inside the device. And I highly recommend you read it. It makes for some great

**Dave Jones:** bedtime reading. You've got the error amplifier, the multiplier, which is pretty much the key to how it all works. Overvoltage comparator, zero current detectors, current sets comparator and latch, how it all works, and it's great stuff. I highly recommend it. And bingo, down

**Dave Jones:** here we've got our design equations, and there's a whole bunch of them down here. You might have seen me go through similar equations like this before for DC to DC converter devices. And one of the problems with this is that, let's say you're trying to calculate the required

**Dave Jones:** converter output power. Well, what is that? Because this is a generic bench power supply. The user could be taking anywhere from zero output power right up to the maximum 600 watts or so. So really, these values are going to be all over the shop, and you have to design

**Dave Jones:** and do various trade-offs for various output powers and things like that. So maybe you would take it, you know, at the maximum output power, but you'd have to go through the formulas to see how much your power factor and other things traded off at lower output power.

**Dave Jones:** So you would have to go through the formulas. Be my guest. Great stuff to do at bedtime. I love it. And how the internal block diagram and the basic application circuit is down here. There's the MOSFET, there's the transformer, exactly how we see it there.

**Dave Jones:** And here's a typical table of some power factor controller test data. And we've got power factors of 0.999 down to 0.996, so it's going to be pretty close to 1. So these things work pretty well. If you take a brief look at the application circuit here, you can see the main inductor

**Dave Jones:** T here, but it's actually a transformer because it's got a secondary winding here that goes down to ground, and that taps, effectively allows you to tap off the output, read the output current, and that's exactly what happens on pin 5 here, which detects 0.

**Dave Jones:** Output current pin 8 is the VCC pin, so it just filters that there and powers the actual device. And pin 3 down here is our multiplier input, and you'll notice the, it's just a voltage divider here from the, directly from the rectified mains input.

**Dave Jones:** So that's reading, that's going to be reading the harmonics off there that come from the full wave bridge rectifier, and that goes in to the multiplier and the rest of the device. And there's our output driver which drives the MOSFET, which pulls that down to ground, once again through a current

**Dave Jones:** sense resistor there. So, that's basically all there is to it, and we see that it's got some typical waveforms here which is quite nice, and if you want to take a look, typical test things, error amplifiers, error output comp, current waveform spikes, suppression,

**Dave Jones:** all sorts of things. I highly recommend you download this, oh look at the old school layout, look at the old school taped layout there, I love that, brilliant. Geez, that'd be home anywhere in the 1970s. But it can't really be that old, nobody cared about power factor

**Dave Jones:** correction back in the 70s did they? Except for huge, maybe big industrial stuff or things like that, certainly not the bench power supply, lab power supply level I don't think. Anyway, I highly recommend you download this data sheet and print it out and have some good

**Dave Jones:** bedtime reading, it's most interesting.
