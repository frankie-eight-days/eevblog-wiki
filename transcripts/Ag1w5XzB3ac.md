---
video_id: Ag1w5XzB3ac
title: EEVblog #922 - Mailbag
url: https://www.youtube.com/watch?v=Ag1w5XzB3ac
source: youtube-asr
---

**Dave Jones:** Hi, welcome everyone's favorite segment, mailbag. I don't actually have too many on the shelf compared to the backlogs I've had recently. So, this won't be like 20 items or something. So, it might actually be a bit shorter. Anyway,

**Dave Jones:** let's get straight into it. Thank you very much Anthony Anthony Fitzpatrick. He's from Western Australia, WA. So, hi to all my Western Australian viewers.

**Dave Jones:** Let's have a look. We've got ourselves a hard case. Woah! Tech Tools Tektronix, huh? Huh? Let's have a look. Here we go. Come on, there's a note. Oh, okay.

**Dave Jones:** Here we go. Woah, oh, oh, it's one of those. Yep. The uh sponge has completely deteriorated. Oh, yep. Oh, woah. Anyway, what is this? I have not seen this before. It's a Tek RFM 90 signal mini. Beauty. Check it out. Tektronix RFM 90 signal

**Dave Jones:** mini. It's an RF TV antenna signal strength meter, basically. Check it out, made in Spain. Hi to all my Spanish viewers. Does this mean that it's actually not a bit of Tektronix kit and they've just rebadged it from someone else? I think

**Dave Jones:** that's very likely. Anyway, I can't really find much info on this thing. I got the specs from an eBay ad. So, there was some press release on Tektronix website, but you had to log in or some like that. I don't know, but

**Dave Jones:** anyway, yeah, I think it could be a uh re-badger, I suspect. This is interesting. It actually uses a Nokia Mobira Cityman 100 mobile phone battery or cellular phone. Um, that's rather interesting. Uh, they actually designed it around an existing

**Dave Jones:** mobile phone battery. Well, not a bad idea, actually. Anyway, so the whole idea is that you go to somebody's house with this and they've got uh TV problems, you plug it in to the antenna. You might even go up on the

**Dave Jones:** roof and plug it uh directly in so you get as little uh losses possible, as little cable losses possible, and uh you tune in the channels you want, and it will tell you the RF uh signal strength. And you know, there'd be uh standards

**Dave Jones:** for that, of course. What what are uh sort of minimum signals or a decent signal strength required to get reasonable footage in a particular area, but it's all changed now. This was back in the old uh analog uh days. And got

**Dave Jones:** headphones here, it decodes the audio. You can probably listen to it. All right, so let's crack this thing open very quickly. A little uh uh belt clip uh came off there. And tada, we're in like Flynn. Check it out.

**Dave Jones:** Do we have any uh manufacturer markings? Because I don't think this is a bit of Tektronix kit. Bingo, we found the manufacturer. Promax, um PRX004004A. That doesn't uh register anything on Google, so yeah, but Promax definitely uh the original manufacturers of these

**Dave Jones:** things. Very interesting construction how they've done this uh charging connector on the or interface connector, whatever it is. It's like it's got a separate board down in there, and it's they've soldered along here to make the contacts. I don't get it. They've done

**Dave Jones:** it for strength uh reasons, I would suggest, but um yeah, that's Hmm, rather interesting. Anyway, they've got the Why not just mount it directly on the board and have it a right angle connector and have the physical um and and rely on the physical mounts

**Dave Jones:** on the connector. I don't get it. Anyway, um very interesting. We've got ourselves some uh big ass looking relays there. Check those puppies out. Are they RF relays? No, they wouldn't be on the top board. No, they're just a Joe Blog's uh

**Dave Jones:** small signal relay, which is Yeah, it's doing a lot of switching though. Very interesting construction how this is all packaged together and uh even the relays, they're on their own little board going off here. And uh look, they're shielded on the bottom.

**Dave Jones:** So, they're obviously doing some important signal switching, but no, hang on. I stand corrected. That's where that Look, that's the uh antenna connector there. So, they're actually using that as an antenna switching relay. So, that's interesting. Um and yeah, well, it's a

**Dave Jones:** What? Different uh attenuation ranges for the input antenna uh input perhaps? Anyway, there's the input. There's the output going in the RF can. Oh, I know you RF aficionados want to see inside the can. You always do. Look at that.

**Dave Jones:** Oh, we've got ourselves some little coils. They're not uh waxed down at all to hold them in place. Hang on, there's a big fat ROM here, but uh where's the micro? Is it a ROM? Uh I think that could be a

**Dave Jones:** pre-programmed micro. It must be because there's nothing else there that I can see. So, let's peel the label off. And if we lift the kilt on this thing, here we go. 60 um ST6225. And that is a massively obsolete uh

**Dave Jones:** 8-bit uh mask ROM micro. Actually, the date code on that is '99. So, there you go. That's That's in 1999. We're going to party like it's 1999. Um so, this is it's a relatively modern in the scheme of things, but the design is probably

**Dave Jones:** ancient and this probably had like a 10-year product lifespan or something like that. So, it wouldn't surprise me if this was developed in the late '80s or early '90s. So, anyway, thank you very much, Anthony. That was more than a 2-minute

**Dave Jones:** teardown RF signal strength meter. Cool. Next up, we have one from the United States of America, Robert Frank Yeah, I'm not going to try and pronounce it. From Lancaster, California. Don't think I've heard of Lancaster, California before. I don't know my

**Dave Jones:** Californian viewers. Love California. It's probably the closest uh thing America's got to Australia, like in terms of um weather, culture, especially San Fran. Um San Fran's actually a sister city, if you didn't know. Anyway, up Oh, well, we've got documentation.

**Dave Jones:** It is Tada! An Emerson um compact C- CD clock radio thingamabob. 2-minute teardown. Now, this thing this Emerson stereo clock radio CD player wake to your favorite CD track. Neat. I'm sure that was neat back in the day. Anyway,

**Dave Jones:** um this is interesting. Robert says it it's a very says it's a haunted radio. Of course, there's no such thing as haunted There's just engineering. It has developed an interesting unique fault. It's become an FM transmitter. I guess it got tired of just receiving. It

**Dave Jones:** transmits a weird signal around 95.1 meg right after being plugged in. Uh including two pictures of the spectrum um captured with his software uh, defined radio. And uh, recorded audio with very weak waveform. Anyway, it's spooky. There you

**Dave Jones:** go. Thank you very much, Robert. And sure enough, here's the spectrum, 95.1 MHz, and it's transmitting something. So, what's going on there? I would suspect is that the, uh, uh, that would be the local oscillator, of course, um, plus the IF, uh, frequency,

**Dave Jones:** 455 kHz usually. That's the audio tone. What else have we got there? Yeah, we've got ourselves a spectrum. Oh, that's the audio, uh, spectrum. So, yes, that would be my guess is that the local oscillator. I don't know why it's

**Dave Jones:** transmitting, um, some fire inside. I'm not exactly sure, but there it must have a local oscillator in there. Um, local oscillator plus the IF. So, I that would be that would be my guess. Anyway, 2002 vintage. And sure enough, check it out.

**Dave Jones:** I've just got the, uh, input to the spectrum analyzer here, uh, just, uh, intertwined with the antenna, the FM antenna on this thing. And sure enough, look at that. That is huge. That's minus, uh, 20 dBm at, uh, 95.5

**Dave Jones:** meg or thereabouts. Wow, it's jumping around like a jack rabbit, too. And there's a 100 MHz span on the puppy. Wow. That is, that is terrible. What's going on there? Anyone got any thoughts? I I don't think it's like,

**Dave Jones:** yeah, we're not going to see anything interesting in a 2-minute teardown, but that is fascinating. If anyone's ever seen a failure mode like that in an FM radio, let us know, cuz sure enough, that thing is damn well

**Dave Jones:** transmitting at quite a reasonable power. All right, you know I I resist. 2-minute teardown. Um, typical uh construction that you'd find in something like this. Uh single-sided PCB, of course. They've got a uh Toshiba That'd be a Toshiba uh tuner in there.

**Dave Jones:** And well, no, actually that'd be a Toshi- that'd be a Toshiba amp. Um, your tuner's going to be around here. There's all the wax I was talking about uh before for the uh coils. There's our AM um receiver uh ferrite rod. And uh it's

**Dave Jones:** just hanging off the end. They're a bit loosey-goosey. Um, and yeah, the treble's going to be in there somewhere. I don't know what, but uh hmm there's basically uh bugger all in the rest of it. Got a regular uh in

**Dave Jones:** there to power the thing and the CD mechanism's just, you know, it's just bugger all, really. Um, jeez, they put that on a vibration mount. I'm surprised in such a cheap-ass thing, but um yeah, obviously. It was either absolutely required to

**Dave Jones:** make it work or they killed the lily just a tad. There's actually a lot of parts that go into a uh little bedside clock radio like this thing, but they churn them out, you know, cheap as uh chips in

**Dave Jones:** China, but yeah. Anyway, if anyone's got any clue about how this is uh turned into a pretty crappy transmitter at the uh presumably at the it's a local oscillator doing it. Uh please let us know. And for those playing along at home,

**Dave Jones:** there is the Toshiba part number. I'll try and link in the data sheet if I can. Hi to all my Norwegian viewers in particular. Uh Gerhard Just Olsen from um yeah, Norway. Um, fantastic. If I get too many from Norway, so let's

**Dave Jones:** crack this one open and see what we've got. It's another spoiler alert. Another broken electronics? Broken electronics usually means two-minute teardown.

**Dave Jones:** It's in an RS Components box. Do they have RS Components in Norway? Um for it yet, two-minute teardown. Cool. All right.

**Dave Jones:** Double-wrapped for our protection. Red. Red. Red what? Guess I should read the note. It's a battery charger used for first or second generation professional RED Digital Cinema cameras. Yes. Um very expensive stuff. And I thought it might be interesting to see the design

**Dave Jones:** decisions. And the fire Oh, okay. I like Yeah. What? Like a portable field thing cuz it's got carry handle on it. And presumably Ah, yeah, right. You plug the RED battery on the back. Sorry, I'm not I've never played with a RED camera.

**Dave Jones:** Presumably it's got a massive fast battery pack. It looks big. And you plug it in there and it Oh, oh, two of them. You can have one either side. All right. Interesting. Two-minute teardown. Two-minute teardown on this RED

**Dave Jones:** lithium-ion battery charger. Not going to be a huge amount in it. Um in fact, I don't even see temperature sensing, but it's obviously done inside the cell. Look at the multi contacts down in there. So, meh, it'll just have a power

**Dave Jones:** supply and a lithium-ion uh charger chip in it. Just one of the many off-the-shelf charger chips would be my guess. Anyway, it is mains-powered, so it's Oh. It's Is it already It's already open. It's already open. Aw. Already had a crack at

**Dave Jones:** it. There we go. And Whoop. I can see lots of big current shunt resistors down in there. Hardware okay. Someone's tested it. Okay, the hardware is okay. Uh electrolytic cap there. You can actually see the That's not a solid

**Dave Jones:** uh electrolyte in there because you can see the pressure vent mark on there. Hopefully, you can see that on the camera. Anyway, couple of relays down there for switching. What's their chipset? Oh, that's intelligent. Looks like it's got a micro down in

**Dave Jones:** there. And another bunch of uh current shunt resistors down in there. And well, that looks quite reasonable. It's got the requisite Got some protection and filtering on the input. There's our main rectifier cap. What brand? And we're looking at uh the

**Dave Jones:** big M there. That's a shitah, so I Panasonic caps. Good brand. And what else have we got on there? Oh, nothing on the underside. Oh, those joints look pretty how you doing. Look at those. Wow. Dry as a dead dingo's donger. I'd have

**Dave Jones:** to get in there under the microscope, but uh yeah, is that like just the lead-free But I don't know. It looks pretty crusty. Is it just a flux? Maybe I could clean it up and it might look a bit better, but yeah, I

**Dave Jones:** doesn't instill a lot of confidence, really. Oopsie. Check out the bodgy little transformer tap coming off there. Wow, that's It's a bit how you doing as well. We've got ourselves a PIC18F series for all you PIC fanboys. But uh what like are

**Dave Jones:** they using that to do the custom controlling? I would have expected just an off-the-shelf lithium ion charger IC there. So, this is much more advanced than what I expected, let me tell you. And there's lots of current shunt

**Dave Jones:** resistors everywhere. Well, nope, I don't see any other dedicated uh traditional lithium ion off-the-shelf charger chip on there. So, there It looks like they're doing it. They custom implemented it in the pic. Wow, that is fascinating. They've really

**Dave Jones:** gilded the lily in terms of the engineering required to uh charge a lithium-ion battery. I mean, there's off-the-shelf chips. You could have just had a power supply and off-the-shelf chip which handles everything and Bob's your uncle. But no,

**Dave Jones:** all these current sense resistors are all doing stuff. Lots of protection. Uh and yeah, they really seem to be charging this very cautiously. And I can only presume that this big uh Dale 5-W resistor here is for uh discharging the

**Dave Jones:** battery as well. So, maybe they get some uh you know, charge characterization, uh charge discharge cycles that can characterize um you know, how much uh capacity's left in the battery and stuff like that would be my guess. Anyway, that's interesting.

**Dave Jones:** That's inside a red battery lithium-ion battery charger. Much more complicated than you'd expect. Another one for the United States of America from uh Tempe, Arizona. Hello to all my viewers in Tempe. Or just Arizona in particular. Um I've been to Arizona.

**Dave Jones:** Been to Meteor Crater in Arizona. Didn't quite get to um uh Winslow though. Anyway, um ooh, what we got here? Oh, look at Oh, look at that Oh, look at the Look at the case. Geez, this is What?

**Dave Jones:** Okay. So, that's a charger thingo. That's cigarette lighter. What? Auto Auto shaver it says. I guess it is an auto shaver. Wow, this uh this thing is ancient. What? I ju- I got a little Oh, what on earth is this dog doing?

**Dave Jones:** Better read the note. John is an student from Phoenix, Arizona. Hi to all my viewers in Phoenix. A big fan of your channel, particularly mailbag. Everyone loves it. It's everyone's favorite segment. After seeing all the cool and crazy stuff, he thought he'd send in

**Dave Jones:** some cool and crazy stuff. Anyway, this second item is an Alec Tri-Pup. Um it's a porcelain electrical splitter manufactured in the 1930s. What? It is. Look. It's just an It's a like basically a double adapter as we'd call it here. Um

**Dave Jones:** or a triple adapter. And uh one of them's a bit loosey-goosey, but the Alec Tri-Pup. I think there you go. I mean it's for all you trademark registered Alec Tri-Pup. Um for all you uh history buffs, all you collectors out

**Dave Jones:** there. Wow. And this is a travel electric auto shaver charger. Is designed to operate between 12 and 14.5 volts. There you go. For service, see any radio repairman. Love it. Anyway, isn't that a funky case for it? There's the output. Let's crack it open.

**Dave Jones:** Wow, check it out. It's a mechanical vibrator. Look at that. Mechanical vibrator inverter. Designed to generate 120 volts. Uh that American rubbish, out of course. There's a 1 MFD. None of this micro None of this micro mu symbol rubbish. Good

**Dave Jones:** old MFD. Yes, 1 MFD. For all you uh non-old school people, it's a one microfarad. That's how they used to uh write microfarad back in the day. Anyway, it's a mechanical vibrator that uh steps up the 12 volts. Uh converts

**Dave Jones:** the 12 volts DC from the car battery into 120 volts AC. Pretty crusty from the mechanical vibrator. Terrific.

**Dave Jones:** That's terrific. It's so loud. If you want to see I'll I'll get my high-speed camera on this at 1,000 frames per second. So, if you want to see this in 1,000 frames per second, click here, hopefully, and go over to my

**Dave Jones:** EEVblog 2 channel and I'll show you. Thank you very much, Colby Newman from parts unknown in the United States. Sounds like a wrestler. From parts unknown. And we have ourselves a four-banger. Check it out. This is the APF Mark 25

**Dave Jones:** memory with wood paneling. Look at that. Imitation wood paneling. Four-banger calculator. Oh, goodness. It turns on, but um yeah, it doesn't seem to be doing that well. Hm, one sick puppy. Made in the United States of America. 1975.

**Dave Jones:** Yep. Where's the nipple? I want to play off the nipple. There it is, down there. Ooh, love the nipple. There's something that's sadly lacking these days, a diagram of the actual chip, the physical orientation of it on the silk screen. Bloody ripper. I've got

**Dave Jones:** one from the old dart from Knivd. K N I V capital D. Hat and beard. Anyway, um to all my Pommy viewers, let's have a look. We do like PCBs and looks like we have some proto boards. Let's check them out.

**Dave Jones:** We have yet another prototyping board, but this one's substantially more than meets the eye here. This is the router board by Knivd. All right, yeah, I don't know how to pronounce that. Anyway, um look, if they're uh it's like a matrix board, okay? But

**Dave Jones:** then it has these individual traces coming off. They're not actually going anywhere. You have to bridge them over with a with a solder and then you can actually connect these kind of like an FP So, think of it like an FPGA matrix kind of

**Dave Jones:** you know cell kind of matrix. So, this one can go to the one next to it if it wants it can go to one there but it can also go diagonally as well. So, you can actually join up pins diagonally like

**Dave Jones:** that. And it's it's rather fascinating. How good it is in practice, I don't know. I'd have to actually try. You would have to save that for a different video. But not only is it interesting from that respect, yes, it's registered trademark

**Dave Jones:** and blah blah blah all that sort of jazz, but it's and it's also a Kickstarter as well. And well, you can actually buy it. I think the Kickstarter's over. The other interesting thing is it comes with its own

**Dave Jones:** router board description language. You can actually use a language to actually design your routes on here and it comes with this awesome looking visual editing software that you can presumably do the programming language in, import and export, and then manually tweak it and

**Dave Jones:** things like that in the software. It's A for effort on this one. Whether or not it, you know, is really useful in practice, as I said, I don't know, but it's probably the most interesting proto board we've seen to

**Dave Jones:** date. I'll link it in down below. Check it out. I'll tell you what though, there's one thing I absolutely hate is the black solder mask. Maybe if I hold it up like this, I don't know. I've got my can't see it very good on the

**Dave Jones:** camcorder LCD, but you can see the traces going up there diagonally. Just You can see them going over, but the black solder mask just all right, just it's frustrating. You can't see the traces underneath. Don't like it. Hello to my Swedish viewers,

**Dave Jones:** Karoli Simon. I'm assuming it's back to front. May not be. Simon Karoli, Karoli Simon. Thank you very much from Lens Corona or something in Sweden. Cool. All right. It's up. Oh, that didn't work. Actually, I think there might be

**Dave Jones:** something there. That's why it didn't work. Okay, yep. There we go. It's got a little dongle integri-fuse. Oh. It's a little USB fuse in-line electronic fuse. Let's check it out. And this is the integri-fuse, a USB dual protection device that makes

**Dave Jones:** it possible to enable disable data comms, which can be used to protect private data when charging a phone tablet. If you're paranoid about that sort of stuff, Big Brother is watching. Remember that. Also, they're not only watching, but they're

**Dave Jones:** logging everything. Also, a power fuse function is implemented. Five current threshold levels to choose between. And there is, like you might think, well, okay, how does it work? Okay, there's our symbols. And there's our little table on the

**Dave Jones:** back. And presumably, is that number of flashes? I don't know. One, two. Anyway, um it does have a teeny weeny itty-bitty switch on the side. Well, I'll tell you what, I can't make heads or tails of the mode thing here. Um

**Dave Jones:** it's I think I maybe set something, but I don't Yeah, get it. Maybe I don't know. Maybe I need to RTFM or something. Anyway, I looked at the Indiegogo campaign. There's like 15 days left, but it says that

**Dave Jones:** like there's no description anymore. It's got a joke video, and um just saying it's not possible to order it anymore. So, I don't know what the hell's going on with this project. Anyway, I'll link it in down below.

**Dave Jones:** Actually, there are quite a few ones here. This one's been sitting here for ages. Um, sorry to um, somebody in the UK. Um, but yeah, I haven't opened this one. Let's have a look. It is an Orange Pi one because

**Dave Jones:** yes. Um, I complained quite some time ago before I got my Orange Pi ones that I couldn't get it. I was having problems getting a AliExpress. They sent me one. Thank you very much, Brian Dory. Um, and has also sent

**Dave Jones:** some stuff they sell on their website, ab-electronics.co.do.co.uk. Let's check them out. And Brian from AB Electronics.co.uk, um, does these uh, prototyping boards. Here's a Raspberry Pi prototyping board. It's got one of those extender um, headers with it. Um, yep, we've got What's that? A little

**Dave Jones:** extender header? Not sure what's going on there. Anyway, um, a breakout uh, Raspberry Pi Zero uh, board and other little headers and things like that. So, I'll link them in down below. They got a Raspberry Pi 2 GPIO port. And thanks for the Orange Pi.

**Dave Jones:** I'll add it to my cluster. Oops. Sorry, I opened this one uh, off camera. I've had this for quite some time. I thought it was like a double delivery or something cuz we've seen this before. It's a Digilent Analog

**Dave Jones:** Discovery 2. And we've seen that before, but I just remembered the previous one. So, that was like the National Instruments branded version of the Analog Discovery 2. This is the Digilent branded one, but they didn't just send that. They sent the some of those power

**Dave Jones:** bricks that we've uh seen before. Those are the little power bricks, they're very cool. So, they come in handy. We've got a Pmod A, measure your circuit's impedance over an I squared C interface. That could be interesting, so we'll take a quick look

**Dave Jones:** at that. Uh the interface board. And this is they've got like an analog a Digilent analog parts kit. That looks pretty good. Got a smallish bread Oh, a long thin breadboard. Okay, it hasn't got the top strips on it and a whole bunch of parts.

**Dave Jones:** That could be really useful. Now, this is actually really cool. For 65 bucks, you can get this Digilent analog parts kit. And here's all the stuff in it for those playing along at home. They've got uh instrumentation amps, they've got uh

**Dave Jones:** you know, precision op-amps, they've got voltage reference 8584, they've got uh magnetic field sensors, current shunt monitors, accelerometers, microphone, IR transmitter, uh piezo uh temperature sensor. All sorts of fantastic stuff. So, let's take a quick squeeze inside this puppy.

**Dave Jones:** And look at this. Beautiful. Um yeah, that's not that's anti-static. That's not conductive, so that's not the best way to store those. Anyway, I've done a whole video on that. Hm, anyway, we've got uh these like uh regulators down in there or transistors,

**Dave Jones:** I'm not sure. You get some leads, caps, uh electrodes, resistors. And a uh partial breadboard doesn't have the uh power strips uh top and bottom. And all the um uh a lot of the chips on uh surface in surface mount packages like

**Dave Jones:** the accelerometer, for example. I'm not sure if that that maybe looks like an accelerometer there. That looks like a microphone. Is it? Does it mount on the bottom? It's got a hole in it. Hm, I don't know. Anyway, um SMD parts and

**Dave Jones:** they've put those already populated onto the um SMD to DIP converter. And you get one of these funky um Digilent/National Instruments um screwdrivers, which are very very handy. And And whoa, I got ourselves a big power resistor. Look at

**Dave Jones:** that. 6.2 ohms, thank you very much. And a whole bunch of jumper wires. That is a neat kit. I really really like that. I'll link it in down below if you want to nab it. Tell you what, I really like the

**Dave Jones:** idea of this. It measures your circuit's impedance over an I2C interface, and it uses a real funky chip, the Analog Devices AD5933. Not only it's an it's an impedance converter. Not only does it contain the AD a 12-bit 1 megasample 12-bit ADC, but

**Dave Jones:** it's got a DDS signal generator in there, and and DSP processing, which does the Fourier transforms and every it's it is beautiful. I'm really really interested in this chip. I might have to do a project on that. It's very cool.

**Dave Jones:** Anyway, it's all integrated. It's one little board. I won't, you know, it's yeah, the board itself. It's basically the Analog Devices chip on a board. Comes with some cables, and you can measure complex impedances from 100 ohms to 10

**Dave Jones:** meg with the discrete discrete Fourier transform DFT performed in the Analog Devices chip. Neat. Linked down below. On these rails, and there it is. There's the other one. There's a slave version. There's several ways to design an LCR meter. But the

**Dave Jones:** technique I chose for this is the voltage and current measurement technique. Basically, you feed a fixed frequency into the device under test, and you measure the voltage and the current and the phases, and from that from those basic measurements you can

**Dave Jones:** calculate everything. And stick with me with the here, but here's the technique.
