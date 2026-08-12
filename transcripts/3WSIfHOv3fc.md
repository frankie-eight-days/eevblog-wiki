---
video_id: 3WSIfHOv3fc
title: EEVblog 1484 - Kaba Mas X-09 High Security Electronic Lock Teardown
url: https://www.youtube.com/watch?v=3WSIfHOv3fc
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 29, "3": 40, "4": 50, "5": 73, "6": 88, "7": 101, "8": 124, "9": 134, "10": 155, "11": 163, "12": 178, "13": 199, "14": 208, "15": 221, "16": 229, "17": 246, "18": 255, "19": 264, "20": 276, "21": 291, "22": 302, "23": 319, "24": 335, "25": 359, "26": 367, "27": 391, "28": 406, "29": 412, "30": 433, "31": 452, "32": 465, "33": 481, "34": 495, "35": 503, "36": 517, "37": 528, "38": 542, "39": 563, "40": 583, "41": 608, "42": 619, "43": 635, "44": 654, "45": 665, "46": 680, "47": 694, "48": 710, "49": 722, "50": 742, "51": 757, "52": 781, "53": 800, "54": 815, "55": 827, "56": 840, "57": 851, "58": 864, "59": 876, "60": 888, "61": 905, "62": 919, "63": 932, "64": 942, "65": 956, "66": 964, "67": 972, "68": 989, "69": 1012, "70": 1028, "71": 1040, "72": 1051, "73": 1065, "74": 1086, "75": 1099}
---

**Dave Jones:** What is it? I guess we're going to take this top thing apart and figure out what this sensor is. Um but like there's no ca- Oh yeah, no no no, I was going to say there's no cables going to it.

**Dave Jones:** There's a little ribbon going down there. So I Aha, I thought the name Kaba rang a bell. Yes, Kaba actually uh manufacture um high-security electronic locks um for safes and other, you know, vault doors and other high-security installations and stuff like that.

**Dave Jones:** And that's what we've got here. This is not a stepper motor. This is a This is the back part of this safe lock. So that goes inside the safe, the part you want to uh secure.

**Dave Jones:** And outside here you have what looks and feels like uh your traditional safe um tumbler. So this Kaba XO9, uh which I believe this one is and probably the X10 is probably uh the same.

**Dave Jones:** And this is designed to simulate the look and feel, the user interface of a tumbler lock, but actually make it instead of a having a mechanical uh lock on the back, you know, you spin it uh you know, four times this way to the right number and then you spin it three times in the other direction to the right number and then two and then one and that will open the uh your

**Dave Jones:** traditional uh tumbler lock safe lock. Well, this one simulates that but with an electronic interface. And I was uh thinking, well, where where are the numbers? You know, you usually have like zero to 99 around here and like an arrow so you know exactly where you're turning it to.

**Dave Jones:** Well, this up here looks like it's actually an LCD. So it looks like it would actually display the number and this would be mounted on the front of the door, of course, either a safe door or other uh door.

**Dave Jones:** It's mounted in like this. You All you've got between them is a couple of ribbon cables like this because um this won't have any active electronics in it. Because in a high-security electronic lock uh you want to minimize the um attack methods and I've done a whole video on, um, electronic, uh, safe locks and, uh, trying to actually, uh, do a side channel attack on them.

**Dave Jones:** So, it looks like there's actually two So, no, three. There's three ribbon cables inside this. Just tiny little a couple only a couple of, uh, three or four, uh, pins each or something.

**Dave Jones:** So, this would have an encoder in it, which then, um, sends the signals down, uh, to here and then, uh, the microcontroller inside the actual lock, uh, part of it will, uh, decode, um, you know, how many times you spin it this way, how many times you spin it that way and I would assume it's going to display a two-digit number on there.

**Dave Jones:** It wouldn't be any more than that. Uh, wouldn't be any less. So, a two-digit number so that has the same look and feel as a tumbler lock. So, this is really cool.

**Dave Jones:** But, it looks like, check out down here, somebody Somebody's had fun. Holy Toledo. Somebody had fun. They've obviously attempted to drill into this thing, um, to get it open.

**Dave Jones:** So, is Did this come from like a, uh, an attempted cracked, um, safe or something like that? Because if you don't know any, uh, decent safe will actually have not only the safe door sits in between here and it could be, you know, a huge hardened, uh, steel safe door or, you know, a vault door or, uh, something like that.

**Dave Jones:** That's why it's so wide. It can have like a really thick, uh, door like this. Um, but they'll often have, uh, like manganese is often, uh, used as like an anti-drill plate on here.

**Dave Jones:** I don't think this would actually have actually be like a manganese, um, steel anti-drill, uh, type thing. Obviously, somebody's able to drill into this thing, but you can integrate those into, uh, safes.

**Dave Jones:** They'll have like an anti-drill plate that actually, uh, dulls the drill bits as you try and, uh, drill through them. And the safe or vault doors often, uh, they won't be like large solid steel.

**Dave Jones:** They'll have a, you know, a decent amount of steel in them. Might be, you know, 10-15 mm worth or something like that. But inside they often contain like Duralin compounds in there, like a material that actually dulls your drill bit if you try and actually drill through.

**Dave Jones:** Because if you try one of the attack methods for safes is to actually drill through like, you know, you you could rip this thing off the front. You can pry it off.

**Dave Jones:** But then you can actually drill through the door. And if you drill through in the right location, here is the Can we pull that out? Yeah, here's the locking bolt that comes out.

**Dave Jones:** And if you drill through in the right location, you can actually get through and either, you know, did all the mechanism in there that holds this bolt in place and actually retract it, pull it and retract it back.

**Dave Jones:** And that's how you would get in via a drill attack method. And another attack method might be to try and like feed in like, you know, high voltage into here to try and back power the electronics in here and then open the solenoid that way.

**Dave Jones:** Cuz this has an electronic solenoid in it. And if you apply power to the solenoid, boom, the latch comes out or goes back in. So, yeah, that's one of the other attack methods.

**Dave Jones:** But these Kaba locks, this is, you know, a really expensive, probably high security, meets, you know, probably, you know, international security standards and stuff like that. So, this would likely be very expensive, certified, probably incredibly difficult if not impossible to actually um hack.

**Dave Jones:** I don't know. Leave it in the comments if you know if this Kaba X-09 has actually been hacked. So, you know, really, unless you know the combination or you can attack the door or the safe some other way, you ain't getting in there.

**Dave Jones:** And one of the other methods for getting into safes would be magnet, of course, because the solenoid is operated magnetically. So, you know, you get a big ass magnet like next to if you've got a real flimsy safe door and stuff, like you can maybe put a large magnet in the correct big neodymium magnet in the correct location and it can actually open the solenoid, but you know, your high security

**Dave Jones:** certified ones would not be vulnerable to those sort of magnetic attacks either. So, let's take this part and see what we've got. So, this is the front spinnery thing.

**Dave Jones:** I don't know how you would enter the numbers like this. Can you Is that going to Is that going to push? No, I think maybe you just like you know, spin it until it gets to a number and then you wait and for a second and then you'd reverse direction and then you would reverse direction again and it knows which number it gets to on the display here and then this thing like

**Dave Jones:** will just continually spin forever and the microcontroller in here would do the decoding and display your number on here for the user as they enter. So, you know, it just simulates the look and feel, but anyway, so that is interface to there.

**Dave Jones:** If we crack this open, so if we get all this off, that comes off. So, that's just designed to go in the shaft and that just goes into the top there.

**Dave Jones:** Very nice. It's got a seal around there, weatherproof rubber baby buggy bumper seal on there. That's nice and then inside here, here's your interface. So, that would be your encoder to actually encode that and it looks like it just goes into, yeah, a zebra interface down here.

**Dave Jones:** Zebra strip and last America connector like this and that just interfaces. So, they go to a lot of effort in there to sort of like interface the rotary encoder here with that and then we've got a couple of other ribbons here which go into this little board.

**Dave Jones:** There's no electronics in there. That's just a interface. We can take the yep, we can take the whole lot off. Up here will be our display. Uh Yep, that comes out like that and there you go.

**Dave Jones:** Yep, that's right. That's just an LCD. So, I'll have to put up the I'm assuming I can get a manual for this thing and yeah, it'll have the indicator of what's on here, but I reckon that's going to be a two-digit display to simulate the look and feel of an old traditional tumbler jobby.

**Dave Jones:** So, as you can see, there's no electronics in there at all cuz you don't want any attack methods into the lock by having the electronics on this side. It's just a rotor encoder here and the LCD that gets the feedback.

**Dave Jones:** So, you know, it's not like you can like override you know, you can tap into the LCD pins and then try and get into the micro controller that way.

**Dave Jones:** Although, I guess in theory that might be possible for a power line attack or something like that perhaps, but I got to a think that, you know, a big reputable certified brand like Kaba would have you know, thought of that sort of thing.

**Dave Jones:** But, anyway, in theory like a maybe a like a power line attack might be possible as well cuz you got these access to these ribbon cables, but all you got to do is like filter on the other side and Bob's your uncle.

**Dave Jones:** So, if we open this up, you can see what's in there. We've got ourselves a shaft here which comes through and this piece just fell out and it looks like that goes into the inside right in there.

**Dave Jones:** That looks like it's sheared off there. So, that would be part of the bolt that comes out there. So, this would be looks like your little motor solenoidy thing that just moves this arm up here which then moves your plate out like that and then that's what locks your door, of course.

**Dave Jones:** So, all of your strength is in this bolt here, but of course, if you look inside a safe, you're like a large safe, you'll see that this then pushes on Um, big armatures which then might have, you know, three or four big bolts, huge big, you know, 30 mm diameter jobbies that then go into the side of the safe.

**Dave Jones:** So, this just like pushes on, uh, you know, a big mechanical arm inside here. I'll see if I can get a, uh, photo and, uh, put one up. So, this might get, you know, on a small safe, this might be, uh, this here might be the only mechanical thing that, you know, prevents the safe, uh, from opening, but this can actually, um, be extended out into uh, larger things, uh, depending on

**Dave Jones:** how, uh, you want the installation, um, in whatever size safe or vault door or whatever you're doing. And here's the PCB, and you'll note from the shiny shiny, that's all potted, completely potted for, uh, moisture ingress.

**Dave Jones:** Then we've got this thing here which presses in, and I originally thought that this might have been like, you know, if you press the front of this, this is how you enter a number, and then that presses on that, but it's not because the shaft actually goes in here like this.

**Dave Jones:** So, yeah, that looks like it goes down into there somewhere. So, I'm not sure, I don't know, is that an anti-tamper, um, thing or not? I'm not sure whether or not that has something to do with sensing whether or not this is open, but it doesn't seem to be Right.

**Dave Jones:** Anyway, I won't go into, uh, the full details there, but anyway, we've got ourselves a super cap, and of course, one thing you might be wondering here is how they actually power this thing.

**Dave Jones:** Um, there is no internal battery, and that's what the super cap's for. You might think, are the super cap's, uh, for holding the, uh, combination when it loses power, but no, um, the combination is stored in a secure E-squared, uh, prom here.

**Dave Jones:** That'd be the, uh, micro there. I'm not sure what that other, uh, chippy up there is. Don't know, but anyway, it doesn't matter. So, what I think happens here is I have to confirm this with the manual, whack it up, but it it has to be right.

**Dave Jones:** You know, by deduction, this thing, actually this encoder here, of course, generates a voltage, you know, it could be like a quadrature output or something, but then that can be used, you can actually rectify that and build the charge up on the cap.

**Dave Jones:** And that's why I think they've got this reduction gear mechanism in here. So, it spins this faster and then you can use that, you can rectify that and then store it in the capacitor.

**Dave Jones:** So, what I reckon happens is that you, you know, spin this a couple of times to build up enough power to turn the lock on. So, when you walk up to the door and it's been depowered for a while, you won't see anything on the LCD, but you spin it a few times and I reckon that builds up enough charge in here, you know, for a minute of operation or whatever, and

**Dave Jones:** then as you, you know, spin the dial to enter the combination, it puts even more and more charge in there. And then that's enough charge to operate the micro- controller and also it's got to operate the the solenoid motor thing down here, which then deactivates that.

**Dave Jones:** So, yeah, you can, you know, you have to get a decent amount of energy out of that to power it, but this thing is not externally battery powered. Anyway, I won't go through and look at the details on that board, but suffice it to say this would almost be certainly be a certified to a standard and you probably can't change the firmware at all once you, you know, certify this thing with the

**Dave Jones:** certification authority, they would, you know, you can't change the firmware or anything. If you wanted to do that, you probably have to re-certify the thing, but yeah, anyway, there's the pin interface, which then goes down to the pins down here, which goes through those ribbon cables going over to the front end.

**Dave Jones:** And I was going to say they have multiple ones for redundancy, but it doesn't look like it. That's a five-pin jobby. That's a four-pin jobby. And then another couple of pins then going over another four or five going over to your encoder on the front.

**Dave Jones:** And I'm trying to get medieval on its ass here. But it's like you can see it's all gunked inside there. Trying to get this out. So sorry to all you carba aficionados.

**Dave Jones:** This is probably sacrilege, but yeah, I don't think I like my chances of getting that out intact. Oh goodness. Going to need a bigger boat. Yeah, here we go.

**Dave Jones:** I think I think I got it. Oh, look at that. Oh, wow. Oh, there's all the stuff on the bottom as well. Wow, that's interesting. What were these two pins down here?

**Dave Jones:** I'm not sure what they went to. And yes, we have voided the voided the warranty on this year. There's a It's a little two-pin interface down there. Does that actually Could that be a battery interface?

**Dave Jones:** Maybe I'm wrong about it being self- powered. But yeah, anyway, that's the back of the board. Still can't really figure out what that does. Doesn't Does it do anything?

**Dave Jones:** Not sure that does anything at all. That just might be part of the mechanical. That might be just required for the mechanical interface and the board just got in the way, so they had to put a hole through it.

**Dave Jones:** Um yeah, not entirely sure. But anyway, there is a lot of stuff in there, isn't there? Hey, for one of one of these electronic locks, so yeah, they're quite complicated and yes, they're designed to be not hackable, but maybe in theory there's a way to get through them.

**Dave Jones:** Oh no, look at that. The potting The potting ripped off those poor sot 23 jobbies. Oh no, ripped off some of the board as well. I thought for a second that there was another board embedded in that potting, but there's not.

**Dave Jones:** Well, there kind of is partially, but it was part of this top board. It just It just ripped off a whole bunch of the components. Yeah, you can see why that has that uh exposed copper there.

**Dave Jones:** Half the SA23s are missing. Nice. And there was another little uh coggy thing which uh goes down in there somewhere. I'm not absolutely sure of that, but there you go.

**Dave Jones:** That is a uh Kaba um X09 high security electronic lock for safes, vault doors, um even regular, you know, doors in a high security installation or uh something like that.

**Dave Jones:** And this puppy wouldn't be uh cheap. I'll see if I can find a uh price on this, but uh you're not going to get any change from many, many hundreds of dollars, let me tell you.

**Dave Jones:** Someone's had a hurry hacker at this one. Um unfortunately, we didn't get a note with it, so uh we don't know the uh history of this, but thank you very much for sending that in.

**Dave Jones:** I've got uh really interesting electronic uh safe locks, and these are fascinating things, and there's a lot of engineering effort and certification and testing and standards and stuff that go into these electronic locks to ensure that they aren't um you know, hackable.

**Dave Jones:** That's why there's no electronics on the door um side of things over here with the knob. That's just the uh encoder and the LCD uh feedback uh display. And yeah, I'm not sure like you'd be able to um put any like high-energy, high-voltage pulses into this and then back feed uh the solenoid in here which opens this sort of thing.

**Dave Jones:** They would have been, you know, thoroughly uh tested and certified uh for those sorts of attacks. Of course, your cheap, no-name, OneHungLow brand electronic locks, um yeah, they're not going to be built uh to the same standard as this one, but uh yeah, I'm sure this is why you pay a pretty penny for it.

**Dave Jones:** Um and it doesn't look like a new design, either. Aha, there you go. Scraped off the potting. That's an 8566 Philips um LCD driver. Hard to get the numbers at the right angle.

**Dave Jones:** And this is a Philips micro. There you go. There you go. P something or other 87C something. I can't read it on my camcorder screen, but yeah, that's the micro.

**Dave Jones:** And that's where the code is stored in this thing. I don't see a secure E-squared prom externally. No, it's just internal to the micro. But of course, the whole idea is that you don't have access to this electronics because it's inside the safe.

**Dave Jones:** It's on the other side of that vault. Um and unless you can like drill through and probe it or you know, in theory like do a power line attack over the LCD cable or something like that, then yeah, but it's you know, it's not hard to design out those attack scenarios if you're aware of them.

**Dave Jones:** I'm sure um Kaba cuz they know what they're doing. They're a big name in the business. So there you go. That is a fascinating. I hope you enjoyed that look inside these high-security electronic safe locks as much as I did.

**Dave Jones:** And if you did, give it a big thumbs-up. And as always, discuss down below. Catch you next time.
