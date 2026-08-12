---
video_id: IVnOy8dYBkA
title: EEVblog 1643 - DON'T BUY this Cheap 7kW 32A EV EVSE Charger
url: https://www.youtube.com/watch?v=IVnOy8dYBkA
source: youtube-asr
timestamps: {"0": 0, "1": 31, "2": 55, "3": 83, "4": 111, "5": 139, "6": 166, "7": 185, "8": 199, "9": 226, "10": 241, "11": 271, "12": 292, "13": 318, "14": 351, "15": 381, "16": 406, "17": 435, "18": 466, "19": 476, "20": 503, "21": 530}
---

**Dave Jones:** Hi, it's teardown time of another super cheap EV charger here. And uh we've got a new energy charger. I think it goes under multiple brands. And this bobby dazzler cost me 190 Aussie bucks. Uh not sure how much it is in Yankee land, but yeah, it's got the Aussie 32 amp connector on it. You've seen that in my install for my Zappy charger. So, I wanted a portable 7 kW charger. And I've I'll link it in down below and up here if you haven't seen it. I've done a

**Dave Jones:** teardown a review video a super cheap 15 amp jobby. So, 3.3 kW or thereabouts, which I do actually use, but I wanted a 7 kW one and this was the cheapest thing I could find. So, we're going to tear it down and we're going to give it a test and see what it's like. It's got the standard type two connector on there. There you go. No worries. Not that Tesla rubbish.

**Dave Jones:** And the first thing I note is that the cable here claims to have two uh 6 square millimeters plus a 0.75 square millimeter earth in there. Plus your control lines as well, but it doesn't have any certification or rating on it. So, is it even like real copper or is it, you know, a lot of companies will replace copper with aluminum these days and they have like copper coated aluminum. So, sort of like fake copper cables. I don't know. So, so let's tear this thing apart

**Dave Jones:** and see what's in it. Now, I've also got a video which I'll link in and you have to watch that. If you don't know what an EV charger is. I'm using quote marks here cuz this is not a charger. It's what it what is called an EVSE or an electric vehicle service equipment. All it is is basically just a smart little controller in here. They got a nice little graphic screen here. And what it basically does is sends out a PWM control signal on the control line here

**Dave Jones:** to the car to tell the car how much power is available from in this particular case the 32 amp connector on here and you can the big A button here allows you to select different charge current. So, yeah, might be 10 amps, you know, 16 amps, 32 amps, that sort of thing. We'll find out when we actually uh power it up. But, yeah, the basically the only thing inside this is a a couple of relays which uh connect the mains directly through to the uh car because

**Dave Jones:** the car is the thing that actually contains the proper charger for the battery inside the car. So, this thing is not a charger. It's just smart little doohickey box that just sends out a PWM signal and uh it has some earth protection and uh stuff like that. But, it's basically just a smart relay box, really. There you go. Claims uh IP66 rating, so you can kind of like use it outdoors in the rain um up to uh 32 amps uh max and um yeah, claims to meet some

**Dave Jones:** standard, but let's take it apart. Get the rubber feet off here and we've got four machine inserts here, so that's nice. No, that's self-tapping rubbish, so that's good. And bingo, there we go. Is that just going to just going to pop off?

**Dave Jones:** The grommet's going to stick. I don't know what the Yeah, there we go. The front comes off and yeah, it's um quite similar to the one we had before. Not as good not as sexy as the previous one I looked at, I don't think, from memory.

**Dave Jones:** Um that looks pretty basic, doesn't it? There's not much in there at all. So, they've got the control board up the top. That's neither here nor there. Anyway, uh yeah, the LCD is uh soldered down to uh the flat flex ribbon just down there and that's a STC micro, is it? There you go. You can read that at home. I'm not going to bother. But, this is what it's all about. Anyway, I like the uh clamping on the input and the output. That's really nice. No worries

**Dave Jones:** there whatsoever. Is there a shake-proof washer there on those? Anyway, I like the uh crimping. It's not too shabby at all. Oh, no, that thing up the top here, that was not a I thought that was a like a little micro switch. It's not.

**Dave Jones:** It's actually a like a cable thing. They got the same thing down here and it's a little cable clamp like that. Neat. Anyway, um basically, yeah, so we got a common neutral here and they're just relaying the the positive there. I can't remember if the previous one did that. I'm going to have to check my teardown. Yeah, I put up a photo of the other cheap one that I had and it had two relays in there. One for the active and one for the neutral and it had a

**Dave Jones:** core balance relay as well. But if we look over here, there's no core balance relay. So they haven't got the active and the neutral going through the relay. They're only measuring the current there on the neutral side of that. So So yeah, I think they're that's how they're getting the cost down on this thing. They're skimping a bit.

**Dave Jones:** Anyway, some nice isolation slots down in there. So they're doing all the requisite stuff. It's just a simpler design. So I'm not sure about the various standards, but looks like we've got a a cover over our relay. What's going What's going on there? Yeah, that's kind of odd. It's almost as if it like it has a like protective case around it. So I'm not going to try and get that off cuz it looks like I'm going to break it.

**Dave Jones:** Anyway, that's an 80 amp rating. I don't know that brand. It's not a Hongfa which is traditionally used in you know, a lot of EV charger designs like this. So And there's our power supply there. That's just our isolated converter there for powering the electronics. So it comes out here and you can see the ground going all the way around like that to the low side basically. And then we have a high voltage series string of SMD resistors there. They put them in series to get the high voltage, of

**Dave Jones:** course, cuz they're only like, you know, 150, 200 volts max rated each. So, you whack them in series, and that's how you get a cheap high-voltage resistor. I'm going to try and peel back some insulation on there and see what's what. All right, does that look like copper to you? That looks like copper to me, so Uh yeah, I think I'm going to call copper there. Anyway, it's the how many hundreds of strands in there cuz it is a very flexible. Now, for the 32-amp standard, it should have

**Dave Jones:** a 220-ohm resistor approximately on the proximity pilot pin and earth here. So, let's measure that. Yep, there you go. No worries. And this thing should contain an energy monitoring chip. Uh doubt they're all doing it in the micro, so that's our micro. So, I'm guessing that's the chip down there. Let's see if we can get in there. There you go.

**Dave Jones:** There's our number down there. I'll put the data sheet up. That should be an energy monitoring chip. So, basically, this is an absolute bare-bones penny-pinched design, and I'm not sure if it's even compliant with various standards. I mean, it's legally sold presumably legally sold here in Australia cuz I bought it from an Australian supplier. But yeah, it's only got the single relay, whereas I thought you were supposed to dual relay isolate them. Not going to Not going to go into the various standards and might be

**Dave Jones:** different in every country and every situation and everything else, but yeah, basically, only got the single active switch in here. They're not isolating the negative. So, if you have this plugged into your car, it's it's permanently actually connected through It's got no earth leak internal earth leakage protection at all. So, you're relying on the external circuit to do that. Once again, not even sure if that's actually technically compliant at all. So, yeah, I mean, it's going to work. It's going to do your basic thing. I'm going

**Dave Jones:** to test it on the EV and I'm sure it will get you out of trouble in a pinch. But I got to give this one a thumbs down and I guess it's well, you get what you pay for.

**Dave Jones:** So yeah, it'll get you out of trouble in a pinch, but it's probably not something that you want to use on a permanent basis. I don't think. So yeah, that's a fail. Unlike that previous my daughter brand one which we looked at. So I'm not sure if this is common in these 32 amp jobbies at all. But yeah, so I'd have to get another brand to do a comparison. So yeah, now is the official verdict on this one. It's going to work. I'll do a quick test at home

**Dave Jones:** and plug it in to the EV. And yeah, it'll get you out of trouble, but yeah, no. You definitely get what you pay for in these EV chargers. Catch you next time. All right, does it actually power MY IONIC EV? WELL, LET'S TRY IT. I've got it to installed on my 32 amp outlet here. And well, here we go. Let's plug her in and see. And yeah, there you go. 32 amps.

**Dave Jones:** Yeah, there we go. 31.6 amps, 7.6 kilowatts. Um it works. It's very night ridery.
