---
video_id: 5ai9PLpbGIE
title: EEVblog #320 - Mailbag Monday
url: https://www.youtube.com/watch?v=5ai9PLpbGIE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 22, "2": 38, "3": 63, "4": 83, "5": 93, "6": 108, "7": 128, "8": 143, "9": 163, "10": 188, "11": 208, "12": 228, "13": 243, "14": 263, "15": 283, "16": 308, "17": 323, "18": 343, "19": 363, "20": 378, "21": 398, "22": 418, "23": 443, "24": 463, "25": 483, "26": 508, "27": 528, "28": 543, "29": 558, "30": 583, "31": 603, "32": 618, "33": 638, "34": 663, "35": 678, "36": 703, "37": 723, "38": 743, "39": 763, "40": 783, "41": 803, "42": 828, "43": 843, "44": 863, "45": 878, "46": 898, "47": 923, "48": 943, "49": 963, "50": 988, "51": 1003, "52": 1028, "53": 1048, "54": 1073, "55": 1088, "56": 1108, "57": 1128, "58": 1148, "59": 1168, "60": 1188, "61": 1208, "62": 1228}
---

**Dave Jones:** Hi, welcome to the ever-popular mailbag segment, where I open my mail live, in quote marks, here on the blog. And if you want to send me stuff, send it to, here it is, Dave Jones, ThatCrazyAussieBloke, P.O. Box 7949, Balcombe Hills, BC, NSW 2153, Australia.

**Dave Jones:** Not Austria. Alright, I've got two mailbag items today. In fact, I've got more than that, but we'll, you know, I don't want to hog it. And this thing looks like it contains three items. Exciting. So, yeah, we'll just limit it to two today.

**Dave Jones:** Let's give it a go. Let's open this one first. It is from Ray's Hobby Shop. There it is. Ray's Hobby Shop. I assume it's Rayshobbyshop.com. I'm not quite sure. From the US, Amherst, MA, which I believe is Massachusetts, even I know that. And I'm from Australia.

**Dave Jones:** Pretty sure I got it right. And we have one printed circuit board. Thank you very much, Ray. I have no idea, he didn't clue me up on this, so let's open it up and have a look. Ta-da! And we have a partially assembled board, and a note.

**Dave Jones:** Let's give it a go. Hi Dave, I was watching your video on the USB power supply, thought I'd send you this circuit board. He's called the AA Saver. Nice. It's a voltage booster that takes two AA batteries, outputs 5 volts or 3.3 volts selectable.

**Dave Jones:** Pin headers match the spacing of a standard breadboard. Oh, I like these. So that you can plug it into your breadboard for circuit experiments. Apple current is up to 350 milliamps with fresh batteries. I know it's not an idea, not a new idea, but I've designed it to add dual functions.

**Dave Jones:** Ball can also hold two LEDs, you can use it as a LED flashlight, because it can work with quite low voltages. Awesome! I assume like down to maybe, you know, 0.8 or single cell or something like that. So yeah, as he says, you can use dead cells

**Dave Jones:** in these things typically. So let's have a look. AA Saver instructions of use. Instructions, ah, okay, it's got metal battery clips up there, and a couple of LEDs. Let's have a look. Nice photos, I like it. Use it doubles as a flashlight. Neat.

**Dave Jones:** And you can see the two pin headers there, which are standard breadboard spacing. And it mounts on a breadboard like that, which is very, very handy. So no schematic, unfortunately. So we don't actually know what's being used in here, but let's take a look.

**Dave Jones:** Let's pour it all out here, and nothing left. We've got our nice, these PCB mount battery holders, just snap into there like that. And unfortunately, we're not going to be able to see what the IC is, it's one of those 6-pin SOT-23s. It'll have a marking on it, but it won't actually have the real

**Dave Jones:** part number. So unfortunately we don't know what part it is, but they just snap in there like that. Nice. Looks like he's got the footprint correct. I don't mind these at all, but I probably would have preferred to see like a plastic AA holder or something, maybe mounted on top, maybe covering the

**Dave Jones:** circuitry. Thermally it shouldn't have been much of an issue, but yeah. Works any way you want to do it. And here's a switch, we've got 5 volts and 3.3 volts, there it is, and on-off. Pretty basic. And a AA battery saver. Now here's the

**Dave Jones:** two going to the breadboard, but I wouldn't... oh, is it? No, hang on. Duh. I was just going to make the complaint that if they were here, in the middle of the board, then you're taking up space, you'd want them on the edges.

**Dave Jones:** And duh, of course they're actually on the edges. I should look before talking, but eh. And there's his web address, raisehobby.net. I wouldn't get .com, I guess. So I had to get .net. That can suck sometimes. But anyway, I'm going to solder these two on here and see if it plugs

**Dave Jones:** into the breadboard. Wah, wah, wah, wah. Look what's happened. It's clearly not designed for my type of breadboard. So it's designed for this smaller type one here, which has got the narrower space between the top and the bottom. I thought mine was a pretty darn standard breadboard.

**Dave Jones:** It is a K&H, a very popular one. K&H model RH32. I've got a couple of these. And unfortunately, it's not the right pitch. It needs to be a bit wider. I guess it would be nice if it supported both pitches. Make the board a little bit, actually it doesn't even need to be wider, it is

**Dave Jones:** just the correct width. Just needs a couple of extra footprints on there. Alright, let's give it a quick go here. I've got my power supply killer, the BK Precision 8500 300 watt programmable electronic load. Love it. So we can, I put it in constant current mode, here we go.

**Dave Jones:** We've got I-set, constant current, 0.1 amps, 100 milliamps, so that should be fine. It said it was up to 300 milliamps or something. And we've got our input voltage here. And our output voltage, this is the output voltage as well. It just double-checks that, we don't really need

**Dave Jones:** this meter. So we'll give it a go here. 0.1 amps, constant current, 100 milliamps, 3.1 volts input voltage, which will be a couple of fresh alkaline cells. And let's switch it on. It drops down a little bit. Drops down 150 odd millivolts or something like that.

**Dave Jones:** And we want, I'll wind the input voltage down, and we want it to go down to 0.8 volts per cell. And there's two series cells on this circuit here, so a good alkaline, well an alkaline battery will be deemed to be completely dead at 0.8 volts.

**Dave Jones:** So if it works down to 1.6 volts, then it's a winner. So let's wind down my input voltage, still hanging in there, still hanging in there. 1.6, not a problem. It definitely uses all of the, ah, there we go, it's starting to drop out now.

**Dave Jones:** There we go. So that's at 100 milliamps. And Ray claims 350 milliamps output current, but that's clearly not on the 5 volt rail, because I've got 3 volts input, and it's dropped down to 4 volts, so it's certainly not capable of, ah, let me measure the temperature down there with my finger.

**Dave Jones:** It's not wet, but it's a finger. So, no, it's not getting warm at all, but it's certainly not capable of delivering 350 milliamps at 5 volts, that's for sure. Let's switch on over to the 3.3 volt one. Let's, ah, restart that, and there we go, it is able to do 3.3 volts output at 350 milliamps

**Dave Jones:** though. And once again, we'll wind down the input voltage, and oh, there we go, 2.88, no, it's real, no, it won't do 350 milliamps below, at 3.3 below 2 point, yeah, 2.5 odd volts there, so yeah, that's definitely not maximizing the usable capacity of the battery.

**Dave Jones:** So I don't think it's going to do 350 milliamps on either of the ranges. Well, actually this comes as no surprise, I just checked Ray's website, he's got the schematic up there, you can download it, as well as the board files and stuff, and it uses the microchip MCP1640.

**Dave Jones:** And sure enough, it's at 3.3 volts output voltage, it's only rated for 350 milliamps for a 2.4 volt input voltage. So as soon as it gets to 2 point, well in our case it's no, it's like 2.5 or thereabouts, so you know, it's

**Dave Jones:** near enough to the data sheet there. And if you want 5 volts out at 350 milliamps, then it requires an input voltage of 3.3 volts. So we can try that, we can go up to 3 point, let's go above that, let's point 3.33, and let's switch our output to

**Dave Jones:** 5 volts. It doesn't look like it likes switching that voltage with the load there. So let's, there we go, yeah it's, we're going to have to wind up, it's low, there we go, 3 point, there we go, it's climbing up, so it's almost there, 3.5 volts.

**Dave Jones:** So it's not going to be spot on to the data sheet value, because that depends on the type of inductor used and the components and stuff like that. So you know, the data sheet values are only going to be typical, but it seems to match that reasonably well.

**Dave Jones:** It's a 96 percent maximum efficiency device, it's not bad at all, and it's works down to 0.35 volts input voltage, but it doesn't start up at that, it will start up at 0.65 volts. So it's not a bad little DC to DC converter, but you've got to work within its limits.

**Dave Jones:** So there you have it, there's Ray's little AA battery saver. As I said, I think it needs the correct, it needs different footprint pitch headers on there for different types of breadboards, maybe there's only two different generic types, I'm not 100% sure, but it certainly doesn't fit mine, which is a bit of a bummer.

**Dave Jones:** If you've got metal battery holders, it would have been nicer if maybe you've got a standoff plastic one, because these can short out. You know, if you're throwing, you know, if this is just around your bench and you've got leads and things going everywhere,

**Dave Jones:** you don't want to accidentally short out the battery terminals anywhere, that could be a bummer and ruin your day, but hey, not a bad little thing. And if you want to check it out, there's the address, aasaver.rayshobby.net. Thanks Ray, good one. And our second package, looks like it comes

**Dave Jones:** from Sweden, Swedish Post. There it is, everyone's got the CN22 customs form. Contains old mobile computing devices. Mmm. I love old computing stuff. Three pieces with a value of 100. What is that? The Swedish KR, Krona. I think. Rings a bell. I thought Sweden used the Euro,

**Dave Jones:** but looks like they're using the Krona, I guess. And it comes from Frederick. Frederick Petrini. Thank you very much, Frederick from Sweden. Hello to all my viewers in Sweden. And I like, by the way, I don't actually know what's on those stamps there.

**Dave Jones:** I'm not sure what that word is, what are they? It looks weird. It's almost like a flower-like thing or something cut open, I'm not sure. Anyway, no idea. But this is interesting. Open here. So, well, let's do just that. Ooh, it's a bit spongy, so

**Dave Jones:** I guess we can get in there with let's have a look. Don't know why I have to open it at a specific end. Could be a surprise, who knows? Ta-da! Ah, I don't think it matters which way we open it. Hi Dave, time for another vintage teardown?

**Dave Jones:** While digging around in my junk boxes, found some old gear I thought would be interesting for one of your Tuesday teardowns. See, find devices from three generations of PDAs. Ooh, oldest device, Scion Organizer 2CM from 86. Oh, contains an 8-bit CPU run at whopping 900 kHz and 8K RAM.

**Dave Jones:** This device is left over from my dad's computer shop. Never been used. Next one is Palm US Robotics Pilot 5000 from 1996. Oh, 10 years later. This model was the very first in the Palm series. Okay, I've got a Palm 3, I think it is, as well as a Palm

**Dave Jones:** 5, you know, with the nifty fold-out thing. Anyway, it has 16 MHz Motorola 68328 512K. Oh, big step up in 10 years. Keep track of your schedule at uni. Last item is a PDA-GPS combination from 2003. HP iPack H5550 with a 400 MHz XScale.

**Dave Jones:** Whatever happened to the XScale processor? Is it still around? I don't know. 128 MB RAM. Rest comfortably in a Navman GPS jacket. Woohoo! Car Navigator and my first geocaching GPS. Oh, he's a fellow geocacher. Excellent. My geocaching name is Ecoteam. Nicole and I were, well, we were Ecoteam.

**Dave Jones:** We still are Ecoteam. Haven't cached for quite some time, but there you go. Reception was quite bad for geocaching with the PDA. Keep track of them. Excellent. Thank you very much, Frederick. Beautiful. Here we go. Oh, there it is. Palm Pilot US Robotics.

**Dave Jones:** Beautiful. That was before they changed. They used to be called US Robotics, right? I think. And then they changed their name to Palm, or they were bought out by Palm or whatever. Made in Singapore. Singapore made a lot of stuff back in the

**Dave Jones:** day. There's a reset there. Powered from two AAAs. And what else have we got here? Oh hey, there we go. Look at that. Beautiful. US Robotics Palm Computing Division. There you go. I didn't know. Maybe that's why they changed their name. They were the Palm Computing Division and they thought, oh, Palm's a nice

**Dave Jones:** name. I don't know. I have to check out the history of that. Well, the history of the name. It's got the pen for all you youngsters out there. Yes, they used to come with pens. Custom port. What else have we got? Oh wow!

**Dave Jones:** Look at that! Man, that is awesome! Almost want to use it. Don't want to tear that down. But it might, certainly it might make an interest in tear down this trio to see the history of, like I did with the mobile phones. Maybe I can do a teardown chronicling the history

**Dave Jones:** of these Palm devices. Beautiful. Is that the huge antenna on it? Absolutely massive. This is before they obviously discovered the fractal antennas, because that's just, that's ridiculous. Hey, you can see my reflection. Hey! Hello! These reflective screens. And yeah, that is huge. Is that

**Dave Jones:** another antenna there? And, oh, external antenna socket. Compact, that looks like a compact flash card. And it sits obviously designed for the cradle. Another custom connector down there. Beautiful. Where's the battery? This has obviously got a, does it have a, no, there we go, it slides.

**Dave Jones:** Oh, this is the cradle. Duh. Okay. Silly me. I thought this was the whole device. Of course not. I know what I'm talking about. Here it is. H5550. Beautiful. And I assume that, well, the battery, the custom battery for it is, maybe it's in there.

**Dave Jones:** Maybe it has got the custom battery. What's that? Cyan Organizer. Oh, this. That's a 32k data pack. Oh, I love it. It'll have a 32k SRAM in it. That's probably all that's in that thing. But back then, hey, a 32k SRAM chip cost you

**Dave Jones:** an arm and a leg. Well, they charge you a premium. Wasn't that expensive around that time. That's all that's in the box. And we've got pocket spreadsheet module. There you go. Made in the UK. Made in the old dart. I've got all my UK viewers.

**Dave Jones:** And there you go. It was like that program pack system. And here is the Cyan Organizer. I always wanted one of these. I lusted after these things when I was a youngster. And it's, no, this one doesn't, here we go. There it is.

**Dave Jones:** Yes. I remember this. I lusted after these things. These were before, like, they were more for industrial. These Cyan Organizers, and there were other brands as well, I can't remember, but they were really big in the industrial scene for industrial control and warehouse inventory systems.

**Dave Jones:** You can get barcode scanners and all sorts of stuff for them. And there's the program packs. They just slide into there. Nice. I like it. And yeah, these were big. Made in the UK back in their day. The Model CM. Brilliant. Yeah, these weren't really consumery

**Dave Jones:** type things back then. There we go. It's a PP3. 9 volt. There you go. Interesting to measure the current consumption of that thing. It's probably not much at all. Well let's try and measure the power consumption of this thing. First of all, standby.

**Dave Jones:** I've got it on microamp range here, set to 9 volts, and I'll have to hold it in there. It's a bit annoying, so let's, because it's got a soft power button, it'll, it won't power on automatically, but it'll go into standby, and there's an initial

**Dave Jones:** current surge there, because that's like an internal cap charging up, and then it's going down, down. Looks like it's settling around 55 microamps. Standby. And if you do the math on that, a standard alkaline 9 volt battery is I think around 800 milliamp

**Dave Jones:** hours or something like that. So if we do 55 microamps standby, then the standby consumption is going to be like 14,000 hours. It's huge. It's basically shelf life of the battery. Let's try and get this thing when it powers up, shall we? It's going to be hard, I've got to hold it.

**Dave Jones:** Hey, copyright. Scion 1986. Brilliant. English. French. Spanish. Oh, what happened there? Something horrible happened. Maybe I took my finger off. Anyway, we're talking 3.3 milliamps. Beautiful. Can I get down there and press execute on that, maybe? Oh, there we go. Fine. Save. Diary.

**Dave Jones:** Calc. Prog. Erase. Brilliant. Anyway, it draws 3.3 milliamps. And once again, if you do the math, 800 milliamp hour roughly for the battery, assuming that, you know, you're the usable capacity, all that sort of stuff. 3.3 milliamps, you know, you're going to get a couple of hundred hours use out of this thing.

**Dave Jones:** Brilliant. So thank you very much, Frederick. That's absolutely awesome. I always wanted one of these. Oh, fantastic. Now I've got one. And we've got a chronological history of these sort of devices. It's going to be really interesting to do the teardown. I'm clearly not going

**Dave Jones:** to do it for the mailbag, but definitely teardown Tuesday material. Thanks, Frederick. And remember, if you want to send me stuff, the address was at the start there. Send me anything you want, pretty much. No more lingerie. Thanks, guys. But if you enjoyed it, please give it a big thumbs up if you enjoyed the mailbag

**Dave Jones:** experiment. And if you want to discuss it, jump on over to the EEVblog forum made in the UK. Catch you later.
