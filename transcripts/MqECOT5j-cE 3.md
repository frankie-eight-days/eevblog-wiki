---
video_id: MqECOT5j-cE
title: Latte Panda BIOS Linux Troubleshooting - Featuring Sagan
url: https://www.youtube.com/watch?v=MqECOT5j-cE
source: youtube-asr
timestamps: {"0": 0, "1": 22, "2": 40, "3": 54, "4": 66, "5": 81, "6": 90, "7": 101, "8": 118, "9": 135, "10": 158, "11": 180, "12": 195, "13": 221, "14": 241, "15": 261, "16": 276, "17": 286, "18": 315, "19": 344, "20": 363, "21": 391, "22": 419, "23": 447, "24": 463, "25": 475, "26": 488, "27": 504, "28": 515, "29": 531, "30": 547, "31": 559, "32": 578, "33": 595, "34": 611, "35": 625, "36": 641, "37": 654, "38": 666, "39": 686, "40": 708, "41": 725, "42": 745, "43": 775, "44": 786, "45": 798, "46": 812, "47": 829, "48": 843, "49": 859, "50": 874, "51": 889, "52": 906, "53": 924, "54": 941, "55": 960, "56": 975, "57": 992, "58": 1007, "59": 1016, "60": 1026, "61": 1039, "62": 1050, "63": 1062, "64": 1076, "65": 1095, "66": 1108, "67": 1123, "68": 1138, "69": 1159, "70": 1177, "71": 1192, "72": 1204, "73": 1215, "74": 1229, "75": 1243, "76": 1263, "77": 1276}
---

**Dave Jones:** Hi, it's troubleshooting time. I'm here with Sean. >> Hello. >> He's off camera. We're both off camera, but um this is Sean's um well, you've seen on the mailbag before, but it's now Sean's. He's claimed it latte panda uh board on the um their big uh carrier board. And tell us all about this, what you're going to use it for, what you've done to it. What's the history? Let's go.

**Dave Jones:** >> Uh the history is it arrives in the mail bag. I stole it like with a lot of things. >> I'm sorry. >> Sorry. And then so I wanted to use it for a school project and and other things along those lines and everything was going great. I was testing it and I ran into a BIOS issue and that sucked.

**Dave Jones:** That consumed many months of my life. >> Months? I'm bias. Yeah. Okay. >> You've got no idea. >> Well, what did you install on it? >> Well, okay. Well, I installed Linux Mint because I am a >> Linux nerd.

**Dave Jones:** >> Yes. >> Yeah. Right. >> Yeah. No, I I I won't use Windows anymore. But so I installed >> Linux Mint. >> I installed Linux Mint on it to and I tried to update the BIOS because I wanted to use the GPIO.

**Dave Jones:** >> Yeah, that's right. The GPIO where the GPIO there. Yeah, but we need a lot of GPIOs cuz we're doing an arcade cabinet, right? Arcade >> all of these. >> And we needed all of them. And the standard, the old version, the bias it came with didn't have support for all those.

**Dave Jones:** >> For all of them? No, >> for all of them. Right. So, we had to update it. But the new bias did, >> didn't it? No, I haven't even updated it. >> No, but if we can install the new bias, it will.

**Dave Jones:** >> Yeah. So, you tried to install the bias and what happened. >> Uh, three different error messages. >> Great. Okay. >> Yeah. And I troubleshooted that, troubleshoot that and then concluded that the only solution was to move to Windows.

**Dave Jones:** >> Yep. You did discover that it actually had dual bias though. Yes, it hashed two copies of the bias on there. So you can install two copies and you found that maybe >> if you installed the if you changed the jumper and then flashed the second bias you might be able to get a boot from the second bias but that didn't work either.

**Dave Jones:** >> That didn't work either. >> And we were getting what? Spy bus error messages or something. Yeah. Right. Something something along those lines. Um >> anyway that's not related. >> And then so I woke up one morning and I was like oh wanted to deal with this again. And I tried to tell no one and it wouldn't.

**Dave Jones:** >> It wouldn't. And trust us, we actually have 12 volts plugged into there at the moment. So, it just died. >> Just died. It had not been touched for 4 days. >> You hadn't t Yeah, we went away for 4 days and then we came back and it just it wouldn't boot anymore. Um, yeah. And Well, okay. Troubleshooting time. Um, >> step one, multimeter.

**Dave Jones:** >> Multimeter up the clacker. There we go. 12.22 volts. whether or not that drops under load. Um, well, we did actually measure it on the back of the board at home, didn't we? Yes. And it was uh 12 volt. So, the plug pack, it's just a no-name. Give us a look under the What happened there? Oh, I must have turned on max mode. Yeah, I turned on max mode by mistake.

**Dave Jones:** >> Well, the power supply, it's a cheap Chinese no-name thing. >> Yep. >> It's got multiple spelling errors, >> but it works. >> The mold apparently. The Look, the mold. >> Oh, no. No. You haven't even gotten the best part. Read that.

**Dave Jones:** >> For use with information technology equipment in information for hang on disconnected for use with information technology equipment only the mold 143 PC. >> So yeah, I didn't trust it too much. >> No, no, I wouldn't be trusting that.

**Dave Jones:** Neither would I trust any uh certifications on here um at all. So yeah, anyway, it it is outputting 12 volts um which this board is supposed to take and it was it was working fine with this plug pack and then one day >> and completely died and normally we've the cap's gone from here. Did it ever have a cap?

**Dave Jones:** >> No, never had a cap. >> Okay. And we're supposed to get fan spin, right? >> Y >> and we're supposed to get >> No, there's a light comes on right there. >> Yeah. various leads come on because it's got the um solid state drive in there, isn't it? And they Yeah, you've installed the >> It's not SD, but it's like >> No, it's a Yeah, >> it's like some cheap flash stuff.

**Dave Jones:** >> Um MMC, isn't it? >> EMMC. >> EMMC. E MM >> No, eMMC. EMMC. >> MMC. >> The E is separated from the MMC. >> Got it. >> Okay. Um but it, you know, it's good enough for Australia. Works. It works.

**Dave Jones:** >> Um so yeah, what the heck um is going on here? Now, we can actually power it in different ways. We can power it through Oh, do we have that? >> I left it at home. >> Oh, you left it at home.

**Dave Jones:** >> Power through USBC. >> Oh, we can power it through USBC. Oh, okay. Cool. Bananas. Uh, we we haven't tried that before. Um, or we can power it from the lab power supply or something. Okay. So, you reckon it can power from USBC here, which is interesting because it's on the opposite side of the board to all the DC toDC converters over there. But, okay. But that's what you read in the manual, >> I think. Okay. Well, let's power it up the clacker. This can do 65 uh watts

**Dave Jones:** battery bank. I could plug a uh Yeah, it's detected that we've plugged something in. And nope. Nope. >> Either it's very dead or I was incorrect in reading, >> which is all right, >> that happens. >> Next. All right, we got the power supply. So, let's set that to 12 volts at uh 2 amps. So, that's 24 odd watts there. Thought I had manual focus.

**Dave Jones:** Focus, you bastard. Yeah, let's power that on. So, 24 watts. It won't take that. >> It'll it'll idle two watts. >> Oh, right. It's incredibly efficient. Yes. >> Sniff of an oily rag stuff. All right. Uh channel one output on. Oh, there you go. It's drawing idle. It's drawing 170 milliamps.

**Dave Jones:** That's a fair amount of standby and it's not changing. It's not booting. Okay. It's It's drawing something. It just won't boot. So, you've changed no jumpers or anything. All right. So, I don't think it's the plug pack. It doesn't seem to be the plug pack at fault cuz you can power it from power over Ethernet as well. Um, that's what those pin headers there are for PoE. So, what the heck would be stopping? There's an auto power jumper here, but we tried that, didn't we?

**Dave Jones:** >> Yeah, we already tried. >> We moved that over from there over to there. Presume. Let me turn the power off and on again. And presumably without reading the manual, I'd say that would automatically boot it without the having the soft power button. So that's for industrial applications where, you know, you just want it to boot every time. You don't want to have to have the, you know, a service tech come around and power up your gear again. You know, press the power on button. Although,

**Dave Jones:** that's a pretty good job. If you can get a service call out as a service tech, you know, button, 150 bucks an hour or something plus $100 service call just just to press the power button. Trust me. Okay. 186 um milliamps sounds like a decent enough. It's a bit high. Um that's, you know, in the order of a couple of watts um standby. What is uh 12 volts times 0.18 or round it to 0.2?

**Dave Jones:** It's one uh fifth >> one of uh 1/5 of 12 watts. If I hold it down, right, what did you do to the bias last time? >> Nothing. >> Nothing. >> Didn't touch it. >> All right. So, it was working before you went away.

**Dave Jones:** >> Yeah. >> And then once I I I got that weird error message. I was like, "Oh, got to switch to Windows again." Yeah. And I turned it off and I turned it on again just to check that I didn't do any damage and it worked fine. And then I turned it off and left it for 4 days.

**Dave Jones:** >> And then we went and then we went away and we came back and now it's not booting. >> Yeah. >> What the heck? Hello it. Have you tried um turning this off and this module taking it out and plugging it back in again? I don't know. We're getting desperate.

**Dave Jones:** >> I wouldn't. >> I know. But >> it's the vibe. It's the vibe. Humor me. It's sodium slot, which is interesting. Uses a me a mobile memory slot for its thing. >> Oh, right. Yes, it does. Right. Yeah.

**Dave Jones:** >> High bandwidth. And >> so, do you how do you >> You got to unscrew those screws. >> Oh, you got to unscrew the screws. Oh, and then it pops out. Oh, okay. Well, that's not magnetic. All right.

**Dave Jones:** >> You just slide it out. >> Slide it out. I've got the power. Oh, slide it out. But it's got catches on the side. Oh. Oh, yeah. There we go. Catch and catch. Hey, there it comes. >> There it is. Your little latte panda.

**Dave Jones:** >> So cute. >> It is so cute, isn't it? There's our flash. All right. Now, it's got It's got the pogo pins on here. Maybe there's something going on with the pogo pins, but they're pretty good. They're pretty schmick pogo pins. Like, feel those bad boys. Push those in. They feel really springy.

**Dave Jones:** >> Those are nice. >> Yeah. Yeah. The contacts are They're all goldplated. Should work. I already looked at all the contacts on the um slot because if one of those breaks then >> Yeah. Yeah. Yeah. You come. >> It's totally >> all right.

**Dave Jones:** >> It's the entire thing is basically factory new. Like it looks >> no damage to it at all. >> Hang on. I didn't power it up with no latte panda. >> It won't cuz that's all I know. Yeah, I know. It's all the computer. But there you go. It's now drawing 7 007.

**Dave Jones:** >> Yeah, cuz that's just >> standby. Yeah. Okay. So it's uh so there is at least something hello fan spin. We have fan spin >> because the fan's connected to the main board. >> It's connected to the main board.

**Dave Jones:** >> So maybe the process is stopping itself from powering up somehow. Yeah, we actually have fan spin. Woohoo. >> It doesn't know how what to set it to. So it just it's just bumping it 100. >> It just turns it to 100%. Yeah, cuz that is quite loud, isn't it? Yeah.

**Dave Jones:** >> Um, yeah. And it's drawing 250 milliamps now. All right. Let's turn that off. All right. Cool. So, >> so the fact that it that the standby changed when we sold it in proves that there's nothing wrong with the board.

**Dave Jones:** >> Well, it proves that the board that there's power standby voltage going to the board. Um, >> it doesn't it doesn't tell you anything beyond that really. I don't think >> we could take the fan off. >> Yeah, we could. Maybe like a gremlin got in and decided to stab them.

**Dave Jones:** >> A gremlin. >> Gremlin got >> You did not like Gremlins the movie. >> No, >> you were not happy. >> I did not like it. >> We tried to Huxley didn't like it either. We tried to watch Gremlins and you you dissed it.

**Dave Jones:** >> No, didn't. >> You walked out. >> No. >> Unbelievable. Ah, kids these days. Jeez. >> One out of 10. We'll go watch Apollo 13 instead. >> Oh, well, Apollo 13's classic, dude. All right. Well, let's power that up again.

**Dave Jones:** And 17. No, we're back to where we came from. >> Yay. Shock horror. So, can we get the fan out there? >> Yeah. Yeah. No. >> Um, so I would have initially said that you did something to the bias to like you like nuked the bias and then it's got nothing to boot.

**Dave Jones:** >> But you said you booted it back up to test that you didn't you were aware of that >> and it booted fine and now it doesn't >> now it doesn't boot at all. Uh, Ber, Ber, Ber, Ber. Come on, you have to do the line after that.

**Dave Jones:** Oh, he's sick. My best friend's girlfriend's brother's boyfriend and knows this guy who's going with this girl who saw Ferris pass out at Further One Flavors last night. I guess it must be serious. >> Thank you, Simone. >> Can you quote the rest of the movie as well?

**Dave Jones:** >> Probably. I might have gotten a word or two wrong there, but you know, a little bit rusty on my ferris quotes. Um, oh, but he's very popular, Ed. The sporto, the motorheads, the geeks, bloods, waste toys, dweebies, they all adore him. They think he's a righteous dude.

**Dave Jones:** >> What? You remember useless trivia? >> Yeah. All right. All right. All right. All right. Don't judge. All right. Um, it is a good movie though, right? Ferris is classic. Ferris. >> Ferris is great. >> Should we open it up to the comments because we don't have all day to work on this? I We just wanted to get it here to see if it was drawing like standby power and stuff. Oh, it's got two little fuses down there. Two little onboard fuses, but they wouldn't be blowing. I mean,

**Dave Jones:** it's drawing standby. So, >> we could try switching back to the other BIOS. Both of them work fine. >> Oh, yes. Yeah, yeah, yeah. Okay. Yes, yes, please. Where's the Where's the jumper switch for the other bias? >> There.

**Dave Jones:** >> There. Oh, little dip switches. Oh god, look at the tiny things. And they are they labeled? >> Uh, yes. >> Yeah, they're labelled. You can read that. >> You cannot read them. >> No, I can't read that. Even with my glasses, I can Oh, I can barely read it.

**Dave Jones:** >> Give me something very small. >> Here you go. >> Small pointy. >> Why don't you have a Swiss Army knife on you yet, dude? >> Because mother, >> right? No, she'd let you have a Swiss Army knife. All right.

**Dave Jones:** Here we go. Okay. Power off. Power back on. And Oh. Oh, THAT WAS IT. IT WAS THE BIAS. >> WHAT? >> It was the bias. >> The other one didn't work. >> But the other one worked. >> But the other one worked. You booted it up the other day.

**Dave Jones:** >> Both of them work. >> Yeah. You booted up the other day and now it's Oh, >> no. That's normal. >> Oh, it just Oh, it is. Oh, okay. Oh, yeah. Yeah. There it goes. >> It just goes on and on. the fan the fan curve is really like wanky janky.

**Dave Jones:** >> Right. It's just going through the boot process and it's just Yeah. Yeah. Okay. So, now it's now it's 9.87 amps. >> Yeah. >> Um >> we need a display. >> We do need a display. And we can um see all the minty goodness. All right. We'll get back to you with a display.

**Dave Jones:** >> So, we're slapping it like you could put it like next to a um CRT. >> Oh, yes. >> Yeah. >> And tell everyone you're you're running a CRT at home, aren't you? Oh yes. >> Old school. What is it? A 17 inch jobby or something? It's pretty smack. It's pretty. But it does 1080p.

**Dave Jones:** >> It does. It does do 1080p. >> If you go lower resolution, it does 85 Hz. >> It's like real real smack. >> Yeah. Yeah. Plug her in. Push in it. Yep. Yep. It's up the right way. >> Oh, no. That's not a VGA. That's a 9 pin serial.

**Dave Jones:** >> It's for debugging. >> It's for debugging. Oh, you thought there was VGA on there. All right. We need HDMI. All right. Shove HDMI up the clacker and uh >> we'll need a keyboard and mouse. >> Oh jeez, you want everything. Kids these days.

**Dave Jones:** >> Damn. >> I'll let you know. I can do more with a terminal than 98% population of this planet. >> And he's not kidding, folks. Oh, how should we apply power to the monitor? >> No, maybe we have to reboot it. Is that HDMI one or two or >> I think that's the second one. You turn auto power on.

**Dave Jones:** >> I did turn auto power on, didn't I? It's so cute when it goes be cuz it goes >> Yeah. >> I've got that plugged in. There we go. Yay. We win a chicken dinner. >> Oh, Camos check some error. Oh, it's got a dodgy battery in it.

**Dave Jones:** >> Oh, >> it it could have a >> That might be why the second BIOS doesn't work. >> It's really only to keep the real time clock. >> Um, usually. >> Yay. >> Latte panda. >> It's working. We are pandering. Never pander folks. Don't pander to people.

**Dave Jones:** >> Oh yes, that took me too long. >> Yes. Trap for young players that one. >> Oh, >> Linux men. Linux men. >> We're not worthy. We're not. >> Right. So why was that bias doing that? >> I have no idea.

**Dave Jones:** >> Like it that other bias wouldn't work. Should have tried that at home. But but the problem is you had anticipated that. >> I did. and you had tested it. So, >> look at that beautiful >> 1680 by 1050. Oh, yeah. This is an oddball monitor, I think. Yeah.

**Dave Jones:** >> No 1080p. >> Oh, that's tasty. >> Yeah, this is an oddball monitor, I reckon. Sync Master B 2240. >> Oh, that's cool. It seems to It detects the battery of my wireless things. I had no idea Linux was that capable.

**Dave Jones:** >> Oh, did you bring a mouse? Did you >> wireless mouse? >> Oh, right. Okay. >> I found it lying around. Oh, and it's already hooked up to Oh, you've got a dongle in there. Okay. Oh, that's my mouse.

**Dave Jones:** >> Yeah. >> Oh, you found it lying around the lab. Okay. >> Lakes people get angry if I don't do this. You don't understand. Neoetch. >> Neo. What is it? >> Neofetch. You have to do this to show offet.

**Dave Jones:** >> What Linux is show you're using so everyone can flame you online. >> Oh, got it. Okay. Right. Yeah. Well, you want to be flamed online. >> This is just a stock Linux install. This is not >> Okay. You haven't done anything fancy.

**Dave Jones:** >> Nothing fancy. You should see my laptop. It's >> Oh, man. >> Oh, that's the dumpster laptop. We're using that dumpster laptop we found. What is it? >> Call it a dumpster laptop. >> It's a Dell. It's great. Yeah, we've actually pimped it out.

**Dave Jones:** >> It's a beautiful machine. >> Yep. Yeah. Pimped it out with a new battery and more memory and Yep. >> Yeah. >> Sweet. So, we've got an Intel N100. That's good enough for running our little arcade project we want to run it for.

**Dave Jones:** >> Compared to like a even compared to a Raspberry Pi 5 compute, which is like that's the big beefy Raspberry Pi. Y >> the CPU performance is up to twice as better as good and the and the internal GPU performance is 80 times.

**Dave Jones:** >> Mhm. >> Not 80%. 80 times better. >> Right. >> So yes. >> What is mutter? Muffin. >> Muffin. Oh, that's >> WM Windows man. >> Window manager. >> Window manager. >> Windows window manager. >> And and your theme is mint white dark aqua.

**Dave Jones:** >> So that's just the stock. The real important one is the um is the display driver. >> Cinnamon. >> Yeah. >> All right. >> Yeah. >> Cool. >> It works. >> Do you manually install Cinnamon? Did you or >> No, no. That's what mint uses. Okay.

**Dave Jones:** Right. >> You can use other display ones, but it's not recommended. >> Got it. Okay. >> What else can you show us? >> Look guys, I use Linux. >> Yay. >> You're the only one in school who knows what Linux is, right?

**Dave Jones:** >> Oh, yeah. Totally. >> Yeah. Tech literacy in this generation is horrible. >> Yeah. >> Are you kidding? >> Unbelievable. And you tried to take um your originally you can you still to this day >> cannot connect some school cannot connect that dumpster laptop running.

**Dave Jones:** You're the only one who takes a lint Mac a lint laptop. >> Did you say lint? No. A a lint >> lint >> a a Linux laptop to school. >> Yeah. >> And you can't connect it with the Wi-Fi because Yeah. What was the technical problem that you discovered though? It wasn't compatible with >> proprietary software. Screw you, middle finger.

**Dave Jones:** >> Oh, right. Okay. And it was it claims to be compatible with Linux, but it's not. >> It's not. >> And even it couldn't. >> Yeah. >> Yeah. The IT whole entire IT DEPARTMENT WENT A REAL problem to solve. And um No, they couldn't do it either. And you tried various patches, didn't you? You tried lots of research the hell out of it.

**Dave Jones:** >> But I gave up and just started using mobile router. >> Right. Okay. Yes, we Yep. Once again, another dumpster item. >> Yay. >> Yeah. Dumpster laptop, dumpster item running. >> Everything >> dumpster mint.

**Dave Jones:** >> I wonder when you'd get that. Yeah. Anyway, um that's problem solved. So, what happens if we switch back to the other bias now? Will it boot? >> It dies. >> Let's see. Let's see. >> Okay. Yeah, that that'll be the last thing we try. Which which one is it?

**Dave Jones:** One, two, three, or four? >> There you go. Now, this is the bias on the on the carrier. >> All right. Well, turn the power supply on. Press the output. No, >> no, >> no. See, it doesn't. It doesn't like that at all, does it?

**Dave Jones:** >> The other BIOS. >> Yeah, but you flashed the other BI or you attempted to flash the other bias and Yeah. No, you couldn't, right? It wouldn't let you. >> I booted it back up again. >> You booted it from that second bias.

**Dave Jones:** So, what? The second bias has suddenly died. That's weird, huh? >> Hold on. I just want to check that we didn't get a fluke. I'm going to switch back to the other BIOS. Yep. >> Switch back to the other one >> and turn it off and on again. Hello, it Yep. Yep. There you go. And it boots.

**Dave Jones:** Wow. All right. Well, that's strange. We'll have to deal with that. But that's it for this video. Catch you next time. >> You got to say catch you next time. >> I don't I'm not good at saying. >> You got to invent your own catchphrase then. If you're not going to carry on the family catchphrase, you're going to come up with your own.

**Dave Jones:** >> That is not the family catchphrase. >> Well, I've I've started a trend. So, you either got to use the family catchphrase. Catch you next time. Or you got to come up with your own. What's it going to be, kid?

**Dave Jones:** >> Catch you next time. >> Thank you.
