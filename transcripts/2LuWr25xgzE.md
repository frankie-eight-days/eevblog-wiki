---
video_id: 2LuWr25xgzE
title: EEVblog #1277 - Electric Fence Controller Teardown
url: https://www.youtube.com/watch?v=2LuWr25xgzE
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 29, "3": 45, "4": 60, "5": 78, "6": 102, "7": 118, "8": 134, "9": 151, "10": 168, "11": 183, "12": 199, "13": 212, "14": 225, "15": 240, "16": 255, "17": 269, "18": 284, "19": 295, "20": 306, "21": 324, "22": 341, "23": 356, "24": 369, "25": 383, "26": 397, "27": 411, "28": 424, "29": 439, "30": 452, "31": 464, "32": 477, "33": 491, "34": 507, "35": 522, "36": 535, "37": 553, "38": 565, "39": 580, "40": 594, "41": 609, "42": 626, "43": 640, "44": 655, "45": 665, "46": 682, "47": 695, "48": 712, "49": 723, "50": 738, "51": 753, "52": 767, "53": 780, "54": 792, "55": 808, "56": 822, "57": 835, "58": 847, "59": 862, "60": 882, "61": 902, "62": 917, "63": 933, "64": 949, "65": 965, "66": 979, "67": 996, "68": 1015, "69": 1030, "70": 1042, "71": 1055, "72": 1068, "73": 1080, "74": 1090, "75": 1103, "76": 1120, "77": 1134, "78": 1147}
---

**Dave Jones:** Hi, check this one out. It's a random teardown item from the bunker and it's an electric fence controller. It's the MBT 200. Look at these gigantic screw terminals on here and it's actually an Australian unit. Check it out,

**Dave Jones:** manufactured by Paxton Technologies. They are still around and this is what they do. They manufacture electric fence controllers. So, I've contacted them to see if I can get a schematic. I'll see if it turns up in time by the time I

**Dave Jones:** finish this video. Anyway, it's a really old model that I can't find any info on at all. It's the MBT 200 type D, whatever that is. Input 16 volts AC or 12 volts DC. Output into a 100 ohm load 12 joules. So,

**Dave Jones:** doesn't tell you how many kilovolts it does, but it's got a kilovolt display on it. AC and DC inputs and a switch and that's about it. And well, I don't know anything about electric fence controllers. So, let's crack it

**Dave Jones:** open and see what's inside. Lots of big caps, no doubt. All right, six screws on here and hello. Wow, look at that Wow, that's enormous. Look at those caps. Oh, yeah, that's where all the joules are being stored. Oh, BUT LOOK AT THIS,

**Dave Jones:** MADE IN AUSTRALIA. YOU bloody ripper. Unbelievable. What's that? 30 mic Plessey Ducon caps. 30 mic 900 volts DC each. Wow, pulse grade capacitor made in Australia. Oh, bloody beauty. Yeah, Plessey. I used to work at GEC Marconi. Yeah, they were

**Dave Jones:** Plessey. I think GEC Marconi bought out Plessey and now the GEC Marconi technology park at Meadowbank is now just there's only a few buildings left and there's a road called Faraday Road left and that's it. And it's all

**Dave Jones:** like housing development apartment development complexes now. It's really quite sad. Anyway, that was a they had their own ceramic hybrid manufacturing facility and everything. Anyway, I don't think they made they didn't make the caps there. I'm not sure where they made those, but

**Dave Jones:** somewhere in Australia. Oh, check it out. That's a Look at the size of that transformer in there. Wow. And here's all the output caps. Wow, check that out. Got a separate riser board for that. So, got a bunch of big power resistors and yes, I

**Dave Jones:** can poke around here. It's been turned off forever. It's just been sitting in the bunker. So, I'm sure it's completely discharged. They'd be amazing caps if they weren't. So, I would assume they'd be in series, I would guess, to get the

**Dave Jones:** to get the voltage requirement. I'm not sure how many kilovolts this sucker's going to be, but Oh, anyway, there we go. There's different models. This is the MBT 200. So, MBT 50 and BT 50 and BT 80. Maybe I can get

**Dave Jones:** some info on the BTs. So, that's actually 2004 vintage down there. And if you go to the website, which I'll link in down below, they've actually got some amazing repair guides for these things. Like a PDF with all the instructions on

**Dave Jones:** how to troubleshoot and repair these things. Unfortunately, they don't have this particular model and they don't have a schematic in the ones that I saw, but yeah, really is quite nice. So, they really do seem to support these and they do

**Dave Jones:** actually have an eBay store where they sell replacement capacitors. The same 30 mic 900 volts, but not the Plessey ones anymore cuz I'm pretty sure you can't they're not making these anymore in Australia and you can't buy them, but

**Dave Jones:** exactly the same rating from Hong Kong or HK capacitor. I assume it's Hong Kong capacitor. Uh they manufacture a range of these same ones. So, they still sell replacement caps in these things. So, anyway, yeah, these are these are

**Dave Jones:** fantastic jobbies. They'll be flameproof and they'll be, you know, they're designed for like high pulses because electric fence controllers, I believe, although there's many different types, there's lethal, non-lethal, and there's ones that go that go from like giving

**Dave Jones:** you a warning zap to ones that then on the second zap will kill you. You know, they're designed for like, you know, prisons and uh military installations and uh stuff like that. But, uh yeah, this is probably just an agricultural

**Dave Jones:** uh model. So, you know, to stop animals getting through um electric fences on the farm. So, it's probably not lethal, but you wouldn't want to touch it. Um you know, 12 joules. Oh, jeez, you'll know you're alive if you get hit with that. That's

**Dave Jones:** That's for sure. So, it looks like a pretty uh dumb unit. There's no smarts in here. Um I I'd say that the uh kilovolt meter is just like a panel meter uh type thing cuz I don't see any

**Dave Jones:** microcontroller unless you know something's on the other side. Maybe we can take the board out and uh flip it over, but I wouldn't expect anything on the other side. I think we've just got uh primary side uh storage and uh

**Dave Jones:** switching here. It looks like we've got three big uh probably uh MOSFETs in there. And that switches this uh huge big custom transformer here and uh to the secondary. Has it got any feedback? I would say that this big resistor here

**Dave Jones:** uh oh, that's marked D02. What's in there? Ooh. What is that? It's got a cover on it. Oh, there's two leads on each side. Oh, oh, 02. It's an opto is it It's an optocoupler, is it? Anyway, um these are

**Dave Jones:** usually uh like pulsed uh DC type things. I'm I'm there's many different uh standards and and stuff like that for them. Uh but yeah, I believe it's like a pulsed uh DC type thing, so it doesn't give you like continuous direct uh DC

**Dave Jones:** shock. It will actually pulse. That's why you need uh pulse grade uh capacitors input and output, too, of course. But yeah, I'd say it's got some sort of uh feedback to regulate that. And what's that resistor up there doing?

**Dave Jones:** Is that a bleed resistor? Is that a uh feedback jobby? Aha, if you have a look down in there, it says HTFB. That would be high tension feedback. So, that's either feeding back from the secondary uh side, but given its

**Dave Jones:** location, it doesn't seem to be. So, maybe there's like a uh intermediate uh step up there and then before it gets to the big perhaps, and that's what they mean. Well, there you go. I spoke too soon. There's your microcontroller

**Dave Jones:** down there. All the PIC fanboys go wild. What one is that? A PIC 16F uh series, given the vintage of this sucker. And that's just driving uh the LCD. There is some extra uh surface mount chippies under there. They're just They would

**Dave Jones:** just be uh LCD drivers because the PIC wouldn't um have direct LCD drivers. And there's not enough pins, anyway. So, yeah. So, it's probably a little op amp in there. I couldn't be bothered checking. Uh we've got some LEDs. And no

**Dave Jones:** surprises for seeing uh big cutouts between uh the capacitors here. Although, they don't extend all the way out here. I would have extended those out a bit further than that. That's a bit uh It's a bit tight-ass. Um look, they've

**Dave Jones:** extended it out this side, but they haven't extended it out that side. Um Is this an afterthought? Uh they've got a uh MOV on the uh straight across that cap there. So, yeah, maybe they I don't know. It come a

**Dave Jones:** guts or somehow in the design, and they've added that as an afterthought cuz uh otherwise, you'd put that uh directly on the PCB. And then they've got another uh switching um on its back on the bottom side, which is

**Dave Jones:** unusual. Don't know why you wouldn't have you know, laid that out on the top side. It's all a layout issue, really. But, yep, all three of those uh caps are in parallel, so yeah, no touchy. And I'll just check to see if the negative

**Dave Jones:** of these caps is uh ground referenced. So, yep, of course it is. Now, this is interesting. Uh this that was the big power resistor we saw on the top, and sure enough, it's between the positive and the negative output like this, but

**Dave Jones:** it goes through that little uh opto sensory type thing. This component across there is just a uh reverse biased diode. Uh that might just be a dropper resistor. That doesn't actually have to be a load. Otherwise, it'd be current

**Dave Jones:** sensing the load. So, I'd say more likely it's just voltage sensing, and that's just a dropper for whatever the heck part this is. Just wanted to show you a 4K close-up of these Plezy Ducon caps, cuz yeah, you

**Dave Jones:** rarely see those, and you won't see them anymore, cuz I'm pretty sure they don't make them. Ha, I figured this out. It's obvious. It is an optocoupler, and there's nothing in the middle. Squishy, squishy. That's a LED, and that's a

**Dave Jones:** phototranny. So, they're just rolling their own um optocoupler there, cuz uh presumably they couldn't uh find one with enough uh withstanding voltage. Fair enough. It's a cheap way to do it. So, that right there is a 1 meg LED dropper

**Dave Jones:** resistor. Have you ever seen a 1 meg LED dropper resistor? Hands up. I'm sure there's not many of you. So, if you do the calculation for that, of course, ignoring the little uh piddly uh diode drop compared to 1,000 V, you know, you

**Dave Jones:** just do rules of thumb in engineering, then that's uh 1 mA per kilovolt. So, a typical LED might be 20 mA max, uh for example, then, you know, 0 to 20 kV. That makes sense. Doesn't mean it's going to go up to 20 kilovolts. I don't

**Dave Jones:** think it does. I think these only go up to, you know, several kilovolts, maybe five uh tops or something like that. Perhaps could go higher, but um yeah, that makes sense. Just 1 milliamp per kilovolt. Easy. So, you would just get a

**Dave Jones:** uh proportional current in the phototransistor on the other side of that optocoupler, roughly. And for you power aficionados, there you go. But, the one on the uh left there, uh the friend of Jake the Pig, he's only got two legs. In fact, both of those

**Dave Jones:** other parts down in there, they're a diode-y. They ain't So, obviously, we've got a first-stage uh switcher here. There's our switching There's our switching uh transformer. And uh that would be generating Well, these are 900-V caps. They're all in

**Dave Jones:** parallel. So, you know, be generating, you know, 7-800 V, um something like that. You wouldn't be pushing it right to the uh 900, of course. And then that um then you'd use the this other switching over here to

**Dave Jones:** uh take the energy from these caps and drive your transformer to get um switching again uh to a boost it to your high output voltage. I actually rather like this uh spade lug arrangement like this. PCB mount spade lugs, and they

**Dave Jones:** just go in like that. That's a neat way to do a vertical uh riser board. But, anyway, um there you go. We've got the positive and negative outputs, and we've got a common uh as well. And we've got

**Dave Jones:** two big Oh, no, they're different values. 56R and 100R. There you go. But, yep, I'm guessing all these caps are in series, and yep, I'm right. Yep, check it out. There we go. One there, series, series, series, series, series. So,

**Dave Jones:** we've got six caps in series. How many volts each? That'll tell us our maximum output. So, if you don't know the maximum output voltage of a design like this, you can just calculate it. Well, these are 250 V cap and 250 V each. They

**Dave Jones:** wouldn't be running them at uh 250 V. So, let's just say uh 200. 6 * 200 1,200 V. So, 12 * 200 that would make uh 2,400 V with an absolute max uh voltage rating of 3,000 V. So, yeah, it's not going to

**Dave Jones:** be over 3,000. This is good um because I have an old analog meter. Not not this digital rubbish. Have an old analog meter that measures up to 5 kV. So, if I power this thing on, I'll be able to uh

**Dave Jones:** measure that directly with my analog meter. Beauty. And in case you're wondering, those big power resistors, here's the positive input coming from the transformer and it goes through a series resistor and then through the series caps like that. So, those caps

**Dave Jones:** are actually um in series and then they're just half tapping uh the capacitance uh network here to give you your common. And some people might be wondering, well, why don't they put uh slots in a board like this? Well, you can of course

**Dave Jones:** uh to prevent creepage, which is um across your board like this if you get moisture contamination or something like that across your board. You can certainly do that, but because these are only 250 V rated each, essentially, there's only 250 V between there and

**Dave Jones:** there and that's plenty of uh creepage clearance for uh 250 V uh DC. So, when you whack them all in series, oh, you could argue like there's more across there and stuff like that. So, you could argue they could should be

**Dave Jones:** maybe a slot down there or something like that. But yeah, I know. It's It obviously does the job. But yeah, I think if you go and get your uh chart out and work out your clearances, it's it should be enough. And then

**Dave Jones:** there's uh three of those mobs in series or six of them in series uh across the entire positive negative output. Again, because they didn't have the individual uh rated ones, I guess. And these two unpopulated components marked here, um

**Dave Jones:** S, they would be spark gaps. So, um yeah, they just haven't populated in the spark gaps. I'm guessing, you know, they didn't want both the MOVs and the spark gaps. So, you know, either or. So, I do actually like this uh front terminal

**Dave Jones:** arrangement. Really is quite good in that vertical board with the uh spade lugs. And these go through the holes on the uh PCB like that. That is That's really quite neat solution. All right, I'm going to power this thing up. no

**Dave Jones:** idea if it works. I don't It literally came from the dumpster, so I don't know what the deal is. Um I'm going to power it off my micro supply. And as I've said many times before, anything over 12 V DC

**Dave Jones:** scares the out of me. So, I'm not going to be anywhere near this sucker. So, let me move this away a bit further. So, here we go. Uh 12 V 1 A. I'm going to turn it on. And oh, it works. It works. There's

**Dave Jones:** digits. There's digits on there. 12 V load factor. Let's uh There's a dash dash dash. Let me It's drawing 14 mA. That's quiescent current, obviously. Then it dies out. All eights. So, that's a a power on test, I guess. So, let's

**Dave Jones:** switch it on. Uh nothing. Maybe it was already on. Um nothing. Either way, I You don't need a load on it, I don't think. And there's no energizer light on there or anything. So, no. Wub wub wub wub. Sorry. Decided

**Dave Jones:** to hook it up to my uh beefier lab supply here. And a 1.5 A current limit, which my little micro supply can't do it. And we do get a brief output here. Watch this. Overload and then energizer okay

**Dave Jones:** briefly, but no. It's only It's It's rated for 1.1 A. So, maybe there's like some input pulse, something like that. I might leave it there. I was briefly thinking it'd charge up slowly, but like it's 10 milliamps. This is quiescent stuff. It's

**Dave Jones:** not It's not loading any energy. There's no joules going into those gorgeous Aussie caps. All right. Well, let's try it with a load. Got this in the previous mailbag, coincidentally. I don't know its voltage rating and it does have exposed terms turns there

**Dave Jones:** because it's an adjustable power resistor, but she'll be right. That's 1K. This thing's rated for lower loads than that. So, anyway, let's give it a burl. Nope. Exactly the same thing as before. I don't know if you saw that the

**Dave Jones:** energizer LED does briefly come on, but that's it. I mean, it's not going into overload or anything, just quiescent current. So, I've had a bit of a little quick poke around in here, but I can't see anything obvious. Now, one of the

**Dave Jones:** things is the the switch on the side here. This is actually connected into a like a single in-line header there. Is that the right one? I don't know. It is labeled T2. Whatever the heck that means. So, but

**Dave Jones:** unfortunately, like without a manual and without a schematic, we're flying a bit blind. Sure, I could you know, start reverse engineering this or or having an educated poke around, but the good thing is is that Paxton claim that they will supply the

**Dave Jones:** schematics. They actually tell you this on the website and on the in the actual like troubleshooting documentation as well. So, I have emailed them, but like it's Christmas and New Year's time. So, they're probably like completely shut down. So, rather than spend my time

**Dave Jones:** actually you know, doing this, I'll wait until I come back. And if you're watching this, I I actually on walkabout somewhere. So, I'm not in the lab. So, uh yeah, I won't be back until uh towards late January.

**Dave Jones:** Um, so hopefully uh by then they'll be uh back and they can uh send us a schematic and maybe uh maybe an operational manual for these things. So, we might get lucky and if they don't uh come through, then we can

**Dave Jones:** always do a reverse engineering video. So, if you want to see a reverse engineer uh of the circuit of this thing, then mention it in the comments down below and give a thumbs up, too. The more thumbs up I get, um the more tempted I

**Dave Jones:** will be to do a follow-up video for this one. This was supposed to be just a teardown. So, I'll call it quits there and I won't uh attempt to repair this thing and or if there's anything wrong with it, maybe it's just a, you know, a

**Dave Jones:** PEBKAC. Um, I don't know how to use this thing. Maybe someone's fiddled around with it. I don't know. Um, and it's got not for sale written on the back of it. So, I'm not sure if this is And given

**Dave Jones:** that I can't find any info on it, um maybe it's a could even be like an unreleased or limited release product or or something like that. But, it does have, you know, proper serial number and everything up there. So, yeah, not sure what the deal

**Dave Jones:** is. But, anyway, I'm packed and do claim to supply the schematics. And this is, well, uh 16 years old. Geez, you know, 2004, that was yesterday. And well, it's 2020 now by the time you're watching this. Geez. Anyway, um yeah. So, hope you

**Dave Jones:** liked that uh teardown of this Aussie uh designed and manufactured unit. Absolutely brilliant. Uh Plezy caps. Uh let us know in the comments down below if you've used uh Plezy caps and when they actually uh stopped making I

**Dave Jones:** presume they stopped making them. I don't think they make them anymore. I Please correct me if I'm wrong. And this custom up here, is that made in Australia, too? Maybe. Anyway, um yeah, ripper. So, anyway, they do have lots of

**Dave Jones:** more advanced models now, but uh yeah, if they come through with the schematic, then we can have a go. If not, or reverse engineer, maybe. Hope you enjoyed it. Catch you next time.
