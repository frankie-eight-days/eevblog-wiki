---
video_id: SJZ3zetpNOI
title: EEVblog #955 - World's First Portable Computer Teardown
url: https://www.youtube.com/watch?v=SJZ3zetpNOI
source: youtube-asr
---

**Dave Jones:** Hi. Imagine it's only 1981 and you're a business person and you wanted one of these newfangled personal computers. What did you want? Well, well, you wanted something that was affordable, maybe something that's portable, definitely something that ran on the

**Dave Jones:** latest standards of the time, and definitely something that came with all the business software that you needed. Who delivered? Adam Osborne delivered and we've got one. This is the baby that you wanted, the Osborne 1. Wow, it doesn't get much more

**Dave Jones:** groundbreaking than this puppy. Ta-da! Look at this. It was an absolute revolution in its day, the Osborne 1. Let's check it out. People's jaws dropped when Adam Osborne released this thing in early 1981. It was basically the world's first portable computer or

**Dave Jones:** luggable computer, designed basically fit under an airline seat so that you could actually carry this thing on a plane. You're a business person, this was the ducks guts and it was released at the groundbreaking price of $1,795 US. What's that about four and a half or

**Dave Jones:** five grand in today's money? But, the thing with this is that it came with all the software. It came with WordStar, which was the word processor of choice back in the day. It came with a spreadsheet, SuperCalc, I think it

**Dave Jones:** was. It came with DBASE II. It ran the CPM operating system, which was the standard at the time. Remember, this is early 1981, the IBM PC didn't come out until late 1981. So, basically CPM was the standard. It wasn't only until a

**Dave Jones:** year or two later that DOS, PC-DOS, MS-DOS started to take over. So, this ran the standard operating system and it came at an incredible price. People joked that you basically got the computer for free because the software was worth about the same as the

**Dave Jones:** computer. Wow. But as far as actual computers go, it wasn't that great. It wasn't fast, it wasn't powerful. Standard Z80 processor working at a standard 4 MHz. Tiny 5-in monochrome screen on the thing. 52 by 24 characters, I think it was, which was

**Dave Jones:** software mapped into a larger 128 by 32 screen. Dual floppy drives in it, but they were only single-sided, 90K each. Couldn't That wasn't Even back then, that wasn't a lot of data to actually store on these things. And it basically

**Dave Jones:** wasn't really expandable. So, there was no modem built in or anything like that. So, basically, it was a pretty bare-bones CPM computer. But the fact is, it was at that price point, and you got all that software for free. So,

**Dave Jones:** businesses thought this was the greatest thing since sliced bread, and Adam Osborne thought, "Oh, we might sell 10,000 of these." They ended up selling 10,000 a month. And it was designed by the legendary Lee Felsenstein, who you might know as designer of the Sol

**Dave Jones:** computer, and also the original moderator of the Homebrew Computer Club. He's the one who ran the meetings and sort of organized them and kept all the nerds under control. So, an absolute classic computer, classic time, but it didn't last. Whilst this was a very

**Dave Jones:** successful computer, the ultimate failure of the company not too many years later led the industry to coin the famous term the Osborne effect. And this is where Osborne basically released details, or rumors came about that they were developing

**Dave Jones:** this new computer. And what happened? Nobody bought this one. They held off purchasing, so all the computer stores were left with stock, unsold stock, and things like that. People were holding out for that new machine that coming out, and ultimately, that played a

**Dave Jones:** fairly large part in the ultimate bankruptcy of Osborne computers. So, the Osborne effect still a very popular term today to mean that if you mention your future product release details of it, then it can have an impact on the sales

**Dave Jones:** of your current product. So, just be aware many a company has come a cropper because of that. But, I know what you're saying. Dave, STOP YAPPING. WE WANT TO see inside this puppy. Well, yep, you know what we say here on the EV blog.

**Dave Jones:** Don't turn it on. Take it apart. One of the most remarkable things when I first got this and took it apart is just how big and clunky this keyboard is. I mean, why does it have to be this thick?

**Dave Jones:** I mean, I know it's got nice, you know, full travel. Well, actually not really full travel there. Anyway, um you know, it's got a real keyboard on it, but why it's got to be that that hugely thick um is is beyond me. I

**Dave Jones:** don't know. It's absolutely enormous, and it sort of adds to the size and the bulk of this thing. I mean, it is not really that big a computer, you know, like in terms of uh to fit an entire CPM

**Dave Jones:** computer in here with 5 and 1/4-in uh full two 5 and 1/4-in full height drives and and everything else. It's quite fine, but that keyboard just adds so much to it. Wow. So, if we have a look at the front here, we've got a standard

**Dave Jones:** 0.1-in header for the keyboard, and the keyboard's removable. That's a very nice touch with the ribbon cable. Not sure if they had any long-term issues with that, though. It turns out they did have issues with the reliability of the

**Dave Jones:** ribbon cable going across, as you'll see when I tear down the keyboard later, and they sort of changed it to this curly type with a right-angle attachment there in future revisions of the unit. And it looks very industrial with it you know

**Dave Jones:** the little pokey 5-in CRT screen here, the big huge 5 and 1/4-in full height floppies in here. I early '81, did they actually have half height 5 and 1/4-in discs available? I'm not entirely sure, but anyway they went

**Dave Jones:** with the full height ones and that's obviously the huge bulk of this product. They could have made it you know like like half that height if they actually used or almost, you know, if they used a compact 5 and 1/4-in move the screen

**Dave Jones:** down whatever redesign the board or whatever. You know, they could have made this thing a lot smaller, but anyway we have these two little cutouts here. Obviously they're designed for your discs so your 5 and 1/4-in floppy discs

**Dave Jones:** you'd all store them in there and then you'd whack them in there. It couldn't of course you had to put the disc in to boot up CPM. You know, it wasn't built into ROM or anything like that. We've got a modem

**Dave Jones:** port over here which is basically a serial port. It didn't have a building modem. You had to have an external one. Standard D25 serial RS232. Good old IEEE 488 the HPIB interface standard which you can use as a parallel port for

**Dave Jones:** driving printers. I think they had like a printer adapter and stuff. Of course the keyboard and brightness and contrast for the CRT. External video. I'm not sure if anyone actually used the external video, but they might have do not remove while

**Dave Jones:** power is on. Well, let's whip that out and that was a cartridge connector. Got a big fat reset button there. It's sort of not really recessed, but you know, I guess it'd be hard to hit that one accidentally. And there's

**Dave Jones:** an external 9-pin D connector here labeled bat and that must be for an external battery. I don't think I've ever heard of anyone using an external battery with this thing because it was mains power. Did not have a battery

**Dave Jones:** built in. So while it was portable, in {quote} marks, um yeah, it was not the world's first uh battery-powered portable computer. And we've also got uh external us uh a socket here, presumably for the external monitor, but like yeah,

**Dave Jones:** I don't know anyone who actually uh used an external monitor for with this thing. But anyway, there's the badge shot for you badge aficionados. Let's have a look at the back of this baby, and you'll find that there's not much at all. This

**Dave Jones:** one, the carry handle's gone all completely crusty and rusty. So, uh yeah, it probably had like a proper leather strap or uh something on there. And you've got mains input. That's it. This thing basically was not expandable. And for those playing along at home,

**Dave Jones:** serial number A 20,370. Given that uh they sold like uh 10 or 11,000 of these in the first month, I believe, um could this be a very early unit? Well, there's only one way to find out. Take it apart. So, this thing was actually

**Dave Jones:** designed uh to be fairly rugged and actually survive uh drops, I believe. But uh so, inside, we expect maybe to find some sort of uh cushioning support for the CRT, perhaps. Um anyway, we'll find out because there are, you know,

**Dave Jones:** many reports of this thing actually surviving all the rough handling, uh you know, taking on business trips and planes and and uh stuff like that. So, it was famously designed to fit under an airline seat, and I think that might

**Dave Jones:** have been one of uh Adam Osborne's first uh requirements to uh Lee Felsenstein was that, "Hey, I want this baby to fit under an airline seat. This is a business machine. Real business people, they take their They take their uh

**Dave Jones:** personal computers on the airplanes. And there's one thing you'll notice with the Osborne 1 is that it is actually fanless. There's some grills here on the front, but uh yeah, there is no fan in this thing. So, apart

**Dave Jones:** from the floppy drives, I'm silent operation, beauty. And of course, this isn't the original uh color of this thing. Um it was actually white, but it's a yellowed. This is a classic case of uh bromine, a fire retardant material

**Dave Jones:** in the ABS plastics of the day in these early uh computers. Very common for uh old computers like this to turn yellow. All right. So, let's open this thing up. Got the knobs off with the grub screws, and uh

**Dave Jones:** there'll be a Yeah, there's going to be a cable attached to that, but ta-da! Apart from that, we're in like Flynn. There's a bit of dust inside here, but not a huge amount. But of course, given that it's a

**Dave Jones:** fanless, you wouldn't uh expect a huge amount in there. So, they've got like There seems to be a lot of wasted space under this main board here. I mean, uh this main board's actually on an angle. Um so, it slopes down towards the back

**Dave Jones:** here. It's got these metal uh brackets, but yeah, there's an It's It's a fair bit of wasted space inside this puppy. So, um I'm not sure why they couldn't lower the floppy drives down. I know they did use

**Dave Jones:** uh you know, this space in here and here to hold the uh floppy drives, but you know, they could have had an external pouch for that and made the thing smaller, perhaps. I mean, you know, there's a lot of air in there in there.

**Dave Jones:** So, yeah, it's not the most efficient layout. Oh, yeah, we've got some got some crusty stuff. Now, as for the CRT mount, it is uh separated from the outside of the case. So, it seems to be fairly rigidly mounted to the inner

**Dave Jones:** plastic, but that's going to allow some a reasonable amount of uh shock absorption. You see that uh fold over like that. So, that's you know, an interesting sort of mechanical solution for mounting the CRT in there. But, they

**Dave Jones:** certainly you know, it's not like they've whacked on a like a some sort of spring shock mount or something like that, I don't think. Now, I'm not sure how much I help Leaf Elsonstein had on actually designing this thing. But, you

**Dave Jones:** know, it could have been a fairly one-man bandish type operation. So, you know, I probably wouldn't expect a huge amount of industrial, you know, big company optimization and getting it right down. They probably went, "I want it to fit under an airline seat. That's

**Dave Jones:** the requirement. This is the envelope. Make it fit." And, you know, they would have had a tight time frame to do it in. So, you know, it's not necessarily the most optimized solution. All right, I've taken the screws out the back. So,

**Dave Jones:** hopefully and the side here, there's just two screws there. So, hopefully this inner chassis will just pull out. That's the plan anyway. Oh, do I have to tip it upside down and lift the whole lid off? It's going to be ugly, I think. That's

**Dave Jones:** the key. Just wiggle it out like that. Wiggle, wiggle, wiggle, wiggle, wiggle. Yeah. Come on. Otherwise, you've got to have someone to help you, I think. But, ultimately, I think we are in. Like Flynn. Errol, that is. So, that really is quite

**Dave Jones:** fascinating how it's inner chassis is just this folded ABS plastic, I presume it is, in a shell like this. And, I guess it's actually it it's probably kind of clever in that this would be really cheap to manufacture. I mean, it's just basically

**Dave Jones:** folded plastic like that, and it gives some supporting there, some give for the internal CRT, which does seem to be ah has it got rubber? No, no, no, I think it's rigidly connected. CRT is rigidly connected, but then they

**Dave Jones:** they give some give to the outer shell. So, yeah, it's just could you use the word clever? I don't know, but certainly clever at a low cost. That's for sure, I think. If we take a look at the bottom, we can see

**Dave Jones:** the classic double-sided layout here. All the most of the traces on the bottom are going in the horizontal direction. You'll find that most of the traces on the top side of the board going in the vertical direction like this. None of

**Dave Jones:** this four-layer rubbish back in the day. And obviously all our memories over here, CPUs in here somewhere, and that looks like a quite a decent layout typical of the day. I don't know if Lee himself actually laid out the board.

**Dave Jones:** They may have had a somebody else do that, but yeah, that's pretty neat. And of course, absolutely classic rolled tin plated board here, and then the solder mask over that. Hence all the little the little crinkly solder mask like

**Dave Jones:** that. Geez, I don't miss that solder mask at all. These you know, famously back in the day you get poor quality solder mask. The the like the resin technology and all the you know, the materials technology wasn't that great. Sometimes they'd peel

**Dave Jones:** off and be pretty horrible. Made in the United States of America. Man, if we flip it on its back and take those four screws off. Ta-da! There is the main PCB. That actually comes apart quite well. I like

**Dave Jones:** it. And here's where all the magic happens. Two-board construction main logic board down here, and it looks like this one is most likely the video board. Dead giveaway on the video Bob, we'll take a a quick look at that. Uh,

**Dave Jones:** obviously we've got our character generator ROM here. We've got some uh, 26116. They would be the uh, character uh, the the video uh, RAM. And this connector over here is the uh, coax that goes off to the RCA connector. So, that's for the

**Dave Jones:** external monitor. But wow, this is how you're doing. Check this out. I mean, you know, nice board. You know, they use the uh, DIP socket here. Board-to-board uh, interconnect with uh, those, you know, down here as well. So, there's

**Dave Jones:** three board-to-board interconnects. That's really nice. And they've gone and ruined it with this completely how you're doing wiring going over soldered to individual pins and vias all over the damn board. What? Lee, seriously, what were you thinking? I mean, you must have been desperate to

**Dave Jones:** get this thing out. Oh, well. I mean, this actually um, screams of uh, PCB layout desperation. Actually, like, oh, I've got a point up here, point up here, couple of points down here. Oh, I can't get them right

**Dave Jones:** down to a connector down here. But, you know, a lot of these are pretty close. Um, what, you couldn't route those down here? But, you know, might have run out of routing space. But, uh, you know, that's the PCB layout person's job is to

**Dave Jones:** uh, figure that all out. And like, they've made the conscious, you know, they did the board-to-board interconnects here. Everything's fine. And then they purposely had the um, uh, classic DIP uh, ribbon cable arrangement going over to various points. Whether like last-minute change

**Dave Jones:** and they didn't want to respin the board or what? Or whether or not they just ran out of routing space. It'd be interesting to know the story of that one. And I might actually uh, see if I can find some photos of some uh, later

**Dave Jones:** model uh, units as well. Maybe they might have fixed that in a later design. But, you know, serial number 20,000, I think this is one of the uh, early units. Hi to all my Brazilian viewers. Are there any TI fabs left in Brazil, I

**Dave Jones:** wonder? Hmm. But of course this is not just a CRT board, it's also got the Z80 processor. In this case it's an NEC job, the D 780C, but it's a Z80 equivalent processor. So it's interesting that the main processor is

**Dave Jones:** on here and you'll see that actually goes into a socket right down to the secondary board, which is rather interesting. So it's a fascinating that when into putting the processor on this secondary board which has to do the

**Dave Jones:** display stuff and not have it on the main logic board over here. That's really weird. I'd love to hear Lee's you know rationale behind all that. So underneath our video board we can actually see this is the main Z80

**Dave Jones:** processor socket here and then we've actually got our ROM, so there it is. We'll be able to see if this puppy works later, but I'll get out the EPROM reader and actually extract the data from that and I'll have it on my website for those

**Dave Jones:** playing along at home. So here's our serial number and our revision. It's upside down here. This is revision J and I'll link in the service manual for this thing down below. Very comprehensive service manual. It lists all the

**Dave Jones:** revisions of the board and they did a complete layout and everything else. It talks about manual wiring changes that we've actually you know seen down here and things like this, but this is one of the released boards after November 1981

**Dave Jones:** rev J. So why it still has all that point to point wiring, not entirely sure cuz like a rev E version of the board was a complete re-layout of the board and they even mention a later I think 1982 there was a complete

**Dave Jones:** multi-layer version of this board to meet FCC requirements because this double-sided board wouldn't be that terrific. You know there's no big ground plane on here. So wouldn't have met the new FCC requirements and quite a quite a few

**Dave Jones:** computer companies of the day actually had issues with SEC compliance and you know, you hear stories about the old Trash-80 computer, I think it is. Like you turn it on, Tandy Trash-80 that is, TRS-80 for those who don't like the name

**Dave Jones:** Trash-80. Like you turn it on, it interferes with your AM or FM radio or something like that. So, yeah. So, they went to a four-layer board for this, but this is definitely one of the earlier double-sided layouts. So, other

**Dave Jones:** stuff around the processor here, the ROM of course, and then some classic Motorola MC6821 PIA or parallel peripheral interface adapter, sorry. And then this ceramic package here, this SAB 1793. I haven't seen that one before, but that's a looks to be the floppy drive

**Dave Jones:** controller. And no surprises because if you follow the money, follow the traces from this floppy controller up here, all the way across here, it's going to that ribbon cable which then goes off to the floppy drives. And then next to that, we've got

**Dave Jones:** a Motorola MC6850. That's our UART for our serial ports, dead giveaway if you show the traces going down there, that's going to our serial outputs here, both for the modem and the main serial port. And we've got a buzzer up here bigger as

**Dave Jones:** well. We've got the bell character on our keyboard, so it has to go ping. And this one thing which you'll notice that's not on here, and that is your traditional battery backup. There was none of this CMOS bias rubbish back in

**Dave Jones:** the day, and there was no real-time clock either. So, this thing couldn't even keep the time when you switched it off. And we can see right down here that this is actually a release rev F board. Look at all the dust. And here's our

**Dave Jones:** memory, check it out. The interesting thing about this is that look, it's all higgledy-piggledy. They just got the chips from wherever they could. Didn't matter the brand, the factory, whatever. No, they didn't buy these all at once. They just the purchasing department at

**Dave Jones:** Osborne master just got the cheapest memory from wherever they could get it and then just whack it in there. Thank you very much. And of course we've got the classic bypass arrangement like this. You see the big fat power traces

**Dave Jones:** running under the memory like this. So they have a bypass cap on axial thank you. No of this radial rubbish. And on each IC like that of the memory array and then some bulk tantalum stuff over here. Yeah, fire starters tantalum. And as far

**Dave Jones:** as the battery pack went, well there's no regulation circuitry around here. There's a couple of diodes to prevent reverse polarity, but that's about it. So we would have you would have had to power this thing like a back power it through the board.

**Dave Jones:** So presumably that's a 5-volt battery pack or it could have had 5 and 12 and then going off. I'm not entirely sure of the details. There's also another thing missing here and that is like a traditional CRT controller chip. So

**Dave Jones:** we've got the processor we've got our character generator ROM, our display RAM, but basically yeah, no traditional CRT controller chip. Must be doing it all manually. As far as the rest of it goes, yeah, look at our exposed mains wiring there. No worries.

**Dave Jones:** Wouldn't be too compliant these days, but back then not a problem. And as for the power supply, nothing hugely special here. We've got a 115-volt tap flapping around in the breeze here. We've got our power transistor on the

**Dave Jones:** side there. We've got a couple of do up couple of axial diodes there with their heat sinks and Rubicon caps there. Thank you very much. And as was common back then and still is today, as tech components somebody else just laid this

**Dave Jones:** thing out. There you go, 1980. So, it's reasonably old. Actually, it's a rather interesting layout in that the mains is coming in here through the fuse around around around around around and primary side switching and then the secondary

**Dave Jones:** stuff. So, the mains input right next to the secondary output. Anyway, fascinating. And we're of course we'd be getting 5 volts out as well for the main logic. Now, interestingly, tucked away inside there, that to me looks all the

**Dave Jones:** world like a thermal cutout. Is it not one of those thermal switches? Huh, I wonder what it's doing. Well, that's fascinating. I followed the wire and it and it actually comes out here and goes to the mains input. So, it's a

**Dave Jones:** thermal cutout on the mains input. Okay. And for all you floppy driver aficionados, here we go. It's a Micro Peripherals Inc. model 51, is it? Manufactured up March 1982. And look, I love how they've got the calibration wheel speed wheel on here,

**Dave Jones:** 50 and 60 revolutions per minute to actually calibrate this using a strobe light. Fantastic. But yeah, the rubber's still in good nick. That'll most likely still work. Anyway, you can see the head in there. You can see the

**Dave Jones:** gold tape under there. Single-sided drive. Now, rumor has it that they deliberately decided to go with a single-sided drive instead of a double-sided drive cuz they thought double-sided might not be as reliable if somebody drops this thing being a

**Dave Jones:** portable computer and that limited the data, you know, capability to single-sided discs. So, I don't know the truth to that, but anyway, single-sided only. Even though double-sided was available back then, they just decided not to do it. And as is classic

**Dave Jones:** for the day, there's not much inside your typical floppy drive. And I love the sector sensor here. Check it out. There we go. They've actually got that as just the Look, there it is. Ta-da! They've just got the photo sensor

**Dave Jones:** directly in there and just that just clips on. Absolutely brilliant. Wonderful tech. 5 and 1/4 in floppy, I miss it. And you'll notice another sensor down in there. Hopefully, you can see it in the darkness. And that's for

**Dave Jones:** seeing that there's a disc actually inserted in this thing. Now, I'd love to get the CRT module out for you, but I've taken all the screws out, but it doesn't seem to be budging. So, I'm not sure what the deal is there. I'm running out

**Dave Jones:** of time, so I might have to leave that, but nothing too exciting. It's from Nippon Electric uh Co. And well, yeah, it's a little 5-in CRT. Ooh, love the big power resistor. Now, I have to know what the hell made

**Dave Jones:** this keyboard so big and thick. Nothing. Oh. Oh. Oh, we've got something Some pins uh really bent to buggery there. What's going on anyway? Tech Inc. assembled in Mexico. Hello to all my Mexican viewers, but yeah, basically, there's a lot of um

**Dave Jones:** empty space inside this thing. I mean, they've made it ergonomic like this, but it's like it only needs to be that thick and it's like No. No. Fail. Anyway, separate numeric keypad. Look at this. And the bell, you got to have the bell

**Dave Jones:** symbol. Got to have make it go ping. And the The ridiculous thing is there's absolutely no strain relief at all on this ribbon cable. There's nothing to hold it in the back. That's just Wow, that is crap. So, that is one

**Dave Jones:** interesting beast, the Osborne 1. And what basically the world's first portable luggable computer. Wasn't battery powered, but hey, this was an absolute phenomenon. They practically gave the computer away for free with the software. Hmm, go figure. Anyway, this

**Dave Jones:** was a revolutionary groundbreaking product, but hey, it didn't last that long. Other models like our Kaypro and other portables came along fairly quickly after this. And of course the classic Osborne effect where they announced a new product and this thing

**Dave Jones:** just uh you know, sales of this thing dried up. And also rumor has it that when they went bankrupt, apparently all the employees just walked out with the units and security apparently didn't know. Like they didn't They looked like they were carrying out

**Dave Jones:** big briefcases or uh you know, something like that. So, they apparently just walked out with all the uh stock. Anyway, I'm not sure how true that is, but fascinating teardown of this thing. And I'd love to hear from uh Lee. I'm I'm

**Dave Jones:** pretty sure he's still around. Uh what's he doing these days? And uh the design of this thing. But yeah, it was popular back in the day, but didn't last uh very long. But a truly groundbreaking product. So, I hope you enjoyed that

**Dave Jones:** teardown. I got some high-res photos over at evblog.com. Link down below somewhere. Check that out. If you like the video, please give it a big thumbs up and discuss it down below and over on the forum and all that sort of jazz. I

**Dave Jones:** will actually put this back together and try and power it up. I think it actually stands a reasonably good chance of working, given it's uh you know, 35 years old or thereabouts, approaching that. Um it's you know, these old computers, not

**Dave Jones:** much that can go wrong with them apart from our power supplies and stuff like that. But unfortunately, I don't have any flo- CPM floppies for it so it does work. I can't power it up. Oh, like as in get it running. Anyway,

**Dave Jones:** catch you next time. I'll tell you what, I can't help but be fascinated by the physical construction of this thing. Oh, wow. It's so kind of we've been given the envelope as a designer. I've been given the envelope and let's just make it fit and

**Dave Jones:** just bend some plastic and you know, she'll be right. No worries, mate. And yep, oops, the carry strap broke putting IT BACK TOGETHER. OH, AND YES, IT DOES ACTUALLY survive a drop of several inches onto the bench onto the

**Dave Jones:** CRT face. No worries. All right, let's see if this puppy still powers up, shall we? Let's give it a bell. I plugged the mains into it. This is a 230 volt model so fingers crossed. Whoa! Heard it go plonk. I saw the lads.

**Dave Jones:** I saw the lads. Come on. You can do it. Come on. These CRT's take a while to brightness. Whoa! We're in! Osborne 1! Look at that! Oh, isn't that beautiful? Osborne 1 rev 1.44 copyright 1983. OCC Osborne Computer Corporation. Insert

**Dave Jones:** disk drive disk and drive and press return. Unfortunately, I have no way to actually produce a 5 and a quarter inch floppy let alone one with CPM 2.2 on it so wouldn't surprise me if the floppy still worked. It might need a head clean or

**Dave Jones:** something like that, but yeah, I mean, all the electronics still working this baby. Do something useful, damn you. Where's a CPM 5 and a quarter inch floppy when you need one? And how quick does it boot? That quick. Well, except when it's got

**Dave Jones:** to read the OS from the floppy, which is CPM. So, if we have a quick look at the ROM dump here, this is the main BIOS ROM. You can see the ASCII equivalent down here, and you can see that we've got

**Dave Jones:** boot error there. Basically, just in here looking for little hidden Easter egg text or something like that. But, here's the boot screen, Osborne 1 rev 1.44 copyright 1983. That's exactly what we saw when we turned it on, insert disk

**Dave Jones:** drive 1, press return, blah blah blah. But, that's um basically all she wrote in terms of uh text in there. There we go. So, we've got some keyboard key mapping, presumably. Uh what's going on there? Anyway, I'm not sure. I can't

**Dave Jones:** see any like hidden Easter egg like, you know, Leif Elsonstein was here.
