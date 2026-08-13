---
video_id: 7OW5ga49QBg
title: EEVblog #725 - LG Plasma TV Teardown
url: https://www.youtube.com/watch?v=7OW5ga49QBg
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 53, "4": 85, "5": 117, "6": 133, "7": 153, "8": 165, "9": 181, "10": 197, "11": 217, "12": 229, "13": 253, "14": 273, "15": 289, "16": 305, "17": 325, "18": 341, "19": 361, "20": 385, "21": 409, "22": 429, "23": 449, "24": 465, "25": 481, "26": 497, "27": 513, "28": 537, "29": 553, "30": 573, "31": 589, "32": 613, "33": 625, "34": 641, "35": 657, "36": 673, "37": 685, "38": 701, "39": 713, "40": 733, "41": 745, "42": 765, "43": 789, "44": 805, "45": 817, "46": 837, "47": 853, "48": 865, "49": 881, "50": 901, "51": 917, "52": 937, "53": 953, "54": 973, "55": 993, "56": 1013, "57": 1025, "58": 1045, "59": 1069, "60": 1089, "61": 1109, "62": 1125, "63": 1145, "64": 1161, "65": 1177, "66": 1201, "67": 1221, "68": 1241, "69": 1257, "70": 1273, "71": 1285, "72": 1301, "73": 1317, "74": 1333, "75": 1349, "76": 1365}
---

**Dave Jones:** Hi. In a recent video, you saw me score this 50-inch LG plasma TV from the dumpster, and it mostly works. There's an issue with the screen flicker on it, a couple of little lines across it and things like that. But anyway, I thought we'd open it up, check

**Dave Jones:** out what's inside this thing, maybe repair it. I don't know whether or not it's worth repairing something like this. It weighs almost 50 kilos. It's ridiculous compared to modern LCD TVs. They chew a ton of power. They produce EM radiation, which a lot of people complain about as well.

**Dave Jones:** Interference, all sorts of stuff. So the plasma TVs are really just completely dead technology, totally killed by LCDs. But hey, you know, they do contain a lot of usable salvageable parts in them. And well, I guess if you can fix it, if you

**Dave Jones:** can mount the bloody 50 kilos up on the wall, then well, maybe they're worth repairing and get some use out of things. But anyway, let's just take a look inside, see what's going on. Here we go! Alright, I think I got most of the screws out, although

**Dave Jones:** probably not. Odds are I've missed one. So the back should lift off. Ta-da! Let's... yep! I got them all! Unbelievable! Wow! Look at that! We're in like Flynn. Now I really enjoy looking inside these plasma TVs, because they're always well-engineered, well-laid out. At least the top brands are.

**Dave Jones:** I'm not sure the real bottom-basement crap ones, but you know, LG, at least... okay, some people are going to argue, you know, a shit brand. But hey, they're at least one of the big name brands. And this is beautifully engineered and laid out.

**Dave Jones:** You know, at first glance and everything like that. We've got all our high-voltage boards, all modular, so like some of these large caps here are likely to be the cause of fire and cause of that flicker. You know, fairly odds-on in that respect,

**Dave Jones:** because there is a horrible screen flicker on this thing. It's hard to show on camera, it's almost impossible to get that sort of flicker on camera, but as soon as we turned it on, we noticed that, yeah, it was just... you couldn't watch it.

**Dave Jones:** You couldn't actually stare at the screen, it was that horrible. So there's something going wrong there. We'll have to have a close look at those caps, but beautifully modular. We've got all our main video processing all on this board here. Dead giveaway is

**Dave Jones:** all the huge ASICs. It's probably obscured by the bar there. Huge, big die-cast bar in these things with the big die-cast chassis in there. So, but anyway, a couple of big... three big ASICs on that board, big display processing. Then we've got our road drivers

**Dave Jones:** either side, and our column driver boards. They're not one big PCB, because you can't manufacture or you can manufacture a PCB this big, which is like just under a metre long or something like that. But it's... you can get them specially made, but it's much easier, as they've done,

**Dave Jones:** you might be able to see here, split them up into individual boards, three separate boards like that. It's just easier to get them bare-board manufactured, easier to get them assembled, etc. So that's what they've done. So they're the column driver boards, top and bottom.

**Dave Jones:** Huge road driver boards. These are the big power beasts, and this is where all the power's been consumed in these plasma TVs, which have horrible power consumption. I might actually measure it. Actually, just what the... just the static power consumption of this thing is, because they're absolutely horrible compared

**Dave Jones:** to modern LCDs. Got a couple of little pissant fans up here. They're actually shock... are they shock-mounted? Sort of loosely... yeah? Yeah, they're actually shock-compliant mounted on there to minimise noise. So that's not bad at all. Little bit of dust on them, but this is a pretty

**Dave Jones:** clean unit, actually. And by the way, little safety tip. These things generate... these can store a lot of energy in the reservoir caps in here. So a well-designed unit will have bleed resistors on the main filter caps in here, so it should bleed off the energy.

**Dave Jones:** But you don't want to be go-poking around here, A, when the power's on, unless you use an isolator supply, you know, proper probing, you know exactly what you're doing, or you've just disconnected the thing and then you go touching around. You don't want to do that.

**Dave Jones:** I've got our high-voltage caps here, or our high-voltage caps, which are connected together so they don't flap around in the breeze. And it's very, very nice. I'll show you some close-ups. We've got all our RF beads over here on all the cabling, so that's to pass

**Dave Jones:** EMI requirements, even though these things spew out all sorts of garbage. But yeah, I guess they meet some standard. We've got our vacuum fluorescent display down the bottom, which is a particular feature of this dumpster dive video, but beautifully modular engineering. I love it.

**Dave Jones:** But yeah, 50 kilos. It's all this huge die-cast weight and everything, the big glass panel on the front, and oh man, unbelievable. So here's our main power supply boards, and I don't see any bulges in the caps. And they're Sanwa, yes, Sanwa brand caps.

**Dave Jones:** Yeah, not exactly the best. They're not Nippon Chemicon or Nichicon. They're not quite one hung low, but jeez, probably not far off it. So yeah, but likely, even though there's no bulging in those, you might replace those as a matter of course. These other ones here,

**Dave Jones:** I can't get the brand. Apart from that, it's not bad quality. All single-sided board construction as all these power supplies typically are to save a bit of cost. Everything's siliconed down quite reasonably quite nicely, and the transformers look decent quality. The big inductors up here, they look like they're doing

**Dave Jones:** the business. They're big common-mode chokes, are they, by the looks of it? Looks like two separate windings either side, so that's a dead giveaway for a common-mode choke. And some decent heat sinking and attachment with the silicon pads under here. Some of them are, some of them aren't, but I can show you that in a

**Dave Jones:** second. But generally that's not too bad. Even though they've got some fans on here, it's minimally fan-cooled. There's not a huge amount of airflow with these tiny little fans in such a large volume. You can see our main drive transistors here, and they've got a couple of other ones just not as well

**Dave Jones:** attached to the heat sink there. They don't have sill pads, but they don't need to be, because they don't need any isolation. They wouldn't have an exposed metal on the back of those, they'd just be the plastic packages. And likewise, they've got a bunch of diodes

**Dave Jones:** there attached to these heat sinks down in there. So yeah, that's alright. It's doing the business. Many more power transistors all tucked away in there, all driving these big-ass transformers here. And here's the main video input board. We've got a huge big-ass ASIC processor under there.

**Dave Jones:** We've got ourselves the digital, or is this an analog tuner? I think it might be old enough to have an analog tuner in this thing. I don't think it's digital. I have to find a day code, actually, see what this thing is. But anyway,

**Dave Jones:** if you're wondering what all this tape here is, that's actually RF shielding tape. They're actually connecting this heat sink over here with the main chassis over here. And if you don't believe that, you can always get your meter on there, it's going to have conductive thread in there.

**Dave Jones:** Ta-da! Look at that! So they don't want this heat sink here flapping around in the breeze RF-wise, just picking up all sorts of crap and re-radiating it. So they're deliberately shorting it out to the chassis over here. And as I mentioned before, the wiring in here, they've gone to town, they've

**Dave Jones:** put an extra loop there in the ferrite, surrounding the ferrite bead there, just so that they take the edge off all that RF crap. And they've got more of that hidden down in here. You can see the vacuum fluorescent display board down in there, because this thing has a big vacuum

**Dave Jones:** fluoro display which reflects off a glass surface down here, and then it's got a capacitive touch interface or something like that to detect that your finger presses on these imaginary projected displays. Yeah, they've gone to town on the tape here, you can see it joining

**Dave Jones:** this big die-cast frame here with the main metal chassis down here. They've done that on that side, that side, and also over here as well for the input connectors over here. And for those playing along at home, there's those super high quality Senwire caps.

**Dave Jones:** Hmm. I'm always a sucker for nicely wound chokes like that. It's just beautiful, look at them! Big beefy suckers too, love it. You'll notice that these high voltage row driver ICs here got their own heat sink, but they're also, look, very well sealed all the way around like that.

**Dave Jones:** Why? Because the high voltage is going to attract dust and moisture is going to be an issue and all that sort of stuff, so you really want to seal those things. It looks like they're little quad flat packs under there by the looks of it.

**Dave Jones:** Yeah, but you definitely want to seal those in from all sorts of dust and contamination and crap. Now in terms of Plasma TV voltage rails, they're going to have two major supply rails. One's called VS and the other's called VA. The VS supply, well

**Dave Jones:** VS, V Supply Voltage, but it's actually the Horizontal Grid Supply Voltage, so that's going to these horizontal row driver boards here. And that's going to be this main power supply in here, this lead going out here. I'll show you the close-up of the silkscreen in a second.

**Dave Jones:** It does indeed say VS, and that's going to be typically at 190 volts DC. So, as and a lot of power as you can tell by all the heat sink in, you know, all the big beefy components on the thing. But that should be about

**Dave Jones:** 190 volts. And in addition to that, you're going to have a vertical grid supply voltage, that's called VA. And that's going to be typically in the order of 65 volts. So let's see if we can find those in the power supply sections here.

**Dave Jones:** Please excuse the upside-down nature of the video footage here, I know all the electrons are going to fall out, but you can see it there. VS, VS, VS, and ground there. So they've got three lines, they're going to be all shorted together for extra

**Dave Jones:** current handling capacity of course. So that is going to go out and supply this horizontal board over here. So that's our horizontal grid supply voltage. So that's popping out there, going into our main connector on there. We've got some extra filtering happening in here.

**Dave Jones:** You should also notice the VA down in there. So they've got that for the vertical grid supply voltage going through to the main board through on the main supply as well. So they're going to be our two main supply voltages. So in a plasma TV, they're the

**Dave Jones:** two things you're going to want to check first if there's anything wrong with anything. And then we've got this smaller power supply module here, not nearly as high a power you can tell by the significantly smaller heatsink. And this is all your low voltage stuff.

**Dave Jones:** So you're going to find let's get down in here, you're going to find things like there we go, 5 volt and 3.3 and various stuff like that, just for all your digital logic side of things. Oh, check out that tiny little fuse in

**Dave Jones:** there. Wonder what that puppy's doing. But look, it's a very interesting axial type fuse. Wow! Fascinating. Anyway, there are a couple of fuses over this board. Look, the horizontal board here we go, it's got a socketed fuse and there's a few more on the main power supply ones in there, and all scattered

**Dave Jones:** around the place. So, you know, occasionally if you have a fault, it could be a blown fuse, but usually air's a blown fuse for a reason, and these are HRC ones too, none of this glass fuse rubbish. So with those two supply rails I was telling you about, 190 volts for the horizontal

**Dave Jones:** and 65 odd volts for the vertical, you can see we've got two different types of caps here. You'll notice that these puppies here, sorry for the shaky camera footage, they're 250 volt rated. What brand are they? I can't quite see them at the moment.

**Dave Jones:** Are they Rubicons? Anyway, have a close look. So they would be your main ones for your horizontal supply, your 190 odd volts. And then these puppies here, check it out, they're 100 volt rated, so they're going to be for your 65 volt vertical

**Dave Jones:** and ta-da! No surprises for guessing, the wiring comes straight out of there over to your vertical boards here. And those things aren't particularly high power, so what they can do is just loop the power through here and have it come in over there

**Dave Jones:** like that. No problems whatsoever. In fact, they have sensibly marked those there we go, VA, that's going to be our 65 volt supply, plus they're running the 5 volt there for the digital as well and ground, and that's basically all there is for those boards.

**Dave Jones:** So they just daisy chain those across these boards here, not consuming a huge amount of power at all. You can tell by the fact that A, they're daisy chained through the boards like that, and B, oops, that's my remote cable just hanging down there

**Dave Jones:** flapping the breeze. Sorry about that, my remote wireless microphone Sennheiser EW100G3 wireless mic if you're wondering which one I'm using at the moment. Anyway, yeah, they're just daisy chaining those through, and the wiring is just really pissant. Look at that tiny stuff. So you know there's not a huge amount of power there.

**Dave Jones:** Oh, actually, ta-da! Look at this! This is handy, they actually tell you. There we go, VS 190 volts and VA 60 volts. So I was slightly off there on the vertical grid supply voltage, but there you go, no problems whatsoever. 5.3 volts there for the power supply.

**Dave Jones:** Why is it 5.3 instead of your nominal 5 volts of 5.25? Well, you want to set it so that you're allowing for voltage crop drop across all your wiring and all your boards. So if you've got your main 5 volt supply voltage on this high voltage power, not high

**Dave Jones:** voltage, but your main switch mode digital power supply here, then you want to allow, because of the huge big space modular nature and all the cabling running off, you want to allow for the voltage drop in the cable. So you're going to typically set your 5 volt rail here, not to 5 volts

**Dave Jones:** but 5.3, and that'd be fairly typical. So when it gets over to these boards, eh, it might be nominally, you know, 5 to 5.25 volts. And 570 watts max total power dissipation, thank you very much. Man, you can fly to Alpha Centauri on 570

**Dave Jones:** watts! Kidding me? Alright, let's see how much power this puppy takes, just static. So I'll plug the thing in, and probably heard some relays clicking there, and don't know if it's actually switched on or not, it's still lying on the floor here, but

**Dave Jones:** there we go, we've got a hundred and... no, there we go, 230 watts. And so it must be, obviously that's not standby, that's displaying something on the screen at the moment, so it's obviously booted up, so yeah, over 200 watts there. Wow. So we can see

**Dave Jones:** our power factor, there we go, we've got a 250 VA and our power factor there, there we go, 0.82. But of course that 200-odd watts is going to change drastically with the information on the screen though, that's not going to be consistent at all.

**Dave Jones:** I think it's displaying a white menu screen at the moment. So just for fun, let's just measure our main DC supply rail here, so that's going to be our ground, and yep, I've definitely got it plugged into the volts, you betcha. And let's measure

**Dave Jones:** the VA first, shall we? The vertical grid. There we go, bang on, 60 volts, as that label said it should be. And now let's check our VS, 192, so there you go. We're bang on there, although we'd also probably check that for some voltage ripple as well.

**Dave Jones:** And just for kicks, we can do that with our Breiman 869 here with its dual display capability. We can do measure our AC and our DC at the same time. So let's do that. There we go, and this is VA, it's our vertical grid.

**Dave Jones:** It's not the quickest, but there we go, 60 volts, well, it's initially showing 6 volts AC, but yeah, it's like under a volt AC, nothing going on there at all, nothing doing. Let's try a horizontal grid, 192, and it's got, oh, only about, yeah,

**Dave Jones:** about the same amount of ripple, so we're doing pretty well there. Nothing wrong with that supply at all. So that's those, those main rails aren't a source for our horrible flicker that we're seeing. So at this point, I'm not that enthusiastic about continuing

**Dave Jones:** trying to repair this thing. The horrible screen flicker on it, plus there's a few, I think if I remember rightly, vertical lines on the thing just randomly going through, so yeah, it could be power supply issues, but the vertical lines or any horizontal lines or anything like that could be any of the driver boards

**Dave Jones:** and then, well, unless you can get a new driver board, sometimes some of the devices you can reheat and things like that if they're BGA parts and stuff like that, but these ones aren't, and well, I don't know about the vertical drivers, but oh, they're all just

**Dave Jones:** these plasma screens, they're just, they're awful, they chew a lot of power, they're massively heavy, so trying to mount them somewhere, and the image quality is, well, you know, some people rave about them, oh, the blacks are really black, you know, and I don't know.

**Dave Jones:** But yeah, they're just evil things that are just, these things, plasma screens just fill the junkyards now, because they die very easily because they're really high power devices, so they fail pretty early, and they're just huge, nobody wants a big, thick, heavy screen

**Dave Jones:** like this anymore that chews a ton of power, that's notoriously troublesome. So yeah, everyone switched over to LCDs and these just, I don't know, how many people are still running plasma at home if they're still going from 2008? This one, so big 50-inch, state-of-the-art for its day, and

**Dave Jones:** it did the job, but yeah, this is not a particularly top-of-the-line one, I don't think, I think this was like a pretty Joe Bloggs affordable average one, but yeah, I've got no use for it really, so when you get these, they're, you know, usually if people are tossing them out, hey,

**Dave Jones:** you know, scrap them for the parts! You know, you're talking about big high-voltage power transistors, you've got some big caps in there, even if they're semi, you might keep them for something, you've got nice big common-mode chokes you'd rip out, some nice transformers you might be able to reuse, and take

**Dave Jones:** all the boards and modules out, keep those in your, you know, I've got like containers filled with, you know, boards like this, so if I need a part, I need a nice big high-voltage cap here, I can get one of those from here, need a nice choke, they've got some fuses in them, you'd rip those out,

**Dave Jones:** and you might be able to just salvage some parts like that, usually I just leave them as whole boards in there, so if I'm desperate for a part, I haven't got time to go desolder all the parts like I did when I was a kid and put them in the parts

**Dave Jones:** drawers and stuff like that, not anymore, but yeah, keep the bare boards, heat sinks are always very useful, you get the fans out of them, you put those in your fan bins, and yeah, but all your digital stuff is all pretty useless, but there might be some

**Dave Jones:** surface mount caps on there you might be able to reuse at a pinch for example, so it's worth salvaging these things, if people are chucking them out, eh, there's lots of useful parts in them, you get all the ferrites, if you're desperate for wiring you might get some of that, but yeah,

**Dave Jones:** there's some, you know, quite reasonably decent parts on these things, so well worth salvaging. So there you go, that's a look inside another plasma TV, the LG 50 inch whatever model it is, who cares, they're ancient, obsolete, nobody wants them, scrap them for parts.

**Dave Jones:** Beauty. If you want to discuss it, link down below to the EEVblog forum, I'll leave YouTube or blog comments in if you like it, please give it a big thumbs up, yeah, sorry, people will complain they didn't go through and repair it, what's the point?

**Dave Jones:** I've got better things to do. So yeah, I'll probably I don't know, what will I do with it? Just, yeah, exactly as I said, rip the boards out and eh, she'll be right, might dump the rest. Bit of a shame, but I've got no use for it, what the hell

**Dave Jones:** am I going to use a 50 kilo 50 inch plasma for? I wouldn't even be able to mount it on the wall here I don't think. The chiprock screws wouldn't even hold the damn thing in, I suspect. So, ah, nah. Catch you next time.
