---
video_id: qOzP5Vl-CIk
title: EEVblog #525 - Bank Note Acceptor Teardown
url: https://www.youtube.com/watch?v=qOzP5Vl-CIk
source: youtube-asr
timestamps: {"0": 2, "1": 29, "2": 42, "3": 62, "4": 75, "5": 97, "6": 119, "7": 133, "8": 156, "9": 180, "10": 192, "11": 218, "12": 228, "13": 243, "14": 258, "15": 270, "16": 285, "17": 301, "18": 311, "19": 322, "20": 332, "21": 340, "22": 352, "23": 362, "24": 371, "25": 385, "26": 396, "27": 407, "28": 416, "29": 425, "30": 440, "31": 457, "32": 465, "33": 478, "34": 491, "35": 505, "36": 518, "37": 531, "38": 548, "39": 561, "40": 579, "41": 589, "42": 612, "43": 627, "44": 643, "45": 657, "46": 679, "47": 689, "48": 701, "49": 713, "50": 724, "51": 737, "52": 751, "53": 763, "54": 787, "55": 803, "56": 814, "57": 825, "58": 847, "59": 861, "60": 876, "61": 888, "62": 907, "63": 918, "64": 936, "65": 953, "66": 968, "67": 990, "68": 1001, "69": 1012, "70": 1030, "71": 1040, "72": 1058, "73": 1069, "74": 1083, "75": 1092, "76": 1106, "77": 1119, "78": 1130, "79": 1144, "80": 1159, "81": 1174, "82": 1189, "83": 1203, "84": 1215, "85": 1230, "86": 1239, "87": 1256, "88": 1271, "89": 1280, "90": 1290, "91": 1300, "92": 1311, "93": 1330, "94": 1340, "95": 1353, "96": 1366, "97": 1379, "98": 1391, "99": 1412, "100": 1425, "101": 1436, "102": 1461, "103": 1472, "104": 1499, "105": 1512, "106": 1528, "107": 1552, "108": 1574, "109": 1591, "110": 1604, "111": 1618, "112": 1637, "113": 1652, "114": 1672, "115": 1685, "116": 1701, "117": 1716, "118": 1731, "119": 1744, "120": 1757, "121": 1778, "122": 1792, "123": 1802, "124": 1818, "125": 1829, "126": 1854, "127": 1871, "128": 1882, "129": 1913, "130": 1939, "131": 1950, "132": 1968, "133": 1980, "134": 1992, "135": 2007, "136": 2020, "137": 2035, "138": 2053, "139": 2063, "140": 2081, "141": 2093, "142": 2102, "143": 2112, "144": 2124, "145": 2135, "146": 2146, "147": 2158, "148": 2168, "149": 2180, "150": 2199, "151": 2212, "152": 2226}
---

**Dave Jones:** Hi, welcome to teardown Tuesday. Why do I have a Yankee five buck note here? One of these funny money cotton based crappy notes. In God we trust. Well, it's a good question because we have for today's teardown one of these note validators or bill validators or bill acceptors or note acceptors, whatever you want to call them.

**Dave Jones:** The ones that you typically find in vending machines and things like that that accept your bill. You feed your hard earned money in there and it either accepts or rejects it and detects whether the currency is legal.

**Dave Jones:** So I thought we'd uh teardown one of these. Could be a rather interesting. This one is a money controls. They're one of the probably not one of they're not one of the major manufacturers of these things but they are one of the reputable reputable manufacturers anyway of these bill acceptors, bill validators.

**Dave Jones:** And this is the MC 2600 model that we've actually got here. And there's a lot of art and science which goes into detecting whether or not a note is genuine or not.

**Dave Jones:** And it's going to vary between runs of notes over time. They do actually change things and different currencies as well. I mean this silly US cotton based funny money is just you know crap compared to like in terms of security compared to a Australian designed technology designed in Australia by the way.

**Dave Jones:** These are polymer bank notes we've got in Australia. I mean we basically don't have a counterfeiting problem here in Australia because we use these very secure polymer notes. But sort of actually detecting notes like this going to use different technologies or can use different technologies to this simple US currency or is it that simple?

**Dave Jones:** Well, they've got as you might know, they've got hidden watermarks in there. They've got security strips in there which are fluoresce it different colors I believe under UV lights and you can tell the bills apart that way.

**Dave Jones:** They use magnetic inks of course and even some of the watermarks with the magnetic inks they can resonate at different you know, resonate a a a detector circuit at different frequencies based on what type of note it is cuz not only do you have to determine whether or not it's a genuine or fake note, but you have to determine or the unit has to determine the currency of the bill as well.

**Dave Jones:** Is it a $1, a $5, a $10, a $20, you know, whatever. So as we'll see as various technologies that goes into this and you can easily see this for example, if you just really light up these notes from behind, it's it's not hard to actually see Here we go.

**Dave Jones:** There's a hidden five in there for example, you see that big five in there which isn't of course on the reverse side there. So that's you know, there's an inbuilt watermark right there and of course there's the strip.

**Dave Jones:** You can see that. I'll zoom in. You can't see it on the note. It's basically right down there, but if we shine that from behind, you can see it's got USA five on it and that security strip goes all the way down there and I believe I don't quote me on this, but that fluoresces under a different color under UV light and they can use infrared detectors and all sorts of

**Dave Jones:** other detection mechanisms to to detect whether or not these bills are genuine. See there's five going down there. You can see the see the watermark in there. So 555 plus the security strip.

**Dave Jones:** That's a at least an absolute minimum that they've got going in these US $5 notes. And as I said, they do change things up occasionally. So, these bill validators occasionally have to be updated with new firmware.

**Dave Jones:** You know, they may not accept the new 2013 $5 bill, for example. So, you got to go out and update the firmware for this sucker. But, yeah. So, something like this note validator here is going to use various technologies.

**Dave Jones:** So, I'd expect and dimensions of bills, for example. They're probably going to, you know, make sure it's the exact size and things like that as as a minimum. So, really we expect to find quite a few sensors in here.

**Dave Jones:** And as you can see, they've obviously there's like one main control board in the back here. It's got various notes. We'll take a look at that. But, it's got like a sensor module down the bottom of here underneath the or in as part of the slot.

**Dave Jones:** And then they've got a cable running over there to the main board like that. And this money controls a unit basic dip switch interface. And then the vendor, you know, the person who owns the vending machine can just, you know, set it to accept various notes.

**Dave Jones:** It's designed to accept 1, 5, 10, and $20 notes. No higher. And yes, it is a used unit. I don't know if it actually works or not. It's obviously been pulled out of a unit.

**Dave Jones:** But, anyway, you can enable and disable the various currencies. And then this is a very simple pulsed interface one. It has, as we'll see on the other side, does have other interfaces as well.

**Dave Jones:** But, basically it can just give out one or four pulses per dollar. So, that's how other circuitry in the machine can actually detect things. So, you put your note in there.

**Dave Jones:** Doesn't give change or anything like that. It just accepts the note and either puts it in the cash box in the back, which we'll take a look at, or just throws it back out.

**Dave Jones:** And it actually came with the cable to hook up to it. And it just plugs in here. I mean, it does have a serial interfaces. There you go, and it's got a download diagnostics as well.

**Dave Jones:** You can For this particular brand, you can buy a diagnostic box which hooks up to the PC and you know, allows you to extract data out of it or change it or maybe even update the firmware remotely.

**Dave Jones:** I'm not entirely sure about that, but this one can be a simple This one's a 120 V AC model. You can get ones based on a 12 V DC and stuff like that.

**Dave Jones:** So, that just plugs in there and all we've got is basically 120 V AC in and just a relay contact out or a you know, a pulsed contact out which gives the number of pulses based on the bill and whether or not it's accepted it.

**Dave Jones:** That's it. So, incredibly simple interface. Just four wires plus ground. So, obviously the bill goes in the front there. There's a sensor board in there which actually detects all the stuff.

**Dave Jones:** There's a processor board in the back and then this big thing looks all complicated, but it's not. It's very simple. You just release that clip and this is the money box.

**Dave Jones:** There it is. That just It's got a couple of springs in there and that just fills up with money. Obviously, I'm not sure how many actual bills you can fit in there.

**Dave Jones:** I don't know. I don't know. What's the average thickness of a bill? No idea, but you know, you might get 500 or bills or something like that in there.

**Dave Jones:** So, I'm not sure how that would how long that would last in a typical scenario, but there you go. There's the diagnostic stuff for and yeah. And basically, they've just got some belt and pulleys which then suck the note through here.

**Dave Jones:** I'm not entirely sure exactly how I assume this one if it rejects it will spit the note back out. So, maybe it only comes partial part of the way in cuz it's not like the note sort of pops out the back here and then either gets directed into there or spat back out.

**Dave Jones:** So, it probably comes like halfway in, detects if it It detect that it's a valid bill, it just reverses the motors and whoop, shoots it back out the front.

**Dave Jones:** But yeah, that's all there is to it. Um mechanically, um you know, pretty simple. And if we take those four screws off the front, bit of a dust Yeah, bit of dust in there.

**Dave Jones:** Smells, but uh we're in and we have our first look at the main board there. That's the bottom of the main board. They've got uh very nicely aligned SMD resistors there.

**Dave Jones:** I rather like that. They've got a flat flex cable going into It looks like they've got a top sensor board and there the status LEDs there. They I didn't see that, but they obviously uh poke through the front and that's what we had on the back here.

**Dave Jones:** That's what they had on the unit, the uh back of the unit here, the uh diagnostics. Maybe I should actually power this thing up before I uh take it apart, just in case I goof up some of the mechanicals or something like that.

**Dave Jones:** I think I might give it a go. Okay, I think I've got the pin outs correct. This is of course a US 120 volts AC 60 hertz. So I'm using my um uh variable frequency converter here to uh generate just that.

**Dave Jones:** I've got the ground wire hooked up as well. So hopefully the magic smoke and no smoke doesn't escape. Let's give it a go. Oh. That sounded good. All the motors went, so let's whack in our funny money.

**Dave Jones:** I don't know which way up. Uh there we go. It gives you a photo of the head, I guess. There we go. Let's Let's give it a go. Give it a bill.

**Dave Jones:** Hello. It's not detecting. It's not detecting my note. No. No. Uh fail. Oh, there we go. We had something. There we go. No. So, it's obviously it's just rejected that straight away.

**Dave Jones:** No, there we go. Ah, what I did there is flicked a dip switch on the side here which just changed it from the pulse from vendor serial to pulse protocol.

**Dave Jones:** So, maybe, you know, that's what was going on there, but it doesn't like my $5 note as all at all. I've got two of them. So, I'll try another one and uh No, it does not like that in the least.

**Dave Jones:** No. I'm pretty sure the note has to be up there. I mean, you know, Yanks are probably laughing at me because uh our our ones here pretty much accept the bills basically in, you know, any um any orientation at all.

**Dave Jones:** But, yeah, that's not No, it's just rejecting my $5 note. Unbelievable, but it I don't know. Is this a new note? I don't know. When was it manufactured? You know, you'd have to know like it does this support the latest firmware for this $5 bill.

**Dave Jones:** I've got $5 enabled on the dip switch on the side, but yep, it's not accepting. Bummer. So, it'll have to be properly vertical. Is there something going on there?

**Dave Jones:** No. Sometimes it doesn't go in all the way at all. No. No. Loser. It's kind of doing the business, but it's not accepting my note. Bummer. Let's just have a look at the back of that when we shoot that bill in, shall we, and see what uh Yeah, as I as I thought, yeah, it goes like partial way in and then so it doesn't feed it all the way in.

**Dave Jones:** Only when it accepts it and it gets to that point, it processes it accepts it, will it uh feed up the whole way and then uh put it in the um the little storage container.

**Dave Jones:** And popped off that top cover there. Easy. We've got some uh cutouts in the board here for three large caps there. And of course, there are obviously a bit of a premium on space there.

**Dave Jones:** So, and there's not much of circuitry on the board. So, they've decided to make some cutouts there. It's not you know, not uncommon for space sensitive applications to do something like that.

**Dave Jones:** But, let's get the rest of this board out and we'll take out these ribbon cables here. And see what's on the top side. So, we'll lever that out and it looks like they were held in with clips.

**Dave Jones:** So, this board should just pop out. Too easy. There's one more cable. Oh, a Lattice semiconductor part. We're going to have a good look in here. But, check that out.

**Dave Jones:** Interesting. It's a rather interesting board. You know, there's quite a bit of logic going on happening over here. There's a Lattice PLD over here. There's a 68 uh 100 processor which we'll take a look at.

**Dave Jones:** There's the prom obviously for the thing and basically we're in sandwich sort of in the middle here is the mains switch mode power supply. Obviously, there's our switch mode transformer there.

**Dave Jones:** There's our high voltage caps 200 V a pop. And yeah, I mean you know, input fuse there and we've got some protection. And but we've got I mean obviously, you know, not a huge um sort of thought given to differentiating or isolating these sort of you know, the low voltage stuff from the mains side here.

**Dave Jones:** So, I mean there's you know, the dip switch sort of right next to the main input filter caps. You know, you got to it's crazy. Anyway, we've got some regulators, you know, some low voltage regulators, low side regulators around here.

**Dave Jones:** Maybe they're like some little optocouplers or something like that for the digital out. I mean, here's our mains input here. So, it's popping in here. So, yeah, just looks a bit real, you know, it's a just messy business.

**Dave Jones:** I sort of, you know, not huge amount of thought has gone into that. Sort of, you know, hack and slash kind of design, I think. Anyway, we've got ourselves a couple of optical detectors here.

**Dave Jones:** This one here is for an optical encoder wheel down there, if you can see that properly. So, that obviously turns around with the motor just to ensure, I guess, that a bit of feedback to ensure that yeah, the motor has actually turned and the thing, you know, maybe for slipped bills or or something like that, perhaps.

**Dave Jones:** Some some sort of detection. Another one here which you know, mates up with uh this over here which I'm not sure. That just looks I'm not sure how that moves at all.

**Dave Jones:** That little plastic is just like a plastic tab. So, I'm not quite sure what that one's doing there. Maybe some sort of, you know, this thing's going to have maybe, you know, a little bit of anti-tamper stuff in it as well, but I really know what that's doing.

**Dave Jones:** I mean, whew, strange. What does it detect that this whole mechanism has popped out of the bottom? I don't know. Hmm, you know, that firmware sticker might explain why possibly it didn't accept my note.

**Dave Jones:** One of the reasons, um look, it's dated 2002. So, 11 years old unless you know, unless the sticker's old and it's uh reflashable or something. Let's have a poke under here and actually have a look.

**Dave Jones:** Yeah, that's really crusty. Looks like it's been on there for 10 years or more, that's for sure. Let's have a look at what we've got. There you go, it's an AM29F002.

**Dave Jones:** So, it's a 2 megabit uh from the parallel flash. Um prom. So, yeah, it's it is reflashable, but I doubt it has the internal ability to reflash remotely. I'm going to probably have to take it out, whack it in your programmer, and do it that way.

**Dave Jones:** Now, to understand whether or not that flash chip contains the actual firmware for the processor or maybe contains, you know, the in all the data and the images and all sorts of other stuff for the various nodes and things like that.

**Dave Jones:** All the data. Seems a bit big for that. Anyway, to figure that out, we need to take a look at the exact type of processor here. And they've got a Motorola now Freescale, of course, MC classic MC68HC11.

**Dave Jones:** But, of course, the 68HC11 comes in endless varieties. Some contain internal prom, some don't. E-squared prom, this, that. They come in a million different types. Well, this is actually the F series chip, and you can't confuse it with other series like the E series, different again.

**Dave Jones:** And so, you've got to look at the F1 and then the CPU 5 after that. So, we need to go into the data sheet and have a look at the specific type type of chip to see whether or not it contains an internal ROM or not.

**Dave Jones:** And I checked the data sheet, which I will link in down below for this thing. If you want to follow along at home, no, this one does not contain an internal ROM.

**Dave Jones:** Although, it's got an internal E-squared prom, only 512 bytes. It's got like 1K of SRAM, not a particularly powerful processor at all. It does have a built-in 8-bit multi-channel ADC, though, which they're probably using for some probably using for two measure some of the sensor stuff.

**Dave Jones:** So, we'll have to check the other chips to see if there's an external one there. But, yeah, they're possibly using that. So, obviously, this is the firmware for all of that.

**Dave Jones:** And I was going to say that, you know, because we've got a Lattice um uh PLD over here, maybe they could have interfaced the memory through that to sort of, you know, externally program it and then sort of, you know, route it through to the CPU here.

**Dave Jones:** But by the looks of that, no, it's just going it's just going direct. I can't see anything on the back there, but anyway, internal layers there. But that's no, it's running straight over.

**Dave Jones:** So, I think to reprogram that sucker, we need to uh you know, you need to pull it out or the uh service tech comes along, pulls it out, reflashes the chip, and then uh updates it for the the latest currency.

**Dave Jones:** So, most likely, yes, this contains, unless they didn't change the sticker, contains the firmware from 2002. So, any notes after that, if they have changed, this thing likely won't accept them.

**Dave Jones:** And the PLD here is an old Lattice uh Mark 4 PLD, only 64 macrocells. You know, it's pretty tiny, not much doing there. But uh obviously, they need it for some sort of uh glue logic in there.

**Dave Jones:** Not sure what. And we've got ourselves an ISSI uh external SRAM there. In this case, uh 32K * 8, big whopping uh SRAM cuz this thing doesn't have much, as I said, like 1K.

**Dave Jones:** So, obviously, they're using the PLD as some sort of glue logic to uh maybe uh you know, get that into the processor. Although, should be able to just uh whack that straight on the bus.

**Dave Jones:** From the mains power supply, we've got ourselves a power integration uh top switch device, a top 247R, and that's just a uh flyback controller. There's our flyback transformer down there, and uh you know, nothing special going on the uh main side of things there.

**Dave Jones:** Just got a fuse on the input there, common mode choke, our bridge rectifier is uh four separate diodes underneath there, our filter caps, and then our main flyback controller, and Bob's your uncle.

**Dave Jones:** And there's our feedback optocoupler hidden under there. And as I said, just very messy layout. I mean, I don't like it at all. Look at it. It's not over near here, near the photo interrupter, and it's just Ah, it's it's terrible.

**Dave Jones:** Awful layout. And the only other thing of note on here is this uh Texas TLV5629, and that's an 8-bit uh DAC. Probably not a huge surprise to find that on there.

**Dave Jones:** So, they're using the DAC to drive some sensor stuff, probably, and the built-in ADC, as I said, in the HC11 over there, reading that back. But whole bunch of transistors, not sure what's going on there.

**Dave Jones:** Maybe that's a part of all the sensors. And what's that little sucker? No idea. Uh looks like a 74HC14 We've got you know, it's part of the secondary power supply here.

**Dave Jones:** There's an LM324, by the looks of it. And And this AE2595 is just an 8-channel open collector driver, like it just like the classic ULN2803, for example. But you know, here it is, over here.

**Dave Jones:** It's obviously driving the output pins, but where are they? I mean, they're all the way all the output connectors all the way over on this side of the board.

**Dave Jones:** Crazy. And same with the MAX232 driver. I mean, where's the connector? Over here somewhere. And actually, just with the layout of the board, I just noticed something. The You can see, you know, it's a multi-layer board.

**Dave Jones:** You can see the internal, the darker green in there. You can see that's flood filled all the way through, even all over this mains section here, complete ground plane right around the whole blinking lot.

**Dave Jones:** And that's also, you can actually see that um a similar thing happening on the top. I can't get a good light angle on that, but you can see it definitely happening here.

**Dave Jones:** And here's the mains input here. Right? This connector here. Here is the two mains input, right? You know, active and neutral. There it is. There's the ground input, of course.

**Dave Jones:** The ground input is actually connected through to the ground plane on the bottom and they cut this trace running over here. And that's all connected. So, the ground is connected through.

**Dave Jones:** And of course, this is a flyback uh mains uh power supply. So, the outputs are going to be isolated from the mains. But look at the clearance. Look, just around the pad there.

**Dave Jones:** Are you [ __ ] me? Like the person that laid out this obviously has no clue about the I meeting any standard, I guess. And cuz I don't think I think it's unlikely to and um you know, be just how to layout boards for clearance.

**Dave Jones:** I mean, it's just an absolute mess. And to have one solid ground fill all the way with just that little piss-ant amount of clearance in there. What is that, you know?

**Dave Jones:** A couple of millimeters? You got to be [ __ ] me. All right. Well, enough of the PCB cuz there's nothing really special on there. It's a processor with a DAC and an ADC and maybe a bit of analoggy stuff and that's about it.

**Dave Jones:** So, let's uh see if we can get into this um sensor part. I think that there might be a uh top and a bottom board there. You can just actually remove the entire sensor thing like that.

**Dave Jones:** And uh whoop whoop whoop, lost some pulleys and things. Oops. Oops. Yeah, I did take out a few screws and well, I'm a few screws loose. And sure enough, there are two uh sensor boards in this thing.

**Dave Jones:** This is the bottom sensor board and uh nothing special on the backside there. It's just a double-sided board and uh it looks like there's no huge amount of circuitry in there, but we've got a couple of uh LEDs and things.

**Dave Jones:** We've got our um edge to our uh note edge detection here. So, you know, clearly there we've got a LED here and a phototransistor over here. So, as soon as you put the bill in, it uh interrupts that and it knows to uh uh then uh feed that through with the various uh rollers on the uh top and bottom side here.

**Dave Jones:** Here's the front rollers, which I've actually taken out. They're little tiny rollers like that and they've got springs in behind those. So, yeah, it can then start once it detects that, bang, it just starts pulling it through.

**Dave Jones:** And at first glance, this looks just to be an optical solution, really. I mean, we've got some LEDs in here and uh basically three by the looks of it.

**Dave Jones:** Actually not sure what's under there. Not sure what that top part there is. I don't know, but yeah, they seem to match up with the sensors. I will have to get this board out in here, of course, but they seem to match up with the sensors on the other side, which makes sense, of course, because they're going to be uh shining uh various uh wavelengths of light, either visible or um

**Dave Jones:** uh UV or infrared or a combination of all uh three with the different LEDs through the notes to actually detect things as it goes in, but nothing hugely complicated there at all.

**Dave Jones:** I actually don't see a magnetic uh detector at first glance. Anyway, let's take the board out. There you go. That's the top side of the board and uh it looks like it is just an optical solution, as I said, because look, we've got a uh LED here, of course, which is um you know, I don't know, that be the IR one.

**Dave Jones:** I'm not sure, but we've got an interesting angled like you know, photo transistor or some sensor down in there and it's on like a 45 degree angle, which is rather interesting.

**Dave Jones:** It'll be interesting to see if that's matched on the top side and why it's actually angled like that. Then we've got two extra LEDs in here. Once again, they will probably be matching on the other side with photo transistors over there to actually detect that.

**Dave Jones:** So yeah, really, I don't see any magnetic unless it's on the top side board. On the bottom side board here, I don't see any magnetic detection at all. And as far as the chips go, we've got an LM336 2.5 volt voltage reference there and just a couple of dual op-amps LMC6062 and LMC 662.

**Dave Jones:** So really, not much doing at all. Couple of transistors there presumably for driving the LEDs at quite a high brightness, I'm assuming. Apart from that, that's it. And that plate on the top side there, I maybe had a thought that maybe it's some sort of filter or something, but I don't know.

**Dave Jones:** I think it's just likely just masking out the extraneous light perhaps. Now I've got the top sensor assembly here and that of course just fits in place over there like that and it the note just goes between the two slots there and then just pops up.

**Dave Jones:** Looks like we've got some other LEDs slash sensors there. Yeah, there we go. There we go. There's a couple of No, they're just Oh, it's it's a light pipe.

**Dave Jones:** Okay, that looks like it just might be a light pipe cuz this has no circuitry going. I don't know. Is there circuitry going up to that? No, that just looks like See, there's no wires I mean sorry.

**Dave Jones:** So, that just looks like a light pipe feeding in from there and coming back out there. So, the board the top sensor board is in here and yep, probably got an LED and a photo transistor on the other side and then just detecting that the bill has actually made it through there.

**Dave Jones:** I don't think that's part of the validation of the note at all. But anyway, if we flip that open we can see that they're essentially duplicates. Oh, no. There we go.

**Dave Jones:** One side they aren't lined up. There we go. So, they're they're different alignments there. So, two different combination of LED and then sensor. So, that's why they've put that in to mask out the light from one side to the from one side to the other.

**Dave Jones:** So, there's two paths there that they're trying to read. There's one one path lined up with the note there and one from the other. And we probably saw that that's probably the internal strip.

**Dave Jones:** Um perhaps lined up with the uh lined up with the text on the internal strip. I don't know. Um but it looks like exactly the same array with the LED and the sensor and two other LEDs on the sides.

**Dave Jones:** They look like LEDs and those down there, if we can see it, look like the two matching photo transistors as I said, yeah. So, we're getting looks so looks like there's four optical detection path four optical detection points.

**Dave Jones:** This one here, this one over here which just goes straight through the note and then two separate paths across the note there. So, I don't know. You know, feed that sucker in there.

**Dave Jones:** Feed old Lincoln in and uh what do they line up with? I don't know. Not much. Your guess is as good as mine exactly what they're actually what points of the note that they're actually detecting along the path there.

**Dave Jones:** There's a good look down into that photo diode there and that is one big ass sensor die on that, that's for sure with a uh nice clear window over the front.

**Dave Jones:** It could even be uh uh you know, filtered in some way. Who knows, but uh yeah, I mean, is that a UV or is it an IR one? I'm not uh entirely sure, but they're obviously quite serious more serious with that one than just these smaller ones.

**Dave Jones:** There's a smaller photo diodes down there. That does look like it's got some sort of uh maybe some sort of filter lens there perhaps. I'm not sure, but uh it certainly is different.

**Dave Jones:** I mean, this one is much much clearer and you can just see the gold inside there. This one does look like it's or maybe it isn't. Maybe it's the same.

**Dave Jones:** Maybe it is clear and it's just an optical illusion really that it looks like there's that coating is a different color. It could just be completely clear. Uh sorry, I completely forgot these two extra leads over there and there.

**Dave Jones:** So, they've got a couple of So, they've got two extra points there. So, sorry, 1 2 3 4 and then 5 and 6 separate optical detection points. There we go.

**Dave Jones:** There's a much better view. There we go. We've got our metal can sensors here and then we've got our three diodes here and those ones those little suckers, um yeah, they're uh most likely uh based on the color, of course, the UV um sensors there and these are the um I I you know, they could be infrared or whatever.

**Dave Jones:** I don't exactly know. We have ourselves a part number there, folks, SLD-67HF2, 1902. Brilliant. To Google and sure enough, that's a Siliconix uh photodiode. Found the data sheet real easy.

**Dave Jones:** I'll link it in down below. Uh a spectrum range of 400 to 1,100 nm, which puts it uh covers basically all of the entire visible spectrum plus the infrared up at the higher part.

**Dave Jones:** Doesn't do ultraviolet. So, clearly, um these two inner uh sensors here, so this will be an infrared uh LED, of course, and uh infrared photodiodes. But, unfortunately, the part number is going to escape us on that, but just by the color of that and the fact that I know that uh you know, these note validators uh do often do infrared and um ultraviolet uh UV stuff as well, then um that's

**Dave Jones:** clearly, you know, almost certainly UV. And there's our upper sensor board. Once again, practically identical except with uh matching sensors. So, on this one, we've got our infrared diode, our infrared photodiode, and which the other one sort of uh goes about here on the other side of the board, so that gets those two strips in there and then uh we've got ourselves our um uh phototransistor over here and over

**Dave Jones:** here, which uh made up with the uh LED on the other side on the other board, and then likewise, these two LEDs here match up with the photodiodes on the other board.

**Dave Jones:** So, it looks like we uh could have three wavelengths operating here, uh UV. This is uh most likely the UV sensitive uh photo transistor there and it's it's definitely like it's a photo transistor arrangement you call it cuz it's actually got the Q designated down there instead of the D designated.

**Dave Jones:** By the way, that's why, you know, this one is actually a photo diode so they have actually called it D down on the designated there. These ones are likely infrared but they could be, you know, I I I don't know.

**Dave Jones:** You know, you would have to know what that particular LED here is cuz these are quite broad range. They can do anything from visible, as I said, up to the infrared range, no problems whatsoever.

**Dave Jones:** So, but likely two infrared ones in the center there, maybe some visible stuff happening over here, I'm not sure, but you know, it could be other wavelengths. I'm not entirely sure, but these are almost certainly UV and well, Bob's your uncle.

**Dave Jones:** That's it. Um as I said, there are a couple of LEDs on the back here, but they I'm pretty sure they're just uh uh actually detecting that the note's actually gone through and not the fact that it because that's that's a position.

**Dave Jones:** And if we go back to our first board here, we can see the edge detecting. This is obviously our first edge and then on our top side board, we've got our second edge detection with uh this diode and that light pipe just uh feeding back over there as I said before.

**Dave Jones:** That just detects that the note of the second edge so it knows how far the note's gone through. As soon as it hits that point, it knows the timing to turn on the LEDs and read the data back at a specific point as the note goes through cuz you wouldn't do it over the whole strip.

**Dave Jones:** You'd only do it at a at a specific point on the note which has that particular uh security feature that they're trying to read. So, actually I'm a bit disappointed that that's all we found, really.

**Dave Jones:** I mean, basically we've got um six different uh detection points they're using, you know, at most three different uh wavelengths of light. There's no magnetic stuff happening there. There's no width detection by the way of the note or anything like that at all.

**Dave Jones:** So, yeah, this is a pretty rudimentary bill acceptor. And of course, people are going to ask, "Well, how easy is it to, you know, fool these sort of things?"

**Dave Jones:** Well, I'm not entirely sure. You know, you'd have to do a lot of test, but considering that, you know, no magnetic sensors, just you know, some optical stuff. I don't know.

**Dave Jones:** Maybe it you know, if you really got down to it, you could possibly try and fool these things perhaps. But by the time you went to that effort, jeez, I don't know.

**Dave Jones:** To get, you know, a 20 buck thing out of a vending machine, jeez, not worth the effort. And I won't bother taking that apart. There's nothing in there. I mean, there's two motors.

**Dave Jones:** That's what our two wires hanging out there for. That's, you know, nothing special whatsoever. It's got that optical encoding feedback positional wheel, as I said. But that's about all she wrote.

**Dave Jones:** So, there you go. I hope you liked that. That's what's inside a pretty rudimentary I mean, a more modern one, a more advanced one is going to use lots more advanced technology in this one.

**Dave Jones:** I mean, there's no image matching, there's no camera, there's no, you know, nothing like that which you might possibly get in a more modern one. But you know, it does the job.

**Dave Jones:** Maybe it's just for a simple vending machine that just reads some six points at various light spectrums. And well, that's all there is to it. So, there you go.

**Dave Jones:** If you want to discuss it and if you got any more info on exactly, you know, might what might be going on in the various US bills cuz I don't know US currency, that stupid funny cotton funny money stuff.

**Dave Jones:** I don't know about that. But anyway, if you got any more for on exactly what's going on here, please let us know. It could be interesting to you know, power this thing up and get the timing and figure out what the wavelengths these LEDs are actually working at and stuff like that.

**Dave Jones:** Maybe I could do that in a second video. We'll see. Anyway, if you like teardown Tuesday, please give it a big thumbs up and if you want to discuss it, the EVblog forum link down below is the place to do it.

**Dave Jones:** That's down below on YouTube, down there. Or if you're watching the embedded version on EVblog.com, then the links are going to be up the top there. But because you're looking at the blog website, you already know that.

**Dave Jones:** So, I'm wasting my time. Catch you next time. I still can't get over the layout of this power supply. It's awful.
