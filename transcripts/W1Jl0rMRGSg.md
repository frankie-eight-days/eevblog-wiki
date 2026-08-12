---
video_id: W1Jl0rMRGSg
title: EEVblog 1503 - Rigol HDO4000 12bit Oscilloscope TEARDOWN
url: https://www.youtube.com/watch?v=W1Jl0rMRGSg
source: youtube-asr
---

**Dave Jones:** Hi, it's time to tear down this new Rigol HDO 4000 series scope. I'll leave my first impressions and noise measurements video linked in up here. If you haven't seen it, it's got a new Rigol ASIC in it and I believe it also

**Dave Jones:** has a new Rigol front end and of course it is a 12-bit jobby. So this same I think the same front end chipset in this is going to be used in the new HDO 1000 series which is on the way. Anyway,

**Dave Jones:** let's take it apart, shall we? Not a fan of the feet, really? Oh, you betcha. Beauty. Oh, look at that. Jeez, that was a bit horrific. Got medieval. And it uses kind of like the de facto standard four screw

**Dave Jones:** arrangement here just to hold on the back case. And by the way, on my first impressions one I totally missed the fact that this has a battery pack slider on there. Hence all this wanky shape in here is designed and like clips up in

**Dave Jones:** here designed to have a battery pack slide in there, but I I don't know if that option is available yet, but it's there. It's obvious so obviously there'll be a back piece to be in there. Anyway, this will lift off and

**Dave Jones:** we've got the metal work. Oh, and that's oh yeah, there you go. So that's actually screwed into the back of the metal work there. Got a couple of RFI tabs there and you can see it's probably going to be one big single

**Dave Jones:** board construction. Oh, no, actually. I don't know. Anyway, we'll find out. Is it one big single board? Oh, look at this, dual fan jobby, dual exhaust on this bad boy. No wonder it's loud. Jeez. So anyway, air flow wise, it's all

**Dave Jones:** coming in this side. I like how it goes down onto the board as well. You can see the heat sink in here is angled in the right direction. Oh, that that that heat sink extends all the way down into

**Dave Jones:** there. When we get that off you'll see it. But anyway, the air comes in here and they've got the fins in the right direction for the air flow and also the power supply inside there. So the power supply is in the upper half here and

**Dave Jones:** then that all comes out the other side. But yeah, as I said in the in first impressions, it is rather annoyingly loud and whiny. And as is common, we have to get the nuts off here. There's no washer, no star washer

**Dave Jones:** under there before we can lift off the entire thing. There we go. Although, yep, yep, I have to disconnect a few things. I'll get back to you. And we're in. There you go. AND WOW, LOOK AT THE heat sink on the front end here. And

**Dave Jones:** also, would this be the ADCs as well? So, um yeah, the new front end, the 12-bit front end ASIC is chewing some power here. That is like the heftiest heat sink in this thing. Um and usually when you got four channels like this,

**Dave Jones:** there'll be four ASICs here for the front end, and then probably two ADCs in here, and then the acquisition um ASIC, and then the whatever processor they're using to run the Android operating system on this thing. Anyway, that is very impressive and nice

**Dave Jones:** big single-board construction. And I am liking the look of the mains assembly down in here. The earth point there is very nice. Look at that. And they've got all crimps as well. It's neat and tidy, though. Should be easy enough to upgrade

**Dave Jones:** the fans in there for quieter ones. So, yeah, check out the just multi-stranded. That is just one big crimp terminal in there. They've got the multi-strands coming out here cuz I guess they wanted to like reuse the connector over here.

**Dave Jones:** And obviously, this is the battery contact board, and we can actually get that out there. You can see they've got a nice little plastic interface there with metal threaded inserts. So, that's really nice. So, there There you go.

**Dave Jones:** That is just It's basically just some MOSFET switch in there for your battery. So, it chooses either the battery interface um or it just comes from the power supply. And that's it. Took me a few seconds to figure out what that

**Dave Jones:** board down there was, but it actually tells us our AC triggering board. So, they've got an optocoupler there, and so it just takes the mains output and the mains input here, um and just gives us an optocoupler output, which then goes

**Dave Jones:** over this cable goes over to the main board. So, yeah, that's just for our line triggering. So, they've gone to a lot of trouble there. And we'll go through the board in some detail, but this is the LCD connection, so we can

**Dave Jones:** take that off and then we can see it, but I'm going to just going to now remove all the heat sinks so that we can take some high-res photos and go into it. If you don't know, I always have

**Dave Jones:** high-res photos available on my EVBlog Flickr account linked over on evblog.com. Well, I found an Artec 7 under there, and this one over here looks interesting, but we'll take a look at that. Now, let's see what's under the

**Dave Jones:** front end. Oh. Oh, okay. There you go. Oh, isn't that nice diecast case? Oh, isn't that beautiful? They've used sil pads there, and let's have a look. There's our four front ends. Geez, there's not much in it. Remember, this is an 800 meg bandwidth

**Dave Jones:** software upgradeable front end. So, this is 800 meg. So, this is all their custom I do believe they've rolled their own custom front end, but I'll take some high-res photos and we'll go in there and check it out. There's not much.

**Dave Jones:** They've got two relays. What brand are they? Not sure from this point. And up here, we've just got Yeah, they heat sinked all three of those chips. Well, I'll tell you what, I'm pretty impressed. Everything in here is metal

**Dave Jones:** threaded inserts for all of the like holding down the main metal chassis here, and you normally get self-tappers for that kind of stuff, but anyway, that just easily popped out. Then we can see the front panel board here for the

**Dave Jones:** SmartProbe interface things, so that'll be going off on its own ribbon cable, I would be assuming. Then we have our optical encoders, cuz one of their marketing claims is that uh these are not uh wiper type uh ones that wear out.

**Dave Jones:** These are optical or photo uh encoders, you know, they've got a LED and a phototransistor in there that, you know, detects the motion in either direction. So, there's no contacts to wear out inside these things. I'm not seeing a

**Dave Jones:** brand on it though, but um yeah, this is one of their uh one of their brags, and it has been a a sticking point um for several scope brands um over the years. And did Rigol actually cop some flak

**Dave Jones:** over the years for it? I'm not sure um but anyway, yeah, I think a few of the scope manufacturers have on the EEVblog forum and other places um for, you know, their their pots wear out. You use them

**Dave Jones:** so many times, and but these are optical. So, there's the interface, and interestingly, they do have a large cutout in here. That would be for the mixed uh signal connector, which is not there. It's not even populated on the

**Dave Jones:** board, so don't get your hopes up. Um no, this is not a mixed-signal scope. Doesn't have an arbitrary waveform gen, but interestingly, they do have uh cutouts there for two extra BNCs. That would be um you know, your arb gen

**Dave Jones:** output and whatnot. So, um interestingly, what I thought was um that might have been the LCD connector is not. You can see it actually goes to the front panel board here. So, they've got a ribbon, and this cable actually

**Dave Jones:** going through uh presumably for all of the uh contacts here. Um that could be individual power going over to power uh the active probes, and that power hypothesis makes sense cuz it goes over to here like this. And there's um like

**Dave Jones:** some switch mode uh chips in there. So, yeah, looks like that's active uh probe power. And the back of the interface board there, check that out. They've got uh polyswitch protection on all of the um like there's like four for each one.

**Dave Jones:** That is a lot. Uh I guess they expect a lot of goose, you know, idiot engineers short out active probes all the time. It's interesting how they've have to the effort to um like emboss these out from the other

**Dave Jones:** side. I guess that's to get a little bit more height for the connectors underneath. Let's go through the main PCB here and I am capturing this in 4K, so you will be able to see all the detail, but as I said, high-res

**Dave Jones:** photos are available on evblog.com if you want to have a squeeze. Now, this is the main PCB here and if we compare it with the Rigol 5000, which was quite a few years ago, but that was their new

**Dave Jones:** Phoenix chipset, I think it was at the time and they and they had like an eagle on there. This one has like a I don't know, it's some sort of flying bird, almost looks like a toucan or something. But this is supposed to be

**Dave Jones:** the Centaur chipset. So, anyway, this is the original Rigol 5000. It was very simplistic here and I don't believe I ever took these off cuz these were adhesive glue. So, yeah, we couldn't actually see what was under these, even

**Dave Jones:** the front end. I did take the cans off. Anyway, I was able to get the heat sinks off these cuz these weren't adhesive. So, we've got a Xilinx Artix 7 here. So, it's the main bad boy. So, all their new

**Dave Jones:** Ultra Vision 3 stuff is inside the Artix 7 and that's the main memory there. There is no extra memory on the bottom. I might show you the bottom of the board, but there's basically nothing of note on there at all. So, yeah, the that

**Dave Jones:** Artix 7 is not cheap. And if I'm right, Digikey puts that at about 205 US dollars 40 of quantity. So, we'll have a look at the main processor over here in a minute, but anyway, we have our bird

**Dave Jones:** here. Somebody had fun on the PCB, but this is really what we care about is the front end down here. So, actually take a closer up look at this. Now, as you can see, they're all identical. Um all of

**Dave Jones:** these is I don't think there's a single difference uh between them and they require substantial heat sinking. So, this is a new Rigol developed custom front end, but I believe this is the new center chip set upside down, so all the

**Dave Jones:** electrons are going to fall out, but that's the RT8847 or 4471, uh something like that. So, um yeah, a few hairy scary's on there. Um so, we've got two of those. So, one of those, obviously, uh shares the two channels

**Dave Jones:** and I believe that's the case. You you know, turn on channel one and channel two and it halves the sample rate because you've got your single ADC here like this. But, if you turn on channel one and channel um three like that or

**Dave Jones:** channel four, for example, you'll get the full sample rate on two channels. Most uh scopes work like that. And this in here, which is also uh heat sunk, this is actually you can tell by the uh component arrangement down here that

**Dave Jones:** this is the PLL. This is the clock generator PLL uh for this thing and that is a uh TI jobby. It's an LMK0482 ultra low noise clock jitter cleaner and clock jitter cleaner um with dual loop PLLs. So, it's got roomba function. Um

**Dave Jones:** and yeah, it's just there you go, uh femtosecond for you uh you know, clock aficionados. You can go for your life in that. Anyway, this does have a external 10 meg oscillator in. I don't know if it's this one down

**Dave Jones:** here, it's one of these. Um anyway, yeah, all this miscellaneous circuitry around here, this is for like internal uh it's got 10 MHz reference out, 10 MHz external reference in as well. But, I'm not actually seeing the oscillator

**Dave Jones:** there, though. So, I don't know what's doing there. And are these two LEDs? Are these two I don't know, I haven't powered it up without the back on it, but uh they look like there's there's two LEDs there. I mean, we can zoom in

**Dave Jones:** on that. That That That looks pretty leddy, doesn't it? So, this here is the Rigol 5000 front end like this. And as you can see, there's the BNC input. Then we've got our AC coupling switching relay here. We've just got one IC here,

**Dave Jones:** where whatever that is, I don't know. Could even be a discrete off-the-shelf chipset. And then all of your divider stuff around here. And then a just a differential pair output buggering off there. But the new one is actually

**Dave Jones:** substantially different. Let's have a look at the front end. Now, I've actually taken the bottom. So, this is the bottom side of the Well, the front. The bottom side of the actual PCB as such, but it's the BNC It's the business

**Dave Jones:** side of it. And this is the top here. But this 5000 series Rigol front end here, this is like a lower-end scope. You get it like sub at $1000 now. So, it's more fair to compare this one with

**Dave Jones:** the upcoming HDO 1000, which I'm getting in another week or two. And we'll take a look at that. So, I expect a simplistic front end like this. So, it's fair to compare it with the Rigol 7000 series, which I've done a teardown of

**Dave Jones:** that as well. And here we go. It's not rotated, unfortunately. Can I rotate? So, this is the 7000. You can see that we've got two relays here, which we didn't have on the 5000. And we've got the AC coupling relay here. That's the

**Dave Jones:** little Cosmo solar state jobby there. And it looks like I think I don't know if I saw this in the previous one, but it looks like this actually has a separate 50 ohm path like this and a separate 1 megaohm path. I might have

**Dave Jones:** missed that in the previous teardown, but have a look. But if we compare that with the new HDO 4000, here it is. It's relatively similar. We've got our two relays here. You'll note that they are exactly the same and it's interesting to

**Dave Jones:** note that a Chinese oscilloscope actually uses Japanese Fujitsu relays cuz some of the best relays are made in Japan. All the best stuffs are made in the Japan. They're actually a Fujitsu jobby. There you go. Ultra miniature relay. They're not shielded or anything

**Dave Jones:** like that, but they do actually specify you know, high frequency characteristic here. So, yeah, superior contact spring for high frequency characteristic. So, it complies with various standards, but they're not shielded relays. They're not like high frequency coaxial relays or

**Dave Jones:** anything fancy like that. So, this is a Remember, this is an 800 MHz front end. When I was a boy, 800 MHz front ends they didn't look like this. Yeah, it's just absolutely incredible. Anyway, we've got the new

**Dave Jones:** Rigol AC key. This is the RT1642 IQ. So, I There's no info on that at all. If somebody can get info on that, I doubt Rigol are going to give us anything. I don't know. I should ask maybe. Maybe they

**Dave Jones:** will. You know, they might give us a block diagram. They wouldn't give us more than the block diagram or anything. But, this is Rigol's secret weapon here and this is of course, this is not a 12-bit front end, but it would have the

**Dave Jones:** dynamic range and low noise capability cuz this is a low noise 12-bit well, 12 bits is the converter which is further up. It's not in the front end, but the front end has to have the low noise dynamic range for the

**Dave Jones:** to enable the 12-bit functionality. But, anyway, the So, so the relays are the same. So, it seems like this does have a separate 50 ohm path and a separate 1 megaohm path as people are speculating on the EVblog

**Dave Jones:** forum. You can see tiny little biddly traces there. They're really thin. Thin as. Anyway, if it goes through the relay like this if you AC or DC coupling, it doesn't matter. It goes through the relay and then it comes through like

**Dave Jones:** this and this is your AC path like that going into your divide-y amplifier differential driver front end chip. But the 50 ohm path actually is here. And I have actually measured this. This point here is actually physically connected through to If we draw this,

**Dave Jones:** the relay has three Please forgive my mouse, but it has three contacts like this. And this is the center pin, and then it flips between there or down here. Yeah, so that point is actually it it's not actually connected over to here. It's

**Dave Jones:** actually physically connected through to just the just the actual input pin here like this. So I've measured that. But the 50 ohm looks like this flips it on. It goes through here. I have measured that resistor there. Even though it

**Dave Jones:** doesn't say it on the top, that is a 50 ohm resistor. And then it goes through here. Once again, contact over to here. And this is your 50 ohm path. Here's another 50 ohm resistor here. And it goes up

**Dave Jones:** into there. So separate 50 ohm and 1 megaohm paths. Interesting. And once again, we've got all of our divider stuff like this. But this is Rigol's new secret weapon, which is their low noise front end. And as you saw in my previous

**Dave Jones:** video, this is not a 100 microvolt per division front end. It's only a 1 millivolt per division front end. Uh 100 200 500 microvolts are software magnified. But you can do that because you got the 12-bit converter. And

**Dave Jones:** anyway, people over on the EV blog forum I'll put the link down below. They have actually measured uh the noise and compared it with the Siglent and a Lecroy I think something like that. And yeah, the Rigol does a pretty decent

**Dave Jones:** job. The front end is pretty decently low noise especially for the cost. So yeah, it's it's really good. But this is an entire front end. I mean, you know, there's nothing doing over here. There's a whole bunch of bypassing and stuff.

**Dave Jones:** Looks like we have a filter there because you can tell it's got the extra extra contacts in the middle extra contacts in the middle there. You can see those. But apart from that like there's nothing else doing here. Sorry,

**Dave Jones:** I do have to my head's in the way. So let me move my head floating Dave head. There we go. But what I didn't show you down here this this image is flipped just to make it the same way around but this is a 4053

**Dave Jones:** the classic 4053 jelly bean 4000 series CMOS analog switch is still used in everything. This is a 272. There was another one if you spotted up closely up on the main board. There's probably a whole bunch of these. The 272 is just a

**Dave Jones:** here it is. It's just a precision dual op-amp. It's nothing you know super special. So this would be doing the bias function which this has which is actually different to the offset. This actually I I got that wrong in the

**Dave Jones:** previous video. I just assumed that the bias in the front end settings was the offset but it's not. The actual physical offset where you move the waveform up and down. That's different to the DC bias. You can actually add a DC bias to

**Dave Jones:** the front end and I think I suspect that's what that's doing there. Yeah, but there's nothing else here doing at all. So it's that's an 800 meg front end. There's not much cost in that. I don't know what this A6 cost them. What sort

**Dave Jones:** of process they did that on? I don't know. If you know what sort of you know process they would have used for that thing. Obviously it's pretty high power because like it needs a pretty decent heat sink as you saw. Now as for getting

**Dave Jones:** the signal out you can see that there's actually two there's a different way there's actually two differential pairs coming out of here. So these two here and these two here. So there's two differential pairs coming out. So I

**Dave Jones:** don't know what the deal is and I can't see those on the bottom of the board. So I think they're actually going through that this is what this via stitching here's for, I suspect. Um so yeah, that's obviously I don't know. It's

**Dave Jones:** buggering off to the ADC. What is clearly right goals uh 4 gig sample per second ADC. So this is their center chipset here um that they, you know, claim. And the, you know, the UltraVision 3 technology whatever, that's just being run in the Arctic 7

**Dave Jones:** FPGA. So this is the bottom of the board here. As you can see, like there's not much doing. You can see all the matched length traces. We've got the wiggle wiggle wiggle years in here. Check those out. So what's going on here is when you

**Dave Jones:** see both pairs like that take a snake, it means that they're matching the entire length of this pair with all the other pairs. They're length matching. But when you see a wiggle wiggle wiggle year in just one of the traces like that

**Dave Jones:** and down here as well, what they're doing there is matching one the one side of the differential pair with the other side of the differential pair. They're just matching between the two. So there's two different types of length matching and

**Dave Jones:** you can mix and match those two. They want to ensure that the, obviously this is coming out of the ADC. They want to ensure the data coming from the ADC is exactly the same matched timing going from both channels over to the FPGA

**Dave Jones:** here. Yeah, there's really nothing else on there. It's not very exciting, is it? So we want to look at the processor now. Here it is. It's a Rockchip RK3399. Hadn't heard of this before. Turns out it's actually um quite old. I've got a

**Dave Jones:** data sheet of 2018 here um and it's an arm processor. It's running the Android operating system. I think I showed that in the previous video. So yeah, it's got Cortex A72 quad core Cortex A53 with separate neon coprocessor.

**Dave Jones:** Uh yeah, it's got H264 265 decoders, 10 bit jobbies. Um 1080p, 30 frames per second, JPEG encoder decoder, um, pre image processors and stuff like that, embedded 3D GPU. Well, we don't need that. But yeah, there you go. For those playing

**Dave Jones:** along at home, um, it's got cryptography extensions and stuff. But yeah, I don't know. It's just they presumably chose it. I don't know. Because it's cheap or they have experience with the ecosystem or whatever. Um, you could choose any

**Dave Jones:** arm based processor here. But this one's, you know, it's it's at least 4 years old. It's not something new. And mysteriously, there are two buttons up here. I wonder what they do. They're not marked. Huh. And they're populated. So,

**Dave Jones:** what? That's interesting. But as I mentioned before, this is the power supply up here by the looks of it or at least part of that, um, for the connector that goes off to the active probes on the, uh,

**Dave Jones:** front end. That's like mostly, um, power there. They had all those wires going over. Don't know why. Um, just separate uh, fused ones. I don't know. And I don't know if this had, uh, HDMI output direct. Did it Did it? Yes, display

**Dave Jones:** interface, one HDMI port. There you go. So, I'm not sure what that one's doing. Let's look it up. Yeah, I'm not finding any ready info on that. So, like you can see that some of the pairs go direct from the

**Dave Jones:** Rockchip over the HDMI driver on there. But others, um, come from the 4C. So, I don't know what's doing there. Anyway, um, here's our touch, uh, sensor for the, uh, touch screen. And this is our, um, LCD ribbon

**Dave Jones:** cable. You can see those going on physically over onto the LCD over there. And basically, that's coming directly from the Rockchip over here. Now, I don't know how much memory is associated with that. You can decode the, uh,

**Dave Jones:** Micron part number over there as you can do for the, uh, FPGA, um, as well for the Micron memory. We've got a, uh, real-time battery, uh, backup. Yeah, so apart from like your auxiliary ins and outs here, there's

**Dave Jones:** nothing doing. There is a third unpopulated USB over here, so I don't know. But yeah, obviously like this board doesn't even have the options for the of what you saw with the connector cutouts on the front panel. There's no option for

**Dave Jones:** mixed signal waveform gen or anything like that. So, nothing doing there um at all, really. And one of these inputs over here was external trigger. Was that external trigger at the top? Anyway, we have a very nice populated JTAG over there for

**Dave Jones:** us. That's excellent. If you want to hack this thing, is there any like serial? Oh yeah, there you go. That could be a UART interface. Geez, the the real mouse operation's really laggy on my 4K when I'm capturing my 4K

**Dave Jones:** screen. Doesn't do this on the 1080. But anyway, this is the power input. It's just I think it's just 12 volts in for the whole thing, really. And and then you've got, you know, look, there's obviously like there's 0.9

**Dave Jones:** volts here, is it? Yeah, there's 0.9 volts here. There's, you know, separate voltage for the CPU. There's 3.3 volts there. There's another CPU jobby over here. VDD center here. I assume that's the supply for the high-speed split transmission

**Dave Jones:** line termination. So, that'll be what that's for. There's another analog VGC management analog VCC. There's 1 volt over here. There's 2.5 volts over here. There's 1.8 volts here. There's another 1.8 volt generator here. There's like like it's crazy. In fact, what we don't

**Dave Jones:** see here inside the front end, we don't actually see a low noise supply. So, this looks switching like. What's going on here? Not seeing any major inductories. So, of course you wouldn't have a switching supply powering your ultra low noise front end here. Um

**Dave Jones:** you're just not going to do that, but I'm uh maybe five five five 5.2? Would they be uh low noise? They they might be powering the front end. Perhaps, but I would have expected to see one for each, and I

**Dave Jones:** didn't see it on the bottom. There is a three-pin jobby there, but I don't think that's doing it. So, yeah, they must be supplying them outside. So, that's that's surprising. Didn't expect that. There you go. That's it for the um

**Dave Jones:** teardown the Rigol HDO 4000. So, yeah, this is a it's a serious bit of kit. As I said, like the performance of the front end seems pretty good. Like it's not industry leading or anything, but for the price point, um it's pretty

**Dave Jones:** good. Now, for the HDO 1000 series upcoming, uh should be that should be on the uh on the plane in another week or two. Um so, we'll be able to tear on that, but as I said, I wouldn't expect uh the

**Dave Jones:** dual relay front end cuz this lower bandwidth. It's not 800 meg, but I suspect it might you because it is a 12-bit. Once again, it's 12-bit. So, it's going to be using the new Centauri chipset, and I suspect it will use the

**Dave Jones:** front end 800 MHz capable. Obviously, who knows? It might even go higher than that. We don't know. Um but yeah, I expect it to use the exact same chip, but as you uh saw in the Rigol 5000, I

**Dave Jones:** expect it to eliminate cuz it won't have 50 ohm, right? So, it won't it won't need the relays. It'll probably just eliminate both of those, and it'll just have the uh AC DC input ac dc, and um yeah, Bob's your uncle, but where is the

**Dave Jones:** power supply for each each of the front ends? I like ultra low noise. I would have expected like this bad these bad boys to have a a low noise um linear reg on each one of them. I don't know. Maybe it's built in.

**Dave Jones:** Anyway, it'll be interesting to compare this with the HDO 1000, a much cheaper one which starts at $699. This one starts at $2699, I think it is. Um, so it's significantly uh more expensive. Um, yeah, I don't know if they've like

**Dave Jones:** cheaped out on the uh processor over here. The Arctic 7, you know, you'll find that in any, you know, top-end oscilloscope these days, something like that. So, I don't think they've necessarily like they haven't really skimped there, I guess. Um, and they've

**Dave Jones:** developed their own custom um front end and new center chipset here. Or is center like both of these combined or something? That might be, you know, that might be the thing. But, yeah, it's like it's amazing how simple the front end 8

**Dave Jones:** 800 meg front end, come on. And it seems to be a pretty decent front end, low noise. 12-bit capable front end, 1 mV per division. Um, yeah, really quite amazing stuff. And this will have uh software bandwidth limiters in there as well, I

**Dave Jones:** suspect. Um, so yeah, there's probably like an I2C bus that comes into it or something that actually commands sends the commands uh to it cuz there's no separate uh PGA programmable gain amplifier. It's all in here. There's no separate

**Dave Jones:** differential uh driver. So, it's got a programmable gain amplifier, you know, with with the attenuator uh system and stuff. And it's got the differential uh driver output. Or it's probably got adjustable bandwidth limiters in there, 20 meg, 200 meg,

**Dave Jones:** 400 and 800 uh meg. Um, cuz I I think they'd be implementing those in the front end and not actually like digitally inside the FPGA. But, uh yeah, anyway, you can tell that from the um shape. I mean, uh everyone over on the

**Dave Jones:** EVBlog forums analyzing the uh shape of the noise curve and everything. Um, and you can actually tell a lot from the shape of the noise curve. It's rather interesting. Anyway, that's really cool. So, if you like that, please give it a

**Dave Jones:** big thumbs up and as always, you can discuss down below. I'll link the EV blog forum down below where people are discussing this bad boy and comparing the noise and analyzing doing performance analysis and all sorts of stuff. So, if you're interested in

**Dave Jones:** getting one of these and you're you know, curious to know how good like the 12-bit performance and front end is, there's people over there doing tests and comparisons and stuff. Really neat. And I'm impressed by the construction of

**Dave Jones:** this thing, too. It's you know, it's really good and and Rigol seem to have engineered this pretty well. So, I'm quite happy with it. And thanks to all the patrons who help pay for all the stuff that I do here. This is my

**Dave Jones:** full-time job and they help pay for it. So, that's always linked in down below and is very much appreciated as is the EVblog store. If you want to support, you can buy like a multimeter on the EVblog store. Clamp meter coming soon,

**Dave Jones:** by the way. So, I hope you enjoyed that and found it useful. Give it a big thumbs up, comment cuz that adds to the metrics and it you know, it really helps beat the algorithm. Catch you next time.
