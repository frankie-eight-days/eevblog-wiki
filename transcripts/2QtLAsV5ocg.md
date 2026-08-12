---
video_id: 2QtLAsV5ocg
title: EEVblog #970 - Mailbag
url: https://www.youtube.com/watch?v=2QtLAsV5ocg
source: youtube-asr
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, Mail Bag. Let's get right into it. This one contains awesomeness, so we're going to crack this one open. It is from Ready Made RC. Ooh, sounds good. Ah, so much crap on this bench. Don't know

**Dave Jones:** where to start. Let's get into it. What have we got? We've got a note. Don't want to spoil it for myself. Ooh. Does look pretty awesome. In terms of boards, aha, James Field, thank you very much, James. Um,

**Dave Jones:** and aw. We've got some serious power business happening on there. There you go. Look at that. Anyway, what have we got? We've got a portable Android player, too. Ah. Maybe it's not. No, this looks all old stuff. So, let's

**Dave Jones:** Yeah, we have a portable Android A Pap II. This is like that feels so crusty. That's got to be one of those, you know, cheap eBay jobbies or something. Um, you know, AliExpress jobs. Um, little Android game player, really?

**Dave Jones:** In that sort of Nintendo E type form factor, and we've got a controller board out of something. Enclosed is a single channel output card from a high-end audio amplifier. Uh, typically used to power high high output loudspeakers in commercial insta-

**Dave Jones:** installations. Data sheet enclosed. Aha, there is our data sheet. It's a C88 column four for those playing along at home. So, this is what we're looking at here, the Lab.gruppen. Um, Gruppen, never heard of them. C series, C88 four. There's the back of the baby,

**Dave Jones:** 8,800 W uh peak. Okay, peak total power output. Yeah. Good old PMPO. Geez, what are we back in the late '80s or early '90s or something? Anyway, here's the board and James says this is like one of the

**Dave Jones:** Rolls-Royce of pro audio amps. Retails for about 5,000 AU. So, yes, here's a bit of kit. It was apparently cheaper just to do just to replace the board than it was to you know fix it or whatever. So, yeah, it

**Dave Jones:** said DC output protection fault. So, who knows? So, it's actually not a bad layout board here. Very typical of a stereo amp. You can see the symmetry right down the middle. Just flip the thing open and you know power down here

**Dave Jones:** at all. It's going to all flow quite well. The layout's quite reasonable, I suspect, but it's there's a lot of you know you have to get the grounds right, everything else. Classic star grounding is Let's have a look here, you know,

**Dave Jones:** fanning out from the power supply like this and then that's tapping off there. So, you know, probably they're doing the business. But anyway, um for those power transistor fanboys, ooh, don't recognize that. And everyone's going, "Dave, what are you talking

**Dave Jones:** about? They're obviously sanking 2SC3263s." Yeah, okay. Obviously jelly bean NPN Well, I'm not going to say jelly bean, but you know, there's nothing special about it. They're like four bucks one-off quantity from Digikey NPN planner power transistor. Meh. Tell you what, I

**Dave Jones:** do like how they've bolted those down to that heat sink. That really is quite uh That really is quite jazzy. Look at that. I mean, it's got them going vertically like this cuz you could see that on the photo that we saw before.

**Dave Jones:** These go right on the back panel and the air flow comes from inside straight over those. So, I would hazard a guess that'd be pretty darn effective. They've gone to effort to make a little surface mount board there. Presumably, that's, you know, a

**Dave Jones:** deep and discrete transistor front end amp, I would presume. And but of course, everything else is through-hole tech. I mean, there's nothing, you know, really fabulously modern going on here. The design could date from, you know, anywhere back to

**Dave Jones:** the '80s, really. And of course, the symmetry in the design there not for, you know, it's two separate channels, but it's going to be both the positive and negative cycles. If you look at any typical schematic for a power amplifier,

**Dave Jones:** they're going to be contained like it's basically a totem pole output. So, there's going to be transistors. If we flip it over, there'll be There you go. We've got ourselves there'll be matched N-channel and P-channel or NPN PNP, depending on

**Dave Jones:** whether they're MOSFET or bipolar. Symmetry in the design like that. So, yeah, it's both designed to drive it hard to the negative rail, hard to the positive rail, all about the center ground point. And of course, that will

**Dave Jones:** star out nicely and all your usual star grounding techniques will be involved in that. So, I can't see anything really wrong with that. It's quite well made. It's just, you know, a typical high-quality discrete transistor design. It's but 5,000 ayou, the Rolls-Royce. I

**Dave Jones:** don't know. Just Just doesn't smell Rolls-Royce, but it's certainly not 100 low. Interestingly, on this side here, we have an NTC thermistor that's doing temperature sensing of that heat sink. But this side over here has three transistors instead of the two

**Dave Jones:** with no thermistor. So, hmm, they're only thermally checking one of the rails. It's a bit poor. So, they don't look particularly like main output tranny-worthy. So, let's have a peek under here. I've taken out the screws. Ta-da! Woah, yeah. Looks like power

**Dave Jones:** MOSFET time. Oh, yeah, now we're talking. ST semi, uh, 60N K 30s. These are super mesh power Woah, now we're talking. Beauty. And I can't read the number on these, which are clearly, uh, diodes. They're, you know, two-pin,

**Dave Jones:** uh, power packages. And um, under the Mantis microscope, with the right at the light at the right angle, they're an ST something or other. Anyway, it doesn't matter. What they're doing is they're actually, uh, going back here. Woop. Through

**Dave Jones:** some big chokes on there, and they're going to the output, uh, heat sink here. So, these heat sinks aren't actually connected. Well, there it is, right? There's the two, um, there's the diode between, uh, the heat sink of the output power

**Dave Jones:** transistors and the heat sink over here. So, what they're doing? Some sort of big protection. It's a big power Oh, there's a little sneaky bugger. Temperature sensor on that heat sink there, the main power transistor heat sink. Neat. It's the PAP 2, portable

**Dave Jones:** Android player. It's a gaming tablet thingamabob. Interesting. The IC PAP 200. Sh- It feels really crappy quality. Anyway, it's got Android and I guess some games built in. Yes, it does work. Takes forever to boot, though. It's got little

**Dave Jones:** clicky buttons, which have, uh, backlit LEDs behind them. It's kind of, you know, give it to your kid, it'll probably cost 10 bucks or something. I don't know. Hmm. Well, plays Angry Birds, whatever that is. I don't know.

**Dave Jones:** I'm not newfangled freaking games. And it's actually rather neat inside. Bit of battery of questionable origin and quality just flapping around in the breeze, held down with tape. And we've got AM logic What is that? AM 8726 M3. It's not a Cortex M3. It's actually

**Dave Jones:** a a Cortex That's actually an ARM Cortex A9. And that's an ARM 7 Cortex A9. And it's not particularly powerful, but you know, it's cheap and cheerful system on chip stuff. We've got some memory and we've got the little joystick down here. That

**Dave Jones:** looks funky, but that's just a joystick. You might think, "Ooh, what's that little antennary thing?" No, it's just the bottom of the joystick. Just just cheaply soldered onto the side of the board like that. It's not very robust,

**Dave Jones:** but kind of sort of built down to a price. Does the job and not much else. Basically one big system on chip but that's all you need. ARM Cortex A9. And that for all the world looks like a

**Dave Jones:** Realtek Wi-Fi module. So, that's about all she wrote. We've got a headphone socket, there's a USB for the charging. Bob's your uncle. So, I'm not sure how much this was. It seems to Let's see. Hard to find info on it. Sort of like

**Dave Jones:** discontinued as you'd expect. These things have a you know, 6 to 9-month lifespan if they're lucky. But you know, tens of dollars maybe. It's like It's bugger all. I mean, you can get a mobile phone for tens of bucks, can't

**Dave Jones:** you? It's crazy what you can get. I mean, it's just the technology 10 years ago. This would have been insane. But wait, as a bonus we have the USB charger 5 volts half an amp. Made in China. Oh good. Xiang X caps.

**Dave Jones:** Oh yeah, wonderful. Just Well, at least it's fused flapping around in the breeze there. But bugger all clearance between primary and secondary. Come on. And that transformer, I mean, seriously, that, you know, where's that way on? Someone's kitchen

**Dave Jones:** table? But, I've seen worse. Next up, we have one from Bataroo Inc. Open it up. Bataroo battery life extender AA batterizers, as they're better known. Who gives a anymore? I mean, like I I think I've lost all enthusiasm to do

**Dave Jones:** another batterizer video. It's just been debunked as so many times on the forum and everything else. It's like, yeah, it's yeah, there's the thank you note from Dr. Bob. Like, who gives a anymore? This product it it's just

**Dave Jones:** so demonstrably crap. It's Next. All right, we've got ourselves a local jobby from person unknown from uh Melbourne, Bourke Street in Mel- posted from Melbourne CBD. So, let's check it out. Thank you very much, person anonymous. They may actually reveal themselves

**Dave Jones:** inside. Who knows? It's pink. That's a concern right off the bat. Um original phone, crusty old plug pack, a princess made in Taiwan plug plug pack. All the best stuff was made in Taiwan. Um wow. Wow, I haven't seen one of those for a

**Dave Jones:** long time. It's a princess PBW 121 portable television. It's a portable television studio. Oh, wow. That is gold. Hands up if you had one of these babies, the princess handy TV. Thank you very much. You can just take it anywhere. Get your fingers

**Dave Jones:** under there, carry it around. Rocking. And who's William McGregor? Born 21st of October, 1928, I assume this came from some estate sale. Watch this. Color-coded dial, pink and then yellow to match the symbols next to it. That is

**Dave Jones:** gold or pink. Mhm. And yep, that's exactly what you'd expect to find inside this thing. A little tiny CRT, which is really cute. And it it does the business. It's very typical of a It's neat and tidy, very typical of a little

**Dave Jones:** portable TV of the time. We've got our tuner down there. We've got a lovely looking yoke there. Got our flyback transformer. No touchy, of course. Um and it you can just one main chip down the bottom, which is an AN 515

**Dave Jones:** 1N or IN? I don't know. Anyway, that's a Mitsubishi job, and that's just neat and tidy. I kind of like it. And it's a Clinton CRT. I think they went out of business this year, didn't they? Or late

**Dave Jones:** last year. Mhm. You know, I'm going to assume that's a date code, 8642. So, yeah, 1986, that would be the vintage that I remember these things. I can I can remember these in the shops and thinking, "Oh, yeah, that's pretty cool.

**Dave Jones:** Portable TV. Wow." And of course, this is a black and white CRT. None of that color rubbish. There's no, you know, usual big focusing coils and all that other gizmo in there. And you know, your triple electron guns and all that fancy

**Dave Jones:** pantsy stuff. No, black and white did the business. VHF and UHF. Unbelievable. Now, will it work? Switch it on. UHF and let's tune in channel 62. See if we can pick up the video from UHF. Hang on. I forgot the telescopic rod antenna.

**Dave Jones:** YOU BLOODY RIPPER! HEY KIDS, WHERE DO YOU WANT TO GO? Uncle Nazi's clubhouse. That's right. I'm your Uncle Nazi AND BOY OH BOY ARE WE GOING TO HAVE SOME BIG FUN TODAY, HUH KIDS? Another local jobby. I won't pretend I

**Dave Jones:** haven't opened this because it didn't have mail bag on it. If you're going to send something into the mail bag, actually write mail bag on it somewhere so I don't um you know, I thought this is maybe something I ordered on eBay or

**Dave Jones:** something like that and it just came in the came in the post. So, sorry to Although, I haven't actually opened the item yet. Sorry to Cody. Um I just thought I'd send what used to be my old Curiosity got the better of it. He tore

**Dave Jones:** it down himself. Uh Anyway, there's also a kit something with it. Um this will not be a 2-minute teardown.

**Dave Jones:** I love when I get stuff pre-torn down. Look at this. Oh oh. Woah, that's crusty as. Okay, I thought it was like um it is a Nikon D300S pre-torn down. Wow, and it sort of looks in pretty crusty

**Dave Jones:** uh condition, too. So, we'll take a closer look at that. And there's the pentamirror. Beautiful. Look at that. That's just gorgeous. That um you know, they're I'd love to know the manufacturing that goes into those. They're pretty darn high

**Dave Jones:** quality and you can see that down there that like, you know, this is like a was a serious and still is a serious camera in its day and being able to uh uh deflect the light like that and with,

**Dave Jones:** you know, keeping all the optical properties of it, these things are pretty jazzy. I like them. Now, the way a pentaprism works called a pentaprism because it's got five sides on it and we've got two windows here, one here and

**Dave Jones:** one here and it basically bends the light 90° like that. And of course, you could just use a regular mirror, but if you use a mirror, then it flips the image. But, a pentamirror doesn't do that. It doesn't flip the image at all.

**Dave Jones:** But, this is what's called a roof pentamirror. There's the part number for those playing along at home. A roof pentamirror like used in digital SLR cameras like this um only flips the image laterally and I'll show you and

**Dave Jones:** I've got a demo of that. We've got Hello World's flipped laterally like that. Look at that. Beautiful.

**Dave Jones:** Looks like we've got an Aussie fist today. Bloody ripper. Um this is from No Worries Turf. Okay. Um it feels weird. I'm not sure what's in here. Um Let's open it up. Anyway, um from uh Mordialloc a loc

**Dave Jones:** IN VICTORIA. WHAT? UM OKAY. It is actually turf. That's a first. Um I've been sent turf to an electronics mailbag. Um I don't 13 mm Pro golf turf for those playing along at home. Um, like like why? WHY?

**Dave Jones:** WHY have I been sent noworriesturf.com.au instant lawn? It's fake lawn. I like real lawn. I've got buffalo myself. Um, and it's bloody everywhere. Unbelievable. What?

**Dave Jones:** Somebody who watches just wanted to plug their turf lawn business. Okay. You got to wonder whether or not they're going to astro turf in the comments. Get it? Astro turfing. Next. Thank you very much Pedro Silva and hi to all my Portuguese viewers. We

**Dave Jones:** don't get many from Portugal, so that's awesome. Um, let's get straight into it. What have we got? The requisite note. But what is Oh, my god, I uh got a $2 scientific calculator. Oh, crusty as. A Joinus brand scientific calculator.

**Dave Jones:** Oh, well, that's got to be at least worth two bucks. It's got to be. Yep, that's a classic rip off of the Casio FX 82, one of the variants or the 82 MS, I guess it is. Um, and I guess

**Dave Jones:** imitation is the sincerest form of flattery, is it not? Anyway, I've run the uh famous calculator forensics thing on it and this is the result I get. I can't remember the guy's name, but uh he came up with this algorithm that uh you

**Dave Jones:** can work out which chip set or try work out which chip set's used in this thing by doing um sin cos tan arc sin cos tan of nine. And basically, it does a really good result. It gets very close to nine.

**Dave Jones:** I mean, the ideal result is nine spot on, but it's very, very close and there's only two others in the database, these unknown and Dura brand or something and some other One Hung Low brand one that gives the same result to

**Dave Jones:** more decimal places. Um you can find out more decimal places, but anyway, um it it actually does a reasonable result on that. And well, you know, the keys feel okay, but I would not trust a no-name brand like this. Like, you don't know

**Dave Jones:** if it's got any bugs in it or whatever. I would stick with the real brands. Um you know, it I know it's tempting for a couple of bucks, but yeah, just don't. And we'll do the classic 69 factorial

**Dave Jones:** and that's okay. Nothing wrong with that. So, you've got to wonder why it pays them to clone these things. Let's have a look inside. Oh, yeah, there we go. Just Wow, it it's got to use Look, a real

**Dave Jones:** separate piece of piece. So, not as refined as the uh Casio ones, which use the membrane. Everything's integrated in one, but yeah, I mean, they can churn this out for cheap as chips, but it's not like the genuine Casios are super

**Dave Jones:** expensive anyway. Um so, yeah, I don't know. I guess volume. People go, "Oh, yeah, it's a you know, it's got 82 in the number. It's familiar." You know, so they buy it at the $2 store. Meh, I They kind of do the job, but yeah, I

**Dave Jones:** just don't want to use one of these things. It gives me the heebie-jeebies. Where they getting the chipset from? I mean, somebody had to, you know, did they clone the Casio, reverse engineer the Casio chipset as in like clone the

**Dave Jones:** damn thing? I don't I don't think so. Um cuz I think if you I don't have a genuine uh FX-82 here to actually MS to actually compare it with, but I think it'd have to give you a different

**Dave Jones:** calculator forensics result. So, it's I don't think it's an exact clone. So, you've got to wonder who actually does this. I mean, goes to the effort to rip off an already reasonably low-cost calculator and just undercut it severely. I know it's probably volume

**Dave Jones:** and everything else and they've got to be making money from this, but it's not like this is like a uh ghost product that's come off a ghost run on the same assembly line that manufactures the FX uh 82. It doesn't you you know, it's not

**Dave Jones:** built the same. It is like it is a rip off of it. It is not a clone. The chipset is different. The calculator forensics result is different to the genuine FX 82, so it's not using exact copy of the chip in there. And

**Dave Jones:** yeah, I don't get these things. Anyway, I wouldn't touch it with a 10-ft pole. And this is a 4 euro model. Wow, that's pricey. Um you know, I've seen them in the $2 shop here in Australia for two

**Dave Jones:** bucks. Like that's $2 Australian, so what's that in like a $1.50 euro or something like that. Um so yeah, they can be even had cheaper. Didn't even come with batteries. Complete rip off. Anyway, thanks Pedro. It's not a mailbag

**Dave Jones:** without getting one of these. Um thank you very much uh Matthew Shia Shia? Something like that. Anyway, I'm from Dallas, Texas. Awesome, let's check it out. Uh yeah, don't these have a pull tab thing on them or am I wrong?

**Dave Jones:** I believe you ordinarily can open these boxes if memory serves me correctly. Got a requisite note with it. Let's have a look here. What have we got? We've got a dev board. Oh. This looks interesting. I won't show you what it is. I'll just

**Dave Jones:** hook it up and try it out. What we've got here is an ECG or electrocardiogram. I love electrocardiograms and this one's on uh Crowd Supply. Um let Matt uh take it away. There we go. Um he's This is

**Dave Jones:** available on uh Crowd Supply. I'll link it in down below, but it's a uh ECG analog front end for makers, hobbyists, and academics to use with their own biomedical device or electrophysiology projects. Fantastic. And that's how we hook it up. And I will hook it up. Um

**Dave Jones:** you can hook it up to a scope, of course. The uh scope uh your battery here shouldn't be uh mains earth uh referenced. And if your mains were earth reference the output, that's okay, but just be aware it's the

**Dave Jones:** output. And here it is. I rather like the uh enclosure. I don't know why. Like if it's designed to hook up to a scope, I mean we've just got pin headers like this for the output. And that one's not

**Dave Jones:** labeled as well. Or is that the same over here? Vref out. I think they're duplicated. I think Yep. I think that's the same as that. I'll buzz that out, but it's exactly the same. Okay, so they are labeled. So

**Dave Jones:** that's our Vref um uh output. So we put our scope actually on Vref, which is a bit unusual, but you can change the reference in here. They've got various links to uh change the reference. And this is going

**Dave Jones:** to be completely safe. I have no worries hooking it up. Why? Because you can see inside we've got our uh 10k resistor in series there. And I'll hook it up. It only draws uh you know, a couple of hundred

**Dave Jones:** microamps uh total or milliamps. So I'll just hook it up to like a CR2032 coin cell that battery. The power supply is from 1.8 volts to 5.5. So very wide range. You just run off a coin cell battery. Completely safe. You've got uh

**Dave Jones:** the protection resistors in series. Nothing can possibly go wrong. Well, if I release this video, you know I'm not dead. And there's the main board there. I'll link it in down below where you can get uh all the information for

**Dave Jones:** it, but it's got the uh castellations there, so you can solder it directly on the board as we uh see here. So that's all right. I do actually like the um laser cut enclosure, how they've you know done that. Oh, and I forgot to show

**Dave Jones:** the back. There we go. Look at this. All the information, unipolar limb leads, and oh, the Wilson central terminal equations. Look at that. Beautiful. So, all everything you need to know about hooking up ECGs is on the back.

**Dave Jones:** That's kind of neat. I like that. Um yeah, you know, it's a reasonable approach to construction and how they've actually put those in the center of the board and hooked to those and soldered those directly onto the board. So,

**Dave Jones:** that's they've done the slot for the cutout. Uh the slot cutout for the um the nuts in there, the locking nuts. Even they didn't really have to do that cuz the locking nuts don't add a huge amount. I guess you could do them up to

**Dave Jones:** go against the PCB. So, that kind of Yeah. That kind of works. Although, they've still got the leverage on there like that. So, yeah, it's not the most robust thing. But anyway, I would have probably liked to have seen a

**Dave Jones:** like you can get right angle 4 mm banana jacks. But I don't know if these are like uh stand These are probably industry standard for ECG leads. Are they? I'm not in the game. But I like them. And sure enough, it draws about 230 odd

**Dave Jones:** microamps. No worries from a CR2032 coin cell battery. Thing I don't like though is that there's no LED on there to show you that a the power is connected and it's on. And it would have been nice to see a LED on there like

**Dave Jones:** flashing time with the heartbeat as well. I mean, you could surely you could do that in analog, take the output waveform, square it up, do whatever, um and flash a LED. I really would have liked to have seen that. I really think

**Dave Jones:** that's a nice feature that could be added. And even with nothing connected to the input, we're picking up a whole bunch of 50 Hz crap here. That's probably not surprising. It's going to be picking that up from the mat. And if I take it

**Dave Jones:** off there see and get it closer like that. Yep, it just starts to pick up all the all the garbage. It should be right once we actually get a decent impedance on the input from the body. And sorry for the nudity.

**Dave Jones:** I probably don't have a white balance that's high enough to take care of my pasty white nerdy skin, but this is very temperamental. I've got to hold it like this. Can't put it otherwise it's too noisy. And if I move at all or do

**Dave Jones:** anything, then it's going to go all over the shop. Hang on. I think I can talk. But yeah, it's pretty much all over the shop, but you can see the cardiac pulse is actually there and it's doing its

**Dave Jones:** thing. So, it kind of works, but yeah, these I I think this is common of ECG stuff like this, but yeah, it's not terrific. And if we clean that up a bit, I don't know. It's all over the shop.

**Dave Jones:** But you can you can get the cardiac waveform, but it's not pretty. And the other thing I notice is that there's no labeling on these. I mean, sure it's got green, white, and red here, but it doesn't tell

**Dave Jones:** you how that translates to these positions here on the back. So, yeah, I mean, luckily Matthew included that diagram which I'm following. Otherwise, I just looking at this, I wouldn't know. Now, I can actually get decent results from this, but it just

**Dave Jones:** varies all over the shop. I mean, all of a sudden like I'll get crap in there like that and then all of a sudden I'll get that because I've gone near the screen. Look. There we go. I'm picking up the switching crap from

**Dave Jones:** the screen. If I take my hand away, hands further back. No, it's no good. Got to put it back here. There we go. Let me put my hand back. Yeah, put it towards there like it's super duper sensitive. But if I stand right back

**Dave Jones:** from the bench, I can actually get my cardiac waveform, kind of. But jeez. Stevdi Stevdi Hmm, sounds like doesn't sound German. I'm Sven. Um from Berlin. HI TO ALL MY Berlin viewers. So let's check it out. See what we've got. Sven.

**Dave Jones:** Sorry, I can't help but think of a you know, Swedish massage person or something. Um yeah. Anyway, we've got the requisite uh Digikey style um Uh and there's a name for that. I forget the name of it. The corrugated cardboard

**Dave Jones:** packaging stuff. There's like a trademark name for it. Oh, it's a radiosonde. Ooh. Wow, cool. And ta-da! Hi Dave, have fun. Tektronix. That's before they That's the old logo. None of this new logo rubbish. What have we got? An oscilloscope evaluation guy.

**Dave Jones:** We've got some original tech documentation. Um and a little itty-bitty teeny weeny board. Oh, is that a It looks like it's a scope eval kit. Oh, cool. So it generates waveforms and stuff like that. I love little Yeah, it's a genuine

**Dave Jones:** Tektronix evaluation board. Let's see what it does. We've got ourselves a Vaisala radiosonde RS80 for those playing along at home. Helsinki, Finland. Hi to all my Finnish viewers. And is it Look, it's got a and like the attachment string

**Dave Jones:** thing for it. What do you do? Just pull it out of the box? How Why is that sticking out of the box? Anyway, let's have a Oh. Oh, I expected What? What? Why is it in a just a Where's the

**Dave Jones:** I assumed it was like a water radio boy or whatever, but it maybe it's just the internals. Anyway, we've got some RF goodness here. This is obviously our uh our antenna. We've got some RF magic happening inside that can. Obviously,

**Dave Jones:** and like I loved a little grounding thing here. This is neat, but where's the Where's the case for this? It's all The guts have been ripped out. Doh, silly me and my marine seismic background. I'm I just assumed

**Dave Jones:** it was a water you know, a water radio sonde, but it's not. This is an airborne one designed to attach to you know, helium balloons. Hence, this is I believe this is its actual package. So, this I believe is

**Dave Jones:** its actual packaging and it would hook up to the battery on the balloon or does it have an internal one? Not entirely sure, but this is its actual packaging. It's got to be as light as possible cuz it's lifted up

**Dave Jones:** into the stratosphere or where it however high it goes on under and underneath a helium balloon and probably just I don't know how they actually deploy it. It just hangs from the bottom designed to take temperature, barometric pressure and stuff like that. So, the

**Dave Jones:** Styrofoam would help keep it at a Well, you know, it's going to keep out the temperature for a bit, but hence why a little probe here. So, is that temperature or is that a barometric pressure probe? Anyway, this is the

**Dave Jones:** transmit here. Of course, that's the antenna and they're designed to be low-cost disposable. They whack these up in the atmosphere and then they just drift wherever and land wherever. And the planet is you know scattered with these. I think people even play games of

**Dave Jones:** trying to like find them, hunt them down and stuff like that. I don't know how long they actually transmit for but if anyone's uh anyone's playing that game, well, where does that How does that attach? I don't know. I've lost it. Anyway, um yeah,

**Dave Jones:** these you know you find them in the middle of fields or they could land in cities or water or you know anywhere. Um and they build them down to a cost. So that is absolutely fascinating. I've always wanted to have a look at one of

**Dave Jones:** those and it like yeah, it's pretty crude but that's all it needs to do is transmit data and you know transmit the data back and you know they'd have a receiver somewhere. I don't know what that chip is. You want a D0863,

**Dave Jones:** is it? So there it is. There's our sensor down in there. So I I you know, what is it? I assume it's like is that just temperature? Hmm, if anyone knows, um please please let us know. Now it turns out

**Dave Jones:** this model the RS80 dates from uh 1981 and it's like it was like is maybe was um the gold standard uh the reference uh transfer standard as they like to uh claim in radiosondes like this. So yeah, I'm sure it's come a long way since then

**Dave Jones:** but um fascinating. Oh, I love how the is soldered into the metal can like that and they've got the penetrators uh coming in the side here, which get the wires through the outer. But look this the transistor onto the

**Dave Jones:** outside. That is That's brilliant. Anyway, what is an NECC 1600? Probably some sort of RFR transistor. Well, I'll tell you what, I cracked the can open and this is fascinating. Look at this. What we've got here, we've got ourselves little inductor. So, this

**Dave Jones:** penetrator comes in, goes through an inductor, then it goes through a capacitor. This is a slug-tuned capacitor from the outside. Basically, well, actually, is it? No, it's Well, it's a slug-tuned capacitor from here to the outer shell, I believe. That's

**Dave Jones:** basically what it's uh what it's doing there. Goes into one lead of the down in there. Of course, the other lead of the transistor is the body itself. You can see that it's been uh the leads been chopped off

**Dave Jones:** there. Then the output of that goes through here. Okay, basically got a It's effectively a transmission line, I guess. Um and then look, there was another piece of plastic on top of here. They're using air dielectric capacitors, basically. It's absolutely fascinating.

**Dave Jones:** So, it loops around here like this and then look, there's another plate there. It AC couples via those two plates to the antenna. That is insane. Wow. And then they've got this going down here and that's going through to

**Dave Jones:** the other penetrator over there. That is absolutely brilliant. Now, there must be uh physical reasons why they're implementing this sort of technique rather than just using components. Now, in the blurb {slash} product brochure for that has a range of products, they

**Dave Jones:** claim that this has new patented stuff for measuring small capacitances and you know taking so there must be like you know maybe they have a patent on this sort of implementation perhaps but I'm not sure you know maybe you can get a

**Dave Jones:** patent on the implementation maybe but not air cord you know air dielectric capacitors and stuff like that in shielded enclosures that's you know I mean you know it's not rocket science but it's interesting why they must have implemented

**Dave Jones:** this sort of thing it must be because the environmental temperature extremes are probably too much for your regular capacitor so they just relied on this air cord stuff so I don't know if anyone's got experience in this sort

**Dave Jones:** of field please let us know how something like this would perform in extremely low temperatures compared to say you know traditional ceramic NPO caps and stuff like that let us know cuz there's a there's definitely a reason why they've

**Dave Jones:** implemented it like this and you know I shot like it's not in 81 it's not recent but still there'd be a particular electrical reason why it was implemented like that but there's not much in it that's basically all it is is

**Dave Jones:** just an RF transistor oscillator that transmits but absolutely fascinating physical implementation I love it and what that chip there chip there is doing it's obviously like they're obviously modulated it might be a custom ASIC modulating the temperature or whatever

**Dave Jones:** they're actually what this particular probes actually measuring I believe it that's normally temperature barometric pressure stuff like that that they're actually measuring so maybe two parameters with the one sensor or maybe it's combined I'm not exactly sure what's

**Dave Jones:** going on there, but anyway. No, looks like no, they've just got the two two wires going out to that with the shielded back in on it. Hmm, interesting. So, there you go. Always wanted to have a look inside one of those things and

**Dave Jones:** there I wonder how much they actually cost to build cuz they are designed to be disposable. They're not allowed to use any you know any sort of you know bad chemical batteries or something like that. So, I believe they have a special

**Dave Jones:** battery in them which probably works in low temperatures. They're not designed to you know pollute the environments that they land in and stuff like that, but yeah, I'd love to like maybe compare a modern one, but this is one from you

**Dave Jones:** know like a state-of-the-art reference standard one you know industry standard one from 1981. Brilliant. Hi Dave, have fun. Scope evaluation kit. I most certainly will. Think your scope can measure up? Let's find out. I've got an oscilloscope evaluation guide. How DPO speeds

**Dave Jones:** debugging because the digital phosphor oscilloscope is the technology used in the tech scopes and this is what we've got here. Data, clock, square wave, reset pads, and ground. Hook it up to a 9-V battery, plug it into your scope,

**Dave Jones:** and Bob's your uncle. You can get various uh test signals that show you know glitches and probably other stuff to do with the DPO troubleshooting XY displays. How DPO speeds debugging and there you go. It's all there. It's all there. Technical reference.

**Dave Jones:** You've got to like that. There's informative tech application notes. I'm sure you can now just download them from the website. The DPO breakthrough, the digital phosphor oscilloscope technology, the power of DPX, and everything else. It was great back in

**Dave Jones:** the day, but of course everyone every man and his dog's doing it these days, but yeah. Let's try this out. What I'm using is a Tektronix MDO 3104 mixed domain oscilloscope. It's the follow-on to the DPO, the original DPO technology scope.

**Dave Jones:** So, it's got the same sort of thing in here. I've got it hooked up to the clock and data. And for those playing along at home, this is the data communications test setting with eye diagrams. And I've set it up exactly like this with the

**Dave Jones:** infinite persistence. And basically, it's designed to show the difference between the DPO and the regular DSO acquisition. After an hour, it'll only collect 300,000 blah blah blah. May not have sufficient to you know to detect any timing violations

**Dave Jones:** and stuff like that. And of course, this is a classic test. And I've got it set to infinite persistence here. And if you clear the persistent I it did capture one. You probably saw it there. So, zoom in on the screen. And you know, you sit

**Dave Jones:** here, wait for a while. It's not doing the business. So, what we'll do is we'll do fast acquisition on, which is basically the DPO technology. You'll notice it switched to the record length of 1K. So, it's only got 1,000 samples.

**Dave Jones:** Bingo. We start capturing all the little timing violations, set up and hold violations on the signal. But of course, the trade-off here with that high waveform update rate, the DPO technology fast acquisition, is of course that 1,000 sample limit. So, if

**Dave Jones:** we stop that and then we actually zoom into that, we don't have much detailed data at the there at all. So, unfortunately, that is going to be the trade-off. But hey, at least it lets you see that there's something wrong there. Once you

**Dave Jones:** see it, aha, got you. And then you can investigate your design. You know you've got the set up and hold violation or whatever it is. You've got a glitch or whatever. So, yeah. It's a reasonable demo. All right,

**Dave Jones:** shoot-out time. The Tektronix MDO 3104 versus the Keysight InfiniiVision MSO-X 3054. So, let's do clear persistence on both of them. I've got all the same settings, and of course, you don't have to set any mode. You know, there's no like fast

**Dave Jones:** acquisition mode or anything on the Keysight scope. It just does the business. You don't have to specifically turn on that fast acquisition mode like you do on the Tektronix. So, if we clear the persistence on both of these, bingo.

**Dave Jones:** We've got them hooked up, and we're well, we're starting to find them over here. We're starting to find a couple here. Sorry, I've got them both set to 95% intensity up here, but these ones just aren't as pronounced as here, but

**Dave Jones:** they're showing up. It's pretty pretty equal, but they aren't capturing exactly the same thing because the trigger point is going to be different on each one. So, but yeah, we're getting in a similar number on both. I don't know. Let's try

**Dave Jones:** that again. Clear persistence. Boom. And they I think they come up a bit quicker on the tech. Uh no, it depends. Once it like it's a random thing. So, you know, they're pretty equivalent in that respect. And if we take a lower-end

**Dave Jones:** scope like a $400 entry-level model, but this is still a pretty quick scope, 50,000 waveform updates per second, GW Instek GDS-1104B for the 100 MHz jobby, but it's got that zinc FPGA in there. It does like 1 meg point

**Dave Jones:** FFT really quick. It's very nice, but yeah, where I've had it running for just since I started this clip, and we haven't picked up any yet. Whereas we can clear the persistence here. Here we go. Between the two and

**Dave Jones:** we're not picking up any yet, so that's to be expected. That's the difference between one of the lower end scopes and one of the really higher end scopes with DPO you know type technology. But this isn't a fair comparison cuz the GW Instek was

**Dave Jones:** running at one meg points. Let's put it to a thousand points that we've got on the MDO 3000 here. So exactly the same record length setting and we got one. We got one. Look at this, it's coming up.

**Dave Jones:** So let's just clear the persistence on both of these. How do I do it? I hate changing scopes like this. It's really rather annoying. There we go. Okay, clear persistence. Boom and it they started coming up straight away. It's

**Dave Jones:** almost as good as the Wiz bang DPO technology, the fast acquisition in the Tektronix MDO. But that's what you get with a thousand points. Of course if you increase the memory, it's not updating as often. The waveform per second figure is not magic. If you

**Dave Jones:** have the longer record length, then you know, you can't help it. But look, that works a treat. Anyway, thanks for everyone who sent in stuff to today's mailbag. I still got some more stuff and I did have a camera

**Dave Jones:** that I shot as well that came in the mailbag, but I think I'm going to do a separate teardown of that well. Yeah, separate video explaining how a digital SLR camera works. So hopefully I'll do that in a separate video. I just

**Dave Jones:** didn't want to it was a bit too much detail for the mailbag. Anyway, hope you enjoyed it. Catch you next time.

**Dave Jones:** Mhm.
