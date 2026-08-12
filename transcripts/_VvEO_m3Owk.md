---
video_id: _VvEO_m3Owk
title: EEVblog #389 - Casio Calculator Investigation
url: https://www.youtube.com/watch?v=_VvEO_m3Owk
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 30, "3": 44, "4": 63, "5": 77, "6": 91, "7": 109, "8": 126, "9": 143, "10": 157, "11": 172, "12": 185, "13": 205, "14": 222, "15": 237, "16": 250, "17": 263, "18": 277, "19": 295, "20": 311, "21": 325, "22": 337, "23": 352, "24": 366, "25": 383, "26": 399, "27": 419, "28": 433, "29": 451, "30": 467, "31": 489, "32": 512, "33": 529, "34": 546, "35": 559, "36": 573, "37": 589, "38": 603, "39": 622, "40": 640, "41": 658, "42": 677, "43": 691, "44": 708, "45": 725, "46": 742, "47": 758, "48": 773, "49": 793, "50": 816, "51": 835, "52": 857, "53": 868, "54": 886, "55": 905, "56": 922, "57": 937, "58": 953}
---

**Dave Jones:** Hi, I've done a video quite a long time ago called solar power hope where I looked at solar cells and did some measurements because I was looking at developing a solar powered calculator but as it turns out this piss

**Dave Jones:** ant little solar cells even the best ones on the market most efficient ones on the market could not generate the required current that I needed for the dot matrix display and things and I just got curious I did

**Dave Jones:** measurements on the solar cell itself but I never did any measurements on these solar powered calculators and how much current they actually draw. So, I thought that might be interesting. So, I thought we'd take a representative example a fairly recent

**Dave Jones:** one in terms of these types of Casio's it's the pre VPAM rubbish of course it's the FX 260 solar it goes under other part numbers as well I believe in different countries but this one is fairly recent I don't know it's probably

**Dave Jones:** five or six years old they might even still sell it in places and I thought we just crack this thing open and uh have a look at it because the solar it's obviously got a big cap in it

**Dave Jones:** check it out see if I cover that solar cell up there's obviously a big electrolytic cap in there or something holding on the charge there for quite some time and even when the display blanks like that it's still

**Dave Jones:** still keeps it it's still in there. So, I thought we'd actually crack this thing open and do some measurements and see the actual current consumption both static display and also during calculation if we're able to probe it but I've got lots of calculators if we

**Dave Jones:** can't easily probe this one sure I can probe another. Let's give it a go. And here it is tada look at that we've just got a chip on board classic black blob there. They've got the epoxy coating on that. These Casios

**Dave Jones:** many different construction techniques. I might even take another one apart later and show you like you know a bare die approach or something like that. And there's our solar cell. It's a Sanyo SA1154 and there's not much else in there.

**Dave Jones:** There's the electrolytic cap. Of course that was fairly obvious that I had a large size cap in there and all it's got is two other service mount ceramic caps and that's it. I mean you know there's no crystal, no nothing in this thing.

**Dave Jones:** Obviously a building RC oscillator in this thing. It'd only be running at you know tens of kilohertz or something like that at most. This thing of course is not particularly fast. Let's do something and probably the most complex thing this thing can

**Dave Jones:** do. Let's do 69 factorial. Shall we? It's 69 cuz that's the upper limit of a 99 exponent and you can No, it did it reasonably quickly. I've got slower ones than that but yeah anyway it's not a particularly fast

**Dave Jones:** machine. Incidentally, let's see if that's any slower if we lower that voltage so the LCD dims. It's really quite dim now. So let's do that 69. You can just see it.

**Dave Jones:** And No, it's probably about the same amount of time I think. So looks like voltage has no effect on the speed. It might have a slight effect maybe because of the RC oscillator in the thing but yeah, probably not much but

**Dave Jones:** anyway the good thing about this one is that we can just crack straight into there and power this thing from a bench supply. See where it see what operational voltage range it runs over, and also measure the current. And uh we'll do

**Dave Jones:** that uh we'll also take out the uh supply cap as well, cuz we don't want that um interfering with our uh pulse uh current measurements. Okay, this is the test setup I've got here. I've got my micro current, of course. Classic uh

**Dave Jones:** example for the use of this. I got it on the uh micro amp range, so it's going to give out 1 mV per micro amp. So, I've got the output of that going in to the new Agilent U1273AX.

**Dave Jones:** You haven't seen this uh meter before. It is a newy. Um it's basically exactly the same as the U uh 1273, but it's and with the OLED uh this very sexy OLED display on it, but it's designed to go

**Dave Jones:** down to minus 40° or something like that. Uh That's its only advantage. Anyway, go figure. But, the OLED display is sexy. You probably see some flicker there due to the uh uh frame rate of the video. Anyway, that's measuring the uh current

**Dave Jones:** uh draw of the thing. I've got it powered from a bench uh power supply, and the Fluke 87 here is going to measure the uh input voltage. At the moment, I'm actually measuring the uh solar cell voltage, so it's um 2.62

**Dave Jones:** uh volts there. You know, if I put my hand over it a little bit, drops to 2.5. So, it looks like, you know, 2. I've got like 1,000 lux here on the bench. So, um looks like 2.6 is, you know, the maximum

**Dave Jones:** you maybe you might get a bit higher than that, you know, out in direct sun where you're talking tens of thousands of lux or something, but indoor environment here, about 2.6 V, so we know it uh operates from, you know, 2.6 downwards,

**Dave Jones:** so we'll uh start around there on our power supply and drop it until it dies. So, here we go. I've got the power supply set to 2.55 V. It's not measuring the uh solar cell anymore, it's measuring the bench supply input and of

**Dave Jones:** course it's working just hunky-dory and we're getting it's drawing about three just over three microamps. So, I don't know, I kind of expected it to be a little bit less than that. This thing has an auto dimming mode. You got to

**Dave Jones:** turn it on to get the real sexy bright OLED. Does that to save power consumption, I guess. Um now, it's working just fine. So, let's drop this sucker. Bench supply here until the calculator we're viewing it sort of

**Dave Jones:** almost straight on, maybe a bit above angle, but it's certainly still excellent contrast on that LCD at 1.25. It sort of starts to drop it. Yeah, say about 1. Uh yeah, if you view it down on a lower

**Dave Jones:** angle down here. Yeah, you can It's probably It looks better on camera here, but uh There you go. Let's drop it down a bit further. And uh it's certainly is still usable down to 1 volt. So, yeah, mate. If you You can't see it on

**Dave Jones:** the screen there, but if you raise the angle there, you can just see it. So, it's barely usable at a volt and it you know, under that it's just completely dead. But, at a volt um we're getting about 1.4

**Dave Jones:** microamps. And so, but let's take it back up to two for example. So, 1.4 to 2.6 is not a huge difference in the operational current there. So, let's see what happens when we press a key. Let's see the current.

**Dave Jones:** Three. There we go. It does jump up. Hard to Well, I can set the peak mode on this and see if we can capture the peak of this. There we go. It's beeping away at us. So, let's capture.

**Dave Jones:** Yeah, there we go. It's peaking at like 5 6 It's Yeah, let's try 69 factorial. Wow, there we go. When it was doing that factorial, jumped up to 16.2 microamps. Oh, what a whopper. Let's try that at 2 and

**Dave Jones:** 1/2 V so thereabouts. 69 factorial. Yeah, yeah. Nah, it's pretty much 16 and 1/2 is where it's going to peak. Let's uh zero that out and let's do it again. 69 factorial. Boom. Let's see what happens when it's

**Dave Jones:** say doing a uh doing a log here. Let's do I don't know the log of Let's do the log of 42. There we go. 10.5. So, it's not as high as the uh factorial one there. And if we do say

**Dave Jones:** square root of 42. This is a good use for the min max mode on your uh multimeter. You can capture these peaks cuz it is quite capable of uh getting those peaks. Now, it does a square root really quickly. So, uh there's not much

**Dave Jones:** uh peak in there. It takes more to do the log. So, we go 40 No. 42 log. There we go. Yeah, it definitely takes more current to do a log than it does a square root. And if you watch it

**Dave Jones:** closely, you can actually when I press a key, you might be able to see it capture a uh sort of transition up there on the bar graph there cuz the bar graph updates much faster than the display does. So,

**Dave Jones:** there you go. Interesting. And because the other one doesn't uh, switch off because it's there's no battery and it's solar powered only, there's no off function. I can't measure the standby current consumption. So, I thought I'd get this, uh, Tandy EC-414.

**Dave Jones:** Um, it's a rebadged Casio, of course. I'm not sure of the Casio model number off the top of my head. And when it's on, it's drawing about 3.8 microamps. And when it's off, let me rather than wait for the timeout, I'll

**Dave Jones:** just switch the damn thing off. And, uh, just let's switch down to the microamp range. Sorry, the nanoamp range. And, uh, move this up a bit. There we go. 700, just over 700 nanoamps. And if you're curious to see inside this one,

**Dave Jones:** it's just a quad flat pack. Very traditional construction with, uh, some axial diodes there, actually, uh, hand soldered on. And once again, that's about it. Nothing else. And this is, of course, a, uh, dual power solar battery version. So, we've got our solar cell up

**Dave Jones:** there. And also the battery connection. And I did promise you one with different construction. And I know that this one, cuz I took it apart when I first got it, of course, back in, probably 1987. I think I got this one. These are about

**Dave Jones:** the same vintage. I got this one a year or two possibly before that. Um, so this is, you know, about '87, possibly '88 vintage at most. And it's the, uh, Tandy EC-431. And I know this one has different to, even

**Dave Jones:** though it's the, um, almost practically the same age as this one, which had the quad flat pack, this one has radically different, uh, chip construction in there. So, let's take a look. And there it is. Check it out. I I get the macro

**Dave Jones:** lens out and have a good close-up of that, but it is radically different to the quad flat pack we saw before. And check out this flat flex on here, which has these two diodes. Can I I'm not sure if I can

**Dave Jones:** peel that all the way back. Oh, yeah, why not? Anyway, there we go. Look at that. They've got a flat flex in there just to mount those two diodes on. Very very interesting. So, you can see that there's no PCB in this thing. I

**Dave Jones:** guess they were experimenting with what cost savings they could get with no PCB. And they've gone, you know, the complete flat flex route cuz they knew they had to mount the two diodes on there. So, they decided to

**Dave Jones:** mount them solder them directly to the flat flex, bonded on, and well, look at that. Nothing. I mean, the battery contacts down in there, it's just got your it's just got the flat flex membrane down in there under the battery for the

**Dave Jones:** lower battery contacts. Some of that's actually worn off by the looks of it. And check that out. That is obviously the bottom of the die there. And they've flipped it over and mounted it on the other side because it's clearly the

**Dave Jones:** bottom because you can't see the circuitry on the top of that, the actual you know, the circuitry etched into the silicon wafer. So, it is it is very interesting. I'll see if I can lift this membrane out of here and try and

**Dave Jones:** have a look at the other side of that. Here we go. Let's have a look at this. Check that out. Isn't that absolutely fascinating? Little bubbles in there. They almost look like little vias or something, but they clearly aren't.

**Dave Jones:** That's just uh something trapped underneath the bottom of the chip there, but you can see the individual wires sort of, you know, like a kind of like bonding out from the chip, but they aren't actually bond wires. They're actually impregnated

**Dave Jones:** into the plastic film there. So, they've got a two-layer construction on that. They've got this very They've got this uh Actually, that is That is not Yeah, yeah, it's flexible. It's flexible. So, that is a bit of more

**Dave Jones:** rigid type of plastic. So, they've got that, which is what they mount the chip on. And they So, they flip it over, and it looks like they do actually solder it down to these very fine pitch. I'm not

**Dave Jones:** sure what that pitch is in there, but it's absolutely incredibly fine, I'm sure. And then these come out to the pads along here, which then this is bonded to So, that thicker plastic there is then bonded onto your traditional

**Dave Jones:** uh carbon based membrane there. Absolutely fascinating. If anyone knows what this construction technique is called and or if it's still used these days, please uh leave it in the comments or jump on over to the forum to uh

**Dave Jones:** let us know because it really is fascinating. So, I wonder if this is like uh something Casio were experimenting with at the time and whether or not they still use it. I'm not not entirely sure, but there you go. That is only like a

**Dave Jones:** year or two difference between that uh uh other Tandy one we saw before and this model which in the other one before just used a standard PCB and a quad flat pack. And this one radically different. Absolutely fascinating. So there you

**Dave Jones:** have it for this particular Casio FX-260 solar calculator current draw ranges from you know in the order of uh 2 microamps up to uh 15 or 16 microamps. Uh I expected uh uh a bit less than that actually. I'm a

**Dave Jones:** little bit surprised that it draws that much. But go figure. Anyway, little experiment I thought I'd share. Catch you next time.
