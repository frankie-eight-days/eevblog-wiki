---
video_id: anTMgvCK-3g
title: EEVblog 1730 - AC Basics Tutorial Part 8: Apparent, Reactive & Real Power
url: https://www.youtube.com/watch?v=anTMgvCK-3g
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 33, "3": 50, "4": 65, "5": 77, "6": 92, "7": 109, "8": 125, "9": 142, "10": 157, "11": 171, "12": 187, "13": 204, "14": 216, "15": 232, "16": 250, "17": 266, "18": 282, "19": 298, "20": 315, "21": 334, "22": 352, "23": 368, "24": 382, "25": 399, "26": 415, "27": 431, "28": 446, "29": 462, "30": 481, "31": 497, "32": 511, "33": 524, "34": 541, "35": 560, "36": 576, "37": 592, "38": 606, "39": 626, "40": 645, "41": 661, "42": 674, "43": 689, "44": 706, "45": 720, "46": 735, "47": 750, "48": 762, "49": 777, "50": 791, "51": 801, "52": 817, "53": 834, "54": 852, "55": 867, "56": 882, "57": 898, "58": 910, "59": 924, "60": 939, "61": 950, "62": 965, "63": 980, "64": 993, "65": 1006, "66": 1020, "67": 1032, "68": 1048, "69": 1063, "70": 1077, "71": 1096, "72": 1109, "73": 1126, "74": 1143, "75": 1156, "76": 1171, "77": 1186, "78": 1202, "79": 1217, "80": 1231, "81": 1245, "82": 1259, "83": 1278, "84": 1293, "85": 1312, "86": 1326, "87": 1338, "88": 1355, "89": 1368, "90": 1384, "91": 1398, "92": 1414, "93": 1430, "94": 1446, "95": 1462, "96": 1474, "97": 1487, "98": 1501, "99": 1515, "100": 1530, "101": 1543, "102": 1559, "103": 1573, "104": 1585, "105": 1600, "106": 1612, "107": 1627, "108": 1643, "109": 1660, "110": 1674, "111": 1683}
---

**Dave Jones:** Hi, welcome to part eight of the AC Basics tutorial series. Going to look at something very important today, not some obscure rubbish. We're taking a look at apparent, reactive, and real power. And we'll take a look at power factor as

**Dave Jones:** well. You'll encounter these terms absolutely everywhere in all aspects of power distribution, power supply, AC power distribution, AC power supply, or your mains powered stuff. If you've ever seen me review a mains powered product, and an oscilloscope or a computer, I

**Dave Jones:** might actually measure its mains, like its power consumption from the mains. And it might measure, say, 15 VA, or 15 W, or 15 VAR, for example. And what do all these terms mean? It's incredibly important for almost everything. Let's

**Dave Jones:** go. As we've looked at in previous videos, assuming a sine wave, but it doesn't have to be, when you've got an AC waveform, then you've got a phase relationship between the voltage and the current. And I won't be even

**Dave Jones:** bothered to draw them on the board. You've seen them in previous videos. But just imagine a two sine waves, one's voltage, one's current, and they can be in phase like this, totally in phase. Assuming that my hand in front here is

**Dave Jones:** the current, and this is the voltage waveform, and this is, say, the zero crossing point, or whatever, then the current can either lead the voltage, or it can lag the voltage. And you've seen in previous video the acronym civil, c i

**Dave Jones:** v i l. And that tells you that if the current is leading the voltage like this, then your reactance is primarily capacitive in nature. And if it's lagging like this, you know it's primarily inductive. So, let's talk about a basic AC circuit

**Dave Jones:** here. We've got our voltage, our AC voltage source, we've got current, and it's flowing through uh, both a real resistance here and a reactance X, which we've seen in previous videos. And the reactance X can be plus or minus JX, and

**Dave Jones:** reactance is in ohms, just like resistance is in ohms, but the plus or minus depends on whether it's primarily capacitive, uh, reactance, or whether it's inductive reactance, whether or not, uh, that's plus or minus J there. And the impedance, Z, is equal to the

**Dave Jones:** real component, the real resistive component, plus the imaginary reactive component. So, let's take the case you've got an AC power source here. Uh, could be your 240 V mains, or whatever, 110 for you Yanks. Um, and you put it

**Dave Jones:** directly across a resistor. It's just a pure resistor, has no inductance, no capacitive, not that that's reality in circuit. There's always little inductors somewhere, and little capacitances somewhere. But, let's just assume an ideal resistor. Put it straight across a

**Dave Jones:** resistor, then you're going to have no phase relationship between your voltage and current. Your current and voltage are going to be completely, uh, in phase. There's going to be zero phase difference, or what's called theta, in there. So, you'll be dissipating 100%

**Dave Jones:** true power, or real power, here in the load. So, just like in DC circuit theory, power equals voltage times current, and it's expressed in the units of watts. But, because we're talking about an AC circuit here, the real power

**Dave Jones:** equation has an extra term in here, cos theta. And theta is that phase angle, but we've got zero phase angle. So, get your confuser out here, and make sure it's in degrees mode, because when we're talking about phase angles, we're

**Dave Jones:** talking about degrees, not radians, not gradients. So, your confuser has to be in degrees mode, okay? But, uh, put in cos of zero. And what do you get? You get the value of one. So, it's multiplied by one, so it might not even

**Dave Jones:** exist. So, when you have a purely resistive load on your AC supply, then it's just the power in watts is simply the voltage times the current. And also, you've got your regular power equation, just swap it around. Power equals I squared times R, and

**Dave Jones:** power equals V squared on R. Simple. But, that's when you only have a resistive load. There's no reactive component down here. There's no imaginary component at all. But, hey, this is AC theory. We don't just have resistances in our circuit. We have

**Dave Jones:** capacitance and inductors, especially in things like motors and even switch-mode power supplies, for example, in your oscilloscope or your computer or whatever. When you measure those, they're actually not just a purely resistive load. If your oscilloscope says it takes 50 W

**Dave Jones:** power consumption, and that's what we need to get into with apparent and reactive power. Once you have any sort of complex load, and by complex I mean the imaginary component, the imaginary reactance down here, then you'll get a phase difference

**Dave Jones:** between voltage and current. And that's where you no longer just have real power, you will have apparent power and reactive power. Now, the most important thing to remember about real, apparent, and reactive power in AC circuits and loads and and transmission lines and

**Dave Jones:** like generators and everything else and transformers is that there is only ever power or real power dissipated in resistances. They're never dissipated in capacitances, never dissipated in inductors. They're only dissipated in resistances. But, of course, if you look

**Dave Jones:** at the model of a capacitor or an inductor, a capacitor has equivalent series resistance in it, right? It's got leakage resistance across it, for example. And inductors, they have series resistance, they have DC resistance in the coils, and that's where power is

**Dave Jones:** dissipated. If you have an ideal capacitor or an ideal inductor in an AC circuit, it doesn't dissipate any power whatsoever. Zero, zilch, nada. But in the real world, let's look at say this is a component, say this is an inductor

**Dave Jones:** here, or it's a transformer for example. We have the reactive component, which is like the magnetic field or the actual inductance, for example. But we also have the resistance of the windings and things like that. But it's only the

**Dave Jones:** resistance in the windings, say of a transformer, that's actually going to dissipate power. Just think of those big gigantic power transformers at the substation or on your street poles or whatever. Those transformers, if they weren't like 99. whatever percent

**Dave Jones:** efficient, they would get incredibly hot. It means that there's very little series resistance in that those transformers, but there's some. And that's the only place in the resistive component of that transformer that is going to dissipate power. So

**Dave Jones:** anytime you introduce a reactance in your circuit or your load, for example, then you're going to get that voltage current phase difference, and that's when the cos theta term comes into here. So let's look at apparent power here.

**Dave Jones:** What is apparent power? Well, it uses the term S here. That's what stands for apparent power. And it's simply the voltage times the current. And the V should be like an italicized V and the I is an italicized I just in case that

**Dave Jones:** it's like AC instead of DC. But it's simply voltage times current. Well, isn't that power? Is simply voltage times current? Yes, it is. But we're talking about the total impedance here, Z. We've got the real component and the

**Dave Jones:** imaginary reactive component JX here. So, you'll see that S is also equal to instead of I squared times R here, it's I squared times the impedance Z, not the resistance. The impedance includes the real the actual resistance plus the

**Dave Jones:** imaginary component. And likewise, S is also equal to V squared on Z, not V squared on So, we're talking about impedances now, which includes complex components. This is best explained if I show you a practical experiment I've set

**Dave Jones:** up on the bench over there. Here's a photo of it and you can see that I've got an AC power meter actually in series powering an oscilloscope, but it could be a computer, could be any like AC product whatsoever. And you can see that

**Dave Jones:** the voltage is 240 volts AC. When we're talking about everything on here by the way, we're talking about RMS. So, we're talking about RMS voltages and RMS currents. Okay, just remember that. We've got the voltage which is 240 volts

**Dave Jones:** RMS AC there. We've got the current which is 280 milliamps or so. Once again, AC RMS. And so, you multiply the voltage times the current and that gives you about 67 watts or so. But, that's not watts. You'll see that's actually on the

**Dave Jones:** left-hand side there, that's actually VA. And apparent power is not measured in watts like real power is, it's measured in what's called volt amps or VA. Because it's simply it literally is that. It's voltage times the current. That's why the units are in VA. But, VA

**Dave Jones:** is not watts. So, you'll see underneath the voltage and current there that this product this oscilloscope is not drawing 67 watts as the VA indicates. You can't just multiply the voltage by the current. That is not the true power that

**Dave Jones:** this product is taking. It's actually 30 W displayed below it. How does that work out? Well, that's where apparent and reactive power comes in. Because this oscilloscope uses a switching power supply and it doesn't have what's called a power factor correction circuit. We'll

**Dave Jones:** talk about that that later. There is going to be a phase difference between the voltage and the current and that's going to manifest itself in how much true power is actually being dissipated by this product. So, if you look at the

**Dave Jones:** back label of the product for this oscilloscope, it says maximum power 50 W, but we're getting 67 VA. If you simply multiply the voltage and the current, then well, it's exceeding its maximum power rating. That's because apparent power is not real power or true power.

**Dave Jones:** It's a huge difference. And that brings us to two important points about apparent power here. Apparent power has actually no physical reality in the load itself. Apparent power is not I repeat, not dissipated in that load. That oscilloscope might take 67 VA when you

**Dave Jones:** multiply the voltage by the current. You simply put a voltmeter on there and you put an ammeter on there and you multiply those values. It'll say 67 VA, but that's not 67 W worth of real power dissipation inside the product. So, what

**Dave Jones:** does that mean? Is it just imaginary like it is with reactance when we talk about imaginary numbers? Is it Does it just not exist? Well, no, it actually exists. That current is actually real. That current going into that

**Dave Jones:** oscilloscope is actually real and therefore that current has to be supplied by the power source. It has to be supplied by the substation and ultimately the you know, the nuclear power plant or the coal power plant or the gas or your you know, solar power

**Dave Jones:** system on your roof or whatever. That current has to be provided by the upstream power source, whatever that is. And when you've got current flowing through wires, transmission lines, power cords, the wiring in your house, the street wires, the tran- massive 500 kV

**Dave Jones:** transmission lines, everything else, they when they carry current, they've got resistors in them and they will dissipate real power. There will be I squared R or copper losses as they're called. Just use the term I squared R. Makes you sound important in the

**Dave Jones:** industry, you know, "Oh yeah, I squared R losses." So, you'll have I squared R copper losses in and they're and they're real losses. That's real power that that the you know, you have to burn more coal or more nuclear fuel to get that you know,

**Dave Jones:** to actually deliver that current. But, it's not the product that's actually taking that power. The losses are going to happen upstream in your power delivery system. Got it? Now, I know this can be confusing for a lot of

**Dave Jones:** people. So, I'll I'll draw a system diagram here. Please excuse the crude little model. Didn't have time to build to scale or to paint it. Which shows our product here, which is our silloscope. It could be anything that we're

**Dave Jones:** measuring the power consumption of. And you saw that we were get it was drawing 30 W, but it was also drawing 67 VA, volts times amps. So, what does that mean? Well, we have to look at the entire

**Dave Jones:** chain coming from the power station. The actual assuming this coming from like a coal-fired power station or whatever, right? Then you've got your high voltage 500 kV transmission lines here. You've got your local substations and transformers. You might have a

**Dave Jones:** transformer on your pole out on your street or something like that. It eventually gets into your house and it goes through your the mains wiring in your house. That's all copper. So, it's going to have resistance. So, it's going

**Dave Jones:** to have I squared R copper losses. And even the power cable that you use to connect to the product, all of this has real losses in it, real copper losses, real power losses in watts, in watts, that not in VA, not in apparent power,

**Dave Jones:** not in some imaginary power, but in real copper losses in this system to power this product. So, there's 30 watts power dissipation in that product, but that you remember that 280 milliamps? That volts times current? That 280 milliamps,

**Dave Jones:** that current has to be provided eventually via, you know, don't worry about transformer effects and all that, but just like it has to be provided eventually from the power source, the power station. So, because we actually measured 67 VA going in into our

**Dave Jones:** product, that was simply volts times amps, the current has to be provided by all this, and therefore, somewhere in that chain, we we know that we're dissipating 30 watts of real power, not imaginary power, real power in the

**Dave Jones:** product, there must be another 37 watts dissipated somewhere else in the system, cuz that current's not imaginary, it's real current. So, there's going to be 37 watts in I squared R losses, cuz remember we said real power is only

**Dave Jones:** dissipated in resistances. It's not dissipated in in capacitance of these wires, it's not dissipated in the inductive magnetic fields of the transformers or anything else, it's only dissipated in the resistors. I I E, the I squared R losses in the

**Dave Jones:** copper. Inside the transformer, they have all these windings and all the connections and crimps and all the, you know, all the copper and or, in this case, aluminum that they might use to save weight on the transmission lines,

**Dave Jones:** that all adds up. Somewhere in that system, across all that, there's going to be an extra 37 watts dissipated, and that is why, if we get this off here, we said before that apparent power, volts times amps has no physical reality in

**Dave Jones:** the load, but remember we got the rest of that system in there. So, it's actually VA is a very important figure. That's uh used for conductor sizing. How big do we have to make our transmission line wires? How

**Dave Jones:** uh big do we have to make the windings in our transformers in in the substations in the power poles on the street? How big do we have to make it inside the product for example? You could have a transformer inside your

**Dave Jones:** actual uh itself. And so, that's why you'll find that transformers and other things are actually rated in VA. They're not rated in watts. They're rated in VA because you have to take into account the phase difference and that apparent

**Dave Jones:** power. So, if your energy provider has to provide all of these extra lines, they're going to charge you for VA. They're going to charge you in volt amps or in VA or in kilo VA or mega VA if

**Dave Jones:** you're a huge, you know, massive uh data center customer or something like that. Giga these days, jeez. But often in this country and other some other countries, your country may vary, but usually the energy provider is not really uh going

**Dave Jones:** to charge you the individual residential customer for VA. They're only going to charge you for true watts because you're such a small customer. It's not worth, you know, fussing around with. So, this brings us to and I've done debunking

**Dave Jones:** several debunking videos on this. I'll link them in down below of these energy saver scams. People advertise these products as oh, just plug it into your wall and it'll save 90% on your electricity bill. And they're complete scams. They're just a

**Dave Jones:** capacitor in a box and we'll talk about that in a minute when we talk about uh power factor correction. But like all good scams, there's a kernel of truth in there. In fact, there's a lot of truth because if you're a large industrial

**Dave Jones:** customer, they will charge you for VA because you're drawing more current than what your actual load is actually taking. And that means they have to provide bigger infrastructure and everything else and it's got to come eventually from the generator somewhere.

**Dave Jones:** But yeah, they're just scams. As a residential customer, you're probably only going to be paying for watts and those power factor correction wizbang energy saver devices actually don't really save you any energy at all. In fact, they might take more energy as

**Dave Jones:** I've seen I've I've demonstrated in my debunking videos. So that brings us to reactive power. What is reactive power? Well, it's kind of the difference between the apparent power and the real power like we saw here. This 37 watts in

**Dave Jones:** I squared R losses, even though that's real power being dissipated, essentially that is the difference at the product level. That difference of 37 watts is the reactive power. So the reactive power plus the real power equals the apparent power, VA. So our reactive

**Dave Jones:** power here is in units VA, but we add R on the end. It can be little or big R, and that stands for of course reactive. So it's volt amps reactive. And that reactive power is just as its name says,

**Dave Jones:** it's the imaginary power in the reactance. So it's basically you can think of it as the power transferred to and from reactances. And remember I said that capacitors and inductors, ideal capacitors and inductors, just purely capacitive and inductive, they don't

**Dave Jones:** dissipate any power whatsoever. So you can, you know, transfer power between capacitors and resistors all day long and there's actually no real power being dissipated there. But because you've got a phase difference between your voltage and your current, the reactive power,

**Dave Jones:** which is designated by Q here, is once again the voltage times the current here. So it's exactly the same as the power as the apparent power, but it's got that sine theta component, theta being the phase difference in degrees

**Dave Jones:** between your voltage and your current. And you notice that's different to your real power, which is cos instead of sine. So, get your confuser here and in degrees mode, of course, and put sine of zero. If you've got zero phase angle,

**Dave Jones:** you've only got a resistive load, it's just a an actual resistor, and you've got no phase angle between voltage and current, then sine of zero is zero times voltage and current is zero. So, your reactive power is zero when you've got a

**Dave Jones:** purely resistive load. But, over your real power equation over here, put cos zero into your confuser and you get a value of one. So, it's one times the voltage and current, so it's simply power equals voltage times current in a

**Dave Jones:** resistive load. But, when you've got a reactance in your circuit, your load, or whatever, then you're going to have yet that This doesn't become zero anymore. This actually becomes a number and multiplied by the voltage and current, that's going to give you a reactive

**Dave Jones:** component there. And that reactive component is going to manifest itself in the impedance Z here, cuz you've got the real, which is, you know, resistances and everything else, and your reactive component, your impedance is the real plus the imaginary, and this is all

**Dave Jones:** imaginary. This is like fugazi. It doesn't exist. It's fairy dust. >> I think it's all a fugazi. You know what fugazi is? >> No. >> Fugazi, it's a fake. >> Yeah, fugazi, fugazi, it's a wazi, it's a woozy, it's a

**Dave Jones:** fairy dust. It doesn't exist. It's never landed. It is no matter. It's not on the elemental chart. It It's not real. >> Right. >> All right. >> Right. >> So, although it's this reactive power is is simply imaginary, it doesn't exist,

**Dave Jones:** it does manifest itself upstream in the power delivery system as apparent power in volts times amps. So, even though there's no actual power dissipated in any capacitance in your circuit or any inductance in your circuit, that has flow-on effects in I squared R copper

**Dave Jones:** losses in the rest of your system. Got it? And that's why the reactive power Q, instead of I squared times Z or I squared times R over here, it's I squared of just That's why there's an X in there. I X squared, which is just the

**Dave Jones:** reactive component itself. Just the capacitance or just the inductance with no extra losses in there, multiplied squared multiplied by the reactance in ohms. And likewise, V V X squared on X here, cuz we're dealing with just the reactive component, hence the name

**Dave Jones:** reactive power. Or if you prefer to think of all of this in terms of vector diagrams like we've done in our previous videos, here's the famous power triangle, it's called, cuz it looks like a triangle like this. And basically,

**Dave Jones:** you've got your real power down here on this axis like this. So, this is your real power vector. And then you've got your phase angle between your voltage and your current, that's theta, and that gives you your apparent power vector

**Dave Jones:** like that, which is S, which is V times I, and that's an actual, you know, quantity you can actually measure. And then the reactive power VAR over here is basically that vertical vector that joins them like that. So, this is your

**Dave Jones:** imaginary component over here. And basically, if you've got just a resistor in your circuit like this, and you've got real power like this, you can think of that as you increase the phase angle like this, normally, it would be like

**Dave Jones:** the same value like this, but it's not. It extends upwards like this. The apparent power goes increases. The apparent power increases. It doesn't matter whether or not you go negative like this or positive like this, because it's just one's inductive, one's

**Dave Jones:** capacitive, doesn't matter. It's It's the same thing. You don't just have that real power anymore, you've got this extra bit, which is going to be your uh VA reactive, your reactive power. But, that is imaginary, it's not actually

**Dave Jones:** dissipated anywhere in your actual uh circuit or product. And by inspection, you can see that the apparent power S is equal to uh P squared, which is uh your real watts, uh plus uh Q squared over here, and square root of that, which is

**Dave Jones:** also equal to, as we saw before, uh the real component plus minus the J imaginary component Q, which is your imaginary reactive component. Got it? That's the power triangle. And that brings us to power factor, and you might

**Dave Jones:** have heard this before. That is simply the real power divided by the apparent power. And ideally, when you're designing a product like that, a cell phone, your computer, or whatever, or a big industrial bit of machinery, for example, or your entire factory, then

**Dave Jones:** you want a power factor that's actually equal to one. You want the real component to equal the apparent component. You want to just have basically a resistive load. You don't want any imaginary reactive component in there. You don't want any reactive uh

**Dave Jones:** component at all in your factory, because if you're a big factory, they're going to charge you for VA. So, the closer you can get your power factor to one, and it's never over one, it's always one or below, from zero to one,

**Dave Jones:** then the closer you can get to that, the less your electricity bill for your factory is going to be. And you'll notice that's also equal to cos theta, which is the term over here in that real factor. So, if cos theta is one, you've

**Dave Jones:** only got a resistive load, then it's going to be equal to one. Because put cos zero, zero phase difference in the uh confuser here, and that's going to give you a value of one. So, your power factor is going to be one at best. So,

**Dave Jones:** the closer you get towards zero, the more current you're going to take from your entire up upstream power delivery system, and the more the electricity provider is going to charge you for that. So, that's why you will often have

**Dave Jones:** a power factor correction circuit inside your product. I've done an entire extensive video on this, so I'll link that in down below, and you can design active and passive power factor correction circuits. An example of passive power factor correction might

**Dave Jones:** be, for example, if you've got a factory that's got a ton of motors, for example, that's almost entirely inductive. So, your phase difference is right out here. You want to add some capacitance in parallel to compensate for that

**Dave Jones:** in big inductive load. You can actually cancel that out and get your power factor as close to that one ideal one value as possible. So, like power stations might have or factories might have big capacitor power factor correction banks in there, for example.

**Dave Jones:** But, if you've got a capacitive load, which is often like what a switch mode power supply in, for example, that oscilloscope product, then you want to add some actually inductance in there to actually compensate that out. You just

**Dave Jones:** want to add the opposite of whatever type of reactive component you have in your circuit or your factory or whatever. That's why if we go back to our oscilloscope setup over there, you can see that the power factor is only

**Dave Jones:** 0.45. That's actually pretty poor. That's why we get 67 VA, but only 30 W in real power because we've got a 0.45 power factor. Put those into your computer, and that number will work out. So, hopefully you now understand

**Dave Jones:** apparent, reactive, and real power. It is quite confusing, and if you're not using it all the time, you go, "Oh, is it reactive power? Is it apparent power? Oh, what's the different one? Which one am I using?" So, you have to be aware of

**Dave Jones:** this when you're looking at power consumption of products, for example. Any well-designed, well-specified product will specify it in VA instead of watts. If it's in watts, it's like, "No, not really. I don't believe you. I don't think there's a power factor

**Dave Jones:** correction circuit inside that oscilloscope." And well, as you saw an example and in our example, there's not. It's got a piss-poor power power factor of 0.45. So, the big takeaway from this is that whilst there's no power dissipated in reactive loads, it's

**Dave Jones:** simply just transferring this imaginary power to and from, that can actually manifest itself in real losses upstream in as apparent power and actual current in your conductors because, you know, unless you got superconductors, which have zero resistance, then yeah,

**Dave Jones:** you're going to get losses in your system. And that's why VA matters and that's why transformers and other things will be measured in VA and not in watts because that's what matters. So, anyway, I hope you enjoyed that and found it

**Dave Jones:** useful. If you did, please give it a big thumbs up and as always, discuss down below. Catch you next time.

**Dave Jones:** >> [music]
