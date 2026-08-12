---
video_id: yOJ7xPugsdc
title: Hoymiles Microinverter Reverse Engineering CORRECTION
url: https://www.youtube.com/watch?v=yOJ7xPugsdc
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 26, "3": 36, "4": 46, "5": 60, "6": 79, "7": 89, "8": 98, "9": 111, "10": 120, "11": 135, "12": 147, "13": 166, "14": 177, "15": 191, "16": 200, "17": 219, "18": 232, "19": 242, "20": 256, "21": 267, "22": 280, "23": 292, "24": 313, "25": 327, "26": 342, "27": 357, "28": 373, "29": 396, "30": 414, "31": 428, "32": 440, "33": 453, "34": 464, "35": 480, "36": 495, "37": 510, "38": 524, "39": 540, "40": 551, "41": 565}
---

**Dave Jones:** Hi, just a quick follow-up video to the video I just released like a couple of hours ago. Um, which was the teardown and sort of like depoting and reverse engineering of the Hoymiles microinverter.

**Dave Jones:** And a couple of eagle-eyed uh viewers um spotted something that yeah, I got wrong. A couple of things actually. So, I didn't want to pull the video and lose all the comments and everything else and re-edit it.

**Dave Jones:** So, I'll just do this um follow-up video. So, thank you uh for the couple of eagle-eyed viewers who realized quite a large mistake in the uh reverse engineering of this thing.

**Dave Jones:** And this is what happens when you don't engage your brain and you just press record and you just, you know, draw some stuff and yap on and then uh whack it on YouTube.

**Dave Jones:** So, um yeah, oops. Now, the issue is here, right? So, here's the top and bottom of the depoted uh microinverter board. This all looks uh fine here. By the way, a couple of people pointed out, yep, uh I forgot about this one.

**Dave Jones:** These little transformers down here, these are actually uh current uh transformers. TR101 and uh 102 here and and TR100. Um the and this makes sense because look, if you got there's a the current flowing through here like this.

**Dave Jones:** So, I should have actually looked up the number on these because these are a a very cute little uh current transformer. We can have a look at the data sheet here.

**Dave Jones:** They're actually uh Pulse Engineering one. So, once again, you know, top quality uh stuff in here. Anyway, um they're so up to 20 amps uh 20 kHz to 1 meg.

**Dave Jones:** Um yeah, so they're little current transformers. Uh looks like uh what have we got? We've got the 100 to 1 turns ratio, which is common in the solar all of the year um solar current transformers.

**Dave Jones:** For example, you know, like my uh solar analytics one, they're all like 100 to 1 Uh current uh transformer uh ratio. So, yeah. That's that's pretty groovy, isn't it?

**Dave Jones:** Look, and yeah, they don't have physically how it works, but it looks like it flows through the the actual metal on top. So, yeah, it looks like it actually does it flow through that metal there on top, and that is the current.

**Dave Jones:** Well, that's the only thing that can withstand 20 amps, otherwise it's in internally. But, yeah, it flows through there, and then it's got the secondary turns. So, and Bob's your uncle.

**Dave Jones:** And of course, you can turn it into a voltage output one by putting a resistor across that. So, you can current transformers gives you current output. By the way, if you leave a current transformer open circuit, then yeah, the voltage just goes to in theory infinite, but there are limits until it breaks down.

**Dave Jones:** So, yes, don't clamp on your current transformers and have the the output leads just flapping around in the breeze, cuz they can generate a really high voltage. You cannot beat the laws of physics, Captain.

**Dave Jones:** So, yes, if you want to convert the voltage, simply put a suitable spec resistor across there, and converts current to voltage. Easy. But, yeah, they're really quite cool. So, that's that is number one.

**Dave Jones:** Current transformer, I should have just looked at the part number and thought about it a bit more. Once again, you know, got to put more thought into my videos.

**Dave Jones:** But, anyway, the major thing up here is this transformer up here, which I thought was a isolation transformer. I don't know why. Just looking at the arrangement, it's obviously it's obviously it's obvious that they've got a core going around here like this, okay?

**Dave Jones:** And the yellow is a coil. So, you've got one coil on top, and one coil on bottom. This is not a transformer. This is a common mode choke. Common mode, because it uses the same uh core, and it it's choke.

**Dave Jones:** So, this is actually a common mode inductor. So, this is all part of the filtering. So, this is not actually correct. So, we need to kill that. And we need to redraw that.

**Dave Jones:** So, we need to go like that. There you go. And like that, we'll draw them on the inside like that because then it shows that they're well, they're common mode like that.

**Dave Jones:** Okay? So, they're inductors. So, all of this main stuff from right down here, right over to here like this, this is all This is all Well, it goes under here as well.

**Dave Jones:** This is all primary side like this. So, all of your isolation is being done under here like that and in these main transformers like this. And this is obvious.

**Dave Jones:** Once again, if I gave it 2 seconds thought, at 50 because this would have to be like 50 Hz. And at 50 Hz, that tiny little transformer ain't going to do it, okay?

**Dave Jones:** And this is why there at higher frequency switching, they can get away with smaller transformers here like this. But yeah, there's your galvanic isolation is Well, it's goes through under those resistors, and there's your galvanic isolation like that, which Actually, I'll draw the galvanic isolation.

**Dave Jones:** Galvanic isolation goes under like that. Under the transformer. Under those resistors and around like that. And you should be able to see that on the other side. There it is there.

**Dave Jones:** You can physically see the galvanic isolation like that. Going around. Like that. And once again, it's fairly obvious. Um just looking at the top here, right? Um it's Yeah, it's just dumb.

**Dave Jones:** So, anyway, yeah, we've got the dual transformer in a leaf uh flyback here, and then we still have the H bridge, like I said, but basically yeah, we've got the output inductors like this, and that all forms part of the output filtering like this.

**Dave Jones:** So, we got our cap here, and then our common mode inductor, and then our filtering here. Probably this one and that one, is it? And then these ones are after the relay here.

**Dave Jones:** So, yeah, there you go. Yeah, I Now, somebody did actually mention also about the isolation down here, about the creepage isolation and how well, that's not really important because we've got galvanic isolation here, and there's no need for the current to flow from here to here.

**Dave Jones:** Well, not really because you have to assume the reason the galvanic isolation is there is cuz you have to assume a fault on the secondary side. You know, the solar panel, you know, something's happened in this circuitry, something's happened in your physical install with your solar panels, which are all earthed, by the way.

**Dave Jones:** They're all earthed back to your mains earth and up here, and up here, as well. So, they're all they're all connected. All your physical panels, you know, if you get water ingress in your panels and there's, right?

**Dave Jones:** So, you can get leakage from your mains earth through your solar panels back to this side, right? If you've got a failed solar panel, bad installation, water ingress, whatever it is, right?

**Dave Jones:** And then that's when you have to have galvanic isolation between there. That's when it actually matters. So, yes, otherwise they wouldn't bother on the PCB. It's all part of the galvanic isolation.

**Dave Jones:** Yeah, so all of this space, all this clearance here, under here, is all part of the galvanic isolation, just like you get here. In fact, that looks smaller actually.

**Dave Jones:** Um there's a smaller path there actually and that's all part of an end also including the galvanic isolation in your transformers here as well. Um and yeah, so it's all part of it.

**Dave Jones:** So you have to have that clearance there. It's it's just as important as having the galvanic isolation in your transformers. So that's that. And also somebody uh very sharply, huh, I'm here all week sharply, get it?

**Dave Jones:** Gas discharge tube sharp points, that's why. I'm here all week. Um Yeah, I got this uh wrong and that the gas discharge tube is not directly across there. It's there.

**Dave Jones:** Let me grab my pen. It's more likely in series with the MOV and sure enough it is in series with the MOV. If you jump over to the bottom here, the GDT is Yeah, the GDT is here and then the MOV goes over like that or something, doesn't it?

**Dave Jones:** Um yes, it is in series. Yes. Um in fact, you've got two You've got two identical MOVs there. Is it? Anyway, yeah, you can dig around with that, but yes, I do believe that the uh discharge tube GDT is in series with the MOV there.

**Dave Jones:** So yeah, um there you go. That's uh I think they were the main issues that people pointed out. So thank you very much. Um yeah, that was really obvious.

**Dave Jones:** Duh. I'll probably still get emails in a year's time from that video going, "Oh, no, I think this is a not a isolation transformer because it's too small for the 50 Hz." And uh yeah, it's it's an inductor.

**Dave Jones:** It's part of the output filtering. And yep, there you go. So I hope you enjoyed that little update. As always, thoughts and comments down below. Catch you next time.
