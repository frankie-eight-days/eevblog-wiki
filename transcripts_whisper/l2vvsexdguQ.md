---
video_id: l2vvsexdguQ
title: EEVblog #67 - Hacking the Princeton Tec EOS LED Headlamp with a Cree XPG
url: https://www.youtube.com/watch?v=l2vvsexdguQ
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 18, "2": 28, "3": 47, "4": 62, "5": 80, "6": 98, "7": 115, "8": 132, "9": 150, "10": 163, "11": 184, "12": 193, "13": 203, "14": 219, "15": 236, "16": 252, "17": 268, "18": 280, "19": 298, "20": 316, "21": 340, "22": 359, "23": 374, "24": 392, "25": 414, "26": 437, "27": 453, "28": 466, "29": 487, "30": 506, "31": 520, "32": 546, "33": 558, "34": 582, "35": 601, "36": 617, "37": 644, "38": 664, "39": 681, "40": 692, "41": 719, "42": 731, "43": 756, "44": 778, "45": 801, "46": 818, "47": 832, "48": 851, "49": 871, "50": 891, "51": 900, "52": 921, "53": 940, "54": 963, "55": 981, "56": 1000, "57": 1016, "58": 1027, "59": 1049, "60": 1072, "61": 1096, "62": 1107, "63": 1138, "64": 1157, "65": 1178, "66": 1193, "67": 1212, "68": 1225, "69": 1243, "70": 1262, "71": 1275, "72": 1296, "73": 1308, "74": 1335, "75": 1352, "76": 1365, "77": 1383, "78": 1401, "79": 1423, "80": 1435, "81": 1458}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's time for a product teardown, not a product review, but what I'm going to do is I'm going to take a product which I've,

**Dave Jones:** which I really like, I've liked for a long time, I think it's some really great engineering in it, we're going to take it apart, see how it works, check out why it's, why I think it's so good, and then we're going to hack it, mod it, to get better performance.

**Dave Jones:** Should be fun. And here it is. This is what we're going to tear down. This is the Princeton Tech EOS headlamp. Now, I think it's one of the best, if not the best, um, headlamp in its class on the market. I don't think you can do any better.

**Dave Jones:** Now, it's been around for a long time, it's probably, probably been around for, I don't know, the best part of a decade, I think, and they still sell it, and it's still one of the best headlamps on the market. Now, I use this headlamp for my

**Dave Jones:** canyoning because it's waterproof, um, and I use it for all my other adventure activities, and I think it's one of the best, uh, headlamps in its class on the market. Um, it's, it's, it's not cheap, it's, you know, it's $35, $40. I know you can buy cheap crap headlamps on eBay

**Dave Jones:** for five bucks with 50 LEDs in them and things like that, but they're just utter, utter garbage. They really are. You get what you pay for. For about 35 US dollars, it's much more expensive here in Australia, but, uh, in the US, 35 bucks, and I reckon it's the best headlamp you could get.

**Dave Jones:** Now, there are many things I like about this. I like the fact that it's small, it's light, uh, it's waterproof to one meter, and, um, it's, it's got o-ring seals, it's powered by three AAA batteries, it's all self-contained, it's got a, it's got a nice headband, and it's made using

**Dave Jones:** impact-resistant polymer plastic casing, and that makes it real tough and rugged, and it's got a one-watt, um, Luxion slash King Bright slash something else LED in it, and, uh, that's what we're gonna upgrade. And one of the great things about this headlamp is that it's made in the USA,

**Dave Jones:** it's not made in China or anywhere else, it's made in the US, and Princeton Tech have put a lot of design effort, as we'll see, into this, and I really love it. Now, one of the reasons that I'm so keen to upgrade this headlamp, while I love it, um, I think it's, it's not really suited, um, as well

**Dave Jones:** as it could be to my particular purposes. Now, it's got a, it's got a, a computer design, whiz-bang design focusing, uh, lens in here, which is designed to throw the beam up to 50 meters, which is very impressive for a 50 lumen, uh, one-watt LED.

**Dave Jones:** Now, um, I, I would much rather, um, because I'm not out spotting things in a tree 50 meters away, when I'm out, uh, doing adventure stuff, I'm usually, you know, I want to see things 5, 10 meters away at tops, and I'd rather have a wider dispersed beam and a brighter

**Dave Jones:** beam. One of the neat things about this headlamp is the different modes. I know all headlamps have different modes these days, but back when this first came out, it was, it was kind of a big deal, you know, to have a one-watt LED with all these different modes.

**Dave Jones:** And there's a, there's a nice, uh, rubber button on top here, which is very hard to hit when it, when you pack, when you put it in your pack and things like that. I've never had it accidentally come on, so it's really quite nice.

**Dave Jones:** And it's got different modes. You press it once, which is, it comes on high first of all, then you press it again after a certain time, and it'll go off. But if you press it multiple times, that'll go to the second level, and then a lower level, and then it'll have a flashing level as well.

**Dave Jones:** I really like the, the, the fact that they've shaved these, um, bits off here, which makes it less bulky. It really makes it lighter weight, and it takes up less room in your pack. Now the other thing is, it's got a tilting, um, thing here.

**Dave Jones:** They've built these little notches on the outside to snap into different orientations. So that's when you, when it's on your forehead, you can tilt it up and down like that. Now they've actually, uh, made the, made this bit here rounded, so that when you put it on your

**Dave Jones:** forehead, because your forehead's not straight, your forehead is round. So they've made that round, which is really neat. And the other thing is, is that they've put this, um, really nice, huge, big, uh, thumb thing on here for undoing the batteries. You can undo it with your, with just your fingers,

**Dave Jones:** or if you need to, you can get a big screwdriver, or your fingernail, or a bottle cap, or anything like that in there, and it opens up, and there's the three, uh, AAA batteries. Now as you can see, it's got an O-ring seal all around the outside here, which is really quite nice.

**Dave Jones:** It's got reasonably, uh, good surface finish here. So if you actually grease up these O-rings, it can actually be extremely, uh, waterproof. You'll see that it's held in with these two heat stakes here and here. Now if you drill through those, it'll pop straight out, and it's, it's really quite neat.

**Dave Jones:** So we'll take it apart, but look at these extra ridges they've put in here. Now they've done that to add strength, um, while actually lightening the weight, I would presume. They're, they're, they're not there for show. There's deliberately, deliberate reasons why they've done that.

**Dave Jones:** And the hinge is actually reasonably good as well. It's got a solid metal pin straight through it in there, and it's just a really nice design. Really excellent industrial design. It's lightweight, it's compact, and does exactly what you need. I really doubt you could make it, a headlamp, any more efficient

**Dave Jones:** with three AA's and a one watt LED. OK, so I've just drilled out these two little heat stakes here, and it just pulls out like this as one complete module. It's really very elegant and very nice. Now as you can see down here, internal to the case, integral, once again, held together with

**Dave Jones:** heat stakes, is, is the button. So you push the button on top, and it pushes that little lever, which then pushes on a standard, uh, PCB mount, uh, micro switch here. And there it is. And look at something else rather interesting here. Check out the, uh, the design of the plastic.

**Dave Jones:** They've added a little plastic shaft onto there, in order to hold the switch in place. They've gone to a lot of trouble to think about stuff like that, and it's really neat. And you'll notice there are no screws on this design at all.

**Dave Jones:** There, once again, this PC, this top PCB is held in, and it's soldered with that solder point there and that one, straight on to the battery contacts. Um, and there's no screws because these four heat stakes, here, here, here, and there, actually hold the board onto the

**Dave Jones:** case. And that minimizes your, uh, assembly cost and your assembly time. And it's, they've put a lot of, uh, thought and a lot of effort into it. Now, let's take off this, um, lens assembly here. And as you can see, it's a single, um, uh, nicely designed piece of, uh, sort of plastic acrylic or something, something

**Dave Jones:** like that. And that just sits right in there. And this bit here comes off. It's just held in with these four, um, four pillars here. So it's all, once again, there are no screws at all. It comes off, and bingo! There's the Luxion Star, um, LED.

**Dave Jones:** Now, this is actually an older model headlamp. I'll show you a newer one in a minute. Now, one of the things you'll notice here is that the Luxion Star LED does not have any heat sink. It just sits down in there like that.

**Dave Jones:** But what it's got is, uh, it's got, there's a thermistor. Check it out. Right under there, to sense the heat from this thing, to, uh, to either regulate it or shut it off. But we'll, um, do some circuit investigation to actually see, uh, see how that

**Dave Jones:** actually works. Now, here's my original, uh, headlamp, which I've had for many years. I've got a couple of them, um, and it's a slightly different design to this brand new one, which I've, which I just got, um, straight from the US. There, there are a slight few component differences on the board, but, uh, not a

**Dave Jones:** huge amount. And the, as you can see, the LED is actually different. This one's a, um, uh, opulent Rebel Star, it says. It's a Rebel Star LED, and it's, um, nothing printed on the bottom. The, uh, lens is a bit, too. This is the original one here, and this is the new one.

**Dave Jones:** It's, like, frosted, and it's slightly, it's slightly different, but it's a, you know, essentially it's the same design. And once again, they've changed these, um, plastic holsters to match the, um, to actually match the, uh, LED they're using. This one's got a smaller aperture on it, which, um, could cause us a problem when we go to change our

**Dave Jones:** LED. But, uh, yeah, the old one's much better in that respect. The other thing you'll notice about it is that the polycarb, um, front lens protector is, is really embedded in the plastic in there, and that's what, um, gives it its inherent, uh, waterproofness and toughness.

**Dave Jones:** It really is a tough and waterproof little headlamp. We're actually going to test to see whether or not this little thermistor actually regulates the constant current through the LED on, on, like, a continuous basis, or whether or not it's just a hysteresis type, um, you know, a on-off type protection device.

**Dave Jones:** So we're going to do that. We're going to switch it on to full brightness like that, and we're going to apply the soldering iron, and, whoop, there we go, it dropped down to the next level. Okay, let's try the thermistor thing again, but with the current, but actually measuring the current.

**Dave Jones:** Bingo, there we go, it went down to 100. So it doesn't quite, will it jump back up? No, there you go, it does. It almost does have a sort of semi-continuous type effect there. Okay, well, let's actually measure the current in the different modes, shall we?

**Dave Jones:** On high, bingo, three, oh, 288. I expected about 350 milliamps, actually, but, um, it's only about 290 milliamps. And let's go the second mode, 100 milliamps, yeah, that's 95 milliamps, that's pretty much what I expected. And the third and low mode is 25 milliamps, that's pretty much what I expected too.

**Dave Jones:** Okay, let's try and measure the efficiency of this DC to DC converter. Now, ladies and gentlemen, boys and girls, here's a classic example of why in every good lab it needs at least four multimeters. Here I am, I've got, uh, measuring the, um, input voltage from the supply, I'm

**Dave Jones:** measuring the input current, so we can, from that, we can work out the input power. We've got the, um, LED working on maximum brightness, and here's the LED, uh, current, 290 milliamps, and here's the LED voltage, almost three volts. So there you go, that's a reason to have actually

**Dave Jones:** at least four, let alone five, because if I want to probe that circuit, I now need a fifth multimeter. This is a first stab at what's happening here. Here's, ground is over here, okay, that's your ground input, and this is your positive input from the battery.

**Dave Jones:** Now, there's a diode here which goes off somewhere, there's a transistor here, Q something or other, uh, there's your, um, there's your main DC to DC, um, converter inductor, okay, so that's 100 microhenries by the looks of it, and, uh, there's your diode as well, there's the input smoothing cap, that's obviously,

**Dave Jones:** uh, going between there and, um, presumably ground, and the output from the inductor, I can see, the good thing about this board is that you don't really have to see the tracks on the bottom to know what's actually going on here. It's really, really quite neat.

**Dave Jones:** Um, so the output of the inductor is going to there, so it's got a single transistor switch into an inductor, presumably that transistor's driven by the, um, IC, and, uh, what else have we got here? We've got the, um, output, um, smoothing cap as well here, and that goes right through to the negative rail

**Dave Jones:** of the, um, lead here. So, really, it's a very basic, um, DC to DC converter. It's just a single transistor switch with an inductor, and a diode, and a, and a smoothing cap, because this, uh, headlamp is actually a constant current mode. Each mode is supposed to have a constant current, which we'll check out

**Dave Jones:** later to see if it actually does. Um, now, these, uh, so, so to get that constant current, you actually need to have, you need for the, uh, you need for the IC to intelligently control the switch over here. That larger resistor there, you can tell that's a, um, current sense shunt resistor just by its size

**Dave Jones:** compared to all the others. I think they're actually, um, separate range control transistors to get the different current ranges. Now, I'm guessing that they're going to have a fixed current range, and then they switch in a, a sense resistor somewhere here, and all this stuff over

**Dave Jones:** here, um, all this circuitry is just some sort of, um, you know, voltage sense, um, circuitry. This stuff up here probably goes from the thermistor into there, so that's like a, a, um, a over temperature detect circuit. And here's a quick reverse engineer of the circuit.

**Dave Jones:** Now, it may not be 100% correct, because I only did it very quickly, so don't quote me on it, but I think it's pretty darn close, because it's basically exactly what I expected. So, here it is. You've got your battery input here, which goes to a series diode, which goes to a diode through a

**Dave Jones:** high-value series resistor, which powers the IC. You've got an input filter cap, then you've got the input switching transistor, a diode, an inductor, and a cap. And if you ignore the rest of this down here, and you have this, if you had this going to ground, then that right there would be a classic

**Dave Jones:** buck, uh, DC to DC converter, a buck step-down converter. Absolutely textbook example of it. Now, um, but instead of just being that basic thing, instead of this going to ground, it goes into these current sense range resistors down here. And as, as I suspected, there's, um, three different

**Dave Jones:** ranges, and you've got two transistors to switch. So there's a permanent range branch down there, there's another range here, and there's another range here. And you can turn these transistors on in combinations to get, uh, the low, medium, and high, uh, brightness constant current ranges.

**Dave Jones:** Now, this is 3R9 here, so that's the highest value one that's fixed. So that's obviously the low range, and it switches in the combination of 0.33 ohms and or, um, 3R in parallel with 2R2. So it, um, so through a combination of those, they can get the three ranges.

**Dave Jones:** Easy. And then it's, um, they take a sense, uh, uh, tap off here, which goes into some sense circuitry, which I haven't really looked at, um, and it goes back into the IC. So the IC clearly controls the, um, DC to DC, uh, it can, it pulse,

**Dave Jones:** controls the pulse width modulation on, well, on the gate here, um, at a particular frequency to keep a constant current through this circuit. It's neat, it's elegant, and I like it. A more advanced circuit would have actually replaced the diode here with another switching transistor,

**Dave Jones:** and that would have been a synchronous buck converter, which allows you higher efficiency. But it's, you know, in an LED headlamp, it's, it's probably not worth the effort. On the high range, I got 90.3 percent efficiency from the DC to DC converter. That's not bad for a, for a basic buck.

**Dave Jones:** And, um, uh, medium range, I got, um, 88 percent, so it's basically the same on the high and the medium ranges, and the efficiency, as to be expected on the low range, drops a bit. I get about, um, 68 percent efficiency on the low range, but that doesn't matter, it's just the low range, so it's not bad at all.

**Dave Jones:** So if we're going to hack this thing and increase the brightness of the LED on, um, any or all ranges, how do we do it? Well, it's obvious, and it was obvious before I even drew the circuit, because that large 0805, um, current sense resistor I pointed out, which is here, uh, 0.33 ohms, that's

**Dave Jones:** clearly the value for the high range. So all we have to do is, if we want to increase the brightness on the high range, just change the value of that resistor. And likewise on the other ranges as well, if you're not happy with those values.

**Dave Jones:** Simple. Or alternatively, you could muck around with the sense circuit, perhaps, but that's not worth the effort. Just change the range value resistors, and, uh, to keep the constant voltage across there. So if you lower the value, it requires more current, and, um, it, you don't have to muck around or know anything about this sense circuit or how it works.

**Dave Jones:** Let's check out the driving transistor on the various modes. This is the low mode, it's about 574 kilohertz, as you can see, and it does, uh, jitter and, uh, jump around a little bit, showing that it's continuously, um, adjusting that constant current. And this is high, we've got, uh, around about, uh,

**Dave Jones:** 56 kilohertz, and medium, we've got around 228 kilohertz. So we'll correct that and adjust the frequency, uh, to maintain a constant current. Let's have a look at the lead output, shall we, on the different modes. This is the modified headlamp, and, as you can see, there's not much

**Dave Jones:** ripple there at all. That's on high, medium, and low. All right, let's check out at what voltage the regulator actually drops out of constant current at, because that's important as the battery ages. Now, this is the battery, uh, input voltage here, and this is the LED current.

**Dave Jones:** Now, I'm going to switch it to the middle range, which is the range I typically use it at, and let's wind down the battery voltage and watch the current to see where it drops out at. Still going, now we're down to about 1.1 volts per cell now, and it's still there, and it's going to

**Dave Jones:** drop out, yeah, it starts to drop out at just over a volt per cell, really. But, uh, the good thing is, is that as the battery voltage keeps going down, you can see it doesn't just die. The lead just starts to dim, and the current still kicks in there, so you're getting useful life right down

**Dave Jones:** to now, where the lead is cut out at about, completely, at about 2.3 volts. Nice! So, as you saw there, the current regulation isn't really perfect, because a perfect current regulator in this instance wouldn't, would maintain that, uh, constant current until the battery voltage is completely dead, which

**Dave Jones:** for an alkaline cell is about, uh, 0.8 to 0.9 volts or thereabouts. So, um, it continued to work down to under 0.8, but, um, it didn't maintain it. But that's a result of the simplistic, uh, circuitry used, really, but it's not a bad performer at all.

**Dave Jones:** It certainly, uh, maintains that, uh, down to about 1 volt per cell, which is precisely what you want, really. So, it's not bad design. Now, you may be wondering why they chose the star mount LED. In fact, um, you may be thinking that, well, it was an obvious choice, because

**Dave Jones:** it's an industry standard, um, format. But really, if you're producing a headlamp like this, you cost margins at everything. So, it would have been, um, possibly, uh, it would have been much better for them to mount the LED directly onto the main PCB there.

**Dave Jones:** It would have been much more economical for them, um, less assembly, because they wouldn't have to do the wires. You could possibly make it more compact, because it's not stood off from the PCB like that, and you could do heat sinking on the board, and all sorts of advantages

**Dave Jones:** to doing that. But they chose the star LED. Why? It's because they wanted to decouple the design from the main, the LED from the main PCB. And that makes sense in the LED industry, because these LEDs are constantly changing, changing, uh, suppliers. They, you know, might get a more efficient one or something

**Dave Jones:** like that, and the footprints change. But this star mount is pretty much an industry standard, um, but it's it's because it's decoupled, you can, uh, make changes later on in the design process, or even after it's in production, with no effect on your main PCB.

**Dave Jones:** Even though it's got extra cost in assembly and stuff like that, it has its advantages. So there's much more thought gone into selecting that star LED than you might imagine. I can picture, you know, them having lots and lots of Dilbert-style meetings about this LED,

**Dave Jones:** and should they mount it on the board or separately? So, I'm going to modify one with one of these new Cree XPG LEDs. The most efficient in the world, pretty much, I think. I've used them in a previous blog, and I should be able to, um, get about, uh, 150 lumens out of this.

**Dave Jones:** Now, the standard EOS headlamp is only, uh, 50 lumens on the high mode. When we've modded the LED, we've got the choice to either increase the current on the, uh, various ranges, or just leave it the same. You can just simply replace the LED, because the new Cree XPG LED is a hell of a lot more efficient than the, uh, older Luxion

**Dave Jones:** King Bright one they're using. So, you know, just changing the LED alone is going to give you a, you know, a two and a half fold to almost three fold increase in brightness. But considering that I use my headlamp mostly on the medium or the low mode, I only use it on the high one occasionally,

**Dave Jones:** I think I'll just mod the high mode to give me, um, some increased current, maybe, uh, you know, just the 350 to 400 milliamps instead of 290, and, uh, that should be give me a useful high, uh, burst mode when I actually need it.

**Dave Jones:** I totally expect the radiation pattern to change when I mod the headlamp, but that's good, because I want a wider beam instead of a more focused beam. So, just bodging up this, I'll get some loss in, um, because it's not optimized for this particular

**Dave Jones:** LED, but the extra brightness in this LED will more than make up for it. Okay, here's a completely unscientific test in the garage here. Now, here's a standard Princeton Tech EOS headlamp on high. As you can see, there you can see the spot at the end there, and it's, it really is a spot

**Dave Jones:** headlamp. It doesn't evenly light up the, um, the areas just in front of you. Now, compare that with the new modded one. Look at that. There's no spot at the end, and it lights up either side. It lights up the cars on the side, which is really quite nice, and what I need, um, for really, uh, for

**Dave Jones:** canyoning and other outdoor work. It's really quite neat. Okay, let's try and compare the beam patterns on the wall. This is the standard Princeton Tech EOS. As you can see, it's got a really, uh, bright centered spot. Now, let's check out the new one.

**Dave Jones:** Check it out. It's, uh, really, it is much, much more even. Let's try that one more time up closer now, and this one on the right is the previous Princeton Tech EOS, and the one on the left is the new modified one. As you can see, quite a big

**Dave Jones:** difference. They're the same distance from the wall, and as you can see, there's a really, a substantial difference in the beam patterns in these two lamps. I really like the new modded one. It's very nice. you
