---
video_id: BnKDj4ed40Y
title: EEVblog 1387 - MOSFET Repair Replacement Search
url: https://www.youtube.com/watch?v=BnKDj4ed40Y
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 23, "2": 53, "3": 74, "4": 98, "5": 113, "6": 131, "7": 150, "8": 164, "9": 183, "10": 196, "11": 216, "12": 240, "13": 256, "14": 278, "15": 292, "16": 308, "17": 329, "18": 347, "19": 367, "20": 382, "21": 394, "22": 412, "23": 426, "24": 442, "25": 463, "26": 475, "27": 492, "28": 508, "29": 525, "30": 539, "31": 556, "32": 572, "33": 590, "34": 607, "35": 627, "36": 640, "37": 663, "38": 678, "39": 693, "40": 710, "41": 731, "42": 748, "43": 764, "44": 785, "45": 801, "46": 819, "47": 837, "48": 855, "49": 869, "50": 883, "51": 899, "52": 915, "53": 931, "54": 950, "55": 970, "56": 986, "57": 1006, "58": 1021, "59": 1041, "60": 1059, "61": 1078, "62": 1097, "63": 1110, "64": 1129, "65": 1144, "66": 1164, "67": 1182, "68": 1198, "69": 1209, "70": 1228, "71": 1249, "72": 1267, "73": 1280, "74": 1293, "75": 1308, "76": 1327, "77": 1342, "78": 1361, "79": 1377, "80": 1389, "81": 1405, "82": 1421, "83": 1442, "84": 1457, "85": 1478, "86": 1494, "87": 1514, "88": 1535, "89": 1549, "90": 1561, "91": 1574, "92": 1587, "93": 1603, "94": 1618, "95": 1631, "96": 1645, "97": 1656, "98": 1671}
---

**Dave Jones:** Hi, it's component replacement source in time, because sometimes when you're doing a repair and you've got a failed part, it's, Murphy says, it's not going to be a part that you actually have in stock or necessarily an equivalent part. Anyway, I was doing a repair video, which you'll see in a future video, and one of the things which has failed, there was more than one, is a MOSFET.

**Dave Jones:** So, I've removed the heatsink here. Focus, you bastard. Not sure if you can see that, but anyway, it's an MDF18N50. So, let's jump back over to the datary sheets. This is from a company called MagnaChip. Now, of course, I want to do this fairly quickly, so I could probably, you know, maybe find this on DigiKey or Mouser overseas, but of course, I'm from Australia and I, you get it relatively quickly, but, you know, it'd be nice if I had it, like, either side.

**Dave Jones:** So, I thought I'd have a quick look to see if I could find a suitable replacement, because I don't seem to be able to find the MDF18M50, or here's where we have to get into the intricacies of parts and part numbers and prefixes and things like that.

**Dave Jones:** Anyway, I can't find this part on either Element 14 or RS components, which are the two major local, you know, catalogue. So, let's take a look at the data sheet here and see if we can find a suitable replacement, which I can hopefully source locally in stock, because just because you're buying it from Farnells or RS here in Australia doesn't necessarily mean they have it in stock here in Australia.

**Dave Jones:** In fact, Murphy will get you, yet again, guarantee the part you need, it'll be five, yeah, Farnell will have it, but it's in their UK, or RS will have it, but it's in their UK headquarters or whatever. So, anyway, we need to get into part numbers and prefixes.

**Dave Jones:** So, we're looking at an N-channel MOSFET here, it's a grunty little beast, it's 18 amps at 500 volts, 0.27 ohm nominal on resistance, and it's used in, actually, the power factor correction circuit in the power supply, which I'm actually repairing at the moment.

**Dave Jones:** So, you know, 240 volt mains power factor correction, so it needs to be a fairly grunty little MOSFET. And, look, it says this power supply PFC, power factor correction. Shock! High current. High speed switching, blah, blah, blah. So, we have to get into looking at the part number here.

**Dave Jones:** So, you know, you can just go search Google, you can go search your favourite catalogue supplier for the part number, but in this particular case, I can't find it. Look, if I even copy that into DigiKey, for example, I'm not going to find it.

**Dave Jones:** Do the same thing for Mouser here, and MDF 18N50, spinning its wheels, 0. So, two of the world's biggest catalogue suppliers. Don't have it. Then you can go to something like findchips.com, for example, and, well, arrow, okay, no, zero stock in America, 250 in Europe.

**Dave Jones:** There we go. I don't know, those in Europe tell me it's probably some broker or something like that. RFQ is request for quotation, so they don't even give you the price. They probably source it. They may not even have it. They might source it from the grey market.

**Dave Jones:** And, as you can see, maybe one in-chain semiconductor has, like, one in stock. Come on. Technically, that's all I need, though. Then another search engine is Octopart, for example, and they basically are findchips and Octoparts, and there are some others. They will search, like, all your different catalogue suppliers for the parts.

**Dave Jones:** Once again, arrow, you can request a quotation for 4,000. Oh, look, Winsource Electronics have 5,524 in stock at $1.20 each. Seven days delivery. I have no idea who Winsource Electronics is. But, anyway, as you can see, this is a, you know, fairly... Fairly obscure part if you're taking the actual full part number like this.

**Dave Jones:** In this particular case, this is where we have to start breaking this up. Now, a part number for this MOSFET is not always the case, but usually, you know, the number here, the 18N50, is going to be the actual part number. And the, usually, a lot of parts will have a prefix like this.

**Dave Jones:** In this particular case, MDF seems to be specific to a magna chip. Now, if you're familiar with your MOSFET nomenclature, do I get that right? Naming. If you're familiar with your MOSFET naming, you might be familiar with the 18N50. And you might see down here, 18, 18, 500, 50.

**Dave Jones:** That's not a coincidence. And N is not a coincidence for N-channel MOSFET naming typically follows this sort of formula. The first digit here will be your current. In this particular case, 18 amps. N is, of course... N is, of course... N is, of course...

**Dave Jones:** If you wanted a N-channel, if you wanted a P-channel version, that would have a P in it. And 50 is not 50 volts, it's 500. So, right off the bat, we should be able to go search for an equivalent 18N50. And pretty much any 18N50 from any manufacturer should do the job.

**Dave Jones:** I mean, you'd really have to have a bad day with Murphy's Law to see that only one manufacturer's specific type of MOSFET worked in your circuit. It's, you know, it's not going to be that critical. So, any 18N50... 18N50 should work. But if we go over to element 14, and you type in 18N50 here...

**Dave Jones:** Wah, wah, wah, wah. They have no 18N50s. You type it into RS Components here, and I tweeted this. It corrected me. Corrected from 18N50. No, I meant exactly what I typed, RS. Thank you very much. Do not correct me to 18250. Bugger off.

**Dave Jones:** So, digi-key. We type 18N50, and bingo. We're going to find a whole bunch. Look, we've got oscillators, voltage supervisors, and, you know, all sorts of stuff. But we want transistors, MOSFETs, singles. There's 18 different devices. And what do you know? 17 amps, 18 amps, 19 amps, 20 amps.

**Dave Jones:** So, we scroll down here. We've got Onsemi, Vishay, Rochester, and Ixis down here, of course. You know, not in the package we want. Now, I do ultimately want to find a local source, but I'm just showing you the digi-key search here. Because a lot of people will be using this.

**Dave Jones:** The first thing you want to search for, of course, is in-stock. You want to tick that little in-stock box right there. That bad boy. Can I actually make this bigger? I think I can make this bigger for you. For those on small screens and stuff like that.

**Dave Jones:** Anyway, so we've got several different manufacturers to choose from that have different prefixes. Look, DPF here for Onsemi, Vishay have IRFB, and there's a lot of history behind the name. Lots of name changes over the years, and companies change hands, and all sorts.

**Dave Jones:** Lots of things. Anyway, the first thing you want is make sure it's in-stock. And the second thing you want is to make sure it's in the package that you want. Because, you know, we might get a little bit of versatility. You might be able to hack in a different version into this heatsink here, for example.

**Dave Jones:** But, you know, really, this is a plastic TO220. So, you know, we want the TO220 package. So it looks like we have to search for more filters here. There we go. TO220. Let's go for that. Apply filter. There's six remaining, and we'll only get...

**Dave Jones:** the TO220 packages. And sure enough, like, there's 9,000 in stock, 2,000, blah, blah, blah, $3.88, no wuckers. Like, you know, like, you wouldn't even get the minimum required for postage. But, as you can see, these are all 500 volt, 18 amp equivalent. They should be pretty much equivalent MOSFETs.

**Dave Jones:** So let's choose, say, the Onsemi one here. We'll open the data sheet for that. So let's whack them side by side here and see how compatible they are. But, as I said, they're not as compatible as the Onsemi. In an application like this power factor correction device,

**Dave Jones:** as long as you've got 500 volts, 18 amps, you've got a relatively similar RDS on and stuff like that, it, like, all the other, you know, the huge number of parameters here, like, there's a large number of actual parameters in a MOSFET. Just, you know, check these out.

**Dave Jones:** It doesn't really matter for that application. If you're designing something, it would be different. But if you're just looking for a replacement MOSFET here, then, you know, no wuckers. She'll be right. No worries. So this is the MagnaChip one. You know, drain source voltage, we're talking 500 volts.

**Dave Jones:** We're matching that over here because, of course, it's the exact same part number. The continuous drain current is 18 amps here. 100 degrees, it's only 11. Continuous at 100 degrees, it's 10.8. So, you know, like, at a greater thermal rating. So, you know, that's good enough for Australia.

**Dave Jones:** No worries. Pulse drain current, 72 amps. That happens to be identical. You know, maybe you might expect to see some difference. There in the pulse drain current, perhaps. Power dissipation, 37 watts. This thing's not going to be dissipating 37 watts, let me tell you.

**Dave Jones:** This one here doesn't even have a maximum wattage, does it? Anyway, we're in the absolute maximum ratings here. So gate source voltage VGS is 30 volts on the original. Gate source voltage, plus minus 30 volts here. Avalanche energy and stuff like that in megajoules, 950.

**Dave Jones:** You might expect to see, like, there's very little difference there. 945 and 950, you know, these are... Pretty darn close parts, actually. I'm pretty impressed. But anyway, they're like the absolute maximum ratings, for example. You know, some data sheets will have things that the others don't.

**Dave Jones:** Like this on SEMI-1 has a breakdown voltage temperature coefficient, volts per degree C. Not seeing that over here, for example. But, you know, like, stuff like that, it doesn't matter a rat. And things where you might come aguts are gate drive capacitance. You know, driving the capacitance.

**Dave Jones:** A lot of problems. With MOSFETs, you actually have driving the gate of the thing. If they've got large input... And here it is. CISS input capacitance here at VDS, 25 volts. I don't know what it's actually operating at. You know, we're talking a nominal 2200 picofarads.

**Dave Jones:** That's over here. Input capacitance, 2400. So this on SEMI-1 is actually a lower nominal input capacitance than the one that we're replacing, the MagnaChip one here. So the lower... The lower input capacitance, the better. It's not going to hurt. You know, but it might have, like, reverse transfer capacitance.

**Dave Jones:** Now we're getting into the nitty-gritty of MOSFETs. 25 puff over here. It's only 10 puff over here, but it's not going to matter. It's not going to matter a rat. Anyway, I won't go into the details. Suffice it to say that, yeah, no wuckers.

**Dave Jones:** 99.999% guarantee that you could replace this MDF18N50 with a FDP18N50. And that probably goes for any of the others. That we saw here. Almost certainly. But one thing you want to look out for, this one's actually a plastic tab, okay? So this is actually isolated, whereas this one here is a metal tab.

**Dave Jones:** Let me check to see if this actually has any metal on the back of it. Wipe all the gunk off it. As you can see, nope, no metal. It's a plastic package. So this is inherently insulated, so you would have to be careful

**Dave Jones:** because there's no... Well, if you wanted to add a metal tab, you could, but you might have to add an insulating washer on there. Let me check the traces on the PCB here. Sure enough, check it out. There's one of the holes right there,

**Dave Jones:** and it is actually electrically connected. The other one up here is isolated, and the other one over there is also isolated by the looks of it. So this thing is electrically connected. So let's say you could only get the art metal tab version in stock.

**Dave Jones:** That's okay. It's going to work. But you would add a micro-washer plus a little plastic insulating sleeve in there. In this particular case, the Fairchild on Semi make an F version and insulated one as well. And RS 18N50, they don't have any options either.

**Dave Jones:** So I put this on Twitter, and somebody said, oh, RS in Europe, like, have it, but it doesn't show up in the RS Australian search anyway. Useless. So what you might search for now, for example, you might search, say, anything higher current or higher voltage rating would be fine.

**Dave Jones:** So you might search for a 20N50. I don't know if a 20N50 exists, but, you know, like, well, we can go over to someone with a bigger catalog, a 20N50. Does a 20-amp jobby actually exist? It looks like it might. There you go.

**Dave Jones:** A 20N50, and sure enough, go over here, 500 volts, 20 amps. There you go. It's on. Oh, I didn't. I didn't check the RDS on, did I? Yeah, 265 milli-ohms and 270. So, yeah, it's more better. But, of course, that's going to be specified at a particular gate source voltage.

**Dave Jones:** So that's VGS 10 volts, and over here is at VGS 10 volts. It's exactly the same specification, and at 9 amps. So, you know, you've got to look at these little things. Like the Banner, don't always believe the Banner spec. It might be 265 milli-ohms, but in this particular case,

**Dave Jones:** it's at 9 amps. It's not, and at VGS 10 volts, it's not at the full 18 amps rating and whatever VGS you happen to be using at that. But for an application like this, as I said, it's going to be completely equivalent. Let's try 20N50 at RS.

**Dave Jones:** No, and they've corrected it to 2050. Thanks, RS. Useless. Tits on a ball. Right, so you might want to go to, like, a 600-volt version. Is there a 20N60? You can guess stuff like this, but you might want to go into, like, parametric searches.

**Dave Jones:** Nah, 20N60, like, if you go back here, 20N60 from DigiKey, does such a beast exist? It might. Yep, a 20N60 certainly exists. And yep, sure enough, it's 600 volts, 20 amps. It exists. Local suppliers, Element 14 and RS, they don't have, like, anything like that.

**Dave Jones:** So I've pretty much got to go now into the parametric searching. So anyway, we basically want to go, into single MOSFET here, and we have to start parametric searching. Once again, in stock, there's no point. Well, technically, there might be a point doing out of stock

**Dave Jones:** if you're doing parametric search. You just want to, might find equivalents. You might be desperate for your part, for example. And even though Element 14 might not have it, you might be after some obscure part, but then DigiKey or Mouser or some other obscure provider

**Dave Jones:** might actually have the one you want. But in this particular case, I can easily get one, my exact, practically exact replacement, from DigiKey or Mouser. I just want to find it locally. So in this particular case, I want it all stock, and I want next day delivery.

**Dave Jones:** This means that they'll have local stock in the local warehouse. Is this a new thing they've had for the search? Because I remember when they didn't have this, you had to actually go through the list to find that, oh, they're all available. You know, you had to search this list here.

**Dave Jones:** You have to actually sort the availability column and stuff like that. So let's do our parametric search. And we're in stock, next day available. So we want n-channel only. Thank you very much. Show results. Oh, now we're, see, already we've hit like 100 volts,

**Dave Jones:** 33 amps and stuff like that. And of course, we want the correct package. Only one, well, let's just show the through-hole ones first because we might be able to make anything fit. Okay, right. So we're getting 100 volts, 60 volts, 60 volts. Okay, so now you want to be looking for your voltage.

**Dave Jones:** So voltage rate, 18 amps here, I think that's just an over rating. But do we have a voltage rate? Drain source voltage, VDS, there we go. So we want 500 volts absolute minimum. So we want 500, 600 volts. Show results, 11 products. That's a TOR247 package.

**Dave Jones:** Here we go, 500 volts, 8 amps. Oh, we're after 18. Once again, that one might, like, it might work. It might work, but it might not. It's a power factor correction thing. This is not really a high-power product. It's only like a 100-watt product.

**Dave Jones:** It could be overkill. But anyway, 600 volts, 6 amps, 15 amps. See, that one might be near enough, right? Three available for next business day delivery, $5.60, doesn't matter. Like, if you were desperate, that one might do the business. I would certainly be using that to get you up and running.

**Dave Jones:** Maybe, you know, only temporarily until you can get the correct part, you know, it's just, it's just good vibe to, you know, use the correct rate of power. But 15 amps, like, near enough to 18 amps. So that one might do the business.

**Dave Jones:** Once again, it's a metal tab, so you'd have to insulate that. What have we got? No, no, we've got nothing down here. Zippity-doo-dah, I'm searching 500 volts and 600 volts, and we're getting, nah, zip. And best seller, hot stuff, is the IRF840. Fantastic.

**Dave Jones:** From Farnells, still call them Farnells after all these years. Element 14, it looks like the best, that's the best they have for next business day delivery in their Sydney warehouse. Like, I could, I could have this within the hour. I could, like, go pick it up, as long as they don't flag me, 'cause I've got on my website here.

**Dave Jones:** This was from, wow, 2014, how Element 14 were holding my orders because I was on a US government watch list. Anyway, I might have linked that down below, you can read the story. Uh, down here, and that was a, a legit thing. My name was on a US government watch list, and it's, "Element 14 were holding orders."

**Dave Jones:** Don't know if they still do it anymore, but anyway, it was a thing. That's ridiculous. But yeah, really, that Ixos one there seems to be the go. Mosfet. Most-fet? Most-fet. Mosfets, 10,000. Let's see what the, uh, parametric search on RS has to do.

**Dave Jones:** See, like, you're wasting so much time, like, I'm just doing this for shits and giggles. Like, this video's gonna be like 30 minutes long, 'cause I'm just explaining this, but, you know, usually this is only like a couple of minutes' work, like, to find a, uh, replacement part.

**Dave Jones:** Why don't you know what you're looking for? So it looks like they don't have, in their filters down here, we might have to do it later, like the in-stock thing. Anyway, that's disappointing. So we want channel type N, geez, 8,800 as opposed to P, at, uh, 1580 devices, N channel.

**Dave Jones:** Much more popular. I like this, uh, like, interface on RS better. It's like, it's really nice how they, like, pop out each one. You can just see all your parameters there just on one page. It's just, from a user interface point of view, it's much nicer.

**Dave Jones:** Anyway, maximum drain source voltage here, we're talking at least 500 volts, 'cause that, to me, is the most important, uh, parameter here. You wouldn't wanna go anything under that. You can see how many, look at this, 839 600-volt devices. 650, 576 devices, so you don't wanna be ruling those out.

**Dave Jones:** Once you start getting above here, this is really exotic stuff, so I probably wouldn't go, uh, you can just tick all the boxes if you want. Why not? And I really do like this interface better on RS. Look at this, N channel, like, green, and then, then you can just, like, delete X and remove an individual one and stuff like that.

**Dave Jones:** Fantastic. Anyway, uh, drain source can, maximum continuous drain current. Wow, this could be good. Anyway, we want at least 47 volts. So, we're gonna, uh, I don't know, we want at least 47 devices. Wow. None of 'em gonna be in stock. Okay, I'll leave it at 20 amps.

**Dave Jones:** Once again, you could, like, go all the way with LBJ, like, but, you know, it's, it's gonna be some big-ass package up here at, at, like, at 170 amps. So, we'll leave it at that. There you go, up to 500 to 800 volts.

**Dave Jones:** So, you know, once again, we're, like, you know, it's given us the TO247, uh, packages and stuff like that. One day, you know, you could probably bodge it in, make it fit. N channel, here we go. And 18. And 18N50. Why? That's what we were looking for, wasn't it?

**Dave Jones:** Yes, I'm just checking, I'm not insane. 18N50. Eh, bloody bastards. Their search is buggered. Their search is absolutely neutered. Look at this, 18N50. That's the plastic package. On semi. Do, do they have the damn thing in stock? Shows up in the parametric search.

**Dave Jones:** Doesn't show up. Doesn't show up in the direct search. It couldn't extract, I presume it couldn't extract the 18N50. It was only searching, like, full words or whatever. Next, uh, next working day. Winner, winner. Chicken dinner. There it is. Next working day. AU stock.

**Dave Jones:** N channel MOSFET. FDPF. It's the FR version. The 18N50. We got it. Here I was, thinking I wouldn't be able to get it in Australia, but there we go. Next working day. I've got to get a minimum order, so, you know, have a look around the lab.

**Dave Jones:** Figure out what else I've got to order. You know, if there's any niceties and stuff like that to get my free shipping. You know, otherwise it's like, I can't remember what RS charge now, but it's like 25 bucks shipping or something. You know, whereas if you order like 50 bucks worth of parts, you get your free shipping.

**Dave Jones:** So that's how they suck you in. I could, like, go pick that up right now. Um, well, not right now, because it's almost 5 o'clock. I found it. That will do nicely. That is the plastic package, as you can see. That is practically, that is identical to this.

**Dave Jones:** So, as you're probably starting to realise. The search on RS components and on element 14 is different to other websites. It's not searching like a partial term. So it looks like we have to put asterisks in there and 18N50. And if we do that, ta-da!

**Dave Jones:** There they are. So that's all we had to do. And there is the one that we found. There's our identical replacement. Bam. Straight off the bat. So it's simply a matter of putting in the asterisks there, but anyway. I hope the rest of it was interesting.

**Dave Jones:** And Farnells does the same thing. 18N50 like this, and bam, we actually get it. But if you put just 18N50. Wah, wah, wah, wah. And other sites like, say, um, arrow.com. 18N50. You whack that in. No asterisks required. They actually give you. Pops up.

**Dave Jones:** It searches the partial term. But for some reason, RS and element 14 don't do it. But Digikey, Mouser, Arrow, and Finechips, and Octoparts, and all the rest. They don't do it. You can come against it like that. But hopefully you learned that really, you know, the parametric search is one of the

**Dave Jones:** better ways of doing it. Of course, if we didn't have an exact match here in Australia, then I would have had to choose an equivalent. So I might have had to go with like a 20N50 or something like that. And that's a metal tab.

**Dave Jones:** And then, you know, if that's the only one I could have got in stock, then eh, so be it. You know, I could have made do. And for those wondering what this MPN is here, that's the manufacturer's part number so you can actually search by that and you don't need the asterisk, 18N50.

**Dave Jones:** I don't think that's always been there, so that's why I didn't see that. And yep, sure enough, and it's different up here. It's got search by MPN. So if we just do 18N50 there and search, we get our nothing burger like we got before,

**Dave Jones:** 18N50, search by manufacturer's part number, bingo, we're gonna get it like that. Fantastic. But, element 14 don't have anything like that to search for the manufacturer's part number field. You've got to put in the asterisk, otherwise you won't find it. So that's totally different to all the other websites.

**Dave Jones:** But check this out. The partial match on the manufacturer's part number doesn't always work. Check this out. Let's search for a, like a pick, 16F88, for example, RS, do carry this, right? If we just do our normal search like this, of course, we get nothing.

**Dave Jones:** We get connectors, right? Whoa, jeez, they look, oh, they look gorgeous, don't they? Anyway, and if we search by manufacturer's part number, it should work like the 18N50. It should do the partial match, but it doesn't. But it knows it's a microcontroller. Look at this.

**Dave Jones:** So it knows the category that it's in, but it won't actually give you the search result. You've got to put in the asterisk, and then you'll get the chip. And the asterisk, with the manufacturer's part number search, you'll get the chip. Like what the?

**Dave Jones:** But there you go, winner, winner, chicken dinner. I found a locally sourced 18N50 in the plastic package, so I don't even have to dick around with insulating that either. So that's fair. And I got them. Wow. Murphy's asleep right now. I should auto search for and order other stuff.

**Dave Jones:** Once again, like, there are infinite variations on, like, manufacturers. Part numbers, part numbers, and things like that. But MOSFETs, you know, they're fairly reasonably well, you know, de facto standardized on this current voltage, you know, N-channel type thing. So that's pretty handy to know when you're searching for replacement parts like this.

**Dave Jones:** Once again, it's, you know, a lot of the parameters down here might matter. They might matter a lot. You could come a gutter if you don't get them right in terms of design and stuff like that. But for a simple, like, a mains power factor correction.

**Dave Jones:** And for a device that only draws, like, 100 watts or something, like, I think they've over-specced the transistor in this. And not over-specced in terms of voltage. 500 volts would be bang on what you actually, you know, would be, like, the minimum that

**Dave Jones:** you'd sort of want for an application like this. But the 18 amps continuous, it's never going to draw 18 amps continuous. And they're always going to have a much, you know, if you're just talking about peak inrush currents and, you know, stuff like that, then what's the peak current of this?

**Dave Jones:** It's like, a pulsed drain current is 72 amps. So even if you've got, like, 10 amps. The 5-amp version of this or something like that, it would probably do the job. But don't skimp on the voltage rating. Because, yeah, I think you might come a gutter there.

**Dave Jones:** And the RDS on, it's probably not going to make a huge difference. When you're talking similar specified parts in terms of voltage and current, they're almost always going to be, so within a, like, fraction of an order of magnitude, you know, 10, 20%

**Dave Jones:** or something is near enough in terms of the RDS on, for example, which is the other major parameter. You wouldn't worry about, you know, drive capacitance and stuff like that unless there was some really horrid part. But in this particular case, any 18N50 would do the job.

**Dave Jones:** Or any sort of, like, you know, 20N50 or maybe even a 5N50. I don't know. Leave your thoughts in the comments down below. If you were desperate, I'd certainly install, like, a lower current rating job. So there you go. So, yeah, I'm still working.

**Dave Jones:** I'll order this part. And I'm going to release this video before I release a repair video. And hopefully I can repair this thing. I don't know. I found a couple. I failed parts. Spoiler alert. And we'll see if these parts will actually get this thing back up and running that I

**Dave Jones:** found in the dumpster. So it's worth a shot anyway. Yeah, I don't carry this sort of, you know, stuff in stock. I might be able to, like, if I look through old boards and stuff like that, I might be able to salvage a part.

**Dave Jones:** Perhaps, like, if I was really desperate. But, yeah. Anyway. It's easy just to do a quick search like this. This would have taken me minutes. And then I would have found this RS part. And eventually, and I would have ordered it or I would have gone and picked it up.

**Dave Jones:** And, yeah, no worries. Anyway, I hope you enjoyed that and found it useful. If you did, give it a big thumbs up. Catch you next time. Thanks for watching.
