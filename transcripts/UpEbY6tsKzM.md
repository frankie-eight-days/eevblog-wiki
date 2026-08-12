---
video_id: UpEbY6tsKzM
title: EEVblog #643 - Mailbag
url: https://www.youtube.com/watch?v=UpEbY6tsKzM
source: youtube-asr
---

**Dave Jones:** Hi, welcome to mail bag Monday, everyone's favorite segment. Yes, I'm using the new benches. So I thought I'd change it up, experiment with the mail bag a bit where I actually open them on camera here on the bench in front of me.

**Dave Jones:** I'll give it a go. Let me know if you don't like it. Let me know if you prefer the previous format. I'll just open them here and then I'll cut to the other bench where I actually do my existing

**Dave Jones:** shot and play with the item once I've taken it out of the package so you can see my reaction when I open it. That's the whole idea. Anyway, let me know. Yes, I have changed a bit of the

**Dave Jones:** background. I've got a bit more instrument porn behind me. So, let's get right into it. And for those who've been watching on EEVblog 2 where I did a couple of tests with exposure and this setup, I'm actually using my

**Dave Jones:** Rode VideoMic Pro shotgun mic instead of my wireless lapel mic that I'd normally do for a like a 2-m distance away from the camera. So, that seems to be working quite well in this position. Anyway, I've now got 10 items to open. Not sure

**Dave Jones:** if I'll get through them all on today's mail bag. But let's give it a go. This one is from Mark Richards and he's from Sylvania in Ohio where Chris Gammell is from. Everyone's from bloody Ohio these days. Cheers fellow blogger Martin

**Dave Jones:** Lawton's there. And uh seems every man and his dog is uh moving there. Although I've heard Rigol are moving out of Ohio. So, there you go. So, thank you very much Mark. Let's have a look here. I know what's in it.

**Dave Jones:** Good thing about this is that I don't have to like hide all the address anymore. There's something in there. Don't want to throw it out. This is the Digi-Key recycled uh packaging. Of course, we've looked we've looked at that before. This is great. I

**Dave Jones:** can just throw it off the front of the bench. How efficient. Like efficiency. Anyway, we've got some Oh. It's a 3D printed stand. And it's a bat symbol.

**Dave Jones:** Hang on. Got to be something else in here, I reckon. Yep, there is. There's a couple of little boards. Let's go to the other bench. First up he's included a bat symbol here for our sake and cut out of red oak and

**Dave Jones:** it's 24-carat gilded edges on it and a three with a 3D printed stand here. So, that is pretty neat. Thank you very much. By the way, how do you guild edges like that? I'm not into doing that sort of thing. Please let me

**Dave Jones:** know. But the major thing he sent in here is what he calls a power or or a power or board. Get it? Power or power? Love it. Anyway, it's a dual input uh power supply that switches basically switches between different

**Dave Jones:** input two different inputs and you can set a threshold voltage with this pot here and then it automatically transitions between two different power sources. Like you could have say a battery power source and a mains power source and it'll the Texas Instruments

**Dave Jones:** chip in here will automatically switch. There it is. Will automatically switch between both inputs when you get to a certain threshold it'll seamlessly so it'll continue to power your product. For example, when the mains fails it'll automatically switch over to battery or vice versa or

**Dave Jones:** you could have it solar powered something solar powered for example then it would switch over to battery. And it's quite a comprehensive list of functions here set by various jumpers and pads on the bottom of the board down

**Dave Jones:** in here. And it can various uh I won't bore you with all the details, but uh it's rather interesting design for a microcontroller, Raspberry Pi, and other low-voltage projects, and uh stuff like that. Now, Mark wants me to

**Dave Jones:** critique the design. All right, let's go. And by the way, Mark is a beginner, and uh yes, this is one of his first uh projects, so I'll go easy on him. But uh anyway, one of the first things I

**Dave Jones:** noticed is that well, the pot is one of these huge ones like this. These These things are easily bumped. You know, you accidentally sort of you know, brush it or move it about, throw it about the place. I wouldn't have used that uh

**Dave Jones:** trimmer there as a set point for something like this. I would have uh used, you know, like at least a flat one that you need to get like a screwdriver in there to actually turn it. Anything that can be turned by hand, no, bad

**Dave Jones:** idea. Now, I can understand why you did this uh two-board arrangement here. It's actually designed to be breadboard friendly, so that uh it plugs in, and yes, I have checked that you did get the uh pin pitch and everything correct, so

**Dave Jones:** thumbs up there, no problems whatsoever. So, it does plug into a breadboard, and then if you want to use it for say a Raspberry Pi, then you just plug it into this shield at the bottom, and of course, the standard micro the existing

**Dave Jones:** micro USB input here, you can have a secondary input coming in over here, and then you've got of course the USB output, which then goes off to your Raspberry Pi or other USB power product, and then it can then it can

**Dave Jones:** automatically select between the USB or some other uh wide in power source. But the other big issue that is immediately obvious is that the symmetrical pin layout. I can take this off, rotate it, and put it in backwards. So, unless

**Dave Jones:** you've been very clever and actually wired it, uh set the pin out so that it doesn't matter which way it goes in, then uh that's a bad move there. You even need to stagger uh the pins or you know, plug

**Dave Jones:** up one of the holes or do something so you you can't plug it in the wrong way around. And the next thing is the soldering. So, you haven't used nearly enough solder there. I do applaud your use of

**Dave Jones:** minimalist solder. Too much solder looks really ugly, but you really haven't used enough there at all. Always use fine solder, of course. I believe you have been using fine solder like I use, you know, .4 or .35 mm diameter solder.

**Dave Jones:** Really thin stuff, but then feed it on there until the until you get a nice fillet on all of those joints. On the positive side, there's nothing wrong with your hand soldered SMD stuff there. Good work. As far as your jump your

**Dave Jones:** solder jumpers on the back here, I I like solder jumpers. Of course, it looks like you got the pad in the middle and you're just bridging this side here. But, what is L and what is P? When I dig

**Dave Jones:** this out of my you know, junk box to go use the thing, then I don't want to have to go back and read the documentation to figure out what that means. You've got plenty of silk screen space in there to put, you

**Dave Jones:** know, at least a complete word, a complete description. And the other good thing is that on your layout here, you have got solder mask between your individual pads in there. That's a big big beginner mistake. A lot of beginners

**Dave Jones:** just the solder mask expansion is too big and they don't have any solder mask between there or it's so very thin that the manufacturers can't actually manufacture it properly and then you can get solder bridges and stuff between

**Dave Jones:** there. So, excellent work on the solder mask expansion there. Now, I do like the fact also that you've put the manual set resistors underneath the pot. You can't see it here, but Marcus told me that he's done that. I can see it on the PCB

**Dave Jones:** layout overlay as well. So, if you remove the pot, then there's two footprints under there for two set resistors. So, you can manually set and do away with the pot. So, that's neat. I guess if you really wanted to, you could

**Dave Jones:** have squeezed out maybe an extra row in there and put these pins here and just had some of the resistors on the back, for example. But, anyway, like you've decided to top populated. I probably would have maybe populated all the parts on the bottom

**Dave Jones:** because you've got all room in there. You've got that height there available for all your SMD parts. So, it kind of makes sense to put all your SMD parts on that side. Don't worry about calling the board the top or the bottom or or

**Dave Jones:** whatever. It's, you know, it makes no difference as long as you got all your parts on one side, then you could have a through hole part on the other side, for example. And that's how you can get really tiny footprints. So, I think it

**Dave Jones:** could have even It's quite small now, but I think you could have even made that one smaller. Like you could have put the chip and all the other capacitors and resistors underneath this pot and then maybe moved this one row

**Dave Jones:** over and maybe even moved that one row over and just squeezed in the pot right on top. That would have been neat. And my other complaint has absolutely nothing to do with the board or the design whatsoever. It has to do with the

**Dave Jones:** fact that you haven't provided me with a schematic to look at. And also, I went to the website, which I love the name, Mouse Bite Fever, on GitHub. And there are no PDF schematic files available for easy viewing. You've only got the Eagle board

**Dave Jones:** and schematic files. And I don't have Eagle in my system. I'm not going to install Eagle just to view a schematic. So, that's just a note to everyone who's doing open source hardware projects like this. There was actually a threat on the

**Dave Jones:** forum about this, somebody complaining about it. Or one of the threads just went a bit berko on this exact topic, not providing a schematic in a, you know, an easily viewable PDF format. And I think that's pretty essential. And you

**Dave Jones:** know, if you're going to go to the effort to do and release an open source hardware product, just, you know, make the schematic easily viewable. Not everyone has Eagle or whatever on their system. And for those who haven't seen

**Dave Jones:** inside uh this chip before, they are quite neat. They're not a voltage regulator or anything like that. They're basically just a dual switch to automatically switch between the two inputs here. And uh that's exactly what we're doing to uh power MOSFETs in

**Dave Jones:** there. Not huge power, of course. It's only uh this particular device is only designed for low power stuff. But I noticed on Mark's uh GitHub that he's done another design which uses an external MOSFET which uh allows for

**Dave Jones:** higher voltages and higher currents. Anyway, two internal MOSFETs which are just basically switch off and on. But it allows some extra functionality. It's got a current limit adjust here set by an external resistor. And I don't know I

**Dave Jones:** Mark didn't mention anything about the current uh limiting. So that's probably one extra thing I would have done on here maybe if you had room. I'd at least put a footprint for the current limiting resistor. I'd maybe even if you had

**Dave Jones:** room, maybe not on this design, but if you did, I'd have like a couple of uh DIP switches on there. Maybe a little uh two or a four-way DIP switch or something like that with four different value resistors. And the user can just

**Dave Jones:** like choose four different two or even just two different uh current limit settings. That would uh that would be nice. Anyway, it's got a building thermal cutout and all sorts of stuff like that. And uh really quite nice

**Dave Jones:** dedicated chip for switching between two input sources here. And dead easy to use. I mean, you basically feed the voltage in, you just decouple it. Feed the voltage out, you might have to decouple the output. And but uh not much

**Dave Jones:** else. Bob's your uncle. And as far as the PCB layout goes, I don't uh mind it at all. Uh you've got some right angles there. The electrons is going to fall fall off the corner. Jeez, some people take that seriously.

**Dave Jones:** Unbelievable, but yeah, we can basically switch between the top and the bottom there. Look at that. Neat. And something that I immediately always look for on designs like this is, well, do you have enough via stitching in here to

**Dave Jones:** get your ground coupling over because your current is not flowing through here at all. It just stops. That's just some flood fill. See how flood fill this is? Not bad. And but basically you've got your ground coming across here going

**Dave Jones:** through up through one via there and jumping across to another via down in there. So, you know, as a general rule of thumb, one via good enough for, you know, half an amp, something like that. So, on this design, which is designed

**Dave Jones:** for low current applications, yeah, it's going to be good enough. Just as a matter of course, maybe I would have thrown in an extra via, but probably not on this design. So, that's fine. And yeah, not a real issue, but as I

**Dave Jones:** said, I would have just mounted all of the parts on the bottom, SMD parts on the bottom underneath the through-hole trim pot, and then did it that way. So, you still get the advantage of being able to mass

**Dave Jones:** manufacture this thing because your components are only, well, mass manufacturing, you still manufacture it when it's whether either it's single-sided or double-sided component loaded, but the fact is it only has to go through one pass in the SMD machine.

**Dave Jones:** If you were mass manufacturing this, which isn't the case, but if you were, then good practice dictates you put on the parts on one side and the through-hole part, well, they would just hand solder those anyway. So, and that's

**Dave Jones:** a potential way you could have maybe, you know, made the board, you know, that wide or something like that, perhaps. At a guess, I don't know. I haven't done the actual measurements and things like that, but hey, that is a good first effort for an

**Dave Jones:** electronics beginner. I like that. Good on you, Mark. Thanks for sending that one in. And if want to check out his project, it's github.com mousebitefever. Staying alive. Staying alive. Staying alive. Next up, we have one from the old dart.

**Dave Jones:** Yes, England. And uh this one comes from Mr. Damian Nagel. Good on you, Damian. And let's crack this sucker open. Let's see what we've got inside.

**Dave Jones:** I'm liking the look of this. Liking the look. Here we go. Ooh. Go away. Yes. Casio FX-7000 GB. Awesome. GB, Great Britain. Hey. Beauty. Unbelievable. Damian went and married a bloody pom. Oh, he's actually an Aussie and he married a

**Dave Jones:** pom and that's why he's over there, but he's back now apparently. He has returned. Anyway, he This is what he actually paid for it, two pounds 50 p. Awesome. In a thrift shop. Unbelievable. I always wanted one of these babies, the

**Dave Jones:** FX-7000. I lusted after this. I never had this one and it's just awesome. Look, you can get a sine wave.

**Dave Jones:** And this is pre-VPAM rubbish, too, I think. So, yeah. Beauty. Like I hate VPAM. VPAM's stupid. And there's a nice postcard of the Clifton Suspension Bridge. I haven't seen that one, but I have been over the world's longest

**Dave Jones:** suspension bridge, which or second longest or whatever. It was the world's longest at one point and that was in That's the Humber Bridge. I can't believe what I can't remember what town it was in, but it was on the East Coast

**Dave Jones:** south of Bridlington where I stayed for a couple of weeks. So, it was like yeah, like half an hour's drive from there. And then we have Bristol. Awesome. I have not been to Bristol. That looks a very nice. I'd

**Dave Jones:** love to go back to England. It'd be fantastic. There we go. Somerset and even the Bristol Bristol Channel. Terrific. Haven't been there. I've been to Bath, which is around here somewhere, I think. Yeah, that's right. Bath is like out here somewhere southeast of

**Dave Jones:** Bristol. So slightly off the map. Anyway, I maybe we sort of scooted through the outskirts of Bristol. I can't exactly recall, but yeah, anyway, been to Bath. Love Bath. Fantastic. Wow, there it is. Check that out. That's in really good

**Dave Jones:** nick. I love that. That is fantastic. It needs some batteries apparently. It doesn't work. But yeah, made in Japan. CR2032. Three of them. No worries. I can get that sucker powered up. No problems whatsoever. And as far as keyboard key

**Dave Jones:** layout goes, not bad. Dedicated engineering button, that's what you need. Dedicated inverse button, that's what you need as well. And it doesn't have a dedicated XY swap button. No, that's a bit of a bummer. But it doesn't have a it's got

**Dave Jones:** dedicated squared button, which is excellent. But yeah, shame it doesn't have a register swap dedicated key unless I'm missing it. Actually, this is rather interesting that it's only got two screws on one side here and then has the

**Dave Jones:** tabs on the other side. So that's rather unusual. There you go. Notes on battery replacement. Switch power off. Blah blah blah blah blah. Let's whack some batteries in. That's a rather unusual battery compartment. Just goes in there and just slides in and just hooks under

**Dave Jones:** there like that. It's actually rather effective. I like that. All right, let's see if we can power this relic up. It's not that old. There we go. We have to seriously do some contrast there on the screen, but there we go.

**Dave Jones:** We're in like Flynn. Yeah, it's certainly not the best display there. Look at that. You know, you turn that decent contrast and then then you get all the stuff on the back there. So, it's not It's not terrific screen,

**Dave Jones:** that's for sure, but that's what you get with dot matrixes of that era really. And according to Wikipedia, this was the world's first graph in scientific calculator back released back in 1985. Oh, you know what else happened in 1985?

**Dave Jones:** Yeah. When this baby hits 88 miles an hour, you're going to see some serious Oh, no. Dammit, I was wrong. Even though it's not It doesn't use V Pam, visually perfect algebraic method, it uses true algebraic mode. So, basically what that

**Dave Jones:** means is if you enter like you know, 10, you can't just go in there and hit sign like that. It doesn't work. It gives you a syntax error. You've You've got to actually do it as written. So, you've

**Dave Jones:** got to go sign, it's the operator first and then 10 like that to give you the answer. And that's great if you want to actually, you know, evaluate a big long expression, you enter it in it in and

**Dave Jones:** you know, yeah, okay, it's it's fantastic, but just for every every day day-to-day use, I prefer the old fashioned method. Oh, V Pam. Bloody hell. And forgive me for shooting on this angle, but it's just easier to get a display up and view the uh

**Dave Jones:** keyboard at the same time. Now, if you wanted to graph something, it literally was as easy as this. Graph sign for example, and bingo, it had a draw your sine wave. Look at that. Uh these were just the building functions. Of course,

**Dave Jones:** you could do uh user uh defined functions, but yeah, look, we can just go whoops. We can just go graph, say 10 to the X. Look at that. Here it goes. It's going up and up and up and up and

**Dave Jones:** up. And then you could do stuff like you see trace mode here and then you can just cycle through. You probably can't see it, but there's a tiny little dot somewhere or inverse dot somewhere on that waveform. You can scroll it across

**Dave Jones:** and you can actually get the value off the graph. One of the main disadvantages for your user-defined functions, it wouldn't auto-scale the graph for you. So, you had to go into the range mode here and then actually enter in your

**Dave Jones:** uh ranges manually of your graph. But, you know, apart from that, hey, pretty useful. And this was groundbreaking when it first came out. Oh, you graph your own functions. Unbelievable. I guess the one saving grace of this interface is

**Dave Jones:** that you could actually use the engineering mode. For example, we can go minus three, for example, like that. And then we can actually take the calculator result and then we can cycle through it like that in the engineering mode. So,

**Dave Jones:** yeah, that was okay. But, then like you know, you couldn't just suddenly take that result and then just invert that. You had to do that and then press EXE. It's like For your average one-off day-to-day calculations, that's just annoying. Too

**Dave Jones:** many button presses. And he also sent me one of these ideal voltage detection sticks. Everyone should have one of these. I've got a Fluke one. I've also done a teardown of this one. But, he says this one uses a different board to

**Dave Jones:** the one I tore down. So, let me crack this sucker open and uh see if we can't have a quick squeeze at that. There we go. I can't remember. I haven't watched the previous video. I can't remember, but that's

**Dave Jones:** supposed to be a different board and chip to the one I tore down previously. Haha. So, thank you very much, Damien. This is just awesome. I love calculators. And this one is a classic. I always got it wanted one and this is going straight to

**Dave Jones:** the pool room. Next up we have one from, you guessed it, Deutschland, Germany. We always get one from Germany. I have a huge contingent of German viewers. I'm big in Germany for some reason. So, hi to all my German viewers. Thank you very

**Dave Jones:** much and this one is from F Schlumberger. Sorry, can't pronounce it at all in uh uh Aurienburg? In Germany? I Sorry, I can't pronounce. I'm hopeless at pronunciations. But anyway, let's whip this one open. And let's have a look

**Dave Jones:** what you sent. So, thank you very much F. I presume that's your first name. Frank, good on you, Frank. Here we go. We have a letter from Frank. Um I have the Metrawatt Unigor A43 is Crusty. Uh yes, in a previous mailbag we looked at

**Dave Jones:** the uh There it is. Ta-da! The Unigor A 43 there. We did that in a previous uh teardown and mailbag. This is an AVO meter. It's produced in the former German Democratic Republic of East Germany in 1989. Let's have a look.

**Dave Jones:** We have our Oh. Oh. Oh, good. Look at that classic. Yeah, I'm going to walk around. Look, I'm going to be all modern and trendy with my uh leather multimeter pouch. Look at that. Oh, just whip it out. Here we go. Just going

**Dave Jones:** to whip out my AVO meter except for the fact that I can't get it out and I don't need to because it opens. Oh. Whatever smell that is, it opens like that. Look at that. Beauty. There you go. And it uses a

**Dave Jones:** What's this? 2R10 battery? Never heard of it. Um anyway, the German Democratic Republic, East Germany, 1989. Oh my goodness, look at that. That is crusty as Oh my goodness, does anyone remember using one? I mean, you know, 1989 is

**Dave Jones:** pretty bloody recent and it's just an ohmmeter. That's it. Nothing else. Not even a multi Can't even call this one a multimeter because a multimeter measures multiple things. And usually, you know, vom, volt ohmmeter. You know, at least

**Dave Jones:** it measures volts and ohms and ohms only. Goodness. Actually, you take it out of the box and it is rather cute. Look at that. It's I rather like that. It's got the binding posts and the banana plugs on top. No

**Dave Jones:** holes in it to feed your wires through, but that is That is really quite cute. Look. Beautiful. Ah, look at that back on it. You can see through it. We've got to crack this open. Not that there's going to be much in it. Look at

**Dave Jones:** the bizarre range selection switch here. It's just got dots. I mean, you think they They put the dots on there. They think it And then they've got the dots associated on the display. I think they could have printed them in there, but

**Dave Jones:** maybe they got different models with different maximum scales or something like that. Anyway, down there is times .1 of the scale. So, that'll be from like That'll be like 10 ohms there. Um instead of 100 and over here it'd be times one. So, that'd be

**Dave Jones:** 100 ohms there. And times 10 all the way over here. So, that'd be 1K, 2K. There's no even on-off button on this thing. You just, you know, have it switched to the range and it only works when you actually do the probe. The I

**Dave Jones:** can't even zero that thing properly. So, uh there's something wrong. It's completely cactus. And there's the battery holder down in there. Uh half of that 2R10 battery, whatever the hell a 2R10 battery is. But, yeah, look at that. Anyway, four screws, in we go. So,

**Dave Jones:** there's a look inside the movement. And by the way, the uh this on the back here, on the bottom I mean, would be the uh zero ohms adjust, of course. And uh But, yeah, that Oh, oh, oh, there we go. We managed to

**Dave Jones:** managed to bring it back out. We can actually center that. We can actually z- adjust that right to infinity. There we go. Woohoo! She's back in action. And of course, then we use the uh zero ohms adjust on there. So, if we can hook up a

**Dave Jones:** battery to it, this puppy might still work. And I powered it up here. And well, I can get it to deflect. But, uh basically, I can't get the uh zeroed ohms function to work at all. And well, it's nowhere near it. And it just

**Dave Jones:** doesn't seem to really work. So, what fail. And it's not really worth taking apart any further. Take that plate off. I mean, down in there, there's a couple of resistors and basically uh bugger all else. But, that's that's pretty much what you'd

**Dave Jones:** expect out of an ohmmeter like this. I mean, you know, we've got a So, there's a big magnet in there, which uh sits around our coil, our deflection coil. And uh well, you know, it's about it. It's got a

**Dave Jones:** trimmer down here. And well, not much at all. And the original manual. Look at this. There we go. For those who can read it. I'm sure a good uh probably 1/3 of a quarter of my audience can anyway and

**Dave Jones:** fantastic there you go. That's who makes it in VEB what even try and pronounce that but you go in Linnenstrabe in no that's street sorry Linnenstrabe 244 244 Linnenstrabe is a street is it not and there we go we have some specs.

**Dave Jones:** Couple if there's no schematic in it. Ripped off there it is 5th of March 1989. Guess there was still a call for this thing in 89. Go figure tested by number three I think what proof means I'm assuming

**Dave Jones:** so there you go thank you very much Frank that is I wouldn't say crusty but minimalist would be probably a term I would use but it's kind of cute I mean it's got a it's got a nice case so it's really quite

**Dave Jones:** rugged I'm sure it could survive a fair bit of abuse actually and probably has because well it's it seems to be non-functional but there you go thing of beauty joy forever. And this one looks like it's from anonymous but look it does have

**Dave Jones:** my picture on it. Woohoo look at that fantastic. All right any resemblance? Great anyway thank you anonymous person at local of course if you don't know the Australia Post bubble wraps from Mount Annan local post office. That's here in

**Dave Jones:** not too far from here and hey hello. Oh there we go. Dymo we have a letter. Greetings Dave and it's from Mike. I've included for your teardown and fault finding pleasure an old sharp ZQ-5200 electronic organizer. Yes, a whopping 64K of

**Dave Jones:** memory. Um he received this from his father as a child when he was working as an electronics engineer at Sharp in Huntingwood. Yes, Huntingwood is just here in Sydney, just down the Great Western Highway there, out west. Uh back

**Dave Jones:** in the '80s and '90s. I wonder if they're still there. I haven't driven past there in years, but there used to be a huge Sharp factory uh on the Great Western Highway out in Western Sydney here. Geez, I started

**Dave Jones:** working in 1989. How young are you, Mike? Geez, if your dad worked there in the '80s and '90s. Um there you go. It certainly seen better days. Well, yes, it has. Look at that. I used one of these. It was a small much smaller

**Dave Jones:** thinner one. It was even thinner than half that. May- Yeah, it was like a third of the thickness of this thing and it was a I think it was 32 or 64. Um but I didn't get this one because I wanted

**Dave Jones:** something really uh slimline. And uh yeah, I remember these things and I actually used it back in the day. I had uh you know, I used it as an address book and stuff like that. I had people's uh contact details and phone numbers

**Dave Jones:** back then before the days of mobile phones, of course. You know, you'd have these things and you keep diary appointments for my very hectic social life as a nerd. Yeah, right. And yeah, these were um quite useful back in the day.

**Dave Jones:** And uh they I never lost any info from it. They always had a a primary battery and a second uh battery backup uh battery. But uh you could and then a supercap on top of that. There we go. It's still in

**Dave Jones:** there. See, two three uh two three Goodness, we'll get it right eventually. CR2032 batteries. And uh normal operation, yeah, this one had the mode switch where you had to actually uh put it if you certain location if you wanted

**Dave Jones:** to replace the sucker. And these battery replacement mechanisms were what actually work quite well. In normal operation, look, with the tab switch there, you couldn't physically slide this across like that to remove these batteries here. If you want to replace

**Dave Jones:** the And if you wanted to get And this one at the So, this is These are the operational batteries. This is the battery backup one here. You couldn't physically slide that. So, none of them could fall out. You couldn't replace

**Dave Jones:** them. If you want to replace the backup battery, you had to move that over there, and then you could slide that out. You still couldn't get these out. If you want to replace the main batteries, you slide that down, and

**Dave Jones:** bingo, you can pop the batteries out. It's a neat system, idiot-proof, so that your muggles operating these damn things can't uh screw it up. And lose all their contents. And of course, cuz these were kept in SRAM back

**Dave Jones:** in the day, they weren't uh you know, kept in flash or anything like that. All right, I've replaced the batteries. Let's see if this sucker works. Nah, it's a It's a file. Might have to Is there a reset switch on this

**Dave Jones:** sucker? Nah, it doesn't even work after pressing the reset switch. It's cactus. All right, so let's open this. I've taken off the uh peeled off the back cover. It literally just peeled off. It was just stuck on the instructions

**Dave Jones:** there. And uh of course, this thing is uh It's not going to be much in here. There's going to be a basically a single-chip solution pretty much plus my uh external memory. There will be an external 64-Joule 32K

**Dave Jones:** SRAM. And uh kilobytes, that is. And that's probably uh all she wrote. Look at that. We got some I don't know. Do I have to peel that one off, too? Probably a couple of screws under there. Yes, uh Sharp pretty much owned

**Dave Jones:** the organizer business back in the day. I'm not sure when the glory days of the organizer started and ended. If anyone knows, it's probably on Wikipedia. If anyone knows, that would be a interesting to find out. Ah, anyway, got

**Dave Jones:** another bloody screw up under here. Maybe I could just break that sucker, but yeah, Sharp were pretty much number one. The Sharp organizers flooded the market. They had so many different models and I I I really liked the user interface on

**Dave Jones:** them. I thought it was really quite good. And there we go. Yeah. Quad flat packs and uh memory ROM single chip solution chip on board job there doing something. So, let's and that's our expansion interface over there that Mike was talking about the

**Dave Jones:** serial expansion or some other expansion interface right on the end like that. And yeah, it's about all she wrote. There's our 32 kHz crystal. Now, check this out. What I at first glance, I thought this chip on board device here

**Dave Jones:** was actually yeah, mounted on the main board, but it's not. It's on a secondary board here and then that board is surface mount soldered onto here. Almost like it's I don't know, not really an after thought, but gee, I don't know. And then the

**Dave Jones:** 32.768 kHz watch crystal is then just you know, tacked onto a couple of the pins and that chip here. So, that's going to be more than the just the real-time clock chip. It seems they went to a lot of trouble for a real-time

**Dave Jones:** clock chip. I mean, this is not hugely old this thing. So, anyway, we've got ourselves yeah, there we go. 27C 256. They're our ROMs actually. So, that's our firmware and there's our SRAM up there. And really there's not much

**Dave Jones:** else to it. Here's one of the expansion ports on the side here and that's just a serial expansion port. Couple of look, they've got an insulated pad under there and they've gunked down a couple of these chokes here.

**Dave Jones:** Not sure why they've done that. They've bodged on a cap here, look, and they've tensioned the detail and they've actually put Don't know why they've bothered, but they have. They've put a some heat shrink tubing over one side of that and

**Dave Jones:** there's the other expansion port underneath there, but as you can see there's bugger all inside these things. I mean there's, you know, there's naff all in them and it's all in the firmware and and of course all the

**Dave Jones:** LCD driving stuff is all going to be up in here, so that'll be, you know, the big dot matrix display that's going to have its own, so maybe we can crack that open and just very quickly and have a look at

**Dave Jones:** the LCD drivers up there. Nothing exciting though. Well, that's interesting. I expected another PCB in there maybe with some quad flat packs driving that board and a zebra strip or something going in there, but we have some, you know,

**Dave Jones:** chip on flex here and uh some hot bar stuff going on there and uh There we go. Well, we've got another one. There we go. And so they're on on the flex membrane and that's pretty much it and of course this would be a

**Dave Jones:** sharp LCD cuz sharp were, I think they still are, huge in LCDs. So, there you go. They really know how to manufacture LCDs, sharp, and they would have been able to churn those out for pennies and that's, you know, it's quite advanced

**Dave Jones:** manufacturing which you know, goes into getting those sort of things right. So, that is about all she wrote. Then we've got a keypad going down there and not much else. So, here you go. It's a bit of a mess, but thank you very much Mike

**Dave Jones:** for sending that one in. These were these pocket organizers were huge. So, if you do know the uh lifespan of these things, when they actually, you know, died and how quickly they die. I think they did die a pretty

**Dave Jones:** quick uh death in the end, but I I certainly had a sharp one and I've probably still got it somewhere. And it probably still works. Probably still got the original backup battery in there. These cuz these SRAMs are ridiculously,

**Dave Jones:** you know, it's ridiculously low current. It's basically the shelf life of the battery in these things and yeah, they were great back in the day. And lucky last for today, yes, I still got two four five left. So, I'll

**Dave Jones:** leave those for next mailbag Monday, which hopefully should be next week. Can't be 10 in one episode. It gets pretty ridiculous. Oh, this one's from uh Aiden Senior. Once again, Aussie um envelope. He's from uh Stockton. Once again, in New South Wales. So, thank you

**Dave Jones:** very much Aiden. What do we have? Oh, another bloody mobile phone. You know how many bloody mobile phones I've got? Uh unbelievable. This is a tiny though. A little Motorola thing. Man, they don't make them this small anymore and

**Dave Jones:** well, yeah, I can see why. Geez, you could almost swallow that thing. Unbelievable. And what else have we got? It's a universal dimmer. Why? There's a note. All right, Dave, I thought this clips will be controller dimmer would make an interesting mini

**Dave Jones:** teardown fun and quite fascinating considering their size and the fact that it can drive 450 W. Yeah, there's probably going to be very little uh well, there has to be by their nature, uh very little loss in there. Uh they

**Dave Jones:** have to be quite efficient. Um just, you know, the sheer numbers. You can't uh drive 450 W and be 90% efficient cuz if you're 90% efficient, you're dropping, you know, 45 W in this thing. Not possible. So, they're incredibly efficient. This

**Dave Jones:** particular one was scratchy. I keep love the blog. Keep up the good work. I watch your episodes with frequency until it megahertz. What what what what. Thanks, Aiden. Yeah, I've never used one of these before and I don't

**Dave Jones:** particularly know what's in them, but there is a board. Look at the bottom. I mean, this one has a has a nice big pot on the back. That's what he said was scratchy and there's a fair bit of

**Dave Jones:** surface mount integration in that circuit. Let's crack it open. Wow, these little puppies are chock-a-block. Look at this. I mean, we've got Looks like we're going to have double-sided load on Look at this. Little cube construction board. So, three boards we're going to

**Dave Jones:** have probably double-sided load on it. There's a lot going on in there and that's actually fairly common to butt boards together in this configuration like that. Right angle boards. I've done that a few times myself, especially inside our slots. You can actually cut

**Dave Jones:** out slots inside a board and then mount it right angles like that and have the solder on both sides. You can actually get a pretty good right angle board out of a main just sticking out of a main

**Dave Jones:** board there. So, they've got just the one tab on here. So, we're going to have to desolder that. And I'm trying to pry this thing open and these bastards are soldered shut. Unbelievable. What a turd. Oh, there ain't nothing you can't

**Dave Jones:** fix with a drill. Here we go. Woohoo! We're in. So, there you go. That's what's inside one of these puppies and there's our pot still on there. I just cut the pins off the top of that to get

**Dave Jones:** one of the boards out and these two boards here, of course, they were soldered together like that. I had to get my solder sucker and suck out all those pins before I could even get that board out. And um

**Dave Jones:** yeah, so they're actually double-sided, pretty densely populated uh double-sided load there. Lots of little uh six-pin sot-23 packages. I don't know why they need to go to all that trouble. Anyway, here we go. Here's the uh Here's where we get

**Dave Jones:** all of our uh the switching and efficiency from. We've got two MOSFETs here. They were riveted into the sides here. There you go. They've got some pop rivets there. So, I had to drill those out and uh let's take a look at that top

**Dave Jones:** board. Once again, double-sided load, not surprising. Here's our mains input. Here, we've got our four uh bridge rectifier diodes. So, they're forming a bridge rectifier, no doubt. Uh that's not surprising. And then we've got a cap on top of this. And of course, that cap

**Dave Jones:** is a quality uh Reifa brand one there. So, you know, no drama there whatsoever. You'd expect these to be high quality, of course. And then there's an E3F uh 250-V rated 115°C thermal cutout. That's from Microtherm. They make a nice little thermal cutout

**Dave Jones:** devices. So, basically, if in the inside of here, I mean, it's not thermally bonded over here, but basically, if the inside of that uh case pretty much gets to 115°C, then it's just only just going to cut the mains off completely. So, little

**Dave Jones:** safety feature. And no surprises for guessing, we've got some MOSFETs in there. It's standard pretty standard ones, 20N60C3. Well, standard for this sort of uh application that requires the uh massively high efficiency cuz, you know, that's not much of a heat sink there.

**Dave Jones:** So, you really, you know, these things have to be incredibly efficient. Um as we said before, 450 W. So, you know, you can only uh even at 1%, you know, 99% efficiency, that's still 4 and W inside that tiny

**Dave Jones:** little beast there. So, let's go to the data sheet. And no surprises for guessing that you get sort of, you know, the world's best RDS on, which is the on resistance when the MOSFET is switched on in a TO-220 package. So, world's best

**Dave Jones:** one, don't know if that claim is actually true, but RDS on 0.19 ohms there, 650 V VDS rated, 20 amps. These things are a beast. And I'm not They're probably not cheap, either. I don't know what the Digi-Key price is,

**Dave Jones:** but yeah, these puppies wouldn't be extreme DVDT rated or periodic avalanche rated. Beautiful. Look at the specs. So, thank you very much, Aiden. That's a rather little interesting mini teardown, as you suspected it would be. These things are

**Dave Jones:** chock-a-block. I can't believe how much, you know, why they need all of that. Gee, I don't know, but if anyone has a schematic for one of these puppies, it'd be really interesting. I mean, we're not going to get part numbers off these,

**Dave Jones:** really, you know, easily obtainable part numbers off these little six-pin sot-23s and stuff like that. So, if anyone does have a schematic for one of these puppies, please link it in. Let us know. So, there you go. This has actually been

**Dave Jones:** a very lengthy mailbag Monday, even though I only opened up half my stuff. Anyway, please let me know about the new format with, you know, the talking head shot on camera. If it's any good and if you like that, I've I'm actually

**Dave Jones:** shooting this with two different cameras here, by the way. There it is. So, I got my got my B-roll camera. That one was the one I was like shooting the material with, and there's my Rode VideoMic shotgun VideoMic Pro, and I just sit there, and

**Dave Jones:** it actually works pretty well. I just, you know, soon as I'm done shooting something here, I come over this bench, which has my Canon HF G10, my main camera, and I shoot all the stuff on the bench as I

**Dave Jones:** normally would. So, let me know if that's any good. If you want to discuss it, jump on over to the EEVblog forum. And as always, if you like Mailbag Monday, please give me a big thumbs up. Catch you next time.
