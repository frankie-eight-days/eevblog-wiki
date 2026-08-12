---
video_id: 7Br3L1B80ow
title: EEVblog #1020 - Is A $7 LCR / Component Tester Any Good?
url: https://www.youtube.com/watch?v=7Br3L1B80ow
source: youtube-asr
---

**Dave Jones:** Hi, this is going to be a follow-up video to my previous mailbag one where right at the end of the mailbag somebody sent in this thing which looked like just some no-name generic tester board from eBay. There were like no

**Dave Jones:** instructions, no nothing. There's no labeling on it. Uh you know, it just like what the hell was this thing? And I just sort of, you know, brushed it aside and quite rightly I copped a lot of flak for this. So, yeah, sorry. I should have

**Dave Jones:** at least put it through its paces. So, here we go. We're going to take a look at one of these $7 uh you can might even be able to get it slightly cheaper $7 delivered uh LCR meter {slash} transistor tester {slash}

**Dave Jones:** component analyzer {slash} whatever you want to call this thing. Now, I I was aware that these kind of things existed, but I hadn't I hadn't been following the 156 page EEVblog forum thread on this. That's not post, that's pages. So,

**Dave Jones:** please forgive me that I'm not going to go back and read the entire 156 page thread about these things. Now, this particular one I've found it on eBay and it's the M328, but it goes under various different names and it calls itself you power it

**Dave Jones:** up calls itself the M tester. Um like there's no other like information on here and that's one of the things like I know it's only seven bucks, but is it too hard to actually you know, silk screen on there what this thing actually

**Dave Jones:** does or something like that? I don't know. It would have been handy. Anyway, let's get into it. Apparently, it's a component tester and apparently it's pretty good. These have a big following, lots of fanboys out there and people

**Dave Jones:** wanted me to test it out. So, let's give it a go. This is this particular M328 one and yes, I do have a brand new battery. Cuz if you noticed in the mailbag, if I used one that had a much lower voltage,

**Dave Jones:** which by the way, does not show up like 7.something volts. There you go, the contrast is just unreadable on this thing, even though it doesn't give you a low battery warning error message. So, there's the first problem with this thing. Now, I know that there

**Dave Jones:** are dozens and dozens of variations on these things, if not hundreds of variations on this thing. People put them in their own do-it-yourself housings and all sorts of stuff. I believe the one like the first one was like a a regular two-line 16-character

**Dave Jones:** LCD. This is a particular graphics based one, and we can whack a component in here, and that's what the numbers are there for. It's got three different terminals, and it's got presumably duplicated over here. I haven't tried it for power

**Dave Jones:** transistor pads, and you can plug a component into any part of that, just power it on, and it simply does a test. There it is, a 100-ohm resistor between pins one and three. Beautiful. So, yes, I have no idea what

**Dave Jones:** firmware version this is running, what variant what you know, schematic variant this thing is. It's just a generic eBay M328. So, yeah, take that as it is. Now, one of the first problems I have with this thing is, well, this particular unit in

**Dave Jones:** particular, is the backlight. So, let's switch it on, and it's just like it's pissing away the power. Like, why they need that backlight? I've got a capacitor in there now, 100N. Like, a lot of that will be the backlight. Like,

**Dave Jones:** why? Frustrating. Anyway, this thing is really quite jazzy. Look, if I put a transistor in there, just got one out of the junk in junk bin. What is it? A BD137, I think it is. Let's power it on, and

**Dave Jones:** have a look. And I do like the automatic nature of this. It is very nice. Look at that. It's automatically identified the transistor, which you know, base collector emitter on which particular pin there, and it gives us the HFE and

**Dave Jones:** the forward voltage but at what current I don't know. So, we can actually take that, flip it around, and see if it works the same. You basically got to press the button each time. It just repowers it basically.

**Dave Jones:** There we go. Look at that. Beautiful. So, there's obviously a lot of refinement that's gone into this firmware and and I'm sure firmware is totally different across many different variants of this the countless different variants of this product, but this one I

**Dave Jones:** mean I tried resistors, capacitors, and transistors now and it it's just very nice. So, yeah, huge thumbs up to this. Where this originally comes from, who's writing this code, who's building it, I don't know the history behind this. It's

**Dave Jones:** probably some huge mash-up of code over time. I don't know if anyone's like does anyone know the original developer of this, but I've seen projects like this for going back, you know, decades in the magazines and things like that. So, I I

**Dave Jones:** don't think it's particularly new. And I guess I don't mind the use of a ZIF socket like this for testing. It's okay, you know, like it's fine. Especially for like seven bucks. I remember like seven bucks delivered. I remember when the ZIF

**Dave Jones:** sockets like this used to cost seven bucks and text tool it doesn't have 3M on it, does it? So, it's probably just some yeah, one hung low variant. Anyway, I'm going to try and fool the crap out of this thing cuz I don't know what

**Dave Jones:** range of stuff it test. The I'll plug in a 7805. I don't expect it to work at all. It'll probably confuse it and say it's something else. But let's try it. No, no unknown or damaged part. There you go. It didn't It

**Dave Jones:** went well, that's outside the bounds of what I know about, I only know about these particular parts and it doesn't test like any of them. So, that's pretty groovy. Don't mind that at all. Come on. Can't fool it. Can't fool it. Surely,

**Dave Jones:** it's going through all its routines. No, it doesn't know what that is. Nice. Does it know what a red LED is? There you go, you can see it pulsing. Ah, there you go. It well, it says it's a

**Dave Jones:** diode, which is exactly what it is. Um, it's just a light emitting diode and uh 2 volts and it says it even gives you the capacitance for the diode 4 puff. Isn't that jazzy? So, I'll just repeat that. I turned it around and put it in

**Dave Jones:** different ones. Yeah, that's pretty repeatable. Nice. Green diode there. Sweet. We'll try a VN10K MOSFET here. But, what? Fail. It thinks it's an NPN transistor. Hm. So, that's interesting. It knows it's acting like a transistor, which it is. It's just a MOSFET. Um, and

**Dave Jones:** it is an N-channel MOSFET. So, it's got that right and the HN, it knows that the gain is massive, but it hasn't identified that it's actually a MOSFET instead of a bipolar. And as for capacitors, it just gives us

**Dave Jones:** capacitance, but I had it before, it was showing up what's called V loss, which it was 0.1%, which I like I can't get it to do it again, but I swear it came up. There it is. 0.1%. So, I

**Dave Jones:** assume that's the dissipation factor. So, let's compare that with a real LCR tester and see what we get. 94.8 at 1 kHz, I believe the test frequency is. Yeah, it's not quite there, but for a ballpark measurements like component

**Dave Jones:** identification, I mean, it's it's just fine. So, I'm not going to quibble over that. And as for that voltage loss there, there you go, dissipation factor, you know, point it said 0.1%. Eh, 0.03, near enough. Aha, it starts to give us

**Dave Jones:** more info if we had put an electrolytic in there. I was wondering if it was going to do the ESR and certainly it does. 1.6 ohms, 48.88 with a 1% dissipation factor. And we're getting 1.6 ohms there, which is pretty good for

**Dave Jones:** the ESR. Once again, for component ID, it's it's doing the job just fine. Okay, so let's try the resistance over a entire range here. I wouldn't quibble over anything less than 1 ohm. I haven't included test leads here,

**Dave Jones:** so that's just fine. 10.8, 101, 1,009, 10.08, 101. Getting a little bit out, but you know, 1 meg still pretty schmick. See if we can do 10 meg. Hey, that's not bad at all. I am liking that. Let's say let's go up

**Dave Jones:** to say something difficult like 50 meg. That's not easy to yet no unknown parts. So, what does it do? Go up to, you know, 20 meg or something? That's fine. That's great. So, that seems to be reasonably accurate over the entire range. Don't

**Dave Jones:** mind that at all. Okay, let's try a big cap 2,200 microfarad electrolytic. Let's go. It's I measured it 1869 on my LCR meter and was at .05 ESR. .18, it's a little bit out. 1965, but like it doesn't matter. I'm

**Dave Jones:** happy with that just for component identification. That's a winner. But you saw it there had .9% V loss and like that doesn't match anything doing with any sort of at 1 kilohertz the dissipation quality factor of this thing. So,

**Dave Jones:** I'm not sure what's going on there. Now, it's supposed to be able to measure MOSFETs, but of course you saw it fail with that VN10K one there. So, let's put in this IRF610 and give that a whirl. I'll be very

**Dave Jones:** impressed if it can, uh, it's supposed to do the, "I!" Wow, okay. Consider me suitably impressed. Look at that. That's impressive. N-channel MOSFET. Even get like and it shows the internal wire diode and let's whack that around like that. Okay, so I

**Dave Jones:** didn't like the VN, uh, 10K one, but it certainly does the business on this IRF610. That's very impressive. And really, you don't care about the parameters that much. It's not, uh, you know, a precision bit of kit. It's a component identifier, um,

**Dave Jones:** essentially. So, you know, that's pretty much all you want. Let's try one again. We've got an IRF9110 P-channel MOSFET. So, let's give that one a whirl. Nice. That's that's worth its weight in gold. And let's do a, uh, desoldered salvaged,

**Dave Jones:** uh, 50N06, shall we? Pretty standard part. Oh, no, it can't handle the, uh, solder on the pins all that well. Let's give that a whirl. Uh-oh. What what what what. Hang on, might not be making contact. Ha! Works a treat. A winner winner

**Dave Jones:** chicken dinner. Okay, let's try a surface mount bipolar here. Got a, uh, 22 22 for those playing along at home. Let's see if we can Ah, that's my LCR meter turning off. So, I'll hold it down on there. I don't like

**Dave Jones:** those pads, but it's obviously working in this case. Neat. All right, let's try a 3.9 V Zener diode. See what we get. Hey, look at that. That is bang on to what you want like it doesn't tell you it's a Zener diode, but

**Dave Jones:** it's implying it's a Zener diode because it's got the forward voltage. Yeah, it's not quite there 3.9 V At these low voltages for these low voltages, then it's going to depend heavily on the test current. So, yeah, don't like that's good enough, right?

**Dave Jones:** And then it knows that the diode in the opposite direction is your standard silicon drop like that. So, from that you can infer it's a, you know, 3.5-ish V Zener. Neat. It's just got another little ceramic cap here, but you can see

**Dave Jones:** that I'll I'll show you that the the dissi- the supposed dissipation factor is going to be, you know, it it's fairly out on this. So, I wouldn't really take that as anything meaningful, you know, 0.6% V loss. It you know, it's near enough on

**Dave Jones:** the capacitance. Just use it for component ID. It seems to be grossly out on you know, depends. Maybe there's a sweet spot of capacitance where, you know, it does fairly well on that, but you know, some I've measured just aren't anywhere

**Dave Jones:** even in the ballpark. And I just did a little little 1,000 micro Henry or 1 milli Henry inductor surface mount inductor there just by holding it on there, and that did a reasonable job. There you go. There's the resistance of

**Dave Jones:** that and the inductance of that at 1 kHz. So, it's pretty close. Nice. And that's a 10 micro Henry inductor, but it doesn't seem to really look at the resolution there. It's pretty terrible. And it can't measure a 1 micro Henry at

**Dave Jones:** all. It just thinks it's a resistor. And well, that's fine. It's got a lower limit. So, there you go. I'm actually very impressed by this little thing. It's amazing what you can get out of just a little ATmega micro, some very

**Dave Jones:** clever software that's no doubt been much refined over time, and a couple of passives and other stuff. There's a couple of in there and a few diodes, you know. There's really nothing to these things, and it you can build

**Dave Jones:** these yourself. I'm just like there are countless designs out there apparently and I'll link in the uh EV blog forum to this thing, all 156 pages of it. So, for seven bucks delivered, this thing is just magical. Um it definitely get one,

**Dave Jones:** but I'd recommend uh like maybe get like spending a bit more and getting one that has a case with proper banana uh jacks on it or something that you can plug, you know, little uh LCR type test leads

**Dave Jones:** into or something like that or you can make your own. You can just buy the bare-bones one like this and you know, get rid of the ZIF socket or even have it on the front panel, make your own

**Dave Jones:** case, do with a 3D printed case, do whatever. Make a little do-it-yourself project out of it cuz these things are quite impressive. Don't use it as a substitute for a real LCR meter to take, you know, quantitative measurements of parts. Um

**Dave Jones:** that's not what this for. It's for, you know, a basically component identifier, go no-go tester. You know, it gives you a ballpark figure. It seems reasonably accurate though for various capacitances and resistances and it doesn't go that low in

**Dave Jones:** inductances and stuff like that, but for transistor identification, like I wouldn't be taking the beta for granted and, you know, stuff like that. So, there seems to be a large community of people actually, you know, hacking around with these things and changing

**Dave Jones:** the firmware and changing the design and, you know, doing their own builds and things like that which is fantastic. So, it's um definitely worth having one of these things in your kit, especially, you know, for the price. If you're on a

**Dave Jones:** budget, then, you know, seven bucks delivered for a component identifier and basic measure, you know, basic measurement tool like this, just fantastic. It almost you know, practically can't be beat. And but there are tons of variations of this as

**Dave Jones:** I said. So, um apparently can well, some others I've read do uh you know, SCR thyristors and stuff like that. I don't have any of those uh handy here, but I it's impressive the amount of components that I can do and can do it like MOSFETs

**Dave Jones:** like that. That's just fantastic. Anyway, hope you enjoyed that. If you did, please give the video a big thumbs up. And as always, discuss down below. Catch you next time.
