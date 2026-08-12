---
video_id: qWzGZnV4kAk
title: EEVblog #475 - GW Instek GDS-2000A Oscilloscope Teardown
url: https://www.youtube.com/watch?v=qWzGZnV4kAk
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Tearown Tuesday. This is a follow-up to the previous video, which was an unboxing and playing around with the new GW Inst GDS 2000 A series uh VPO oscilloscope. So, let's tear it down, see what's inside, including uh

**Dave Jones:** hopefully the logic analyzer modules if we can take those apart. and uh definitely the um option modules as well for the function gen and the logic analyzer. Let's see what's inside this puppy. Just as a quick aside that I

**Dave Jones:** didn't mention in the previous video cuz I didn't know about it and you would think that because this has two function generator output BNC's on the front that this is a dual channel function generator. Well, according to the

**Dave Jones:** manual, it's not. If you read it, it says um if you plug in two of these, you can only use one at any one time. Crazy. Why have two BNC's on the front and which implies a dual channel function

**Dave Jones:** generator if you can't actually do it? It's insane. Anyway, I don't have a second one to test that, but that's what it says in the manual. So, maybe we'll start out with this function generator and uh see what's inside this. So I can

**Dave Jones:** only presume what they're doing there is having a separate B and C output coming from a dedicated uh pin on this option module. So it doesn't matter whether which one you uh which slot you plug this function gen module into. It'll

**Dave Jones:** either route it through manually through to the channel one BNC or the channel two BNC. So they don't have to put like a relay inside to switch the thing. But ah man, unbelievable. And we got four screws on the bottom here. So, we'll

**Dave Jones:** whip these out. They're selftappers. And uh what do we expect in here? Well, I it maybe is it all of the function generator uh circuitry. And literally, as I said, the uh output from one of the pins here goes straight to

**Dave Jones:** the BNC. Or whether or not there's some extra buffer circuitry inside the scope. I don't know. We haven't opened the scope yet. We won't know. But let's whip this open. And uh Oh, there we go. Mostly ground plane. It looks like we

**Dave Jones:** have a programming. So, there's some sort of programmable device in here. Let's have a look. Aha. Actually, one of the first things I noticed here was the fact that this what I thought was metal shield from the outside is not actually

**Dave Jones:** connected to anything at all. I mean, it's got these little raised bits which come up there and then actually do make contact with the board, but it's actually the um solder mask part of the board. But there's no exposed uh solder

**Dave Jones:** mask on the bottom side of that to actually make contact there. So I don't, you know, look, nothing. I don't know what the deal is there. That's just it's just floating. And this backing plate here is actually a powdercoated

**Dave Jones:** metal. It's not actually plastic. Go figure. Well, it's not an FPGA. It's an Alira Max 2 CLD in a little uh thin quad flat pack there. JTAG uh programming interface of course. Um quite a few. It looks like a you know a parallel sort of

**Dave Jones:** bus coming in to that. Not much else really. Not much doing on the bottom side in terms of the connections. There's a few around here but mostly power seems to be grouped in the middle here. And uh clearly we have our output

**Dave Jones:** down here. So it's on a fixed pin. So that would be the um So then yeah, I think that there looks like there's probably a driver on here and it does probably go through directly to the BNC output there. And uh there's the uh

**Dave Jones:** oscillator for the CPL and um yeah, there's not much else. So at least with the CPLD, it does have um some functionality, but not full it wouldn't have full arbitrary uh waveform capability or uh anything like that really. So we can see that on the power

**Dave Jones:** side of things here, though. It looks like um uh a lot of the regulation is done internally to the scope and it's just powered through here. Look, you can see it coming in here. It's decoupled with that cap through an inductor there

**Dave Jones:** and then it uh just buggers off through some uh four vas down there over to the bottom side over here to an internal layer. This is obviously a uh four layer board and uh then it powers off there.

**Dave Jones:** Looks like they've got a little low dropout uh reg there for something or other for some uh local regulation probably for the uh Max 2 uh PLLD or something like that. But generally it looks like they're just uh powered

**Dave Jones:** directly from the uh supplies within the scope, but that's not uh surprising at all. Well, there's absolutely no surprises on this uh board at all. Of course, it's going to be a DDS generator. So, apart from the uh Max 2

**Dave Jones:** CPLD, which is just um probably working as some sort of interface or glue uh logic on the board, we have tada, surprise surprise, analog devices 80 9834, one of the uh Jellybean uh 75 MHz DDS generators. I've used those myself.

**Dave Jones:** They're quite good. So, direct digital synthesis up to 75 MHz. This thing only goes to like 3 or 5 MHz. But then we have an old school LM 311 there. What else have we got? We've got a um AD

**Dave Jones:** 8000, which is a very high-speed one gig uh current feedback uh op amp. And then we have an OP. What do we got here? An OPA 132 uh precision FET op amp. OP07. Another precision op amp down in there.

**Dave Jones:** Look at that bodgege wire. Ah man. Anyway, they had to do what they had to do. I guess they couldn't respin this little board. Wouldn't have cost that much really. It's not that respinning in the main motherboard for the scope or

**Dave Jones:** something like that. Oh, anyway, sorry, another relay in here. Um, our first relay uh quad op amp TL74 just jelly bean stuff happening there. And then our output uh buffer looks to be an AD uh 8009 which is once again a 1 gig very

**Dave Jones:** high speed to give you a high gain bandwidth uh product current feedback um op amp used for pulse applications and stuff like that. And there's an output relay to switch it off and on. So yeah, pretty much uh exactly um what I

**Dave Jones:** expected really. Um nothing fancy at all. it's bare minimum, but they've actually used um analog devices uh parts in here quite expens extensively and they're not the uh cheapest thing around. So, they haven't really uh skimped on uh price anyway, but feature

**Dave Jones:** set of course eh it's just a DDS uh generator which means they can't do um ARB uh waveform capability or anything like that. It's not built in. They certainly could come out with better functionality uh in the future whether

**Dave Jones:** or not um there's any like you know second well there's no second channel modulation capability because that would um need a second uh DDS chip. This one only has a single DDS chip. So it's not like they can generate a second signal

**Dave Jones:** and then uh modulate it. You would have to do that using um you know not a discrete method like this but using a um some sort of ARB capability. And just based on the uh tracking or lack thereof, um there's really only an

**Dave Jones:** output from this. So I don't see like any sort of analog input coming in for any sort of uh optional external modulation capability with like an extra connector on the uh back panel or something like that. I well, you know,

**Dave Jones:** because this is module based, there's nothing to actually uh stop them, you know, whacking an external modulation, revising this thing and whacking an external modulation input on there, for example. So, can certainly be done. Um, they just, you know, have to release a

**Dave Jones:** new module that has that capability. Onto the logic analyzer module here, the input module, um, I don't see any screws on there. So, whether or not that's heat sealed or whether or not it's snap sealed, I don't know. I might try and

**Dave Jones:** prize it open, but apologies if I can't get that input pod open. I certainly don't want to destroy it. I'd expect there to be a little something in this cuz it can certainly uh detect that it's plugged in, but uh that could be as

**Dave Jones:** simple as, you know, shorting a pin on the connector in there. Um could be as simple as that as far as module detection goes. So whether or not there's actually anything in there, we can find out because tada. This one has

**Dave Jones:** screws. All right, this one just pops open. Little bit of a clip on the side [Music] and just a cable. And there's nothing on the flip side of that either. Just got the individual uh pairs running. This is

**Dave Jones:** for obviously the uh 16 channel. That's the extra connector up there for the 16 channel which isn't uh populated. Exactly the same pod, but uh they've only got the one connector wired in. But there you go. It's just got some power

**Dave Jones:** wired through there. the thicker the thicker traces and then the individual pairs running back. Interestingly, if you count the pairs, 1 2 3 4 5 6 7 8, you'll notice that there's an extra pair over here. There's actually nine pairs

**Dave Jones:** for each pod there. And they got exactly the same on the back. Eight plus that ninth pair. So whether or not that's for an external clock or whatever, I don't know because uh it doesn't have an external clock capability on the input

**Dave Jones:** here. And the thing with that is no external clock means no state analysis capability because uh logic analyzers have two types of mode either state analysis or timing analysis. And in this case state analysis requires an external clock so that your sampling of your

**Dave Jones:** input signals can be in synchronization with the external clock from your circuit under test. This one doesn't have it. Tada. We're into the main pod which connects to the head. There we go. It looks like um yeah, looks like we

**Dave Jones:** have some sort of E squared PROM there. We'll take a look at that. And uh there's some power, definitely some power coming through there. We'll have a look what's on the top. And that is indeed a serial EROM. So uh presumably

**Dave Jones:** that is the ID which uh then tells the firmware that this module is plugged in. So you can't just make your own pod. You'd have to actually uh copy that firmware. And of course there's no onboard regulation here. Just a couple

**Dave Jones:** of inductors there. bit of filtering powered from the uh main machine, the motherboard on the main machine. And there's the input circuitry it looks like. Although you can see the traces on the bottom side there going all the way through to the

**Dave Jones:** connector, it just doesn't seem to make sense with all that sort of stuff down there. That looks like a lot of um that looks like chip bypassing some of that. Anyway, so I think we're going to find some circuitry underneath this

**Dave Jones:** puppy. And that one there, that bunch of uh all that but those passives there, they indicate that there's active circuitry under there somewhere doing something. And likewise this one down here. So I think we're going to find some chippies under here and here

**Dave Jones:** and here. Let's flip it over. Taa. Look at that. There we go. We got some serious uh logic analyzer stuff happening here. I'm really going to have to get in there with the zoom and have a look at the uh chip numbers on these

**Dave Jones:** interesting looking LCC or are they little quad? Looks like they're little uh quad flat packs there. Going to have to get a look in there. Obviously handling two channels a pop and that's why we saw a differential um uh pair

**Dave Jones:** coming out possibly. are they uh a a differential uh driver? We'll uh have to have a look. But there we there's an OPA 1777 there. And I'm not sure what that one is. Can't read it. Let's get in

**Dave Jones:** there. But it looks like Oh, Diode. It is a diode. That's a funny looking diode package. Wow. Look at that. G13 number 119. obviously doesn't ring any any any bells off the top of my head. I'm going to have to uh go Google

**Dave Jones:** that one, but uh I'm not sure if we'll get any luck there. But uh anyway, look, you can see the individual pixels on the silk screen there. Check it out. You can see that this is a uh dot printed silk

**Dave Jones:** screen. Pretty cheap and nasty one. Jeez. But not not that it matters. Just thought I'd point it out. But anyway, we got four of those clearly uh handling two channels each. And that one there, LBMHN 891225. I don't know. Obviously, some

**Dave Jones:** sort of uh DC toDC converter locally. Um I'm not sure why. Um Jeez, does it need Does it need that much uh power right at the head to drive these uh uh logic analyzer um input buffers here? I don't

**Dave Jones:** know. Well, I don't know about that G13. I couldn't immediately find anything on Google. There's like a Renus um RL78 G13 micro, but that's definitely not it. This is only a 16 pin uh package. It's not going to be a microcontroller there.

**Dave Jones:** So, I don't know. Um if you got any info on that, um please leave it in the comments or on the EE blog forum. And there's our input network there coming directly from the connector. Small value series resistor there. 90 odd K resistor

**Dave Jones:** there. So, there you have it. I'm quite impressed by that. The build quality is uh excellent and design quality looks good and uh you do actually um get a decent logic analyzer uh input for your money. Anyway, if we've what your 500

**Dave Jones:** bucks for the uh logic analyzer option and of course um the input uh logic threshold as well. I don't know where that's um set. Clearly that's uh it it could be uh going into these devices. They could be you know fully

**Dave Jones:** programmable input uh programmable thresholds and uh stuff like that. So, that could actually be quite a little complex beast on the input there. And once again, I'm not going to spend uh a lot of time trying to track down the

**Dave Jones:** info on that. I'll leave it up to the viewer. Someone will post it. Now, let's do what everyone's come here to see. The main scope. Looks like we have uh some self maybe selftappers down here. I don't know. And a couple up the top

**Dave Jones:** here. But uh there we go. Let me zoom out a bit. Couple up the top here under the handle. And that's uh all she wrote. So as I said in the previous video, I expect this to be quite decent quality.

**Dave Jones:** GW Inst are quite a uh reputable company. Thread metal threaded inserts of course. So the other ones are obviously that I would have been disappointed if they were selftappers and uh dropped it. Always have leftover screws or not

**Dave Jones:** enough when you put it back together. Oh well. So anyway, the back cover will just lift off there. I don't see much screen. Oh yeah. Yeah, there's Yeah, there's probably a Looks like there's a big metal shield inside. So

**Dave Jones:** we'll we expect that in modern uh scopes. EMI is a big uh big issue. So they have to uh knock that on the head pretty well. So it looks like this will just pop off. I can see our noisy fan in

**Dave Jones:** there. Oh, there we go. Too easy. Tada. But it looks like no. Oh yeah, there we go. Separate power supply there on its own board. Not shielded um in its own right, which uh is a lot different to uh

**Dave Jones:** some of the other uh scopes I've modern scopes I've taken apart. Usually this is uh or in its own power supplies in its own uh shielded enclosure, but no, there it is just hanging its ass in the breeze

**Dave Jones:** there. So that's not uh terribly exciting. If you don't like the noisy fan, you could get in there and uh replace that. Not a problem. They've got a separate output board here, which we'll take a look at for the uh USB and

**Dave Jones:** the serial and the uh other BNC's going via cable. It's all neatly cable tied. Not a problem. We got our slots coming out here, our PCI slots, and well, looks pretty simple, but nothing wrong so far really apart. Bit disappointed though

**Dave Jones:** that there's not a shield on that. Actually, one thing that just became immediately obvious where uh I really haven't uh seen this before. Where are the output voltage cables on these? Usually you see nice big beefy, you know, individually wide output cables,

**Dave Jones:** big molex connector, something like that. Nice high current things like that. No, all we've got is a bloody standard.1 in ribbon cable. Are you kidding me? That's the entire um output supply from this thing going over to the main board. What how much power

**Dave Jones:** does this thing take? It can't take much or either that or they're really pushing the margins there with a little Well, they're probably using multiple pins of course, but you know, there's generally rule of thumb with these is only an amp

**Dave Jones:** uh per pin or thereabouts. But yeah, I just jeez a.1 in header. Give me a break. Now, this is interesting. Check out this. They've just got like like an afterthought almost. Oh, let's just bring this winding out here. We don't

**Dave Jones:** have enough pins on our on our uh the bottom of the thing. Let's just bring out an individual winding and put it in there. And yeah, okay, they've glued it down. That's okay. But jeez, you know, um almost like an afterthought. They've

**Dave Jones:** glued that resistor in there. A little bit of attention to detail just to ensure that doesn't flap around in the breeze. They got some input protection down there. I see a uh mauv and a thermister down there. Fuse of course.

**Dave Jones:** Um it's not directly soldered in. Why they've got this just jumping over to there like that, I don't know. Um it maybe it allows them uh to get a current clamp over that thing perhaps. I don't know. Um weird. Anyway, looks like we do have

**Dave Jones:** a common mode choke here filtering. So they're at least doing uh all the basic filtering stuff. There's our big ass um clunking mechanical switch there. Very nice. I like that. It doesn't look like they're uh they're faking that and just

**Dave Jones:** doing uh standby power. You can see the optoouplers down in there. It's, you know, it looks like a pretty basic uh reasonably designed power supply. Let's take a look at the brand of the caps. That folks is a nipon chemiccon symbol.

**Dave Jones:** I didn't expect a nippon chemicon in here. Excellent. top worldclass brand cap in there. I assume it looks like all their all of them, even the output caps over here. Nipon Chemiccon. Brilliant. Every single one of them, they haven't used another brand

**Dave Jones:** electro in there. Very nice. I'm impressed. Thumbs up. And they're the KMG series for those playing along at home. 105° C. It got that a tad close to the uh p almost touching the heat sink down in there. That's not great for uh

**Dave Jones:** longevity. Once again, another one right next to the heat sink. But you know, these things you are cramped for space. But you know, that one over there, there's probably no excuse for putting like almost touching that heat sink

**Dave Jones:** really. But anyway, I'm impressed with the quality of the caps, that's for sure. Usually you'll get a mix of uh brands of caps in this thing, but uh in a typical uh power supply, they'll like, you know, skip on the ones that aren't

**Dave Jones:** super critical to the design. They'll skimp on a cheaper uh brand to save a few cents here and there to trim off the bomb cost. But no, they've used Nipon Chemicon throughout. And there's nothing worth looking at on this uh USB and uh

**Dave Jones:** RS232 connector board up here. put your notes. Notice the nice little uh RFI EMI uh fingers there on the connectors. Nice. They've done that right now. It's interesting to note when you look at the side profile of this thing, you'll see

**Dave Jones:** all the circuitry is within half the depth of this thing. The other half is taken up with the power supply in this horizontal configuration like this. And the fan which is then you know mounted out like that and this connector board

**Dave Jones:** on the back. If they really wanted to uh you know uh put some engineering effort into it this they could have actually made it not much thicker than that itself. But then again it almost becomes pointless because well how do you you

**Dave Jones:** can make something that thin for sure but then how do you keep it from you know falling over and stuff like that? You got to have proper you know tilt feet like that that come you know that come out to give it some uh counter um

**Dave Jones:** balance on there and that sort of stuff. So, eh, but interesting to note they could have done that. And ta, I pop that whole metal shield off and we're in like Flynn. Look at that one main board. Of

**Dave Jones:** course, no surprises. I sense an analog devices black thin DSP up here. We've seen those before in the uh Ryol. heat sink stuck onto. Oh, I could almost move that, but I won't take Oh, should I try and get those heat sinks off to have a

**Dave Jones:** look at the chip? I don't know. I probably shouldn't. Oh, jeez. But look, looks like we can get through the metal shield here for our four channels. This is marked as the four channel board. Of course, the two channel board presumably

**Dave Jones:** uh the two channel scope wouldn't have uh complete two channels populated in here. and probably that second device here cuz as you saw in the second video uh the sample rate does have when you uh turn on um channel one and channel two

**Dave Jones:** for example the sample rate halves. So obviously they've got the one chip controlling two channels the second device over here. So that's why if you turn on channel one and channel three the sample rate doesn't have because you've got a separate chip handling each

**Dave Jones:** one. But presumably they wouldn't be silly enough to uh populate all those if you're only buying the twochannel model cuz it's not software upgradeable or license upgradeable or anything like that. You're physically uh paying more for the extra twochannel front end.

**Dave Jones:** Probably the extra chip there and maybe something else. But that's the main cost. But there you go. Um it's pretty spartan actually. I I like it. Let's have a look at the main devices. All right, three devices here. analog

**Dave Jones:** devices, black fin DSP, ADSP, BF531. We've seen these um that's used pretty uh frequently in these um scopes actually. So yeah, it seems to be uh the processor of choice for uh uh driving um well the gooey interface of these uh

**Dave Jones:** scopes. Of course, it doesn't handle uh you know the input sampling and uh processing and all that sort of stuff. It's just pretty much the uh you know the operating system, the on-creen graphics and user interface and things

**Dave Jones:** like that. Then we've got an ISP 1761 USB uh host controller and also an outer max 2 CLD same as what we saw in the module there. And then no surprise to find that that CLD is actually hooked up

**Dave Jones:** to uh the modules there. So obviously some sort of glue logic that uh handles the uh module module function capability something like that. and coupled around what's clearly an FPGA uh under here. I don't know if I'll remove that heat sink

**Dave Jones:** yet. Could be really messy. I don't know. But anyway, we got ourselves a GS 88036 uh CGT, a 9 megabbit uh synchronous SRAM in a 256K time uh 36-bit configuration. So, effectively a total there of uh only 2

**Dave Jones:** megabytes. But that's what this thing's got, 2 megabytes of sample memory. So clearly that's uh 2 mega sample memory with an extra bit. And of course coupled onto our FPGA, these two suckers under here are obviously our analog to digital

**Dave Jones:** converters and dead giveaway because they're right near the vertical front ends. The vertical front end straight out of the programmable gain amp there straight up into the dual analog to digital converters. As I said, if you bought the two channel module, you'd

**Dave Jones:** probably only get the one ADC. And curiously, next to that, there is a metal can. Check that out. And that one's actually soldered directly onto the board. What a bastard. I'm definitely not going to uh desolder that can to see what's under there, but I

**Dave Jones:** don't Is that like a ADC clock or something perhaps? I don't know. Let's have a look at that puppy in there. Looks a bit interesting. And no surprises to find an ultraast comparator. Analog devices AD CMP 567. um obviously used for uh part of the

**Dave Jones:** triggering circuitry. And tada, I popped the heat sink on it and here it is. They haven't scrubbed the numbers off. Brilliant. The ADC is a um national semiconductor now TI ADC uh 8D500 which is a 500 meg sample per second 8bit dual

**Dave Jones:** analog to digital converter. So basically um one of these converters is only capable of either 500 meg samples per second on dual channel or one channel at 1 gig sample per second if you interle them. Now of course this is

**Dave Jones:** a 2 gig sample per second scope. So maybe the two channel version actually does populate both analog to digital converters and that's how they get using four of those converters in two chips. That's how they get the 2 gig sample per

**Dave Jones:** second. Either that or they're overclocking. And I popped the skirt on the main chip there. And of course, yes, I was right. It is an FPGA offtheshelf Alira Cyclone 4, the EP4CE30F29 blah blah blah. Go look it up

**Dave Jones:** if you want to know the exact gate count and feature set. Now, here's the interesting thing or possibly not so interesting thing depending on how you look at it. compared to the Ryol and the Agyant tearowns that we've seen in the

**Dave Jones:** past. For example, modern scopes. This one, yeah, we got our ADCs here. We got our one FPGA here. Pretty good FPGA in it, but it's only one. So, presumably this is only doing the uh the sampling, all that sort of stuff, and the trigger

**Dave Jones:** and everything else, plus probably, you know, the intensity grading, the color mapping, and all that sort of uh jazz as well. But look where the LCD is connected. It looks like it's right next to coupled to the analog devices black

**Dave Jones:** fin DSP. Now, if I can't see where the traces on there go, they could actually go down here to the FPGA. In that case, okay, they're mapping the data directly from the FPGA onto the screen, and that's how they're able to get 80,000

**Dave Jones:** waveform updates per second. But if they're not, then they're driving it from the BlackFin DSP, and that's going to be a big bottleneck, and that's probably why the intensity grading isn't that great. But anyway, I'm not going to

**Dave Jones:** make a call until I flip it over and see where those pairs are going. So, they're either they could go over to here. I see a couple of traces see a bunch of traces in there that could jump over, but uh

**Dave Jones:** more likely, I think it's due to the placement. But then again, I don't know. Let's flip it over. Anyway, that's different to the Ryol one, which of course has a dedicated display FPGA, better horsepower, and that's how it can

**Dave Jones:** get like its uh uh multi uh you know, 256 level intensity graded display or whatever it is. Whereas this one, um, who knows, they might be doing it in and taxing that poor old black fin processor. And to get the main board

**Dave Jones:** out, unfortunately, we do have to lift out the entire or take off the front panel with the rubber key mapins and everything else. So, well, I'll put those back into place soon. Where'd they come from? There. There we

**Dave Jones:** go. Tada. Not a problem. There we go. That's our front of our board. There's the top key mapping. Nothing exciting on the top here. I pro I won't even bother uh like unscrewing all of the um uh the

**Dave Jones:** top board here and the LCD. Not very exciting. I just want to take a look at the underside of that board. We've got the LCD cable hooked on. But ah there we go. Got some more memory on the bottom.

**Dave Jones:** Aha. Yep. Duplicated memory on the bottom there. So we've actually got double the me amount of memory that I said before. Looks like exactly the same devices that uh we had on the top. So, yep, doubled our amount of memory. We

**Dave Jones:** got our program flash down here and uh that but that's all it that's all she wrote. And there's those VAS for the LCD there. That's the LCD cable. Goes up to a separate uh board in there. Not much

**Dave Jones:** doing there at all. It's just got a little bit of a uh is that a like a backlight inverter or something on there? I don't know. Um but yeah, nothing interesting. But I can't see where those traces go. But whether or

**Dave Jones:** not they come down here to the main um FPGA, it doesn't look like they do. I think they've got to be coupled into that DSP. So, my money would be on the Blackfin DSP handling all of the display

**Dave Jones:** processing, and that's a bottleneck compared to the Agyant one, which does it in the Mega Zoom 4 ASIC and compared to the Ryol 2000, which does it in a dedicated FPGA. But you know what? If that's actually the case, then getting,

**Dave Jones:** you know, the 80,000 waveform updates per second uh via that BlackFin DSP is actually quite impressive. And on the back back side of the uh input amplifiers here, we got a reasonable amount of heat sink. Uh well, you know,

**Dave Jones:** a bottom ground plane heatsink. You can see all the VAS uh via stitching there going from the back of the device, thermal pad on the back of the device there. That would be like um the output uh amp which is driving the um ADC which

**Dave Jones:** are around about here somewhere. And uh that because that's the top part that would be the final output uh uh differential uh driver to drive the uh ADC differentially. Not much on the bottom of the uh uh front end here. The

**Dave Jones:** front end's very uh unexciting. And they got some solder mask removed in uh various spots here where they uh you know because this is like a 300 MHz uh bandwidth front end. Then uh yeah, they've just uh removed some ground

**Dave Jones:** plane on the top there just to get the performance they need. But apart from that, nothing else interesting on here. Apart from all the decoupling on that FPGA. So there you go folks. If you want to know what sort of decoupling's

**Dave Jones:** required on the bottom of something like that uh Spartan 6 FPGA in there, pretty big beast then. Yeah, look at all that little bastard 0402 parts in there. But yeah, you have to do that to fit them in. But that is the sort of uh

**Dave Jones:** decoupling you require. And of course, this would be like a six or eight layer board in able to uh in order to fan out all the signals. You can see all the VAS in there. There's lots of uh decoupers,

**Dave Jones:** you know, solid decoupling in the middle in there, but uh some of these vas have to get all the way out past all these other ones because you can only run one or maybe two if you're lucky uh traces

**Dave Jones:** between each pad. So, you got to have all those different layers to route out all the signals. And of course, the soldering is first class on this. Can't find any problems at all. No leftover residue or anything like that, both top

**Dave Jones:** and bottom side of the board. And for those curious to see how they handle big thermal mass items like the front panel B and C there, those solder joints, yeah, look cold and frosty, but that's the lead-free stuff for you. There's

**Dave Jones:** absolutely nothing wrong with that at all. And speaking of the front end, I'm sure we have a lot of people very interested in the design of this 300 MHz front end because yes, it'll be the same design from the 70 MHz model upwards.

**Dave Jones:** And if you want to uh check out the high-res uh photos of this board, uh hop on over to my Flickr account. The uh link is always in my description below. That's where I post uh usually uh post

**Dave Jones:** high-res photos of my tearown. So, I'm sure there'll be no shortage of uh people uh sort of reverse engineering this front end as well. You don't have to reverse engineer it. You know, it's pretty easy because they haven't rubbed

**Dave Jones:** off any numbers at all here. But there we go. We've just got some uh input uh coupling there. On the input, we've got a relay. We got two relays. Looks like we got a solid state relay. We got a

**Dave Jones:** trimmer cap. Got another trimmer cap. Further up, we got a second relay there. And uh a few passes. And there's a few transistors in there as well. Discreet. And all that leads up to tada. That would be our output programmable uh gain

**Dave Jones:** amp and ADC driver. That's the one that's actually heat sunk. So, that'll have a thermal pad on the bottom of that, which then goes through to the uh exposed copper on the other side to uh try and keep the heat down on that. I'll

**Dave Jones:** see if I can get the part number. I see it's a National Semiconductor. And yeah, National Semiconductor VM21AB. It shows that you really have to get the angle on this to really read these suckers. You just got to get the

**Dave Jones:** right contrast. There it is. Let me go look that up. And aha that's actually the uh LMH6518. And no surprises whatsoever, it is the recommended device for that particular national semiconductor analog to digital converter designed or you know very uh well listed one of the

**Dave Jones:** applications for an oscilloscope front end. Go figure. And that's actually a 900 MHz programmable uh gain amp. And yes, it does have via SPI. uh the gains controllable via SPI and yes it does have internal bandwidth limities um on

**Dave Jones:** the output of uh I think 60 100 200 and then 350 MGHertz so they're probably using that as the bandwidth limiter although I wouldn't rule out that they've got something else down in there that they could switch with a digital

**Dave Jones:** line or something like that to do the filtering. Um, so yeah, I don't know. Someone will no doubt uh reverse and you know, I don't see a veractor in there or anything like that. There certainly could be. I don't know. I'm not going to

**Dave Jones:** decode it. I'll leave that up to uh the afficionados out there to uh tell us exactly how their software bandwidth limiting this thing. And uh but yeah, there's definitely the capability built into that device directly on the output.

**Dave Jones:** So if they are actually using this chip as the bandwidth uh limiter for the different models then yes in theory you could get in there tap into the SPI line and then um you know and change the command to increase uh the output

**Dave Jones:** bandwidth of that um ADC uh driver amp. But uh who knows they may actually um because this thing is not software upgradeable they may actually uh choose different parts in there for example. So there could be different resistor or

**Dave Jones:** capacitor values or something like that to actually uh bandwidth limit that uh somewhere else. But then that wouldn't leave their options open for the future if they wanted to then offer a bandwidth uh upgradeable model. So yeah, anyway,

**Dave Jones:** in theory, you could actually crack into the SPI bus on that and um change the gain to anything you like. Um but of course then you wouldn't have things like the uh timebased setting and other stuff in the uh software. So yeah, I

**Dave Jones:** don't know. I'll leave that one definitely up to the afficionados. Now, interestingly, uh if you look at the membrane, key membrane on the front panel, there's three more buttons down in here, and it's like, aha, is there, you know, some uh

**Dave Jones:** upgraded or some potential future upgrade? Well, let's lift that up and have a look. Uh it looks like it's just duplicated. Look, math ref bus. And for those curious to see what uh the rotary encoders are, well, they're 124A1. I have no idea. There's

**Dave Jones:** no brand marked on there at all. So, of course, these things get wear and tear. They are something that uh could potentially or almost certainly will eventually uh wear out in some people's machines. Depends on how often you use

**Dave Jones:** them. So, if anyone has any more details on that, post it. And for those curious to see the uh trigger circuitry in here, well, I'll post the high-res photos. I won't go into uh details here, but if anyone wants to uh any of you trigger

**Dave Jones:** afficionados there, want to uh check it out, by all means do. Aha, there's the same AD CMP 567 we saw further up on the board. And that's that ultraast comparator. So, there you have it. That's a tear down of the new Goodwill

**Dave Jones:** Inst GDS 2000A series oscilloscope. And uh thanks to GW Insting that in. Most interesting build quality. Um yeah, first class as you'd expect like from a company like GW Inst. They're not one of the uh one hung low cheapies, that's for sure. So build,

**Dave Jones:** solder quality, design quality, very well done. I like it. Um no problems whatsoever. um just a bit maybe um just a bit underpowered say compared to the uh Ryol uh 2000 series for example or the Agyant um 2000 series as well with

**Dave Jones:** their Mega Zoom 4 A6. So yeah, only the single F FPGA. I was a bit surprised by that. But I was expecting to see a uh second one, but uh I guess um the I still don't know um whether or not the

**Dave Jones:** uh display is directly driven from the um analog devices black fin or the FPGA. I'll have to uh figure that out or if somebody can uh come through with more info then uh please tell exactly how they're doing that. But anyway, that was

**Dave Jones:** an interesting tear down as it always is with these uh test equipment. I really like them. And as I said before, if you want to see the high-res uh photos of this, jump on over to my Flickr account.

**Dave Jones:** The link will be down below, and there'll, I'm sure, be no shortage of people discussing this on the EV blog forum. So, if you like tearown Tuesday, please give it a big thumbs up. I'm working late tonight, 7:30. Well, that's

**Dave Jones:** late for a family man, you know. Catch you next time. Move down.
