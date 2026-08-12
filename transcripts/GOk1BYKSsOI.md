---
video_id: GOk1BYKSsOI
title: EEVblog 1415 - Reverse Engineering the DP10007 Differential Probe
url: https://www.youtube.com/watch?v=GOk1BYKSsOI
source: youtube-asr
---

**Dave Jones:** Hi, somebody asked me if I could reverse engineer the Mixig DP10007 high voltage differential probe that we looked at, did a teardown of, and some experiments with in the previous video, linked in down below, if you haven't seen it, because I have actually torn

**Dave Jones:** down a differential probe before and explained, with the intention of explaining how the differential probe actually works. So, once again, linked in somewhere up here and down below, if you haven't seen that video, highly recommend it. It was quite pop- popular.

**Dave Jones:** And this is where I reverse engineered the Lecroy/Sapphire high voltage differential probe. And if we take a squeeze out of here, you can see that it's really old school all through hole design and everything, absolutely fantastic. Designed by Mr.

**Dave Jones:** Woo. Everyone knows Mr. Woo designs the the best probes. So, Mr. Woo from Sapphire, absolutely fantastic. Anyway, all through hole design and stuff like that. They did rub the numbers off the chips here, but meh, whatever. The intention was was actually to get a

**Dave Jones:** reverse engineered schematic of how this one worked. This one actually had discrete FETs on the input and you know, like a standard op amp differential amplifier front end high voltage resistor divider string here and stuff like this. And this is how all high

**Dave Jones:** voltage probes work. So, we're going to have something very similar here, but instead of the discrete FETs here, we're actually going to have to just a FET input high speed FET input op amps here. And so, I thought, yeah, it'd be

**Dave Jones:** interesting to just reverse engineer this and get at least a a partial schematic out of it. I don't want to do an absolute full schematic cuz I don't see any reason to like reverse engineer like the power supply and maybe the

**Dave Jones:** microcontroller and stuff down here. That's like, meh, it doesn't really matter. But, this is not going to be a how to reverse engineer cuz I've already done an extensive video, which was very popular. It got 153,000 views, also

**Dave Jones:** linked in um the cards up here and down below, and this is how basically how to do reverse engineering of a PCB. In this particular case, I use the example of the Rigol DS1054Z oscilloscope and the front end for it.

**Dave Jones:** Lots of cool tips in here of how to actually do this. And uh the way that I used in this particular case was to actually get photos of the board, make sure your camera's like right on top and

**Dave Jones:** it's centered and your board's flat, and then you convert them to black and white, and then you convert them I use IrfanView here, highly recommended. I'm an IrfanView fanboy. Um I I use IrfanView to uh then convert to like a

**Dave Jones:** what I use the find edges tool so that it kind of uh creates like an edge outline like this. I show how you can actually then um lift them up and you can put them back down and then you can

**Dave Jones:** flop essentially flip-flop between ha see what I did there? I'm here all week. Flip-flop between the top and the bottom so you can trace things out. And the good thing about using the transparent overlays is that you can use marker pens

**Dave Jones:** to uh then mark off all the components and traces. I use uh whiteboard uh markers and then you can mark them off. So anyway, there's lots of other um tips in here that There you go. You can actually mark it up like this. This is a

**Dave Jones:** how to reverse engineer video and lots of tips how to do it. So I'm not going to cover uh that in this video. By the way, I mentioned this on Twitter and a lot of people seem to agree with me that

**Dave Jones:** I reckon that there's a niche market out there for a tool, a reverse engineering tool that was just dedicated to this particular car task. And what it needs is it's just like a image editor like this that allows you to load in two

**Dave Jones:** photos, one top, one bottom, possibly with some alignment and stuff like that, but you can do that uh yourself, but then has like a big fader bar or something like that that just allows you to fade between the two images like

**Dave Jones:** this, right, top and bottom like that. And then, it would be really cool if I had like a toolbar up the top here that just allowed you to like mark it up, mark like, you know, like a you could

**Dave Jones:** put like an X on like components. You could just click and it put like an X on a component that you've already marked off and maybe a different color highlight for traces and things like that. It When you're on the top like

**Dave Jones:** this, it'd show all the components on the top that you've done. And then, when you faded through to the bottom like this, it'd change to all the components that you've marked off the bottom and stuff like that. That would be really

**Dave Jones:** cool. Um it would be an absolute bonus if that particular program actually, you know, allowed you to like maybe create a schematic netlist or something like that in KiCad or something like that. That'd be really cool. But even like it just a

**Dave Jones:** program. I'm sure there's some people out there who could just write this in like 5 minutes. But done. That's easy, Dave. No worries. Here it is. Um yeah, like there's probably myself and a lot of other people would probably pay for a

**Dave Jones:** a dedicated PCB reverse engineering tool like this. Leave it in the comments down below. I'm sure all my audience can come up with many different ways to make such a program useful. But I think that would be really cool. Anyway, um the way I'm

**Dave Jones:** fading between these at the moment is I'm actually using my video editing program Magix Vegas, formerly Sony Vegas, and I've just put the two images one on top of each other and I'm just simply using the fader bar. I took these photos not

**Dave Jones:** intending to actually reverse engineer this cuz it's important when you take these photos to have the board completely flat. Like it needs to be completely flat or the camera needs to be completely right angle with the board. And also, you got to use a proper

**Dave Jones:** one-to-one macro lens. That really helps. Otherwise, you get like distortion of the board and and, you know, it warps with the lens and and things like that. So, it's really important to get that. So, when I took these photos,

**Dave Jones:** which are available on my Flickr account, by By way, when I almost always when I do teardowns, I actually not just do video, I actually take macro photos as well. And I always put those on my Flickr account. So, I've

**Dave Jones:** probably got like a hundred different teardowns of all high-res teardown photos on my Flickr account. So, I'll link that down below if I remember. So, anyway, I didn't intend to actually do this reverse engineering video. Otherwise, I would have put a bit more

**Dave Jones:** effort into making sure these boards were completely flat. It's really difficult when you got like cables like running off this thing and you got big components like these tall components like the DC-DC converter or big electrolytic caps or whatever it is.

**Dave Jones:** It's often hard to ensure that your board is completely flat relative to the camera. And of course, you can actually set this up. And if I was to do this, I would have put the board in my light box

**Dave Jones:** with like little standoffs like this. So, like on each corner of the board, so I knew that the board was completely flat and then the components wouldn't affect the you know, wouldn't wobble and all that. But, I just sort of like

**Dave Jones:** just took basic uh photos like this. So, um with no intention of reverse reverse engineering. So, I've done my best to sort of line them up and overlay top and bottom like that. So, you can see like on this side over here, it's a little

**Dave Jones:** bit off. Um but, yeah, it's it's good enough for Australia, right? I'm going to be able to easily reverse engineer this. So, anyway, this one should be fairly easy to reverse engineer cuz although it is a four-layer board and you can see the dark outline

**Dave Jones:** in there, that's the internal ground plane. You can see the ground planes like that. And often uh you can hold these things up to a light box the board up to a light box as well. You can take

**Dave Jones:** photos off them through a light box and that helps like expose uh the inner layers and stuff like that. But, in this particular case, we've got hardly any traces on the bottom. Look, we've just got a couple here like this. These are

**Dave Jones:** just like these are probably just uh like power supply bypassing for the FET and a power supply filtering. So, this one's going to be pretty easy. I shouldn't have to put much work into it. Now, of course, when like traces go

**Dave Jones:** under components like this, this is when you This is the All these tips are in my reverse engineering video. You have You might have to start off like, you know, scraping off like the annulus ring around the via or something like that,

**Dave Jones:** and then probing out where things go, and like, you know, sweeping your probe across the board to find where all the traces go. And if you want all the values as well, you often have to go in there and measure them, and some of them

**Dave Jones:** are hard to do in circuit. But, you know, if you want to know what the value of these capacitors here is, I don't know. Is it, you know, a couple of puff? Is it tens of puff? I don't know,

**Dave Jones:** something like that. You might even have to lift components out of circuit. So, I'm not going to go into a huge depth to do this. It's just going to be a bit of a how-you-doing job. These high-voltage differential probes, you know how

**Dave Jones:** they're going to work. They're going to have a symmetrical string like this. So, I wouldn't even bother reverse engineering this bottom part down here like this. There's just no point, because it's going to be completely identical to this top half up here. This

**Dave Jones:** is how differential amplifiers work. It only starts to differ when you start talking the nitty-gritty details around the output side of the FET input buffer here, and the output over here. Once you've done all the work up there,

**Dave Jones:** this bottom one, you just duplicate it. But, of course, every circuit is different. Some are a pain in the ass, some are relatively easy like this one. I can see most of the traces. And the good thing is, once you learn all your

**Dave Jones:** building block circuits, you can pretty much guess when you've gone wrong. Like, if you can see that, "Oh, this op-amp doesn't have any feedback. Oh, tool. I forgot to, you know, R49 there is probably the feedback resistor, for

**Dave Jones:** example." So, like, it's pretty obvious when you've goofed up, or you've shorted things out, and it doesn't make any sense. Things are connected here or there that don't make any sense. And sometimes it's really obvious if you know your building

**Dave Jones:** blocks. It really helps. If you were reverse engineering this without some of that knowledge, it's it's just a little bit harder to spot obvious goofs. But, I don't think I'm not going to print like a transparent overlay like I did for the Rigol scope

**Dave Jones:** for this. I don't think I need to. I'm just going to fade between that and that, measure a few things, and Bob's your uncle. Um, hopefully we'll have a half-polished turd of a schematic at the end of this.

**Dave Jones:** Okay, so I'm part of the way through, and here's a progress. Pretty easy up until this point, and now I've got to do the feedback resistor on the op amp here. Obviously, it needs a feedback resistor. You can see that, as I said,

**Dave Jones:** R49 here, that seems to be the feedback resistor. Cuz, look, two traces bugger off under here like this. So, you got to assume that that one goes down there. I actually have put the product back together, so I can't actually um I have

**Dave Jones:** to crack it open if I want to measure anything at this point. So, this is obviously going to the output, which is pin six here, and you can see that buggering off to the output resistor divider here, and the relay switching

**Dave Jones:** for the gain. But, you notice that there's no other resistor here, and obviously the other side of this R49 here obviously goes to pin two. Pin three is the positive, so that's the input, and then pin two is the negative,

**Dave Jones:** the inverting input of the op amp. But, there's only one resistor. And if I drag that under like that, you can see that there's no other resistors on the bottom. So, if there's only a single resistor for the feedback like this, and it's a

**Dave Jones:** standard op amp, then well, then you can see like these are there's obviously an inductor here and a cap, which then are a couple of caps for different frequencies, which then powers the chip. So, that's filtered, but there's

**Dave Jones:** no other resistors here. So, obviously, by deduction I can draw that resistor in there is going to the um input like that. So, it's a unity gain buffer. I didn't think that op-amp was capable of unity gain, but apparently it is. No wackers

**Dave Jones:** whatsoever. There it is, 325 MHz unity gain bandwidth. Maximum bandwidth, 325 meg. It's plenty. And then, you'll notice that in here, the positive input here, it has two additional trim pots, which the negative side does not. So, obviously, they're using these to

**Dave Jones:** balance out the positive all the variances in the positive input compared to the negative input. This can improve your common mode rejection ratio. So, obviously, once you've drawn this one, you know that this one's going to be identical, except that one of the

**Dave Jones:** resistors in here is going to be replaced by one of the trim pots. And you'll notice that, sure enough, this has a block of four resistors here like this. This only has three of them. And it goes off to the resistor here. So,

**Dave Jones:** clearly, it's exactly the same, except this resistor here, which is R34, has been replaced by a trim pot. So, when you go in and draw it, there's our negative input there. That has fixed resistors. The positive one just has

**Dave Jones:** that one there just replaced by a little trimmer there. And the other trimmer down here like this is just to compensate for the gain divider that's fixed up here. And they just and then trim it. Somebody goes with their tongue at the right angle,

**Dave Jones:** and trims that sucker to the right value. So, there you go. That makes sense. I don't even need to buzz that sort of stuff out on the board, even if you can't see the traces going under the parts or what not, which, well, you

**Dave Jones:** can't. Like, you know, there's some traces under here, which I just physically can't see, but it's obvious that's where they're going. Now, here's a really annoying thing. I'm trying to trace out the microcontroller on here. What we've got on here is obviously a

**Dave Jones:** QFN uh 16 package. Four pins per side there. It's one of these EFM8 Busy Bee things or something bee. You get the data sheet and there's no There's an SOIC-16, but there's only QFN-20s. And sure enough, if I go to like

**Dave Jones:** Digi-Key and search for all of the Busy Bee parts, 596 of them, the only available packages are 16-pin chip scale and uh the SOIC and and the chip scale one is of course like the little BGA thing. Pain in the ass. So, that's annoying. Is

**Dave Jones:** it like an obsolete package that they've discontinued or something or is it in some other series that Digi-Key happened to not carry? Uh-huh. And that's a trap for young players including Dave. Quickly realize that yet here's the footprint. They're all QFN-20s. There's

**Dave Jones:** four extra pads on the corner there, which you can't actually see inside here like this. Like you zoom like I'm I've also got like a zoomed-in picture up here. And oh no, actually, I can just see it. There it is there.

**Dave Jones:** Maybe. Can you see a tiny little bit of solder on the side there. And there and sure enough, I should have known like there's a track going in there. There you go. Yep, another track going in there and another one going in there and

**Dave Jones:** that one's probably not connected or it's going under there. Don't and QFN-20. Don't rely on your mark one eyeball. Trap for young players. Anyway, my input here comes across here, goes over to here, goes over to here. That's a not

**Dave Jones:** fitted part and then goes into pin now that I know it's a 20-pin 18. So, yep, goes into pin 18. So, the feedback from the output goes into pin 18. So, looking at the pinout here, sorry I haven't got

**Dave Jones:** my green screen this time and couldn't be bothered turning my lights on, so yeah, whatever. Uh anyway, let's go down here to the package, 20-pin QFN. There it is there. So, pin 18 there is PO4. 18 multifunction IO, it's a PO mat.

**Dave Jones:** Whatever that is, it's an ADC. Okay, there you go. So, it's an ADC input comparator positive and negative, so I don't think they're doing any comparator function with it. Can't see why you'd do that on the output. This is this pin is directly

**Dave Jones:** sampling the output via two series resistors. That must be what measures the clipping for the output cuz you saw in the previous video how the uh LED button flashes if you get over range. That's how they're doing it. That's going into

**Dave Jones:** the ADC. And here's where we enter the bizarro world of the 6604. It's a SOT26-pin SOT23 package down here. And well, if you go look this up um okay, there's no 16604. So, if you actually know what's going on

**Dave Jones:** here, please leave it in the comments. But anyway, here's an MCH6604 from ON Semiconductor. Okay, it's a dual MOSFET as you'd expect in a six-pin package. If you know, you wouldn't get a six-pin package for a MOSFET unless you're

**Dave Jones:** you know, unless it's a dual jobby. This one's actually not a SOT 23 package, so it's not the actual one. Anyway, it's a dual N N-channel power MOSFET. And we'll have a look at the pinout in a second, but if

**Dave Jones:** we go over to this one over here, this is an Alpha and Omega one well, it's look, an N-channel and a P-channel. It's a six-pin SOT23. So, yeah, okay, right? So, you can, you know, use them like as a totem pole

**Dave Jones:** output or something. Like, you know, totem pole driver or something like that. You know, really handy kind of thing, motor drive, stuff like that. So, very handy. N-channel and P-channel in the same package. Nice. But, you go over

**Dave Jones:** to this one. This is a Toshiba TPC6604 jobby. And, well, let's have a look at this one. Um that doesn't look like a MOSFET. That looks like a bipolar. Um yeah, and it's a single. It's not a dual. So, what the heck? Um I found like

**Dave Jones:** three just searching three different types of 6604. Anyway, we If we go to the actual board in here, you can see they're actually connected in parallel. Whatever it is that they've got inside in here. Look, parallel like that. These are the gate

**Dave Jones:** terminals on one of the package, the gate terminals, and this was like the source, I think, on one of them or the drain or whatever. And, they're both connected in parallel, okay? And, that obviously goes off to the relay drive.

**Dave Jones:** But, this other one here, once again, they're connected parallel depending on the configuration, and that's going up here. And, I can't actually see under there, but well, I don't know where Like, I assume it's going over to the

**Dave Jones:** other side of the relay here. So, are they like differentially driving the relay? Why? I, you know, the micro's obviously driving this thing like the gate, this trace here if this is the gate, right? I like I think all the gates connected

**Dave Jones:** inside there like that. And, if you have a look on the bottom side, there's just a couple of There's just a couple of resistors and stuff in there. And, that'll go off to the micro which drives it, but I don't

**Dave Jones:** I don't know why or what the heck's going on with that relay drive. So, I'm not even going to bother to try and include that. Anyway, relay switch is on and off. Which like I can only assume that they

**Dave Jones:** use the 6604 as a standard ball item in many of their products and they just didn't want another type of transistor in here. But, there you go. Um no, they these are diodes. Okay, now I thought they were

**Dave Jones:** all three-pin transistor No, here's a No, Q. Q5, here's a transistor over here. Whatever that one is, 703. Why couldn't they use that to drive the relay, either? I don't get it. All you need's like a standard BJT to drive the or a MOSFET or

**Dave Jones:** whatever single to drive the relay from like the plus 12-V rail or what a plus Yeah, it's plus minus 12, isn't it? Or whatever. And Yeah, I don't know. I don't get it. All right, so we've got my final DaveCAD

**Dave Jones:** here. Only final because I really couldn't be bothered going in here and like reverse engineering the AFM8 and the U6. And you'll see why in a second. Anyway, on we've basically come to the conclusion that here's the output

**Dave Jones:** resistor here, 50 ohms, 49.5 and 9 ohms, good enough for Australia. And that drives the coax out here. And then we're actually I don't know why they're tapping off two here, but they tap off the output here and then this goes into

**Dave Jones:** a dual op amp. Oh, I forgot to put the part number on there. But, anyway, it goes into a dual op amp in a standard inverting configuration. Here, it's just drawn a bit differently. Don't When you look at building blocks like this, the

**Dave Jones:** positive goes down to ground there via a matching resistor. I've done a video on this and how that matches input bias currents and things like that. But, anyway, you don't necessarily have to have it. You can just ground the non-inverting input

**Dave Jones:** there. And that's a standard inverting op amp. I don't know where that actually goes out to. I presume it eventually goes back into the micro somewhere because what is the functionality of this thing? It just simply reads the

**Dave Jones:** output and and flashes the LED for like over range and and then it controls the relay here. So, yeah, like that'll have a like a transistor that weird ass 6604 transistor driver in there to drive your jewel relay here.

**Dave Jones:** And which switches the gain by the way on both of the channels. But anyway, so the EFM8 it doesn't really have to do much. But if we have a look at the actual board for this thing, the bloody

**Dave Jones:** thing doesn't retain my zoomed in status. Anyway, here it is. So, here's our 50 ohm output resistor. This is our coax up here. I've just zoomed in a bit more and here's R26 that we had there and that goes into this op

**Dave Jones:** amp. Whoop, it goes into the op amp here. So, this is I don't know what part that is. A TI98. I had a look, OPMI. Had a look, I don't know. If you know what it is, leave it in the comments down

**Dave Jones:** below. But anyway, it looks like it is a TI jobby of some description. Couldn't be bothered decoding the part number. But anyway, yeah, so the top half of the op amp in there is a basic non-inverting sorry, inverting op amp.

**Dave Jones:** So, I I don't know what the bottom op amp here is doing and look at all these parts around here. I don't know what's going on there. But anyway, like once again, I I put this thing back together. And I so

**Dave Jones:** I haven't bothered to actually I don't have access to it again. I couldn't just couldn't be bothered taking it apart to get into the nitty-gritty detail. But look, there's a lot of stuff in here and what these diodes over here are doing

**Dave Jones:** and and stuff like that. They've got three diodes over here. We know that this tap R22 as we saw on the schematic. This goes down here. This jumps. This actually jumps over to on the bottom side over to here and this is what then

**Dave Jones:** goes into that pin of the micro that we saw which is actually either an ADC or a comparator. I don't know where yeah, I don't know what how it could be a comparator. So, I think that they're using that as an ADC, but why they have

**Dave Jones:** to read off both sides of this? I presume maybe it's got another error detection mode to detect shorted output like, you know, the load is shorted. Your oscilloscopes, you know, you shorted the output or whatever. So, yeah, I don't know, but there's an

**Dave Jones:** awful lot of stuff in there for micro that's its only purpose essentially is to drive this relay off and on when you push a button. You know, which range do you want? The times 10 or the times 100 range and it just switches that

**Dave Jones:** relay and then it just flashes the LED when it's over range. So, all it needs is like it an op-amp and like the ADC and Bob's your uncle. So, I don't know. I don't know. If you've got any ideas, leave it in the comments

**Dave Jones:** down below, but yeah, I couldn't be bothered actually reverse engineering the whole kit and caboodle. So, anyway, um yeah, this is rather interesting. There is so I am actually surprised that they use quite you know, like 1206 parts in here. I

**Dave Jones:** thought, you know, I'm surprised it survived the 1,100 V RMS that we actually put on it cuz normally I think 1206s only have a 250 or 300 V rating each, don't they? So, you know, like you really like yeah, you're pushing your

**Dave Jones:** luck there. But, it's interesting that this one and I think somebody on the forum mentioned that one of the higher end models doesn't have these trimmers or doesn't have one of these trimmers or something like that. I think it's the

**Dave Jones:** CMRR one from memory. So, yeah, there So, anyway, they have added a common mode rejection ratio trimmer in here, which just means that you're matching cuz common mode rejection ratio will involve you know, if these are unmatched, if the value of this string

**Dave Jones:** here, which includes these resistors and the lower divider resistor here, then if they're unmatched, I should show you the schematic for this. So, if they Bloody Yeah, why can't you keep the zoom status? What's going on here? Maybe

**Dave Jones:** there's a setting. I don't know. Anyway, I'm using Drawboard PDF for those who don't know. It's got like this laser tool that can, you know, if you draw it like this, it'll go like that. Really cool. And you can just

**Dave Jones:** do up the, you know, annotate PDFs. It's really quite cool. Anyway, I think it's designed for like It's an Australian software which is designed for like marking up PDFs for like architects and things like that, I think. And stuff like that. Anyway,

**Dave Jones:** we can have a Yeah, so if if this entire string here is unbalanced compared to this one up here, and that's going to screw up your common mode rejection ratio. So, that's why they have the CMRR trimmer in there. And then they've got a

**Dave Jones:** gain trimmer here just to match the gain for the differential amplifier here. This is a standard differential, single op-amp differential amplifier circuit. They aren't using like a specific diff amp. It's just a very high-speed regular op-amp. And that's it. And they

**Dave Jones:** just do the relay switching here for the gain, which is determined by, of course, these resistors here and this one and these here. So, they they determine the gain of this cuz these are just buffer amplifiers here. And that's it. Got a

**Dave Jones:** little bit of compensation there. And this up here is interesting. This is a They've got a a resistor on the bottom. NF means not fitted. So, that's just a common thing on schematics. If it's not or do not fit or, you know, DNF or

**Dave Jones:** something like that. Not fitted, DNF. And yeah, so they've got these footprints for the resistors. But this capacitor here, I've have it as a shared capacitor. Cuz if we go over to the board here, you can see on the top side

**Dave Jones:** here that the resistors aren't fitted and they've got these just pads. And of course, but a pad with another pad on the other side is a capacitor. So, yeah, they're just using those and they got one big square pad on the bottom like

**Dave Jones:** that. I don't have the other one loaded up, but they got one big square pad and there's another resistor in here like this, which then goes to yeah, here. It It goes to here. So, it's across that resistor there. So, they got some sort

**Dave Jones:** of like compensation network that uses the PCB pads and I'm not sure, you know, it's obviously like some sort of upper resistor compensation or something. I don't I don't know what the If you've got any idea what they're trying to

**Dave Jones:** actually do there or tried to do I They didn't do it on the production version, obviously. So, yeah, anyway, and they've got dual compensation down here like this, which is, you know, going to town a bit. Don't know why they need the dual

**Dave Jones:** compensation, but But anyway, like I haven't gone in like measured part values and stuff like that. We just really want to look at the topology of this thing and it is a pretty bog standard uh you know, implementation of

**Dave Jones:** a high-voltage differential amplifier. The high-voltage straight The high-voltage resistors like this, the lower side of the resistor divider completely matched um positive and negative and this is Once again, have a look at that video of how a differential

**Dave Jones:** probe works. I go into a bit more detail, but there you go. Um that's Yeah. Interesting. Anyway, I don't know what all this stuff and what's going on here. I don't It's strange. Got any idea? Leave it in the

**Dave Jones:** comments down below, but I hope you found that video interesting. If you did, give it a big thumbs up. As always, discuss down below. Catch you next time.

**Dave Jones:** Mhm.
