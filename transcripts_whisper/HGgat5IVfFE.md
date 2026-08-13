---
video_id: HGgat5IVfFE
title: EEVblog #688 - How To Rework Solder SMD Chips - BTTF Time Circuits Repair!
url: https://www.youtube.com/watch?v=HGgat5IVfFE
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 21, "2": 39, "3": 54, "4": 66, "5": 81, "6": 96, "7": 114, "8": 137, "9": 153, "10": 166, "11": 184, "12": 198, "13": 215, "14": 229, "15": 244, "16": 254, "17": 267, "18": 281, "19": 295, "20": 308, "21": 322, "22": 335, "23": 350, "24": 363, "25": 377, "26": 392, "27": 406, "28": 421, "29": 434, "30": 452, "31": 471, "32": 487, "33": 499, "34": 514, "35": 529, "36": 545, "37": 560, "38": 575, "39": 587, "40": 600, "41": 614, "42": 626, "43": 643, "44": 665, "45": 678, "46": 699, "47": 717, "48": 734, "49": 747, "50": 761, "51": 782, "52": 794, "53": 811, "54": 825, "55": 842, "56": 859, "57": 874, "58": 890, "59": 907, "60": 929, "61": 944, "62": 965, "63": 990, "64": 1008, "65": 1026, "66": 1041, "67": 1059, "68": 1071, "69": 1092, "70": 1116, "71": 1131, "72": 1149, "73": 1167, "74": 1188, "75": 1209, "76": 1230, "77": 1248, "78": 1266, "79": 1284, "80": 1296, "81": 1311, "82": 1329, "83": 1344, "84": 1359, "85": 1377, "86": 1392, "87": 1410, "88": 1425, "89": 1446, "90": 1464, "91": 1479}
---

**Dave Jones:** Hi, quite some time ago, in fact an embarrassingly long time ago, I got this in the mailbag. Thanks to the guys at the Shackspace, a hackerspace in Germany. And they sent me this fantastic Back to the Future Time Circuit, which I consequently went and blew up.

**Dave Jones:** Yes, the magic smoke escaped in my mailbag episode because I plugged the cable in this thing back to front. Unfortunately, oops, and I'd been meaning to repair the damn thing. But as it turns out, quite a few things conspired against me to not get around to this.

**Dave Jones:** First of all, I did immediately go out and order some more chips. And then they were sitting around and I had a lab clean up and I lost them, never found the damn things. So I eventually ordered some more ones, but they got mistakenly sent to my PCB assembler.

**Dave Jones:** And then they didn't know what to do with them. And by the time I figured it all out, they had misplaced them and oh goodness. So then I ordered them again and here they are, and we're going to replace them. So let's go.

**Dave Jones:** So I'll link in the previous video if you haven't seen it. And what happened was, the problem is the board actually hooks up to an Arduino. And it came with a ribbon cable, but stupid me, of course, plugged the damn thing in backwards.

**Dave Jones:** Murphy gets me every time. And yep, oops, because there was no, it's not a shrouded header with the keyed thing like up here. It hasn't got the key in it. So this is the output here, which then you can cascade to another display.

**Dave Jones:** But this is the input. So I got it back to front and of course applied the 5 volts backwards, which goes directly on the rail to the chips on here. There's only two chips on here. There's a 74HC164. I think that's okay, but I do have spares for that if it doesn't work.

**Dave Jones:** And there's the TLC59282 lead driver chip, and that's the one that's blown. I'll quickly show you the blowhole in that. Well, not quite. I think there is a blowhole. I think that's it right there, if you can see that. I can't zoom in a huge amount more, but anyway, tiny little blowhole and it's all burnt and everything else.

**Dave Jones:** That's why you can't see the number very well. But anyway, yet the magic smoke escaped. The active ingredient in all components is the magic smoke, and once it escapes, it doesn't work anymore. So we have to suck this chip out and replace it.

**Dave Jones:** Now there are a couple of methods to getting a surface mount chip like this off, and I've shown some in previous videos. One, of course, if all you've got is a soldering iron, and you've got even a chip like this should be able to do it.

**Dave Jones:** You can apply just regular solder both sides, huge blobs of it covering all the pins like that, and then get in with the iron and then heat up, alternate between both sides like that until it all gets really hot. And hopefully you haven't got, like, lots of big surrounding ground playing that sort of,

**Dave Jones:** you know, sinks all the heat away from it. And if you can get both sides equally heated up, then you can get in there with a pair of tweezers, and you can lift the thing off, or you can tilt the board until the chip falls off,

**Dave Jones:** or you can hold it upside down and, you know, hold your tongue at the right angle until the chip falls off. But it's best to have a large thermal mass iron with quite a decent chisel tip on it, like this JBC iron here, because if you try and use one of those conical tips,

**Dave Jones:** you're not going to get the heat transfer through to the chip. The other way to do it, which I've shown in a previous video, is to use some of this ChipQuik or compatible stuff, which is a very low melting point solder, and it works the same way, except it,

**Dave Jones:** except because it's a very low melting point temperature, then the molten solder stays very molten both sides for a long time. It can stay there for, like, you know, tens of seconds. So you only have to heat up one side once, one side the other,

**Dave Jones:** and then you can even, got time to get in there and get your tweezers and boom, lift it straight off, or as I said, you can tilt the thing or hang it upside down if there's enough mass in the part. It should just fall off.

**Dave Jones:** And your third method is to use your hot air gun like this, and you can get around and just swirl it in there like that. You don't just hold it there unless you've got a large opening tip. You swirl it around like that until you can get,

**Dave Jones:** and once again, heat the whole thing up enough, every joint enough, to physically lift or make the chip fall off. This one's a bit easier to do it, like, upside down and hold it upside down or on the side like that and get around.

**Dave Jones:** And hopefully it should just fall off. Now the main problem with using a hot air gun like this is surrounding parts, of course. You can accidentally heat those up. You've got to watch for parts on the other side. For example, in this case, it's just 7-segment lead displays.

**Dave Jones:** They're not going to be too bad, so. But still, you've got to heat up that board a lot, and it's going to stay hot for a very long time. And of course, if you've got something like this preheater plate, then you can actually put your board in there

**Dave Jones:** and it heats up the bottom of the board, and then exactly what it says, it preheats the bottom of the board so that when you get in here with your hot air gun on the top, you don't have to use as much or keep it there as long as you would

**Dave Jones:** with just a bare board like that, because the bottom of the board and the bulk of the board in there is already heated up, preheated, to a specific temperature. But, of course, we can't do that in this case, because, well, we'd have to take the whole thing apart,

**Dave Jones:** and then we've got our 7-segment lead displays on the bottom. It's just no good for a preheater in this case. So for this particular example here, we could use either the hot air gun or this ChipQuik. The ChipQuik is nicer if you've got it,

**Dave Jones:** and I think that's what I'll use today, because I do have it. But the hot air gun would work quite okay, because there's not a large amount of thermal mass connected to the pads. There's only, like, some ground plane here connected to a pin,

**Dave Jones:** and one up there. So, you know, the hot air would work reasonably well, and there's not many surrounding parts. There's only a resistor there, by the looks of it, and a bypass cap, that's it. And there really is no need to use a high temperature here at all,

**Dave Jones:** because we've got low thermal mass SND parts, we've got a low temperature melting point solder, around about 100 degrees or something like that, I think it is. It's incredibly low. Anyway, so we want to dial in, you know, I've dialed in, like, 260 on there.

**Dave Jones:** So just a very low, safe working temperature for replacing an SMD chip like this. And we've got a large chisel tip. Yes, that is the hot end, so I won't touch it, that'd be embarrassing. And so that will get the heat efficiently through to our ChipQuik,

**Dave Jones:** but you can use pretty much any iron for this, or any tip. You don't need a large thermal mass iron like this in this particular case. And of course, if you're wondering why I didn't turn that temperature right, down, is because, well, we have to melt the existing solder on here too.

**Dave Jones:** So, you know, it's not low melting point like this ChipQuik stuff. Anyway, let's get in here. May not have a... I've only got a tiny little bit here. So let's get in there. Sorry, this is always quite hard to do under the camera.

**Dave Jones:** I've got the camera close with the macro lens, and it's really quite awkward, I'm standing up. Non-ideal. Anyway, let's get in there. And move the ChipQuik across there like that. That should be enough. Now on the other side here as well. Don't apply too much force to those pins,

**Dave Jones:** and bingo, our chip is gone. So you wear a good 10 seconds after that, and that, some of that ChipQuik is still molten. So, yeah, it really does stay molten for a very long time. That's the advantage of it. You only have to touch each side of these once,

**Dave Jones:** and it's pretty much heated up. It stays like that. And the existing solder on the joints mixes with the QuickChip alloy solder. So, and then that, of course, because it's mixed, you know, you've got this mixed alloy in there. Yes, it's going to raise the temperature,

**Dave Jones:** but the bulk of the solder that you're applying is this ChipQuik alloy, so it's still going to have a reasonably low melting point. So that's why it stays molten for so long, and your chip just falls off. I should have kept this at an angle,

**Dave Jones:** and it would have just fell off based on its own weight. But the problem with boards like this, these surface mount pads, there is not much adhesion on the base of that copper pad in there. So if you get in there and if you're very heavy-handed with your iron,

**Dave Jones:** you can actually easily, and or, the iron is too hot, you can easily rip these pads off. And that's the thing you definitely want to avoid when you're doing SMD rework like this, is to actually rip the pads off. And to ensure you don't do that,

**Dave Jones:** when you're getting in there with the solder wick, which I'll show you in a second, always go in this direction like this. This longitudinal direction of the pad like that, because if you go, if you scrape across like that, I won't do it, so I don't want to ruin this,

**Dave Jones:** if you scrape across in this direction back and forth, you risk actually lifting the pads off more than if you stroke back and forth like that. So you really have to have a feather-light touch on these pads otherwise. And a low temperature, as I said,

**Dave Jones:** you know, 260, 270 degrees, something like that, more than enough. If you've got an iron that has a fixed temperature, a 350 or something like that, which might be a typical fixed temperature iron, well, yeah, you're not using the right tool for the job.

**Dave Jones:** Now if you're wondering why I didn't use the ChipQuik flux which comes with this, that is the recommended method, by the way, is to put a little bit of flux along all the pins first before you apply the ChipQuik solder which I did just there.

**Dave Jones:** Well, I've found that I've never really had to use this. It's always worked without the flux. I mean, flux is always, you can never have too much flux when you're doing anything with soldering. But if you maybe, if you've got a stubborn chip or something like that,

**Dave Jones:** really old joints, things like that, yeah, a flux is going to help it work better. But I've had complete success without using the flux at all. And to clean up the pads afterwards, we're going to use some of this solder wick, a reasonably wide one like this,

**Dave Jones:** so you can get in there with your wide tip. Always have, like, different width ones available. I've got some, this is sort of, you know, medium width one, you can get really wide stuff, or you can get the really fine stuff. You really need a roll of each at least.

**Dave Jones:** And this is good multi-core brand, there's nothing worse than getting a cheap-ass brand solder wick. This'll have good flux in it and it'll work really well. So, yeah, avoid the cheapies. And here's where a little bit of flux might come in handy if there's not enough in your solder wick.

**Dave Jones:** We'll just apply a tiny little amount across there like that. And just to help us get that, because we've now got the chipquick alloy mixed in with the regular lead-free solder we had on there before, so it's a nasty little combination, so a bit of flux might help.

**Dave Jones:** And that flux might certainly help if you've got, like, old solder wick lying around or something like that. Anyway, what we want to do is get in there, and as I said, don't scrape it unless you absolutely have to. So we'll just go in there and dab,

**Dave Jones:** just dab them like that at first. And that should hopefully, all that flux burning, don't breathe it in. Can be nasty stuff. So... So I'm not scraping these at all. If I went along and scraped it like that, I'd really do risk lifting up all those pads.

**Dave Jones:** And, well, that's going to ruin your day. And then you'll have to do some serious rework. As I said, the camera's in the way, this wasn't the most convenient one. But anyway, if you do need to scrape, which you shouldn't, definitely do it in the longitudinal direction like that.

**Dave Jones:** So I think those pads look reasonably clean. Need to get in there and inspect them. There we go, if we have a look at those pads, you can see they're relatively flat. There's a little bit of dagginess left there, I could dab a bit more off that,

**Dave Jones:** but still, not a huge drama. So what we want to do is get in there now, and put some flux on these pads. I'm going to use my flux pen here, I prefer my flux pen, there we go. You can never have too much.

**Dave Jones:** And that is genuine ElectroLube flux pen. If you haven't seen that before, nice stuff. They're about, you know, 10 bucks, they can cost like 10 bucks a pen, but you really should have one, and they last forever. Alright, so we want to solder our chip on,

**Dave Jones:** and once again, you've seen me do this before. I'm going to just tack one little pin down in this corner down here. So I'm going to apply some solder over here. Once again, I'm at some weird-ass angle here due to the camera. So I'll apply some solder to that one,

**Dave Jones:** and then we'll be able to tack that one pin in place in the other corner, and our chip will be held in place nicely. Then we'll apply some more flux, and we should be able to drag solder. Now normally I'd do this under my Mantis microscope,

**Dave Jones:** but unfortunately I've got to shoot this video to show you how to do it, so please forgive me if my technique isn't the best here. I'm leaning over the camera at some weird-ass angle, and I've got to try and get that pin tacked down.

**Dave Jones:** There we go, I think I got it. Now I'm actually using my Tigano microscope now, and if you're wondering why I didn't use that to begin with, well, I've been having a lot of issues with the PC used to actually capture this thing,

**Dave Jones:** because I've got to capture the full HDMI output at 15 frames per second. I've got an AvaMedia HDMI capture card and software driver issues causing the machine to crash, all sorts of things, really. And the HDMI output switch to switch between the monitor

**Dave Jones:** and the actual camera output, that's dodgy because it's a passive one, and I need an active HDMI switch for the monitor. Well, all sorts of things, that's just me rocking the table there. I'm zoomed in enough that if I hit the bench, it does rock a bit.

**Dave Jones:** But anyway, now we can do some drag soldering. So it wasn't that good before, and you can see my chip is a little bit off, but that's okay, so I'll tack solder this pin up here, and then we'll be able to drag solder.

**Dave Jones:** Okay, here we go, I'm just going to tack this other pin down here, and I'm using very fine solder, you should always have very fine solder for surface mount soldering. This is 0.38 millimeters, about as fine as you can get. It's multi-core brand, so it's got five flux cores in there,

**Dave Jones:** well, they call it crystal 511, no clean flux. I'll actually provide the link down in here. So yes, it is lead-free stuff, so let's get in there, and quite hard, those pins get in the way a little bit. Having that bigger pin on there, that bigger pad on there,

**Dave Jones:** is kind of a little bit handy. There we go. Bingo. It's now tacked down, and we can do some drag soldering. So we'll get our flux pen again, just go in there, there we go. Tons of... tons of flux along there. As I said, one of these pens might cost you ten bucks,

**Dave Jones:** but they last forever. I've had that same one for years, I think. So here we go, we'll do some drag soldering. I'm going to actually drag it, instead of along, I'm going to drag it out like this. These pins might actually get in the way a little bit,

**Dave Jones:** but let's give it a go. So let's apply some solder to our tip there, and... Sorry, my camera is actually cutting out, my monitor's cutting out here. It's really quite annoying, but there we go. We've dragged, soldered most of those pins. Yep, all of them.

**Dave Jones:** Looks good. Do the other side now, just get a little bit of solder on the end of your tip, and drag it out like so. No problems whatsoever. Oop! A little short there, that'll come off because of the... Oop, my image vanished. There we go, and we're done.

**Dave Jones:** Bob's your uncle. Look at that, reflowed chip. And I'll tell you what, nothing can beat a good stereo vision microscope like this Mantis for inspection. You can move your head around and see that in 3D, which you can't get on the Togano microscope.

**Dave Jones:** Beauty. And we'll just finish that off with a little clean using some, well, choose your cleaner. This one's got a nice little brush on the end, so I'll use that. This is made just down the road here in Australia. Beauty. And that is like a bought one.

**Dave Jones:** Beauty. Now what I want to do is not blow this thing up and let the magic smoke escape again. So what I'm going to do is I'm going to plug it in and measure it before I power the damn thing up. Now, because you'll notice like it's got green over here,

**Dave Jones:** green and black over here, so I'd assume that it plugs in green like that as well. And this connector over here on here is actually polarized. You can see the polarized tab on there, and that goes in there, but we've got no polarization over here.

**Dave Jones:** So I'm going to assume that it matches up like that. But we don't just want to assume, that's what I did last time. Well, I probably didn't assume, I don't think I checked it, although I had some other reason. Anyway, I'm going to take the

**Dave Jones:** negative rail of this thing, this tantalum cap here, or maybe the negative point of this DC jack. Let's take the cap here, and let's measure that. Negative pin over here of the 74HC64, bingo! Look at that, there we go, 0.1 ohms. And I can't just use the pin out of this chip because it's not

**Dave Jones:** a standard pin out. So anyway, the positive side of this cap goes to, bingo, the positive side of there. And the rail is not shorted, as you can see. So it's got 1k and that'll probably change if we swap our probes over here, so no problem at all.

**Dave Jones:** It's not shorted as it was before. So all is good. And that low value we just read there, well, if you disconnect your Arduino over here and measure that again, we'll get a totally different result. And yeah, we're getting 12, 14, it's open.

**Dave Jones:** Alright, here we go. Moment of truth, we're going to power it up. I haven't got the external 5V high current supply to power the display hooked up, but it should at least work dim and power up and give us something with just the 5V

**Dave Jones:** from the USB jack. So here we go. Let's give it a go. Yay! Look at that! Beauty! It works. The green one, as before, very, very dim. I have to adjust the pot on the back. But that is a winner. We haven't actually programmed it with anything, we have to

**Dave Jones:** talk to it via the serial and actually set it up. But that is a winner! Fixed! It'll probably change the display every time we power it up differently. Yeah, we get something different each time. Just random data going to there, but beautiful. Fixed!

**Dave Jones:** Repaired! We can go back to the future. And woohoo! We're up and running. I'm using my Freetronics 11 here, which is an Arduino Uno compatible board. I'm running my Arduino IDE here. I've got the source code from the GitHub and I've loaded that in.

**Dave Jones:** I've downloaded it, everything's hunky-dory. And then I'm running the serial terminal. I typed in question mark as they said, and that gives me the help and bingo, it's running and now I should be able to set up, via the serial commands here, set up the display, the time-date display.

**Dave Jones:** Excellent. Now I was able to talk to it and set up the real-time clock, but nothing changed on here. Because I was measuring actually 4.1 volts on the display here, and maybe I don't know, that's not enough for it to actually communicate with the chips and update the display on here

**Dave Jones:** via the serial interface. Anyway, so I'll power that. Yes, I have checked that this is 5 volts center positive on this pin, and we should be able to plug it in here and just go. And it should have booted up. I've set the real-time

**Dave Jones:** clock display for each one of these, but it's not doing anything. It's not updating at all, unfortunately. So it's not that. So I'm not left with much option but to fire up the scope and probe some pins to see if it's actually sending out the data.

**Dave Jones:** So I've got to start troubleshooting this thing, and here comes the first issue I've got with people who just whack stuff on GitHub like this. I mentioned it before, it always comes up. Look, yeah, they've got all the, you know, it's open source, they've got

**Dave Jones:** it all here, it's fantastic, but where is the schematic in PDF version? No, it's just eaglefiles.sketch. And well, I don't use Eagle, and so I've got to go, for me to see the schematic for this thing, I've got to go into Eagle, I've got to

**Dave Jones:** install Eagle, load it up, and view the schematic just to view the schematic. So please, people, if you're going to do these projects, talking to everyone here, you know, if you're going to release them publicly, please make a PDF available. I know you use Eagle, or you use DipTrace,

**Dave Jones:** or you use Outium, or you use something else, and people, you know, you might assume that everyone else uses the same thing. It just takes a couple of seconds to upload a PDF. Please! And well, here's the issue. I've downloaded the latest version of Eagle, I've tried to

**Dave Jones:** load up the file here, and all I get is start tag, accepted, error, line 1, column 1, blah blah, I don't know, SCH something else, I assumed it was an Eagle file, but it ain't loading. Is it a previous version? Is it some

**Dave Jones:** other program? Grrrr! Wouldn't have happened if I just had a PDF. What? There you go! The controller was designed with Eagle because the Arduino shield that we've looked at, but the display board designed using KiCad, of course, because of the Eagle size limits.

**Dave Jones:** Great, I don't use KiCad either, so I've got to go install that now. Just to look at the schematics so I can start probing this thing and playing around. Well, I just plugged it into the single board here, and it's doing exactly the same thing.

**Dave Jones:** And I'm reading an email from Jockey, and he says that yeah, it should, once I've programmed the real-time clock in here, which I have, I've verified with the serial commands that it's actually ticking over and everything else, then the display should automatically update.

**Dave Jones:** And you can actually choose to plug this into, like, any board you like here. And it's just not working on any of the boards, so I'm not sure if something more is damaged on there, maybe some of the driver transistors or something like that, perhaps?

**Dave Jones:** Or the 164s? I'm not sure, so yeah, I'm going to actually leave that video here, because I really only wanted to do just the soldering of repairing the chip on here. So that's mission accomplished, fixed, and it's powered back up, but yeah, this is going to require some troubleshooting.

**Dave Jones:** So unless it's incredibly easy and it's a pebcac and I'm doing just something dumb, in which case I won't do a follow-up video, but otherwise there might be a follow-up video actually getting the scope out and debugging this thing and figuring out what's wrong.

**Dave Jones:** Anyway, I hope you enjoyed that. It's longer than I expected, I waffle on, I am the waffle master. But anyway, if you want to discuss it, jump on over to the EEVblog forum or leave it in the comments. And remember, as always, if you like it, please give it a big thumbs up.

**Dave Jones:** Catch you next time. www.EEVblog.com
