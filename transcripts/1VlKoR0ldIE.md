---
video_id: 1VlKoR0ldIE
title: EEVblog #1057 -  µCurrent Murphy
url: https://www.youtube.com/watch?v=1VlKoR0ldIE
source: youtube-asr
timestamps: {"0": 0, "1": 20, "2": 36, "3": 50, "4": 68, "5": 90, "6": 107, "7": 119, "8": 136, "9": 154, "10": 178, "11": 194, "12": 215, "13": 230, "14": 246, "15": 264, "16": 284, "17": 311, "18": 335, "19": 357, "20": 378, "21": 394, "22": 418, "23": 432, "24": 449, "25": 467, "26": 486, "27": 505, "28": 518, "29": 532, "30": 546, "31": 561, "32": 572, "33": 588, "34": 602, "35": 616, "36": 634, "37": 653, "38": 669, "39": 685, "40": 711, "41": 732, "42": 744, "43": 759, "44": 783, "45": 799, "46": 821, "47": 842, "48": 861, "49": 877, "50": 895, "51": 912, "52": 931, "53": 950, "54": 962, "55": 977, "56": 996, "57": 1016, "58": 1033, "59": 1048, "60": 1064, "61": 1082, "62": 1095, "63": 1111, "64": 1128, "65": 1145, "66": 1165, "67": 1187, "68": 1203, "69": 1218, "70": 1231, "71": 1247, "72": 1264, "73": 1282, "74": 1296, "75": 1314, "76": 1331, "77": 1347, "78": 1361, "79": 1375, "80": 1396, "81": 1409, "82": 1424, "83": 1433, "84": 1449, "85": 1469, "86": 1483, "87": 1502, "88": 1524, "89": 1538, "90": 1555, "91": 1573, "92": 1591, "93": 1608, "94": 1632, "95": 1650, "96": 1666, "97": 1687, "98": 1703, "99": 1721, "100": 1735, "101": 1750, "102": 1762, "103": 1775, "104": 1793, "105": 1807, "106": 1826, "107": 1841, "108": 1855, "109": 1870, "110": 1882, "111": 1897, "112": 1913, "113": 1928, "114": 1942, "115": 1956, "116": 1975, "117": 1993, "118": 2013, "119": 2031, "120": 2046, "121": 2060, "122": 2075, "123": 2090, "124": 2105, "125": 2117, "126": 2132, "127": 2145, "128": 2161, "129": 2176, "130": 2191, "131": 2203, "132": 2214, "133": 2232, "134": 2243, "135": 2255, "136": 2270, "137": 2309}
---

**Dave Jones:** Hi, I got a real interesting one for you today. Check this out. Oh, okay, it's a humble microcurrent EV blog forum member uh Insatman uh reported that he recently uh purchased a microcurrent and was having a problem with the offset voltage of this and was

**Dave Jones:** getting in the order of like millivolts um you know, four, five millivolts, something like that offset voltage uh with no current on the input. And of course um the spec is much, much better than that. In fact, the uh Maxim

**Dave Jones:** chip inside this thing I've done videos before is rated for a nominal uh 0.1 or a typical 0.1 microvolts or 100 nanovolts offset voltage typical. And if you multiply that by the times 100 gain in this thing typically, even though

**Dave Jones:** it's a two-stage, um let's call it um 0.01 millivolts. And even if you account for like absolute worst-case data sheet uh values, you know, the right extreme ends of the uh bell curve for the offset of this uh chip taken into account

**Dave Jones:** manufacturing process uh variations and temperature over the extreme range, it's still rated for um 2.5 microvolt offset voltage or uh what's that? 0.25 millivolts um offset. But they're ordering at least they're getting at least an order of magnitude more than that. So, something

**Dave Jones:** was up. And then when a second user uh named Keox actually reported and uh posted the findings of a similar thing, I thought, "Aha, let's actually investigate." So, I got myself a uh like a new production batch 5,000 odd

**Dave Jones:** serial number microcurrent. Let's plug it in and see what happens. So, what we'll do is we'll actually uh short the input. It's got a shorting switch to actually uh do that. And I'll just like put it to the middle of the range.

**Dave Jones:** Doesn't really matter, but just for reference, we'll do all our tests in the 10 ohm shunt resistance range or 1 mV per microamp. So, there you go. It's powered on. Plug it in, and look, no worries whatsoever. There's absolutely nothing

**Dave Jones:** wrong with this thing. Hmm. So, you know, you can confirm that on any meter you happen to use. There you go. 0.02. It's no problems whatsoever. So, like, and you know, I tested a few of these, and I got

**Dave Jones:** basically the same result. So, like, what's going on? I don't like, you know, did a couple of people get bad ones? Oh. Oh. Oh. Oops. What's going on here? So, why does the 121GW measure different to everything else? I mean, 3 mV

**Dave Jones:** actually minus 3.7 mV. This is, you know, the order of what they were measuring. So, what's going on here? Take the exact same leads, plug them in here again to verify. This is a bloody good 7 1/2 digit Keysight meter.

**Dave Jones:** Nothing. I I I don't understand. Let's try the Keithley. What? 10 mV? What the heck's going on? I mean, if you have a look at the microcurrent schematic, it's the output is fairly low impedance through a protection resistor

**Dave Jones:** driven by the Maxim chip, and there's a split rail system in there. If that moves, it shouldn't cause a problem because look at the star reference point in there. The output ground is taken from there, and like, it should

**Dave Jones:** work. So, really, the only way that we could be getting an offset error here with a short on the input is if there was something wrong offset voltage on those maximum chips, but this is like more than an order of magnitude out of

**Dave Jones:** the absolute worst-case production spec over the entire temperature range. I've just never seen anything like this. So, I tried various meters in the lab here and sure enough only the Keithley uh DMM 7510, the most expensive meter I've got here, highest

**Dave Jones:** spec meter I've got here in the lab, and the 121GW actually measure a high offset voltage, and they actually measure different. -4 and was it minus that we were getting there? 10? Yep, -10 mV. This is strange. But wait, you ain't

**Dave Jones:** seen nothing yet. Look at this. -4 mV. Nothing. And it's short. This has a resolution of a 800 microvolts. So, we should be able to get it should be like reading like 40 counts there. What? What? Mind-blowing. And sure enough, look at this. If I put

**Dave Jones:** the Keysight and the 121GW in parallel, okay, -6 mV, they match. No worries whatsoever. Switch that to volts. Poof. Gone. It's magic. So, let's see what happens if we plug another set of leads in parallel here and actually plug these

**Dave Jones:** into the meter to confirm it. Aha. Now we're getting somewhere. Bang on, and it's changed yet again. 15.1 mV. Let's go over here. It's dropped back down to nine. Aha, now we're able to confirm it with other meters. But, if we actually

**Dave Jones:** disconnect the Keithley meter, it causes a problem. And no, it's not the input impedance down here. It's a standard 10 meg, but I switch it to auto and it causes exactly the same issue. But, only when we put two meters in

**Dave Jones:** parallel, does it actually cause a problem. And sure enough, if we actually put pretty much any two meters in parallel, we're able to get something. Um once again, it's a different value every time. So, you might think, "Aha, when you put multiple

**Dave Jones:** 10 meg input resistances in parallel, that might do it." Well, let's check that out. There you go. That meter in parallel with 10 meg does absolutely nothing. Hmm. How about 1 meg? Nope. 100k? Nope. It's not the load. So, you might

**Dave Jones:** think, "Okay, maybe there's something wrong with that split rail generator in there cuz we've just got the single coin cell battery and then it uses that LMV321 op amp to just split that in the middle." Well, if we put our meter on

**Dave Jones:** the reference output with reference ground output, which is actually the output of the virtual ground, and measure our battery, then 1.33 plus and minus 1.33. Perfect. So, this is just madness. So, what we want to do is compare that cuz

**Dave Jones:** this is the new batch number, the 5000 one. Let's compare this with an older batch unit. I happen to have one, 3690 here. So, it's from a couple of thousand Where am I plugging this into? There. Couple of thousand to go and

**Dave Jones:** let's try that. Nope, it's absolutely fine. That's the offset voltage you'd expect and uh this worst case thing we had, plug it into both. No, it's hunky-dory. In fact, I've done this with many old ones over a whole bunch of serial numbers. Not a

**Dave Jones:** problem. And I've confirmed this with a second one as well, a second uh recent serial number. So, something very strange is going on here with the with this new batch one compared to any previous old batch version which I've uh measured and

**Dave Jones:** I've never had a single reported issue with offset voltage apart from user error or uh you know, some other such thing. It just hasn't been a problem. Some have been a little bit higher, but the this is like an order of magnitude

**Dave Jones:** or more higher than what you'd expect absolute worst case. I mean, there's not much that can go wrong on this thing. There's just the two maximum uh precision chopper amps on there. Um never had an issue with those. I'm

**Dave Jones:** always buying uh genuine parts for those. We've got just the offset uh op amp for the split uh rail thing. Never had an issue with that. And there's a couple of shunt resistors and couple of switches and Bob's your uncle. I mean,

**Dave Jones:** what can possibly go wrong with this thing? Well, you saw that it was different depending on what sort of meter we hooked it up to. So, even though we couldn't confirm it by a resistive load, hm maybe something else

**Dave Jones:** is going on. So, let's hook up the output to a scope, see what's what. All right. So, let's hook up a good uh low noise scope. We've got the Rohde & Schwarz one here with this big 10-bit uh

**Dave Jones:** converter. I'm using a proper uh scope probe to BNC lead using the uh proper probing technique. So, let's switch it on. See what we get. Uh 10 mV per division um and that's kind of like the noise you expect, like the

**Dave Jones:** high bandwidth uh noise, of course. So, I There's really nothing doing there and uh we're in high resolution mode, you know, we can go to sample mode. That's the There's more of the noise, which you kind of expect from a high resolution

**Dave Jones:** converter. I've done a whole video on uh digital scope noise in quote marks. Um but that's fine and dandy. It's no problem. So, if we hook that up to the decade resistance box in parallel, let's go to a meg there. Everything's

**Dave Jones:** hunky-dory. Um we can Well, we There we go. We can go down to 10K. Everything's fine. Let's go down to 1K. Ooh. Doesn't like that, does it? You can see that offset drop a bit. And you can see it over here. Hmm. We're

**Dave Jones:** getting somewhere. But this is a very low load. I mean, 1K. We were seeing this with 10 megaohm input impedance meters. So, let's go back to our trusty 121G W here and switch between it. Woah. This is heavy.

**Dave Jones:** Look at that. 4.6 mV offset and sure enough, you can see we're at 10 mV per division and you can see that it is basically dropping by that 5 mV there. On average, I mean, you can whack uh average on if you want. It's not

**Dave Jones:** going to be a huge amount better. We might have to put some more averages on, but you can Woah. That's bad. We've got something oscillating in this puppy, have we? Doesn't look great, does it? Woah. Look at that.

**Dave Jones:** Wow. Wow. We've got a whole bunch of Woah. High frequency stuff. Look at that. High frequency oscillation in there. Wow. And that frequency is about 2.57 MHz. Well, there you go. Hey. This little baby's oscillating. But what's oscillating? It's got to be

**Dave Jones:** the op amp. I've never had never seen that maximum op amp oscillate before. It's crazy. And if we whack in the old board, let's give that a burl. There we go. No worries whatsoever. And I'm millivolt mode, look at that. Stable as Uluru. And as

**Dave Jones:** you may have started to guess by now, it perhaps has something to do with a capacitive load, not just resistive load, or probably doesn't have anything to do with resistive load at all, really. Um so, I've got a little decade

**Dave Jones:** capacitance box here, and I've got nothing connected in parallel at the moment. Switch it up. I'm at What is it? 5 puff, 10 puff. So, I'm just putting some Hey. Hello. Try and keep my fingers off it. There we

**Dave Jones:** go. Look at that. That's 100 puff. Wow. There you go. And let's put Sure enough, 100 puff. Yep. That thing oscillates. Let's get the old one. Whack it in. See if it does the same thing. Nope. Look at that. Where we up to? Let's put

**Dave Jones:** in Let's go for broke. Put in a microfarad. No. No. No problems whatsoever. That's so that can do like That's 100 mic. 100 microfarads on the output. The existing ones don't oscillate at all. And that's what I've always found. But

**Dave Jones:** there's something a foot here. Hmm. I smell some fight rarefied subtle problems here. All right, so let's look at both boards under the microscope here. Here's our problem one and an older batch one and apart from the color of the PC of the

**Dave Jones:** solder mask, yes, it was changed at one point. There's like no obvious like manufacturing you know, issues like solder joint issues or anything like that. Everything looks Everything looks hunky-dory. Let's go in and have a look at our Maxim chip, shall we? Sorry,

**Dave Jones:** sometimes it's hard to see those laser markings on there ABAA and sure enough that is correct as per the data sheet. It's that's the manufacturing code on top for the max 4239 and I always buy these Maxim chips from

**Dave Jones:** the genuine source cuz they are like it's the main thing that gives this along with the resistors which I've come a cropper on before video linked in at the end of this. That's worth a look, too. Where I had a similar sort of

**Dave Jones:** production specification problem due to the resistors and but that basically determines the full performance of this thing. So, like what's going on? I've I've I I buy from like Digikey and sure enough if you have a look at the older board over here,

**Dave Jones:** it's exactly the same ABAA. I I bet my bottom dollar they are genuine Maxim. So, maybe let's go over here and check out the only other active component we have in here, which is our split rail op-amp and this is an LMV

**Dave Jones:** 321 and the old one has the code RC1F on it. Let's have a look at this one here. Aha, 321S but I I you know, I mean, it's it's an LM like it's a 321. So, but it but it does

**Dave Jones:** look different. It has those bars top and bottom, but technically that is different. Hmm. Now, normally the offset voltage of this LMV321 op-amp doesn't matter. And well, it doesn't. You can go I could go and demonstrate this, but you know, really

**Dave Jones:** it's a trivial concept because the output reference point of our amplifiers and the gain of the amplifiers is all determined by that split rail. So, that rail can be anywhere within that 3-V range. It doesn't have to be exactly

**Dave Jones:** plus minus 1.5 V. It can be plus half a volt and and negative 2.5 V for example. It doesn't matter. It's only that only becomes a problem when you've got you know, the head room of the amplifier to swing the output

**Dave Jones:** voltage, but its actual value does not matter. So, technically, even if this thing oscillated and that value changed by 5 mV or something, it's not really an issue. But, aha, it also couples through via the battery and the bypass capacitors

**Dave Jones:** through to the power rails of the max of the maximum op-amp. So, maybe the power supply rejection ratio at that high frequency of the maximum op-amp is what's causing it to couple in and give that offset voltage on the output somehow, something like

**Dave Jones:** that. So, in theory, it's possible for this LMV321 to actually do that. But, jeez, it's it it was such a remote possibility. And it's especially more surprising considering that I've already taken care of this in the design aspect

**Dave Jones:** of the microcurrent. I've put in a 270-Ω output resistor. A lot of people over the have asked what that is for and that is just for stability of this op amp. Even though the LM V321 is actually rated to drive a 200 picofarad load in a

**Dave Jones:** unity gain configuration without any series resistance. Adding the series resistance on the output just increases the capacitive load that you can drive and keeps it stable. So we're seeing here oscillations of you know like 50 to 100 puff or something was

**Dave Jones:** starting to go at I think 50 picofarads. So you know really something is seriously wrong here. This it's almost as if this is not an LMV321. Is it just an LM321 and they are two very different parts. Each the difference between the LM and

**Dave Jones:** LMV is V stands for voltage. It goes down to a lower voltage rail. In the case of the LMV it's rated down it's fully specified down at 2.7 volts which just happens to be the dropout voltage of the battery in this particular

**Dave Jones:** application which is why this little op amp is almost perfect for this sort of application. Now as it turns out I did have a couple of old bags of some old leftover parts from previous runs or whatever. This one's from 2013

**Dave Jones:** and I've always used the LMV There it is 321IDBVR the Texas Instruments part and I've always bought them from Digikey or Mouser in that particular part and I've checked the number on that and it's got RC1F sure enough and and this one dates

**Dave Jones:** from September 2010 and it's exactly the same thing and it's an RC1F but I did find an RC1K so K might be you know some other like date variant or you know something like that. But once again they all have

**Dave Jones:** that RC1 on them not that 321T or S. And sure enough I did check out my Mouser orders and I did actually order, it looks like I they must have been like out of stock or something like that perhaps of the IDBVR

**Dave Jones:** or whatever it is. So I actually ordered an LMv321AS5X from on semiconductor Fairchild. And if we go in and actually have a look at the data sheet of this thing it's actually the only data sheet I can find that does not tell me

**Dave Jones:** what the designator is on the actual chip, the SMD code. It just doesn't tell me. Maybe I'm blind but I cannot find it in here. It's just got some crap to do with the evaluation board and things like

**Dave Jones:** that but it does not have like there's the evaluation board great there fantastic. Thanks for the info on the eval board but then it just goes down into the physical dimensions of the package and gives you no identifier whatsoever. So I don't

**Dave Jones:** know if this is I assume it is like assuming that Mouser haven't goofed up and they haven't given haven't substitute the part although it as I said at the end of this video you'll see another video where this has happened

**Dave Jones:** before where I think it was Digikey was it actually screwed up the parts of the manufacturer screwed up the parts sent into them and I don't know whether or not it's an LM 321 or not but yeah, anyway the code's not there. So I

**Dave Jones:** I still I've looked through a lot of LMv321 data sheets cannot find that code at all. I've looked through the various SMD substitution code list on the internet. Can't find anything with 321 T or S. But in any case the on semi one or

**Dave Jones:** slash Fairchild one Um, it basically has exactly the same specs, it's still rated for the 200 uh picofarad load and stuff like that. It's exactly the same. So, why one works robustly with like a 10 Oh, what, a 100 microfarad load on the

**Dave Jones:** output and the other one doesn't? Like not even it doesn't even meet that 200 puff. I that's the crazy thing I don't understand. And if you have a look at the schematic here, granted it is a bit unusual in the way that um, you know, we

**Dave Jones:** don't have a direct capacitance load on V ground here, for example, cuz the bypass caps on the MAX439 are actually across V plus and V minus. So, they're directly across the battery, not actually on the output. So, it's

**Dave Jones:** kind of hard to say what the effective capacitance is on that virtual ground relative to say the negative rail, uh for example. So, it's hard to tell, but like I've uh proven that the Texas Instrument part with exactly the same

**Dave Jones:** specs it it just never oscillates with any capacitive load, it's completely robust. But, this one isn't. So, it it's almost I starting to suspect that it's actually an incorrect or possibly even a fake part. But, fake parts from the likes of

**Dave Jones:** Mouser virtually unheard of. That's why you buy from Digi-Key and Mouser and Farnell and the other reputable uh catalog suppliers so that you don't get the fakes. And I have got the assembler searching to see if maybe they

**Dave Jones:** can find the original reel for this one, but unfortunately it wasn't a manufacturer reel, it was a Mouser reel. So, they re-reeled it and put their own Mouser sticker on it. Um, so really it wouldn't it's probably devoid of the

**Dave Jones:** original manufacturer's uh label, unfortunately. So, bugger. Come a to there. And if we have a look at the on semiconductor LM321, then well, if you look at the market, they do have the marking description here. Specific device code. I I don't

**Dave Jones:** know. Would that be 321? And but then it would have the assembly location, the year, and the work week. So, really it ain't that. And it And it's this and one has like the bars over the top, not

**Dave Jones:** these little dots here. So, it's definitely not an on semi LM321. So, there's only one thing left to do to test my theory that it actually is that LM V321 is to suck it out and put on a

**Dave Jones:** good one. Found another reel. This is an old Digikey reel. Once again, RC1K. So, I'll whack that in. See how it goes.

**Dave Jones:** And there we have our new chip on there. Let's plug her in and try it out. Look at that. 0.01 mV. No worries whatsoever. That worked a treat. And we'll just add in some capacitance there and have a look at the

**Dave Jones:** scope. Yep. No worries. Beautiful. Okay, so what I've gone and done is actually got a couple of ones that I could get in stock. LMV 321s, various types. The LMV321AS 5X, which is the on semi part, which I

**Dave Jones:** think might be the one in here, but we'll have a look at that. We've got the LMV321M5, which is a TI part, which is the same as the IDBV part, which I know definitely works and has been used in almost all my

**Dave Jones:** production units. But there there's an M5 variant. So, whatever, we'll use that. And there's an LMV321I LITL, is it? No, ILT or something like that. And that's an ST micro part, but they're all LMV321. So, let's give them

**Dave Jones:** all a whirl. And sure enough, if we take a look at the AS5X variant, it's got that 321 on it. But it's got 321B. So, we've seen what 321S and 321T. So, it looks like the culprit might be this onsemi

**Dave Jones:** part, which is the LMV321AS5X. So, but what I'll do is I'll I'll solder this one in and give it a go. See if it has the exact same problem as the S ones that are in the current board. Um but

**Dave Jones:** once again, the data sheet doesn't tell you what that S or B or T or whatever it is means. And wow, there you go. That's 100 millivolts per division. This is awful. Like we're talking 190 millivolts offset now. This is insane.

**Dave Jones:** That's like a half an order of magnitude worse than the uh than the other 321T or whatever it is, which I presume is like a an onsemi one as well. So, what is it with these onsemi parts? Wow, horrible.

**Dave Jones:** So, that's definitely a problem. Let's actually uh disconnect the the meter. Oh, that's the 121GW. Let's switch it. No, I switched it to volts and did the uh did the volt millivolt thing and uh it's still makes no difference. Disconnect it. No.

**Dave Jones:** No, look, that's just the scope. That is just the scope now. Wow. Um that is So, this B variant, whatever that is, is grossly different in this particular circuit configuration with this particular load with the times 10 probe.

**Dave Jones:** But like, let me actually disconnect the those leads from there. Wow, look at that. That's ridiculous. And here's the 321ILT part. This is from ST. There we go. It's K177. Let's give that a try. Well, go ST. There we go. .04.

**Dave Jones:** No worries whatsoever. Clean as a whistle there. We know modify. Let's put our capacitive um the load. Don't put it on the input. Okay. Let's wind her up.

**Dave Jones:** No, that's still okay. Couple of hundred puff. Yeah, no worries. Let's whack on a hundred mic. Whoa. Yeah, okay. It's not terrific on a hundred mic, is it? There we go. I mean, we've got some oscillation there, but with a hundred

**Dave Jones:** Sorry, with two microfarads on there. Hundred mic hundred mic. It's a little bit of switching noise. Don't worry about that. And yeah, but otherwise, it's I mean, it's stable. No worries. If we actually feed one milliamp into it, of

**Dave Jones:** course, you know, no worries whatsoever. We get our well, that's off scale, but anyway, there it is. There's our yellow line right on a volt. No worries. And that's with a like 33 microfarad load on the output. So, that ST1 is operating a treat. Okay,

**Dave Jones:** let's try the TI part. Let's try this M5. What is that? That's got A13 on it. All right, here she goes. Now, that one's not too bad, but it is showing a slightly higher offset. We're talking you know, point almost .2 millivolts

**Dave Jones:** there. It's still you know, order of magnitude lower than the problem we're getting. And uh it's it's still okay. So, I wouldn't uh quibble about that at all as long as it doesn't uh oscillate with any sort of uh capacitive load,

**Dave Jones:** then uh that's okay. So, we'll whack a load on, 33 microfarad on there. So, that's all right. Hundreds of puff, yeah, not a problem. Uh it gets a bit noisier up there, but still like not in the order of

**Dave Jones:** millivolts. It's in the order of like uh hundreds of millivolts. So, yeah, I would say um that particular TI part is a pass as well. By the way, I'm doing this on a different board just so I do

**Dave Jones:** have different boards to play with, and I haven't tested this one for its original offset. I probably should have. So, that offset could be uh coming from the Maxim uh chip. So, but the main thing we're looking for here is that,

**Dave Jones:** you know, it doesn't oscillate like the uh ON Semi / uh Fairchild part does. So, there you have it. That's a real interesting uh Murphy, that's probably like a level five Murphy got you because not only do we have a uh

**Dave Jones:** a difference in between manufacturers' uh parts when there should be no difference according to the data sheet. They should both be Well, all of them What did we test out? Like four different chips there, and only one out

**Dave Jones:** of those four, the AS5X from uh Fairchild / ON Semiconductor, is the culprit. And would you believe it? That one is the one I actually originally specified in my bomb, and that bomb bomb comes from like eight years ago, like way way longer than nine

**Dave Jones:** years ago when I developed the first microcurrent, I think. Um way before the microcurrent gold, but I don't think I've ever really used that apart from obviously um this new uh production run. It looks like I still haven't confirmed,

**Dave Jones:** uh but I think the AS5X variant may have been used in there. So, like just luck of the draw and a really, you know, I I've always considered that part to be completely um, safe, you know, cuz I

**Dave Jones:** designed in the the aspects that would take into account the capacitive load and it shouldn't have been a problem and it's not on three out of the four chips we tested. Two were TI brand, one ST and one onsemi

**Dave Jones:** and it it doesn't even Well, I you know, we could do further videos actually just testing that chip on its own. That might be an interesting just putting a capacitive load on there, nothing else, just hooking it up on a bare board with

**Dave Jones:** nothing else in there except for that chip. That might be fascinating. I won't do that today, but if I do, I'll whack it over just on maybe EVBlog 2 channel or something like that. By the way, EVBlog 2 channel linked in at the end of

**Dave Jones:** this video somewhere here. Check it out. Um, I think I'm up to 54, 55,000 subs or something. So, I was joking before to David that wouldn't be funny if we actually got a YouTube silver button, got to 100,000 subs for just my second

**Dave Jones:** channel where I just throw random videos and stuff. Just, you know, single take things and other stuff that doesn't really isn't polished and produced for the main channel. So, anyway, so yeah, subscribe to EVBlog 2. There's tons of

**Dave Jones:** content over there. Let's see if we can get that silver play button just for shits and giggles. Anyway, um, I hope you found that interesting. That is absolutely fascinating that we found this problem. It's not something you'd expect in a precision instrument like

**Dave Jones:** this. I've had problems with the resistors before. That was like a supply manufacturing supply distributor goof up and I'll link that video in somewhere here at the end. As I said, and you'd expect the maximum chip to be at

**Dave Jones:** fault, and no, it was oscillation in the virtual rail chip. And against all odds, um like I did I I don't know. So, yeah, it would be interesting to do a follow-up video on that, but there you go. That's how

**Dave Jones:** little you can get little gotchas like that that caused an issue. Wow. It's like unbelievable. Anyway, just for uh kicks, let's hook up uh That's Are we on the right range there? Let's just hook up our current gen. Oh, sorry.

**Dave Jones:** I keep mixing these knobs up. Keep switching between the oscilloscopes, and it's like it's crazy. There we go. 1 V. So, let's actually do some single shot trigger auto normal single shot. I'm going to switch that on. And

**Dave Jones:** hey. There we go. Is it going to ramp up cleanly? What I'm doing is uh just switching on I'm just operating the uh output uh of my programmable function gen here. Oh, turned off. Uh yeah, no. All right.

**Dave Jones:** Go. Hey, look at that. Beautiful ramp. Ah, thing of beauty is a joy forever. Anyway, I hope you enjoyed that uh video. That's absolutely fascinating. You don't see that one every day. Uh I think that one's a level five Murphy.

**Dave Jones:** This, and I'm still not sure of the exact um serial number ranges and stuff like that because I didn't keep track to that level, you know? Maybe if you're Apple or somebody, you might track, you know, you might have a comprehensive

**Dave Jones:** um system that, you know, a comprehensive production documentation system that actually documents what serial number parts came from what supplier, went into what serial number boards, on what day, and all that, you know, sort of jazz if you're a huge enterprise and, you know,

**Dave Jones:** that could be worth millions or hundreds of millions of dollars to you. Um, if you have any potential issues, um, but of course I'm very careful where I get the uh Maxim chip from, of course, and really there are, you know, there's no

**Dave Jones:** substitutes for that uh chip. But, of course, there is the possibility of fakes for that, so I always buy those through Mouser and Digi-Key. But, I'm pretty sure I've always bought the LM V321 also through Mouser or Digi-Key or

**Dave Jones:** another reputable supplier. So, I'm not sure of the exact date codes and things like that. I still maybe have to go through some old records. I might be able to pull up something. So, this is actually a problem that

**Dave Jones:** uh is not going to affect all micro currents with that particular uh chip on it in all scenarios. I mean, you don't even if you hook it up to uh the oscilloscope with the probe capacitance everything, you're not going to see

**Dave Jones:** that. Or if you hook it up to the right type of multimeter that so happens that, you know, that doesn't have the uh reactive load on it that uh is required to make this thing oscillate, then you're never going to see it. So,

**Dave Jones:** even hooked up to like a high-end multimeter and a high-end scope, you don't see necessarily see the problem unless you put a a reactive enough load on there that causes instability and causes the thing to oscillate. So, it's it's one of

**Dave Jones:** those like marginal cases that in this case I've actually got a production uh test jig. I don't have one here. It's at the assembler that actually measures the offset voltage as part of the production go no-go test. I can't remember the

**Dave Jones:** exact limit. It's like, you know, half a millivolt or something like that. Um, and I'd have to read my documentation on that. But, like it obviously presents a small load enough that it didn't none of these units actually

**Dave Jones:** failed that test as far as I'm aware anyway. So, I test for offset voltage. I test for gain on all three of the different ranges with the production test jig. I think I may have done a video somewhere

**Dave Jones:** on some of those production test jigs. Anyway, if I did I'll link them in at the end of this video. Hopefully, if I can find them. Made too many videos. I forget. Um so, I hope you found that

**Dave Jones:** interesting. That is like a real world gotcha, a trap for young players and old alike um on what's supposed to be an equivalent part across all manufacturers. I guess it's fortunate for us. I guess you know, like this problem is fortunate in that it

**Dave Jones:** allows us to see a real a rare quite a rare real world problem like this. By the way, if you've got one of these new ones and it is an issue I've only had a couple of people report it.

**Dave Jones:** Obviously, it's only going to be a problem on certain capacities of loads and things like that. There may even be variations in the chip itself the production chips. I don't know. But, yeah it looks like only several people

**Dave Jones:** have reported that. But, if you do have a problem with your micro current it should all previous ones should be fine. I think it's just this batch production run that may have had some of these on semi slash Fairchild parts fitted to

**Dave Jones:** it unknowingly. Anyway, yeah if you do have one contact me and we can arrange something. So, anyway I hope you enjoyed that. If you did please give it a big thumbs up. As always, discuss down below. Catch you next time.

**Dave Jones:** Mhm.
