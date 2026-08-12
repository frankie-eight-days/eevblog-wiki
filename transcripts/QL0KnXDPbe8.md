---
video_id: QL0KnXDPbe8
title: EEVblog #366 - USB PSU Troubleshooting
url: https://www.youtube.com/watch?v=QL0KnXDPbe8
source: youtube-asr
---

**Dave Jones:** Hi, just another quick video on the USB power supply. Now, I know this is completely out of order. I haven't done the schematic or I haven't been through the schematic and the design decisions and everything for this yet. Don't

**Dave Jones:** worry, I will get on to it. So, I know it's completely out of order, but I was just troubleshooting this thing or well, I was about to. It needs some troubleshooting cuz I've hit a bit of a snag with the DC-to-DC converter down in

**Dave Jones:** here. You um seen a previous video of me soldering that thing and it's a bit of a drama. Now, I've gotten to a point where caught, you know, I thought, "Oh, yeah, I soldered everything together." I thought it all works, so I did some

**Dave Jones:** firmware and of course, I got a hello world going. Here it is. Ta-da! Hello world. So, it all works. So, the firmware works beautifully, but the DC-to-DC converter in there doesn't seem to be switching on. And well, I thought

**Dave Jones:** I'd troubleshoot it. Might as well switch on the camera. Let's go. Now, of course, the first thing I suspected here was this pain in the ass little 0.5 mm pitch leadless chip, which we've looked at soldering before. They're a real pain in

**Dave Jones:** the ass. So, I thoroughly inspected that. I even took it off and replaced it and well, no, it it exactly the same issue. Now, I'll show you what's actually happening. I've got ground down here and let's probe the input. If you have a look at

**Dave Jones:** the circuit there, this is the input to the DC-to-DC converter on this inductor here. You'll notice that it's 5.14 V, okay? So, that's across C24 there. That's the input side to the inductor, pins 10 and 11 of the chip there. And of

**Dave Jones:** course, you can't really get down and probe the exact pin on the chip. It's not like, you know, an SO one where you can't actually probe the pin down there. So, you know, you've just got to inspect it and rely

**Dave Jones:** on the fact that, you know, you've inspected the joint and and it's all good. But, we can do some resistance measurements. So, let's switch the meter over here and let's uh first of all well, actually, no. Sorry, I didn't finish showing you what the

**Dave Jones:** problem was. Here we go. So, the problem is we've got 5.14 V on the inputs here and we've got on the output 5.142 exactly the same voltage on the input and output of the inductor there, which shows that the

**Dave Jones:** switch pins seven and eight there of the IC are not switching to ground and this uh DC-to-DC converter is not switched on. I don't even need my oscilloscope there to probe that switching point to see if it's switching or not. I know

**Dave Jones:** it's not switching. It's the exact same DC voltage. So, clearly that DC-to-DC converter is not turned on. Why? And well, um what I suspected is that it may have been something to do with Q two around there and I've been I've actually played

**Dave Jones:** around with the software in here. I've been playing around for a little while and so, what I decided to do is short out Q two and that's exactly what I did. Just take that out of the equation and I

**Dave Jones:** replaced R2 under there. Sorry, yes, R2. Um it's supposed to be 12K, but I actually replaced it with uh 51K just to eliminate that uh Q2 control aspect from the DC-to-DC converter. So, it should as soon as you power it up and

**Dave Jones:** apply 5 V to the input, it should give you, you know, a much higher output voltage. It should boost it up, but it's not. The output voltage and of course, we can see the drop on the diode here as well. Okay, here's

**Dave Jones:** the input voltage 5.143 5.143 and then the output side of the diode here is 4.98. So, because the rest of the circuit is going to draw some uh you know, some current. So, uh we've got a voltage drop across our diode there.

**Dave Jones:** It all looks quite reasonable. So, going to actually do some resistance measurements here. Let's switch it over. And of course, the output's not going to be shorted. The output of the diode there, the power rail uh VR there, that

**Dave Jones:** one's not going to be shorted at all. And you can measure it. It's jumping around. You know, we can auto range that to sort of um you know, give us like a ballpark of what's going on there. But, it's

**Dave Jones:** definitely not shorted. Okay? So, it was confusing the auto ranger there, mucking around. It does that sometimes on various meters. Um this Fluke is no exception. Now, uh let's measure the feedback point, which is pin for look at the schematic,

**Dave Jones:** pin three, which is um the uh six in there. Where is it down? Down there. That will be the feedback pin. And there you go. Once again, it's jumping.

**Dave Jones:** Up. There There we go. The feedback pin is roughly 10 K. And you'll notice that R6 there is 10 K to ground. So, it's just under that. So, there's impedance there. You know, there's impedance in parallel across that due to the feedback pin of

**Dave Jones:** the chip. Everything's just fine. And if we measure the VR rail, which is the output voltage, which is here, with that point, let's So, let's probe that. And what do we get? Uh it's it's a bit low. It's supposed to be 51

**Dave Jones:** K. But, that could be the input resistance of the uh the input impedance of the chip. I swapped the leads around. So, there could be something loading that down. No, that's There we go. Yeah, I it's climbing. I

**Dave Jones:** mean, it's supposed to be uh 51K, but, you know, it's got all sorts of uh stuff in parallel with it. So, really, um uh that like there's nothing shorted there. Doesn't seem to be anything open. Seems to be working just fine, but this

**Dave Jones:** stupid thing does not start up. Now, I've actually looked at this uh under the microscope multiple times, and it uh definitely I mean, it might look a bit messy. There's lots of flux residue there. I've been mucking around with the

**Dave Jones:** soldering on this thing, but it it trust me, it actually looks quite good. So, it's facepalm time, folks. Can you see the problem? I can see I just found it. I've been looking at this for quite some time.

**Dave Jones:** I've double-checked things to make sure the components were in the right place, and well, I've overlooked it. Check it out. Look for C26, which is the capacitor, which is the uh bypass capacitor on the upper resistor R2 there. Where's C26?

**Dave Jones:** Down here. It's C26. What? Fail. I've bloody idiot. I've put a 10K resistor in there. 103, there it is. I That is supposed to be a 100 puff uh uh bypass cap for the upper part of the voltage divider for this DC-to-DC

**Dave Jones:** converter. So, I've put a 10K resistor in there. What an idiot. So, that's actually if you follow the trace in because it goes that goes through to here and then that point there goes up under the up through under the diode

**Dave Jones:** there around to here through this resistor. So, it's in parallel with that 51k. It's in parallel with that uh what is it? R2 there. It's in parallel with R2. So, that's it's supposed to be 51k, but it's 10k in

**Dave Jones:** parallel with 51k. No wonder this bloody thing is not starting up. Unbelievable. Uh man, I've looked at this multiple times, would you believe it? And I did not see that. Couldn't see the forest for the trees. That's what happens when

**Dave Jones:** you try and check your own stuff. Murphy will get you every time. What a pain in the ass. Man, I've been think I've been changing this chip and I'm inspecting it and scratching my head and doing all sorts of stuff. And there it

**Dave Jones:** is, a simple stupid component in the wrong place. Soldering iron time. Well, that was pretty darn embarrassing. Man, I thought it'd be something more obscure than just a stupid idiotic mistake like that. But due to Murphy's, I absolutely missed it. Actually, I

**Dave Jones:** won't power that up yet. Let's uh measure the resistance of this uh point again. You know how we're getting what? 8 10k or something 8k before. Basically, we're just measuring um R2. There, there we go. No, it's uh it's all over the shop. It's

**Dave Jones:** jumping around. It's confusing the auto ranger there. Let's uh take that. That's 600k. Let's put it there. That'll do.

**Dave Jones:** There we go, 30 charging up. Boom. No problem whatsoever. And that should eventually Well, there we go. It's going to settle on about 40, but it's Yeah, we'll get in, you know, 8 or 10 K before, which was kind of a a dead

**Dave Jones:** giveaway, really, with the hindsight, but um you know, it could have been the feedback pin on that uh chip there causing or you know, other stuff causing an issue um to measure R2 in circuit like that. And uh well, you know,

**Dave Jones:** But there you go. Um so, we've replaced that. It should be good. So, let's power this thing up. That should start. I think we're expecting about 7.6 V out or something. Uh because it will be uh 51 K. Um it's

**Dave Jones:** the upper resistor divided by the lower resistor. So, 51 K on 10 K plus one times uh the reference voltage of the DC-to-DC converter, 1.245 V. Um let's see what we get here. 5.1 V in and What? Fail. Still fail. 5.11 V

**Dave Jones:** out. This chip is still not going. Son of a Well, I just went and inspected and reflowed that chip again. I'm absolutely sure it uh you know, there's nothing else wrong now. Yeah, I was absolutely sure before, too, when

**Dave Jones:** the stupid resistor was in the wrong place, but anyway, uh let's give it a go. Output voltage. Hey, bingo. 8.14 V. Uh oh, actually, that's Yeah, that's higher than the predicted value because um the transistor is still uh in place shorted out. There's R26

**Dave Jones:** down there, which goes off to the rest of the circuit. If we actually lifted uh 26 there, uh uh got rid of the rest of the uh circuit, we would find that it would be on spot-on to the predicted

**Dave Jones:** value. Hey, why not try that? Got the soldering iron. All right, I've removed uh 26 there, and we should get reasonably close to our predicted 7.6 V. Should be a bit of tolerance there. That's our output. There we go. 7.723,

**Dave Jones:** near enough. I'm using like 5% resistors or something horrible in there at the moment uh for that 51K. So, that looks like uh it is working an absolute treat. So, there you go. That's uh two uh things there is

**Dave Jones:** the uh bias, the you know, the personal bias when you're inspecting your own circuits. I simply did not see that resistor in there. That uh That one down in there. Just didn't not see it. If we attempt to have a look at the

**Dave Jones:** joints of that chip under the Mantis microscope here, they look quite decent. Good enough. And uh but they looked like that before I reflowed the things as well. So, you know, obviously it didn't take on the chip somehow. So,

**Dave Jones:** just something to watch out for. Real pain in the butt. When in doubt, reflow. So, there you go. That was a pretty easy, trivial fix in the end. And uh a classic mistake there. There were two uh mistakes. The first one was I simply had

**Dave Jones:** the wrong component in there. I stuffed a resistor in there instead of a capacitor. My brain was elsewhere when I was populating this thing. Uh happens all the time. And of course, it was right next to a capacitor, which I,

**Dave Jones:** you know, I didn't really look at the circuit thoroughly and actually go through it step by step and well, I've said it before and I'll say it again. Do not assume anything electronics. I thought that might you know, that capacitor I think I know what

**Dave Jones:** my mindset was there. Oh, this capacitor was the one that was the bypass capacitor in the circuit and no, I didn't look at the designators there and I had the wrong one. Absolute classic and of course the other one was

**Dave Jones:** soldering this pain in the ass .5 mm leadless uh chip. Real mongrel. I just had to reflow the joints in there before I actually got the thing working. But hey, it's working now. I I don't trust this package any further than I

**Dave Jones:** can throw it. If I'm getting issues hand soldering these things, I don't know what's going to happen in production. Not getting a good vibe. I may end up changing that sucker. I don't know, but anyway, for now, it works and uh there

**Dave Jones:** you go. That's a little troubleshooting of the USB power supply. There'll be a lot more videos to come. Trust me. I just want to get this thing up and running first actually doing what I want before I go

**Dave Jones:** through the whole design aspect of it. I know it's a bit back-to-front, but stick with me. We'll get there eventually. Hope you enjoyed it. Catch you next time.
