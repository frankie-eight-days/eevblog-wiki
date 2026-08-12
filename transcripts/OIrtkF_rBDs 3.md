---
video_id: OIrtkF_rBDs
title: EEVblog #620 - Repair: Stanford Research SR650 Programmable Filter
url: https://www.youtube.com/watch?v=OIrtkF_rBDs
source: youtube-asr
timestamps: {"0": 1, "1": 34, "2": 49, "3": 66, "4": 91, "5": 125, "6": 146, "7": 177, "8": 199, "9": 231, "10": 253, "11": 268, "12": 283, "13": 306, "14": 319, "15": 348, "16": 370, "17": 396, "18": 432, "19": 459, "20": 480, "21": 499, "22": 532, "23": 550, "24": 569, "25": 584, "26": 624, "27": 652, "28": 676, "29": 704, "30": 740, "31": 775, "32": 798, "33": 835, "34": 865, "35": 893, "36": 924, "37": 955, "38": 989, "39": 1020, "40": 1055, "41": 1075, "42": 1103, "43": 1124, "44": 1149, "45": 1178, "46": 1203, "47": 1224, "48": 1255, "49": 1271, "50": 1299, "51": 1315, "52": 1336, "53": 1362, "54": 1398, "55": 1419, "56": 1431, "57": 1460, "58": 1482, "59": 1514, "60": 1539, "61": 1558, "62": 1579, "63": 1601, "64": 1624, "65": 1653, "66": 1686, "67": 1721, "68": 1735, "69": 1764, "70": 1793, "71": 1812}
---

**Dave Jones:** Hi. Yes, I can't help myself. I keep buying test gear on eBay. This one popped up and it is repair. So, it was sold as not working or not powering on. What is it? It's a Stanford Research SR650 dual channel elliptical filter designed for audio low frequency. It's basically DC to 100 kilohertz. So, basically that audio range plus low frequency vibration and shock analysis and stuff like that.

**Dave Jones:** Really handy ones. I've never had a programmable filter in my lab and I've always wanted one, but they've always been pretty expensive. There's a couple of companies that make them. Stanford Research is one, Rockland is another, and there's a few others on the market as well.

**Dave Jones:** So, you know, one of your more obscure bits of kit, but if you need one, you need one. One of those things. So, anyway, I'm hoping this will break the EEVblog curse where the faulty products are either just so incredibly simple like a blown input fuse or something, or they're just beyond economical repair.

**Dave Jones:** BER. So, I hope it's somewhere in between there and we should be able to fix it. Now, the good thing about Stanford Research gear, you've seen some Stanford stuff on my blog before, is that you can get the schematics for them. The manuals come with the full schematics and everything else. I don't have the schematic for it. I haven't tried to see if I can download it somewhere, but you can at least buy them, which is great. The other thing is is that Stanford Research gear looks like

**Dave Jones:** it's been designed in the, you know, early 1990s. It's all DIP technology or uses almost always off-the-shelf parts, so very repairable. I'd be surprised if this thing is beyond economical repair unless it's you know, the power supply has failed. They're usually linear power supplies inside these things unless it's somehow failed and like taken out everything and that might make it beyond economical repair, but anyway, um yeah, we should be able to have a good shot at it. So, I picked this up for just over 100 bucks on eBay and and they still

**Dave Jones:** sell this. Uh it is still a current model, uh but it was designed back in the '90s or something like that. And it goes for 3,300 bucks new. So, beauty, this is the 650, which is the dual channel version, which means you can do uh band pass filtering as well cuz you can select high and low uh frequency and you can do that band pass.

**Dave Jones:** So, let's crack it open, see what we got. Hmm, sold as just doesn't power on or something like that. Let's have a look. So, yeah, these bits are Stanford research gear. Um these type of ones, what they what they usually are is just like a little uh 8-bit uh micro and then basically all just uh passive stuff and switches and muxes and stuff like that. That's what it'll be inside this filter. So, you know, really even if, you know, a power supply has failed and taken out a lot of

**Dave Jones:** stuff, probably still uh probably still repairable even if you had to replace, you know, a whole bunch of op-amps or something like that. Um might still get lucky. So, really there's not much else inside this thing. And this, here we go. This company knows how to pack stuff. Look.

**Dave Jones:** There we go. They've got the uh the molded uh foam, the uh Instapak it's called. So, this is a proper uh professional test equipment company. It's uh the Outback Equipment uh company in Gilroy in California. So, excellent. Well done. So, if you're going to buy stuff from them, uh well, I would uh Yeah, look at that. I mean, that is just fantastic. That's how you should pack test gear. That's brilliant. They've just molded these in here. They've they've chosen a box and then just molded those in specifically. They've

**Dave Jones:** got the machine, the Instapak machine, to manufacture just the right uh but yeah, basically you put these uh little what you do is you put the uh plastic in there and you've got a machine which then squirts the stuff in and then it just molds around the shape of the product. So, this is really good. So, it should have come to me in good condition.

**Dave Jones:** I don't It looks a little bit crusty. There's a bit of uh I didn't get anything else with it. No manual or anything like that. There's a bit of rust on it. Yeah, it's not a it's not a new unit, that's for sure.

**Dave Jones:** Um and yeah, there's a bit of corrosion on the on the BNCs there. That's, you know, that's not terrific, but we can clean those up. But even if something like the BNCs are ruined, you know, you could always replace them in gear like this.

**Dave Jones:** So, uh to scope, yeah, somebody's written on there. Yeah, thanks for that. Terrific. Um yeah, lots of rust on the screws. So, yeah. There we go. Quite a bit pretty crusty, but hey, let's crack it open. Well, no, I'll power it up first. Serial number 28078.

**Dave Jones:** And they probably would have made that many. So, yeah, it's not going to be serial number 78. It could be 8,078, but I doubt it. Stanford have made a lot of these things. Made in the United States of America.

**Dave Jones:** Actually, there doesn't seem to be a voltage select in there. So, I think I'll just crack the lid off first and see, make sure there's no uh jumper in there for 240-V operation. So, as I said, it'll be all DIP mostly all DIP technology. I'm actually I'm surprised I'd be surprised if it's not 100% DIP technology, probably on one or two big boards. There'll be a processor board and there'll be a probably a big analog board. They might integrate them into one. I don't know.

**Dave Jones:** This is an eight-pole elliptical Oh, yeah, mixture of screws. Somebody's had a go at this. Man, we had flathead on the other side, and then we've got a Phillips, and then we've got a tiny little hex. Unbelievable. So, I'm a little bit concerned about the amount of rust on this. You got to wonder what sort of life it's had.

**Dave Jones:** And hey, tada! Look at that. That actually looks fairly clean. I don't mind the look of that at all. There we go. We've got two big uh analog boards cuz this is a a dual channel unit. There is a lesser uh model in the 600 series that uh only has a single one. So, you can combine the uh two channels. And uh So, there we go. I was right. There's an entirely separate digital board up here.

**Dave Jones:** And yes, everything is through-hole. And then a separate analog board for each channel. Look at that. I mean, that is hugely repairable. We've got the all of the designators, all that, nicely spaced out. All DIP. We could just pull that board out and uh desolder things if we have to. Not uh socketed. None of the uh Well, the uh memory and uh stuff over here is socketed. Uh and the ROM, but apart from that, yeah. Um that's pretty darn good. I'm happy with that. And of course, this is

**Dave Jones:** exactly what you see inside a filter. We've got a whole bunch of just passive uh components, and then just um uh muxes and uh switching stuff like that. So, that's pretty much all there is to it because it's just an elliptical filter. It's just using op amps. So, here's all your input uh op amps and stuff over here. And then the rest would be uh And then you've got all the different range resistors and stuff like that. So, yeah. I mean, uh So, it shouldn't be hard to get this

**Dave Jones:** thing uh, up and running. But uh well, let's power it up. Here's what I was uh, afraid of though. Look at all the wiring going into that fuse holder over here coming from the uh, transformer taps, the primary side here. And I love the uh, the big clunking mechanical switch coming from the front panel, of course.

**Dave Jones:** None of this uh, soft power rubbish. I like it. So, yeah, I don't see any initial labeling on there. So, there could be a 240 V configuration of this wiring. So, before I power it up, I probably should consult the manual. Or, actually, I can just do it the easy way.

**Dave Jones:** I'll just got out my uh, 110 V transformer. So, using one of those weird ass Yankee plugs. So, let's uh, let's power this thing on. So, it came uh, from the US, so presumably um, it's still set for 110. If it's set for 240, uh, well, it's going to be under voltage. So, not a problem. I found that some uh, dealers will actually know if they're shipping it to Australia, will actually set it to 240 V for you before they uh, ship it. But, anyway, let's go.

**Dave Jones:** Nope. He's right. Nothing. Dead. What? Well, first of all, I'm uh, before I measure the power supply, I'm just going to do a quick check of that backup battery in there. There we go, 2.92 V. That's okay. Um, so, that is still hunky-dory. Hasn't leaked at all.

**Dave Jones:** Although, in this uh, sort of vintage gear, you'd probably replace that. What date code? We're looking at '96. 24 Yeah, '96 seems to be uh, seems to be the latest that I can see. So, yeah, that mid to late '90s vintage.

**Dave Jones:** It's got that mid to late '90s smell, too. All right, before I start uh, poking around the power supply, let's uh, make sure that the primary of our transformer is uh, is there. So, my power switch is on.

**Dave Jones:** And we'll just measure that. Well, there's your problem. Look at that. No, can't measure the primary side of the transformer. So, that fuse was good. I had a look at that before I powered it on. And yep, it looks intact and measures intact. So, there's nothing wrong with the fuse. So, the primary of the transformer, I'm wondering if maybe there was a sometimes these transformers will have a thermal cutout in them. So, maybe that could be uh that could be an issue perhaps. But anyway, if we can solve the primary side of the

**Dave Jones:** transformer, maybe this thing will come to life and maybe there's nothing wrong with it. I mean, that's ideally what you want in these sort of repair scenarios. If there is actually electrically something wrong with it, then usually you're sort of hoping for a power supply fault cuz they're the easiest things to fix. You know, if it's something like like the EEPROM has died in it due to age or something like that. Or there's something else that you know, some other fault or some other failed chip or something like

**Dave Jones:** that. But usually it's the power supplies that are going to fail first. So, heck, we're not even getting into the main at the primary side of the transformer. Goodness. Now, here's something interesting. Check this here out. Here is the mains input filter here. So, they've got nice little filter module in there with a common mode choke. And I'm measuring the output of that.

**Dave Jones:** And there we go. We've got our 35 ohms. So, hello. That has to be the primary of the transformer. Let's switch it off. Yep. The input pins on the IEC are supposed to just go straight through the filter and out to these two pins. So, we measure our primary of our transformer here, but we don't measure it on these pins.

**Dave Jones:** That is strange. I don't think I've ever seen one of those filters die before. Unbelievable. And you can see the circuit there. I mean, it's just a standard input filter. They've got the common mode choke there and the suppression caps input and output going but that's it. Like it's not like it has any internal fusing. So, really for that So, one side of that common mode choke has to be broken in order for there to be no continuity between the pins the input pins over here and

**Dave Jones:** the output pins here. Whoa. So, let's measure that. No, nothing. There we go. There we go. So, we've got direct continuity on that pin there. Let's try the other pin. Should be this one. And of course, no. Often these things will be potted, too. So, I don't know. Well, let's try This one's not, though. This one's not. So, I will might have to It's probably welded shut, but we might have to rip that thing open and have a look, but I can sort of bypass it cuz I can just

**Dave Jones:** take off I can No, they No, they Well, they're soldered on. I could desolder those and feed the mains directly into there to bypass it, but jeez. I wouldn't have thought the mains input filter. Go figure. I just noticed something out of the ordinary. Look how all these chips are soldered in, yet this one is socketed.

**Dave Jones:** Why? It's almost as if that board has been repaired. I mean, that's just a 74 What is it? 74HC04. Yeah. Hmm. So, that filter just popped out of there. These clips were just holding that in there. So, we should Yeah, there it is. See, it's soldered shut there. So, we can get the iron on that and whip that sucker open. Maybe there's like some internal wiring that's just broken off or something. Maybe there's a board. Maybe it's a right-angle IEC connector or something and yeah, just the internal wiring to that is

**Dave Jones:** broken perhaps. So, I'm having some luck on this. It looks like this whole top cover here can slide off. Hey, nice. There we go. We're in. And check it out. This isn't exactly professional construction on your filter here. There's the common mode choke wrapped in electrical tape and there's your uh there's your mains-rated caps tucked away in there. Three of them.

**Dave Jones:** Oh, goodness. Okay, well, that's embarrassing. I missed the voltage selection switch. I knew it must be in there somewhere with all these wiring going into there. It didn't make sense just to sort of terminate it in there and like and and solder them in the correct position. And yeah, it's tucked it's slid all the way down in there and people watching this in in probably, you know, were screaming at me all along, "Oh, there's the voltage selection switch." Yeah, I missed it. I'm watching the screen of the LCD here. So, I miss these

**Dave Jones:** sorts of things. Anyway, yeah, it was in the 120-V position. So, I can just whack that around and slide it back into the 240-V position, but that doesn't explain why our fuse is good and we're not getting from the output terminals of the filter through to the IEC because, of course, the IEC the IEC input will be going through the fuse and then through to the filter side of it. So, the fuse has to be in that path there somewhere I think. Okay, now I'm fairly

**Dave Jones:** convinced I've figured out what's going on here. Here is one of the IEC well here's the IEC input connector here and of course it's not connected through to there and it should be but it is connected through to the fuse there and of course that goes through the fuse and I can see a trace running on the other side and then that has to run back to this common mode choke over here but there is no connection between those at all that fuse and the other common mode

**Dave Jones:** choke. That's why we get no continuity from the IEC through to there whereas the other one the IEC other IEC input pin is here and we're getting continuity just fine. So I've I've actually resoldered I've reflowed both of those and added new solder through but because the connection is on the other side of the board I can't physically get in there to check that but I'm pretty sure that is supposed to connect through to there and And by the way in the 240 volt position we're getting of course double the

**Dave Jones:** primary resistance 52 ohms whereas we're getting 25 ohms in the other position. Actually I'm beginning to think somebody's had a go at this. There's a nut missing out of here. There's only actually one nut holding the transformer on and well I don't know it kind of looks new and check this out here's the secondary and the secondary has this wire sort of you know hanging out here like this.

**Dave Jones:** It's not like the others and it hasn't been cable tied with the others so I'm not you know I'm not entirely convinced that uh somebody hasn't been fiddling with this thing. Um I don't know. I just get the just get the warm fuzzies. That's the case. All right. So, I put a mod wire in here, but I don't know. I'm getting the heebie-jeebies. There's a reason why that trace under there, and I'm pretty sure that's the trace is broken. I tried to desolder the pins and lever it off,

**Dave Jones:** but it was just all too awkward. Couldn't get in there. It was pain in the ass. That wasn't going to work at all. Okay, I've put a half amp fuse in there. I run it through my 350 power meter. I've disconnected the secondary from there just for now. I just want to power it up and get the primary. So, let's give it a whirl.

**Dave Jones:** And 1. 1.5 W. There we go. That's not too bad at all. Okay, here we go. Moment of truth. We'll plug the secondary back in, and let's give it a whirl. See if anything powers up. Woohoo! Look. It's alive. It's alive. It's doing something.

**Dave Jones:** There you go. Nothing's smoking, so we're at least getting Yeah? Yeah? The micro and everything else uh AC DC coupling overload. Yeah, who well who knows? These are FET input things, I believe. Often No, there we go. It's just resetting.

**Dave Jones:** There we go. So, hey, the micro's working. Everything's hunky-dory. So, something blew the ass out Well, all this intermittent track in that mains input filter there. Go figure. One thing I'm definitely going to do is replace that crusty, noisy fan with a modern, silent one.

**Dave Jones:** Definitely do that mod. Now, one of the good things about this amp is that it's got differential inputs, too. Here it is. It's uh you can either select source A or source B as single-ended. So, you can actually use it as a switch to switch between two input signals, or A minus B is, of course, uh the difference. So, you get a differential input. And, of course, we've got those on both channels. So, two totally independent uh channels, as we saw, two totally independent boards on there.

**Dave Jones:** They have uh they'd have their own isolated power supplies, everything. So, fantastic. And then, you've got your uh input uh gain, of course, for each one. Um so, you can gain it from anywhere from 0 to 60 dB, very nice. And your output uh gain, as well. So, beautiful. All that's left to do is uh feed a signal in and see if it filters, cuz that's all it does. It's a filter.

**Dave Jones:** All right, to test this, I've got my DSA, my dynamic signal analyzer. Why? Well, because I can, and I love dynamic signal analyzers. Um you don't need a DSA to test something like this, of course. All you need is a function gen, a sine source, and your multimeter or your scope, and you can sweep it over the frequency range and determine it.

**Dave Jones:** But, anyway, the DSA will allow us to uh sweep the frequency up to 100 kHz, which, coincidentally, is the uh limit of this thing. So, fantastic. Um what I'm doing is the source output here, I'm generating 1 V RMS of random uh noise. So, there it is, 1 V RMS there. And uh the reason I'm doing random sources cuz this doesn't have a swept sine uh generator. So, what we can do is we can generate random noise. So, it generates random noise over the entire spectrum, and then, over

**Dave Jones:** time, you can average that out and get a flat spectrum response. So, let's actually start that. I've turned averaging on, I've got 100 averages there. What I'll do first is I'll actually show you that noisy input signal. Now, it's working like a scope now, so there's our input signal there.

**Dave Jones:** It's just garbage, okay? So, we can turn that source off, of course, and bang, it drops away to nothing. So, there's our 1-V RMS random noise. And random noise is actually very useful, especially if it's proper random noise, so then you can actually average it out over the cuz the cuz the power in each frequency bin over the time is going to be the same, so you can average that out.

**Dave Jones:** So, anyway, let's turn that back to our spectrum, and then let's start. Here we go. And you see how it starts out noisy, but then it it eventually gets flat. So, I'm just feeding the source directly to the channel one input, okay? So, it's flat over the entire frequency range.

**Dave Jones:** Now, what we'll do is we'll put our filter, our Stanford Research filter, in series with that, and we'll set it to 50 kHz smack in the middle, and we should see it go flat and then drop off like a brick almost like a brick wall, cuz this is an eighth-order filter, really high-order filter, so it should have a really sharp fall off right at 50 kHz.

**Dave Jones:** Pretty much smack in the middle there. All right, we're in the low-pass side of it. The other side is an identical channel, but it's a high-pass filter. So, it's automatically defaulted to 5 kHz at the moment. Well, let's just ramp that up. You notice how it just shows up enter like it's and don't believe it changes like dynamically as you go. You got to hit enter before it actually applies it.

**Dave Jones:** So, that's why it's warning you there with the big enter thing. So, that dynamic speed there isn't bad. There we go. Spot on 50 kHz. We'll enter that in. So, that's our low-pass filter. Our input gain 0 dB, our output gain 0, so we should be hunky-dory. So, let's just go back to here, and uh run this again. And where cursor is at 51.2 kHz at the moment, so just before that cursor, we should see that drop off if this sucker works. So, let's press start again.

**Dave Jones:** Hello. Look at that. There we go. It's not exactly a brick wall. It's uh It's dropping off. But, there we go. It works. What if we lower the frequency down to say 10 kHz and see what happens. There we go. I won't bother zooming in on the DSA. There we go. Let's run that again.

**Dave Jones:** And we should see it drop off about here. Ah, calibration. Come on, give me a break. Come on. You can do it.

**Dave Jones:** Come on. Here we go. Averaging progress. There we go. It's dropping off. Ta-da! Like the proverbial brick wall. This thing as a first order approximation, ha, pun intended, um works. I'm very happy. That is a winner. Awesome. Well, at least the uh low-pass filter stage. Let's try the high-pass filter. So, what we'll do is we'll just move this over here. These BNCs are a bit crusty.

**Dave Jones:** And uh ooh, overload. That's not good. So, that doesn't sound good. 50, nice round number. Okay. Nah, don't like the look of that overload. Uh Okay. So, uh let's run it. No. Not getting a good vibe there. And of course, we should see a flat line here and then drop like that. But, no.

**Dave Jones:** No, we've got nothing. This thing No. So, we could have a fault in unless it's a PEBCAK and I'm using this wrong. Um Uh because I haven't used one of these in donkey's years. Absolutely donkey's years. and I haven't read the manual, of course. So, I know those overload indicators aren't good and you can whack the filter in and out, too. It can just start bypass it. That's very handy, but no no, I don't like the look of that at all. Input A No.

**Dave Jones:** No. We could have a loser on that channel. Woohoo! Excellent. More stuff to troubleshoot. But, this channel over here, the low-pass one, looks like it works a treat. Beauty. Now, I'm back on the low-pass filter again and curiously, um I've selected the filter out. So, I've pressed the filter out button and well, as you can see, the filter is still in.

**Dave Jones:** So, I don't know. There could be an issue there, but no big drama. And of course, the reason we're seeing a relatively gentle roll-off here is because we're in linear axes mode. So, go to your more traditional log axes and you'll see it drop off much faster.

**Dave Jones:** There we go. It's got like 80 dB stop band attenuation and if we wanted to, we could try and measure all that sort of stuff, but I'm not going to do that today. I'm quite happy that at least this low-pass filter section seems to be working. Awesome. There we go. I auto scaled that and we can start to see the roll-off performance. Switched it down to 10 kHz here, so that's 100 kHz.

**Dave Jones:** That's 10 kHz cuz it's a decade cuz we're a log scale and 10 kHz, this would be 1 kHz. So, I could drop that down to 1 kHz just for entertainment and well, just overshot there. I've got to get it spot on. Here we go. Start. Boom! And we'll start to see it drop off at that 1 kHz mark.

**Dave Jones:** Beautiful. No, wait. Hang on. I just tried that high-pass channel again. I just repowered it and the The LEDs have gone off and I set it to 10 kHz, and it's bang on. So, I'm not sure what the hell is happening before, but that works. 10 kHz high pass, no worries whatsoever.

**Dave Jones:** Wow, this thing's fully working. Okay, uh well, uh fully working. Haven't done complete tests on it yet, but hey, I'm happy with that. And what I've done here is put it in band pass configuration. So, my source is coming into here where I've set a high pass filter at a frequency of 10 kHz. So, anything above 10 kHz it's going to allow, and then the output of that goes over to the input of the low pass filter, and then the low pass filter set to 20 kHz. So, anything

**Dave Jones:** below 20 kHz is going to be let through. So, bingo, we've now got a band pass between 10 kHz and 20 kHz, and the output comes from here, back over, and look at that. Woohoo! There is our band pass filter characteristic. 10 kHz to 20 kHz. Bang on. Now, I just switched this to AC coupling mode and just permanently uh set it into overload. Not sure how to reset the uh overload on this thing.

**Dave Jones:** Might have to read the manual. Um but curiously, switching from AC to DC coupling, as you'd expect, I heard a relay. But this channel over here, the low pass filter, there's no relay. I don't hear it. And same with filter in and out. I would have expected that possibly to be a relay bypass, but I can't hear it. So, anyway, there you go. That's a repair, in quote marks, of a Stanford Research SR650 dual channel uh filter. And it's a very nice instrument. If you can pick up one of

**Dave Jones:** these, like I did, for just over 100 bucks, uh and looks like it was just the uh mains input uh blowing then really there's not much else that can go wrong with this. Um I believe this uses the uh FET input just like the uh preamp.

**Dave Jones:** They've Stanford Research have a preamplifier and it's notorious uh the front end on that for blowing the input FETs, but you can get a replacement uh FETs for those and uh actually repair one of those uh pretty easy. I can't remember the model number of that offhand, but uh the SR650 I believe uses that basically the same uh front end on that. So, it could be a similar story with the uh FET inputs, but it seems to be working an absolute treat. So, anyway, I'm going to uh repair the um I

**Dave Jones:** can't put the cover back on the mains filter up there with that bodged wire on it. It doesn't sort of work. Maybe I'll sort of replace it replace that noisy horrible fan in there. Uh got to clean up the BNCs on these things and um yeah, just generally do some more testing on it, but hey, that's a winner. That's band pass. There we go. That's exactly what I wanted. So, now I've got myself a really powerful uh dual channel programmable filter. A very handy addition for the lab and if you need

**Dave Jones:** something like this, you need it. They're great to have lying around. You don't use them all the time, but valuable bit of kit for your lab if you can pick one up like I did. Very nice. All right, I was hoping for something a bit more, you know, an electronic type repair, but hey, uh it's a mains track. Uh whatever.

**Dave Jones:** Catch you next time.
