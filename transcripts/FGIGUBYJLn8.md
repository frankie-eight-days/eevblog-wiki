---
video_id: FGIGUBYJLn8
title: EEVblog #914 - Sony VAIO UX Micro PC Teardown
url: https://www.youtube.com/watch?v=FGIGUBYJLn8
source: youtube-asr
---

**Dave Jones:** Hi, welcome to tear down Tuesday. It's retro computer time again. Not that retro. We're talking about uh 2006-2007 vintage Sony Vaio. And look at this thing. Um it's a pocket Well, it's a portable computer. Sony's idea of what people wanted in a

**Dave Jones:** portable computer in 2006. Um Intel x86 architecture. Uh so, it is actually a PC. It's got Bluetooth, wireless LAN, and it's got uh dual camera on it. The the Sony Motion Eye on the front and back like this. It's got

**Dave Jones:** speaker and it can do all sorts of wiz-bang stuff, headphones, external mic, everything else. And this pretty horrid slide-out QWERTY keyboard. The feel on this is just awful. Um thank you very much to Chris for sending this into the previous mailbag segment.

**Dave Jones:** Obviously, it's uh seen better days with the screen there. So, it doesn't work. Got a button missing up here. It's all cracked around here. And well, let's see what this puppy has to offer, shall we? It's the UX series. And this is the UX

**Dave Jones:** 280P VGN-UX280P for those playing along at home. It's got the Sony Memory Stick Pro, the choice of champions back then. Is anyone still using the Sony Memory Stick anymore? Anyway, it's got a capture button for the camera. And it

**Dave Jones:** got a pretty terrible uh battery life of only a couple of hours, Chris said. And really, it was you know, $2,000 up to 2 1/2 thousand dollars, something like that. It just completely missed the mark and it flopped. Nobody wanted a PC

**Dave Jones:** in this kind of form factor. And you know, you just got to think about the design meeting where they came up with this and what people wanted. I don't know, maybe they hired some focus groups or something like that

**Dave Jones:** and yeah, this is the result. Anyway, you know what we say here on the EV blog, don't turn it on. Take it apart. Wrong screwdriver. Hang on. Maybe one of those. Yeah? No? Probably I we might need a

**Dave Jones:** little teeny top ones. Here we go. Don't turn it on. Take it apart. We got one USB port on here and look at this. Looks like we have a SIM. Wow, look at that. It had everything. 64K smart chip singular.

**Dave Jones:** I've got no idea. Is that a service provider in the US or wherever Chris is from? Um I don't know. Hmm. So this is what's known as an ultra micro portable computer and well, yeah, I can't recall anyone ever actually

**Dave Jones:** using one and Windows XP and you know, it probably did okay, but you were limited by the tiny little piss ant screen on the thing and the really horribly probably not very usable uh QWERTY keyboard. Anyway, let's try

**Dave Jones:** and take this apart. Does it have the usual Sony arrows on there? Hmm. Anyway, we'll find out. Oh, it just had four screws there. Don't tell me it's that easy. It is that easy. We're in like Flynn. Check it out. All we've got is

**Dave Jones:** one cable going up here. What's that? That is that could be for an antenna, I'd be assuming cuz that feels like a coaxy type cable and we've got the uh got the building hard drive. None of this newfangled solid state rubbish

**Dave Jones:** Toshiba. Thank you very much. And that's a 40 gig 4200 RPM drive and that's just going to come out. Presumably that was uh upgradeable. So any uh we'll undo that, but yeah, we're going to see lots of tight integration inside this thing,

**Dave Jones:** no doubt. And we can see lots of tons of flat flex ribbon going everywhere already. So, there's our mic down in there. Is that in it? Yeah, it's got a little rubber Oh, it just What? It like it's been chopped. What the

**Dave Jones:** What on earth? Anyway, yep, that's been chopped. Um it does have a rubber surround on it, which just start stops vibration coming through when you're holding it and stuff like that uh coming through to the mic. That's always a nice

**Dave Jones:** touch, but you'd expect to see that. I am not sure what this is going to this little flat flex here. It's just flapping around in the breeze and it doesn't seem to mate up with anything on this. So,

**Dave Jones:** what's doing there? Look, I just tried to take out the hard drive bracket there and I'll tell you what, this whole thing everything looks very very modular. That's obviously our uh Wi-Fi module there and well, yeah, there goes the uh

**Dave Jones:** antenna. No, there's our Wi-Fi antenna cable up there. So, we got uh Bluetooth and Wi-Fi, of course, but looks like this whole whole lot just might lift out. It's going to be very very modular, but it's tightly packed. Nice

**Dave Jones:** fit to envelope design, that's for sure. Nothing wasted. They've got a rubber surround on the hard drive here, stopping the uh noise and vibration there. So, that's a That's a real nice touch and also impact cuz you're going

**Dave Jones:** to drop you're going to end up dropping this thing. It's uh So, you want to take that out, absolutely, but uh yeah. There we go. It's going to flip out. Oh, we're in like Flynn. There's our Intel. Is that our

**Dave Jones:** processor? And we've got a fan inside this thing. I wonder if this was noisy. That's a real shame to have a fan inside like a micro PC like this. Couldn't they have just engineered it a bit thermally a bit better and got the heat out? I

**Dave Jones:** mean, you hold the thing you could dissipate it, have an aluminum back or something like that. But, yeah, fan, that's just a uh it's a complete cop-out. I don't Yeah, thumbs down. Apparently, the hard drive is dead. Or it's just pulled dead. I don't know.

**Dave Jones:** Hmm. So, this Wi-Fi module connects to via those flat flexes up under there. I should just be able to in theory, pull those off. I'm This is not going back together. So, if it does it come out? How does that It

**Dave Jones:** slides out. There we go. Slides in like that. Trap for young players. So, yeah, that's all very nice. And there's the wireless module. It's an Intel Pro Wireless 3945 for those playing along at home. I'll tell you what, someone's had

**Dave Jones:** a crack at this hard drive. Look at that. Oops. Turns out that is not our processor. That's the IO controller. That's the Intel ICH7 U series. Now, that does pretty much everything the processor doesn't do. It does USB, IDE,

**Dave Jones:** audio, the flashing in the face, PCI, clock, power management, you name it, it's in there. That for all the world looks like a magnesium alloy frame. So, that's very nice attention to detail. I thought this was really interesting to

**Dave Jones:** begin with. I thought, "Oh, look, they've got this USB connector surface mounted. They just put it in there and they just relying on the pressure of the pads to hold down the USB." But, no, it's actually been The pads have been

**Dave Jones:** ripped off and that wasn't me. Hmm. And they've got some customy expansion type header probably going to some docky type thing down in there. And you flip that away. And bingo, there's our power circuitry, dead giveaway with the

**Dave Jones:** big-ass inductors there, the tantalum caps, and everything else. So, that'll be generating the five or half a dozen different rails we need for this silly thing. And sure enough, this whole thing does actually flip out if I uh

**Dave Jones:** get rid of that ribbon cable there. Just a few things tying it in. We've got a ribbon cable down on the bottom, down in there. It's uh There we go. We're There we go. Look, that all comes apart

**Dave Jones:** brilliantly. It's a fantastic modular design. There's our fan. Okay, so that was coming out the bottom there. There's our uh grill down there. So, that's a little squirrel cage fan, and look, we've got ourselves a copper heat pipe coming over

**Dave Jones:** here from our processor is almost certainly under there. That's the thing that's getting hot. I mean, that's why they didn't get much battery life out of this thing. It was running hot. Technology wasn't good enough, and well, yeah, and you got a

**Dave Jones:** few hours use because just got too hot. You got to get the power out. In a micro PC? Nah, poor choice. So, you got to ask, were they limited by the processor technology at the time, or did they try

**Dave Jones:** and push it too hard and get too much performance out of this micro PC? I don't know, you know, were their hands tied? Okay, we have to put this in this micro PC form package. We have to put

**Dave Jones:** the fan in, and we need this amount of cooling, and everything else. Anyway, they haven't wasted a huge amount of space in there, so that is uh very nice indeed. And if we flip this puppy up, ah, there's all our memory.

**Dave Jones:** Bingo, down in there. What brand? Nanya. So, there's our GSM phone module. There's our SIM socket it there, and then we've got a Sony uh Ericsson EE52 Uh phone module, and I guess that answered the question where does that little

**Dave Jones:** What was on the back here? That's the antenna. That's the GSM antenna right in there. And it looks like they had an external GSM antenna connector there, is it? Strange looking. Actually, if you take the cover off there, that coax is

**Dave Jones:** just going up Yeah, to that external connector there. So, uh where is the Where's Wally? Where's the regular GSM antenna? Hmm. So, you can go and decode those DRAM numbers if you want, but that's going to be Yeah, I believe this

**Dave Jones:** model was 1 gig. So, that's just enough to run Windows XP on a device like this. It Yeah, it'll work. All right, let's lift up this and get a look at our processor. There it is. We have another

**Dave Jones:** big Whoop. Yep, we had a little thermal pad on the bottom of there. That just connects down to that baby down there. Don't know what that is, but there's our little copper Is that going to Yep, that's going to

**Dave Jones:** pop off. Let's remove that, and we're in like Flynn. There we go. There's our copper pads. There's not paste on the bottom of there. They got themselves a big thermal pad. Look at that. That's actually quite thick. So,

**Dave Jones:** yeah, that's going to have a bit of loss in that anyway. Does the business. Here we go. Let me show you a close-up. Okay, it's quite difficult to get the number on this one. So, excuse me, but I've had a

**Dave Jones:** look at it under the mantis, and it is This is the 945 GM Express chipset. So, this is the memory controller. No surprises that it's right next to the memory here, and graphics as well. It's not fancy pantsy graphics. It'll do VGA,

**Dave Jones:** and you know, not much else really. So, it's designed for mobile devices like this. But yeah, Um, It's a bigger die than the processor. Look at that. The physical die itself, bigger. And there's nothing on the die there, but if you

**Dave Jones:** look up LE80538, you actually get a um, Celeron M215, but it's not that. But if you actually go to the Intel website and do a search for LE80538, you get what matches this one, the U1500. Or it's actually If you look at

**Dave Jones:** the Wiki page for this uh, Sony product, then you actually this model is supposed to be the U1400 at uh, 1.2 gig, but it's obviously the U1500. So, I don't know, they upgraded or Wiki's wrong. Wikipedia could be

**Dave Jones:** wrong. Anyway, 1.3 gig, it's nothing special. It's designed for, you know, mobile devices like this. It's got a pass mark if you're into that sort of thing at 327. And, meh, you know, it it's good enough for the job in here,

**Dave Jones:** but obviously not low enough power to get away with that heatsink. And audio there for those playing along at home, not too fussed about that, but uh, that's pretty much all she wrote. Looks like we've got some uh, core power

**Dave Jones:** supply stuff happening around here for the processor, but for this main board, that's basically it. So, we've got the processor, uh, graphics and memory controller, main system memory. We've got our uh, IO controller over here. What's this puppy?

**Dave Jones:** Did we look at that? I can't remember. Well, that's a real surprise. That's a Renesas H8S series 2 111 16-bit micro. What's it doing there? As sort of like some system system glue processor, miscellaneous stuff. I I wouldn't have expected to find another

**Dave Jones:** 16-bit micro on there. That is fascinating. Hmm, any guesses? And that one tucked away in there is a Texas Instruments PCI 8412. It's a card bus controller. And that ICL 9LPR321, not exactly sure. Couldn't pull up anything that at first uh

**Dave Jones:** sucker the sav, but um yeah, if I can, I'll pull something up. But by the looks of it, there's our crystal. Uh look, we've got uh termination resistance coming off here. So, I would say that is some sort of uh

**Dave Jones:** clock driver clock gen. Wow, this module here, I swear I didn't do anything. I It has that like What What the What's going on? What on earth is going on there? It's There is no connector. What? Huh? Anyway, you guess what that is. That's

**Dave Jones:** the Bluetooth controller, the UGP uh Z6 there. Um but How does it connect? I'm This is bizarre. Under that plastic cover there, there's our antenna for you antenna aficionados. Here you go. Isn't that a Bobby Dazzler? Ooh, nice and symmetrical. So, now I've

**Dave Jones:** separated the screen from there, and uh there's nothing much else doing in there. Yeah, who cares what's going on there? We've got our uh Sony memory stick interface. Nothing much doing it down there for the Bluetooth interface, and that would just be going over to the

**Dave Jones:** lousy keypad on there. Surely the keyboard might be interesting. Look at this. Ta-da! There's our tactile domes. There we go. And we've got some LEDs to light up. Do we? Looks like it. But yeah, they're pretty wimpy tactile domes. I

**Dave Jones:** mean, this thing basically has almost no tactile feedback. It's It's pretty horrible. You can Ah It It was It's It's better when you when you don't have this on it and you can actually get your finger right around

**Dave Jones:** the key like that. They should have actually had it like that. Cuz when you put this on, it it it's like your finger hits the surround and it it just feels like there's nothing there. You take that away and it's actually a half-reasonable

**Dave Jones:** tactile response. For those who don't know how they manufacture these, they actually just put the pads down on there and you get the tactile domes embedded in there like that. They're little uh snap domes. You get them from companies

**Dave Jones:** like uh Snaptron, for example. Uh make uh really good ones. But yeah, they just sticks over the front like that. Easy peasy. Now, I've actually uh looked into these um for how small they can actually make the pitch between these. And I

**Dave Jones:** think I was trying for 5-mm pitch or or I don't know. It was something some ridiculously small uh pitch for my uh Mark II scientific calculator watch. And I went to the manufacturers of these uh tactile dome membrane uh overlays and they were just

**Dave Jones:** going "Nope. Nope. Too small a pitch." And yeah, that's like bleeding edge stuff and things like that. So, yeah, if I had the luxury to have one this wide, jeez, I would. Look at that. That's That's pretty jazzy. I like that.

**Dave Jones:** And this is where the mechanical engineers have to come in again to develop this slide-in mechanism, which hopefully comes off. Oh, I didn't take the screws off. I swear. There's some screws embedded under there, but uh yeah, there's a lot of disciplines of

**Dave Jones:** engineering which go into developing this thing overall, let alone just the display module. It'll come out somehow. Oh, screws on the side, I think. Ta-da! We're in like Flynn. Well, kinda. Sharp. There you go. Sony didn't uh roll their own there. They uh Sharp are

**Dave Jones:** one of the leaders in uh LCDs, so they obviously developed uh the controller, and of course that would be a Sharp LCD as well. You can see the Ooh, I like the little snaky flex going off there. Isn't

**Dave Jones:** that cute? Um we'll flip that up and move that out. You can see the uh hot bar attachment there. Classic hot bar uh technique going over to the flat flex. They would have uh chip on board uh chip

**Dave Jones:** on flex uh drivers here for the actual uh LCD itself. And there's our speaker, and one of those uh finger printy readers, is it? They were yeah, pretty crusty, but yeah, anyway. Gimmick. And they've got one camera there on that

**Dave Jones:** board, and then they have another board here, which board-to-board interconnect goes to our second camera on the uh yeah, that's the back. One or more of US patents. Well, yeah, that looks like more than one to me. And

**Dave Jones:** that's a Sharp display model number for those playing along at home. And looks like they've really stuck that board down with some uh double-sided tape. That is really They've gone to town on that. Anyway, there's nothing more to see there. As I

**Dave Jones:** said, there would be um chip on uh flex uh drivers under there for the uh rows and the columns, and I don't know what resolution screen that is. So, there you have it. That's a look inside the uh Sony UX280P

**Dave Jones:** or VGN-UX280P micro PC from uh about 2006 to 2007 vintage and I believe it was pretty much a flop. I stand to be corrected but if you had one of these and you thought it was the ducks guts or if you're still using one,

**Dave Jones:** let us know. Anyway, I hope you're going to appreciate the amount of engineering that goes into this thing. I mean, it's not just electronics designers, you know, designing the circuits, laying out the boards, everything else. Just the fit to envelope mechanical engineering

**Dave Jones:** design that went into this. There was very little wasted space, the systems engineering and everything else involved in this thing, the thermal engineering. We've got you know, the graphics and the mechanical displays and the keyboards and the slidey screen and the whole kit

**Dave Jones:** and caboodle. Um, that it's just incredible amount of engineering. Must have taken a lot of different discipline teams to work on something like this and get it going. And how you would actually start off designing something like this. My guess

**Dave Jones:** is that what they'll come up with the shape concept like this and then they would go, "Right, yeah, this is what we want. We want ourselves a sliding screen and we want the keyboard. We want it to be able to hold it like this so you can

**Dave Jones:** use your thumbs like this and the screen slides up and we want Wi-Fi and we want Bluetooth and we want GSM and we want this processor and we want this and that and hard drive and all sorts of uh, you

**Dave Jones:** know, requirements would come out of that and then the system designers are going to go, "Right, scratch your head. Right, how do we fit in this? Well, let's start with our base board like this but our processor takes too much

**Dave Jones:** power so we need to engineer a thermal solution for it." And then that's got to fit inside. We need a battery. What What is our battery solution going to be like? That'd be the one of the first things that could change during the

**Dave Jones:** design process. They could go, "Oh, look, we uh we were really good at fitting everything in and we've got more space. So, let's put in a bigger battery, for example, or something like that." So, that could have changed or it

**Dave Jones:** could have gone we need Maybe they wanted a bigger battery and then uh the systems designers went, "No, we don't have enough room cuz you bloody gave us this processor. We need to put in this thermal solution and we need to do this

**Dave Jones:** and you wanted all this sort of jazz. We don't have the room. You're going to have to make the battery smaller." And that could have you know, rather than throw their hands up and scrap the project and go, "Ah, no, this isn't

**Dave Jones:** going to work." They just go, "Okay, let's do a smaller battery. We'll just change the specs for the battery life. Who cares if it's not good enough and people aren't happy with it. Whatever." There's so many design decisions that go into producing

**Dave Jones:** something like this and it is absolutely phenomenal. So, my hat's off to the design team. I love these um Sony teardowns. They do systems engineering really really well. So, anyway, hope you enjoyed that. If you did, give it a big thumbs up and all

**Dave Jones:** that sort of jazz and discuss down below. Catch you next time. Hi. Welcome to a hopefully short teardown of this Sony E-mount lens here. This is from my NEX-5T camera. Here we go. Oh, there we go. Yeah, look. Hey, whoa. Woohoo. Yep.

**Dave Jones:** There we go. Hey, it's rotating. Op. That's great. Wobbling the camera a little bit and and look, I'll actually pick it up and start shaking it around. And there you go, you can see the steady shot.
