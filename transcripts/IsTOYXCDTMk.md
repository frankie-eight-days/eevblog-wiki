---
video_id: IsTOYXCDTMk
title: EEVblog #966 - CPM700 Counter Surveillance Monitor Repair
url: https://www.youtube.com/watch?v=IsTOYXCDTMk
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 33, "3": 43, "4": 56, "5": 68, "6": 82, "7": 93, "8": 102, "9": 113, "10": 124, "11": 136, "12": 146, "13": 169, "14": 179, "15": 190, "16": 203, "17": 212, "18": 234, "19": 246, "20": 255, "21": 268, "22": 279, "23": 294, "24": 304, "25": 316, "26": 330, "27": 345, "28": 355, "29": 374, "30": 387, "31": 409, "32": 422, "33": 433, "34": 447, "35": 456, "36": 467, "37": 492, "38": 502, "39": 514, "40": 524, "41": 538, "42": 549, "43": 570, "44": 594, "45": 607, "46": 617, "47": 638, "48": 660, "49": 670, "50": 685, "51": 698, "52": 718, "53": 732, "54": 743, "55": 758, "56": 772, "57": 786, "58": 797, "59": 809, "60": 823, "61": 838, "62": 849, "63": 864, "64": 877, "65": 891, "66": 900, "67": 928, "68": 953, "69": 978, "70": 1002, "71": 1028, "72": 1039, "73": 1049, "74": 1065, "75": 1074, "76": 1084, "77": 1093, "78": 1107, "79": 1115, "80": 1126, "81": 1140, "82": 1152, "83": 1160, "84": 1173, "85": 1185, "86": 1202, "87": 1213, "88": 1227, "89": 1245, "90": 1258, "91": 1268, "92": 1284, "93": 1290, "94": 1310, "95": 1323, "96": 1334, "97": 1351, "98": 1366, "99": 1377, "100": 1394, "101": 1410, "102": 1423, "103": 1436, "104": 1449, "105": 1459, "106": 1484, "107": 1502, "108": 1514, "109": 1530, "110": 1540, "111": 1560, "112": 1575, "113": 1587, "114": 1599, "115": 1614, "116": 1632, "117": 1644, "118": 1651, "119": 1664, "120": 1676, "121": 1690, "122": 1709, "123": 1727, "124": 1741, "125": 1755, "126": 1775, "127": 1794, "128": 1808, "129": 1817, "130": 1828, "131": 1840, "132": 1850, "133": 1886, "134": 1901, "135": 1914, "136": 1927, "137": 1936, "138": 1964, "139": 1975, "140": 1990, "141": 2007, "142": 2015, "143": 2036, "144": 2048, "145": 2059}
---

**Dave Jones:** Hi, quite a few people asked me if I could do a repair of this faulty CPM 700 Research Electronics Inc Counter Surveillance Monitor. Basically, a wideband bug detector used for professional bug sweeping.

**Dave Jones:** It's quite a an old model, but you know, it's still sold today and still actually reasonably pricey, I believe, and still quite relevant. But I did a previous video on this, so that'll be linked down below if you want to check it out or maybe there's a little pop-up card thing which pops up in the corner there.

**Dave Jones:** You can just click on that. Always watch out for those little card things cuz that's a new YouTube feature where I can add stuff. But unfortunately, you can't add both cards and annotations.

**Dave Jones:** You know how I used to add little annotation windows? Can't add both. Why not, YouTube? Anyway, rant over. Um let's have a look at repairing this sucker. Now, the fault with this, you can watch the previous video to have a look, but basically, here we go.

**Dave Jones:** It's on and we've got the gain, the speaker in there, and it's basically just a wideband RF detector, couple of gigahertz, and with a diode detector in there, basically.

**Dave Jones:** And you sweep this over your, you know, under your benches, around all your tables, and around the room and everything else, and it picks up localized bugs anywhere from basically DC to a couple of gig.

**Dave Jones:** And it'll should give you a readout on the screen. And according to the manual, one of the like a self-test kind of thing is you're supposed to like hold it up to the LCD and you're supposed to be able to detect like the scan frequency on that.

**Dave Jones:** And what, did we get something there? Well, anyway, I've got the lid off and, you know, it basically does not work. It doesn't detect the uh transmitter which I've tested.

**Dave Jones:** It comes with a like a little test transmitter. That doesn't work. Also comes with a mains test transmitter as well, which transmits stuff onto the mains. You just plug it in and that doesn't work.

**Dave Jones:** So, hmm, where's the fault? Where's Wally? Now, the first thing you do is you look at the symptoms. What is actually wrong with this thing? Well, it's basically not detecting anything.

**Dave Jones:** We get noise out of the speaker, so all the audio amp and everything else is working just fine. So, maybe there's something wrong with the with the diode detection stage, something like that.

**Dave Jones:** Maybe there's something wrong with the RF amplifier because if you actually open this up, it's not just a direct antenna input. We do actually have a wideband amplifier on there.

**Dave Jones:** There we go, two of them. You can see them in there and they're obviously powered from the line up the coax because there's it's just a coax. So, they're superimposing, you know, maybe I don't know, you know, 5-V, maybe the voltage directly from the battery pack or whatever up to power these chips in here and they're just tapped off there with the inductor and the resistor there going

**Dave Jones:** off to the power rail. Very basic stuff used on all TV masthead amplifiers and everything like that. Very basic technique. So, is one of the input amplifiers here blown?

**Dave Jones:** Maybe, you know, somebody could have touched this some high voltage or something or zapped it with some ESD or who knows, right? So, is one of the wideband amplifiers faulty?

**Dave Jones:** Well, I don't think that is necessarily an issue. You might suspect it at first, but look at the other problems, right? I use this probe. It doesn't work either.

**Dave Jones:** So, either this one or this one doesn't work and they're both powered from the coax up to there. Well, this one could presumably be powered from the mains. I'm not sure.

**Dave Jones:** Haven't cracked it open. It's ultrasonically welded, all that sort of jazz, but it's unlikely that both of these are going to be faulty. So, it's either the input front end on inside here like this because that would explain both of them or quite possibly, one of the first things I would suspect and one of the golden rules of troubleshooting, thou shall test voltages.

**Dave Jones:** So, we know by inspection that this has a mast head like a just call it a mast head amplifier front end amplifier powered from the coax. Let's check the voltage going to the coax in here first.

**Dave Jones:** And I think I did I check the voltages coming out of the regulators last time? There's a dodgy regulator up here and stuff like that, but it it you know, it seems to work.

**Dave Jones:** It's you know, updating the display and the gains working and all the modes are working and stuff like that. That's got so some sort of micro in there which does all that and you know, it seems to be doing the business.

**Dave Jones:** The threshold and the gain and all of the filter works and you know, so yeah, it's I think it's something to do with the detection front end. The signal's just not getting to the detector in there.

**Dave Jones:** And of course, we don't have a schematic for this thing and we don't even have the part numbers. You can see that they've ground all the part numbers off and they've just uh texted on some their individual numbers for those chips.

**Dave Jones:** Every single device in here has had the number rubbed off. But yeah, I mean, these are just generic op-amps and things like that. So, we can you know, we we should be able to relatively easily trace this out.

**Dave Jones:** Even the micro's rubbed off and the LCD drivers and you know, stuff like that. Anyway, um the voltage is being fed in over here to the coax. So, let's see if we can measure that.

**Dave Jones:** Now, as for the power supply voltage in this thing, I'm getting uh 6.5 volts across all the main chips on the board down in there. Now, that sounds a bit odd, but 6.5 it was pretty darn close to 6.5.

**Dave Jones:** So, that's almost too coincidental like it's been trimmed there. And sure enough, if you have a look on the back here, there is a Vreg. So, there's a voltage regulator adjust and there's a low battery adjust pot.

**Dave Jones:** Now, 6.5 volts might, you know, it sounds reasonable. This runs from eight AA batteries, either alkaline or nickel metal hydride. There's a switch in there. Yes, it is set to alkaline.

**Dave Jones:** And let's say you had your nickel metal hydride, then it would drop out at say 1.1 volts per cell. That's 8.8 volts. So, you know, if you didn't use an LDO in here, they scrub the number off the regulator on there.

**Dave Jones:** So, you know, adjustable. I like 6.5 sounds reasonable, I guess. So, given that all the numbers are rubbed off the chips, and we don't know what it's supposed to be set at, I'll just leave it for now.

**Dave Jones:** I've confirmed that that works down to about 7 volts, actually, input voltage. I've got it hooked up to my lab power supply there. So, it is regulating. So, I'm going to presume that it's designed to be set at 6.5 volts because we don't know any different unless we got you know, some part numbers or some other type of adjustment service info to go with.

**Dave Jones:** And as for the microcontroller down in here, assuming that the regular pins are the power pins, we're getting 3.25-ish volts. That's pretty darn close to your regular 3.3 volt rail.

**Dave Jones:** I would have expected, like in old design like this, 5 volts. But yeah, at least we're not getting 6.5 volts on the micro. I would have been concerned there if we were.

**Dave Jones:** Now, on second inspection of this thing, I just thought I'd double-check rather than just assume that this was ground and this one down here was the power pin. Now, in that case, I was what I was measuring before, and that's what I got.

**Dave Jones:** But these are not. I double-checked that this was actually a ground, and it is not. So, what we've got here is a resistor in here, and it looks like a bypass cap.

**Dave Jones:** Now, the power pin, this side here, relative to the reference system ground down the bottom is 6.5 volts. So, the do I have 6.5 volts going into this chip?

**Dave Jones:** But, uh then the other side of this resistor here, we actually get 3.8 volts going to pin one and pin two is actually ground. So, yeah, whether this light needs that 6.5 for the LCD uh driver or whatever or what's going on there or what that device is, I don't know, but I'm not going to go chase down a rabbit hole on this one.

**Dave Jones:** Uh given that we we really don't know. I'm going to assume that 6.5 volts is the system power supply and we'll work from there. All right, we'll have a squeeze.

**Dave Jones:** There's a bead inductor. Sorry, it's hard to show you going over here, but I'm going onto the What? It ain't that wasn't going to be that easy. 6.5 volts.

**Dave Jones:** That was a nice first shot. It ain't that. So, there's voltage getting up to the probe. What we'll do now is just actually plug in the probe into here and just verify that we're getting the voltage up here.

**Dave Jones:** Okay, let's measure up its clacker, the ground, and this big uh pad up here is all the uh positive. One nice no solder mask rubbish on there and uh 5.75 volts.

**Dave Jones:** There you go. We're getting some loss on the uh coax. You'd kind of expect that. In fact, if we measure sort of the difference, let's measure the input but the ground through the coax.

**Dave Jones:** There we go. Yeah, 6 volts. Now, if we have a look at the front end here, uh you can see this bead uh goes across which carries the power being derived from here over to that's that's the point down there that goes to the center of the uh BNC and conveniently, it's AC coupled over to there and it looks like we have a terminator resistor down there

**Dave Jones:** and then is it AC coupled again over to two back-to-back last diodes. They're almost certainly a uh germanium uh type. So, that would be doing the diode detection. Reason I wanted to take a look at this front end is because we can feed in a signal here, inject a signal on the front, but we can't do that while we've got AC coupling here, but where of course we're injecting DC.

**Dave Jones:** So, if I hook up a signal generator directly to here, it's going to be outputting that 6 volts onto the coax and that could, you know, really upset your day in terms of the function generator.

**Dave Jones:** Now, of course we could AC couple the function generator, put a cap in series, or we can just simply maybe get in there and just lift one end of that beta or whatever to stop the voltage being fed in.

**Dave Jones:** Either way, yeah, we want to inject a signal into the front end. Whoa, hang on. I WAS ALL SET to like feed a signal here in the input. So, I was going to like inject a modulated signal and try to detect it so that we could trace the circuit all through cuz that's a common technique in say, you know, like audio amplifiers and stuff like that.

**Dave Jones:** Back in the day, you would have like a signal injector, like a 1 kHz tone generator that you could inject in various parts of the signal and then you'd have like a little like a speaker in a box that with an amplifier that just monitors the output and you could see the signal injected in and see it flow through the various stages and see where it stops and

**Dave Jones:** that's, you know, basic troubleshooting technique. We could have done a similar thing here, feed a signal in, and then basically see where it stops. But, I just noticed something.

**Dave Jones:** This is interesting. Look, input here, aux, and there's no input selection switch here. Aha, where's this aux input? Presumably like there's another LCD thing above that. The aux input's actually on the side here.

**Dave Jones:** It's selecting the aux input. Is it that simple? Is it like fixed to the aux input? No, cuz it came with the probes. This is like in you know, the original carry case and everything.

**Dave Jones:** Came with the two types of probes. So, I I suspect that this could be cuz there's no input selection switch. This could be an auto switch over based on when you plug it in here, there can be a contact and insertion contact that detects and switches over to the auxiliary probe input.

**Dave Jones:** So, I can I'll have I'll double-check the manual cuz I've got the original manual for this, but that would explain why the damn input's not working and the probe input's not working on the front panel and we're getting the 6 volts up there and yeah.

**Dave Jones:** Can it be that simple? Yeah. Lucky I realized that before being, you know, led down the garden path trying to trace the signal through that check the detectors working and the amp and everything else and let's sort that out.

**Dave Jones:** Doesn't sound right. Sure enough, like here's the RF probe setup. It's supposed to say probe, not aux input. And if you go over here, it does actually have an input for the auxiliary uh setup.

**Dave Jones:** Probe, there it is. Preliminary setup. I love this. It says monitoring the phone lines is for temporary testing purposes only and is not to be used for surreptitious probe interception or um other than personal use.

**Dave Jones:** Yeah, right. Anyway, um so, you can get like phone line hookups, adapters, and stuff like that. And sure enough, look, aux. So, there's got to be like it doesn't There's no other I don't think there's any other hidden switch inside or whatever.

**Dave Jones:** Have another quick squeeze for that. I think it just auto detects that aux input. Hm. Now, this is interesting. If we take the bottom panel off so that we can get access to the bottom side of the PCB.

**Dave Jones:** Here is the input jack here, okay? And it's only got the three connections like this. And if you hold it up to the light, you can see the outline it actually stops there.

**Dave Jones:** Okay, so it's only got the three pins. We've got the one ground and we've got the two inputs here. So, obviously it's if you flip that over. Sorry, I got to keep the speaker speaker's attached by a permanent wire.

**Dave Jones:** It goes off to two big ass AC coupling caps here which go over. So, that is our dual input. So, there is no switch in there. I sort of expected this to have a switch so that when you plug this in like this it detects cuz these are common.

**Dave Jones:** You can get these switches in these various phono jacks and stuff like that. As soon as you insert it, it has a mechanical contact in there which then you know signals the microcontroller down in here that uh you know, yeah.

**Dave Jones:** Okay, select this external input. It might could drive a relay to physically switch things, an electronic switch, or or do whatever required to switch a signal or an output um off and on, but it doesn't have that.

**Dave Jones:** The auxiliary input will not function if any probe is connected to the probe input. This wasn't an automatic switch over. It's sort of like feeds the signal in so you can only feed in one signal at a time either from the aux or from the input.

**Dave Jones:** So, hm but why is it got aux on there? It's obviously detecting it but like it's got to detect it somehow. It's got to switch over. Like that. Like where's the signal source coming from?

**Dave Jones:** It obviously thinks it's coming from in here. There could be some electronic switching going on here. I don't know. Haven't traced out any of this circuit yet, but yeah.

**Dave Jones:** Uh-huh. It's not going to be a simple one. So, at this stage I'm actually wondering exactly where the detection is coming from and well, you know, is it from like this side here or is it actually detecting like is it assuming that the input is the auxiliary one and then only if it detects like I the probe plugged in IE we saw it a draw we saw saw the drop on the line

**Dave Jones:** there the voltage drops so it's obviously drawing significant current the actual probe for this thing so is it detecting that I mean what is this other stuff in here I mean these you know we've got these two germanium diodes here one goes off down there taps off the input the other goes up here we've got another thing which kind of looks like a diode but that could be like a zener

**Dave Jones:** for example and then we've got a tag tan in here what's this resistor doing over here this one's feeding in the power for the probe but this one's then tapping off and going somewhere else I mean these tag tan ones I would normally suspect those tag tan ones this seems overly complex for what's going on so I'm wondering if it's somehow using this as a detection that the probe is plugged

**Dave Jones:** in but unfortunately but it's kind of hard to sort of see the layout in there and sort of reverse engineer that without taking off the front panel but nothing you can't fix without a back lit torch beauty you can see all those traces now still a pain in the butt though so by inspection what seems to be happening here is this power resistor low value resistor driving of course the

**Dave Jones:** 6.5 volts is coming from on this side and it's then driving through this choke here over to the BNC down in there to power the probe now this is looks like basically it's been used as a current shunt resistor and then it looks like they got a sense resistor which then taps off here and then that buggers off down to I think a pin five or whatever it is

**Dave Jones:** down there so what I'm going to do is measure the voltage on here relative to ground and confirm I'm pretty sure it will Um, will change value when the probe is plugged in.

**Dave Jones:** So, maybe something to do with the uh maybe there's like a window comparator on the other side that actually detects that. So, let me have a measure. So, we're getting 3 V on there with it not loaded.

**Dave Jones:** So, if we load up the probe, which is drawing current, yep, it drops to uh 2. 75. So, you know, 250 mV, that's enough to detect. Um, so, oops, clip came off.

**Dave Jones:** Well, there's your problem. So, that should be enough to detect, but of course we don't know exactly what the threshold levels is, how it uh you know, I'm pretty sure that's how it's doing the detecting.

**Dave Jones:** Why else would you sense off the uh the the voltage for the probe other than to detect when a probe is plugged in? I don't I don't see any other way.

**Dave Jones:** I mean, it's not coded anyway. It says, "Only use these uh CPM probes only." But, I think it's just detecting that there's a current draw on there. That's it.

**Dave Jones:** And if we plug in the other probe, this is the mains power the mains uh probe that uh hooks onto there. Yep, there it is, 2.87. So, it's it's drawing less current, but still it's enough to detect.

**Dave Jones:** Okay, what I'm going to do now is a little bit of manipulation to try and see if my theory is correct that uh detecting the current on the input switches this over.

**Dave Jones:** So, I've got it hooked up to my uh decade resistance box here. This is my big Bobby Dazzler, the 1433F General Radio 1 very nice precision decade resistance box.

**Dave Jones:** Of course, I could use my um IET1, but it's only uh not point uh rating 0.5 W. Not sure if that's overall or uh per step. Anyway, this is a bit higher uh per step.

**Dave Jones:** When I've got it hooked up, I've got it on uh 1K here, okay? So, this doesn't go up particularly high. This is designed for uh low values. You can see these are 10 m uh steps down here.

**Dave Jones:** So, what I'm going to do is I'm going to tweak that. I've actually got what as I said 1K on there at the moment, um and it's showing aux.

**Dave Jones:** So, 1K doesn't do the business, of course. Um trap for young players, when you're turning these things, don't switch down to zero suddenly because you'll have 00000 and you'll short the damn supply out and that could ruin your day.

**Dave Jones:** So, make sure you go around here. Uh it doesn't go up to 11. Bummer. Anyway, so 900 ohms and then we can work down in 1 ohm steps, okay?

**Dave Jones:** So, this is our voltage across that uh sense um that sense resistor there. So, there we go. We drop down a little bit, so it's 900 800 700 ohms 600 ohms 500 400 Come on.

**Dave Jones:** You can Well, no, we saw the voltage go down before, so we know it's not that, okay? So, we got ourselves 100 ohms. So, that's not good enough. So, I'm going to dial in uh let me dial in 100 ohms on the next one.

**Dave Jones:** So, 90 ohms. Here we go. This is where we're at before. Ta-da! There you go. Actually, did I hear it? Oh, sorry. I thought I heard a relay switch.

**Dave Jones:** I think that's a speaker switching, but there you go. It's It's switching between probe and aux right at coincidentally the point where our probe was. So, aha! So, that's at 800 um sorry, 80 ohms.

**Dave Jones:** That's with an 80 ohm load, it's switching over to probe. So, bingo! My theory was correct that it's doing current detection uh based on a voltage uh tap there, but why is that fair?

**Dave Jones:** Well, it could be the window detector or whatever that's going to, but bingo! Um so, But is, you know, this is an issue. We plug this probe in. These probes came with the unit.

**Dave Jones:** Two probes, looks brand new condition, original probes, everything else. It should work. So, obviously there's something wrong with this. All right, so what I've done is actually connected a 100 190 ohm load actually in parallel with the probe.

**Dave Jones:** So, now it detects Let me turn that down. So, now when I plug it in it actually detects it, okay? So, I'm sort of like forcing to detect it.

**Dave Jones:** So, I've plugged my probe in and it's going. Whoa, it's going haywire. But look at this. It's This is the thing that the manual says like go over the LCD and it's supposed to detect that the LCD is outputting.

**Dave Jones:** Now, of course this isn't shielded. It's got the bottom shield off, top shield off. It's all over the place, but uh yeah, it's now doing something. Whereas before it actually if I turn up the resistor Okay, so we haven't got probe.

**Dave Jones:** The when it's selected the aux input, we get none of that. Absolutely none of it. But if I turn that resistor box back down, so it's switched over to probe.

**Dave Jones:** Wow. Yep, so it is doing some sort of switching between those two inputs. Whoa, look at that. Oh, anyway. Yeah, this is looking promising now. Okay, so what I've done here is actually followed this sense resistor here.

**Dave Jones:** It goes down to pin five of the uh board-to-board connector down here and then that goes up to these two resistors right in there on this mystery chip 22 and pin five of that.

**Dave Jones:** And I've got myself a little Dave CAD drawing. This is a bit of the input here. This is the uh BNC connector. There's the RF uh bead there. There's a There's that low value current sense resistor.

**Dave Jones:** That's like ohms. And then uh it's sensing off that and that goes off to pin five of that board and there's two those two resistors in parallel which is interesting because that would be similar to what you do if you're trimming some sort of window comparator or something like that.

**Dave Jones:** You put two resistors in parallel to get the exact value you want. So, maybe something going on there. Anyway, we don't know what chip 22 is, mystery chip. But going back to the input here we have AC coupling.

**Dave Jones:** We've got our input termination resistor, AC coupling again, and then our basic detector. There it is, the standard and classic diode capacitor detector circuit. And yes, I have checked these are germanium diodes, 0.3 volts drop or thereabouts each.

**Dave Jones:** Anyway, that bug is off to pin two and then it looks like we've got another input here driving that. So, there might be some bias being put into the detector system front end.

**Dave Jones:** So, what's going on with this circuit here then? This is our input. So, that actually acts as a divider. Those two resistors in parallel, whatever value they are, there you go for those playing along at home.

**Dave Jones:** It goes into pin 1 2 3 4 5 6 here of this 14-pin chip. Now, I've actually measured this chip and we've got ground here and positive on pin four here.

**Dave Jones:** Now, of course course that's the classic op-amp, you know, quad op-amp LM324 type pinout. And it is not like an LM339 quad comparator which you might expect for like a window detector or something like that because that has power on pin three instead of pin four and ground on pin 12 up here instead of pin 11 here.

**Dave Jones:** So, there's definitely the classic quad op-amp power supply rail there. But of course you can use op-amps as comparators, too. So, the voltage divider formed by these two resistors plus the resistor up here on the main board here, tapped off that voltage point is acting as a comparator here.

**Dave Jones:** And this one actually pin five here assuming this is an op-amp of course goes off to test point two down here and that is important for some reason. Hey, it's a test point.

**Dave Jones:** So it doesn't surprise me that they you know would have a test point to test that sort of thing. And by the way, the other resistor in here was is 330k and 680k and the 680k looked like it had been hand soldered.

**Dave Jones:** So it could have been a select on test resistor where they actually tested at the factory. But wait, why they'd have to do that I don't know or maybe somebody's repaired or replaced it or whatever.

**Dave Jones:** Not entirely sure what the deal is there. But anyway, I've taken that out and this I've measured the test point two it's a 2.7 volts and it buggers off to all sorts of things in here and it's going and buggers off over here somewhere and it goes to town.

**Dave Jones:** It really does. So unless I want to reverse engineer this entire thing which I don't particularly want to do. I don't want this to be an absolute epic. Um then yeah, I'm not exactly sure what's going on there and this output goes off to somewhere convoluted as well.

**Dave Jones:** I don't see it like going off to the micro. There's a couple of diodes down here which are bugger off to the micro and it could make its way back via those.

**Dave Jones:** Anyway, yeah, it trust me, it's convoluted. So what I've been doing now is I've taken out the 680k and I'm just going to whack in uh my decade resistance box here.

**Dave Jones:** 680k on here. I'm just going to dial it down to get a select on test resistor basically. Oh, that's up. 580k. It's not switching over yet. We should We should hear it when it switches over.

**Dave Jones:** Don't even have to watch the display down there. Whoa, hello. There we go. 380 So, maybe we can like match it with a 330 or something like that. That Yep, switch trust me, it's switching between aux and probe input.

**Dave Jones:** All right, so I'm going to whack say a 330 in there. That looks like it's going to do the business. And that rather than figure out where everything else is going on, there might be some sort of drift in there.

**Dave Jones:** Something's changed. I don't know. Maybe one of the caps is a bit leaky or something. I could go through and replace all those as a matter of course. I don't know.

**Dave Jones:** I want to What I want to do is get a select on test resistor, 330k back in there, put the cases back on, see if it actually works. All right, I've got it all back together here.

**Dave Jones:** Get some pretty bad motorboating on there. So, not sure if that's normal. Like I've taken it around the lab, doesn't It It just you know, I could take it outside in the middle of nowhere.

**Dave Jones:** Um but it's still there. So, I'm not sure what the deal is there. That was Sorry, that was with the filter in. That's with the filter out. Whoa. It is much better with low gain though.

**Dave Jones:** Anyway, let's turn on our transmitter here. Whoa. Hello. Warning, Will Robinson. WARNING. WE'VE GOT ONE ALERT TIME. That's really annoying. No wonder they have a silent button on there.

**Dave Jones:** It's detected a candidate signal. I'm not even near it. Maybe cuz it was on the bench and it was propagating. So, if I put it into monitor mode, once you can see the threshold level here that we're setting, once it gets down towards the candidate signal, Bingo.

**Dave Jones:** So, there's our signal. So, it's showing signal strength. And now, if I put it near the antenna here, threshold, put it near the antenna, bingo. Let's see if we can get some feedback here, too, cuz this has a microphone built in.

**Dave Jones:** So, let's switch it on. But, if you put the mic on, I'll shut up. Okay. And we put it in. Hang on. Well, there we go. So, if you get the mic closer, we get feedback.

**Dave Jones:** Check. Check. Check one, two. Hello, it's coming through. Must be those Russian spies. So, if you actually turn the annoying gain down for the speaker and actually kill the audio uh part of it and, you know, like cuz you'd usually monitor with uh headphones or something like that, especially if you're listening for mics and stuff like that.

**Dave Jones:** But, if you're just trying to detect RF uh signals, then you can see that we've actually got quite a strong one here. And then, you can walk around with this thing and say, "Oh, look, there's something there." And, you know, you might set the threshold, but you move around, get your wand in and out, and you get close, and Hello.

**Dave Jones:** Hang on. Whoop. Gotcha. So, that basically seems to be working bang on. It's just, yeah, this stupid audio gain. Of course, it's just picking up wide band crap and stuff like that.

**Dave Jones:** So, it could be anything switching lot lights switching or any sort of crap like that. So, you want to just kill the audio side of it and just rely on that transmitter.

**Dave Jones:** So, beauty. Um that seems to be working just fine now. But, of course, you know, to actually test the full performance of the thing cuz I don't know what actually caused that uh threshold fault.

**Dave Jones:** Um not threshold on the front, but threshold for the uh probe detection. It seemed like it was really marginal. It was a right, you know, the those resistant that resistor was selected.

**Dave Jones:** And as I said it was sold as somebody had a play with that. So, I'm not sure what the deal is there but yeah, anyway it's detecting the probes just fine now and it's doing its job.

**Dave Jones:** So, winner winner chicken dinner. No detector. And of course to fully characterize this thing we do have the specs for the RF probe here. So, we could you know attempt to you know verify these performances and things like that but that's sort of outside of the spec of this video this simple repair video but ultimately I did find an issue and we kind of sort of fix it up.

**Dave Jones:** I still don't know why the reason for it but you know I think that just the probe detection is not going to affect any of the performance aspects in any way but you know assumptions are the mother of all screw ups.

**Dave Jones:** So, you know it probably does need a proper proper performance verification and I'd love to get a reverse engineered schematic of this thing. So, maybe I can put some high res photos up if everyone anyone wants a crack at it.

**Dave Jones:** I might get around to it one day if there's enough interest in this thing and then you know once you have the schematic you can go in there and uh find out exactly why that threshold was out.

**Dave Jones:** Yeah, I still don't know but anyway tweak of the value in there fixes the threshold your probe and plug the probe in and out and it's all uh it's all hunky-dory now.

**Dave Jones:** There you go. Bobby Dasler. Now, I just realized that those resistors in there didn't make sense resistor values. We had 47k as the feedback resistor and part of that divider and 330 and 680 and if you work it out the divider ratio it doesn't make sense with that 2.8 volts Uh like that uh test point uh that we actually measured as the as a detector for the probe.

**Dave Jones:** So, that sort of doesn't make sense. So, whether or not that um reference voltage is off and you know, maybe that could as I said, that goes to other parts of the circuit, I think, and it might upset some other things.

**Dave Jones:** I'm not entirely sure if it affects the performance still. You need a you know, you'd really have to look at the full uh schematic for that. But, yeah, I'm not 100% confident with this thing, but at least we solved that probe problem and we did uh get the thing basically working and detecting stuff.

**Dave Jones:** But, still, yeah, I think further investigation required here. So, that was a rather interesting repair on this thing and a little bit lucky in that I actually noticed that uh the um it was in aux mode aux input instead of probe input.

**Dave Jones:** So, you know, the first rule of uh repair troubleshooting is thou shall test voltages. I guess the second one should be thou shall understand your equipment, how it works.

**Dave Jones:** Do your research on how it actually uh works. So, yeah, if I read the manual, I wouldn't, you know, like don't assume anything. You know, I could have gone down the garden path there if I was just assuming that the um the probe, but you know, I guess I would have eventually uh noticed it and I did and then that led us down the path to finding a threshold

**Dave Jones:** uh issue. I mean, at the start of this, I would have put money on that it was the um uh the power supply, the voltage feeding up for the uh probe, for the masthead amp and everything else, but no, wasn't that.

**Dave Jones:** It turned out to be something a little bit more interesting than that. Anyway, hope you enjoyed it. If you did, please give it a big thumbs up cuz that always helps a lot and always click that There's a little bell icon down there, down near the subscribe button there.

**Dave Jones:** Make sure you enable that so you get all my email subscriptions and all that sort of jazz. Anyway, hope you enjoyed it. Catch you next time. Mhm.
