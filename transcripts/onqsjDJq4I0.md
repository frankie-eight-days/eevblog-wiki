---
video_id: onqsjDJq4I0
title: EEVblog #210 - Krohn-Hite DC Voltage Standard Teardown & Calibration
url: https://www.youtube.com/watch?v=onqsjDJq4I0
source: youtube-asr
---

**Dave Jones:** Hi, check out what just turned up on my bench. Whoa, look at that. Isn't it beautiful? It's a electronic development corporation MV106J DC voltage standard. Look at all the knobs. I love it. Precision City. It's awesome. It's now done. I think it's it's owned

**Dave Jones:** by a company now called Kron Hyde. They still sell it. It's still a current model and I thought we'd turn it on, check it out, see if it still works, calibrate it, look at how it works, internal construction,

**Dave Jones:** teardown, bit of theory maybe, and should be fun. Let's go. And here it is. It comes in a rather old style aluminum rack size cabinet. It's got a It's got a little aluminum tilting bail like this, but it's also got

**Dave Jones:** another flip out tilting bail like that, which is really quite nice. I like it. And it's in fairly good nick. I'm not sure how old it is. I think it's the manual which you can download says it's 19 or

**Dave Jones:** last updated 1991 and 2001, sorry. So, it's like a 10-year-old model, but it could be based on older than that cuz it seems quite old-school with the with the old style rotary encoder knobs, but maybe it's been updated or something

**Dave Jones:** like that. I'm not sure. Full scale of 10 volts or 100 millivolts or 10 millivolts. There's three ranges. There are There is another type which has a current output as well, but this one doesn't now. The cal sticker here, if

**Dave Jones:** you take a look at that, it's last caled in 2000 and well, 2007, so due 2008 and made in Boston, Massachusetts. Do they still make anything in Boston anymore? I don't know. Um I think they are. I'm sure there's a few

**Dave Jones:** things made there. Anyway, uh uh, yeah, I quite like it. It's got um, the sense outputs as well cuz when you're talking about a precision DC instrument like this, it's got a sense the outputs, but it does have little shorting

**Dave Jones:** bridging bars in there. If you're just hooking it up to a voltmeter, then that's fine. You don't need the sense outputs. They can just be tapped directly off the output and you can just use a two-wire instead of four-wire. You

**Dave Jones:** can invert the output. Uh, nothing unusual there. And but I love it's got six decades here and I love these style rotary selection knobs and you'll notice I'm quite a fan of those. I've got quite a few of the Keithley instruments there.

**Dave Jones:** I've actually got four of those and I just love those style knobs. So, I love this thing. It's brilliant. And of course, you can set, let's say we've got 10 V full scale here. You can set 10.0001 V.

**Dave Jones:** That's the resolution of it. Beautiful. It's 10 microvolts resolution on the 10 V range, but if you go down to the 10 mV range, we're talking 10 nanovolt resolution. Wow. Nothing exciting on the back, I'm afraid. Just the model number

**Dave Jones:** and a 240 V selection and switch. So, it was 110. Switched it over to 240 and we'll see if this sucker works. All right, we'll just try it with my Fluke 87 here first. As I said, we've got the

**Dave Jones:** current sensing which shorted with the current bars there. Ideally, if you had a a big load, you would actually take the sense directly onto the load point itself for absolute accuracy, but in this case, it's going to be more than

**Dave Jones:** good enough. So, let's switch it on and see what happens. Let's put it to 10 V and Hey, it lights up. Overload. And uh, Yep, the overload LED is still on. Oh, no, there we go. It's gone out. Looks

**Dave Jones:** like it uh requires some settling time, perhaps. Um and bingo, there we go. 10.0000 V and we're pretty darn spot on to almost to the least significant digit there. So, it looks like it uh works. Let's change it to 100 mV there.

**Dave Jones:** And ah, beautiful. Look at that. 100.00 Spot on. And uh let's We've got 100.00. Well, let's whack the this up one notch. That should give us one least significant digit. And it does. There we go. Changing one at a

**Dave Jones:** time. Wow, it's spot on. And of course, we've got two decades below that, which won't do a damn thing. But if we turn that up by 10, it should jump to eight. And it does. There we go. So, it looks like it's um it's going to

**Dave Jones:** still be Well, I'm not going to say within spec. It's within um you know, the .05% of my uh Fluke 87 here. But uh this thing has specs of uh What are they? Um uh .003 uh or uh 30 uh 30 30 ppm over the

**Dave Jones:** temperature range. Now, this thing actually has um specs of uh plus minus .003% or 30 uh ppm over um well, the the span of a year. Um and uh point uh .0005% or five uh ppm uh per degree C temperature

**Dave Jones:** drift. So, it's not super high-end as far as uh DC uh standards go, but it's not too bad at all. It'll be a nice addition to the lab here, I think, just for a a precision voltage source for uh

**Dave Jones:** testing meters and things like that. But it seems to work just fine. That's the mV range. And we go down 10 mV range. Yep. Not a problem at all. I like it. It's nice, and there doesn't seem to be

**Dave Jones:** any noise on the pots, either. With these things, you've got to sort of if you jiggle the jiggle the pots a bit, you can often see if there's any issues there, but I can't see any problems there at all. So, it seems

**Dave Jones:** to be working just fine. And we'll try the negative on there. And no, it's within, you know, that's pretty darn close, so that's not too bad at all. So, I determine that this sucker is pretty much still within

**Dave Jones:** spec. Well, I'm not going to say within spec because it's, you know, only within pretty, you know, it's pretty close to meet to actually check its performance spec. It's going to need better gear than what I've got here,

**Dave Jones:** which will which is what we'll have to do later, but it basically works. So, I'm pretty darn happy with that. Now, I could check the linearity of it and things like that, but generally with these sort of things, you don't have to

**Dave Jones:** because the linearity is set by by precision voltage divider resistors set up with these pots even in a Kelvin or more more popular format is the Kelvin Valley configuration. So, basically these things shouldn't drift unless those actual resistors drift, which generally

**Dave Jones:** doesn't happen too often. It's more likely that the voltage reference diode in there would drift or something like that, but even those are pretty darn stable. So, I'm not surprised that this thing still works cuz there's not much in them to go wrong. We'll find

**Dave Jones:** that there's only a power supply in there, a reference diode, an amplifier, and a bunch of bunch of precision resistors on these knobs here. Let's go one step further than the Fluke 87, shall we? And get my HP 3478A

**Dave Jones:** bench meter, which is actually got a going to have a similar short-term drift capability to this DC voltage standard. And we've got it set to 10.00000 there, and it's not too far off at all. But I haven't checked the cal in this in

**Dave Jones:** quite some time. And of course, you know, there they have to come up to the same temperature. And well, it's a bit warm today here in the lab. It's probably 25, 26° maybe even 27° C in the lab here. So, you know, it's not exactly

**Dave Jones:** ideal calibration conditions, but we'll fix that later. Now, let's uh go down 100 mV. There you go. That's not That's not too shabby at all. Let's go down to 10 mV. And once again, not too shabby. I don't mind it at all. So, um

**Dave Jones:** it might need Well, see, we don't know which one's out. We don't know whether my 3478A is out or this is out or a combination of both or whatever. Um I'll have to take it to a standards cal lab

**Dave Jones:** to find that out. But if we can calibrate this baby, um then we can use that as a transfer standard to then calibrate um my 3478A. That'd be neat. All right, let's open this sucker up and see what we got

**Dave Jones:** inside. Now, as I said, what you're going to find that you'll get in here, this will be my guess, and I think I'm going to be pretty accurate, is that you'll find in like an old-school PCB with all through-hole components.

**Dave Jones:** Obviously, you'll have a power supply, um mains power supply. You'll have a precision um voltage reference, which will be like a zener or you know, a buried reference zener um temperature temperature-controlled. And it'll have a Kelvin-Varley divider um, the front and an amplifier. And

**Dave Jones:** that's pretty much all it is. It says it's got a chopper amp. I don't have the full manual yet, but, um, I've asked for it, so that should, uh, turn up shortly, I hope. And let's pull it off and see what we get.

**Dave Jones:** Okay, all is off, yep. Hey! There we go. And that's NOT TOO FAR off at all. It's pretty much what I expected. Now, uh, one of the first things I, uh, noticed though, is that, um, quite possibly, uh, this doesn't

**Dave Jones:** look like a Kelvin-Varley, uh, voltage divider arrangement. It just looks like a standard, uh, Kelvin voltage divider. And the giveaway there is that there appears to only be a single link between each, uh, decade bank there, not a jewel link, as you'd,

**Dave Jones:** uh, expect on a more complicated, uh, switch arrangement, as you'd expect on a Kelvin-Varley, which is, uh, what you'll find in my, uh, Keithley, um, instruments over here. They use, uh, Kelvin-Varley, uh, dividers in them. But this one looks like it just uses

**Dave Jones:** standard Kelvin divider. We'll have to get the schematic to verify that, but there you go. Anyway, it's a whole bunch of, uh, very precise resistors on there. We'll have to check out the values. Some, uh, trim pots over here on the

**Dave Jones:** main decade. That's your, um, that's your first decade there, and it looks like it's got um, trim pots for all the various ranges. You've got a main board, uh, down here, and you've got a mains transformer. Now, one of the interesting

**Dave Jones:** things to note about the mains transformer here is look at all the exposed wire in here. It's, um, it there's no heat shrink in, uh, on that at all. It's all totally exposed, as is the, uh, switch on the main switch on

**Dave Jones:** the front panel. And that pretty that, uh, you wouldn't get that, uh, past these days, but, um, yeah, it's, uh, pass pass the safety standards anyway. And and you'll see down here, this is the mains cable input and there's like

**Dave Jones:** an insulated uh stand off there, which is just used to join the two wires. And once again, fully exposed. So, um there's not really much uh put into the um you know, internal uh safety of this instrument. But uh that's, you know,

**Dave Jones:** typical old school stuff. And your output jack's over there. Uh they've got uh gold plated, you know, they'd be really good quality uh gold plated uh contacts and things like that. Crimps and uh going off the uh wire ends are uh

**Dave Jones:** reasonably neat and tidy, I guess. As for holding the uh PCB in place here, this is uh very old school construction technique. They've got the um aluminum uh plate with the cutout for the board and the board uh screwed on the

**Dave Jones:** underside there and they've just cut it out for the uh components. Um uh quite uh you'll see this construction method uh used quite a lot in these sort of uh rack mount um early early designed instruments. Now, one of the first

**Dave Jones:** things I I'm looking for in something like this is where is the uh voltage reference standard. Now, I've got this curious looking uh package here and um but I don't think that is the voltage reference. I get a feeling

**Dave Jones:** that that's not it. I'm not actually sure what that is as well and and at all. It's got two uh common terminals here. It's just a four terminal device, two pins on either side. There's an in, there's an out. Um but that's not what

**Dave Jones:** you'd expect in a uh temperature compensated uh buried Zener reference like um in the um HP 3478A multimeter we just uh had had a look at. It's got an LM uh 299 temperature compensated voltage reference in it. And

**Dave Jones:** that's basically just a bend it and buried Zener diode that isn't very very precise at all. And we'll go into this later, but it keeps it at a constant temperature. And I don't see So I if that was the

**Dave Jones:** voltage reference, I'd expect to see a a heater connection on there, not just in and out. I'd expect to see you know, just the diode connection on one side and the heater on the other, but that's not it. Um

**Dave Jones:** but looking down here, they've got the reference down here and that looks like it might be the reference diode. Let's go check that out. There you go. It's got ADC reference diode 4593 at 6.1730 V at 6.5 mA current. So

**Dave Jones:** obviously they've And because that that diode is in those like soldered after after this thing's assembled into those little contacts there, I reckon that is the reference diode for that thing. So I'm very surprised that it's not temperature compensated. I fully

**Dave Jones:** expected a temperature, you know, with point double 0 What is it? Double 0 double 0 5 or 5 parts per million temperature coefficient. Without getting that without temperature compensation on it, that must be one hell of a good diode. So we're going to

**Dave Jones:** have to wait until we get the manual for that and see what part number it is. Now I've turned the power on and let's see if we can actually measure that diode down in there. And if I'm correct, it

**Dave Jones:** should be 6.1730 V. So let's give it a go. Bingo. 6.173 V it is. Now as for the rest of the board here, there's no uh silk screen at all. Somebody's handwritten, you know, R4, R3, R2A, R2, R1 there.

**Dave Jones:** No silk screen, really old uh through-hole uh kind of stuff. And uh these voltage regulators here, look at the check out the pins. The spacing is not even on them. They've had to splay those pins out. That's, you know, that's

**Dave Jones:** a bit bodgy. I don't like that at all. And we've got a date code on this um LM741 here of uh the fourth week '91. So, there you go. That uh dates this unit to uh at least uh 1991. Now, of

**Dave Jones:** course, one of the things you notice here is this uh little daughter board here. Um and I am I'm going to assume that that's the uh chopper uh amplifier, cuz they talk about that in the manual. So, but it almost looks like it's a

**Dave Jones:** bodged afterthought. Like they had to add it on, but if you actually wiggle it here, it will it should looks like it will pop out. And Ta-da! There we go. Look at that. That is it looks like they've purpose designed

**Dave Jones:** that. Um it was actually designed. I thought it looked like a bodged board, but it's not. It looks like they actually uh manufactured that module um as a separate thing. They probably manufacture and uh test it. I mean,

**Dave Jones:** there's no uh trim pots on there, but maybe they um you know, they test things they actually select the components and uh put them on there or something. But yeah, it's all it's all very uh it's all very old school. And uh I'm

**Dave Jones:** quite surprised at the whole thing. No Kelvin Valley at the impreciseness, really, um of the whole thing. You know, they're not using a temperature compensated uh reference diode down here. They're not using a Kelvin Valley divider. But hey, I you know, they've

**Dave Jones:** they've got away it. It I'm sure it uh will meet its claim specs. And you can see the precision resistors on the decade switches there. That's a 2K plus minus 0.005% precision resistor. And as you go they won't all be that precise, but all the

**Dave Jones:** ones over there will be like the ones further down. You know, they don't have to be as precise. Not necessarily as you go down, but at least some of them are at least 0.005% and the ones down here on the first

**Dave Jones:** decade here, these are at 0.02%. They don't have to be as precise because each one of those is trimmed to its actual value. Actually, I just looked up that part number the TSC7652 there. That is actually a chopper

**Dave Jones:** stabilized amp. So, there you go. And I've talked about chopper stabilized amps before. The reason you're going to use one of those in an instrument like this is that it has essentially it zeros out it nulls out any DC offset errors.

**Dave Jones:** And this is a DC precision reference. So, what don't you want in this? You don't want any DC offset errors. Bingo, you got to use a chopper stabilized amp for that. And thanks to Joe Engles from Chronhite, we've got the schematic for

**Dave Jones:** it in record time. And what can best be described as the manual. It's a bit of a hotchpotch actually the manual bit. We do have the schematic. I'm not sure if it's actually this is all they had. The model I've got is the MV106J. This

**Dave Jones:** just says MV106. I'm not sure what's actually going on there, but anyway, it's pretty much what I expected apart from the Kelvin Valley thing and the temperature control Zener. So, let's actually take a look at it here. We've

**Dave Jones:** got over on the left side here. We've got our We've got our supply rails up here, and we've got bingo, a constant current generator, which you have to Here's the obviously the Zener reference diode here, and it because to get a constant

**Dave Jones:** voltage out of a high precision high stability Zener Not high precision, but high stability. Go into that later. Zener diode, then you need a constant known current through it. So, that's what this is designed. It's got an adjustment pot

**Dave Jones:** there, and you tweak the voltage you tweak the current through the diode until you get the exact voltage you want, and then in theory, it should just start stay like that based on the temperature stability of the diode will be the main

**Dave Jones:** contributing factor to the drift of this absolute reference. So, there's our voltage reference here. So, a constant known current flowing, which is inside it's actually labeled as 6.5 milliamps. So, that you adjust that pot there, which is pot number one, and

**Dave Jones:** they've labeled it pot number one on the board, too. So, that's handy. Um So, we've got pot number one, 6.5 milliamps through that Zener, which gives that measured voltage drop, which is saw written on handwritten on the label inside the unit. So, that's where

**Dave Jones:** all the stability comes from. Bit of bypassing across it there, and then we've got our um We've got our decade resistor networks. There's the first decade there. Once again, it shows all those trim pots we saw on that board, if you remember. And

**Dave Jones:** then once again, it's This is the next decade, then the next decade. And as you can see, they do go down in steps. 20 K, 2 K, 200 ohms, 20 ohms, 2 ohms, and 0.2 ohms. So, there you got your six

**Dave Jones:** decades. And as you can see, because it's not a precision a real precision Kelvin Valley divider, it's just a standard Kelvin divider, then you need these little trimmer we've got little trimmer resistors here for the various ranges to just allow you to tweak the values

**Dave Jones:** there and it's not the best drawn all these range switches are quite complicated and convoluted but pretty much the operation is pretty simple. There's our overload indicator down here. It's just a comparator and LM 741 which then drives the overload lamp

**Dave Jones:** here and here's our chopper amp. So it's basically just a negative feedback zero offset chopper amp based the gain of which is based on the based on the feedback here. So it's it's pretty darn simple and of course there's a driver that they've got

**Dave Jones:** an emitter follower driver here which drives the output but apart from that it's it's fairly simplistic really and it you know, it's obviously good enough for the job if you tweak things and and you design it properly so that it's low

**Dave Jones:** drift. Well, it works a treat. And here's your output resistors down here and as in the manual it match. Basically it's got a 3K output impedance on the 10 millivolt range and then the 100 millivolt range is got a 300 ohm output impedance and

**Dave Jones:** then 3 ohm output impedance on the 10 volt range there. And if you grossly simplify this circuit you end up with nothing more than a simple inverting amplifier here with a very low drift precision buried Zener reference with a constant

**Dave Jones:** current source and as you can see the gain doesn't need to be very high because you've already got 6 volts here for the Zener and our maximum output is only 10 volts. So you only you know, you don't even need a gain of two here

**Dave Jones:** total. So effectively what you're doing is using this as a precision divider and then these are these are your six decade knobs on the front like that and of course I've left out all the little trimmer things and stuff like that to

**Dave Jones:** actually calibrate the thing. I've left out the the emitter follower driver and stuff like that and the sense circuits. This isn't actually grounded here but basically that is pretty MUCH WHAT WE'VE GOT IN HERE. It's very very simplistic

**Dave Jones:** in its basic operation but that's all it needs to be. What exactly is a Kelvin Valley divider I've been talking about? Well, we have to start at the Kelvin divider. Now, you've seen this before. In fact, it is what you know as a

**Dave Jones:** voltage divider, what most people call a voltage divider but it's its real name is actually a Kelvin divider named after Lord Kelvin, obviously you're probably familiar with. Now, uh this is what the what is used in this instrument here. You have this is one

**Dave Jones:** decade, okay? You have a string of 10 resistors like this and you tap off the various voltage that you need. And that's fine if it's just one decade. It's fine and dandy. These could be nice high values like 10k or something like

**Dave Jones:** that. Now, when you get to a multi-decade device though like on this one, this one's got seven decades as you saw and uh really when you get to that point you can actually when you put them in series

**Dave Jones:** you would have another one here which effectively just short actually shorts it out. So, then you put multiple ones of these in series, okay? You would have one of these for each decade. So, you'd have 10 resistors for each decade and

**Dave Jones:** then they short out etc. etc. But the problem with this as you saw in the schematic for this thing is that each decade must get progressively smaller in value by 10 times in order 1/10 in order of magnitude, okay? So, we've got the

**Dave Jones:** our first decade up here is 20k, then it's 2k, then it's 200 ohms, 20 ohms, 2 ohms, point 0.2 ohms. Now, you think, "Okay, what's the big deal?" But, uh-huh, think about it. These are all mechanical switches in here. They all

**Dave Jones:** have, uh you know, dirty contacts and, you know, and they bounce around and do all sorts of funny things. And they're going to have a certain contact resistance, a certain minimum contact resistance. And really, if you uh you know, you don't want to

**Dave Jones:** start off with too high a value cuz then your thermal noise is too high and all sorts of stuff. So, uh but when you progress down like that, down to 0.2 ohms, you're right down in the territory of the contact resistance

**Dave Jones:** of all these switches. And it's not just this decade, but all of these other ones that you've got in series like this. Now, you can, of course, make this uh work as you can see in this instrument. Yeah, you know, but it's a lot of

**Dave Jones:** fiddling around, a lot of other adjustment pots you got to have, a lot of mucking around. And uh if you've got dodgy uh contacts or contacts that uh increase in resistance with time or wear or whatever, then you're going to end up

**Dave Jones:** with all sorts of problems. So, it's really not an ideal solution. And that's why lots of uh precision instruments will use a Kelvin-Varley divider. So, let's take a look at that one. So, to get around this problem, a clever dude

**Dave Jones:** named Varley know his first name. I don't know. I've never bothered to look it up, but it's known as a Kelvin-Varley divider. And uh it's, once again, it's a multiple decade uh system, as we'll see, but it doesn't use progressively lower

**Dave Jones:** value resistors. Or it does, but nowhere near the order of uh magnitude drop for each decade that we saw on the Kelvin divider. Now, um this is actually the internal schematic of an um a very high precision IET brand KVD 700 Kelvin Valley voltage

**Dave Jones:** divider. And you can actually it's in a box, you can actually go buy it and they're really very high precision laboratory grade bits of kit for voltage division. Now, as you can see this is a seven decade one. So, it has 0.1 ppm resolution.

**Dave Jones:** Absolutely incredible. That's one decade more than what we've got on our voltage standard that we're playing with here today. Now, as you can see each decade, if you count up those resistance, it doesn't have 10 of them. It actually has

**Dave Jones:** 11. And that's one of the keys to this thing. Now, as you can see it won't also have just a single um a a single wiper contact coming off here. It will actually have two coming off. There's two contacts like that that

**Dave Jones:** actually move in uh parallel like that up and down. Now, the key to this is that because you've got 11 11 resistors here, okay? And you've got the contacts on on uh a second contact point one over like

**Dave Jones:** that, then the rest of this all of the rest of these resistors on the next decade, including this resistor here and this one and all the rest of them cascaded through seven paralleled up through seven decades like that, is

**Dave Jones:** actually uh equal to um 20K, which then when it's put in parallel with in this case the two 10K resistors here forms a 10K resistor. So, those 11 resistors actually drop down to 10. So, you're tapping off 1/10 of the voltage

**Dave Jones:** at that point. And that's the clever part about it. And likewise, it cascades through the system like that. These two wiper arms here move up in unison like that. So, if they're up here, you would find that the wiper arm would be there

**Dave Jones:** and there for example, or right down the bottom, it'll be there and there. And you can tap off the same exactly the same as the Kelvin divider we saw. Tap off one or dial up 1/10 for each decade a value of one right

**Dave Jones:** down to in this case seven decades 0.1 ppm resolution. But, look at this. The lowest value resistor in here is only 1 K. So, it's nowhere near the switch contact resistance that's going to cause an issue. So, you can get

**Dave Jones:** and you don't have to trim anything. So, you can actually manufacture this thing and not really worry too much about your contact resistance at all as you would in a traditional Kelvin voltage divider. So, there you go. That's And you can go

**Dave Jones:** through and you can actually do the math of what values you need to put in in parallel here. There's a 25 K there and 40 K there. And there's various configurations of it as well as as well as on the output as well. It might have

**Dave Jones:** another divider on the output here which will then tap off. There's various slightly little different configurations of it, but that's basically how a Kelvin Valley voltage divider works. Very obscure, but very very useful. Now, let's take a look at the specs for this

**Dave Jones:** unit, shall we? It has an absolute voltage accuracy on the 10-V range of 0.003%. That's actually If you convert it, that's actually 30 ppm of the setting of the actual setting you got. So, if you got If you got 10 V

**Dave Jones:** dialed in, it's going to be 30 ppm of that absolute accuracy. But, you've got to add on another five ppm here. Basically, the difference between percentages and PPMs is once once you get below about you know 0.01% you just it's bit of an industry

**Dave Jones:** standard to start talking in terms of PPM, parts per million, instead of percentages. They're exactly equivalent, but you know, it's just industry speak really. You're going to once you get into small stuff, you know, it's it's a bit more

**Dave Jones:** bit bit more professional to talk in terms of PPM cuz it it sounds more impressive and it's easier to work with than, you know, throwing in X number of zeros and things like that. Now, we also have to add on two microvolts and we

**Dave Jones:** have to do the math to figure out what that's actually going to be. And that's 5 PPM of the actual range and the range of course down here is the full scale range of 11.111 V. So, if you work those out

**Dave Jones:** 30 PPM of the setting, in this case we might use a 10 V and then we would have 300 microvolts absolute error there plus we have to add on 55.5 microvolts because the percentage error of the range plus two

**Dave Jones:** microvolts a total of 300 and 57 odd microvolts. But one of the keys to something like this is the stability and it's going to good quality instruments will give you different stability over different periods. In this case it's giving you

**Dave Jones:** over a one day eight hour period of plus minus 0.01% or 10 PPM stability. So, it won't drift any more than that over a period of eight hours and over the period of a year it's still fairly tight at 25 PPM.

**Dave Jones:** Once again, plus two microvolts. And even for the 10 mV range down here it's actually identical 0.003% or 0.0035% basically plus the two microvolts. Now, that for 10 mV range that's going to be 10.00037 mV. So, coming back to our unit here, if

**Dave Jones:** we've got it set to our 10 V range here, then that means it's going to be 10.00037 or plus minus 37. That is its absolute value. So, when you calibrate this thing, that's all it's guaranteed to be. So, these last

**Dave Jones:** two digits, especially the last one, you're really getting down into the noise. Effectively, you almost say it's not quite useless because from an absolute accuracy point of view it is, but because you can actually dial it in there, its resolution can be handy. And

**Dave Jones:** as we've talked about before, that's the difference between accuracy and resolution. Just because your accuracy is not the same as your resolution, doesn't mean the resolution isn't useful for various purposes. And the other thing of vital importance is the

**Dave Jones:** temperature coefficient here, and it's plus minus 0.0005% per degree Celsius. And if you translate that over to our dials here, it's 0.00005% per degree Celsius change. So, if if you're sitting in a lab and your temperature changes by 1 degree, you've

**Dave Jones:** effectively dialed an extra five onto that digit there. But, that's going to be a maximum worst case value. It's most likely in practice going to be better than that, substantially better. But, as always in electronics, you should take, especially

**Dave Jones:** when you're doing precision stuff and really serious work, you've got to take take that worst case spec. Now, if you're curious to know what reference diode is used in this thing, I looked up the parts list for it, and it's actually

**Dave Jones:** a 1 in 821 A A U device. Now, it's available from different manufacturers. I don't know which manufacturer is the one used in here. It's most likely not a microsemi, but this was the best data sheet I could

**Dave Jones:** find for an equivalent second sourced part. Now, as you'll see down here, this is 0. There it is. 0.0005% per degree C. And you probably recognize that because that is the temperature coefficient spec of this actual unit. It's based purely upon the reference

**Dave Jones:** diode, as you'd expect. Now, one of the curious things that might puzzle a lot of people with something like this is that look at the reference value. It's plus minus 5%. It's got a huge tolerance. And that is the difference

**Dave Jones:** between absolute accuracy and temperature coefficient. Over here, you can design a high precision instrument like this. High precision, high stability using a plus minus 5% reference diode because you because you're not relying on the factory or the you know, the actual manufactured

**Dave Jones:** absolute tolerance of this thing because you calibrate it. You tweak those knobs. You dial it in. All you care about is the stability of it. So, what with temperature because and and age as well as another thing, but let's not go there, but let's just

**Dave Jones:** talk about temperature itself. That's all you care about. As long as you've got a very low temp co, what is what's called a temp co or temperature coefficient reference device in there. In this case, it's a zener temperature compensated

**Dave Jones:** diode. Then as long as this figure is really really low, you can and you keep that diode at the same temperature or it's so low that it doesn't matter, then you can just tweak your circuit, adjust it, and bingo, you've got a high

**Dave Jones:** precision, high stability circuit. But, the problem is, you've got to actually have access to a you know, some sort of you know, secondary or cal lab standard equipment to do the calibration in the first place. But, if you've got that, as any good

**Dave Jones:** manufacturer does, then you can do it. Not a problem. And if you're wondering what reference is used in the legendary HP 3478A multimeter we've we used before, industry standard bit of kit, it uses an off-the-shelf reference diode. In this case, it's the which you

**Dave Jones:** can't get anymore, it's been obsoleted, but it's the LM299. And basically, all it is is, once again, as I mentioned, it's a Zener diode in there. It's a buried reference, very high stability Zener diode, just like the micro 71 used in here, except it's

**Dave Jones:** got a little internal heater inside the package, which keeps it and it's got some regulation circuitry for the heater in there, that keeps it at a constant temperature. So, if you've got it at a constant temperature and you've got a

**Dave Jones:** constant current flowing through your diode, not a problem. It's going to be very, very high stability. And let's look at the spec. There it is, plus minus at 2%, right? It's horrible. That's the initial tolerance of this thing you buy it, and it can be 2% out.

**Dave Jones:** It's useless, right? You can't use that in a precision five-digit multimeter, it's hopeless. Aha, but look at the temperature coefficient, 0.0001% or 1 ppm per degree Celsius. Fantastic. So, as long as you calibrate and tweak this thing, it'll stay stable.

**Dave Jones:** So, getting back to our 1N821 diode here, it's available in various grades. In this case, we've got the top grade, which is the 1N829 ARU with the lowest temp code. But, this is from Microsemi. They would have, you

**Dave Jones:** know, it's a second source. Well, you know, it's a multiple source part. They would have actually used, because this doesn't quite meet the temp code spec of the unit. They've obviously got an even better device like this. Now, I searched findchips.com. The one

**Dave Jones:** manufacturer had this for $80. Another one had it for $6. So, you know, prices are all over the shop. And really, they would have sourced a really high spec unit. Probably been individually selected from a specific manufacturer, a very reputable

**Dave Jones:** manufacturer, not just, you know, left it up to their purchasing people to purchase it from one Anglo in China or anything like that. Would have been very specifically spec'd and probably even been for them. And they might have even done their own

**Dave Jones:** in-house binning as well. Now, here's some interesting stuff. We love curves, don't we? Curves, characteristic curves are brilliant. They tell you a lot. Now, in this case, it is the change in temperature coefficient in in percent per degree Celsius based on the

**Dave Jones:** operating current or the constant current through that diode. And they specify it at 7.5 milliamps here, which it has the best. It's not actually zero. It's actually 0.005% per degree C if you read the notes down there. But, if you operate it at any

**Dave Jones:** other current, then you're going to be elsewhere on that curve, and you've got to take that into account. Now, this unit here uses 6.5 milliamps. But, as I said, it probably it likely uses a diode from a different manufacturer. Might be

**Dave Jones:** slightly different. You know, who knows? They've taken me into account. Everything's hunky-dory. The other thing to consider with your operating current, this is even more critical that it doesn't actually change with temperature. Your operating current must stay stable. And here's why. Look,

**Dave Jones:** it here is your change in the in your Zener voltage in hundreds of millivolts, 100 millivolts, 200 millivolts per your operating current here. So, if you're operating at 7.5 milliamps here, okay? You smack on zero, but if you change it

**Dave Jones:** the operating current by just a smidgen, you know, 0.1, you can be out by well, in this case, 100 millivolts and 6.5 volts so what we are 1.5%? It's massive, right? It's huge. That's not precision. That's, you know, $2 one

**Dave Jones:** hang low multimeter kind of, you know, accuracy. So, it's critical, absolutely critical, that your operating current remains stable, and it remains stable over temperature. Otherwise, you're not going to have a precision instrument like this. It's critical. So, that brings us back to our constant

**Dave Jones:** current circuit here. This is just as critical as the reference diode itself. This must put a a very precise current through this diode. Once again, it doesn't matter the absolute value of it because you can, you know, trim it to any value you

**Dave Jones:** want here, but it must be completely temperature stable. So, they would have tested that circuit to the hilt and designed it so that it has as good a temp co as the reference diode itself or possibly even better.

**Dave Jones:** Well, it's either that or they've got some really tricky dick spec special buried Zener diode in here which doesn't actually change much on that curve which maybe has a flatter characteristic curve like that. Who knows? You'd have to know the exact one

**Dave Jones:** and where they sourced it from and get the exact data sheet from it. But anyway, that current can be just as important.

**Dave Jones:** And I'm here at Trio Smart Cal in the Nada Cal Lab and we're going to check it out against a HP meter and I've got Charles Holtom here who you've seen last time. Hey Charles. What we've got here is a Hewlett-Packard

**Dave Jones:** Agilent 3458A which is basically the world standard in long scale multimeters. And what we're going to do is take your box which is actually a 30 ppm per year. Yep. That's got about a test uncertainty ratio of about 3.5 to the standard

**Dave Jones:** version of this meter. So that's close enough to give you an idea of just how good Sounds near enough. What's the So the uncertainty ratio is only what? 3.5? 3.5 to one. Ideally we'd like 10 you know as close to 10 to one

**Dave Jones:** 10 order magnitude, yeah. And you haven't got that amount of money. No, exactly. But this is good enough. Let's give it a go. Let's Let's turn it on. We'll have a look at the reading at turn on and then we'll let it warm up and

**Dave Jones:** we'll come back in say 20 minutes or so and see how well it stabilized. Excellent. Well, let's have a look. What are we getting now? So we're just hooked up simple two wire high impedance system so we'll turn it

**Dave Jones:** on. And you've got an overload light come on there. Yeah, it comes on temporarily until it warms up. There we go. So at switch on you've got Well, you're better than uh Yeah, you're better than .0001% already so

**Dave Jones:** that's pretty good. There you go. That's not too bad. Let's come back in about 20 minutes and have a look. All right, what's the temperature in the room here? Um that is 20° plus or minus 1°. 20. They actually specify this its

**Dave Jones:** calibration temperature at 23. Is that like an older That's an older standard, yes. Older standard. The new standard is 20. Yeah, we're we're where we operate this one at about 20. Okay, excellent. Well, we'll come back later and see what happens. All right,

**Dave Jones:** we're back half an hour later and what have we got, Charles? Okay, well, what we've got is we're on the 10-V range and as you can see we're on the fifth digit, so fifth digit on the 10-V range would indicate parts per

**Dave Jones:** million. Yeah. So, one there would be one part per million. We've actually got about three and a half parts per million error looking at this. So, Absolute error assuming that this is absolutely Assuming that this is right and this is

**Dave Jones:** right. This is actually quite amazing given the fact that uh you bought this thing on eBay. And it's And it's within a couple of And it's within it was last calibrated uh 2007. So, I think you got yourself a bargain.

**Dave Jones:** A bargain? Yeah. Fantastic. Don't don't go setting up a rival cal lab with this, will you? No. Let's uh turn it down to a volt, shall we? Yeah, now you will have to allow for stabilization. These things do take time to stabilize.

**Dave Jones:** that. But even so, this is pretty good. Yeah, you're uh about 7 ppm at the moment. Yep. It's 7 or 8 ppm. So, given that the spec's 30, it's uh pretty good. I like it. Yeah. Take it home and never turn it off.

**Dave Jones:** Right, I'll leave it powered up 24/7, you think? But you know, the thing is with us old things, you know, the older that we get, the more stable we get and the same applies to the meter and the same

**Dave Jones:** applies to the calibrator, the burn-in and uh we just get better as we get older. All right, excellent. Looks like it's spot on. I was thought that we'd have to tweak a few pots, but obviously not. No tweaking necessary.

**Dave Jones:** No tweaking necessary. That's good enough. So, I can now take this home, use it as a transfer standard to to calibrate my HP bench meter, my 3478. Yes, absolutely. Yeah. You could certainly do it for your voltage anyway.

**Dave Jones:** 1.8 ppm out on 10 V range. Let's uh Well, you've you've got a little bit of drift. Uh there's a there's a little bit of drift, but that's nine. Uh it's it's just insane. I'll I'll sell it to you, Charles.

**Dave Jones:** Yeah, give it to me. What did you pay for it? I'll give you I'll give you double what you paid. A double what I paid. All right. Uh look at this. This is obscenely pornographic.

**Dave Jones:** It's a good box. It is a good box. I like it. I was I thought I bought the instructions on how to calibrate and everything, but we don't I don't think you need to. I don't think that we need to. Like this

**Dave Jones:** will eventually settle down, you know, but you know, that's just that's ridiculous. Well, you've also got the settling time of the meters It yeah, exactly. It depends if these switches here are actually just operating on a passive divider.

**Dave Jones:** They they they are just a passive divider. really is a passive divider, it's going to Well, actually it's not because it it's a it's a chopper amp. There's a chopper amp in there and it's used in the feedback loop of the chopper amp. But,

**Dave Jones:** it is a passive divider. Um so, let's go to 99. 999996. Uh too good.

**Dave Jones:** Not even going to wait for it to settle. It's already too good. Too good for what you paid. Uh not that I'm bragging.

**Dave Jones:** It's uh this is silly. It's linear, too. I like it. Linearity looks excellent. And if we check out the uh zero error there, because I've got the output uh actually switched off, let's switch that on and it's it's increased a little bit, but

**Dave Jones:** that's a pretty good uh zero offset error. I like it. Yeah, so we're really down in the uh down in the noise here, because uh these digits actually uh match the digits here on the uh on the voltmeter. So, um it's,

**Dave Jones:** you know, we it is fluctuating down in the noise there. We could dick around and try and actually get its performance a bit better in various uh ways, but uh this um is actually a shielded uh test cable we're actually uh using here. Um

**Dave Jones:** but, yeah, as you can see, it's, you know, you've got to not play around with it. Um and so, we are down in the noise, pretty much. But, if we bump that up by .1, we don't see it yet. There we go. Okay,

**Dave Jones:** now we're starting to jump up. So, .2, .3, and it's starting to not quite follow that, but, you know, we are right down in the uh noise region, where, you know, uh where our thermal uh noise and stuff

**Dave Jones:** like that comes into play based on your connections and your type of metals and stuff like that it can actually become an issue. So it's a bit of an art of measuring that low stuff, but if we go

**Dave Jones:** up in the to the 100 mV range, then we can play around with that.
