---
video_id: DihpIvK1fdo
title: EEVblog #449 - Absopulse VFC500 Variable Frequency Converter Teardown
url: https://www.youtube.com/watch?v=DihpIvK1fdo
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 41, "3": 61, "4": 81, "5": 97, "6": 113, "7": 133, "8": 157, "9": 181, "10": 197, "11": 213, "12": 233, "13": 249, "14": 273, "15": 293, "16": 305, "17": 321, "18": 341, "19": 361, "20": 377, "21": 405, "22": 421, "23": 441, "24": 465, "25": 481, "26": 501, "27": 521, "28": 541, "29": 557, "30": 573, "31": 589, "32": 609, "33": 629, "34": 649, "35": 665, "36": 685, "37": 697, "38": 721, "39": 737, "40": 761, "41": 781, "42": 805, "43": 821, "44": 837, "45": 861, "46": 877, "47": 901, "48": 921, "49": 937, "50": 957, "51": 977, "52": 1001, "53": 1017, "54": 1037, "55": 1061, "56": 1081, "57": 1109, "58": 1137, "59": 1157, "60": 1181, "61": 1193, "62": 1209, "63": 1225, "64": 1241, "65": 1265, "66": 1277, "67": 1297, "68": 1317, "69": 1337, "70": 1357, "71": 1377, "72": 1401, "73": 1417, "74": 1437, "75": 1457, "76": 1477, "77": 1493, "78": 1509, "79": 1533, "80": 1549, "81": 1565, "82": 1589, "83": 1605, "84": 1621, "85": 1641, "86": 1661, "87": 1681, "88": 1697, "89": 1721, "90": 1741, "91": 1761, "92": 1785, "93": 1801, "94": 1817, "95": 1833, "96": 1849, "97": 1865, "98": 1885, "99": 1905, "100": 1925, "101": 1949, "102": 1969, "103": 1989, "104": 2009, "105": 2021, "106": 2045, "107": 2061, "108": 2077, "109": 2101, "110": 2129, "111": 2149, "112": 2173, "113": 2189, "114": 2209, "115": 2233, "116": 2261, "117": 2285, "118": 2305, "119": 2317, "120": 2337, "121": 2375, "122": 2397, "123": 2413, "124": 2433}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. I've got another bit of test equipment today, but it's one that you probably haven't seen before, and from a manufacturer you almost certainly haven't heard of before. What is it? It's a variable frequency converter from a company called Absopulse, and yes,

**Dave Jones:** they're from Canada. This was made in Canada, in Ottawa, in Canada, in Canada's Silicon Valley north. Go figure, as they call it. And this is a variable frequency converter, and what it does is it basically takes AC input on the back and outputs AC on the front.

**Dave Jones:** But as you can see, you can select the voltage. So what use is that? Well, it allows you to test the products which you've manufactured for various mains input voltages. So that is a test that is often missed out by even a lot of major companies.

**Dave Jones:** They design and build their product, mains-powered product, and they don't test it over the operational range of the input voltages. You'd be surprised how many companies don't do it. And that's what this allows you to do. It allows you to adjust the mains input voltage to your product, so the output voltage from here,

**Dave Jones:** and this one does frequency as well, so that you can test your product that it works over the full operational range. And you can test its performance and efficiency, or whatever it is that your product does over that mains, or doesn't do over that mains

**Dave Jones:** frequent, that mains voltage range. But not only that, it can do frequency as well, and that allows you to test your company's products that it works in different mains regions. And you may know of 50 and 60 hertz as being the two mains frequencies used in the

**Dave Jones:** world, but there are other higher frequencies used in military systems and things like that. And aircraft and avionics and all sorts of weird and wonderful industries can go up to 400 hertz. So this one I believe goes to 440 hertz. So you can adjust the output voltage from 0 to 260,

**Dave Jones:** what is it? Yeah, 0 to 264 volts RMS at 500 watts, and 40 to 440 hertz output. Very versatile bit of test gear. Essential if you're designing mains-powered products. But most labs won't have one. And the thing about AbsoPulse, not only is it designed and manufactured in

**Dave Jones:** their factory in Canada, but they're a designer of high reliability power supplies. So these things are designed for high MTBF, high mean time between fires. This one has over 100,000 hours MTBF at a rated temperature. Pretty impressive stuff. And they proudly claim on their website that not only do they use

**Dave Jones:** the highest quality components in all their products, but they use design methods to optimize and minimize the components to ensure the utmost in reliability. So this should be really well designed. This is not built down to a price, that's for sure. These are

**Dave Jones:** designed for high reliability, ultra-rugged markets. So hmm. You know what we say here on the EEVblog, don't turn it on, take it apart. But before we do that, let's take a look at the spec sheet here. And the model we've got, even though it's not written on it,

**Dave Jones:** is the VFC 500 series. And it's a variable output voltage and frequency. It's got electronic power factor correction. It is small and light. I've got to admit, it is quite light. It's got some true sinusoidal output voltage. It's got fully isolated outputs, as you'd expect.

**Dave Jones:** 500 watts output power capability, full electronic protection, and field-proven design topology. Excellent. The VFC 500 series is a variable AC power source designed to deliver power at a selectable frequency between 40 hertz and 440 hertz. It uses PWM technology and generates a sine wave output.

**Dave Jones:** Typical distortion less than 5%. Not bad. It features full electronic protection, high efficiency, low output noise, and it's fan-cooled. Woohoo! The use of components with established reliability results in high demonstrated MTBF. It's manufactured in our own plant under strict quality control. Excellent. Now let's have a look at the specs.

**Dave Jones:** It has a universal input voltage range, 95 to 264 volts, and also a large input frequency range from 47 to 410. Not surprising, I guess. The power factor's a minimum of 0.97 at full load for the entire input range. Various input protection schemes are inrush current limiting, varistors, internal safety

**Dave Jones:** fuses, lower voltage than the specified minimum will not damage the unit. That can be, you know, one of the cheap designs or something like that. If you take the input below the 95 volts, it could, I don't know, latch up, blow up, release this magic smoke, do whatever.

**Dave Jones:** This one's designed to not fail at all. It simply just does not work if the input drops below the voltage. So if you've got brownouts or sags or, you know, anything like that happening on your main supply, it's not going to suddenly blow up on you.

**Dave Jones:** Fantastic. It's got 1 hertz step output frequency from 40 to 440, 0.1% frequency stability. Ah, that's piss easy these days. Even, I don't know, 80 years ago it was piss easy to get 0.1%, I guess. Not that hard at all. It's true sinusoidal output,

**Dave Jones:** less than 5%, which isn't bad. You know, like these things are either like your cheaper square wave ones or your true sinusoidal ones. This is a true sinusoidal one, properly designed and yeah, 5% is more than good enough. Line load regulation, maximum plus minus 5%, V out from

**Dave Jones:** no load to full load, that's pretty good. Output ripple and noise, frequency ripple is less than 500 millivolts RMS over 20 hertz 20 megahertz bandwidth. I've done a video on that recently. Output overload protection, current limiting, short circuit protection, thermal shutdown, blah blah blah.

**Dave Jones:** Hiccup at 4.8 amps RMS. Hiccup. Hiccup. Hiccup. Love power supplies that hiccup. Output overvoltage protection, 280 volts AC by internal power supply limiting, 80% efficiency. Oh man, temperature drift 0.05% per degree C, blah blah blah operates from 5 to 95% humidity. MTBF, check it out, 120,000 hours at 45 degrees C

**Dave Jones:** operated. Demonstrated MTBF is significantly higher. Now 120,000 hours, that's like, you know, like more than a decade. Yep, pretty impressive. And there's the money shot for my Canadian viewers. Have to do it on the data sheet because well, it's not written on the unit.

**Dave Jones:** Why? And here's the front panel, nothing fancy. On-off power switch, voltage up-down adjust, frequency adjust, and some hot buttons for set in particular frequency. It's not sure why it doesn't have 50, 60, you know? I mean, jeez, you would think it would have

**Dave Jones:** that, I don't know, 50, 100, 200, 400? What? Anyway, it's got isolated outputs neutral and pH. I assume, I've never heard of pH, I assume that's like phase hot, maybe? Anyway, that's the mains output and ground that would be just connected through to mains earth if you wanted a mains earth

**Dave Jones:** reference output. But that's all there is to it. And on the back of the thing is no more exciting, I'm afraid, universal input. There's a fan which is actually connected to the outside, which is rather unusual, you don't see that a lot. It's got, looks like

**Dave Jones:** it had some compliance, well some testing stamps, Hypot testing by the looks of it, something under there, and some I don't know, production sticker or something from where this particular unit factory or something it came out of. So let's rip this sucker open and see what's inside.

**Dave Jones:** And the case is rather nice, folded aluminium here, it's not your usual steel case, so I rather like that, it's lightweight, looks good, nice bit of engineering. Feels pretty solid and reliable, I like it. Now of course there are many design topologies to do in

**Dave Jones:** something like this. So this will be my complete guess, that it's going to have a basic input to, basic AC input to DC conversion. And it'll either do that direct bridge rectifier on the mains input, or it may actually use an AC to DC

**Dave Jones:** converter as a first stage. And then the second stage of the output will be a DC to AC power inverter. And of course you've, you know, you're familiar with those, you can buy them for next to nothing for converting your, you know, 12 volt

**Dave Jones:** car battery into a mains output. But they're usually pretty crusty. And I have a Davecad drawing right here, which shows how crusty it can be. You can basically have your, you know, 12 volt DC supply or whatever it is, your step-up transformer like this.

**Dave Jones:** And you can have some switching N-channel MOSFETs here, which alternate switch the, well, the primary side in this case of the transformer and the secondary side being the AC output. But of course with just that, you're just going to get that crusty square wave on the output.

**Dave Jones:** You're not actually going to get your sinusoidal output. So this thing will of course have you know, sinusoidal drive control to actually do that. And they typically don't have any feedback as well, because the AC voltage is fairly accurately set by the voltage of your

**Dave Jones:** DC rail plus the ratio of your transformer. So these things actually, even though they've got no feedback, can actually be quite accurate in that case. But they are square wave, they are crusty. Now this thing of course won't, it'll have the step-up transformer of course, but it'll have sinusoidal

**Dave Jones:** control. And it says it does PWM control. In fact, what does it say? It says it uses PWM technology and generates a sine wave output. So the PWM might just be used to generate the sinusoidal waveform. I don't know. And there's probably, you know, likely some

**Dave Jones:** sort of microcontroller in there as well to handle the display and probably generate the required frequency with PWM. But I don't know. There are many other ways they could do it. They could certainly do it some clever scheme like direct AC to AC or something like that.

**Dave Jones:** But I think there's going to be that two-stage process with DC in between. But there's only one way to find out. Screwdriver time. So what we've got is six screws on the top and that looks like it holds, well it, there's like vertical

**Dave Jones:** heat sinks inside and it looks like, oh, you know, mounting aluminium mounting boards or something in there. So like a, you know, separator. So that could be the two halves. Maybe there's one half, maybe there's one board in there, there's the six screws.

**Dave Jones:** So maybe there's one board in there which does the AC to DC conversion and then there's another board in there which does the output DC to AC conversion at variable frequency. So let's undo this thing. And as I said, should have really high reliability

**Dave Jones:** components. We won't find any no-name caps in here, I'm sure. They'll be super high quality because this thing is not built down to a price. Price really has no, you know, the designers of this thing weren't thinking about price. They weren't constrained by price when they were designing

**Dave Jones:** it, I'm sure. So they're free to just choose the best possible components. Right, it is apart. So let's lift, this should just lift off. And ta-da! It does. And yes, folks, we have two boards in there. Well there's one front panel board of course, that was kind of

**Dave Jones:** a given, but we have two boards in there as I expected. And yeah, I think one is certainly going to be the mains AC to DC and the other's going to be the DC to AC board. There's actually quite a bit in there by the looks of it.

**Dave Jones:** I see a bodge cap already. I didn't expect to see a bodge cap, but I see lots of silicon hot snot around the place. And well, interesting. Let's check it out. Now there's one thing I noticed first of all, and I don't like the looks of it.

**Dave Jones:** Now here's the terminals, here's the ground terminal on the front, okay, and there's the green and yellow earth wire coming out from that, okay, and it goes over here and then it's connected over into here, it's got crimped, it's got a shape-proof washer, brilliant.

**Dave Jones:** Okay, and then, okay, that is then screwed down, it goes onto this, which is then screwed onto the bottom plate, and of course the bottom plate is the entire chassis for the thing. But if you have a look inside here, there it is.

**Dave Jones:** There is, I've undone the screws on the back of this thing, there is no connection onto the earth lug of that mains input filter there. Look at that. Nothing. It's not connected at all. What they're relying on is I haven't seen, look, they're relying on the fact

**Dave Jones:** that this mains filter, okay, it's you know, either it's got a dicky connection on the side there, or it's got some you probably can't, you can't get in there and see it, but it's got some metal on the back in there, because the screw which goes into it

**Dave Jones:** which has a shape-proof washer, no worries, they've done well there. But then that's connected onto the plastic there, so it's not even making contact, so it's just the press against the metal of that into the threaded screw hole. I mean, I mean, if that plastic was over-moulded a bit, it may not even

**Dave Jones:** make contact at all. I don't like it. Why have they done that? It seems retarded, it seems so well-engineered at first glance, everything, apart from the lack of the mains. Why wouldn't they just put the extra crimp wire on there and wire it through directly to the front panel?

**Dave Jones:** I don't get it. Alright, so what's going on here is pretty much what I suspected. We've got our 240, our mains comes in here, goes to our front panel switch over here, and then goes over to the top of this board over here, so it goes into this part of the board.

**Dave Jones:** We'll take these boards out and take a better look. And this is the, I believe this will be the AC to DC conversion and these big thick black and red wires there, which go from this module over to this module, are the DC output

**Dave Jones:** down to there, I'm presuming. But curiously they've got this control board here, adjustment pots with, they've put some set-lock on there when they've adjusted that. And it looks like they've really adjusted, they don't want anyone to adjust that pot there either. So, and

**Dave Jones:** there's another one down on the front panel, that's for the display accuracy the display ADC and measurement accuracy, I believe. But this control board in here is rather interesting, which goes through to the front panel control here. So, hmm, maybe is this are they generating the required sine wave on this board and then

**Dave Jones:** feeding it over to here? There's some, we've got some optocouplers down in there by the looks of it. And I don't know, what's the topology of this thing? Well there's certainly no shortage of screws holding this plate down, 10 of them, all with

**Dave Jones:** shake-proof washers. Excellent, they've done well. And ta-da! There it is. There's our AC input module, I guess we could call it. Now this thing looks really messy, of course. And it is, I guess, because you know, it's got celastic everywhere to sort of hold in place

**Dave Jones:** all of these vertical boards, vertical components, all pushed into place. So it really is quite a messy design. They've got all the controls, most of the control circuitry on vertical riser boards here. One here, there's 3 separate boards there, 4, 5 at least, yeah, so it looks like 5 separate vertical

**Dave Jones:** control boards there with all of the main power stuff on the bottom double-sided board, a few miscellaneous stuff around there of course. But yeah, most of the control for that on those vertical boards. And it is very messy, but they've gone to a lot of trouble to mount.

**Dave Jones:** Check out the mounts for these power devices. These look really interesting. A huge screw with shake-proof washers, and some, looks like some sort of custom plastic clip on that, and into that vertical heat sink there. Really really interesting. And look, they are genuine Infineon 47N60C3, or

**Dave Jones:** SPW47N60C3s. And let's go to the data sheet. CoolMOS power transistor, 650 volts, RDS on, 0.07 ohms, 57 amps, worldwide best RDS on, revolutionary high voltage technology, ultra-low gate capacitance, 650 volts by the way, is very very high, so awesome. Periodic avalanche rated, extreme

**Dave Jones:** DVDT rated, ultra-low effective capacitances, woohoo! Top-of-the-line MOSFET here folks. So there you have it, some sort of custom, sort of plastic retention clip there that goes over these power MOSFETs. Really quite nice, and they've used it a couple more times over here as well.

**Dave Jones:** Beautiful. And I think I might know the reason why they've gone for this retention clip like this. I think it has to do with the ultra- high reliability nature of this thing, or possibly even the high voltage insulation and stuff like that. What they've gone with here is

**Dave Jones:** a, you can see the sill pad there, and that is a complete sill pad sheet going right across, and it even wraps around, you can see it wrap around the side they've, around the sides of this thing. So they've, you know, they certainly haven't skimped

**Dave Jones:** there, but it means that they don't use the traditional hole here to put the screw through like that. Because if you do that, then you've got to have the screw with the insulated washer, but it's like we're using here, but it's going to be

**Dave Jones:** much closer to the metal tab on the back of the heat sink, so there's less clearance there, less reliability, less in terms of your manufacturing tolerances. Of course by the way in there, if you go through here, you've got to have a hole in your sill pad and

**Dave Jones:** all that sort of stuff. So this way they don't, they use a complete sill pad sheet in there, unbroken, and then, so they shift the screw up to here, and then they've got no issues with you know, gap tolerance and high-voltage arcing or, you know, anything like that.

**Dave Jones:** Or in terms of manufacturing tolerances being out, and some units being slightly lower, you know, high-voltage tolerance specs than other ones. Nice! Alright, so let's start at our mains input here. Here it is. We've got it going through a looks like a small common mode choke here

**Dave Jones:** by the looks of it. And then we've got this vertical fuse. Check it out. Vertical 3AG fuse. Look at that! I've never sort of, well no, I've occasionally seen that. I'm not going to say I've never seen that, but it is quite rare.

**Dave Jones:** Once again, all these vertical components, they're all silasticed down, they've really gone to town. Someone had fun with the silastic gun at the factory, that's for sure. Check out the, is that a MOV? No, that's a high-voltage cap there. And they've silasticed that down.

**Dave Jones:** This, another big common mode choke they've got here. There's another big series inductors by the looks of it. And there's our suppression cap from the neutral through to the input earth down there, and that of course goes to this shaft here, and that goes off to the chassis.

**Dave Jones:** And there's our input varistor protection. They've gone to the trouble to put, what is that? It's not quite ceramic, I don't know what they've put around the legs of that sucker, but it's not like a ferrite material, so I'm not entirely sure what's going on there, but that's a big-ass varistor

**Dave Jones:** by any stretch. And then we go over here, we've got more mains rated caps all in here. And then we've got this huge cap which we'll take a look at here, and our first switching transformer, and that's input 90 to 265 volts AC, output 2 times 200 volts.

**Dave Jones:** Aha! 1.5 amps each. So it looks like we're going to have a high-voltage DC supply here, and that should be, we'll get more evidence of that of course with the output filter caps when we take a look at their voltage rating. Now what we have here, folks, is a high-voltage

**Dave Jones:** high-reliability metallized polypropylene cap and they've used this instead of a more traditional electrolytic cap for ultra-high reliability. Once again, huge standoff and they've gone to the trouble to put insulation on the leads there. Ah, brilliant, Celestic, the down. I mean it does look ugly, but hey, you know, this sort of thing works.

**Dave Jones:** So what the designers have thought is that, well, this is our critical cap on the input side to our main switching transformer here, let's get an ultra-high reliability cap. And that's what they've done. And we've got a board in there with a whole bunch of power

**Dave Jones:** resistors on it, probably all paralleled up. And once again, some more 47N60s as well down in there. We've got two and possibly a third one on the other side here. I found it! I found it! There you go, folks. Made in Canada. And they haven't mucked around

**Dave Jones:** with the isolation either. Check out that, they've just gone primary, secondary, isolation. Ha! Let's just route out the board, no worries. So this transformer here of course isn't our main isolation transformer. If you have a look at the bottom here, there you go, there's just the isolation

**Dave Jones:** slot here, which is just separating mains earth from the rest of that. But look, it goes straight through. So that's not actually the main switching isolation transformer. All of this part would be part of the active power factor correction circuitry, I believe. So if you have a look at the back of the board, you can actually see the flow

**Dave Jones:** of this thing. Here's our mains input over here, we've got our input filter and our common mode chokes and stuff like that. Then we've got it going into our active power factor correction circuitry, which would be all this stuff in here. We've got high current stuff going around into our

**Dave Jones:** primary side of our main isolation switching transformer here. Here's our secondary side of that, you'll notice that that's also isolated down in there, but they haven't bothered to cut a slot out of that one, but that's a massive isolation slot. They're not mucking around there at all.

**Dave Jones:** And then we've got our output bridge rectifiers here, we've got a big output common mode choke here, and then our output filtering. And it goes straight to our high voltage DC output terminals. And the wave solder in here is also first class, even on the big power transformers.

**Dave Jones:** I like it. And that's a very common thing to, you know, goof up your lower quality manufacturers, they'll either be soldered by hand or, you know, really crusty wave soldering, and you won't get good quality joints. And of course they're going for the best Nippon Chemicon

**Dave Jones:** capacitors, KMH series, 105 degrees C rated, 450 volts 220 microfarads. Beautiful. They would be genuine, bet your bottom dollar. And on the main DC output just near the output connectors here, once again Nippon Chemicon, exactly the same model KMH, 250 volts, 560 microfarads.

**Dave Jones:** So this definitely is a high voltage DC output power supply. It wasn't the low voltage, which I thought probably would have been the least viable option for this. So they're outputting on these two terminals here, outputting yeah, no, I can actually touch that, these have got bleed resistors on there

**Dave Jones:** check it out, not a problem. And safety first folks, I'm a professional, I know what I'm doing. And yeah, so they're outputting high voltage, like you know, 250 odd volts on these terminals here. Check out how they vertically stack those two diodes there.

**Dave Jones:** Absolutely fascinating. And look at the hot snot there oh man, somebody's had fun. Actually if we have a look at the output here, check out that. That's a 0 ohm jumper link there and what they've done is actually these capacitors are in series.

**Dave Jones:** So here's the two output terminals, it's only got two, positive and negative, then that jumper link joins the, there you go, joins the two caps like that so they're actually in series. So we've got a 500 volt cap there. And they not only act as

**Dave Jones:** bleed resistors, but they act as ballast resistors as well to ensure voltage sharing across the two caps. Now this is fascinating, look at this. This little board here that just holds this capacitor and nothing else it's got wires coming off here, and a connector coming in here, is held onto this

**Dave Jones:** board via two plastic clips there there's no electrical connection between these two boards, it's purely just like a physical mounting thing. So why they've done that why they've bothered to go, well look our cable's gonna, you know well, our cable's coming from all the way over here, it's

**Dave Jones:** gonna be wired into here, they've cable-tied it, go into this board, this board will retain on that board and we'll have a separate connector, like it's maybe designed for servicing or ease of manufacture or something at the production stage, something like that, I don't know.

**Dave Jones:** And it looks like they've bodged in a little transformer or choke in there, like just sort of, you know, bodged in between this transformer over here and something else over there, I don't know. Oh man, what a dog's breakfast. So we've got our main switching isolation transformer here, and then we've got two groups

**Dave Jones:** of four diodes in there, so it's, they've got two separate windings out of that thing. So there's our bridge rectifier 1, bridge rectifier 2, this is just a big output inductor and then it goes into the caps of course, that's why there's no

**Dave Jones:** isolation at all between those, because they're just inductors from there to there. And I almost forgot to mention the thermistor on the back of these two main switching power MOSFETs here. Very nice. So over-temperature protection. So what we've probably got here, these boards in here would be part of the control for the active

**Dave Jones:** power factor correction stuff around here, and then this circuitry down here would be our main switching control for our main AC to DC converter, so hence we've got a couple of optoisolators in there, getting some voltage feedback by the looks of it. There's that part of the isolation down in there, and you can see

**Dave Jones:** that on the board, it's separate, they've got the two connectors on the bottom there, you probably can't see that, but there's, that's the isolation gap between primary and secondary side of the main switching transformer. And here's our second DC to AC inverter board.

**Dave Jones:** Not really as interesting as the other one, but eh, still we can get a look at some chips in there and have a look. But once again, oh, look. The person with the hot snot gun has just gone ballistic on anything over 10 millimetres tall.

**Dave Jones:** Oh, everywhere! Once again, if you have a look at the back of the board, you can see how it flows. Here's our high voltage DC input here at, what was it, you know, 250 or 300 volts or whatever. And we've got some more bulk input

**Dave Jones:** capacitance here, and then we've got our switching transistors here. You'll notice that, you know, nothing sort of, you know, we've got ground going off and going, snaking through this part, but there basically are no more high current flows into this part because this is all the control circuitry.

**Dave Jones:** So it basically loops all the high current stuff, just loops around to our output terminals over here. So we've got our switching MOSFETs in there, there's four switching MOSFETs, there's a whole bunch of diodes in there, and we've got our output transformers around here, and there's our output.

**Dave Jones:** So this would be presumably the, we'll have to have a look at the chips. Oh, a bodge wire. Look at that, hello. Hmm, that's not good. Anyway, yeah, this would be our control circuitry for the inverter and possibly the sine wave generator as well.

**Dave Jones:** I don't know, we'll have to take a look at the chips on the top. But yeah, you can see how it flows nicely in here through there, through the power switching transistors here, through the transformers, and out. No surprises on the switching MOSFETs, same 47N60s we had

**Dave Jones:** on the main board with the high voltage retention clips. And check out down in there, we've got around the source lead of the MOSFET, cheeky little ferrite there, just to take the edge off the switching noise. And first cab off the rank there is a UC3644N,

**Dave Jones:** and on a very quick search I can't find any info on that at all. Woohoo! Some 4000 series CMOS porn, classic 4049, beautiful. An LM311, that's been slimed! And we have two IR2110 MOSFET drivers. They're upside down so they're not going to work anymore, all the electrons have fallen out, what a bugger.

**Dave Jones:** The reason we have two of those is because we have two sets of power MOSFETs there. And check it out, we have ourselves a current transformer here. You may remember this on the smart meter teardown, we've basically got a single turn going through there, single wire through, and

**Dave Jones:** it's able to measure the output current. Beautiful. And on the rear side of both of those MOSFET heat sinks there, we've got ourselves a couple of cheeky little power diodes sharing the love. And our main input caps here are Nippon Chemicon, they're Cornell Dubli 270 microfarad 450

**Dave Jones:** working volts, 105 degree C rated, high temperature versions. Of course you'll note another 3AG fuse, vertical 3AG fuse down in there as well. Once again, held in place by hot snot, beautiful. But yeah, they are one of the world leaders in capacitors as well, so they certainly

**Dave Jones:** haven't skimped there. They might look a bit plain, but they cost a fortune folks. And we've got ourselves another thermistor down on that other heat sink. But curiously, on the matching heat sink over here, no thermistor. Why they've got it on only one, I don't know.

**Dave Jones:** Once again we've got our high-reliability metaline polypropylene cap on the output here. They're spared no expense. Huge output choke here by the looks of it, and some more output the main output transformers here, and that's about it folks. Oh, we've got a couple of

**Dave Jones:** bridge rectifiers down. No, they don't look like, no, look at that, they've paralleled them up. They've paralleled up the diodes there just to get some extra current. Hope they're matched. Ah, they'll share reasonably well. Good enough for Australia anyway. Good enough for Canada.

**Dave Jones:** There you go. But what we don't really find on here is the you know, the sine wave generator. The frequency control. So it must be on the main board. Well, the front panel board. Let's take a look at that. And here it is.

**Dave Jones:** Well, they're certainly fond of through-hole technology, aren't they? There's not a single surface mount part in this entire product. So what we have here are 4 large dip parts with labels on them. So presumably they're all microcontrollers. This one's VRMS 8. This one is IND

**Dave Jones:** F5, maybe for indication. Aha! OSC VF C1, oscillator variable frequency, and COD F7. Hmm. And it's very difficult to get in there and see that, but surprise surprise folks, it's a PIC16 F872. Another PIC for the indicator. The one we just looked at was the RMS, so it'd be measuring

**Dave Jones:** the RMS voltage and displaying that. And this is your there's our variable frequency oscillator. They're dedicated PICs to each individual task. COD? I'm not sure what COD is. Control something? I don't know. All right, I couldn't help myself. There you go. PIC16 F872.

**Dave Jones:** That is the COD chip. So I'm sure they are all identical or variations of various 16-bit PIC chips. Yeah, even the variable frequency oscillator, same device. And that RMS chip we had over here is obviously driving the display, because it goes down to this connector here, which then goes down to the second board, which then

**Dave Jones:** there's nothing on the second board, by the way, it's just the displays and the switches. And that displays the voltage, the RMS voltage on the front. So there's actually a second tap coming off the output. And there it is. There's the output voltage coming out there.

**Dave Jones:** There's the N and the pH, the phase hot, or whatever it is. So it actually measures that using the built-in ADC. And that can also display the frequency. So COD, I don't know. Control, output, display or something, IND, indicator or something, it looks like it's driving, that one looks like it's driving

**Dave Jones:** the frequency. Display, so indicator is like the frequency measurement and display. And we've got ourselves a couple of optocouplers down there, they're A3140's 8-pin DIP versions. And there's our output, they're there to drive our two outputs for our power MOSFET. So that's our PWM, that'll be our PWM output

**Dave Jones:** driving those power MOSFETs. Well, there you go, that was interesting. All we've got to do now is put it back together. ... ... ... ... And it's time to power this sucker back up and see if it works. Let's go, will the magic

**Dave Jones:** smoke escape? Nope. Not a problem. Look at that. 110 volts, that's probably the last voltage I set it at. And there it is. Bang on, 157 volts, 49.999 hertz, not a problem. Let's go to 50, sorry, 100 hertz. Boom. 200, 400 hertz output.

**Dave Jones:** Ooh, that voltage didn't stay all that regulated, did it? There's a little bit of discrepancy there when you switch up in frequency. Between the set voltage, but there you go. And we can go up all the way to 440 hertz if we so

**Dave Jones:** desire. And you can see the voltage changing a bit with frequency, it's no load, it'll perform slightly different with load, but it's probably, well, I'm sure it's within spec. Now one of the interesting things about this is that you can hear the switch in frequency.

**Dave Jones:** So I'll put my lapel mic right up to the side of the unit over here, I'll increase the gain and I'll change the frequency and we'll see if we can hear it. But you might need really good low frequency response speakers and or headphones to

**Dave Jones:** actually hear this. But we'll give it a go. So there you go, that is the AbsoPulse VFC 500 series. Hope you found that interesting. And if anyone has a schematic for one of these puppies, it'd be very interesting. So please post it, a link to it in the forum, or the comment section

**Dave Jones:** below. And I'll see you next time. Bye. If you can possibly get one, I doubt it. They don't sell these things in huge volumes and I don't think they're about to release the schematics, but you never know. Or if somebody from AbsoPulse is watching and they want to

**Dave Jones:** share the schematics with the world, share the love, then please do so. So there you go, I hope you found that interesting, that's a variable frequency converter. Very unusual bit of power supply test gear, I guess you could call it. And from a company you've almost certainly never heard of.

**Dave Jones:** And made in Canada, which is almost certainly you never hear of either. So there you go. If you want to discuss it, jump on over to the EEVblog forum. And if you like Teardown Tuesday, please give it a big thumbs up. Catch you next time.

**Dave Jones:** www.eevblog.com
