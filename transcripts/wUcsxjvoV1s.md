---
video_id: wUcsxjvoV1s
title: EEVBlog #426 - HP 3457A Multimeter Teardown
url: https://www.youtube.com/watch?v=wUcsxjvoV1s
source: youtube-asr
timestamps: {"0": 2, "1": 15, "2": 35, "3": 50, "4": 64, "5": 72, "6": 86, "7": 98, "8": 111, "9": 125, "10": 143, "11": 154, "12": 165, "13": 181, "14": 192, "15": 211, "16": 223, "17": 232, "18": 246, "19": 263, "20": 271, "21": 288, "22": 303, "23": 319, "24": 332, "25": 348, "26": 364, "27": 373, "28": 383, "29": 392, "30": 399, "31": 412, "32": 421, "33": 429, "34": 439, "35": 449, "36": 458, "37": 486, "38": 500, "39": 514, "40": 524, "41": 537, "42": 549, "43": 565, "44": 579, "45": 600, "46": 613, "47": 627, "48": 641, "49": 658, "50": 670, "51": 684, "52": 703, "53": 712, "54": 726, "55": 741, "56": 754, "57": 764, "58": 779, "59": 791, "60": 811, "61": 823, "62": 833, "63": 846, "64": 859, "65": 870, "66": 882, "67": 900, "68": 907, "69": 918, "70": 927, "71": 951, "72": 963, "73": 972, "74": 984, "75": 1002, "76": 1011, "77": 1028, "78": 1044, "79": 1051, "80": 1064, "81": 1080, "82": 1094, "83": 1118, "84": 1129, "85": 1144, "86": 1162, "87": 1177, "88": 1194, "89": 1206, "90": 1231, "91": 1249, "92": 1265, "93": 1278, "94": 1307, "95": 1316, "96": 1330, "97": 1344, "98": 1364, "99": 1381, "100": 1394, "101": 1405, "102": 1426, "103": 1442, "104": 1452, "105": 1463, "106": 1476, "107": 1486, "108": 1503, "109": 1514, "110": 1528, "111": 1546, "112": 1561, "113": 1574, "114": 1584, "115": 1604, "116": 1629, "117": 1643, "118": 1660, "119": 1676, "120": 1689, "121": 1704, "122": 1724, "123": 1736, "124": 1752, "125": 1765, "126": 1774, "127": 1789, "128": 1801, "129": 1824, "130": 1848, "131": 1862, "132": 1887, "133": 1903, "134": 1915, "135": 1936, "136": 1944, "137": 1959, "138": 1972, "139": 1983, "140": 2003, "141": 2018, "142": 2037, "143": 2062, "144": 2074, "145": 2092, "146": 2114, "147": 2127, "148": 2141, "149": 2155, "150": 2163, "151": 2176, "152": 2197, "153": 2209, "154": 2223, "155": 2235, "156": 2254, "157": 2265, "158": 2280, "159": 2289}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. You've seen me mention my HP 3478A five and a half digit classic bench multimeter before. I've used it in quite a few videos. Well, you may have noticed behind me I have upgraded.

**Dave Jones:** Tada! The HP 3457A six and a half digit multimeter. Big score on eBay. Got it for just over 150 Australian dollars. Fantastic and it's bang on. Beauty. So I thought we'd crack it open, see what makes it tick.

**Dave Jones:** Could be interesting. Let's go. And here it is hooked up to my MV106 transfer voltage standard you've seen in that previous videos. Yes, I did violate my don't turn it on, take it apart rule here.

**Dave Jones:** I just wanted to tweet some photos and check its performance before I go rip the thing apart today on Teardown Tuesday. And as I said, got it on eBay for like 150 bucks and it really is a very nice meter.

**Dave Jones:** It comes with that cal stickers. It's a couple of years out of date, but still that's not bad at all. We'll have a good close up view of it, but here it is.

**Dave Jones:** It I've hooked it up to the MV106. I've set it to 1.00000 volts. I've only got five decimal places there. This thing of course has six decimal places. It's a six and a half digit meter.

**Dave Jones:** In fact, technically with some averaging in high res mode it's capable of seven and a half digits, but you can't get that via the front panel. Apparently you have to do that via the GPIB remotely.

**Dave Jones:** So I do get fairly lucky with these bits of gear on eBay. Absolutely bang on and of course if I dial that up one digit there, you can see it basically changes by 10 least significant digits.

**Dave Jones:** There's a bit of noise there, bit of fluctuation. We can maybe change the power line cycles or something like that. So, anyway, if you want me to do a separate video on using this thing and having a play play around with it, let me know.

**Dave Jones:** So, that's actually not a bad upgrade to the classic HP 3478A. This one's a 3457A and while it's not a metrology grade multimeter like the famous 3458A. This one's the 57A.

**Dave Jones:** Don't get uh confused between the two. It is still a very impressive instrument and really it's hard to beat for any modern multimeter under a thousand bucks for example.

**Dave Jones:** So, you know, to get this thing for a hundred fifty bucks, it's a bargain. So, they're certainly worth paying a couple hundred bucks for if you're in the market for a six and a half digit multimeter.

**Dave Jones:** It's performance is still pretty impressive. It's a 1980s vintage mid to late 1980s. I'm not sure when this one was actually uh designed. We'll find out manufactured. We'll find out when we crack it open by the date codes on the chips and things like that.

**Dave Jones:** But, yeah, it's still a pretty darn good meter and of course it uh one thing my 3478A doesn't have, it's actually got a microamp range as opposed to milliamps.

**Dave Jones:** So, there it is. Bang. Look at that. So, that's a hundred picoamps resolution. Very, very nice bit of kit indeed. And in terms of you know, basic DC volts accuracy on this thing like the 24-hour spec on this thing is pretty good.

**Dave Jones:** It's down in the order of you know, 18 ppm or something like that. It's quite a nice bit of kit. So, if you can pick one up for a decent price, highly recommend it.

**Dave Jones:** Now, while it may look like a big bit of kit sitting on your bench with its big wide front like that. You can see it here compared to the 3478A which is actually quite deep.

**Dave Jones:** And it's actually not that much physically bigger in terms of volume at all, and it's not that much heavier either, which means that you can get shipping usually for quite a reasonable price on these things, even international.

**Dave Jones:** But as always, some equipment dealers like to rip you off. I got this thing delivered via DHL for like 70 bucks or something. So for me, it's a worthwhile upgrade just for the DC current range at microamp range capability.

**Dave Jones:** The accuracy of this thing, I won't go into specs on this. If you want me to do a review of it, say you know, compare to it or something like that, let me know.

**Dave Jones:** But yeah, the specs are a little bit better than 3478A, but it has got some additional ranges and all the math capability and stuff like that as well. So a better instrument all round basically, but it has that larger wide form factor.

**Dave Jones:** Whereas this one is, you know, half width half rack width. So that's probably its main disadvantage is that it can take up some additional space on your bench in terms of width, you know, instrument width on your shelving.

**Dave Jones:** But apart from that, lovely bit of kit. I love it. And here's the front panel for those playing along at home. DC volts, AC volts, ohms four two and four wire, DC current, AC current and frequency measurement as well.

**Dave Jones:** And it's got range, you know, auto manual range selection, display digits and six and a half digits. As I said, it is technically capable of seven and a half digits, but getting that to work on the front panel is not possible.

**Dave Jones:** I believe you've got to do it via the GPIB. As I said, and if we take a look over here at the configuration buttons, we've got the number of power line cycles, so you change the integration time, effectively the uh update time, and that averages things out for you.

**Dave Jones:** It's got auto calibration, auto zero, offset compensation. Uh it's got various uh triggering capabilities and it's got an input uh scanner, an optional input scanner as well, but they're usually a very expensive um option to like you can have multiple input channels as we'll see.

**Dave Jones:** There's um a slot on the back to actually do that. This one's not configured with that. And you can uh uh store and report and recall various uh configuration settings.

**Dave Jones:** And then there's the uh math capability. Now, unfortunately, this thing doesn't have a huge memory uh on it. It's only I think it's only 1K or 1 and 1/2K or something like that.

**Dave Jones:** And I'm not even sure if uh that is the number of readings. I think it's actually less uh than that in number of readings depending on the resolution mode you've got this thing in.

**Dave Jones:** So, you know, you might only be able to store a couple hundred readings, but you can certainly do some usable math and get math and get uh standard deviations and stuff like that.

**Dave Jones:** And of course, we've got uh proper binding post uh inputs here. It's got uh four wire input uh for ohms and uh separate current fused current uh terminal down here.

**Dave Jones:** Now, there's one minor disadvantage compared to the 3478A this one's replacing in my lab here. Um it's only got the front panel terminals. It doesn't have them duplicated on the back.

**Dave Jones:** For my purposes, doesn't matter a rat's ass, but if you've got, you know, wiring these into a production uh test rack or something like that, that sort of thing could matter.

**Dave Jones:** And check it out. It does have calibration stickers on it. Uh unfortunately, it didn't actually come with the calibration certificate, of course, but it's fairly recent. Uh you know, April 2011.

**Dave Jones:** That's not bad at all. I'm certainly not going to complain about that and that's the reason why it's bang on cuz these things, you know, they don't drift much, folks.

**Dave Jones:** So, really, once you've uh you know, if you got it calibrated a couple of years ago, I was pretty confident I saw this in the ad and I went, "Well, you know, that's good enough for me.

**Dave Jones:** I'm you know, I'm taking a bit of a risk, but I I thought this one would be bang on and it was. Now, interestingly, it's got analog devices on here and it seems to have come from owned by analog devices themselves and they presumably have their own internal calibration metrology department which calibrated this thing and we've got another sticker here telling you what capabilities it's been calibrated over

**Dave Jones:** voltage, current and resistance. Not a problem. By the way, it's it was calibrated in 2010. I presume it wasn't calibrated again after that. They probably just let the thing expire, but still that's pretty recent.

**Dave Jones:** It's got a sticker there here that says ADPI. I'm going to guess that stands for analog devices of course production instrument. So, I think this was used in their production environment for manufacturing the analog devices chips.

**Dave Jones:** One you know, those automated test racks and something like that which is why it's in you know, fairly good nick for its age really and it's got a sticker from test equipment depot, but I didn't actually get it from them.

**Dave Jones:** I bought it from another eBay dealer. So, I don't know whether or not they got it from them or what the deal is there. And it's made in the good old US of A serial number 2703A.

**Dave Jones:** A stands for made in America and that's the actual serial number 11,838. No option 700 just the standard option. And there's a slot for the scanner. As you can there's no panel on that.

**Dave Jones:** Didn't come with it, but there's the internal connecting cable for that scanner module. You can pay a couple of hundred bucks for those low EMF relay switching modules. So, unless you really need that capability, don't worry about it one bit.

**Dave Jones:** And it's got GPIB of course or HPIB as they call it and it's got a voltmeter complete output so a signal 5 volt TTL signal when the when it's actually completed and an external trigger input as well.

**Dave Jones:** Standard IEC mains and switchable from 110 to 240, so not a problem. It doesn't matter where you buy this thing, it's going to be usable. And we've got ourselves a couple of calibration void if seal broken stickers, so we'll go right through those.

**Dave Jones:** Lovely, the feeling you get when you crack open the warranty void if seal uh I sorry, calibration void if uh seal broken sticker. Fantastic. There's no screws on the back of this thing by the looks of it.

**Dave Jones:** It looks like it's all sort of done from the bottom here, so I don't know whether or not these screws go all the way through or not. I'm not sure what the deal is there.

**Dave Jones:** Yeah, I think they do. The I presume that the top Those things don't fall out. Lovely design there, captive screws, so this should Yep. Ta-da! Just lift straight off.

**Dave Jones:** Beautiful. All shielded. That's what you'd expect in a 6 and 1/2-digit multimeter. Warning, this panel connected to terminal low, and that's not surprising at all. That internal shield there is connected to your ground.

**Dave Jones:** It's not connected to uh mains earth. It's just connected to the ground on the front panel. And we can verify that by mains earth there, and there we go.

**Dave Jones:** There's no connection whatsoever through to the ground terminal because of course it's uh floating. That's what you'd expect in a multimeter a bench multimeter like this, but you'll probably find that this power supply shield over here is connected.

**Dave Jones:** Yeah, there we go. That one is connected right through, but this one is just internal uh ground connected for you know, it's all part of the uh system ground design to uh shield all the electronics and uh ensure there'd be lots of low EMF uh design in this, lots of star point grounding, and stuff like that.

**Dave Jones:** And they deliberately kept it from mains earth as all part of the system grounding functionality to ensure that they get the 6 and 1/2 digit performance in this thing.

**Dave Jones:** So, this grounded top cover here, and when I say grounded, I actually mean ground and not mains earth as we just saw. They're actually It's through to the bottom cover down here, which is also uh separated from mains earth over here.

**Dave Jones:** So, that one is just the uh shielding cover for the uh relay input switching matrix board, which then slots in underneath here. So, we should be able to lift that out and somehow It's got instructions there.

**Dave Jones:** Should read it. And if we just flip that uh cover open, it's uh held on there by this ribbon cable it's attached on. And won't disconnect that unless I absolutely have to, but uh you know, warning, caution, caution.

**Dave Jones:** We've got some uh We've got a gain and uh flatness control here that uh warns you that it's input high. Uh that's connected to the input high potential, and there's a V offset adjustment as well.

**Dave Jones:** So, but they're the only two adjustments that you can get through this thing. So, we should be able to lift this plate off and see the uh measurement and uh acquisition board on the bottom here, separate from the power supply and digital uh display board over in this part.

**Dave Jones:** You can see the ribbon cables go into the uh keypad and the LCD and stuff. That's all digital control. There'll be some ROMs under there, microprocessor, but this is all your interesting measurement stuff under here.

**Dave Jones:** So, it looks like this thing just unlatches. Yeah, there's some sort There we go. You just push these latches back like that. They're not easy, but unlatch this side first and then you're probably going to unlatch this side over here.

**Dave Jones:** Yep, there we go. And that's a nice design. I like that. Ta-da! Look at that. Oh, can see the voltage reference board straight off the bat. And uh whoa, lots of relay switching.

**Dave Jones:** Whoa, good stuff. And one of the first things I noticed, of course, as part of the uh system design, keeping these grounds separate, you'll notice that there's only two connecting cables on this thing.

**Dave Jones:** One is coming from the transformer over here, so it's got its own transformer tap going over there. That's of course uh isolated due to the uh transformer. Then it's got its own uh just linear rectifier and linear regulator over here.

**Dave Jones:** And then down in the bottom is the only other connection between the digital board down here and the uh and the main signal uh processing board and ADC board over here.

**Dave Jones:** And you'll notice that it looks like there There it is. Opto-isolated. And you can see that opto-isolator down in there with the big slot uh going right through the board.

**Dave Jones:** They've even cut this uh ground uh earthing trace over here cuz this would be connected. You'd just ruin your uh system ground if you connected that straight across. So, they've actually cut that uh straight through with the slot.

**Dave Jones:** And they've used these uh optocouplers here, but they're they're like one of those uh optocouplers you'd see, you know, um uh like in a photocopier or something like that, where you can actually put uh something in in between like that and it just cuts off the signal between the two.

**Dave Jones:** So, that's rather interesting. I wouldn't have expected to see a you know, a basic uh DIP package uh optocoupler or something like that, but they've gone with that type.

**Dave Jones:** So, they're doing that to keep the entire ground system separate. This is the grounding point. So, if we measured, say, this uh screw over here, it'd be on the metal shield.

**Dave Jones:** That'd be going through to the ground connector on the front panel. And of course this one over here is connected through to mains earth as we saw in the measurements before.

**Dave Jones:** Now, my idea for why they've chosen that type is it's probably just basic built-in braces engineering. These type of, you know, going to have a larger withstanding voltage, larger isolation voltage just purely because of the huge physical gap and isolation between the phototransistor and the diode on this thing.

**Dave Jones:** So, yeah, my guess is it's they were much better than the DIP package. So, maybe they just had a higher withstanding voltage than say a standard 4N25 optocoupler or something like that.

**Dave Jones:** But, yeah, I don't know. You'd have to actually get the data on that one. But, even your standard optocouplers are pretty darn good. So, I don't know. Maybe there's some serious built-in braces happening there.

**Dave Jones:** And there you have it. It's not a 1980s vintage, folks. Sorry to disappoint you. It's 42nd week 90. Probably around about the earliest date code I can find on this thing.

**Dave Jones:** The chips seem to be around the 40th or 50th week 1990. So, I'm not sure when they actually stopped manufacture on this thing. If you actually know the start and end manufacture dates on the 3457A, do let us know in the comments or on the forum.

**Dave Jones:** I've popped the top cover off the processor board here, and you can see the lovely power switch extension bar there going all the way back. I love those extension bars.

**Dave Jones:** Great engineering. And there's the backup battery in this thing, lithium battery. Check it out, folks. Made in Britain. Hi to all my British viewers. It's an Eternacell 3-volt battery, and it doesn't look like it's leaked at all.

**Dave Jones:** You have to be very careful, by the way, when you're opening these things, servicing them, prodding and poking around in these things. Don't short out that battery at all, and don't replace it with the power off because you will lose all your calibration data in this thing.

**Dave Jones:** So, I'm going to check the voltage on this, make sure it's still good. Now, make sure I don't have my meter set to amps because that would be really embarrassing.

**Dave Jones:** I'd short out my battery and I'd lose all the fantastic calibration and the bang-on-iness, if that's a term, I'm going to invent it, of this thing. So, let's have a look.

**Dave Jones:** Tada! There we go, 3.06 volts, beautiful. I'm not going to touch that sucker. Now, this is interesting. This processor board seems to have been manufactured at a different time, 4 years prior to when the ADC board.

**Dave Jones:** Most of the 74HC chips on here all seem to be dated '86. Look at that, 40th week, 1986, 44th week, '86, all within the same, you know, all within the same order.

**Dave Jones:** 23rd week, '86 up here. So, almost every one of them. So, that is weird. Why that processor board was clearly manufactured, you know, around I'm presuming around '86, otherwise they bought an absolute buttload of these chips back in '86 and they were still using them 4 years later.

**Dave Jones:** I don't know. It doesn't, you know, it doesn't wash. I mean, all of them, the Intel processors, all these chips all around '86, whereas all this board over here is all 1990 vintage.

**Dave Jones:** I mean, check it out, even the system ROM has a date code of fifth week, 1987. My guess is, well, this is a 1987 vintage instrument, but it's had a complete upgrade of this board in 1990 or so.

**Dave Jones:** That's the only conclusion I can come to. Now, this is really interesting. Check out all of these uh parts around here, including this um part here on the voltage of reference board here, they're all got 1826-something.

**Dave Jones:** Four or five Linear Tech parts there, plus National and TI. Yet, they've all got that same 1826- and then a number like 1382 and uh you know, 0521 and uh 1265 and all sorts of stuff.

**Dave Jones:** So, it looks like HP have had these sort of like uh custom branded. They are, of course, off-the-shelf parts. They aren't like custom chips. They're just regular off-the-shelf parts, but they've had them rebranded possibly with the HP part number.

**Dave Jones:** Now, one thing you won't find in a precision instrument like this is a cooling fan. Why? Well, A, it it doesn't generate a huge amount of heat. I think this thing's rated for like uh 30 W maximum consumption or something.

**Dave Jones:** It could be uh a lot less than that in actual uh power draw. But, because when you have a cooling fan in there and it's sucking air through the side vents, for example, in a typical product and then going out, well, you're creating thermal gradients within the product and over the parts, in particular, the voltage reference down here, which we'll take a look at, and other parts of the board.

**Dave Jones:** And you don't want thermal gradients because if you've seen my thermocouple video, you'll know that basically any dissimilar metal junction within this unit, any junction at all, solder and copper uh clad board and everything else creates dissimilar metal junctions acting as a thermocouple.

**Dave Jones:** So, you're going to get EMF voltages generated in the unit. So, you don't The last thing you want in something like this, you would rather have it heat up to a warm temperature and stay nice and even than try and cool it down with the air flow through the thing.

**Dave Jones:** and we can demonstrate this. All right, what I've got here is my resistance standard uh hooked up to this thing. It's close enough to uh 10K here. So, this least significant digit here represents one ppm of that 10K.

**Dave Jones:** So, one parts per million. And you know, this thing it's tempco is incredibly low in the order of like you know, parts per million. So, any uh you know, change in temperature in here can actually generate um uh EMF small EMF effects which can affect or thermal couple effects in the joints uh or a temperature gradient across components that can actually affect the reading when you're talking

**Dave Jones:** down in this region. Now, I can wave my hand around in here so it's not noise pick up or anything like that. Okay, so what I'm going to do is actually breathe on the circuit in here and you should see this significantly change.

**Dave Jones:** Let's give it a go. Look at that. There you go. That's changing by like hundreds of ppm. Look at that. Hundreds of ppm just by breathing over that circuit there.

**Dave Jones:** So, that is a really big deal for a six and a half digit precision meter like this. So, that's precisely why you won't find a fan in a precision bit of kit like this.

**Dave Jones:** You do not want all that air blowing over and creating those uh temperature differentials across your component. It's a big no-no. And if you take a look at the processor board down here, somebody's actually texted on the serial number for this unit 2703A uh 11838 and then a date code in '93.

**Dave Jones:** So, something and some other numbers there. So, something was done to this thing in 1993. I have no idea what. That is a uh couple of years after the or three years after the uh '90 dated uh chips 1990 dated chips on the analog board.

**Dave Jones:** As for the main board here, we have more HP custom part number branded chips. Here's the main processor U601 here, and it's some sort of Motorola part, but it's got this 1820 2624 part number.

**Dave Jones:** And that looks like a HP part number. Like here, the these resistor networks. Look, these are these are all 1810 and 1820 you'll also find down here. Check this out.

**Dave Jones:** Here we go. Here's a national part 1820 as well. Here's another Harris. I think that's a Harris part down here 1820. There it is again. Um that I believe is the keyboard front panel keyboard controller cuz it goes down to the ribbon cables to the front panel or the LCD.

**Dave Jones:** Sorry, the LCD's got its own controller, but yeah, they got these freaking custom part numbers on them. Real pain in the ass. And here's the schematic which I'll actually link in in the notes below so you can load up the PDF of the service manual.

**Dave Jones:** It's got the full schematics in here. They're a little bit hard to read, but there's the main processor U 601 there that we looked at. And then of course it's got you know the RAM and ROM.

**Dave Jones:** It's all very traditional stuff down here or miscellaneous control stuff. We got the speaker down there. Nothing really majorly important there. And then yeah, here's an extension of it.

**Dave Jones:** It's one of these big long schematics so it's got to be broken up. And then we've got our HPIB / GPIB uh controller stuff around here. We've got um the non-volatile RAM control.

**Dave Jones:** There's our internal battery there. So you can see how that just continually powers that. That's just diode or there. And there's a right calibration lock circuit as well. Watchdog timer.

**Dave Jones:** It's all there. All pretty basic digital stuff. But what that actual Motorola processor is I don't know. One of the Motorola 8-bit processors most likely. And then we have our optocoupler link between boards, and that's what we looked at down below.

**Dave Jones:** That's that There you go. It's just a serial in and serial out data connecting the two boards together. And of course, this analog board over here actually has its own control processor.

**Dave Jones:** And there it is. That's an Intel 8051 microcontroller. And look at this national device here. That's actually I don't know if you can hear that, but that's actually not plastic or anything.

**Dave Jones:** That feels like and sounds like ferrite. So, they've surrounded all of the leads on this chip here, kind of like maybe as an afterthought, that they've put like a little effectively a little ferrite bead uh through each one of the leads on that National Semiconductor device.

**Dave Jones:** I wonder why. And of course, we don't know what the bloody chip is cuz there's one other one of the stupid part numbers. 1820-3174. And here's another device down near the input down here.

**Dave Jones:** What the hell is this doing? This is an 1820-3861. Man. But thankfully, of course, you can pretty much tell what that's going to do based on the proximity of these relays.

**Dave Jones:** I don't see any discrete transistor drivers for all these relays down here. So, that's probably a relay driver chip. And if you have a look at the schematic, there it is.

**Dave Jones:** Relay control U121. And you can see a whole bunch of catch diodes there, which are the get the back EMF of all the switching coils. But basically, all of these relays, they're going to be used for not only switching the inputs, but they're used for the test modes as well.

**Dave Jones:** They can short the inputs, they can disable them, and route them through to other test signals. Cuz this uh meter has a fairly uh comprehensive built-in self-test. So, this 8051 microcontroller, it uh basically, you know, it uh does the relays, it handles the uh it optional input uh switching card, which uh sits on the top, and basically uh handles the ADC as well, and there is the custom hybrid ADC in

**Dave Jones:** this thing. This one ain't off the shelf by the looks of it. So, there you go. I have no idea what that ADC is. Um it's a, you know, some sort of maybe HP uh custom hybrid ASIC ADC or something like that to get the performance.

**Dave Jones:** I don't know. And here it is, U511, that's the uh hybrid-looking custom ADC thing there, all with it, you know, that's the entire AD uh converter circuitry around here, and you can tell, you know, we really start getting into our precision measurements here.

**Dave Jones:** We've got guard nodes marked around here, matched transistor, matched JFET transistor pairs, and uh stuff like that. And here's our uh reference board over here. That's got our uh reference Zener on it, and we'll take a look at that.

**Dave Jones:** But uh yeah, that um ADC is, of course, uh clocked and controlled via the uh 8051 processor. And here's what a lot of people want to see, what is the ref the voltage reference used in this thing?

**Dave Jones:** Well, this is the uh PCB assembly here. This one is obviously the uh reference um Zener diode with a built-in uh heater, too, of course, but it's a linear technology part.

**Dave Jones:** But once again, that custom HP part number, 1826-1249-5, with a date code of the 36th week, 1990s. And once again, we've got another linear uh technology part over here, but once again, HP part number branded, but that's just a precision op amp uh clearly.

**Dave Jones:** So, there's, you know, there's nothing else going on there. And it uh generates the uh plot, I believe, plus minus 10 V reference voltages, which we should be able to measure on those two test points, I'm assuming.

**Dave Jones:** And I'll just verify that. I'll just probe I assume that that uh nut there is ground. So, I'll just probe that. Yeah, minus 10.175. Of course, it doesn't have to be precise because the uh um And of course, it's exactly There you go.

**Dave Jones:** The positive is the exact opposite of that. So, it generates plus minus 10 V supplies, and they don't, of course, have to be spot on because this thing uh compensates for that with the calibration values in the software.

**Dave Jones:** And of course, the key to an instrument like this is not its absolute accuracy. As I've said before, that voltage reference down in there, it can be plus minus 5% absolute accuracy.

**Dave Jones:** You don't care. What you care about is the temperature coefficient, i.e., the uh drift per degree Celsius. How many ppm per degree Celsius drift? Is it 100 ppm? Is it 10 ppm?

**Dave Jones:** Is it 1 ppm? You know, it's really precision stuff like used in say the 34 uh 58A, for example, one of the world's best multimeters and the big brother to this one.

**Dave Jones:** Well, it's not about its absolute accuracy. You can just trim it to anything you want. It's all about the drift. Now, this reference board here, as I mentioned, uh the designator is A25, and it is exactly the same HP part number as the one used in an earlier model uh 3456A, which we do actually have the schematic for.

**Dave Jones:** And here it is, the A25 reference board 03456-66525. And that's exactly the same part number as what's used in this uh 3457A. And as you can see, the same uh a four-pin device here with the internal heater like that and there's the internal zener diode and of course it amplifies that and of course there's not much to it.

**Dave Jones:** It's all about the stability of the zener diode itself, you know, very carefully selected, very carefully tested and characterized for the performance in this thing and you know, there's nothing else on this board.

**Dave Jones:** There's one, two, three resistors and a cap and that's exactly what I see on this board, three resistors and a cap. So, it's an identical board and the service manual for this instrument gives you 500 listed as an LM 299H and that's the classic National Semiconductor reference, but the one we've got here is a linear technology.

**Dave Jones:** So, what but it's still four-pins and in case you're wondering, it also lists you 501 here, which is just an LM301. Now, it's hard to actually get in and see under there, but I can actually see it and this is actually a four-pin device.

**Dave Jones:** So, clearly two of the pins are for the zener diode and the other two are for the heater. And you can see there that we're measuring, you know, roughly like 42, 43° or something on that on that chip.

**Dave Jones:** I the laser's not directly on it cuz there's an offset there when it's up close, folks. So, I haven't let this thing warm up to temperature, but you know, if you move it to the side, you can see that that is obviously got a heater in it to heat up the zener and that would be temperature controlled as well to keep that at a constant temperature.

**Dave Jones:** And if you have a look at the input terminals down in here, yes, they are just wired directly across like that, but they do go through a toroid filter.

**Dave Jones:** They're wrapped around in there, quite nicely heat shrunk down in there and then they go directly into the relays, but because this uh thing is all uh metal uh grounded, shielded, stuff like that.

**Dave Jones:** You can uh get away with uh those effectively quite long leads going from the input terminals. And there's a uh 1.1 ohm high-value resistor. That's uh most likely our input uh current shunt resistor.

**Dave Jones:** And you'll notice all the star grounding branching off from that point. Really is quite nice. And this board mounted on top here, this is the AC converter board. It's doing all the true RMS uh stuff and AC conversion.

**Dave Jones:** Couple of switching relays and those adjustments which we saw in the uh top uh through the top metal uh can. And yes, we've got more HP part numbers. Look at that, 1826 there, 1826 up there for that Analog Devices part, and more of them all the way up the top.

**Dave Jones:** HP part numbers as far as the eye can see. And if we pop that AC converter board out, there's only two wires uh levering that thing on. Nice uh silkscreen designator is all on the bottom there, component designators.

**Dave Jones:** That's also got its own metal shielding can, so we should be able to remove that. And woho! Hello! And looky what we have here, folks. We have a whole bunch of uh well, they at first glance you go, "Whoa, what are they?" They don't look like the other relays, but of course uh Coto is a dead giveaway.

**Dave Jones:** Coto is a very uh high-quality manufacturer of um precision uh low EMF reed reed relays and uh stuff like that. So, these are 0490-1555. Haven't uh been able to find the exact data sheet for that one on a quick uh glance, but they would yeah, be some sort of maybe uh shielded or uh low noise uh low EMF uh relay or something like that.

**Dave Jones:** But we've got ourselves a hybrid. And we also have ourselves a genuine badge. Check that out. They've even heat shrunk the leads. Look at that. Beautiful. And a look at our schematic, folks, reveals all.

**Dave Jones:** U101 is the input hybrid board there and it's got all the switching. Look at that. All the FET switching required for all of the input circuitry. Cuz here's our input circuitry over here and here's the input circuitry here.

**Dave Jones:** There's some ohms over voltage protection there. Here's all our input relay switching stuff. There's our input fuse, by the looks of it, and various switch range switching stuff. So, like you can sort of equate that to say similar to like a Fluke custom input switching hybrid that they use in their multimeters, for example.

**Dave Jones:** So, that's all on that one board and that would be very well matched. And then, of course, the output of that goes into these matched transistor pairs here, precision op-amps, and various other stuff.

**Dave Jones:** So, you can, you know, take a look at this uh schematic until the cows come home. But, there's the ohms current source, for example. Great stuff. There's the input amplifier, which I said, and there's the matched transistor pairs.

**Dave Jones:** And then, we've got a pre-charge offset circuit ah and an offset DAC, as well. Now, that certainly is a very interesting hybrid board, indeed. Obviously, all the circuitry's on the bottom.

**Dave Jones:** They've just got this big ground plane on the top here. There's only one extra trace on there, apart from the ground. And it's actually held in by these two screws.

**Dave Jones:** And it looks like they just press into those pins, those gold plated pins sticking up from the board. So, I should be able to undo those and lift that board off without any damage.

**Dave Jones:** Well, sorry, folks. That's not the least bit exciting. It's all encapsulated. Looks like it's got epoxied in. You could probably, you know, if you wanted to ruin this thing, you could uh and you know, take off the epoxy or break through the epoxy on the outside of that and then uh have a look at the hybrid under there.

**Dave Jones:** But of course, I want my unit to work, so I'm not going to do that. I'm just going to put it back. And we've got ourselves a little metal can Burr-Brown package down in there and the obligatory trim pot.

**Dave Jones:** Now, there's one thing I don't particularly care for on this AC converter board is that it's only held down by that one screw there. I mean, the board does go through over here, but it's not like it's really held in place with that at all.

**Dave Jones:** So, there's only, you know, I wouldn't like to uh know about the uh vibrational modes set up during transporting that thing. I'm not impressed by one mount like that at all.

**Dave Jones:** So, there you have it. That's about all she wrote for the HP 3457A. Um Sorry, I just can't go into more detail on some of the chips. I could try and reverse engineer some of them, uh figure out what they are, but really, um it's it's tough when they brand the things with just generic HP part numbers.

**Dave Jones:** Real pain in the ass. Anyway, if you want to take a look at this thing, the uh service manual for this, which has the full schematics and everything else in it, will be linked in down below.

**Dave Jones:** And uh if you know what that voltage reference is in there from Linear Technology, please let us know. I'm sure there's a lot of people um into, you know, precision references on the forum and stuff like that and they would love to know that sort of thing.

**Dave Jones:** Maybe it's obvious. I don't know. I just haven't looked hard enough, but anyway, if you want to discuss it, jump on over to the EEVblog forum. That's the best place to do it.

**Dave Jones:** And if you like Teardown Tuesday, please give it a big thumbs up. Catch you next time. Mhm.
