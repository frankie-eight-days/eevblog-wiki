---
video_id: 5DJmp6iA1FE
title: EEVblog #539 - RFID Tag Card Repair
url: https://www.youtube.com/watch?v=5DJmp6iA1FE
source: youtube-asr
---

**Dave Jones:** Hi, just a quick impromptu teardown video of one of these RFID cards. This one is actually the card to access my lab here in the EV Blog corporate towers and it has been slowly failing over the last week or two if you've been

**Dave Jones:** following my Twitter updates and now it is finally dead. I had to get a new card and yeah, like for a while I had to sort of like bend it in this direction like this with my thumb No, actually that was

**Dave Jones:** about the sweet spot right there and with my thumb with my finger like that I sort of got it down to a fine art in the end because when you're you know stuck in the lift you know trying to get up after hours

**Dave Jones:** and it yeah, you learned how to sort of do it but it is finally dead. So there's obviously some sort something cracked inside some bond contact or or something like that with the die inside or you know, I don't know but yeah, something

**Dave Jones:** has certainly intermittent inside this card and yeah, like it wouldn't wouldn't go in that direction. I had to specifically be on this face here with this angle with my tongue at the right angle and I'd finally get in.

**Dave Jones:** Anyway, it has died so I thought I'd just crack it open and see if we can see anything inside. Now, I tried to copy this card and I do have a 125 kHz reader and I believe the system we've got here

**Dave Jones:** and and this card is a 125 kHz card but I have to actually go down to the car park to verify that and I will do that at the moment and I will do that right now after this shot actually just to

**Dave Jones:** verify that it's 125 kHz. Anyway, the reader I've got couldn't actually copy the thing. I believe this might it might be a HID brand 125 kHz card and apparently there is a lot of trouble copying the HID card. You can Uh, it if you get a

**Dave Jones:** specific reader that cost big dollars and they claim to do it. I don't know, but the generic reader I've got claims to, I think, do some variation of HID 125 kHz card, but it certainly could not read this one. So, it was no good. All

**Dave Jones:** right, I'm down in the car park and about the only time that something like this little DSO quad will actually be useful, I think. I'm just going to check the frequency of this thing and see what we get. See whether or not it's the one

**Dave Jones:** 125 kHz frequency readers cuz I don't know. So, let's Sorry, I can't hold this at the same time, but hey, there we go. Probe. I've got the right There we go. That's a 125 kHz one. I'm just using the probe. Sorry. Not like that

**Dave Jones:** and set it to 5 microseconds per division and there we go. So, there you go. It was a 125 kHz card and uh, reader. So, let's crack this thing open and see what we get, shall we? I mean, you should just

**Dave Jones:** be able to Oh, yeah. There we go. Should just be a cover, I believe. Hopefully, it's not potted on the inside, but hopefully, like we should usually you can just peel these things peel these things off and uh,

**Dave Jones:** access the Oh, yeah. Yeah, there we go. There's There we can see the coil already. Oh, look at that. Too easy. We're in like Flynn, almost. Well, let's not count our chickens yet, but anyway, let's open this thing up and tada! There

**Dave Jones:** we go. I can just peel peel that back. Might even be able to fix it. There's our chip in the corner. So, I don't know. So, that me having my thumb over here was a bit out, but there's not much doing in these, of

**Dave Jones:** course. There's the big coil. This is specifically for the 125 kilohertz cards, of course the 13 megahertz cards will be entirely different, but uh I'll get my macro lens out, but maybe the solder joint has come off in there.

**Dave Jones:** That'll be an easy Oh, look, there it is. Look. Is that broken? Yeah, look, I can see it. It's broken. I might actually be able to fix this sucker. Beauty. There's the culprit. There we go, the coil is actually The wire is

**Dave Jones:** actually broken off from the base of the coil. It's probably on the underside there. I'd have to flip it open. Really fine. I'm not sure how many turns are on this thing. I don't know. If anyone wants to get in there and count, there

**Dave Jones:** could be multiple layers, but there's you know, many, many dozens of turns on this sucker, that's for sure. There's our chip there, completely got. There it is, and uh no, you know, apart from depoting that, we're not going to see what's inside that sucker,

**Dave Jones:** but yeah, basically the way these things operate haven't If you don't know how these RFID systems work, basically there's a carrier frequency, in this case 125 kilohertz, which is picked up by the coil, and then that generates voltage in there, which then powers the

**Dave Jones:** chip, and then the chip can communicate. It's in this case it's got like a specific ID number in there. All these tags are individually ID'd, so they can track which person comes in and out. And then what it does is just remodulate the

**Dave Jones:** coil back so that the reader can pick it up, and that's called back scattering, and that's how it is able to send, you know, a small amount of data back to the reader. In this case, probably just the

**Dave Jones:** ID number, and that's that's most likely it. So yes, these things don't need any internal power, of course. They are passively what's called a passive reader. They are powered from the 20 125 kilohertz signal from the coil. And

**Dave Jones:** we've got a rough and ready diagram of roughly how this thing works inside the card. There's a coil, of course, couple of, you know, couple of dozen turns, couple of hundred turns, uh depending on the particular card and

**Dave Jones:** frequency, and a uh parallel cap there forming an LC uh tank circuit. And then from that, we can actually uh tap off uh both the voltage, of course, there's going to be a rectifier, which I haven't showed here to rectify the uh voltage to

**Dave Jones:** generate some DC to then uh power our little chip. And then we've got a modulation transistor directly across the coil. Now, it doesn't essentially short it out. It just basically either, you know, the coil is uh damped properly

**Dave Jones:** or undamped depending on how uh well, the state of the transistor. And and the chip just feeds back to feedback its data. All it does is just turns that transistor on and off, one and zero. And that then modulates, amplitude

**Dave Jones:** modulates, the um carrier frequency like that, which then the reader over here can have some smarts in it to actually read back and decode this data. But that's pretty much all it does is changes it between one and zero, changes the modulation of the

**Dave Jones:** 125 kHz carrier frequency. And that's how the chip in here is able to send data back. It And also this generates the clock as well. The 125 kHz frequency here also generates the internal clock for the chip as well to send data back.

**Dave Jones:** Fantastic. And of course, there's various uh modulation schemes here depending on uh which one, you know, the various uh standards or manufacturers have different types. So, the data could be encoded uh certain ways. So, that's probably why the um our reader that

**Dave Jones:** we've got here can't read this particular uh type of card or that HID card cuz they probably use a um you know, an encrypted or proprietary algorithm or something like that. And that's why they uh, sometimes give it

**Dave Jones:** the term backscatter modulation because we're modulating the signal coming in and then the sort of we we just get the reader here is just getting the backscatter modulated signal from our RFID tag. Well, there really are quite a

**Dave Jones:** few terms in that sucker, that's for sure. And I have been able to find the other end of that coil. There it is on the bottom side. And, uh, I can actually Oh, yeah, you saw it there. You can't see it again

**Dave Jones:** now. I didn't break that, it's just the angle. Um, hopefully I can, uh, peel that back up and, uh, uh, scrape that cuz this is enameled, uh, copper wire. Of course, you got to take off or you got to burn off the en-

**Dave Jones:** enamel, uh, from the outside of it, but, uh, yeah, I probably can rejoin that sucker. All right, I'm looking through the, uh, times eight lens on my, uh, Mantis here. Sorry, it doesn't, you know, work very well, but you can see the size of those

**Dave Jones:** wires compared to my tweezers here. So, anyway, I can't, uh, uh, uh, strea- you know, I can't uh, scrape off the enamel on these wires, so I'm just going to burn it off with the iron and some solder.

**Dave Jones:** Not the best way to do it, but it's going to be good enough for the purposes here and we'll try and burn that off and get some solder to take on the end of that enamel wire there. I think we may have

**Dave Jones:** Yeah, I think we may have got it. Beauty. And there you go. I have actually been able to solder that wire back on there. It's absolutely tiny. In comes my Swiss Army knife blade. It's tiny, but, uh, yeah, my soldering

**Dave Jones:** iron accidentally hit hit the plastic there. Oops. And, uh, that is repaired. So, it should probably work again. And I just went and tried it and yep, what do you know, it works a treat. Um I didn't expect to uh you know, I

**Dave Jones:** expected the odds of being able to repair this quite low. But first of all, I expected it to be uh potted, but it wasn't. And uh next I expected the uh because where I was applying seemed to be applying pressure, it seemed to um

**Dave Jones:** indicate that the uh that the chip was in the middle and it certainly wasn't. And uh yeah, it was off to one side. So, I don't know, you know, the angle of how it was making contact, I have no idea.

**Dave Jones:** But uh it wiped uh finally died. So, the construction of this thing is, you know, um a pretty piss-weak considering, you know, these things are designed to be like credit cards to go in your wallet and they bend and all sorts of stuff.

**Dave Jones:** You know, I expected them to be uh potted or have some, you know, they've obviously gunked it a little tiny bit around there, but not much at all. So, uh when I put this back together, I think I might uh you know, put some

**Dave Jones:** silicone and in there and I gunk all that up before I put the uh cover back on and uh well, hopefully it'll last a little bit longer. But there you go. I was uh quite happy with that. Nothing to

**Dave Jones:** see in here, of course. It's coil and a uh potted chip. Yeah, sorry. But anyway, I was able to repair it. So, I thought I'd shoot a video. Why not? Catch you next time. WAIT, STOP THE PRESS. I'VE ACTUALLY GOT

**Dave Jones:** another card here. It's an old uh HID uh prox card, too. I had uh from a former company I uh worked at and uh there it is. HID Corporation. And uh I thought we'd just take the cover off this, see

**Dave Jones:** if it's any different. Here we go. Once we get that off, should be able to Oh, yeah, yeah. Here we go. We can access the coil on this one, too. Geez, aren't any of them potted? I'm sure I've opened some in the

**Dave Jones:** past that have been potted. That coil is really stuck down on there. That one is uh yeah. Ha. May not come off in one piece like the other one. Lot more stickiness. But before we destroy it, I just thought I'd

**Dave Jones:** try it on my um card reader here, my card copier, which uh doesn't work for my card. And um well, press the read button, and no, it doesn't work at all. I mean, you press the you know, the uh

**Dave Jones:** cards that you can um the generic cards that you can buy, and of course, you can read those and copy them, no problem whatsoever. But, this one and uh my one uh for the building, no, not compatible at all, even though it is 125 kHz. And

**Dave Jones:** there you go, that's the 125 kHz waveform I captured, 100 mV per division there, captured from that card copier. And there you go, yes, it did stick to the adhesive, not to the inside of the uh card there. And yes, this one

**Dave Jones:** actually does have its uh center more towards the center like I have seen before. So, this is an a genuine HID prox card, but I don't think we're going to see much interest in there. Now, that looks for all the world like the bottom

**Dave Jones:** of it, so we'll see if we can uh get that up and uh flip it over, perhaps. Ah. Oh, I just chopped the wire. Who cares? Not going to reuse this sucker. Up, and that one is blobbed as well. Sorry, folks. Huh.
