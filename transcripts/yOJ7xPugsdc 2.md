---
video_id: yOJ7xPugsdc
title: Hoymiles Microinverter Reverse Engineering CORRECTION
url: https://www.youtube.com/watch?v=yOJ7xPugsdc
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 30, "3": 46, "4": 60, "5": 79, "6": 91, "7": 105, "8": 120, "9": 135, "10": 148, "11": 164, "12": 177, "13": 192, "14": 209, "15": 224, "16": 240, "17": 256, "18": 270, "19": 286, "20": 304, "21": 324, "22": 344, "23": 361, "24": 382, "25": 401, "26": 414, "27": 428, "28": 444, "29": 461, "30": 480, "31": 495, "32": 512, "33": 524, "34": 540, "35": 555, "36": 571}
---

**Dave Jones:** Hi, just a quick follow-up video to the video I just released like a couple of hours ago. Um, which was the teardown and sort of like depoting and reverse engineering of the Hoymiles microinverter. And a couple of eagle-eyed uh viewers um spotted

**Dave Jones:** something that yeah, I got wrong. A couple of things actually. So, I didn't want to pull the video and lose all the comments and everything else and re-edit it. So, I'll just do this um follow-up video. So, thank you uh for the couple

**Dave Jones:** of eagle-eyed viewers who realized quite a large mistake in the uh reverse engineering of this thing. And this is what happens when you don't engage your brain and you just press record and you just, you know, draw some stuff and yap on and then uh

**Dave Jones:** whack it on YouTube. So, um yeah, oops. Now, the issue is here, right? So, here's the top and bottom of the depoted uh microinverter board. This all looks uh fine here. By the way, a couple of people pointed out, yep, uh

**Dave Jones:** I forgot about this one. These little transformers down here, these are actually uh current uh transformers. TR101 and uh 102 here and and TR100. Um the and this makes sense because look, if you got there's a the current

**Dave Jones:** flowing through here like this. So, I should have actually looked up the number on these because these are a a very cute little uh current transformer. We can have a look at the data sheet here. They're actually uh Pulse

**Dave Jones:** Engineering one. So, once again, you know, top quality uh stuff in here. Anyway, um they're so up to 20 amps uh 20 kHz to 1 meg. Um yeah, so they're little current transformers. Uh looks like uh what have we got? We've got the

**Dave Jones:** 100 to 1 turns ratio, which is common in the solar all of the year um solar current transformers. For example, you know, like my uh solar analytics one, they're all like 100 to 1 Uh current uh transformer uh ratio. So, yeah. That's

**Dave Jones:** that's pretty groovy, isn't it? Look, and yeah, they don't have physically how it works, but it looks like it flows through the the actual metal on top. So, yeah, it looks like it actually does it flow through that metal there on top,

**Dave Jones:** and that is the current. Well, that's the only thing that can withstand 20 amps, otherwise it's in internally. But, yeah, it flows through there, and then it's got the secondary turns. So, and Bob's your uncle. And of course, you can

**Dave Jones:** turn it into a voltage output one by putting a resistor across that. So, you can current transformers gives you current output. By the way, if you leave a current transformer open circuit, then yeah, the voltage just goes to in theory infinite,

**Dave Jones:** but there are limits until it breaks down. So, yes, don't clamp on your current transformers and have the the output leads just flapping around in the breeze, cuz they can generate a really high voltage. You cannot beat the

**Dave Jones:** laws of physics, Captain. So, yes, if you want to convert the voltage, simply put a suitable spec resistor across there, and converts current to voltage. Easy. But, yeah, they're really quite cool. So, that's that is number one. Current transformer, I should have just

**Dave Jones:** looked at the part number and thought about it a bit more. Once again, you know, got to put more thought into my videos. But, anyway, the major thing up here is this transformer up here, which I thought was a isolation transformer. I

**Dave Jones:** don't know why. Just looking at the arrangement, it's obviously it's obviously it's obvious that they've got a core going around here like this, okay? And the yellow is a coil. So, you've got one coil on top, and one coil

**Dave Jones:** on bottom. This is not a transformer. This is a common mode choke. Common mode, because it uses the same uh core, and it it's choke. So, this is actually a common mode inductor. So, this is all part of the filtering. So, this is not

**Dave Jones:** actually correct. So, we need to kill that. And we need to redraw that. So, we need to go like that. There you go. And like that, we'll draw them on the inside like that because then it shows that they're well, they're

**Dave Jones:** common mode like that. Okay? So, they're inductors. So, all of this main stuff from right down here, right over to here like this, this is all This is all Well, it goes under here as well. This is all

**Dave Jones:** primary side like this. So, all of your isolation is being done under here like that and in these main transformers like this. And this is obvious. Once again, if I gave it 2 seconds thought, at 50 because this would have to be like 50

**Dave Jones:** Hz. And at 50 Hz, that tiny little transformer ain't going to do it, okay? And this is why there at higher frequency switching, they can get away with smaller transformers here like this. But yeah, there's your galvanic isolation is

**Dave Jones:** Well, it's goes through under those resistors, and there's your galvanic isolation like that, which Actually, I'll draw the galvanic isolation. Galvanic isolation goes under like that. Under the transformer. Under those resistors and around like that. And you should be able to see that

**Dave Jones:** on the other side. There it is there. You can physically see the galvanic isolation like that. Going around. Like that. And once again, it's fairly obvious. Um just looking at the top here, right? Um it's Yeah, it's just dumb. So, anyway, yeah, we've

**Dave Jones:** got the dual transformer in a leaf uh flyback here, and then we still have the H bridge, like I said, but basically yeah, we've got the output inductors like this, and that all forms part of the output filtering like this. So, we

**Dave Jones:** got our cap here, and then our common mode inductor, and then our filtering here. Probably this one and that one, is it? And then these ones are after the relay here. So, yeah, there you go. Yeah, I Now, somebody did actually mention also

**Dave Jones:** about the isolation down here, about the creepage isolation and how well, that's not really important because we've got galvanic isolation here, and there's no need for the current to flow from here to here. Well, not really because you have to assume

**Dave Jones:** the reason the galvanic isolation is there is cuz you have to assume a fault on the secondary side. You know, the solar panel, you know, something's happened in this circuitry, something's happened in your physical install with your solar panels, which are all

**Dave Jones:** earthed, by the way. They're all earthed back to your mains earth and up here, and up here, as well. So, they're all they're all connected. All your physical panels, you know, if you get water ingress in your panels and there's,

**Dave Jones:** right? So, you can get leakage from your mains earth through your solar panels back to this side, right? If you've got a failed solar panel, bad installation, water ingress, whatever it is, right? And then that's when you have to have

**Dave Jones:** galvanic isolation between there. That's when it actually matters. So, yes, otherwise they wouldn't bother on the PCB. It's all part of the galvanic isolation. Yeah, so all of this space, all this clearance here, under here, is all part of the galvanic

**Dave Jones:** isolation, just like you get here. In fact, that looks smaller actually. Um there's a smaller path there actually and that's all part of an end also including the galvanic isolation in your transformers here as well. Um and yeah,

**Dave Jones:** so it's all part of it. So you have to have that clearance there. It's it's just as important as having the galvanic isolation in your transformers. So that's that. And also somebody uh very sharply, huh, I'm here all week sharply,

**Dave Jones:** get it? Gas discharge tube sharp points, that's why. I'm here all week. Um Yeah, I got this uh wrong and that the gas discharge tube is not directly across there. It's there. Let me grab my pen. It's more likely in

**Dave Jones:** series with the MOV and sure enough it is in series with the MOV. If you jump over to the bottom here, the GDT is Yeah, the GDT is here and then the MOV goes over like that or something,

**Dave Jones:** doesn't it? Um yes, it is in series. Yes. Um in fact, you've got two You've got two identical MOVs there. Is it? Anyway, yeah, you can dig around with that, but yes, I do believe that the uh discharge tube GDT is in series with

**Dave Jones:** the MOV there. So yeah, um there you go. That's uh I think they were the main issues that people pointed out. So thank you very much. Um yeah, that was really obvious. Duh. I'll probably still get emails in a year's time from that video

**Dave Jones:** going, "Oh, no, I think this is a not a isolation transformer because it's too small for the 50 Hz." And uh yeah, it's it's an inductor. It's part of the output filtering. And yep, there you go. So I hope you enjoyed that little

**Dave Jones:** update. As always, thoughts and comments down below. Catch you next time.
