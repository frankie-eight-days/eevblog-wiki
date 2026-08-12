---
video_id: 7j5NtKB0vss
title: EEVblog #1292 - $2 Meter vs JVA Electric Fence Controller!
url: https://www.youtube.com/watch?v=7j5NtKB0vss
source: youtube-asr
timestamps: {"0": 1, "1": 12, "2": 28, "3": 45, "4": 59, "5": 72, "6": 88, "7": 102, "8": 113, "9": 125, "10": 140, "11": 155, "12": 172, "13": 188, "14": 203, "15": 221, "16": 241, "17": 258, "18": 271, "19": 287, "20": 300, "21": 313, "22": 332, "23": 346, "24": 361, "25": 373, "26": 387, "27": 402, "28": 414, "29": 427, "30": 440, "31": 454, "32": 470, "33": 487, "34": 501, "35": 516, "36": 527, "37": 543, "38": 557, "39": 570, "40": 584, "41": 601, "42": 615, "43": 635, "44": 650, "45": 666, "46": 682, "47": 700, "48": 713, "49": 725, "50": 742, "51": 759, "52": 775, "53": 789, "54": 807, "55": 824, "56": 838, "57": 856, "58": 870, "59": 895, "60": 910, "61": 928, "62": 943, "63": 962, "64": 989, "65": 1002, "66": 1016, "67": 1036, "68": 1050, "69": 1068, "70": 1083, "71": 1099, "72": 1114, "73": 1128, "74": 1144, "75": 1155, "76": 1169}
---

**Dave Jones:** Hi, if you remember this electric fence controller I found in the dumpster and if you don't, well, I'll link it in the down below at the end. If you haven't seen the video, it was quite popular. Um, unfortunately, it was broken, but it

**Dave Jones:** was like quite an interesting teardown of this thing. Quite an old unit. Was designed and manufactured by Paxton Technologies here in Australia. He's one of the world leading designers and manufacturers of electric fence controllers. And as it turns out,

**Dave Jones:** I was able to get in contact with the uh founder and CEO and chief designer of uh Paxton Technologies, Paul Thompson. And we actually did an Amp Hour episode talking about uh the history of this unit, how we design the electric fence

**Dave Jones:** uh controller design in general, all sorts of things about lightning protection, and uh tons of interesting technical discussion. I highly recommend you check it out. It's linked in down below over at the ampower.com. You can get it on

**Dave Jones:** your iTunes-es and your iHeart Radios and your favorite podcasting apps and all that sort of stuff. But, he was actually rather embarrassed by this design. He didn't think it was very early design. Didn't think it was very good. So, he said,

**Dave Jones:** "Hey, let me send you in one of our new Bobby Dazzlers." And here it is. Look at this. This is the JVAMB8. And uh JVA is their like uh you know, house brand, but it's actually Paxton Technologies in uh Queensland who

**Dave Jones:** actually design here in Australia who design and manufacture these locally. And uh once again, it's like it's got Wi-Fi and everything else. And in the podcast uh Paul talks about what how farmers they want to, you know, wake up

**Dave Jones:** in the morning and use Wi-Fi and an app on their phone just to check that their electric fence is still working and stuff like that. Anyway, Paul thought this would make a more interesting teardown. And I'm sure it would. So, you

**Dave Jones:** know what we say here on the EV blog, don't turn it on, take it apart. Still got these giant thumb terminals. Look at this. Yes, has a big hole in there for the wire to go through. Fantastic. So,

**Dave Jones:** you know, it's not that these are high current at all. In fact, they're quite low current. They're designed not to kill you, but yeah, you don't want to be touching this because it's not going to be pretty. Anyway, I

**Dave Jones:** love the enclosure. It's all like weather proof and everything else. Absolutely fantastic. Here we go. This is an 8-Joule jobby IP66 rated 12 to 24 volts DC in. And, you know, it's only 10 watts. So, there's not a huge amount of

**Dave Jones:** like actual power behind it. But, 8 joules. You know, that'll wake you up. Made in Australia. No wuckers. And as I mentioned in the previous video, Packard and actually do really amazing repair guides for these things. And Paul talks

**Dave Jones:** about that in the podcast episode about why they do that. And they have an eBay store that sells spare parts for this thing like output transformers because they're a custom jobby. And really interesting discussions on there about transformer

**Dave Jones:** design, you know, graybeard transformer design like that. Sell transformers and output caps and and other spare parts for their products so that people can fix these themselves. Here we go. I have not powered this thing up since I got it

**Dave Jones:** so it's going to be discharged. Oh, look at that. Oh, pop it. Oh, the capacitors. They're floating. Oh, look at that. Little rubber BABY BUGGY BUMPERS. OH. LOVE IT. ANYWAY, LOOK AT the big custom output transformer here. And a very

**Dave Jones:** similar design and construction really to the previous unit. We've got the output riser board here with the output capacitors and also limiting resistors as well. We've got our huge mob protection down here all in series. Absolutely fantastic. We went over the

**Dave Jones:** all this sort of stuff in the previous one. So, it's going to be very similar. Now, Paul talks about this in the podcast as well and it's a fascinating. This is of course an optocoupler, a do-it-yourself optocoupler. The previous design, as you saw in the

**Dave Jones:** last teardown, actually the old one had just some heat shrink tubing going across, but now they've got this custom like injection molded plastic thing, but it's basically it's just a I believe it's an infrared LED over here and just

**Dave Jones:** a phototriac over here and that's the only way that they can get that decent high voltage isolation. And of course, they get it measures the voltage back across this as well. It's not just like that it's on or off. They can actually

**Dave Jones:** measure and monitor the output voltage as well, but yeah, that's nice. And I love it how they give you the error codes here. I assume that's some LEDs, is it? Unless they have a seven-segment display somewhere. This is

**Dave Jones:** one of the runts of the litter here. The 8-Joule looks like it goes up to 20 Joule and well, that's serious. And yes, in the podcast he talks about all the various standards and things like that that these things have to meet in order

**Dave Jones:** to essentially not kill people for starters. Anyway, isn't that a big nice output choke? Wow, love that. That actually looks like it's an air-cored jobbie. I don't see any ferrite in that. And there are monster output transistors down in there. I should be able to get a

**Dave Jones:** part number on that. Let's just focus in on that. There you go. There's the part number for those playing along at home. Now, this thing is a two-stage booster. So, here's the first transformer that actually uh up to

**Dave Jones:** like the six, 700 volts, uh something like that. That charges up our main caps here, and then of course, the big output uh transistors here, they just dump that into the in a very controlled way, by the way. And uh Paul talks about that in

**Dave Jones:** the podcast about the pulse shape and things like that. Maybe we'll be able to uh measure that here perhaps when we power this thing up. So, they just dump the energy from the capacitors into the transfoil through the transformer and

**Dave Jones:** into the electric fence on the output. And the pulse shape is uh very critical for this thing. And they go through pretty much a like 100% charge uh discharge cycle like each uh second for these caps. The output rate just goes,

**Dave Jones:** you know, bang, bang, bang. So, these main storage caps are uh quite different to the ones that we saw in the uh previous one. They're not made in Australia anymore by Plezi, unfortunately. But uh anyway, these are uh potted ones with uh leads coming out.

**Dave Jones:** As I said, they do sell replacement ones. And they decide to put these on standoffs on the board like that. Presumably, it's like to free up space, probably make them easier to uh replace as well. Cuz as I said, like they sell

**Dave Jones:** spare ones of these on eBay if the output caps eventually uh fail, you know, 5 or 10 years or whatever. Cuz these get a hard life, they really do when they're just dumping everything once per second, charging, discharging

**Dave Jones:** once per second for like, you know, 24/7 for like a decade. Yeah, they eventually wear out. So, you can simply uh replace those and get them, buy them as a whole assembly and go plug them in. Very nice.

**Dave Jones:** And all the PIC processor fanboys go wild. And also in the podcast, you got to listen to it, it's fantastic. Paul talks about What the hell fell down in the lab there? Something fell down. Anyway, let's continue. Um he talks about why

**Dave Jones:** they actually use, specifically use a Microchip part. And it's a very interesting story, actually. There's the Wi-Fi module for those into that sort of thing. It is JVA uh branded, so they do actually get that specifically custom made for them. It's the wee. And nope,

**Dave Jones:** nothing really doing on the underside. That makes sense, of course. And there's no need for cutouts and things like that because you have adequate more than adequate creepage distance across the PCB. It's just yeah, it's massive. And one technique you've seen me use many

**Dave Jones:** times is LEDs actually reverse mount LEDs on the top so they're but they're called bottom emitters and you just put a like a hole or a slot cut out in this case in the bottom of the PCB and then

**Dave Jones:** that just shines through the front here. Looks like they didn't even bother with light pipes. Don't even need them. It's just all custom molded into the plastic case. So that's really nice. Bottom emitters really handy because you can place them with standard SMD

**Dave Jones:** components and just goes out the other side of the board. You don't have to dick around with light pipes. Great. Now although we don't have the schematic, Paul's very kindly provided like a overview block diagram of how this thing

**Dave Jones:** works and it's a pretty simplistic. The main charge capacitors are here that store all the joules. In this case we've got 230 microfarad 900 volt caps here and I just realized that another reason that you'd have them sticking out like

**Dave Jones:** this is so that you can put larger caps in there for the bigger joule models presumably. So maybe the you know one size fits all transformer and then depends on the model you got you choose different caps and then just tweak the

**Dave Jones:** firmware or whatever. So yeah, that wouldn't surprise me. Anyway, now we've actually got two pic processors. One is the main pic here and another one is a watchdog pic and that could be a little tiny one over there or something.

**Dave Jones:** Perhaps haven't looked at the like exact part. That little tiny pic you don't need much and that does our and control for safety. And Paul talks about that in the podcast, of course. So, we've got 12 to 24 volts DC in. And

**Dave Jones:** as I said, we've got the first stage step-up transformer here. There's just a MOSFET, doesn't need to be hugely grunty, not like the output SCRs over here. And then output diode and then some feedback resistors here to allow

**Dave Jones:** them to monitor the charge voltage on the capacitor bank as itself. And of course, this has to be grunty enough to charge fully charge these things to get all your eight joules into there within the second or whatever the cycle

**Dave Jones:** period is. And then we've got a output choke here. And that's almost certainly that air-cored jobby there. And then you've just got a SCR driver and one or more SCRs in here, which then just dump all the energy through the primary side

**Dave Jones:** of your output transformer here. And then that's just tapped off at a higher voltage. And the SCRs, they're going to be down in there as per the previous design. So, the layouts are very similar. And then of course, we've got

**Dave Jones:** full voltage feedback here as I said. And basically, it works in the linear version of the latter. Even if it didn't, you could actually compensate for that in software. And you can basically read back the output voltage with your own custom high voltage

**Dave Jones:** opto-isolator. Beautiful. Thing of beauty, joy forever. So, although the basic concept is fairly simple, if you listen to Paul talk about how they developed these things over the years, then there's a lot of art and science which goes into these. The pulse

**Dave Jones:** shape, the transformer design, output protection and input protection, and the charge discharge cycles of the caps, and all sorts of stuff, and lots of intelligence in the firmware to handle all that sort of stuff. Ugh, really not a fan of these connectors.

**Dave Jones:** Um, I don't know what the deal is there. Industry standard thing, I don't know. All right, so let's power this bad boy up, shall we? I've got my uh 1K, like 100 W wire round resistor here, and it's

**Dave Jones:** got some um open coil windings on there, so maybe, I don't know, you could do the math in your head right now to see if uh that could potentially um arc over each one of those. That might be kind of cool

**Dave Jones:** if it could. 24 30 24 kV, that doesn't make sense. Ah, right, no, that's probably firmware version. I'd say, something like that. 1P, okay, where whatever that means. One, we're ready to go. Let's power on. And there you go, it's ticking over. Energizer

**Dave Jones:** okay LED, 7.9 kV, 12 J there. 12 J there. So, it likes ticking over that once per second. Unfortunately, we're getting no sparkies on the resistor, but oh well. Anyway, it is dumping that into that 1K load, 12 J

**Dave Jones:** each and every time. The kilovolt reading on here, that's actually measured directly from the output terminals via the opto uh coupler, and the 12 J is actually the measured energy on the uh capacitors themselves. So, this was supposed to be rated 8, wasn't

**Dave Jones:** it? We got 12. Bonus. All right, let's see if we can get some sparkies happening here. Give it a whirl. Not exactly the best uh point source there, but uh good enough for Australia. And we're ready to dump.

**Dave Jones:** Whoa. Nice, look at that. Haha, terrific. Need to shoot this in uh with my high-speed camera. Wow, oh wow. Wow, yeah, it's just like a bright flash. And the energy's gone. It's actually safe, it actually uh discharges uh away as soon as you turn it off, no

**Dave Jones:** wuckers. Yes, I have actually measured it. Okay, let's try and nab some high speed. I've got my uh Chronos 1.4 uh serial number seven. It's one of the original uh Kickstarter units. Absolutely fantastic high-speed camera. They're up to version two now. But

**Dave Jones:** anyway, I've got that set to uh 1280 by 720 at uh 1,500 frames per second. We'll give this a whirl.

**Dave Jones:** Okay, more light required, I think, and higher frame rate because I just previewed that video and I only got like a couple of frames out of that that were uh usable. Let's go for 640 by 240 at 8,800 frames per second. Woah.

**Dave Jones:** All right, this is just over 8,800 frames per second. And watch it bang in one frame there. You saw it arc over, not partially, just one single frame off, then on, and it forms that plasma arc which sustains it for a bit until

**Dave Jones:** the uh cycle goes back and it self-extinguishes. Huh, cool, huh? So, can your meter go to 6,000 V? My baby can. Look at this, the triple at 630 NA 6,000 V DC and AC mode. So, I'm just going to switch it on.

**Dave Jones:** We're not going to see diddly-squat cuz the pulse is too quick. That needle ain't even budging. All right, let's blow the snot out of this $2 chippy that we got in the mail bag. Put it to its 1,000 V range, and well, let's power it

**Dave Jones:** up. Of course, 8 J is not uh exactly like the I think we had 300 with uh Doug Ford's one where we blew it up. But anyway, let's let's have a go. Boom. You can it arcing inside. Just continually arcing. Bang. Bang.

**Dave Jones:** Can't smell it. Oh, I can see I can see arcing inside. Oh, we're getting our red status there, too. And there it is. It looks like it's all the action's happened up in the chip. Oh, look at the blob. I

**Dave Jones:** think we have a chunk of the blob taken out and a big Ernie Bernie mark right there. I can smell that. Ah, magic smoke. Okay, I'm going to try that again up close. Here we go. Boom. Magic smoke escaping each time. Haha,

**Dave Jones:** this is There we go. Woo. Fantastic. Try that one more time. It's beautiful. Whisp of smoke going up. Fantastic. Ah, I could do that all day. And on the bottom side here, there's a small little Ernie Bernie mark just

**Dave Jones:** between a couple of contacts on the rain switch and that's uh one of the common uh failure points. All right, I'm going to sacrifice a famously rugged meter here, the BM235. Fingers crossed. I do have it on the

**Dave Jones:** full output here, by the way. We can take a half output, but uh I'm going for broke here. So, I I have no idea of like the pulse shape of this compared to the IEC standard and all that. What am I doing? All right,

**Dave Jones:** here we go. Nope. It's 6.9 kilovolts and it's not overloading. There's no over There's no red status there. It is surviving that. Just hunky-dory. That's what you get when you get uh input protection. That's the MOVs kicking in. Nice. And sure

**Dave Jones:** enough, I just uh checked it on DC volts and it's bang on. So, it survives. No worries whatsoever. All right, let's try a 121 G W. This is a lower rated uh meter cat rated meter than the BM 235.

**Dave Jones:** So, let's see what happens. Ping. Ping. Ping. Ping. There's no red status thing. And I checked and that survived just fine as well, measuring bang on. So, um yeah, I don't know. Let's see if we can um actually measure a pulse shape. All

**Dave Jones:** right, so we've got a 1K in resistor in series with a 50 ohm here. I've got my EVblog high voltage probe here. And we're just single shot. We got one. There's this initial spike up there like that, which goes to let's call that uh

**Dave Jones:** full scale, just back down, and then bam, goes up again, and then discharges pretty linearly like that. There's a little bit of undershoot, of course. And that's it. So, and then that pattern repeats every second. So, yeah, is that a

**Dave Jones:** typical pulse shape for a electric fence controller? Have to ask Paul. And at 50 microseconds per division, we're talking less than uh 200 microsecond pulse here. So, it's not much. And if we choose the other middle terminal there, that should be half

**Dave Jones:** voltage single shot. And yep, there you go. Half I, it's just half amplitude, basically. But it it's a little bit little bit more bubbly there. Is that due to the output network? So, there you go. I hope you

**Dave Jones:** found that as interesting as I did. Thank you very much Paul from Packton uh Technology {slash} uh JVA, who's uh the designer of this thing and manufactured in Australia. You bloody ripper. And absolutely fascinating these electric fence controllers and the technology

**Dave Jones:** that goes into them. As I said, listen to the podcast. It's absolutely fantastic with Paul. So, that's linked in uh down below. Definitely can't link it at the end because can't link in audio podcast cuz YouTube doesn't do

**Dave Jones:** that sort of thing, really. So, anyway, if you enjoyed it, please give it a big thumbs up. And as always, discuss down below. And yep, I'm going to plug it every video, my library channel, 13 1/2 thousand subscribers. Check it out.

**Dave Jones:** Catch you next time.
