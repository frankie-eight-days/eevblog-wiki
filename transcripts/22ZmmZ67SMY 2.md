---
video_id: 22ZmmZ67SMY
title: EEVblog 1752 - Texas Instruments SCREWED UP the NE5532!
url: https://www.youtube.com/watch?v=22ZmmZ67SMY
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 34, "3": 46, "4": 61, "5": 71, "6": 86, "7": 98, "8": 109, "9": 122, "10": 134, "11": 145, "12": 160, "13": 183, "14": 189, "15": 201, "16": 224, "17": 248, "18": 256, "19": 269, "20": 291, "21": 298, "22": 312, "23": 343, "24": 359, "25": 372, "26": 396, "27": 407, "28": 421, "29": 431, "30": 443, "31": 466, "32": 477, "33": 488, "34": 500, "35": 512, "36": 523, "37": 539, "38": 550, "39": 561, "40": 587, "41": 606, "42": 621, "43": 644, "44": 671, "45": 679, "46": 694, "47": 705, "48": 723, "49": 738, "50": 755, "51": 766, "52": 782, "53": 798, "54": 809, "55": 822, "56": 836, "57": 864, "58": 872, "59": 890, "60": 905, "61": 915, "62": 929, "63": 942, "64": 969, "65": 979, "66": 991, "67": 1007, "68": 1015, "69": 1034, "70": 1046, "71": 1058, "72": 1076, "73": 1093, "74": 1109, "75": 1140, "76": 1165, "77": 1187, "78": 1202, "79": 1216, "80": 1225, "81": 1245, "82": 1268, "83": 1281, "84": 1292, "85": 1303, "86": 1319, "87": 1331, "88": 1357, "89": 1372, "90": 1385, "91": 1403, "92": 1418, "93": 1428, "94": 1446, "95": 1458, "96": 1466, "97": 1480, "98": 1504, "99": 1522, "100": 1540, "101": 1551, "102": 1560, "103": 1570, "104": 1588, "105": 1596, "106": 1608, "107": 1623, "108": 1651}
---

**Dave Jones:** Hi, Texas Instruments or TI have screwed up big time. And if you're not careful, this could actually cause great damage to your product, your company, whatever, if you're not paying attention and you happen to be using a design specification of a common jelly bean part which they've just changed.

**Dave Jones:** Even though they've kind of sort of notified you of it, they made a big change that could impact a lot of people. And we're talking about the classic NE532 dual audio op amp.

**Dave Jones:** And this is a classic Jelly Bean part. It's been around for decades. It was in my op amp jelly bean video. And Texas Instruments and just Texas Instruments alone because it's multis source.

**Dave Jones:** That was what makes it a jelly bean part. But only Texas Instruments have changed the process node on this chip late last year and they've made a major spec change that could cause you to come if you actually are relying on this specification.

**Dave Jones:** So let's take a look at it here. Here's the latest data sheet. It originally came out in November 1979. That's what makes it a jelly bean. And this is the latest data sheet revised December 2025.

**Dave Jones:** And this is what they call revision K of the data sheet. And over here we have a data sheet from January 2015, the previous version or revision JB Buggeroff Copilot.

**Dave Jones:** So the classic audio jelly bean component used in all, you know, and it's pretty decent performance. In fact, a lot of companies will specify like they'll use it as marketing material.

**Dave Jones:** Oh, and our products got NE532 op amps in it. No worries. you can, you know, you know, it's going to have really good audio performance cuz this is not the highest performance op amp out there, but it's pretty decent.

**Dave Jones:** You know, low THD and everything else, decent drive and all the rest of it, right? It's it's really quite a popular audio op amp used in, I don't know, countless products, but they've changed the silicon.

**Dave Jones:** And let's have a look at what they've changed. Right, the banner specs here. Okay, you might notice Unity game bandwidth 12 megahertz. The previous one was 10 megahertz. Beauty, no worries.

**Dave Jones:** More game bandwidth product. As long as it doesn't come with any other instability issues, no problem. Okay. Improve the specs is always good for the same part. Common mode rejection ratio is exactly the same.

**Dave Jones:** High voltage DC gain is exactly the same. High slooh rate 5 volts per microcond typical. The older version of the silicon high slooh rate 9 volts per microscond typical.

**Dave Jones:** It's slower and the older variation of the chip peakto peak output voltage swing 26 volts typical um into 600 ohms because the double 532 is famous for being able to drive you know decently at high voltage 600 ohm audio loads right they don't have that over here they've removed it but the good thing about these big manufacturers they tell you all this stuff and they note the changes

**Dave Jones:** in the data sheet so in the data sheet they do actually list the changes from RevJ which is the old one 2015 to the new Rev K one here.

**Dave Jones:** We'll go through it because there's a real shocker. Stick around that you're going to come a gutser on. And um here's the old one over here from right from 2009 to 2015.

**Dave Jones:** It didn't change at all. They just added some typical applications and things. But look at the stuff that's changed here. Now, if you're a serious manufacturer designing products, then you're going to a you're going to be buying them from legitimate sources and uh b you're going to get automatically notified via said legitimate sources like, you know, your catalog providers like your big ones like Digi Key and

**Dave Jones:** Mouser or uh from your local, you know, authorized rep for your particular part. In this case, uh TI and TI publish what's called product change notifications or PCN's. So, it's quite common if you've bought parts from Digi Key or Mouser or your uh authorized provider um before, you might get an email saying, "Oh, there's a product notification change coming that we've we've actually changed the silicon on

**Dave Jones:** here. We've made these sorts of changes. Just be aware, you know, there might be a new part number you have to move to or, you know, something like that, right?

**Dave Jones:** Or it's end of life, for example, last time buy." So the purchasing departments at companies um big companies uh can get notified or the engineers can get notified and then they can notify the uh you know re-evaluate the chip to make sure it still works.

**Dave Jones:** If you're making a million widgets a year you know these subtle changes can actually matter cause you to come a gutsy. You don't want the manufacturer to suddenly change the die on you which changes some key specification that you just happen to rely on by Murphy's law and then it goes automatically into your product because it's the same part number and your purchasing department goes well I've got the proper part

**Dave Jones:** number I've ordered the right part but you know not our fault and it makes it way into the product out in the field and it fails out in the field in your million widgets.

**Dave Jones:** You can really come a gutser. So, um, they issue these product change notifications and sure enough, we actually have the product change notification for this 532 here. But it's not just the 532.

**Dave Jones:** If you look down here, impacted products, it's the NE532, it's the LM833, it's the uh 4560, it's the classic 4580. Another jelly bean, it's the SA uh 5532. difference between the NE and the SA is that the SA is extended uh temperature range you know like a commercial industrial uh temperature range is just wider but apart from that same part so yeah it could impact all of these

**Dave Jones:** devices because they've changed the process node the silicon wafer node um and or fab um that they've they've made changes and they go into all the details here if you want to get into the nitty-gritty of it right so here's the PCN number and uh proposed first ship date 2024.

**Dave Jones:** Okay, so it's been around for a while, but yeah, but they didn't revise the data sheet until December 2025. So, I'm not sure what's going on there. So, they made changes to where the actual uh chip is uh assembled.

**Dave Jones:** They've made changes to the packaging shipping, made changer fab material, and the wafer fab process. They've changed all these things which can impact the specifications. So it looks like they've changed it from Mexico to Malaysia have it or something like that and they're changing from I this copper node to this copper mode you know I don't know whatever.

**Dave Jones:** So they've changed the design of this thing. Let's go and see what major things they've changed. So the major changes they've made as I said they've improved the game bandwidth product.

**Dave Jones:** Okay that's fine. They've reduced the slooh rate from 9 volts per microcond to five. So if you were relying on the slooh rate for whatever reason, this exact same part number, remember they haven't changed the part number, anything.

**Dave Jones:** They've simply uh given you this notification that oh these design changes are happening and well if it screws you up, too bad. It's your fault for not rereading the new data sheet.

**Dave Jones:** They've removed the peakto peak voltage swing as we saw. They they actually remove that from page one. See, they tell you all this stuff, but here's one of the here's one of the biggies that potentially could come a gutter.

**Dave Jones:** Change supply voltage positive and negative from uh 22 volts, that's plus - 22 volts to plus - 18. They've changed the maximum supply voltage and the if you know your jelly bean parts, the uh532 has always been a like plus - 22 volt part.

**Dave Jones:** They've changed the input voltage positive and negative from uh minus 10 and + 10 to minus15 and + 15. Okay, looks like they might have improved that. Uh the storage temperature, they've improved that.

**Dave Jones:** Okay, here's another change which you which might come a gutsa potentially out in the field because it's hard to sort of you know test and and model. Well, you know, it's not easy.

**Dave Jones:** Um the HBN, that's human body model. That's basically its susceptibility to static charge on the pins. It's changed from 2,000 volts to they've h haveved it to a,000 volts.

**Dave Jones:** So if you were relying on the 2,000, you know, ESD protection on the inputs, they've got wimpier inputs in this new design. So they've lowered that to a,000 volts.

**Dave Jones:** Unbelievable. And they've removed the maximum peakto peak output voltage swing, the small signal differential voltage amplification, the maximum output bandwidth, the output impedance, and the cross to talk to attenuation.

**Dave Jones:** They've removed all these things from the spec table. Unbelievable. But hey, they have lowered the current from 8 milliamps to 6 milliamps. Winner. They removed the overshoot factor. Why?

**Dave Jones:** And again, they've changed the slooh rate. So again on the right hand side here, this is the previous data sheet, the old uh revision. And you can see we've got a whole bunch more specs here than we've got here.

**Dave Jones:** They've actually removed them in this new data sheet. You'll notice that VOP, the maximum peakto peak output voltage swing, and they specify that into 600 ohms, right? Plus minus 15 volts.

**Dave Jones:** The this chip is famous for like being able to drive 600 ohm loads. No worries. um they've actually removed that completely from the data sheet. Although they do kind of imply over here that um 600 ohms like it can kind of sort of still drive 600 ohms but you know doesn't give you the warm fuzzies that there have move that entire spec line and they've removed BOM which

**Dave Jones:** is the maximum output swinger bandwidth again into 600 ohms here at plus - 10 volts 140 kHz they've actually removed that they've just got the unity gain bandwidth now this is nuts and they've removed the output impedance >> [laughter] >> at.3 ohms and that that spec doesn't exist anymore.

**Dave Jones:** No wonder it probably maybe can't drive the 600 ohm load. And they've removed the cross talk attenuation. That's just gonsky. Poof vanished. And as we saw the slooh rate that's been lowered from 9 volts to 5 volts per microscond.

**Dave Jones:** Equivalent input noise is typically eight. That's kind of stayed the same. Oh, small mercies. So they're effectively using a smaller process node which leads to wimpier transistors basically um like reduced susceptibility or increased susceptibility to electrostatic uh damage and reduced output um gruntiness drive capability.

**Dave Jones:** So let's have a look at some other manufacturers on semi uh for example um yeah once again 600 ohms they're quite proud of it no wuckers and voltage range to plus -20 volts here but it can actually do uh the maximum figure is actually plus -2 volts here no worries and it can drive into those 600 ohm loads no no no workers whatsoever let's check out old school Philips data

**Dave Jones:** sheet for example plus minus 20 volts not this 18 volt rubbish it'll will do. Plus - 22 volts. There it is. There. Old school fair child. Plus - 22 volts.

**Dave Jones:** What do you know? It's almost as if it that's the jelly bean spec everyone expects. Here's the TI data sheet from June 2002. Once again, they you know got the 600 ohms.

**Dave Jones:** They got plus - 20 volts um wide supply range with of course the maximum uh value plus - 22 volts. And here's the TI data sheet going back to 1990.

**Dave Jones:** Um, once again at plus minus 20 volts, right? They've been manufacturing this for like 40 years or whatever. And plus - 22 volts. Let's go to LCSC and look at some, you know, Asian source 532s cuz this is a jelly bean part.

**Dave Jones:** You can get it from dozens of different manufacturers. HG semi plus minus 22 volts. Do semi. What do you know? Plus minus 22 volts. Sikor or whatever you however you pronounce it.

**Dave Jones:** I'm shocked. Plus - 22 volts. To be fair, I was able to actually find one brand here. Hun Jang. Um, that's plus - 18 volts here. Exactly as per the new TI uh revision that they've done.

**Dave Jones:** And sure enough, maximum absolute maximum rating. There it is. plus minus 18 volts. So TI, the new designers at TI have found um kindred spirit here in Hungju Wang.

**Dave Jones:** And here's another absolutely wild TI change that has nothing to do with uh the change note of this the process node or whatever that they've changed another one of their audio amps, the OPA uh 134.

**Dave Jones:** It's the high performance sound plus trademark audio operational amplifier. Look at this. Oh, 8% uh THD. That's like homeopathic quantities of distortion there. Um, you know, so like it's it's the duck's guts, right?

**Dave Jones:** Just take a look at this pin out. Just take a look. Memorize that. See if you notice any difference with uh the previous version of the data sheet. Here it is here.

**Dave Jones:** Exactly the same chip, but this dates from October 2015. Here, let's go down. Same homeopathic quantities of distortion here, right? But uh let's have a look at the pin out.

**Dave Jones:** Look at this offset trim. Offset trim. [laughter] We can go to Burr Brown because these are originally Burr Brown parts. There's a lot of Burr Brown fanboys out there, right?

**Dave Jones:** Still that homeopathic quantities of distortion. And sure enough, offset trim. Offset trim. But in this new one, the November 2024, they've not connected. They've removed the offset trim. So if you design your products around this super schmicko audio op amp and you had your wanted to make it even better for your audio full product, you got to, you know, tweak that offset trim either manually or, you know, with that

**Dave Jones:** tongue at the right angle with your gray beard. um or you did it like automatically you had like an auto circuit that sort of um did trimmed the offset.

**Dave Jones:** If you designed your product around that and you suddenly built your new product, it it's not going to work anymore. It's not connected. What? And you got to remember everything we've been talking about here, these are the same part numbers, exactly the same.

**Dave Jones:** Your purchasing department would not know the difference. your really strict bill of materials where I've gone in this before. You'll have like your main supplier, then you'll have alternative approved suppliers and then your purchasing department can, you know, buy any one of those approved uh suppliers.

**Dave Jones:** This is the same part number. It's not like it's a -1 or, you know, they added an A or a B on the end of it or something. No, it's the exact same part number.

**Dave Jones:** So for this OPA134, look at all the changes they've made from 2015 version to the 2024 version. Look at this. Here it is. Just casually changed the pin 1 and 8 from offset trim to not connected.

**Dave Jones:** [laughter] What? Changed the headroom from 23.6 to 21.3 dB. Too bad if you relied on the headroom. Slightly worse overload recovery time. change channel separation from 135 dB to 128.

**Dave Jones:** Um, and 126 for 20 kHz. So much for the some premium whisbang, you know, ultra performance audio product if you relied on your channel separation. Sorry about that. You've got your, you know, your 128 channel mixing desk and you're using all these premium opamps worth a million bucks and you're using all these premium op amps in it which cost, I don't know, 10 bucks each or something and all of a

**Dave Jones:** sudden your channel separation's changed. And you build your new mixing console and it's like, what? The channel separation isn't as good. What's going on? We just added plus minus to the input bias current.

**Dave Jones:** Typical. What? It wasn't plus minus before. Maybe it was just plus and now it's it could be negative. Again, they're deleting like 600 ohm specs. What? Anyway, that's just another random example, right?

**Dave Jones:** But um yeah, this is just nuts. No new part number, no nothing. No 532-1 or something like that or just announcing that, oh, sorry, we're just going to discontinue uh the part because well, it's not the same spec.

**Dave Jones:** Oh, but no, we can't lose sales on our own classic jelly bean part. And if we chose a new part number, then well, people aren't going to buy it anymore.

**Dave Jones:** So, it's almost like like they deliberately kept the same part number and changed a some major specs in here with the biggie being the maximum supply voltage. It's right here plus - 18 volts where for 40 years it's been plus - 22 volts absolute maximum, right?

**Dave Jones:** And this is absolute maximum rating, right? But just imagine you've got like your I don't know reference monitor speaker or something. I've done tear downs of those before. And you're using like you don't have a regulated uh power supplies.

**Dave Jones:** You just use your full wave bridge rectifier, your big big ass filtering on there. And you get your plus minus uh rails and you aren't quite sure what it's going to be at because you got got a huge mains.

**Dave Jones:** You know, you can have like plus minus uh variation on your mains input. And if you're, you know, like I'm here in the lab, 245 volts, I'm on the high side of what we can, you know, what mains is allowed here and my speakers might output, you know, that bridge rectifier might output 19 volts or something.

**Dave Jones:** What happens then? Yeah, it might work for a while and then your product just dies out in the field because you've um slipped in this new chip with total like with the design change that can't tolerate the voltage that you designed it for.

**Dave Jones:** Unbelievable. But hey, we notified you. But even then, they're flat out lying to you. Cuz look down here, the bit that you care about on this uh change note, anticipated impact on form, fit, function, quality, or reliability, positive or negative.

**Dave Jones:** None. There is no impact. They cla ti claim there's no impact from changing the maximum voltage spec of 22 volts down to 18 volts absolute maximum that we've had you know like a change that has been industry standard for 40 years there's no impact from that no impact from having your slooh rate unbelievable right there if your company has come a gutsa because you read this note and it

**Dave Jones:** it had none down here so you authorized your purchasing department to keep on buying and manufacture your million widgets and your million widgets get out in the field and then a month later they all fail and it cost your company a squillion dollars then well aren't TI might be hearing from their lawyers cuz that ain't true impact none now some people might be wondering does this apply to the single variant the uh

**Dave Jones:** famous double 534 variant uh no it it doesn't um the double 534 and double 532 haven't always been exactly the same design. They've been close enough to everyone goes, "Oh, the the 32 is the dual version of the uh 34." And that's, you know, generally true, but I think there are some subtle uh differences in there.

**Dave Jones:** But anyway, uh no, the 534 is still plus minus 22 volts. And this is the latest data sheet direct from their uh website, November uh 2014. So, they have not changed a single version.

**Dave Jones:** They've only changed the dual version 532. And if we look at uh JRC or Japan Radio Corp, which is like probably one of the biggest uh Asian variant names, um now owned by uh Nishimu Micro Devices, Inc.

**Dave Jones:** You can still find some JRC uh data sheets and stuff, but um yeah, once again, plus minus 22 volts banner spec plus - 2,000 volts human body model. They've have that.

**Dave Jones:** TI have now have that. And it's like come on. Now, if you want to go down another TI change rabbit hole, um the LMHR6518, which is in a whole bunch of oscilloscopes, if you've ever seen the uh tearowns at the front end of the oscilloscopes, and there's a thread on the EV blog forum, I'll have to link it in here.

**Dave Jones:** And um here's the Texas Instruments forum again. Um apparently there's an offset. They they made a silicon change and the off there's an offset problem there that if you have a sustained offset it can offset voltage which you'll have on the front end of a chip which this of an oscilloscope which this chip's used in then um it can it can damage the chip and there's people

**Dave Jones:** on the forum who've actually um recognized that and there's a response from um TI here one of the people that worked on it so their forum's quite good um but yeah so there's some sort of DC offset anyway another rabbit hole there from a potential change.

**Dave Jones:** And it's not just a process change. They've actually changed the design of this thing. So here's the old one over here. They actually gave you, this is the 2015 version.

**Dave Jones:** They gave you the entire schematic here. They've removed the entire schematic and they give you just a functional block diagram. And you'll notice that the inputs here, these are um PNP transistors.

**Dave Jones:** Look on the input PNP. What have we got on the input over here? NPN. Look, they've changed the front end topology of how this works. No wonder it changes like the human body model, the ESD susceptibility on this thing.

**Dave Jones:** No wonder that's harved cuz like the front end has changed. So what have TI done here? Why would you change this classic 40year-old I THINK IT'S 45 years old now?

**Dave Jones:** Yeah. 1979, right? Geez. like you know over 45 year old design to like completely change the input configuration. Are they is it like another op amp and they've just tweaked another op amp uh and rebadged it as the 532 because it's it's they've changed the bloody design of the classic jelly bean part.

**Dave Jones:** I granted I haven't looked to see if any other um manufacturers have exactly the same schematic here, but you would think that's something you wouldn't change from 2015 to 20 uh 26 or 2025 whenever a change was made.

**Dave Jones:** That's nuts. What's going on? Yeah, here's the on semi-chip. Sure enough, look, NPN input. You'll notice that they've got the backto-back protection diodes here. They had them on the other one.

**Dave Jones:** They just showed them as transistors. Check this out. This Jeong Yang whatever um one that I said matched the plus - 18 volts here. Lo and behold, PNP input pair rather than the NPN in the original design.

**Dave Jones:** H another interesting tidbit, the classic LM 317 adjustable voltage uh regulator. Another jelly bean, the 317M. Well, they introduced a new part, but at least they gave it a new part number, the MQ.

**Dave Jones:** So, they call that the MQ is called the new chip. Um, qualified for automotive applications. And if you go down to the specs down here, you can see legacy chip and new chip.

**Dave Jones:** Legacy chip, new chip, legacy chip, new chip, legacy chip, new chip, new chip, legacy chip. Right? At least they tell you and they gave it a new part number up here and a good detailed bill of materials for your purchasing department for your product would actually flag that.

**Dave Jones:** Right? A good purchasing officer would come in and said, "Oh, look, they're they're offering us the LM 317 MQ. Is that the same as the LM 317?" And you go, "Oh, I don't know.

**Dave Jones:** Let me go check." And you read up the data sheet. Sure enough, right, it's very clear that there's a legacy and new chip and like all the specs have changed, right?

**Dave Jones:** So, you would have to qualify that part. Simple voltage regulator, but you might have to re-qualify it cuz you don't know. It might it might drop out differently. It might oscillate, for example, with the different loads and different um bypass caps and things like that, right?

**Dave Jones:** So, yeah. So, you don't know. You go, hold off buying that one until we can re-qualify the part. So that's what happens when you add the extra part number either a letter an extra letter at the end because as a design engineer your job or it might be an huge company it might there might be an engineer dedicated to creating a bill of materials uh like this that would

**Dave Jones:** specify the exact detailed part number like right down right down to like all these detailed options here uh for example. So there could be like there's better examples of this but you know there could be like huge variations in the part numbers and for different packages and things like that and for different even specifications.

**Dave Jones:** So you've got a a good uh design engineer will build that into the bill of materials. must use this part and here's the other qualified parts. And then the good purchasing people will know, okay, I'm not I'm not risking my job by buying any other part except from this supplier with this exact part number.

**Dave Jones:** And you'll give them the links and everything and they'll follow that to the letter. Um, the worst thing you can do is just go, "Oh, buy an LM317. You know, she'll be right.

**Dave Jones:** No worries." Right? You're just going to come a gutter doing that. And same thing for the NE532. You can now come a gutsa. So there you go. I waffled on for long enough.

**Dave Jones:** Bloody ti. What the hell are they doing? What were they thinking when they did this? It's it's very deliberate what they've done. But have they goofed up and said, "Oh no, there's no changes.

**Dave Jones:** No, there's no change to the quality, reliability, fit, form, function That changed a whole bunch of stuff. It's just crazy. Unbelievable. Anyway, thoughts and comments down below and I'll link in there's an EV blog forum thread on this.

**Dave Jones:** So, I won't put the usual forum thread. I'll link it directly to uh the forum thread I started on this and everyone's yapping on about it. And there's all sorts of other examples out there.

**Dave Jones:** So, if you've got another good example of a semiconductor manufacturer changing the part on you without changing the part number and you've come a gutsa, leave your stories in the comments down below.

**Dave Jones:** So yeah, big trap for young players this sort of thing and which is why you buy from legitimate suppliers like Digi Key or Mouser for example, they'll automatically contact you with these change notifications, end of life notifications and and things like that.

**Dave Jones:** um which all the good semiconductor companies will uh actually produce these change notifications and push them out um through their various channels and it eventually gets to you and go oh okay I've made some changes but you don't make this sort of change without changing the part number what are you doing ti unbelievable anyway comment down below catch you next Time.

**Dave Jones:** >> [music]
