---
video_id: rtlN0b-gkic
title: EEVblog #242 - Hakko FX-888 Soldering Iron Hack
url: https://www.youtube.com/watch?v=rtlN0b-gkic
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 34, "3": 48, "4": 63, "5": 76, "6": 92, "7": 109, "8": 125, "9": 141, "10": 153, "11": 168, "12": 181, "13": 194, "14": 208, "15": 227, "16": 246, "17": 264, "18": 282, "19": 295, "20": 311, "21": 328, "22": 342, "23": 355, "24": 366, "25": 378, "26": 394, "27": 413, "28": 426, "29": 441, "30": 458, "31": 473, "32": 486, "33": 498, "34": 508, "35": 527, "36": 544, "37": 559, "38": 572, "39": 590, "40": 606, "41": 620, "42": 634, "43": 649, "44": 666, "45": 686, "46": 696, "47": 710, "48": 729, "49": 745, "50": 757, "51": 773, "52": 784, "53": 798, "54": 813, "55": 825, "56": 841, "57": 855, "58": 873, "59": 886, "60": 899, "61": 915, "62": 932, "63": 950, "64": 964, "65": 979, "66": 997, "67": 1013, "68": 1028, "69": 1042, "70": 1058, "71": 1075, "72": 1092, "73": 1106, "74": 1126, "75": 1146, "76": 1158, "77": 1180, "78": 1199, "79": 1220, "80": 1232, "81": 1246, "82": 1259, "83": 1270, "84": 1280, "85": 1299, "86": 1315, "87": 1336, "88": 1352, "89": 1367, "90": 1383, "91": 1403, "92": 1423, "93": 1438, "94": 1452, "95": 1466, "96": 1479, "97": 1496, "98": 1509, "99": 1526, "100": 1537}
---

**Dave Jones:** Hi. You know, I really like the Hakko FX-888D it's one of my favorites. I It's my recommended iron for beginners. Everyone keeps asking me which iron should you buy? Well, I think you can't go wrong with the FX-888D. It's really nice, but

**Dave Jones:** there's one annoying feature. Go home at night, turn the lights off, and well, did I turn my soldering iron off? Age-old question. You get a bit paranoid. And because the LED is normally off, there it is. Blinks on, and it only comes on

**Dave Jones:** when you when it's actually heating the element, which is kind of okay, but that doesn't when you that's no good when you glance over at the soldering iron as you leave. Oh, did I turn it off or not?

**Dave Jones:** Yeah, you can have all remote switches, and I'll probably eventually do that, but anyway, it's just a bit of a design oversight, I thought. It'd be much better if this thing actually had either power LED or that LED there actually

**Dave Jones:** change to green or something. Toggle between red and green, so it's always on. Because Murphy'll get you every time. You're walking out, and you do a quick glance at it like that, and like, you're bound to miss it. It'll be off

**Dave Jones:** when it's the iron's actually on. It's no good. So, I thought I'd hack this thing and see if I can change the LED in it. Let's go. And just looking at it, it is a very nicely designed tool. I know some people

**Dave Jones:** don't like it, but I I just think it's it's quite artistic, and it's designed really well. The nice the nice lines on here, and the compact footprint, and it's built like a brick donny. It's really solid as with the big internal

**Dave Jones:** transformer. And they've really gone to a lot of effort to design it. In fact, here it is. Someone by the name of Toshiyuki Kita has designed it. I guess he's an He or she is an industrial designer of note and they've signed it

**Dave Jones:** and they're quite proud of it and they love it and whoa, I agree, a beautiful design. But, it's lacking a bit of functionality. Be much better if that LED actually didn't go completely off. It just toggled between red and green.

**Dave Jones:** Bit of a design oversight. Ah, well, you can't have everything, but I think we can fix that. And to crack this thing open is pretty easy. There's four rubber feet on here. You just have to peel them off and

**Dave Jones:** there'll be four Phillips screws under there and I love that they have the adjustment tool in here. It's great for adjusting the cow pot on the front. It's just beautiful and you undo those four screws and tada, you pop it open. There

**Dave Jones:** it is. Now, I know I've done a teardown of this before, but I just can't help myself. Again, it's quite a nice design in here and by the way, before you go poking around in here, just make sure you

**Dave Jones:** unplug the damn thing for safety, okay? Don't work on this thing with the cord plugged in cuz there's exposed mains wiring down here. They've got the switch down there and look, that's actually exposed wiring, but you know, I've got

**Dave Jones:** no problems with that. It's in there nice and safe and sound and there are really some nice design aspects to it. It's the primary up here is our fused, of course, and uh it the cable clamp down here,

**Dave Jones:** excellent. Look at the solid Look at how solid that cable clamp is. It's just absolutely beautiful and then they've put some extra um tubing over there as well and cable tied it down. They've cable tied them here. It's just nice they use proper

**Dave Jones:** uh mounting studs here for the earth point mounting screws into the entire bracket. The transformer looks like it's excellent quality at the you know the laminations and it'll just it'll like last you 20 years like my Hakko 926 has or I think it might even

**Dave Jones:** be 25 years for the Hakko 926 but ah it's just a lovely design. And there's the 5N80 thyristor down there mounted onto the aluminum base like that. They've gone to all the effort to bring there. They've heat shrunk the individual pins down here

**Dave Jones:** nicely and screwed it into the base for heat sinking. Wonderful. More cable ties here, beautifully soldered points on the transformer. I love it. Now here's our main control board here. It's a single-sided board. It's got a Hakko branded chip on it, some surface

**Dave Jones:** mount parts on the bottom side as we'll take a look at and we'll have to get in there with some light and take a look at the LED and see how that's mounted. First of all, what we're going to do is

**Dave Jones:** just undo this little grub screw in here and this knob just pops off like that. Beautiful and this allows the board not to slide out all the way unfortunately cuz it looks like that they sort of slide this board in as a first

**Dave Jones:** step and then they probably screw in the transformer. So it looks like you probably have to screw out the unscrew the transformer to actually get enough room to get that board out but you can actually rotate it like that and get it at least to there

**Dave Jones:** so we can actually access the LED down in there. It's just a standard 5 mm red LED with a PCB mount spacer on the back of it which is really good and there's a whole bunch of room around it

**Dave Jones:** as well. So we can get like a little board in there and put in a bit of uh extra uh circuitry. Hacking some circuitry to uh make this LED turn red and green. So, I rather like that. We

**Dave Jones:** can access it from the bottom of the board down here. If we take a look at the PCB here, we can see the LED soldered at those two points there. This track here looks like it's uh power on

**Dave Jones:** the top side going to ground and that's confirmed if you look at the polarity of the capacitor on the bottom. So, this big uh flood track around here is ground and this one is power. So, it looks like the

**Dave Jones:** LED is on the high side of the power rail there and it goes through and through uh two there, which is a tiny little resistor, and that goes through to one pin on the chip. So, it looks like um it's just an open collector uh

**Dave Jones:** driver on the output, which just pulls that uh LED low. So, um we've got some easy uh capability there to uh do some alternate uh functionality to drive a red green LED. And I've measured the LED drop resistor and it is a 2.2 K and the

**Dave Jones:** voltage rail is 9 V. So, what do we have inside here? Well, as I said, we've got a LED to the high side of a 9 V rail through a 2 K 2 drop resistor into an open collector

**Dave Jones:** um output driver on the IC. It's a custom IC. I'm not sure what device it is. Could be a microcontroller just branded uh Haiko or something like that. But, that's clearly what they're doing. So, what can we do to add on a second LED?

**Dave Jones:** Well, my first thought was when this output here goes low, we want uh we want this red LED to come on and another green LED to actually turn off. But, when this open collector driver is switched off and the red LED is off, we

**Dave Jones:** want to switch the transistor on. So, uh we want to switch another transistor on, which So, what do we do? Well, let's add another LED over here, shall we? Let's add a green LED. I've drawn it in red, but

**Dave Jones:** oh well, what the heck? Okay, and we've got another dropper resistor. Let's permanently tie that. Let's use 2K2 again, okay? We're permanently tied that, and that's our green thing. We'll tie that to the 9-V rail up here, so

**Dave Jones:** it's permanently on. But, that's okay if you just want to do a power LED, but I don't want that. I want these this LED to toggle. I want it to be one of those bi-color LEDs, red green, that would

**Dave Jones:** toggle off or on because I don't want to drill another hole in the case and ruin the nice design and just put a power LED. I want the one LED. So, how do we get this to switch between these two

**Dave Jones:** LEDs? Well, turns out it's pretty simple, actually. Let's connect a resistor in here like this, go through, and what we want to do is short out this LED when it's off. So, let's put in a NPN transistor there,

**Dave Jones:** which connects across the green LED, and let's just drive that straight in there. So, when this goes low like this, then this transistor will switch on through here like this because the current through the through through the emitter

**Dave Jones:** like that goes through these two resistors down to ground and switches this transistor on and shorts out that LED. And, yeah, there's some excess current flowing through the 2K2 cuz you've got 9 V directly across the 2K2, but who cares, right? So, um when your

**Dave Jones:** iron is dissipating, you know, 65, 70 W, doesn't matter a rat's ass. Now, uh when that was So, when the red LED is on, this LED will be on, this transistor will be on, the green LED will be off,

**Dave Jones:** and we want it to toggle the other way. So, when this uh open collector switch opens and the red LED switches off because there's no current flowing through there like that anymore. There's no current. So, this will turn on this trans Sorry, it'll

**Dave Jones:** turn off this transistor because there's now no base current flowing through here at all because they're at the same potential like this 9 volts the base is effectively at the same voltage like that. So, it's going to switch this transistor off and

**Dave Jones:** the green LED turns on. That's it. So, it'll toggle between those two states. Beautiful. Now, I know what you might be thinking. You might be thinking that we can do away with this resistor cuz we already have a resistor here. Well, if

**Dave Jones:** you do that, when then the voltage drop across the base emitter junction here will actually swamp out this LED and switch the red LED off. So, you can't just do away with that resistor. Otherwise, you'll find the red LED will

**Dave Jones:** never come on. But, you could replace that with a MOSFET for example and do it that way. You can get away with out the resistor. But, anyway, I thought this was quite a neat solution and it would work. Unfortunately, it requires a red

**Dave Jones:** green bicolor LED with a common anode common anode connection because there's the anode of the diode and they're connected together. So, it's a a three leaded a three leaded LED and it has one common terminal for both and then the cathode

**Dave Jones:** is a separate terminal for each LED. And it turns out common anode bicolor LEDs rare as hen's teeth. So, can't get one of those. All I can get is one of these LEDs which is bicolor and they're back-to-back like that in the same

**Dave Jones:** in the same package. They're back-to-back. So, going to have to scrap this circuit. But, I just thought I'd show you that anyway. And let's try and figure out how we can drive one of these more readily available, at least what I

**Dave Jones:** can get here anyway, readily available back-to-back LEDs. Let's give it a go. And just for a bit of what the heck fun, I actually built up that circuit we just saw, and here's the red LED, here's the green LED, and

**Dave Jones:** this here simulates the this connection this resistor here simulates the open collector output on that. And as you can see, there you go. But, you need a common either two LEDs like this or a common anode one. So, exactly how do we drive one of these

**Dave Jones:** bidirectional back-to-back LEDs? It's nasty. You got to switch them around, switch the polarity. That's a not an easy thing to do in a circuit traditionally, but there is an easy way. One of the traditional methods is just to use a logic inverter like this.

**Dave Jones:** You're familiar with these. You get six in a package digital logic inverter. You just put the LED between the input and output via a series dropper resistor there, and bingo. If you've got one on the input, you'll have zero on the

**Dave Jones:** output. So, one on here will forward bias this upper LED here and switch it on. And likewise, if you put a zero in here, you'll get a one out here, and then that will forward bias this lower LED in here, and it works both ways cuz

**Dave Jones:** you've got the series dropper resistor in there. So, that's pretty easy, but we don't want to use a logic gate for that. You get six in a package. It's pissing away five of them. We don't want to do

**Dave Jones:** that. We want to be a bit more elegant. Use like a transistor solution like we showed before. So, I've sort of duplicated that circuit down here, and you can think of these two junctions as like the input and output of this

**Dave Jones:** inverter down here. And we've got two pull-up resistors to our positive rail. Now, in the case of the HEF4011, it's 9-V. Why have we added two pull-up resistors there? Well, that allows us to drag either of these junctions down to

**Dave Jones:** zero or even up in the high if you want. You can do things without shorting out the rail. So, and they use them as lead droppers as well. So, let's take a look at how this works. Let's start out by

**Dave Jones:** taking the example of when the internal open collector driver inside the IC, this is our existing high-current IC down here, just like we saw before over here. Okay? And let's say this turns on and switches our traditional red our

**Dave Jones:** existing red LED on. Well, let's look at what happens here. If we pull this down to ground, this transistor, the base, is uh is cut off. So, there's no base current, so it switches this transistor off. So, you can just ignore that. That

**Dave Jones:** transistor there doesn't exist anymore. It's switched off. So, what happens? 9 volts flows through this resistor here. Current flows through this upper LED here cuz it's forward biased down to ground, and bingo, that upper LED lights up, and you would make that the

**Dave Jones:** red one. So, we'll make this one down here the green one. Or you can have any other color. You can use an RGB LED if you want. Uh let's not go there. Red, green, traditional. So, bingo, when this works

**Dave Jones:** exactly the same as before, but let's look look what happens when it switches off the base current here and turns off this transistor. So, this transistor here doesn't exist anymore. What have we got? Well, it's easy. What we've got

**Dave Jones:** here is this resistor up here goes through here, and because this doesn't exist, current will flow through the base of this transistor and switch it on, pulling this junction here down to ground. So, not only will current flow

**Dave Jones:** through here like this and through the uh base resistor down to ground like that, it'll also flow through the green LED down to ground. Bingo, we've just switched on our green LED. And if you switch this off and on, it'll

**Dave Jones:** toggle and it'll switch between red and green. Beautiful. Piece of cake. And once again, just like before, we can't omit this base resistor down here and just rely on this resistor up here to drive this base current. Well, the

**Dave Jones:** base current will be fine. It'll this resistor up here will limit it. This transistor will turn on fine, but then the base emitter junction, remember that? It's a diode. It's 0.7 volts drop. So, this junction here will be at the

**Dave Jones:** base emitter voltage of 0.7 volts. And 0.7 volts aren't enough to turn on a 2-V LED, is it? No, of course not. So, if you omit this resistor, you'll find that or short it out, you'll find that the

**Dave Jones:** green LED won't switch on at all. Your circuit's still toggling, but green LED doesn't work. So, if you're going to use a bipolar transistor like a 2N2222 or a 3904, BC547, whatever, you're going to need that base resistor, but I think we can

**Dave Jones:** reduce our component count just one more and get rid of that resistor and change this puppy here to a MOSFET. So, we'll do just that. We'll replace this with just a bog-standard VN10 MOSFET. It can be any N-channel

**Dave Jones:** MOSFET you like, pretty much. And basically, gate, drain, and source, it works exactly like the transistor except that there's no none of that base emitter drop. So, you can get rid of the resistor and just connect the gate

**Dave Jones:** directly to that junction there. So, bingo. I think this will work. We'll build it up. We'll give it a try and hopefully we'll be able to hack it into the Hay car. There should be enough room to do that. So uh we've basically got a

**Dave Jones:** three component solution. Well, two if you count the existing existing resistor but we probably won't use that but I think that's pretty elegant solution for a toggle red green indicator. There's other way many other ways to do it I'm sure but I just like

**Dave Jones:** this one. So we'll go with this. Let's build it up. And here's the circuit built up but I'm using a bipolar transistor 2N 3904 like I showed you in the first example and this jumper link here shows you just

**Dave Jones:** simulates the Hayco chip the open open collector output. So we'll toggle that and bingo it toggles between red and green. Not a problem these by this LED bi-directional LED I've got it's a J-car cheapy. It's not very good. I've had to lower these

**Dave Jones:** dropper resistors up here to one K but there you go that's with a 1K base resistor and if we replace the base resistor there with a short that's actually a 1 ohm resistor there then you'll find that the red one turns on

**Dave Jones:** but the green one doesn't turn on as I explained but it will do if we pull that out and we replace it with a VN10 MOSFET. Got to get the pins correct here. Assuming I've got it in the right way. I think I do. And let's

**Dave Jones:** disconnect that. Bingo there we go. Red green red green isn't that terribly exciting? I think we've got a nice solution there. All we need to do is build that into our Hayco.

**Dave Jones:** And of course just make sure you've got the LED the right way around that you want it before you actually proceed with this cuz it would suck to have wired the LED in backwards. It would still work, of

**Dave Jones:** course, but you'd have your red green back to front. Can't have that. So, here's my completed assembly and uh as you can see, it's not that complicated at all. Just follow the schematic. The LEDs like that, the resistors uh

**Dave Jones:** one one resistor on each pin go into a common point which goes to a I've got this going to a red wire which will go to the plus 9-V connection. The brown wire down here is um uh the uh source pin on the uh

**Dave Jones:** transistor and the orange pin here is the gate and that will go to the um switch position on the LED the existing um uh LED common common collector switch position. So, there you go. That's the entire assembly. It should be in right

**Dave Jones:** angles like that. Go up against the front panel like that. And then all this stuff will go down the base of the board. The board will be about here about this distance from it. So, it shouldn't touch the

**Dave Jones:** board. Not that there's anything to touch cuz there's no tracks on the top side. So, that should uh fit in there quite well. Let's wire it in. And here's our connections on the board here. We've got uh ground over here on

**Dave Jones:** this side of the cap. And we've got the red wire which is the plus 9-V coming from the other side of the cap. And then the orange wire is the uh gate wire and that goes directly to the bottom side of

**Dave Jones:** the resistor down here. And once again, don't poke around inside this thing unless you've got it switched off. Safety first. All right, let's power it on and give it a try. And once again, make sure if you're going to do this,

**Dave Jones:** make sure you don't short the board the board out to the transformer at all. Make sure it is back cuz it can move. Let's do it.

**Dave Jones:** And it's red. And it's green. There we go. Bingo. Woohoo. Now, that is weird. It's not working as I expected. I expected it to come on and flash red for a little bit and just did for a longer period like it did when we just

**Dave Jones:** had the regular LED in there in the normal product, but it's not. There's a little flash. You see the little flicker of red there and if I actually um heat up the iron. I mean sorry, if I cool it down, it sort

**Dave Jones:** of that flicker rate kind of increases a bit, but there's something weird going on there. I I don't think this is actually a just a a straight logic low output. Maybe they're PWM-ing it or something and that's causing some weirdness to happen.

**Dave Jones:** I think it's time to get the scope out. Okay, what I'm doing here is I'm probing the output from the chip itself directly on the pin there which we thought which we know is an open collector output, but I think we might be getting

**Dave Jones:** some sort of PWM signal on that. So, once again, safety first with this thing. When you probe around in here, it's safe because we've got an isolated transformer, so it's electrically safe as far as that's concerned, but you can easily brush the

**Dave Jones:** main stuff on top of there not insulated. I recommend if you're going to be probing around, insulate all this stuff or just hand completely hands off. Can't stress that enough. So, let's turn it on.

**Dave Jones:** And let's capture the signal. Tada! Oh, we've caught something. Let's try it again. Aha! There you go. PWM. There you go. There we go.

**Dave Jones:** And that's why it's Yeah, that's why we're getting some flicker like that. So, what I've done here is I've added a 220 mic cap 16 volts or greater to the across the open collector output of the chip or from the gate

**Dave Jones:** of the MOSFET to ground. And that might keep the red LED on a bit longer. Perhaps, you know, you can experiment with these values. I've changed the LED drop resistor down to 1K, which of course makes a difference with the time

**Dave Jones:** constant. It makes it worse, actually. But as you can see, it is flickering. And if I cool the sponge down a bit, then it does actually go red like that. So, that's that's nice. I'm pretty happy with that solution. I

**Dave Jones:** think I'll pack that in there and be done with it. And no hack is complete without hot snot. So, that's what I'm going to hold the LED in there for. Unfortunately, the nozzle's a bit small to actually get quite right in there,

**Dave Jones:** but that won't stop me. There you go. And that'll be good enough for Australia. I love it. So, the board just slides back in there like that and the um uh the mod in there doesn't touch the board at all

**Dave Jones:** and we've got our LED in place. Beautiful. And it's all back together. Let's switch it on. Tada! It's red and it will eventually go green. And now I don't have to worry about leaving my Hakko on. Beautiful. And if we turn the wick up a bit, bang!

**Dave Jones:** it instantly switches on the heater and it will eventually come good. And it's pretty obviously what they're doing with the LED there. It's got no fancy pulse stretcher or anything like that on. They're just probably just taking the output for the

**Dave Jones:** LED directly from the switches. So, there's our final circuit. We used If you want if you've got a bright efficient LED, you can use 2K2s up here as originally. I used end up using 1K, 100 mic or a 220 mic or something like

**Dave Jones:** that. Got to be at least 16 volts because your rail's at least 9 volts and Bob's your uncle. Works a treat. There's some room for improvement here if you want to get if you know you could add a micro or

**Dave Jones:** something fancy to get the LED to blink and do all sorts of weird and wonderful things if you're that keen, but nah, I like the single transistor solution. Catch you next time.
