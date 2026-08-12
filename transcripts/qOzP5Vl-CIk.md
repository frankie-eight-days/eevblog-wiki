---
video_id: qOzP5Vl-CIk
title: EEVblog #525 - Bank Note Acceptor Teardown
url: https://www.youtube.com/watch?v=qOzP5Vl-CIk
source: youtube-asr
---

**Dave Jones:** Hi, welcome to teardown Tuesday. Why do I have a Yankee five buck note here? One of these funny money cotton based crappy notes. In God we trust. Well, it's a good question because we have for today's teardown one of these

**Dave Jones:** note validators or bill validators or bill acceptors or note acceptors, whatever you want to call them. The ones that you typically find in vending machines and things like that that accept your bill. You feed your hard earned money in there and it either

**Dave Jones:** accepts or rejects it and detects whether the currency is legal. So I thought we'd uh teardown one of these. Could be a rather interesting. This one is a money controls. They're one of the probably not one of they're not one of

**Dave Jones:** the major manufacturers of these things but they are one of the reputable reputable manufacturers anyway of these bill acceptors, bill validators. And this is the MC 2600 model that we've actually got here. And there's a lot of art and science which

**Dave Jones:** goes into detecting whether or not a note is genuine or not. And it's going to vary between runs of notes over time. They do actually change things and different currencies as well. I mean this silly US cotton based funny money

**Dave Jones:** is just you know crap compared to like in terms of security compared to a Australian designed technology designed in Australia by the way. These are polymer bank notes we've got in Australia. I mean we basically don't have a counterfeiting problem here in

**Dave Jones:** Australia because we use these very secure polymer notes. But sort of actually detecting notes like this going to use different technologies or can use different technologies to this simple US currency or is it that simple? Well, they've got as you might know, they've

**Dave Jones:** got hidden watermarks in there. They've got security strips in there which are fluoresce it different colors I believe under UV lights and you can tell the bills apart that way. They use magnetic inks of course and even some of the

**Dave Jones:** watermarks with the magnetic inks they can resonate at different you know, resonate a a a detector circuit at different frequencies based on what type of note it is cuz not only do you have to determine whether or not it's a genuine

**Dave Jones:** or fake note, but you have to determine or the unit has to determine the currency of the bill as well. Is it a $1, a $5, a $10, a $20, you know, whatever. So as we'll see as various

**Dave Jones:** technologies that goes into this and you can easily see this for example, if you just really light up these notes from behind, it's it's not hard to actually see Here we go. There's a hidden five in there for example, you see that big five

**Dave Jones:** in there which isn't of course on the reverse side there. So that's you know, there's an inbuilt watermark right there and of course there's the strip. You can see that. I'll zoom in. You can't see it on the note. It's basically right down

**Dave Jones:** there, but if we shine that from behind, you can see it's got USA five on it and that security strip goes all the way down there and I believe I don't quote me on this, but that fluoresces under a

**Dave Jones:** different color under UV light and they can use infrared detectors and all sorts of other detection mechanisms to to detect whether or not these bills are genuine. See there's five going down there. You can see the see the watermark in there.

**Dave Jones:** So 555 plus the security strip. That's a at least an absolute minimum that they've got going in these US $5 notes. And as I said, they do change things up occasionally. So, these bill validators occasionally have to be updated with new firmware. You

**Dave Jones:** know, they may not accept the new 2013 $5 bill, for example. So, you got to go out and update the firmware for this sucker. But, yeah. So, something like this note validator here is going to use various technologies. So, I'd expect and

**Dave Jones:** dimensions of bills, for example. They're probably going to, you know, make sure it's the exact size and things like that as as a minimum. So, really we expect to find quite a few sensors in here. And as you can see, they've

**Dave Jones:** obviously there's like one main control board in the back here. It's got various notes. We'll take a look at that. But, it's got like a sensor module down the bottom of here underneath the or in as part of the slot. And then they've got a

**Dave Jones:** cable running over there to the main board like that. And this money controls a unit basic dip switch interface. And then the vendor, you know, the person who owns the vending machine can just, you know, set it to accept various

**Dave Jones:** notes. It's designed to accept 1, 5, 10, and $20 notes. No higher. And yes, it is a used unit. I don't know if it actually works or not. It's obviously been pulled out of a unit. But, anyway, you can

**Dave Jones:** enable and disable the various currencies. And then this is a very simple pulsed interface one. It has, as we'll see on the other side, does have other interfaces as well. But, basically it can just give out one or four pulses per

**Dave Jones:** dollar. So, that's how other circuitry in the machine can actually detect things. So, you put your note in there. Doesn't give change or anything like that. It just accepts the note and either puts it in the cash box in the

**Dave Jones:** back, which we'll take a look at, or just throws it back out. And it actually came with the cable to hook up to it. And it just plugs in here. I mean, it does have a serial interfaces. There you

**Dave Jones:** go, and it's got a download diagnostics as well. You can For this particular brand, you can buy a diagnostic box which hooks up to the PC and you know, allows you to extract data out of it or change it or maybe even update the

**Dave Jones:** firmware remotely. I'm not entirely sure about that, but this one can be a simple This one's a 120 V AC model. You can get ones based on a 12 V DC and stuff like that. So, that just plugs in there and all we've got is

**Dave Jones:** basically 120 V AC in and just a relay contact out or a you know, a pulsed contact out which gives the number of pulses based on the bill and whether or not it's accepted it. That's it. So, incredibly simple interface. Just four

**Dave Jones:** wires plus ground. So, obviously the bill goes in the front there. There's a sensor board in there which actually detects all the stuff. There's a processor board in the back and then this big thing looks all complicated, but

**Dave Jones:** it's not. It's very simple. You just release that clip and this is the money box. There it is. That just It's got a couple of springs in there and that just fills up with money. Obviously, I'm not sure

**Dave Jones:** how many actual bills you can fit in there. I don't know. I don't know. What's the average thickness of a bill? No idea, but you know, you might get 500 or bills or something like that in there. So, I'm not sure how that would how long

**Dave Jones:** that would last in a typical scenario, but there you go. There's the diagnostic stuff for and yeah. And basically, they've just got some belt and pulleys which then suck the note through here. I'm not entirely sure exactly how I assume this one if it

**Dave Jones:** rejects it will spit the note back out. So, maybe it only comes partial part of the way in cuz it's not like the note sort of pops out the back here and then either gets directed into there or spat

**Dave Jones:** back out. So, it probably comes like halfway in, detects if it It detect that it's a valid bill, it just reverses the motors and whoop, shoots it back out the front. But yeah, that's all there is to it. Um mechanically, um you

**Dave Jones:** know, pretty simple. And if we take those four screws off the front, bit of a dust Yeah, bit of dust in there. Smells, but uh we're in and we have our first look at the main board there. That's the bottom

**Dave Jones:** of the main board. They've got uh very nicely aligned SMD resistors there. I rather like that. They've got a flat flex cable going into It looks like they've got a top sensor board and there the status LEDs there. They I didn't see

**Dave Jones:** that, but they obviously uh poke through the front and that's what we had on the back here. That's what they had on the unit, the uh back of the unit here, the uh diagnostics. Maybe I should actually power this thing up before I

**Dave Jones:** uh take it apart, just in case I goof up some of the mechanicals or something like that. I think I might give it a go. Okay, I think I've got the pin outs correct. This is of course a US 120

**Dave Jones:** volts AC 60 hertz. So I'm using my um uh variable frequency converter here to uh generate just that. I've got the ground wire hooked up as well. So hopefully the magic smoke and no smoke doesn't escape. Let's give it a go.

**Dave Jones:** Oh. That sounded good. All the motors went, so let's whack in our funny money. I don't know which way up. Uh there we go. It gives you a photo of the head, I guess. There we go. Let's Let's give it a go. Give it a bill.

**Dave Jones:** Hello. It's not detecting. It's not detecting my note. No. No. Uh fail. Oh, there we go. We had something. There we go. No. So, it's obviously it's just rejected that straight away. No, there we go. Ah, what I did there is flicked a dip

**Dave Jones:** switch on the side here which just changed it from the pulse from vendor serial to pulse protocol. So, maybe, you know, that's what was going on there, but it doesn't like my $5 note as all at all. I've got

**Dave Jones:** two of them. So, I'll try another one and uh No, it does not like that in the least.

**Dave Jones:** No. I'm pretty sure the note has to be up there. I mean, you know, Yanks are probably laughing at me because uh our our ones here pretty much accept the bills basically in, you know, any um any orientation at all. But, yeah,

**Dave Jones:** that's not No, it's just rejecting my $5 note. Unbelievable, but it I don't know. Is this a new note? I don't know. When was it manufactured? You know, you'd have to know like it does this support the latest firmware

**Dave Jones:** for this $5 bill. I've got $5 enabled on the dip switch on the side, but yep, it's not accepting. Bummer. So, it'll have to be properly vertical. Is there something going on there? No. Sometimes it doesn't go in all the

**Dave Jones:** way at all. No. No. Loser. It's kind of doing the business, but it's not accepting my note. Bummer. Let's just have a look at the back of that when we shoot that bill in, shall we, and see what uh

**Dave Jones:** Yeah, as I as I thought, yeah, it goes like partial way in and then so it doesn't feed it all the way in. Only when it accepts it and it gets to that point, it processes it accepts it, will

**Dave Jones:** it uh feed up the whole way and then uh put it in the um the little storage container. And popped off that top cover there. Easy. We've got some uh cutouts in the board here for three large caps

**Dave Jones:** there. And of course, there are obviously a bit of a premium on space there. So, and there's not much of circuitry on the board. So, they've decided to make some cutouts there. It's not you know, not uncommon for space

**Dave Jones:** sensitive applications to do something like that. But, let's get the rest of this board out and we'll take out these ribbon cables here. And see what's on the top side. So, we'll lever that out and it looks like

**Dave Jones:** they were held in with clips. So, this board should just pop out. Too easy. There's one more cable. Oh, a Lattice semiconductor part. We're going to have a good look in here. But, check that out. Interesting. It's a rather interesting

**Dave Jones:** board. You know, there's quite a bit of logic going on happening over here. There's a Lattice PLD over here. There's a 68 uh 100 processor which we'll take a look at. There's the prom obviously for the thing and basically we're in

**Dave Jones:** sandwich sort of in the middle here is the mains switch mode power supply. Obviously, there's our switch mode transformer there. There's our high voltage caps 200 V a pop. And yeah, I mean you know, input fuse there and we've got some protection. And but

**Dave Jones:** we've got I mean obviously, you know, not a huge um sort of thought given to differentiating or isolating these sort of you know, the low voltage stuff from the mains side here. So, I mean there's you know, the

**Dave Jones:** dip switch sort of right next to the main input filter caps. You know, you got to it's crazy. Anyway, we've got some regulators, you know, some low voltage regulators, low side regulators around here. Maybe they're like some little

**Dave Jones:** optocouplers or something like that for the digital out. I mean, here's our mains input here. So, it's popping in here. So, yeah, just looks a bit real, you know, it's a just messy business. I sort of, you know, not huge amount of

**Dave Jones:** thought has gone into that. Sort of, you know, hack and slash kind of design, I think. Anyway, we've got ourselves a couple of optical detectors here. This one here is for an optical encoder wheel down there, if you can see that

**Dave Jones:** properly. So, that obviously turns around with the motor just to ensure, I guess, that a bit of feedback to ensure that yeah, the motor has actually turned and the thing, you know, maybe for slipped bills or or something like that,

**Dave Jones:** perhaps. Some some sort of detection. Another one here which you know, mates up with uh this over here which I'm not sure. That just looks I'm not sure how that moves at all. That little plastic is just like

**Dave Jones:** a plastic tab. So, I'm not quite sure what that one's doing there. Maybe some sort of, you know, this thing's going to have maybe, you know, a little bit of anti-tamper stuff in it as well, but I really know what that's

**Dave Jones:** doing. I mean, whew, strange. What does it detect that this whole mechanism has popped out of the bottom? I don't know. Hmm, you know, that firmware sticker might explain why possibly it didn't accept my note. One of the reasons, um

**Dave Jones:** look, it's dated 2002. So, 11 years old unless you know, unless the sticker's old and it's uh reflashable or something. Let's have a poke under here and actually have a look. Yeah, that's really crusty. Looks like it's been on there for

**Dave Jones:** 10 years or more, that's for sure. Let's have a look at what we've got. There you go, it's an AM29F002. So, it's a 2 megabit uh from the parallel flash. Um prom. So, yeah, it's it is reflashable, but I doubt it has the

**Dave Jones:** internal ability to reflash remotely. I'm going to probably have to take it out, whack it in your programmer, and do it that way. Now, to understand whether or not that flash chip contains the actual firmware for the processor or

**Dave Jones:** maybe contains, you know, the in all the data and the images and all sorts of other stuff for the various nodes and things like that. All the data. Seems a bit big for that. Anyway, to figure that out, we need to

**Dave Jones:** take a look at the exact type of processor here. And they've got a Motorola now Freescale, of course, MC classic MC68HC11. But, of course, the 68HC11 comes in endless varieties. Some contain internal prom, some don't. E-squared prom, this, that.

**Dave Jones:** They come in a million different types. Well, this is actually the F series chip, and you can't confuse it with other series like the E series, different again. And so, you've got to look at the F1 and then the CPU 5 after

**Dave Jones:** that. So, we need to go into the data sheet and have a look at the specific type type of chip to see whether or not it contains an internal ROM or not. And I checked the data sheet, which I will

**Dave Jones:** link in down below for this thing. If you want to follow along at home, no, this one does not contain an internal ROM. Although, it's got an internal E-squared prom, only 512 bytes. It's got like 1K of SRAM, not a particularly

**Dave Jones:** powerful processor at all. It does have a built-in 8-bit multi-channel ADC, though, which they're probably using for some probably using for two measure some of the sensor stuff. So, we'll have to check the other chips to see if there's

**Dave Jones:** an external one there. But, yeah, they're possibly using that. So, obviously, this is the firmware for all of that. And I was going to say that, you know, because we've got a Lattice um uh PLD over here, maybe they could have

**Dave Jones:** interfaced the memory through that to sort of, you know, externally program it and then sort of, you know, route it through to the CPU here. But by the looks of that, no, it's just going it's just going direct. I can't see anything

**Dave Jones:** on the back there, but anyway, internal layers there. But that's no, it's running straight over. So, I think to reprogram that sucker, we need to uh you know, you need to pull it out or the uh service tech comes along, pulls

**Dave Jones:** it out, reflashes the chip, and then uh updates it for the the latest currency. So, most likely, yes, this contains, unless they didn't change the sticker, contains the firmware from 2002. So, any notes after that, if they have changed,

**Dave Jones:** this thing likely won't accept them. And the PLD here is an old Lattice uh Mark 4 PLD, only 64 macrocells. You know, it's pretty tiny, not much doing there. But uh obviously, they need it for some sort of uh glue logic in there. Not sure

**Dave Jones:** what. And we've got ourselves an ISSI uh external SRAM there. In this case, uh 32K * 8, big whopping uh SRAM cuz this thing doesn't have much, as I said, like 1K. So, obviously, they're using the PLD as some sort of glue logic to uh maybe

**Dave Jones:** uh you know, get that into the processor. Although, should be able to just uh whack that straight on the bus. From the mains power supply, we've got ourselves a power integration uh top switch device, a top 247R, and that's

**Dave Jones:** just a uh flyback controller. There's our flyback transformer down there, and uh you know, nothing special going on the uh main side of things there. Just got a fuse on the input there, common mode choke, our bridge rectifier is uh

**Dave Jones:** four separate diodes underneath there, our filter caps, and then our main flyback controller, and Bob's your uncle. And there's our feedback optocoupler hidden under there. And as I said, just very messy layout. I mean, I don't like it at all. Look at it. It's

**Dave Jones:** not over near here, near the photo interrupter, and it's just Ah, it's it's terrible. Awful layout. And the only other thing of note on here is this uh Texas TLV5629, and that's an 8-bit uh DAC. Probably not a huge surprise to find that on there.

**Dave Jones:** So, they're using the DAC to drive some sensor stuff, probably, and the built-in ADC, as I said, in the HC11 over there, reading that back. But whole bunch of transistors, not sure what's going on there. Maybe that's a part of all the

**Dave Jones:** sensors. And what's that little sucker? No idea. Uh looks like a 74HC14 We've got you know, it's part of the secondary power supply here. There's an LM324, by the looks of it. And And this AE2595 is just an 8-channel open collector

**Dave Jones:** driver, like it just like the classic ULN2803, for example. But you know, here it is, over here. It's obviously driving the output pins, but where are they? I mean, they're all the way all the output connectors all the way

**Dave Jones:** over on this side of the board. Crazy. And same with the MAX232 driver. I mean, where's the connector? Over here somewhere. And actually, just with the layout of the board, I just noticed something. The You can see, you

**Dave Jones:** know, it's a multi-layer board. You can see the internal, the darker green in there. You can see that's flood filled all the way through, even all over this mains section here, complete ground plane right around the whole blinking

**Dave Jones:** lot. And that's also, you can actually see that um a similar thing happening on the top. I can't get a good light angle on that, but you can see it definitely happening here. And here's the mains input here. Right? This

**Dave Jones:** connector here. Here is the two mains input, right? You know, active and neutral. There it is. There's the ground input, of course. The ground input is actually connected through to the ground plane on the bottom and they cut this

**Dave Jones:** trace running over here. And that's all connected. So, the ground is connected through. And of course, this is a flyback uh mains uh power supply. So, the outputs are going to be isolated from the mains. But look at the clearance.

**Dave Jones:** Look, just around the pad there. Are you [ __ ] me? Like the person that laid out this obviously has no clue about the I meeting any standard, I guess. And cuz I don't think I think it's unlikely to and um you

**Dave Jones:** know, be just how to layout boards for clearance. I mean, it's just an absolute mess. And to have one solid ground fill all the way with just that little piss-ant amount of clearance in there. What is that, you know? A couple of millimeters?

**Dave Jones:** You got to be [ __ ] me. All right. Well, enough of the PCB cuz there's nothing really special on there. It's a processor with a DAC and an ADC and maybe a bit of analoggy stuff and that's about it. So, let's uh see if we

**Dave Jones:** can get into this um sensor part. I think that there might be a uh top and a bottom board there. You can just actually remove the entire sensor thing like that. And uh whoop whoop whoop, lost some pulleys and

**Dave Jones:** things. Oops. Oops. Yeah, I did take out a few screws and well, I'm a few screws loose. And sure enough, there are two uh sensor boards in this thing. This is the bottom sensor board and uh nothing special on

**Dave Jones:** the backside there. It's just a double-sided board and uh it looks like there's no huge amount of circuitry in there, but we've got a couple of uh LEDs and things. We've got our um edge to our uh note edge

**Dave Jones:** detection here. So, you know, clearly there we've got a LED here and a phototransistor over here. So, as soon as you put the bill in, it uh interrupts that and it knows to uh uh then uh feed that through with the various uh rollers

**Dave Jones:** on the uh top and bottom side here. Here's the front rollers, which I've actually taken out. They're little tiny rollers like that and they've got springs in behind those. So, yeah, it can then start once it detects that,

**Dave Jones:** bang, it just starts pulling it through. And at first glance, this looks just to be an optical solution, really. I mean, we've got some LEDs in here and uh basically three by the looks of it. Actually not sure

**Dave Jones:** what's under there. Not sure what that top part there is. I don't know, but yeah, they seem to match up with the sensors. I will have to get this board out in here, of course, but they seem to match up with the sensors on the

**Dave Jones:** other side, which makes sense, of course, because they're going to be uh shining uh various uh wavelengths of light, either visible or um uh UV or infrared or a combination of all uh three with the different LEDs through the notes to actually detect

**Dave Jones:** things as it goes in, but nothing hugely complicated there at all. I actually don't see a magnetic uh detector at first glance. Anyway, let's take the board out. There you go. That's the top side of the board and uh

**Dave Jones:** it looks like it is just an optical solution, as I said, because look, we've got a uh LED here, of course, which is um you know, I don't know, that be the IR one. I'm not sure, but we've got an

**Dave Jones:** interesting angled like you know, photo transistor or some sensor down in there and it's on like a 45 degree angle, which is rather interesting. It'll be interesting to see if that's matched on the top side and why it's actually angled like that. Then

**Dave Jones:** we've got two extra LEDs in here. Once again, they will probably be matching on the other side with photo transistors over there to actually detect that. So yeah, really, I don't see any magnetic unless it's on the top

**Dave Jones:** side board. On the bottom side board here, I don't see any magnetic detection at all. And as far as the chips go, we've got an LM336 2.5 volt voltage reference there and just a couple of dual op-amps LMC6062

**Dave Jones:** and LMC 662. So really, not much doing at all. Couple of transistors there presumably for driving the LEDs at quite a high brightness, I'm assuming. Apart from that, that's it. And that plate on the top side there, I

**Dave Jones:** maybe had a thought that maybe it's some sort of filter or something, but I don't know. I think it's just likely just masking out the extraneous light perhaps. Now I've got the top sensor assembly here and that of

**Dave Jones:** course just fits in place over there like that and it the note just goes between the two slots there and then just pops up. Looks like we've got some other LEDs slash sensors there. Yeah, there we go. There we go. There's a couple of

**Dave Jones:** No, they're just Oh, it's it's a light pipe. Okay, that looks like it just might be a light pipe cuz this has no circuitry going. I don't know. Is there circuitry going up to that? No, that just looks like See, there's no wires I

**Dave Jones:** mean sorry. So, that just looks like a light pipe feeding in from there and coming back out there. So, the board the top sensor board is in here and yep, probably got an LED and a photo transistor on the other side and then

**Dave Jones:** just detecting that the bill has actually made it through there. I don't think that's part of the validation of the note at all. But anyway, if we flip that open we can see that they're essentially duplicates. Oh, no. There we go. One

**Dave Jones:** side they aren't lined up. There we go. So, they're they're different alignments there. So, two different combination of LED and then sensor. So, that's why they've put that in to mask out the light from one side to the from

**Dave Jones:** one side to the other. So, there's two paths there that they're trying to read. There's one one path lined up with the note there and one from the other. And we probably saw that that's probably the internal strip. Um perhaps lined up with the uh

**Dave Jones:** lined up with the text on the internal strip. I don't know. Um but it looks like exactly the same array with the LED and the sensor and two other LEDs on the sides. They look like LEDs and those

**Dave Jones:** down there, if we can see it, look like the two matching photo transistors as I said, yeah. So, we're getting looks so looks like there's four optical detection path four optical detection points. This one here, this one over

**Dave Jones:** here which just goes straight through the note and then two separate paths across the note there. So, I don't know. You know, feed that sucker in there. Feed old Lincoln in and uh what do they line up with? I don't know.

**Dave Jones:** Not much. Your guess is as good as mine exactly what they're actually what points of the note that they're actually detecting along the path there. There's a good look down into that photo diode there and that is one big ass

**Dave Jones:** sensor die on that, that's for sure with a uh nice clear window over the front. It could even be uh uh you know, filtered in some way. Who knows, but uh yeah, I mean, is that a UV or is it an

**Dave Jones:** IR one? I'm not uh entirely sure, but they're obviously quite serious more serious with that one than just these smaller ones. There's a smaller photo diodes down there. That does look like it's got some sort of uh maybe some sort of filter lens there

**Dave Jones:** perhaps. I'm not sure, but uh it certainly is different. I mean, this one is much much clearer and you can just see the gold inside there. This one does look like it's or maybe it isn't. Maybe it's the same. Maybe it is clear and it's

**Dave Jones:** just an optical illusion really that it looks like there's that coating is a different color. It could just be completely clear. Uh sorry, I completely forgot these two extra leads over there and there. So, they've got a couple of So, they've got two

**Dave Jones:** extra points there. So, sorry, 1 2 3 4 and then 5 and 6 separate optical detection points. There we go. There's a much better view. There we go. We've got our metal can sensors here and then we've got our three

**Dave Jones:** diodes here and those ones those little suckers, um yeah, they're uh most likely uh based on the color, of course, the UV um sensors there and these are the um I I you know, they could be infrared or

**Dave Jones:** whatever. I don't exactly know. We have ourselves a part number there, folks, SLD-67HF2, 1902. Brilliant. To Google and sure enough, that's a Siliconix uh photodiode. Found the data sheet real easy. I'll link it in down below. Uh a spectrum range of 400 to 1,100 nm,

**Dave Jones:** which puts it uh covers basically all of the entire visible spectrum plus the infrared up at the higher part. Doesn't do ultraviolet. So, clearly, um these two inner uh sensors here, so this will be an infrared uh LED, of course, and uh

**Dave Jones:** infrared photodiodes. But, unfortunately, the part number is going to escape us on that, but just by the color of that and the fact that I know that uh you know, these note validators uh do often do infrared and um

**Dave Jones:** ultraviolet uh UV stuff as well, then um that's clearly, you know, almost certainly UV. And there's our upper sensor board. Once again, practically identical except with uh matching sensors. So, on this one, we've got our infrared diode, our

**Dave Jones:** infrared photodiode, and which the other one sort of uh goes about here on the other side of the board, so that gets those two strips in there and then uh we've got ourselves our um uh phototransistor over here and over

**Dave Jones:** here, which uh made up with the uh LED on the other side on the other board, and then likewise, these two LEDs here match up with the photodiodes on the other board. So, it looks like we uh could have three wavelengths

**Dave Jones:** operating here, uh UV. This is uh most likely the UV sensitive uh photo transistor there and it's it's definitely like it's a photo transistor arrangement you call it cuz it's actually got the Q designated down there instead of the D designated. By the way,

**Dave Jones:** that's why, you know, this one is actually a photo diode so they have actually called it D down on the designated there. These ones are likely infrared but they could be, you know, I I I don't know. You know, you would

**Dave Jones:** have to know what that particular LED here is cuz these are quite broad range. They can do anything from visible, as I said, up to the infrared range, no problems whatsoever. So, but likely two infrared ones in the center there, maybe some

**Dave Jones:** visible stuff happening over here, I'm not sure, but you know, it could be other wavelengths. I'm not entirely sure, but these are almost certainly UV and well, Bob's your uncle. That's it. Um as I said, there are a couple of

**Dave Jones:** LEDs on the back here, but they I'm pretty sure they're just uh uh actually detecting that the note's actually gone through and not the fact that it because that's that's a position. And if we go back to our first board here, we can see

**Dave Jones:** the edge detecting. This is obviously our first edge and then on our top side board, we've got our second edge detection with uh this diode and that light pipe just uh feeding back over there as I said before. That just

**Dave Jones:** detects that the note of the second edge so it knows how far the note's gone through. As soon as it hits that point, it knows the timing to turn on the LEDs and read the data back at a specific

**Dave Jones:** point as the note goes through cuz you wouldn't do it over the whole strip. You'd only do it at a at a specific point on the note which has that particular uh security feature that they're trying to read. So, actually I'm

**Dave Jones:** a bit disappointed that that's all we found, really. I mean, basically we've got um six different uh detection points they're using, you know, at most three different uh wavelengths of light. There's no magnetic stuff happening there. There's no width detection by the

**Dave Jones:** way of the note or anything like that at all. So, yeah, this is a pretty rudimentary bill acceptor. And of course, people are going to ask, "Well, how easy is it to, you know, fool these sort of things?"

**Dave Jones:** Well, I'm not entirely sure. You know, you'd have to do a lot of test, but considering that, you know, no magnetic sensors, just you know, some optical stuff. I don't know. Maybe it you know, if you really got down to it, you could possibly

**Dave Jones:** try and fool these things perhaps. But by the time you went to that effort, jeez, I don't know. To get, you know, a 20 buck thing out of a vending machine, jeez, not worth the effort. And I won't

**Dave Jones:** bother taking that apart. There's nothing in there. I mean, there's two motors. That's what our two wires hanging out there for. That's, you know, nothing special whatsoever. It's got that optical encoding feedback positional wheel, as I said. But that's about all

**Dave Jones:** she wrote. So, there you go. I hope you liked that. That's what's inside a pretty rudimentary I mean, a more modern one, a more advanced one is going to use lots more advanced technology in this one. I mean, there's

**Dave Jones:** no image matching, there's no camera, there's no, you know, nothing like that which you might possibly get in a more modern one. But you know, it does the job. Maybe it's just for a simple vending machine that just reads some six

**Dave Jones:** points at various light spectrums. And well, that's all there is to it. So, there you go. If you want to discuss it and if you got any more info on exactly, you know, might what might be going on

**Dave Jones:** in the various US bills cuz I don't know US currency, that stupid funny cotton funny money stuff. I don't know about that. But anyway, if you got any more for on exactly what's going on here, please let us know. It could be interesting to

**Dave Jones:** you know, power this thing up and get the timing and figure out what the wavelengths these LEDs are actually working at and stuff like that. Maybe I could do that in a second video. We'll see. Anyway, if you like teardown

**Dave Jones:** Tuesday, please give it a big thumbs up and if you want to discuss it, the EVblog forum link down below is the place to do it. That's down below on YouTube, down there. Or if you're watching the embedded version on

**Dave Jones:** EVblog.com, then the links are going to be up the top there. But because you're looking at the blog website, you already know that. So, I'm wasting my time. Catch you next time. I still can't get over the layout of

**Dave Jones:** this power supply. It's awful.
