---
video_id: 72sJ5Infuu0
title: EEVblog #365 - ESR Meter Bad Cap Monitor Repair
url: https://www.youtube.com/watch?v=72sJ5Infuu0
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 34, "3": 44, "4": 75, "5": 91, "6": 104, "7": 115, "8": 130, "9": 145, "10": 158, "11": 168, "12": 181, "13": 198, "14": 218, "15": 229, "16": 242, "17": 262, "18": 276, "19": 290, "20": 311, "21": 320, "22": 335, "23": 358, "24": 372, "25": 386, "26": 413, "27": 427, "28": 448, "29": 456, "30": 477, "31": 499, "32": 510, "33": 526, "34": 542, "35": 553, "36": 571, "37": 582, "38": 600, "39": 613, "40": 631, "41": 637, "42": 647, "43": 658, "44": 675, "45": 688, "46": 701, "47": 724, "48": 733, "49": 745, "50": 755, "51": 776, "52": 790, "53": 812, "54": 822, "55": 839, "56": 851, "57": 863, "58": 878, "59": 894, "60": 908, "61": 924, "62": 934, "63": 954}
---

**Dave Jones:** And it's junk been time again, and yes, you guessed it, it's another monitor, another non-working one. I found this one inside a box for a new monitor. I saw the empty box there and I thought, "Oh, I wonder if there's anything in it?" Sure enough, there's the old monitor they were replacing.

**Dave Jones:** In this uh instance, it's an LG, Life's Good. Yeah, they changed it. And it's a Flatron W1942 T, 19-in. It's widescreen, so you know, it's it's not that great, but it's certainly worth salvaging.

**Dave Jones:** And I have tried to power it up, and it gave a image briefly for a couple of seconds, and then it's just kaput. So, what do you bet it's the caps?

**Dave Jones:** Let's crack it open. And it's another one of these pain-in-the-ass clip ones. Really don't like them. Much prefer the uh old-fashioned screw. But, what can you do? I wonder who actually makes these design decisions to go that they're going to make this case clip instead of screw.

**Dave Jones:** I mean, I know you do save a couple of cents, but jeez, you know, really tight asses. We're in like Flynn. Woohoo! There we go. Oi, there we go.

**Dave Jones:** This one's a bit different construction of the other one. The uh flat panel comes out of the top, and the boards are on the bottom. So, let's disconnect the ribbon here.

**Dave Jones:** We've got our backlight over here. And this LG monitor's pretty darn ordinary compared to the Samsung one we looked at last time. It's not a full metal shield chassis at all.

**Dave Jones:** It just sits in this little metal frame here, which is, you know, okay in its own right. Um, but it's certainly nowhere near the quality of the uh Samsung monitor we saw last time in terms of physical uh build construction.

**Dave Jones:** And the board doesn't look nearly as good a qual- And once again, of course, they've got a single-sided PCB, par for the course here, but And look at these diodes here, just pushed in dodgily at any old uh angle.

**Dave Jones:** Horrible, horrible. They've got a little kink in them uh to stop them going all the way through. I mean, they've done that, they've mounted them off like that to uh uh give them uh spacing and some heat sinking with the extra leads and to get them off the board.

**Dave Jones:** And you can actually see on there, you can actually see a heat sink symbol. So, it's almost as if, well, they were supposed to mount these on heat sinks.

**Dave Jones:** And you see the footprint in there for like a uh vertical TO-220 package device. And they've gone, uh bugger that, we won't uh use an expensive TO-220 package diode and a heat sink, cost a fortune.

**Dave Jones:** We'll save some cents and we'll just whack in these ones here and just leave them free standing off the board. Uh, poor form, really. Uh, just terrible. And uh yeah, they're just pushed in there at any old angle in the factory, not in China in this case, in Indonesia.

**Dave Jones:** Up the top here is an M205 size uh direct soldered in fuse. Like that, don't particularly like that, but hey, at least it is fused, right? And uh and they've got, you know, basic adequate protection and um some filtering here, but yeah, they haven't really gone to town on the input side of stuff.

**Dave Jones:** They've got uh uh shake-proof washers on the earth lug down in there. So, it it's okay, you know, it's it's not too bad. I guess it's possible, I guess you could say.

**Dave Jones:** And uh what we're really interested in though are these caps. Well, well, well, what do we have here? Check out that little sucker. You can see the bulge in there.

**Dave Jones:** Clear case of these things dried out and this one here as well completely dried out. 1,000 mic cap, 105° C rated, Samwha brand, SAMWHA. In this case, we haven't I got uh caps on like we got last time.

**Dave Jones:** It looks like there's only bulges in two of them. The other ones look reasonably okay. And the main DC input filter capacity here looks okay, too. No bulges in that.

**Dave Jones:** These ones get less stress usually than the output caps, 450 V rated, 105° C. And once again, it is Samwha brand WL series. And the ones that have clearly failed here are also WL series.

**Dave Jones:** And Samwha aren't that bad a brand of capacitor. And the WL series isn't that bad either. So, I think it's just probably either these things got too hot and or the age of the things and they've just slowly dried out and well, you know, it eventually happens to these caps.

**Dave Jones:** So, let's take So, I'm definitely going to have to replace those two that are bulging, but what about the other ones? I think it's time for the ESR meter.

**Dave Jones:** We didn't look at that one last time. Now, the correct tool for the job here is not, and I repeat not, a capacitance meter. What you need is an ESR meter or an equivalent series resistance meter.

**Dave Jones:** These are specifically designed to measure the ESR of a capacitor because the internal resistance of these capacitors is what actually determines their performance in these switch mode power supplies and it needs to be really low and when they heat up the dielectric material in there actually dries out and the ESR increases.

**Dave Jones:** The capacitance might still read fine but the ESR is the thing that goes through the roof with these bad caps. Now, what I've got here is the famous Bob Parker designed ESR meter.

**Dave Jones:** His name is Bob Parker. He's an Australian and he got this originally published in Electronics Australia magazine but this is the updated Mark II version from Silicon Chip. And ESR meters are all the same.

**Dave Jones:** What they do is they pass the key to it is passing a high frequency 100 kHz test signal through the capacitor because if you look at data sheets for virtually all these electrolytic capacitors, the ESR, the equivalent series resistance, is specified at a frequency of 100 kHz and that's exactly what this ESR meter will put out and it'll also put out a low enough voltage so that it doesn't

**Dave Jones:** turn on any semiconductor junctions in the circuit. So, these not only can measure ESR but they can do it in circuit. I don't have to desolder these capacitors in order to measure them and that's the brilliant thing about one of these ESR meters.

**Dave Jones:** If you're into repairing stuff, pretty much a must-have unit. Now, uh we've got these five output caps here. Only two of them are showing bulges. So, let's switch this sucker on here and we need to zero it out.

**Dave Jones:** There we go. We've zeroed out our test leads here and it does have a table of typical figures on here but you know, that's only really rough rule of thumb.

**Dave Jones:** Like, what are we talking? These caps are 1,000 uh well, 470 mic. Uh yeah, 470 mic at 35 V. So, you know, I'm not really going to go by that 470 mic at 35 V 0.1 100 m so 0.1 on here.

**Dave Jones:** Eh, it should be lower than that. Let's go check check the data sheet. And sure enough, I checked the data sheets for these WL uh series Samwha caps and uh the value is um uh 0.027 or 27 m maximum um at 20° uh C for these particular caps 470 microfarad 35 V.

**Dave Jones:** So, let's uh measure them here and see what we get. So, let's measure a good one. Here, they these two here are good ones. So, let's flip this puppy over.

**Dave Jones:** We've zeroed our meter here and we're looking for something under that 0.027 mark. There we go. 0.01. Not a problem. 0.02, you know, it doesn't have the resolution really to go that low, but ballpark that cap is just fine.

**Dave Jones:** So, really uh there is no reason to change that unless you really want extra long life. I mean, this one these this one might eventually fail as well, but at the moment to get this thing back op- operational again, we don't need to change that cap.

**Dave Jones:** It's just fine. Now, this one next to it here. And by the way, make sure warns you on here discharge capacitor before measuring. You don't want to blow the ass out of your ESR meter.

**Dave Jones:** So, this is another one which is not bulging. And there we go. Not 0.02 ohms, 20 m. That one's fine. I wouldn't bother changing that one. Now, this one here this one here is a bulgy and so is this one.

**Dave Jones:** I can feel it and you can see it. We're seeing the close-ups on that. So, these two Well, let's measure this third one over here which isn't bulging. So let's do this one.

**Dave Jones:** And we've got 0.02 again. That one is fine. Wouldn't bother replacing that, but first bulgy one, let's take a look. There's the two pins there. And the great thing about this is you can actually measure these in circuit.

**Dave Jones:** And cuz it's a low enough voltage, it's not going to switch anything else on. This capacitor or these large value capacitors will be by far the lowest impedance device in this whole circuit parallel across that voltage output rail.

**Dave Jones:** So really, it basically essentially ignores everything else. So let's have a look at it. Hey, there we go. 0.24 240 milliamps. An order of magnitude higher than what is than what the spec for that capacitor is.

**Dave Jones:** So it's clearly failed. So even if it didn't have a bulge in it. A bulge is the usual giveaway, but it doesn't always have to have a bulge in it.

**Dave Jones:** So the standard practice would be to go around and measure all the caps in a product like this and see which ones are out of spec. And here we go.

**Dave Jones:** Next bulgy one. But I found that most of the time they they do bulge when they do fail, they do bulge. And oh look at that one. That's a shocker.

**Dave Jones:** 0.61 ohms. And by the way, no, the polarity doesn't matter a rat's ass with these things. It doesn't matter at all. Um electrolytic capacitors are polarity sensitive, but because this is such a low voltage, it doesn't matter.

**Dave Jones:** You're not going to harm any good capacitors by doing that. So there you go. Bingo. We have these two culprits. I need to replace those. They're goneski. There's a little one down here.

**Dave Jones:** Hasn't bulged. I might actually measure him as well just for good measure, but I don't he's not a big output DC rail caps, so I'm not I'm not too fussed on that.

**Dave Jones:** 0.14, that sounds about right for a cap of that that size. So, yeah, good enough. Need to replace two caps there. There you go. Check out the uh Check out the charring there underneath the um backlight uh transformer there.

**Dave Jones:** Eh, it's been getting a little bit hot, that one. And uh here's the base of the board. Nothing special. Looks a bit Looks a bit grotty. Not Not that impressed.

**Dave Jones:** It's not as good as the Samsung one we we looked at anyway, but yeah, they're kind of doing the right things on there. And for those curious, I will measure the big um high-voltage cap over here.

**Dave Jones:** Yes, I have checked. There's no voltage on that. It is discharged. Usually, they'll have a bleed resistor across it, but always measure it before you do that. Well, this is only 68 microfarads at 450 V.

**Dave Jones:** So, let's flip it over. Where is it there over? That's that one and that one. 0.8 ohms. That sounds pretty decent. I mean, if you go by the uh chart here, it doesn't go up to 450 V, but you know, 68 it you know, I expected under an ohm, and that's what I'm getting.

**Dave Jones:** So, really, I don't think that one is a drama at all. And just to clarify that, we do actually have a mix of WB series and WL series. So, the two that have failed are the WL series.

**Dave Jones:** These 470 mics um uh WB series, they're all fine, but the two that failed here, they are the W L series at 1,000 mic. And the best I've got are these Jcar SI brand 1000 micro 25 V instead of 1000 micro 16 V.

**Dave Jones:** Once again, you can go up in voltage, no drama at all, and you can go up in capacitance, no drama at all, but uh do not go down in voltage.

**Dave Jones:** That's a big no-no. And don't go up. Uh sorry, don't go down in capacitance, either. You can maybe get away with going down a little bit. In general, you don't really want to do that.

**Dave Jones:** So, let's just whip these out here. All you All you got to do is heat up one pin and pull out one side, and then heat up the other one.

**Dave Jones:** Uh what I got my iron set to here? Not that great. So, that pops out. And of course, we can't stick our capacitor through that hole there unless we've actually got a hole.

**Dave Jones:** So, we just wax some solder wick over that and put it down. And bingo, it wicks the solder away, and ta-da, we have a hole. And we do the same thing here.

**Dave Jones:** Got to have solder wick. It's absolutely essential. And that should wick that away. Bingo. And we're ready to whack in our new caps. Make sure you get the polarity correct, and there's the uh they're low ESR type, of course.

**Dave Jones:** You must use low ESR types for their switching power supplies. Crappy SI brand, I know, but it's all I've got. Uh they're 105°C rated. So, let's uh stick those in and solder them and see if we can fix this sucker.

**Dave Jones:** And just to prove that that fixed it, let's measure our ESR again. There we go, point oh three. Not as good as the other ones, but near enough. There we go.

**Dave Jones:** .05, good enough for Australia. That'll get us out of trouble. That'll at least get this monitor up and working. Let's give it a try. So, here we go. Let's give it a try.

**Dave Jones:** I haven't snapped the bezel back on yet. I'll just uh hold off until we get the okay. Ta-da! Hey, we have a blue light. We have a blue light and I saw the LG thing there.

**Dave Jones:** Ta-da! Check signal cable. And bingo, there it is. Foregone conclusion, it works an absolute treat. Perfect. Another win for dumpster diving. I love it. Catch you next time.
