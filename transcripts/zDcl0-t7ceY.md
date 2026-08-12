---
video_id: zDcl0-t7ceY
title: EEVblog #406 - Keithley 480 Picoammeter Teardown & Calibration
url: https://www.youtube.com/watch?v=zDcl0-t7ceY
source: youtube-asr
timestamps: {"0": 1, "1": 26, "2": 43, "3": 53, "4": 65, "5": 74, "6": 86, "7": 98, "8": 110, "9": 118, "10": 135, "11": 144, "12": 157, "13": 169, "14": 188, "15": 206, "16": 216, "17": 233, "18": 243, "19": 257, "20": 266, "21": 279, "22": 293, "23": 305, "24": 320, "25": 332, "26": 349, "27": 364, "28": 386, "29": 405, "30": 416, "31": 424, "32": 439, "33": 454, "34": 471, "35": 484, "36": 501, "37": 520, "38": 529, "39": 546, "40": 557, "41": 565, "42": 582, "43": 596, "44": 606, "45": 621, "46": 642, "47": 652, "48": 672, "49": 691, "50": 702, "51": 717, "52": 728, "53": 741, "54": 754, "55": 767, "56": 790, "57": 800, "58": 810, "59": 822, "60": 830, "61": 840, "62": 851, "63": 872, "64": 887, "65": 905, "66": 917, "67": 927, "68": 937, "69": 957, "70": 973, "71": 988, "72": 999, "73": 1014, "74": 1025, "75": 1041, "76": 1051, "77": 1061, "78": 1083, "79": 1095, "80": 1104, "81": 1118, "82": 1136, "83": 1157, "84": 1168, "85": 1180, "86": 1192, "87": 1204, "88": 1217, "89": 1235, "90": 1250, "91": 1260, "92": 1274, "93": 1290, "94": 1307, "95": 1324, "96": 1333, "97": 1344, "98": 1355, "99": 1372, "100": 1389, "101": 1398, "102": 1409, "103": 1430, "104": 1446, "105": 1465, "106": 1482, "107": 1497, "108": 1515, "109": 1530, "110": 1542, "111": 1552, "112": 1569, "113": 1582, "114": 1594, "115": 1609, "116": 1621, "117": 1636, "118": 1649, "119": 1664, "120": 1676, "121": 1691, "122": 1709, "123": 1725, "124": 1741, "125": 1751, "126": 1765, "127": 1779, "128": 1795, "129": 1805, "130": 1824, "131": 1835, "132": 1853, "133": 1871, "134": 1885, "135": 1897, "136": 1907, "137": 1937, "138": 1950, "139": 1975, "140": 1994, "141": 2015, "142": 2027, "143": 2045, "144": 2062, "145": 2073, "146": 2089, "147": 2106, "148": 2124, "149": 2139, "150": 2151, "151": 2161, "152": 2174, "153": 2182, "154": 2198, "155": 2216, "156": 2225, "157": 2244, "158": 2254, "159": 2270, "160": 2293, "161": 2307, "162": 2325, "163": 2337, "164": 2352, "165": 2361, "166": 2387, "167": 2397, "168": 2410, "169": 2428, "170": 2446, "171": 2456, "172": 2472, "173": 2490, "174": 2502, "175": 2515, "176": 2534, "177": 2549, "178": 2563, "179": 2578, "180": 2588, "181": 2613, "182": 2633, "183": 2644, "184": 2672, "185": 2684, "186": 2692, "187": 2704, "188": 2730, "189": 2740, "190": 2757, "191": 2770, "192": 2784, "193": 2798, "194": 2808, "195": 2820, "196": 2836, "197": 2850, "198": 2863, "199": 2873, "200": 2879, "201": 2891, "202": 2898, "203": 2913, "204": 2924}
---

**Dave Jones:** Hi, today is going to be vintage teardown, repair, troubleshooting, and calibration time. Check out what I've got. It's a vintage Keithley 480 pico ammeter. Fantastic instrument. It dates from about 1979, although the manual, the Keithley manual for this thing which you can download, which has all the full schematics and calibration and servicing information in it, was last printed in 1990.

**Dave Jones:** So, I think this thing had a pretty darn long life. And you know I'm into small currents and stuff like that. I've got a whole range of Keithley gear over here in including pico ammeter sources and stuff like that.

**Dave Jones:** So, I thought this is a nice little match for that. Sure, I've got my micro current to measure low currents, but this little Keithley unit nice score I thought.

**Dave Jones:** I got it for 65 bucks on eBay. And these are pretty rare to find in Australia. They are not so rare in the US, of course, and that's probably about the going price for these things.

**Dave Jones:** So, I thought I'd snap it up. Now, it was actually advertised as um you know, it it would fire up. It would you know, power up but untested. Fair enough.

**Dave Jones:** It's pretty hard to test this thing unless you've got the proper instruments to do it. So, yeah, it the it showed a picture of something on the display and I thought okay, at least powers up.

**Dave Jones:** Beauty. But I got it plug the thing in and what? Nothing. Nothing on the display. So, that's a bit of a bummer. But that means we can do a repair and troubleshooting video.

**Dave Jones:** So, let's give it a go. Once again, this one will be a real time repair. So, I've no idea if this thing is actually repairable. Should be. They're pretty simple inside.

**Dave Jones:** There's not much in them. So, I'd be surprised if I couldn't fix this thing. It could be a very simple thing. Could be a blown fuse. I don't know.

**Dave Jones:** We'll find out. Let's go. And here it is. It's very old school. It's got the old-fashioned gang push-button range switches here. And it's very simple. It's got a single BNC input.

**Dave Jones:** It's got a zero adjust pot down here on the front panel, which is really nice. And it has ranges from 1 milliamp full scale all the way down to 1 nanoamp full scale there.

**Dave Jones:** So with a 3 and 1/2 digit display there as you can see behind the red Perspex there. It can has a resolution of about 1 picoamp, which is really quite nice.

**Dave Jones:** Very handy unit for measuring low currents. And it is a feedback operational type. So the burden voltage on this thing is incredibly low. This one is spec'd to about 250 microvolts burden voltage.

**Dave Jones:** Now, it's got a tilting bail here. And if we have a look on the back, it's got selectable 240 and 110. It's already set to 240 volts. So, you know, presumably that's not the reason why it is blowing.

**Dave Jones:** It's got an Australian plug on it. And well, yeah. We'll find out. It's got a couple of banana jacks on the output here. And the good thing about this is that it's the output directly from that feedback operational amplifier without going through any additional circuitry.

**Dave Jones:** So, you can get the direct output from the feedback amp, which is really quite nice. There's no indication of date on this thing, but we do have a operating instructions on the back.

**Dave Jones:** I rather like that. That's quite neat. Why can't all units do this? And it tells you down here input burden voltage. There it is. Input burden burden voltage is 200 microvolts or less for an on-range reading when zero is properly adjusted.

**Dave Jones:** So, the burden voltage is incredibly low. Um its specs aren't too bad at all. Um half a percent to 8% plus a few three or four digits there. Not too bad at all.

**Dave Jones:** So, I rather like it. Um of course, on the 1 milliamp range, you're only going to get um maximum input voltage is uh 20 volts. And you'll note up the top here that it is designed to have a battery uh pack in it as well.

**Dave Jones:** I've no idea if this one um has got one. Based on the weight of it, it's very light. So, I'm assuming this one doesn't have the battery um option in it.

**Dave Jones:** So, uh yeah, trust me. I've powered this thing up and we get absolutely nothing on the display. So, it's troubleshooting time. First thing we're going to do is uh check the mains plug to see if like there's a mains fuse blown.

**Dave Jones:** I assume like there's a mains fuse inside. There's not one on the back panel. So, we'll just measure the resistance and bingo. Yes, um this is quite common um to when you're measuring primaries of transformers, you can see the multimeter skipping like that.

**Dave Jones:** That's the auto ranging being confused by the massive inductance in the transformer, but there you go. So, yep, we're measuring the primary of the transformer there and it looks like Oh, look.

**Dave Jones:** Look, the the display just popped up. Did you see that? I'm sure it did. Yeah, look. The display's popping on. How the hell is it doing that? There must be some stored charge in there.

**Dave Jones:** Couldn't couldn't be getting it from the multimeter. That's that's bizarre. I I didn't notice that before. No, it looks like it's it's not going to do that anymore. I hope you got that on camera there.

**Dave Jones:** But anyway, um the uh primary is um in intact and the primary is in there regardless of the uh power switch. So, this is effectively a soft uh power switch on this secondary of the transformer.

**Dave Jones:** You're not going to believe it. Man, I cannot cop a break. Look at this. It's working. I swear it wasn't working before. The thing has decided to work all of a sudden.

**Dave Jones:** Oh, man. Massively disappointed. I was hoping this would be a troubleshooting video. But maybe there is something Maybe there's an intermittent issue there. So, yeah. We may have to Well, we're definitely going to crack it open and have a look, but that's a That's a real bummer.

**Dave Jones:** And back in the glory days of Keithley, of course, before the evil Danaher group took them over, it was made in the good old United States of America. Sure it brings a tear to the eye of some Yanks out there, but yeah, you won't catch me singing the Star-Spangled Banner.

**Dave Jones:** So, we'll whip those out. Looks like they go into posts into the other side. Very old school for these instrument cases. Very typical and still used today for this style of instrument case.

**Dave Jones:** And one thing to note, you don't see this very often, is this right-angle cable clamp here. Mains input cable clamp on the bottom of the case instead of the back panel.

**Dave Jones:** I have no idea why they've done that. That's weird, but anyway, let's put it up this way. Screws are out. And let's crack it open. Tada! There it is.

**Dave Jones:** Piece of cake. Lovely. And that is wonderfully, wonderfully old school. I love it. Check out all the square traces on the PCB there. Beautiful. Look at this crystal. Look at the size of that sucker.

**Dave Jones:** That's We'll go in and have a look at that. That looks It's a 100 kHz. 100 kHz crystal. Look at the size of it. Um I'll see if we can get a date code off one of these uh chips and see uh see what the uh build date of this thing is.

**Dave Jones:** There's no data on there. There's a cal inspection sticker. All of the um all of the stuff is under the shielded can, of course. Um this is all just the display and power supply stuff outside here, but all the um the feedback amplifier and everything's inside here.

**Dave Jones:** One interesting thing to note is that the BNC input here Check check this out. They've got a shield there. Right? They've got a shield over the BNC, and then they've got a little what looks like an unshielded Um it's not quite a coax.

**Dave Jones:** It looks like just a single core wire uh with some uh tubing on it coming out there and going down into the can down under there. So, that's I you know, I don't know why they've bothered to uh do that, why they've taken that outside of the can, and all that sort of stuff.

**Dave Jones:** Weird. Well, certainly no shortage of uh test points here. Here's our power supply. We've got plus minus 15 there, plus 5 V test points. We can uh check those out.

**Dave Jones:** And um yeah, we've just got some axial uh filter capacitors. Our transformer is up here. We've got an internal fuse, which isn't blown, of course, because it's working. And we've got a battery and line switch here, which allows us to select the battery module, which presumably plugs into this this connector here.

**Dave Jones:** So, we don't have the battery module on there. And looks like we've got a bridge rectifier there, two more uh rectifier diodes there. So, they might be getting another tap on the transformer.

**Dave Jones:** You can see multiple uh taps on the secondary side of the transformer there. Trim pot, there's another couple of uh trim pots down inside the uh can down here.

**Dave Jones:** So, I'm not exactly uh sure what they're designed to do. I have to read the calibration information for that. And we have some date codes here, folks. We've got a uh 4000 series of 4011, classic 91 uh 42nd week, 1991.

**Dave Jones:** So, and this one's uh directly soldered in. So, that um you know, it was at least manufactured uh 91-92. So, it's a relatively uh recent unit, probably as recent as you can get these things, I would guess.

**Dave Jones:** And uh this um ICL chip over here is a 93 one, but it's in a socket. I'm not sure um why we've got a socket there. We've got another 93 one down here.

**Dave Jones:** So, I certainly haven't been replaced, and those IC sockets were uh factory fitted. And we've got uh curiously a uh blank socket down here. So, I don't know what that one's for, but uh there you go.

**Dave Jones:** So, definitely um early '90s unit. Beautiful. And it's a rev revision F PCB. And check out the shielding spring that they've got here. Um the curious thing about that um is well, it's designed to mate to something, but inside the lid, there's no um you know, shielding on the upper part of the case for it to mate to.

**Dave Jones:** So, I don't know. Maybe uh something to do with the charger board, but I can't see it. So, don't know what's going on there. Now, let's take a look at the data sheet for these two puppies here.

**Dave Jones:** We've got an ICL 71C03 and an ICL8052. And as it turns out, they're actually a pair of They're a matched pair of devices. And what they are is a precision 4 and 1/2 digit AD converter and display driver.

**Dave Jones:** It doesn't tell you that, but that's what it is, as we'll see. And apparently, it was pretty darn state-of-the-art. It's designed 4 and 1/2 digit accuracy um uh 2 200 mV to 2 V uh full scale capability, auto zero, auto polarity, as you'd expect of a dual slope uh conversion uh unit like this.

**Dave Jones:** Typically, less than two microvolts peak-to-peak noise. Um, you know, accuracy guaranteed plus minus one count over the entire full scale range, guaranteed zero reading. So, a pretty darn nice chip for its day.

**Dave Jones:** I like it. Um, use of these chips pairs eliminates clock feed-through problems and avoids critical board layout. Woohoo! Beautiful stuff. And it's also, uh, does a three and a half digit mode, which is what, um, it's used here.

**Dave Jones:** And you can get up 30 readings per second to do that. And I love here how they're tooting their horn, almost ideal differential linearity and time proven dual slope conversion.

**Dave Jones:** Ah, love it. It's got a medium quality reference in it, not a high quality reference. It's a medium quality reference, 40 ppm. Yeah, not that, uh, terrific, but, um, more than good enough for this.

**Dave Jones:** Five pico amp, uh, input current down there. And it's a dual chip solution. And they've got them in the one data sheet, which is, um, quite unusual. Using Usually they'll have, um, separate data sheets for each one.

**Dave Jones:** But, and here's the block diagram for the two chip solution. And you can see the, um, 71C03 with the, uh, red outline here, like this. And the, um, 8052 is that one there.

**Dave Jones:** So, the 8052 just contains a few, uh, buffers and the inner integration amp. And you need the, um, external integration capacitor and, uh, various external components there, internal, uh, voltage reference, and the main, um, ICL71C03, uh, contains the, uh, switching and the zero crossing detector and all the multiplexer multiplexing and latching and counting solution for that.

**Dave Jones:** And you'll notice that it's not a seven segment display, um, output here. It's a four digit, uh, BCD, um, output. So, you need a BCD to seven segment, uh, decoder.

**Dave Jones:** So, we should find that chip elsewhere in the design, probably on the front panel there. And, uh, as you can see, it can drive a 4 and 1/2 digit display, but in this case, we're only driving 3 and 1/2 digits.

**Dave Jones:** And there's a pin to uh strap it to 4 and 1/2 or 3 and 1/2 digit mode there. And, as you can see, there's not much to it, but it's a it was a very precision device for its day.

**Dave Jones:** And if we check out the bottom of the board here, here's this uh shielding tab again. It's all the one piece of bent metal. So, we don't know what it's going to on the top there.

**Dave Jones:** Doesn't appear to go into anything, but the bottom here, of course, down to a big shielding plate on the bottom of the case there. And uh yeah, not much doing there.

**Dave Jones:** Um check out the big star ground point up here. Look at that. Nice. Kind of looks like almost a flying spaghetti monster. I see a vision. Look at that.

**Dave Jones:** Beautiful. Um I love all the square traces and everything like that. It looks like it hasn't been reworked, really. It looks like it is um all factory soldered. Down here, there's a quite a bit of flux residue on the hand soldering for the transformer, but that that's not uncommon even these days.

**Dave Jones:** We've got some uh guard traces around there, little guard rings around these um and they're those uh test points that we saw before through the main cover. So, we'll whip that uh metal cover off later and we'll take a look.

**Dave Jones:** And on the front panel there, there's our BCD to seven-segment decoder, a um CD4511, absolute classic. Uh over here, we have a National Semiconductor DS75492. And that is a um uh hex uh MOS display driver.

**Dave Jones:** So, that's just uh driving um the heavy current on the digits. And there's that crystal, 100.000 kHz. I love it. I haven't seen one that big in a long time.

**Dave Jones:** So, as I said, it's a a real bummer that this thing's working. I was hoping to do a troubleshooting thing on this, but anyway, let's give it a go.

**Dave Jones:** Let's measure these rails. I don't know where a ground is, but presumably, I don't know, the can in the can here or the can of the crystal. Let's give it a go.

**Dave Jones:** So, our 5-V rail, there it is. 5 5.02, not a problem. -15, yep. +15, not a problem. There are our three power rails. So, this thing's just hunky-dory. I have no idea why it wasn't working before.

**Dave Jones:** Um it's really weird. Very strange. And there's that rather unusual input can. I just took the shield off there and it just, you know, they've gone to a lot of trouble to actually design that so it wedges in there and like just over the BNC.

**Dave Jones:** And there it is. There's a single solid core cable going out there over into the shielded can. Weird. Why they just didn't run that on the PCB with a ground trace over it, I've got uh no idea.

**Dave Jones:** But, but, you know, look, they've done the zeros here. Like the There's a zero adjust pot and they've just got those running right over there. Don't know why they didn't do that with the uh with that.

**Dave Jones:** Why they went to all that trouble. Hm. Weird. Like, you know, like you would have ordinarily just designed this input can, designed the circuitry, laid out the board so the input can like extended over this input BNC and the zero pot here.

**Dave Jones:** That's how I would have designed it. Now, as you may have seen before, it looks like we're not getting a zero reading on some of these ranges. I mean, that's the 1-nA range there.

**Dave Jones:** So, we're getting like 5 pA there with no input. And others is showing is showing zero, not a problem, but we're getting five on that as well. So, it looks like we're getting five on those alternate ranges there, and we'll probably get five on this one based on that.

**Dave Jones:** No. There we go. So, that one, that one, and that range, we're getting five. So, um and if we do the zero adjust button here, let's put that in.

**Dave Jones:** Zero adjust. Let's tweak that down, shall we? Let's go down to the lowest range. I haven't read the manual, but it's okay. I've got my tongue at the right angle.

**Dave Jones:** And give that a little tweak. And we're down to zero there. And let's try that again. There we go. Nice. Okay. Everything's fine. I say we just get my um Keithley current source out and uh whack some current into this thing and see if it's spot-on.

**Dave Jones:** Hopefully, it won't be cuz then we'll have to go through the calibration procedure. All right. What I've got is my uh Keithley 261 pico amp current source. So, it's a perfect match for this thing.

**Dave Jones:** I've also got the uh 225 current source. So, uh if we need to go to higher currents for the milliamp ranges, this can't uh do that. This starts from uh 10 to the minus five.

**Dave Jones:** So, it starts from 10 microamps um full scale down to uh you know, femtoamps. It can go Look, this this knob is dicky. It's completely dodgy. Uh there we go.

**Dave Jones:** No, ruined. Uh got to really tighten, maybe flatten the shaft out on this thing, and do that. But, uh anyway, trust me, this thing does actually go down to a minimum of 10 to the power of minus 12, i.e., 10 picoamps full scale.

**Dave Jones:** And you can adjust that because this shows the uh where the decimal point is, then we're talking about um you know, 10 femtoamps resolution on this thing. It's really quite good and more than good enough for um the testing the range of this thing, which is one uh nano um amp full scale.

**Dave Jones:** Anyway, what I've got this thing on is the 10 microamp range, so it's 10.00 microamps here, and I've got it on the uh uh 10 microamp range here, and there it is, 9.99.

**Dave Jones:** You saw it before it was 10.00, so you know, something's drifted somewhere a little bit, but it's basically spot on, and we should be able to tweak that. There we go, and look at that.

**Dave Jones:** Just dial it in. We're only one least significant digit out between these two units. Absolutely incredible. We can dial that up to exactly 10. There we go, we can tweak it.

**Dave Jones:** It's hard to read that uh uh LED display, I think, at least on the screen here. So, I might have to up the current on that thing. I might just change the resistor network there or something like that, just to make it a bit brighter, maybe.

**Dave Jones:** It's a bit washed out, but yeah, look at that. I can just dial in that digit there. Fantastic. I love it. So, that's bloody spot on, unfortunately. And you can see it blinking over range there.

**Dave Jones:** And I just noticed something that I shouldn't be doing. There's the mains cord there, right next to my um lead. That's probably not the best idea. So, let's get that completely away from there.

**Dave Jones:** And so what we're going to do now is we'll just try out the negative uh polarity. I can just swap the leads, of course, or I can just use my negative switch here, and bang, that's, you know, we're only talking it's changed by two least significant digits.

**Dave Jones:** So, it's basically spot on plus minus one. I love it. Um and of course we go down, we get a flashing over range there. And uh so that is working a treat.

**Dave Jones:** So, let's change this uh range down, and if we go up a range, there we go, 9.9, not a problem. We should get nine. Yep. Or 10 I was expecting there, so Ah, man, this thing's spot on.

**Dave Jones:** Not going to do any troubleshooting, not going to do any repair. Looks like we're not going to do any calibration, either. Bummer. And if we go up to the 100 microamp range, yeah, that's as basically as high as we can go on this um uh 261 current source.

**Dave Jones:** But look at that. I mean, that's we're talking. Look at that. That's just ridiculous. Down to the 1 microamp range, we're absolutely bang on. So, let's keep going. Excuse the crude adjustment here.

**Dave Jones:** What are we on now? We're on the 100 nanoamp range. Bang on. Absolutely bang on. Look uh that's just that's just filthy. That really is. Unbelievable. Ah. It's obscene.

**Dave Jones:** There we go. And we're now down on the 10 nanoamp range. If you remember, there's all the ranges there. There they are. 1 1 nanoamp through to 1 milliamp.

**Dave Jones:** Haven't tested the 1 milliamp one yet. I'll have to get my other current source out to do that. But there you go, we're bang on. That's 10 nanoamp range.

**Dave Jones:** Not a problem. And there we go. We're down to our 1 nanoamp and we're picking up some noise here. You can see it's jumping around. I mean, what I've got here is I've just got a shielded BNC.

**Dave Jones:** You can see it. You can see it changing as I play around with that. I mean, we're right down in the noise here. Um if you want to do good low current measurements, Keithley have the I think it's called the low current measurement handbook or low, you know, something like that.

**Dave Jones:** I'll link it in here and it is one of the industry standard reads on low current measurement like this. I mean, you know, I've done a little bit of twist in the wire there just to keep it low, but really, you know, I mean, this probably isn't going to cut it, as you can see.

**Dave Jones:** And if we go back up a range to 10 nanoamps there, you can see that it's basically spot-on. And then if I start to handle that, you can see it starting to kick in there.

**Dave Jones:** So, really, you're getting triboelectric effects in the cable and all sorts of stuff there. So, really, you don't want to touch it. Hands off, keep it as short. There's a whole art to doing this.

**Dave Jones:** Keep it, you know, double-shielded boxes and all sorts of weird and wonderful techniques, which will no doubt be in the Keithley measurement handbook. So, check that out, but if we go right down to the lowest range there, then we adjust that, it is it is bang on if I don't touch that cable at all.

**Dave Jones:** If I get anywhere near that cable, bang, it's just going all around the place. But this thing seems to be in perfect calibration. It's absolutely bang on. I'd be a fool to even attempt to touch this thing.

**Dave Jones:** Let's go to switch it to negative mode, so we're getting minus one nanoamp. Ah, near enough. I'm not going to complain about that. I'd really have to probe it all properly and spend hours around to try and get that right, but there you go, positive and negative.

**Dave Jones:** And if we switch up a range there, it's bang on one negative and positive. Brilliant. Bang on one nanoamp. Do you believe it? Look at that. I can just dial that in, and I can probably dial this one in if I don't get my hands near it.

**Dave Jones:** Look at that. Great stuff. And I have to test out the milliamp range. So, I've got my other Keithley current source here, which is the 225, which covers a larger range and doesn't go as low.

**Dave Jones:** So, it goes all the way from 99.9 milliamps here, so 100 milliamps basically, all the way down to 99.9 nanoamps. So, this one has a resolution of 100 picoamps, so not nearly as low as the current source we had before.

**Dave Jones:** So, with these two instruments, I can cover practically and with my other power supplies, I can cover practically everything from 10 femtoamps all the way up to, you know, amps.

**Dave Jones:** Crazy. Many, many orders of magnitude. And with this one, you can adjust the maximum output voltage anywhere from 10 volts right up to 100 volts. And also, it's got the it's got the positive and negative switch as well.

**Dave Jones:** And it's also got an output filter. So, let's hook this thing up. All right, so I've got this set to 1 milliamp here, 1.00 milliamp. We've obviously got an extra digit over here.

**Dave Jones:** And look at this. We are bang on, folks. Absolutely bang on. I love it. So, we can dial in. Look at that. That's pornographic, really. We can just dial in those digits and it matches precisely.

**Dave Jones:** Fantastic. So, if we switch that down to microamp range, once again, we're bang on. So, these two units match. I mean, I obviously keep them in cal to calibrate my microcurrents.

**Dave Jones:** There we go, a couple of less significant digits out there. Whoop-de-doo, folks. And of course, um this thing and we're not even near full scale on this thing where the accuracy is the is is the best on this thing.

**Dave Jones:** We're right down at 1.00. So, let's go down. There we go. Ah. Ah. Couple of less significant digits out there. Ah, what a bummer, huh? So, 99.9, let's wind the wick up.

**Dave Jones:** There we go, 99.9. Uh that's obscene. And let's just try the negative there. Switch it around. Huh. And we almost forgot to have a look under the metal can there.

**Dave Jones:** But look at this beautiful uh point-to-point hand soldering with the uh turrets there completely surrounded by the ground plane on top there. Beautiful. So, they've just gone completely point-to-point.

**Dave Jones:** We've got uh metal cans here. Beautiful. But by far the most interesting thing in this is look how they're doing the range switching here. I mean, I I don't know if these um switches are actually connected up to anything.

**Dave Jones:** Looks like there are some traces going down there. But look at that. These things push on these gold uh leaf contacts here, which then push on that gold pin like that.

**Dave Jones:** It's just beautiful. I They've gone to a lot of effort there to switch to ensure that they um switch very low noise. They're just switching part of the circuit.

**Dave Jones:** There it's interesting though that they don't do it to the lowest two ranges down here. There's none of that switching at all on those lowest two ranges where you think it would be um absolutely critical to uh do that thing.

**Dave Jones:** So, I have to look at the uh schematic for that. But that is that that is just lovely. They've deemed that they have to go to that effort to get the uh to get the signal integrity, the low noise on this thing instead of using the you know, the crummy switches inside these gang switches.

**Dave Jones:** I mean, no matter how good you manufacture these switches, they're probably going to be pretty crusty. So, they've gone for a beautiful you know, um very probably a very heavily plated uh gold leaf um contact there onto another heavily plated gold pin.

**Dave Jones:** Beautiful. And let's just go for the money shot there. Ah, look at that. Ah, could play with that all day. And if we go and have a look at our schematic here, I'll link it in down below.

**Dave Jones:** And by the way, if you want to check out the manual for this thing which has the full schematic and theory of operation and all sorts of stuff, it'll make a great bedtime reading, I'm sure.

**Dave Jones:** But here we go. We've got some switching down here and that's the decimal point switching. So that's all the digital stuff. So that's what those crummy gang switches will be used for is just the digital part of the decimal point switching, of course.

**Dave Jones:** But all of that beautiful low noise gold leaf contact there is all part of the feedback amplifier. And here's the feedback amplifier here. There's the zero adjust pot there.

**Dave Jones:** It's By the way, you would do this with a, you know, a real top spiker fit input op-amp these days, but they actually used a JFET input front end with matched JFETs.

**Dave Jones:** And incidentally, these two resistors, they've got an asterisk next to them. They're if you look at the notes, they're actually selected at the factory to match the transistors there.

**Dave Jones:** Here you go. You can see the switch contacts in the feedback path there for the feedback resistors. There they are. There and there your gold leaf contacts and they have to be incredibly reliable, incredibly low noise contacts when you're talking about an instrument of this caliber.

**Dave Jones:** And if you notice before we had four of those gold spring contacts and there's the four contacts and they've also got some of the other range switches here which is switching some more non-critical stuff.

**Dave Jones:** And you can see that the 10 nanoamp range and the 100 nano amp range there isn't actually um switched at all as we noticed um inside the unit. So, we bring the unit back over here again, you'll notice that the There you go.

**Dave Jones:** We've got our four spring leaf contacts and the These uh and the two lowest ranges aren't switched in there at all with those gold leaf contacts because um they are fixed across the feedback path and then the others are put in parallel.

**Dave Jones:** So, as you can see, there's not much to these things. It literally is just a feedback amplifier. And uh if you used a modern um op-amp in there, I mean, this thing was designed in, you know, uh the late '70s.

**Dave Jones:** Uh they just weren't around then, so they had to, you know, hand match these JFET inputs, but you can just get a um FET input um op-amp, a really uh low bias current, you know, precision op-amp these days just to do that.

**Dave Jones:** Put a feedback resistor in there, some um low-pass uh filtering caps on there, and Bob's your uncle. And there's the output um terminals and the output banana jacks on the back panel.

**Dave Jones:** So, you can access directly the output of the feedback amplifier. And that um you know, I won't go into theory of feedback uh amps here. I may have even done it uh before, but um basically, it converts uh current into voltage on the output with effectively only the uh difference between the offset voltage between the inputs to the op-amp um which is your burden voltage on the

**Dave Jones:** input. So, this is how you can get incredibly low burden voltage, unlike my microcurrent one which just uses a traditional shunt resistor. This one is a feedback amplifier which works differently, so you can get even lower burden voltage than my microcurrent.

**Dave Jones:** And by the way, just as an aside, if you're playing around with uh very uh you know uh low current precision circuits like this just be careful how you handle this or try to avoid handling them if at all possible because your hands if you you know your hands aren't clean or even if you've just washed them they can still have oils and stuff which can leave

**Dave Jones:** residues on critical parts of the circuit cuz we're talking about you know 100 megaohm resistors here that one's 99 meg and you know if you start getting in there and you get all sorts of dirt and residue and you know all sorts of other gunk in there it can you know upset the calibration of this thing so just be careful.

**Dave Jones:** So of course it turns out I was wrong about these being access points it seemed a bit weird that they were very deep down in there they're just little plastic holders to keep those posts in place so that that those contact switches don't bend and just for kicks let's make sure the burden voltage is less than the 200 microvolts claim.

**Dave Jones:** So what I've got is I'm feeding in 1 milliamp here and I've got a banana to BNC jack here so that we can get in here with our meter and probe it.

**Dave Jones:** Now I'm going to use my Agilent U1272A cuz it's got the 50 millivolt range so it can the resolution can go all the way down to 1 microvolt. Fantastic and as you can see it's pretty darn close to zero there and let's get in there and probe this sucker.

**Dave Jones:** Let me try and apply some pressure you got to be careful here but yeah we're definitely under the 200 microvolts there we're only about 110 microvolts. Love it. And just to double check on a lower range there I've got the 100 nanoamp range there and we're only about 80 odd microvolts.

**Dave Jones:** And because I'm sure there will be people who will ask how does it compare to my micro current here? Well here it is I've got 100 microamps in there, and we're getting 99.96 microamps out of this sucker.

**Dave Jones:** This one obviously has and allows us to get an extra digit of resolution there. And there it is, um, measuring in the order of 100 nanoamps there. And it might be, uh, two least significant digits out on here, but I'm not actually feeding in 100.

**Dave Jones:** I'm feeding in, uh, 99.9 microamps. So, um, you know, in theory, if everything's absolutely bang on perfect, this should be 99.9 nanoamps there, or 99.9 millivolts, cuz it's 1 millivolt per nanoamp range on my microcurrent.

**Dave Jones:** So, there you go. Everything's well within spec. And if you don't have a calibrated current source like I do, you can, uh, easily test this, um, in fact, this is probably the recommended, uh, method to, um, actually, uh, calibrate these because, uh, you can easily get, um, high precision voltage and resistance standards.

**Dave Jones:** So, I've got my, um, MV106, uh, DC voltage standard you've seen here before. Way overkill, I mean, the Keithley 480, uh, picoammeter, you know, is only rated to like 0.5% and this sucker is, uh, a couple orders of magnitude better than that.

**Dave Jones:** So, um, I've also got my resistance standard here, which you've, um, seen before, which is basically just a, uh, 50 ppm resistor in a box. I've got a 10K one and a 1K one.

**Dave Jones:** Um, usually you would, uh, use a much higher, uh, value than this for, um, testing the lower current ranges, but this is the best, um, this is the best resistor I've got.

**Dave Jones:** I've got larger resistance, uh, values, but they're, you know, uh, a few percent or something like that. They're certainly not precision. So, we're talking about, you know, point double 05% um, accurate resistor in a box here.

**Dave Jones:** You can buy those for about 20 bucks or, uh, something like that from Digi-Key. Yes, you can pay 20 bucks for one resistor, but it's a pretty darn schmick one.

**Dave Jones:** So, um, I've got it hooked up here. We're on the 10 V range, but I'm outputting 1 V here, 1 V on 10 K, we're going to get 100 Oh, there it is, 100 microamps.

**Dave Jones:** We are absolutely bang on to the least significant digit. Of course, if I take that up to 10 V on the uh voltage standard here. Oh, one least significant digit out at 10 milliamps.

**Dave Jones:** There you go. And of course, if you you know, you've got to be careful what you're doing here. You've got to take into account the burden voltage. We've already measured that, 250 microvolts.

**Dave Jones:** So, it's insignificant here. It's actually 100 microvolts. The spec is 200 microvolts. So, you know, it's down in the noise here. Now, you might think that we're simply able to reduce the voltage here and um measure the lower current ranges, but that's not really the case.

**Dave Jones:** You can see it's um slightly out here. So, I've got 10 millivolts there over my 10 K, which is going to be 1 microamp there. And you can see we're out.

**Dave Jones:** But, I know it's not out. It's because the offset voltage now becomes a very significant proportion of the burden offset voltage in this thing becomes a very significant proportion of our of our you know, of our calibration setup here.

**Dave Jones:** So, that's why the manual for this thing will recommend minimum input impedances for this thing for for these various ranges. But, what that essentially translates to is not necessarily a minimum input source impedance, but a minimum input voltage essentially so that the burden voltage of this thing doesn't matter.

**Dave Jones:** Now, look, if we go even lower, like well, we'll go up one there. So, we'll go at one A. See, it gets closer there as we go up. So, we're 10 microamps there, but we'll get more further out as we go down.

**Dave Jones:** So, let's drop that down even further, zero and one there. Now, we're even we're way out, okay? We're just you know, we're we're just completely and utterly gone. If I put that to one one millivolt, there we go.

**Dave Jones:** We're completely out. And if we take a look at this Dave CAD drawing here, we can see exactly what's going on here. We've got our MV106 voltage standard generating our test voltage here.

**Dave Jones:** We've got our 10K series resistor going into our feedback amplifier here. Now, at the moment, let's just ignore the feedback resistance here and we've got that measured VOS or offset or burden voltage there of around 100 microvolts.

**Dave Jones:** Let's just you know, round it to 100 microvolts. It's going to change per range and all that sort of stuff, but let's just take that as a value. So, let's have the one volt that we had before.

**Dave Jones:** One volt minus 100 microvolts divided by 10K because that's what's flowing into this this feedback amplifier here gives us 99.99 microamps and we were measuring bang on. So, you know, the error is in the VOS error here is insignificant in this case where we had the one volt and we were generating 100 microamps.

**Dave Jones:** It's pretty darn close. But, then if we drop our test voltage here from the MV106 to 10 millivolts, then we can see our 100 microvolt offset voltage becomes very significant.

**Dave Jones:** You do the math here and it's 990 microamps. So, we'll actually measure that and we should get roughly that figure. And then if we drop it even further, we're going to ridiculously low voltage here.

**Dave Jones:** One millivolt minus 100 microvolts, of course it's going to have a very a um error or a 10% error there of 90 microamps. So, let's actually measure that. So, let's go up here and we've got it set to 1 V here and we're getting our 100 microamps as we saw before, spot-on.

**Dave Jones:** Because um in theory, we should actually expect 99.99 microamps, but because um that value is one uh digit um better than the resolution we've got here, eh it's you know, it's insignificant, especially when you consider the accuracy of this thing.

**Dave Jones:** So, or the intended accuracy of this thing. So, it's insignificant, but if we wind that down to 10 mV here, I'm on the 100 mV range, we're generating 10 mV.

**Dave Jones:** You'll notice that we were expecting What were we expecting before? We were expecting 990 microamps and there you go. We're getting reasonably close to that and but our error is going to get um significantly larger, as you'll see in a second.

**Dave Jones:** Now, and if we switch down to our 10 mV range, we'll generate 1 mV. There you go. We're getting that 90 microamps, which we expect, but uh-huh, well, you know, reasonably close to it, within a ballpark, but let's switch down this range and see what happens.

**Dave Jones:** 100 nA. Look at this. We're measuring 20 like that. So, our error is very hugely significant. The you know, it's it's almost now pointless. It it just reads gibberish now.

**Dave Jones:** Why is it doing that? And here's the answer. I've added an additional Dave CAD drawing here with a formula, which now becomes very, very significant based on our source resistance RS.

**Dave Jones:** So, I basically relabeled the 10k resistor RS. That's our source resistance. Um our feedback resistor here is RFB for feedback and I've redrawn the VOS as a voltage source here, which is a better which is a more common representation of it, but it's the same thing.

**Dave Jones:** It's that 100 microvolts, but that 100 microvolts we measured way before is not a fixed value. It's actually multiplied by this term here which is RFB plus RS divided by RS.

**Dave Jones:** So, let's take uh the example of the 100 microamp range. That's got a 10k feedback resistor. What happens if you plug 10k and 10k into this formula here? This term here becomes a value of two.

**Dave Jones:** So, the VOS at 100 microvolts gets multiplied by two. And then, if you change the range again, let's say you jump to the 100 nanoamp range, then RFB, the feedback resistor, is actually a 1 meg resistor.

**Dave Jones:** And you can look up these values on the schematic for yourself, and I recommend you go do that. Um have the schematic here as you follow along, in fact.

**Dave Jones:** So, then the term becomes huge, and that VOS just goes completely out the window. So, that's why we're reading absolute gibberish as we go as we switch down those ranges cuz as we switch down the ranges to, you know, 100 nanoamps, 10 nanoamps, 1 nanoamp, this RFB gets much, much larger, and this term becomes much, much larger, and VOS just goes out the window, and we're only got a 1

**Dave Jones:** millivolt source here, and VOS is way bigger than that at well, in theory, and you just read absolute gibberish. It just doesn't work. That's why if you read the manual for this thing, it will specify a minimum RS or source resistance value here based on whatever range it is you're measuring.

**Dave Jones:** Now, the manual actually says for a 10k source resistance here, which is what we're using ignoring the source resistance of the MV106 for a minute, then the lowest range we can use is the 10 microamp range.

**Dave Jones:** If we go any lower than that, it just, you know, the error term becomes too significant. And if you really want to go into it, and you can read the manual for this, there's an additional voltage source in here, which is the VN, which is the noise source, which is going to depend on your series capacitance as well, as well as your feedback capacitance in here like this, and all

**Dave Jones:** sorts of stuff like that. And it starts to become very, very complicated with lots of traps for young players if you're measuring very low values of current like this.

**Dave Jones:** There's a real art to measuring this sort of stuff and knowing where all your error terms and things like that are. So, I won't go into details on that.

**Dave Jones:** It's in the Some of it's in the Some of it's in the manual for this thing if you want to read it. It's very interesting. And of course, our simple little dumb ass, you know, like I've got just wires just hanging loose over here.

**Dave Jones:** It's, you know, it's pretty pathetic, actually. So, you know, this isn't the way to do it. As I said before, you've really got to um uh you know, do like have dual shielded boxes and shielded leads and, you know, all sorts of, you know, great quality contacts and stuff like that if you're really going down to very low levels of current like in the order of under 100 nA.

**Dave Jones:** Once you get under, you know, that sort of microamp figures sort of those sort of things start becoming quite significant, and you've really got to know what you're doing.

**Dave Jones:** So, maybe I'll do another video on that, you know, all that sort of stuff of really accurately measuring low value resistances. But, yeah, you've got to have precision high value resistors in, you know, double shielded boxes, and they've got to be isolated with minimum amounts of capacitance and all sorts of stuff.

**Dave Jones:** Really get tricky. Quite a fascinating topic, though. And here's what I'm talking about in terms of the double shielded test fixture here. Now, you can see that the outer case here is actually connected to the earth.

**Dave Jones:** That's you can see the earth symbol there. It's connected to the earth of the DC voltage calibrator over here. And of course we've got our low and high and our sense lines.

**Dave Jones:** And internal you you might also shield this circuitry internally from the shield which is non-mains reference to the Keithley 480 over here. So you'd have the internal precision resistors.

**Dave Jones:** They recommend 10K, 10 meg, and 100 meg. And based on those three and the individual test voltage over here, you can generate all the required currents. But that's what you would do.

**Dave Jones:** You would put this inside an earth shielded box over here. And you'll notice that it's only connected to mains earth over here because the Keithley is not mains earth referenced on the input.

**Dave Jones:** And then the internal ground, you might shield that internally as well if you're going really low. Probably not need double shielding. Probably not needed in this particular case. But if you had another instrument that was going even lower than this one, then that would be important.

**Dave Jones:** So there you have it. I hope you enjoyed that little teardown and little look at calibration checking this very nice Keithley 480 picoammeter. And if you can pick up one of these puppies, I highly recommend it.

**Dave Jones:** You know, I wouldn't pay more than you know, 100 bucks for one for sure. But they're a really nice bit of kit for measuring low currents. And it'll be a nice addition to the lab here I think.

**Dave Jones:** And it was bang on. I can't believe it. So yeah, sorry about that. I still don't know what was initially wrong with this thing cuz it definitely was not working when I first plugged it in.

**Dave Jones:** It wasn't working at home when I first got it. And then I brought it to the lab here, and it didn't work either. But all of a sudden, bang.

**Dave Jones:** So, I don't know, maybe there was a dicky contact in the switch or something like that. And after a couple of goes, it just self-cleaned or something like that.

**Dave Jones:** That is the only thing I can think of. So, yeah, sorry about that. I was hoping to get a troubleshooting and repair video, and ah, Murphy gets you every time.

**Dave Jones:** You hope for a fire, and you don't bloody well get one. Either in the fire of the circuit itself, the unit itself, or the calibration. I was hoping maybe we could, you know, tweak a few more pots and actually go through the calibration procedure, but it's bang on.

**Dave Jones:** So, certainly not going to touch it. So, anyway, if you want to discuss it, jump on over to the EVblog forum. And if you like it, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
