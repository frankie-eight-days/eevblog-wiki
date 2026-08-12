---
video_id: rWBjeB9JP3Y
title: EEVblog #738 - Yamaha DME32 Digital Mixer Teardown
url: https://www.youtube.com/watch?v=rWBjeB9JP3Y
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Tearown Tuesday. We got another interesting bit of kit here from the professional audio industry. I like this kind of stuff cuz it's not something that you get to see every day and it's not a piece of consumer item

**Dave Jones:** that's built down to a price. These are very expensive bits of kit and they've basically spare no expense inside these things. They're built for reliability, built for quality, not trying to meet some stupid consumer price point. So, we've seen this uh previously in the

**Dave Jones:** Sony video uh Matrix Switcher special effects thingamabob, which I'll link in here if you haven't seen it. And it was like superbly engineered and just a massive bit of systems engineering. I expect this one to be quite similar.

**Dave Jones:** What is it? It's a Yamaha DME 32 or digital mixing engine. I don't know huge amount about the um the professional audio industry. What I do know is that it's basically a digital equivalent to one of those analog mixing desks. You've

**Dave Jones:** seen those huge analog mixing desks with the th hundreds of, you know, uh dials and and uh knobs and everything for every bandwidth and every input and they mix all the signals in the analog domain. Well, this does basically the

**Dave Jones:** same thing, but does it in the digital domain. In fact, you can actually get a proper mixing desk which hooks up to this, but it's all digital. So, instead of using like analog pots and op amps, they're actually u like they're motor

**Dave Jones:** controlled. I think they can like move on their own. And it's basically a digital input to drive this. But this is the thing that has the analog to digital converters and the digital analog converters in it. And you can basically

**Dave Jones:** do exactly the same thing or more than you could with the analog mixing desk. And well, you know, your afficionados out there might uh prefer the analog sound. But uh if you want all your special effects, then these sorts of

**Dave Jones:** digital mixing engines cuz they're DSP based can do basically anything you want. They can correct. They can mix uh signals together. They can equalize um bandwidths. You can put in filters. you can correct for speaker and room acoustics and it's just endless what you

**Dave Jones:** can do once you sample the stuff in. So, we expect some high-end analog to digital uh converters in here, digital analog converters. Very wellmade as well. And well, let's check it out. And thank you very much for Matt for

**Dave Jones:** donating this thing for the tear down. Matt is the one who just bought in that uh 3D um 360 degree uh camera that I used to shoot that you just saw previously. So, thank you very much, Matt. You know what we say here on the

**Dave Jones:** EV blog. Don't turn it on, take it apart. Here's a closeup of the front paddle. And as you can see, very spar. We've got a couple of digits here telling us which scene we're on. Whatever that means, configuration, the

**Dave Jones:** scene. I don't know. It seems to be all about the scenes. a uh encoder knob for the data and uh setting parameters, components, values, what sample rate we're working at, 48 kHz or 44.1 kHz, uh whether or not it's locked. Oh,

**Dave Jones:** emergency warning, Will Robinson. I don't know. You know, the global data clock got lost or something. Um a couple of controls to set things and scene recalls. So, it's all about scenes. And looks like you can save stuff to um PC

**Dave Jones:** MCIA card. Yes, this one's a little bit old school, but as you can see, clearly not designed to be like operated from the front panel. Designed to be operated from either the optional uh digital mixing desk and or a uh PC of some

**Dave Jones:** description, something like that. And on the back here, we can see that it's a modular slotbased system. There's four slots here. We've only got three populated, but this is a uh 24bit 96 kohertz analog uh to digital converter

**Dave Jones:** output. And then we've got two input uh two eight channel input modules here. So obviously you can configure them with whatever input and output you need. Uh curiously they got TRS um jacks here and and a D25 for the analog output. So

**Dave Jones:** that's you know rather interesting rather than your XLR your traditional XLR connectors and uh things like that. So I'm not sure what's going on there from a a system point of view. We've got external uh word clock here. This is for

**Dave Jones:** the uh converter. So, you can actually uh synchronize all of your system to the one uh sample clock. And it's got uh MIDI in and out. Uh PC control of course, serial uh port here. You can go RS422 or RS uh 232. And then you saw

**Dave Jones:** that USB connector on the front as well. This hooks, you can use either of these to hook up to a uh PC. It comes with um or it might I don't know you might have to pay extra for it whatever but it has

**Dave Jones:** Windows-based mixing software so you can do all the digital mixing just you know looks and feels just like a real analog mixer um but controlled by a PC and then we got cascade in and out. You can cascade multiple units together for

**Dave Jones:** however many channels you want. And these Phoenix connectors here, these are all uh general purpose IO, so it allows them, you know, you can control whatever it is, you know, stage equipment, all sorts of rack gear or whatever.

**Dave Jones:** Basically, whatever your imagination can think up here in your live scenarios, cuz these are these are typically um used in like in the field for setting like a you know, a concert performance or something like that. So, they're

**Dave Jones:** going to ship one of these around in a Pelican case or something like that. Then all the roadies have to, you know, set it all up on site and things like that, possibly with PC control and or a

**Dave Jones:** digital mixing desk and then wire everything in and they have, you know, all things preconfigured for what that particular band's requirements are. So, here we go. Let's crack the lid. And what I expect in here is uh lots of lots

**Dave Jones:** of huge big ass boards. Uh lot it's going to be all surface mount. This is not ancient. This is not like 80s or 90s or even 90s stuff. This is, I believe, like early 2000s or or something like

**Dave Jones:** that. So, uh it should be reasonably modern. Uh possibly lots of ASIC um stuff like we saw in the uh uh the Sony video mixer uh for example. So, you know, Yamaha, a uh pretty big company. they might uh they might roll their own

**Dave Jones:** chips cuz they did back in the day. Um and you know it wouldn't surprise me that they still do that sort of thing. So and I expect uh yeah no corners to be cut. They're going to be using quality

**Dave Jones:** caps. They're going to be using uh you know real expensive high performance uh you know analog devices maybe um ADCs and DAXs for example in the boards. I probably could have just taken the boards out the uh out there and had a

**Dave Jones:** look at those first. But anyway, let's see all this. Lots of system engineering goes into this thing. It's going to be enormous. I don't think it's just going to be like one simple microcontroller. And woohoo, look at that. Jackpot in like

**Dave Jones:** Flynn. And it seems I've lost my little black pointer, so I have to use the screwdriver. People will complain. Check out this. Wow, this is a huge top board. There's going to be there might be another board underneath, but the

**Dave Jones:** modules actually plug in the back. Not sure how far they actually uh go into it. Got our power supply over here. We'll check a look at take a look at, but look at this. Yamaha Yamaha Yamaha Yamaha. Everything's Yamaha. Now, might

**Dave Jones:** be able to Google those and maybe get some of the numbers, but obviously we've got some memory here. These are going to be like uh custom A6 um designed by Yamaha specifically for this. I'm pretty sure we've got an offtheshelf uh

**Dave Jones:** processor which we'll take a look at, but these might be doing uh these are you know the DSP the switching. Who knows? They got a lot of memory um surrounding them. So not sure what uh what's going on there. But it

**Dave Jones:** looks like all of our inputs are coming from over here. If we have a look at have a look at that. this ribbon cable down. There's actually a whole bunch of ribbon cables. I'll show you here in a

**Dave Jones:** minute. There's four bunches of ribbon cables. They're all coming through here. We've got uh uh some are they some sort of buffer? Something like that. Anyway, into all these these are doing all your heavy duty processing and things like

**Dave Jones:** that. You might notice a few bodgege wires in here. Look at that. Couple of green ones going over there. Big black one running all the way down here. Nicely dobbed down like that. Look at that. Another one in here. This is very

**Dave Jones:** common in this sort of pro gear. They design these boards. Takes a massive many, many years to design these things. And countless engineer hours go into this. And you might find an issue when they write down the track that they go,

**Dave Jones:** do we we don't want to respin the whole board? What the hell? Cuz we don't make these in huge volume. So, let's just put a bodgege wire in there and she'll be right. and they can, you know, do these

**Dave Jones:** professional uh mods in there. And it's very common in uh high-end professional gear like this. So, what would you have here? I don't know. Your guess is as good as mine. These monsters over here could be uh the D the main DSP. Uh

**Dave Jones:** perhaps all the like all sort of like the high-end heavy lifting stuff done over here. These seem more like individual uh filters. cuz I mean we've got sort of, you know, 10 of them there. Um, all of our inputs seem to be like

**Dave Jones:** eight channel cards and things like that. I don't know. Each one of these could be doing um, you know, um, programmable filter function that you download to them. Who knows? They could have a specific use. They could have uh,

**Dave Jones:** pre-programmed lowass, highpass filtering or something like that in them. N, who knows? But what is very clear is that this board is almost entirely digital. It's, as I said, all the um there's four ribbon cables coming over here from the module. So, all the

**Dave Jones:** analog to digital and digital to analog conversion, all done on those plug-in modules as you'd uh expect. So, this is all just the digital DSP processing. And then we've got ourselves the main processor here, which is a Hitachi SH2,

**Dave Jones:** one of these Super H processors. But Hitachi, of course, been bought out by Redus. And now they I think they still do this uh part or you know a variation of it. They still do the super H uh

**Dave Jones:** processor. The reason for all the uh different footprints here is so that during development um it's it's not like you know another chip plugs into there but they can actually plug in a uh realtime incircuit emulator in there for

**Dave Jones:** example and actually um emulate this uh chip emulate this processor and do all sorts of incircuit serial emulation in circuit emulation and all sorts of that jazz during development but during production n they don't need it anymore. And next to that, we've got ourselves an

**Dave Jones:** Alira Max CLD there. It's a silk screen with the model number DME32. So, uh, pre-programmed by Alira, perhaps. Now, this is interesting. We see this at multiple points around the board. This uh anchor screw here mounted to the

**Dave Jones:** metal chassis has its own isolated copper on there, but the designers have left in little exposed pads where somebody at the production stage when they've assembled this board has gone, we want to connect the chassis through to the main ground on here. So, let's

**Dave Jones:** connect these points up by adding these solder blobs. And this is at in several locations around this board. every mounting point. In fact, you can see the digital IO at the back here has its own separate ground plane. And you'll notice

**Dave Jones:** those exposed copper pads there, there, there, which they haven't joined up. They haven't joined the ground at that point. Look all the way along. See them? There, there, there. Where does it join? Bingo. Right at the end over here. So

**Dave Jones:** the designers have gone well let's solve our uh grounding issues at the final stage depending on maybe you know system or customer or model requirements we may actually have to join the grounds at different points. So maybe the designers

**Dave Jones:** were hedging their bets here. Okay let's figure out later where our optimum uh you know star grounding point is going to be. Is it here? Is it going to be in the center of the board here for example

**Dave Jones:** over here or should we just join them all together like that later in production? So maybe they'll hedging their bets. Maybe it's something to do with uh different model um or you know customer requirements configurations something like that perhaps. And check

**Dave Jones:** out this digital cascaded uh input input and output around here. Check out these Murada. These look for all the world like and the designator is almost a dead giveaway em. Now these are almost certainly some sort of um EMI uh

**Dave Jones:** filter for example some sort of you know network array sort of eight channel uh kind of thing handling eight channels a pop. So they're really serious about EMC on these things. And you can see over here as well look EM as well. Not the

**Dave Jones:** same uh networks but obviously they're uh uh doing a couple of uh signals here for the PC. This is like the RSR 42 uh 485 and the COM interface there. So yeah, they're putting some filtering on the line. They've got it also here over

**Dave Jones:** here. Little um EM filter for the input and output uh data clock and aha I was kind of right. The I looked up these YSS910 S's and these are uh yes custom LSIs large scale integration or ASIC or

**Dave Jones:** whatever you want to uh call it. basically ASIC chips from Yamaha and they claim that they're the world's first 44bit DSPs. So each one of these chips is an individual DSP like that. So they got 10 DSPs all around here, all with their own

**Dave Jones:** local memory as well. And they're upside down, so all the electrons are going to fall out. Oops. And these other three bigger ones, YSS 904Fs, all I can get on those at the moment is that they are once again DSPs. So, they've got an

**Dave Jones:** additional three DSPs. And it looks like they are sort of uh coupled into these. You can see some of the uh routing there perhaps like it's Yeah, it's got to be going over here. And yeah, they eventually sort of crossoupling these

**Dave Jones:** DSPs, however they're doing that. But yeah, this thing is all DSPs as we expected. So you can probably guess that this uh Super H processor up here is just running things like the LCD and the user interface and you know all that

**Dave Jones:** sort of miscellaneous uh control stuff and PC control and and cascading control and all that sort of stuff. I don't think it's doing any DSP at all cuz the whole idea of this thing is that it all does DSP directly in dedicated hardware.

**Dave Jones:** And that's the thing you might be wondering, well, why don't you just do this in a PC these days? Well, maybe they do, but um when you've got so many channels like this, having dedicated DSPs in here, it's all about latency and

**Dave Jones:** throughput and all that kind of stuff. You try and put it through the one PC processor. Even if it's, you know, the top-of-the-line Intel i7, it's probably going to choke. You could have latency issues or whatever, interrupt issues.

**Dave Jones:** You don't want any of that. You want dedicated hardware like this. It's just much nicer to do it in dedicated hardware. You get a guaranteed known result, no issues whatsoever. It just works and will always work. By the way,

**Dave Jones:** if you're wondering what that Alter Maxa CLD is doing, I see a couple of traces sort of running up here towards the Cascade uh circuitry. So, maybe it's like the dedicated cascade uh controller for just uh syncing together multiple

**Dave Jones:** units perhaps. I'm liking the look of that crystal from NDK down there. Of course, made in Japan. All of this stuff made in Japan. What are you talking about, Doc? All the best stuff's made in Japan. There you go. That's probably

**Dave Jones:** like a PLL for the uh crystal or something perhaps. I, you know, just by the locality of it uh really. And uh this could be like a um TXO or something, temperature compensated crystal oscillator. Once again, custom ASIC by Yamaha. They just do all their

**Dave Jones:** own silicon. Absolutely amazing. And the only hint of any sort of like analogy or uh power stuff on here is this package. Check out the uh the power pins there. They got the large pin either side acting as a so this is some sort of

**Dave Jones:** large current device by proximity to this rimman cable which looks like it's going towards the seven segment lead display on the front. I'm going to say that's some sort of uh high current lead display driver. And it's interesting to

**Dave Jones:** note that this DSP here has its own 40 megahertz processor. Look at that. All nicely isolated there. So it does is this the master clock for all of the rest of these um all the other all 10 of

**Dave Jones:** those DSPs. And it did give away that this board is digital only. This is the only input power connector 5 volts and 3.3 volts. Thank you very much. Now let's cast our eye over this power supply. I think we might find a

**Dave Jones:** interesting thing or two in here. I love this switch on the front panel. Look, got its own board. It's got big beefy dedicated connectors going down in there. Oh, love it. That's just a beautiful power switch spared. No

**Dave Jones:** expense there whatsoever. I'm seeing uh HRC input fuses. Big ass mo there. We got big ass uh filtering right there. We got a ferite clamp on there just to take the edge off the um RF on this thing.

**Dave Jones:** And well, it's looking very good. Can't see the brand of those caps, but uh you can bet your bottom dollar they're going to be the best ones you can get. And here's something very nice. I like this. Look at this power supply module.

**Dave Jones:** Instead of just putting these uh no presume output power uh transistors slash regulators here, instead of just having them on the board freestanding with little individual heat sinks, no, they've taken the whole back chassis like this, the whole back frame of the

**Dave Jones:** power supply, actually bent and cut that out and then bent it in and used that as a heat sink and mounted them on the bottom. Soldered them through the bottom of the board. Somebody was really thinking there use this whole thing as a

**Dave Jones:** heat sink cuz this thing does not have a fan in it. So it's, you know, it's whisper quiet and it, you know, that's how they can probably get away with it. Not sure how much power this thing uses.

**Dave Jones:** We might be able to see if we have a look down in the label down there. Can't quite uh see it at the moment, but that is just Yeah, that's just very nice indeed. And just small touches like

**Dave Jones:** instead of just having this cable here flap around in the breeze. Put a little cable tie on it there and clamp it to the fite case. Ah, gorgeous. And here we go. I've swung out this power supply. It's still connected. Look at the

**Dave Jones:** isolation here between all the input. Uh we got ourselves the common mode chokes. Look at the input uh filter in here. Just absolutely brilliant there. Monster common mode chokes. Monster filtering. all properly rated. And then these transformers would be the ducks guts as

**Dave Jones:** well. No doubt. And sorry you can't see that, but these are Nippon Chemicon, of course. One of the best in the industry. 105° C rated. Thank you very much. So, obviously very uh carefully chosen. They would be, you know, the right uh

**Dave Jones:** particular model with the right ESR with the right brand. Looks like they got many in parallel over here. I don't like the fact that they are sort of flapping around in the breeze. They did put some salastic on the base of these ones here,

**Dave Jones:** but these ones over here are flapping around. But jeez, I think I'll forgive them for that. Um, yeah, but no, no dodgy caps in this thing whatsoever. And yeah, no shortage of output filtering. Actually, if you can just see that this

**Dave Jones:** looks to be a Na brand. So, it looks like they have uh shop this out, but also made in Japan. And uh you can probably see the various voltages and currents on there. Not sure of the overall power. You'd have to add them

**Dave Jones:** all up. And by my calculations, that's a 48 watt output power supply. And let's see if we can remove this entire top board, shall we? We've disconnected all the cables, taken off all the jacks at the back, and it's

**Dave Jones:** not trivial, but tada, it's out. Beauty. Hey, look at that. Not a huge amount more in here. So, we just got one baseboard down on the bottom. It's just got one main ASIC down in there. That's not a Yamaha.

**Dave Jones:** That's just an offtheshelf uh kind of like a PC type chipset. This is the uh PCMCIA and USB board. As you can see, the P the USB connector is right down there going to the front panel. Got a

**Dave Jones:** PCM old school PCMCIA adapter. And that all goes over via these ribbon cables here. Not else much doing. We got some uh power coming in there. And then the rest of it, as you can see, the four main ribbon cables all connecting

**Dave Jones:** through to this uh motherboard at the back here, which then connects our four slots with their own card cages. We'll take those out separately. And there's one little board on the back for the digital IO. And that digital IO board's

**Dave Jones:** worth a squeeze. Check this out. Once again, they've got some very nicely bodgege resistors on there. Look, they're putting tape under there so they don't short anything out. Individually sleeved these resistors on the top here and then bust them all together like

**Dave Jones:** that. So obviously u they're doing some sort of pull up there cuz it's all common. So they decided, oops, yeah, let's not respin that board. Let's just mod them. Although a really small board like that, I don't know why you wouldn't

**Dave Jones:** have respin respun it cuz that's a fair bit of manual labor on there. So maybe it is cheaper to just to have somebody, you know, if you got a huge stock of these boards, maybe yeah, you don't want

**Dave Jones:** to scrap them. So yeah, maybe it is cheaper just to uh get them to uh redo that. you're paying some assemblers time, you know, 10 minutes per board or something like that instead of a scrapping all the boards, b the design

**Dave Jones:** effort to redesign it, see to re all the parts to respin it. So, yeah. Okay. And there's the entire back side of the board. Mostly just uh bypass caps and a few uh miscellaneous diodes and resistors and things like that. They

**Dave Jones:** couldn't uh populate on the top here. But we we got one bodgege there and we have another very interesting that's a complete bodgege board right under the main processor. So yeah, I'm not sure what the go is there. But check this

**Dave Jones:** out. They've actually sucked out have they actually sucked out the uh solder that was left in these uh pads from this incircuit emulator thing. Sucked that out to get your wires through to the other side of the board. And that's

**Dave Jones:** actually not uncommon actually to use. And in fact, one of the advantages of using uh you know, large pads and large vas, for example, is that you can actually fit mod wires to go from one side of the board to the other cuz

**Dave Jones:** that's an often um that's a a very common requirement when you mod boards like this. How do you get a wire from a trace on the bottom of the board to the top? Sometimes, yeah, it has to be

**Dave Jones:** really ugly. If you got to drill a hole in there, and if it's multi-layer, well, that can be a real pain in the ass. You don't want to short out your inner layers. Um, that's bad if you got like 5

**Dave Jones:** volts and ground like this one is. You can tell by all the dark all the darkness under there that obviously this is a four layer board. So, it's got one big uh copper uh plane in there for your

**Dave Jones:** uh ground and also it's not going to be three layers. They're always like a an an even number almost always an even number of layers. So, they're going to have four. So, they're going to have um the power and uh ground planes in there.

**Dave Jones:** So, if you drill through, just be careful. you might short out your power planes that will ruin your day. Um because you can get burrs between the layers anyway. Very common to have to get them. Like sometimes you might, you

**Dave Jones:** know, if you're desperate, you have to run say a mod wire. Oh, I need this track and I need to go, you know, I can bodgege it into this track. I need to run the wire all the way over here, wrap

**Dave Jones:** it around the edge of the board and go all the way back over the top. And that's a pain. If you can find a shortcut to just jumper under like that, but that's that is very nicely done. I

**Dave Jones:** mean, that's, you know, about as professional as you can get if you're doing mods like this. And you can see the same rear panel ground split here and those little joining uh traces there. And where does it join? Where

**Dave Jones:** does it join? Where does it join? No surprises for guessing. Exactly where it joins on the other side. There's the little solder blob. And here's the 24-bit analog to digital converter board, 96 kHz. Let's take a look at it.

**Dave Jones:** Uh, pretty simple. We've got a secondary uh daughter board up here. So, these are our um I I don't know how many uh channels. I'm going to presume it's uh maybe eight uh channels and there's four um output uh buffers there. They're

**Dave Jones:** going to have identical circuitry underneath there. So, I won't bother taking that off. We can see we've got uh I can see that they're JRC Japan Radio Corp um op amps. So, we'll take a closer look at those. Get the exact model

**Dave Jones:** number. Interestingly, it's all throughhole. Um, uh, well, it's, you know, mostly like through hole resistors and caps and things with surface mount chips. So, that's a bit unusual. Um, yeah. Are they guilding the lily there in terms of, oh, these are lower noise,

**Dave Jones:** these suckers, than what they can get in SMD. Anyway, um, dual side load, which is, uh, a bit interesting. Then they've bent all the leads over and put the silk screen on the bottom. Anyway, very professionally done. I got uh no issues

**Dave Jones:** with that at all. It looks quite nice. And we've got ourselves a XYLink FPGA by the looks of it. No, that's not an FPGA. It's an insystem programmable CLD, the XC9572. It's only got 1500 gates, like 72 macro um cells. Not a huge uh deal.

**Dave Jones:** It's just doing some uh glue logic for the um interface stuff for our digital to analog converters. There they are. So, they must be Well, there's only four of them. We've got some uh looks like these are probably buffers. I can take a

**Dave Jones:** look at those numbers are a bit hard to read there. So, is this this is almost like it's got some conformal coating on this board actually. H anyway, these are just going to be uh buffers, I think. And yeah, I checked. They're very hard

**Dave Jones:** to read the numbers on there, but they're um 74 HCT245. So yeah, just buffers. Aha, these are Wolfson ones. WM8740s. I'll link in the uh data sheet down below so you can take a look. These are stereo decks. So we've got um four

**Dave Jones:** stereo decks on here. So we've got eight. So basically only four stereo uh channels for this whole thing or eight channels um total. I'm not sure. I don't know if they're running stereo uh pairs here. It could just be eight channels or

**Dave Jones:** however you want to configure it. Anyway, um they are very high performance uh you know like you know worldclass uh 24-bit um audio DAXs uh 192 kHz now owned by Sirrus Logic. Wolfson got bought out there but it

**Dave Jones:** turns out you can uh still buy these puppies. They're of course from uh made by Sirrus Logic now, but they're still under the uh same part and the same Wolfson part number about four bucks each in uh 2,000 quantity. And then the

**Dave Jones:** output of our DAC goes there's probably some filtering in there goes to AHA analog devices OP275 as the 275G. And this is a bit of a special puppy. It's specifically designed for the uh you know as an audio

**Dave Jones:** file class op amp 06% distortion. Uh massive 9 MHz bandwidth and it's got in quote marks excellent sonic characteristics. Ooh and it's got a special front end. It uses a butler front end which is a combination of JFETs and uh bipolar. So yeah, super

**Dave Jones:** duper special. Oo, we are not worthy. So it seems like there's running some sort of active uh you know filter around there and then the So we go from our deck to uh and some sort of active uh

**Dave Jones:** filter and maybe some sort of uh band pass filter and then running into our output uh driver. No surprises for finding the Japan radio corp uh 4580s in there there. You know, once again, audio class output uh driver op amps, you

**Dave Jones:** know, trip 5% distortion, all the usual business. And check it out. You don't see so caps that often. And they're just way off the board there, flapping around in the breeze. That's a bit how you do it. But the reason they've done that,

**Dave Jones:** you can see that they've got formed legs. So, they're designed to uh stand off the board like that. And then here's our analog to digital converter board. So, we've got our eight input uh channels there with our TRS jacks. And

**Dave Jones:** no surprises for finding exactly the same audio grade opamp OP275s in there that we had before. So, we've got some um so these are our input amplifier. Got some uh filtering happening there. And look, each channel has a selectable um gain uh either plus

**Dave Jones:** 24 dB or uh uh plus 4. So, I guess they're, you know, they're they're user adjustable. You can just pull these out and set whatever um input gain you like. And once again, they're running just the secondary daughter board there to get

**Dave Jones:** the extra um four channels on top there. So yeah, exactly the same circuitry underneath. If you can see the switches as well. And then we've got the output of our input amp going into surprisingly um a pretty Joe Blogs dual opamp. Once

**Dave Jones:** again, Japan Radio Corp 215s. And they're really nothing special at all. So, they're doing um like a two- stage uh filter in there. High pass and uh uh low pass perhaps. Well, they they do look like identical stages just based on

**Dave Jones:** the layout of the uh components. So, yeah, maybe they're doing a uh a cascaded filter there perhaps and going into our analog to digital converter. Let's check it out. And once again, no surprises for finding Sirrus Logic in

**Dave Jones:** here. Uh no, these aren't Wolfson ones. These are Cirrus Logic uh designed and branded CS5360s. Once again, 24bit um you know, really high performance uh audio class uh Delta Sigma um analog to digital uh converters. So, no worries whatsoever.

**Dave Jones:** And then we've got those just going into some uh once again HC245s, HC1 138. So, we just got some uh decoders and some buffers there. That's about all she wrote. So, nothing fancy on uh these boards at all. They just got as their um

**Dave Jones:** just got their basic functionality ADC or DAC and some uh glue and interface logic and that's about all she wrote. No components on the bottom of this sucker. Notice all the grounds separate. Of course, they're going to design this

**Dave Jones:** properly. They're not going to uh do, you know, a real high performance industrial uh product audio grade uh thing like this and goof up all the uh grounding and not have uh separate grounds for each channel. coming back to

**Dave Jones:** some uh star point. So yeah, they're going to be getting that right. Bet your bottom dollar. So there you go. That's a tear down of a professional Yamaha digital mixer as opposed to one of these um analog ones. And yeah, very

**Dave Jones:** professionally are designed and manufactured as you'd expect uh expect. They really, you know, spared no expense in these things. I'm not sure how much it's worth brand new, but they are, you know, if you have to ask the price, you

**Dave Jones:** can't really uh afford one. They're, you know, designed for, uh, big, you know, uh, bands and, uh, you know, touring um, things and, you know, or even studios or or something like that. Really, um, kind of like world-class stuff. This one is

**Dave Jones:** obsolete now. I think there is an upgraded model uh, to it, but all of the custom DSP processing in there. Absolutely incredible stuff. Imagine the amount of engineering design hours which went into making this. Absolutely phenomenal. So, I hope you enjoyed that

**Dave Jones:** and if you liked it, please give it a big thumbs up on YouTube because that always helps a lot. And if you want to discuss it, jump on over to the EEV blog forum or leave YouTube or blog comments

**Dave Jones:** and follow me on Twitter and all that stuff, but not on Facebook cuz I don't give a toss about Facebook, but I do tweet a lot. So, um yeah, people do ask, "Do I have a Twitter account?" Yeah, bet

**Dave Jones:** your ass I have a Twitter account. And yes, I don't have somebody who sends tweets for me, you know. I'm not one of those celebrities who uh who you know, it's not like Dave's over here. David over here. David 2 is laughing there

**Dave Jones:** behind me. No, I'm not going to get him to like send my tweets now. My tweets are my own. And yes, they're not always about electronics. So, yeah. Anyway, um as always, high-res tear down photos available on evblog.com if you want to

**Dave Jones:** take a look at those. Catch you next time.
