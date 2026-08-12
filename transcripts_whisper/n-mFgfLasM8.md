---
video_id: n-mFgfLasM8
title: EEVblog 1673 - JBL Partybox 310 Repair - Part 2 (SPOILER)
url: https://www.youtube.com/watch?v=n-mFgfLasM8
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 13, "2": 36, "3": 53, "4": 78, "5": 89, "6": 106, "7": 125, "8": 141, "9": 156, "10": 176, "11": 196, "12": 209, "13": 222, "14": 238, "15": 253, "16": 269, "17": 288, "18": 314, "19": 337, "20": 351, "21": 369, "22": 389, "23": 404, "24": 417, "25": 430, "26": 444, "27": 461, "28": 476, "29": 497, "30": 517, "31": 531}
---

**Dave Jones:** Hi, just a quick follow-up video to that JBL PartyBox 310 repair video that I just released this morning. And spoiler alert, if you want to follow through the hunt as I search down and find the fault, watch the video first. Because this is a spoiler alert.

**Dave Jones:** You've been warned, okay? Because it's quite interesting. So, spoiler alert over with, the fault was that, yeah, we had a break in the power, the soft button power switch line here. So, the switch is on this side and then this goes off to the circuitry over here, which you can have a look at.

**Dave Jones:** Here it is here. So, this is the power key line coming in like this. This comes over two ribbon cables plus six, no less than at least six jumper links to actually get to the point. And as well as a ferrite bead inductor, which is over here like this.

**Dave Jones:** And that goes to one side and then the other side of the switch just goes down to ground. That's it. So, yeah, this is the actual signal here. So, I got to thinking like, look at this, right? I've only really seen a break like this on like a bare board PCB where there's been an over etching problem, for example.

**Dave Jones:** Happens all the time. Like, you know, common as mud, really. That's why they do electrical testing on your bare board PCBs to check that there's no breaks in the PCBs like this from over etching. So, that's it. So, yeah, this is the actual signal here.

**Dave Jones:** So, I got to thinking like, look at this, right? Now, of course, the rubber membrane came through here like this. The rubber membrane keypad over here came through. But look, there's no damage to any of the other traces here. You can see that there's maybe a slight rubbing mark on that one there.

**Dave Jones:** But basically, there's no damage to any other traces. Why? So, why is that power trace and only the power trace got this huge chunk of copper taken out? And well, okay, and I speculated that, oh, this is a party box speaker. Somebody else at a party.

**Dave Jones:** Somebody spilled some beer on it or whatever. And, you know, and the beer got in here and it started to erode the trace away. Okay, fine. But usually, spillage faults that you see, actually, you know, they start to attack other traces and things.

**Dave Jones:** And look, this one right next to which technically has a little bit of a wear mark there through the solder mask. That's not attacked at all. Why? Why is there a big chunk taken out of this? So, I'm not really buying anything to do with, like, rubbing on there.

**Dave Jones:** Okay, so rubbing from the rubber button could have, you know, initially rubbed away the solder mask just in a tiny little spot like that. Okay, just like it maybe looks like it might have done there, perhaps. But then why is this one eaten away and this one is not or any of the other traces?

**Dave Jones:** Hmm. And then it dawned on me. You remember during the trouble? Trouble shooting that this power trace I originally assumed would go back to the microcontroller chip on this board here. That multiplexer chip which drives all the LEDs and everything else. And the key matrix, I thought that would, it would just be part of that key matrix.

**Dave Jones:** And that's one of the assumptions that led me to not check in the continuity of this thing straight away. Because, you know, usually you're not going to get, like, a break in just one line like that. And really, you need a lot of magnification.

**Dave Jones:** You need a lot of magnification to see that. And I didn't really see that unless I, once I got to the end and I traced it down and really zoomed in on it. Because this is a really zoomed in view. This is probably like 20 times, 30 times or something like that.

**Dave Jones:** It's, you know, it's, you can't see this with the naked eye. But it wasn't connected to that matrix. And that's the interesting thing. So let's go back to the schematic over here. Okay, this is the line here. What is different with this line compared to all of the other traces on that board?

**Dave Jones:** Well, as you... As you saw in that video, all the other traces on the board go back basically to that microcontroller or to the... I think it was to the ADC lines or something. But basically, that board is basically powered down once you turn the power off.

**Dave Jones:** But because this is a soft button power switch, which basically, okay, here's our battery here, okay? Or the external 24-volt power supply. But they basically both end up at this point here, okay? And then it goes through this 47K resistor, through this 27K resistor.

**Dave Jones:** Through this diode here, and then onto that power key. And then you've basically got, please excuse the crudity of the model, a switch there. So that's the soft button power switch. So this line is always powered up through either of the two mains or battery power sources through here.

**Dave Jones:** So there's actually a voltage on this line. What voltage? Well, it's going to be like the 8.3-volt battery that we had here. Or it's going to be the 24-volt 1-amp adapter. So there's always voltage on that line. And, uh-huh, what happens when you've got a DC voltage on a line and any sort of chemical involved?

**Dave Jones:** Electrolysis. So I reckon that's what's happened here. This trace here permanently has, unless the battery is flat, permanently has that, like, 8 volts on there. Permanently has a DC voltage on there. So any sort of contamination. Here, like I speculated, beer. Other people speculated that, oh, it could have been a factory wash chemical residue left over.

**Dave Jones:** Somebody said, oh, it could have been some vomit from a party or something like that. Somebody puked over the speaker. I'm sorry for the visual there. But, you know, it happens. Somebody could have peed on the speaker. You don't know what happens at these parties, okay?

**Dave Jones:** So it doesn't really matter what sort of chemical, I guess, was on here, okay? But, yeah, I reckon, because this has a permanent... This is the only line that has a permanent, relatively, you know, 8-ish volts or thereabouts, permanently on it, and these other lines wouldn't,

**Dave Jones:** then that's why electrolysis has started and eaten away, like, really cleanly eaten away the copper there. So that is my best guess now as to what's actually happened here. So I don't think it was, like, the rubbing of the membrane button could have, you know, gotten through the solder.

**Dave Jones:** Because normally the solder mask, right, if the solder mask is intact, then, you know, any sort of liquid shouldn't, in theory, get through the solder mask. But you only need a tiny pinprick in the solder mask. So you'll see, like, little marks like that one, right?

**Dave Jones:** You'll see little, like, you know, you always get, like, little holes in your solder mask and stuff like that, right? So it happens all the time. So all you need... So it could have been a bit of the membrane rubbing. It's no coincidence that was in line with that membrane there.

**Dave Jones:** But then any sort of liquid... It would have, you know, lined up along there or something like that. And all it takes is the tiniest little bit on there combined with some voltage on there. Give it enough time. And it's going to eat away your copper.

**Dave Jones:** Anyway, best guess. I don't know. Chemists, leave it in the comments down below. What do you think's happening here? But that is my guess as to why just that trace and that trace alone was impacted like that and had the copper eaten away.

**Dave Jones:** And the other keys you can see here, right, these are just from ADC. That's why it says key ADC there. Once again, I've got the ferrite bead. And then basically it's just an ADC in the main processor just measuring, you know, like a voltage window threshold.

**Dave Jones:** It's basically a window detector with an ADC. So they've got different value resistors in here to give you and then going down to ground so it knows which button is pressed. So it's not your traditional key matrix. But, yeah, these are going off to inputs.

**Dave Jones:** And you can see that key ADC1 there. Basically just goes straight into this microcontroller here, MLC3740. Don't know what that is. But, yeah, it basically just goes straight into there. So essentially, like, depending on the architecture of the ADC inside the chip and stuff, like, there's not really much happening there.

**Dave Jones:** It's not like it's got that permanent 8 volts from the battery or 24 volts from the DC to DC converter. Directly, always on that line 24-7. So, yeah, this. This line is electrically very different to, like, all the other surrounding lines that you see on here that go to the switches.

**Dave Jones:** And somebody else mentioned, oh, it was the hard plastic. And somebody was, like, sitting on the hard plastic. You know, it sat on top of the speaker and that just rubbed on the board. But it doesn't explain why there's no damage to any of the other traces and there's almost nothing there.

**Dave Jones:** You know, there's maybe a little smidge there. That is my best theory as to what has happened there. But if you've got something else, leave it. Leave it in the comments down below. This is very interesting stuff. Catch you next time.
