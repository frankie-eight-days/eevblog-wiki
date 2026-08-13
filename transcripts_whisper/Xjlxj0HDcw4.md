---
video_id: Xjlxj0HDcw4
title: EEVblog #164 - Agilent Fly To The Moon
url: https://www.youtube.com/watch?v=Xjlxj0HDcw4
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 28, "2": 50, "3": 65, "4": 80, "5": 99, "6": 118, "7": 139, "8": 164, "9": 183, "10": 203, "11": 221, "12": 241, "13": 259, "14": 273, "15": 293, "16": 305, "17": 319, "18": 340, "19": 368, "20": 382}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, you remember a couple of months back I reviewed these new Agilent scopes and how groovy I thought they were. Now, a couple of days ago, a person by the name of Rufus on the EEVblog forum noticed that his one, when it was turned off, was still a little bit warm.

**Dave Jones:** And he measured the standby power consumption and, to his surprise and to mine, it wasn't zero. He measured about six watts or something like that, standby power consumption. Now, this thing has, is supposed to have, listen to it, clunk a big real mains power switch.

**Dave Jones:** It's got the mechanical rod which goes all the way back to the mains power board at the back. And, well, I was as shocked as anyone. So, let's investigate it. So, let's measure the power consumption of this thing. I've got the new Agilent InfiniiVision 2000 series scope here.

**Dave Jones:** I've got my Gossen MetraHit energy multimeter. Now, you've seen this in a previous blog. It's really cool. It allows me to measure power and apparent power and a whole bunch of other stuff and log power, not only for the mains but for other stuff.

**Dave Jones:** So, I've actually got the mains cord here which goes to the oscilloscope. I've broken it out and it goes into the multimeter so we can measure power. And, as you can see here, it's actually acquiring data. There's nothing connected but it's working away there and it's drawing about 54.3 watts.

**Dave Jones:** And that's at 247 volts which is the Australian mains voltage. At least that's what it is at my place here in Sydney. At about 256 odd milliamps. Not a problem. And, if we go over here, we can also measure the apparent power as well which is about 63.3.

**Dave Jones:** Now, the power factor is about 0.86 on that. So, let's see if it draws anything when you switch it off. Ta-da! Look at that! There it is! It's still drawing 6.5 watts! Are you kidding me? God, you'll fly to the damn moon on 6.5 watts!

**Dave Jones:** Unbelievable! And the apparent power, because the power factor is much lower now, it's 0.32. The apparent power's gone up to 20.5 but, unbelievable! 6.5 watts! Shame, Agilent, shame! OK, now here's the board. I've taken it apart. And, as you can see, it's got this long, mechanical, very traditional mechanical lever arm

**Dave Jones:** going back here to the mains input power supply. There's the IEC input connector, there's the input choke, and it goes through to the Lineage Power brand switch mode power supply which looks like a really high quality one but, apart from the standby, power consumption, apparently.

**Dave Jones:** Now, when I did the review of this thing, I just gave that a cursory glance, hadn't taken the board out, and I thought, great, it looks like a proper mains mechanical switch. It's over here on the mains isolated side. You can see the ground plane starts from here backwards

**Dave Jones:** and this side here doesn't have the ground plane on it, so it's totally separate. You can see on the back here, it's totally isolated. So I thought, beauty, it's on that side of the board. So, normally, you would think, common sense would tell you, that is switching the mains input.

**Dave Jones:** But, it's not. I thought this was a little bit wimpy at the time, but I didn't really give it a second thought. I thought, beauty, a proper mains power switch. But, look, if you actually take a look at the board here, you'll notice that the input tracks for the line and neutral go straight through to the choke

**Dave Jones:** and then they go straight through to the input connector of the switch mode power supply. It doesn't go to that switch at all. And if you look on the back, you can confirm that. In fact, take a look at that soldering. It's not the world's best, they haven't cleaned that at all,

**Dave Jones:** but, as you can see, it does not connect through at all. Now, unfortunately, I can't see where those tracks go because it's a four-layer board and if I hold it up to the light, I can't actually see the traces going off. So they've got to go around there somewhere.

**Dave Jones:** But, thankfully, you can use your meter here and you can actually measure it. So let's try that. I've discovered that the centre of this goes to this pin over here like this. As you can see, it's connected straight through. So the centre of that main switch is connected through to this pin here.

**Dave Jones:** And there's that wire there, that pin number one or whatever it is. And as you can see, it goes straight through to this separate connector. I'm not sure what this one is. It's probably some sort of monitoring output or something or monitoring input.

**Dave Jones:** But it goes through to the control side and this connector over here is all the output voltages. So there you go. What do you know? The new Agilent InfiniiVision scopes have a six-and-a-half watt standby power consumption. You can fly to the moon on that.

**Dave Jones:** It's incredible. What is this, the 1970s? A six-and-a-half watt figure is something that you'd expect from a VCR straight out of the 70s or the 80s. It's incredible. Not in a modern, properly designed bit of instrumentation like this. I certainly don't expect six-and-a-half watts and it's not acceptable.

**Dave Jones:** 0.65 watts? Maybe. Not a problem. OK. Now, they've gone to all the trouble to engineer this properly for a mains, a proper mains input switch. They've got the isolated main section. They've got the traditional mechanical arm going back. Beautiful. Lovely. But then they put it into a logic-level switch and they've decided to switch the output off and on, logic-level, on the switch mode power supply.

**Dave Jones:** Why? What's the advantage of it? Does it increase the mean time between fire of the power supply, because it's already warmed up, and you stop those huge inrush currents when you switch them off and on? I don't know. I can guess at it.

**Dave Jones:** Agilent, what's going on here? Let us know, because this is just unacceptable. Really. www.agilent.com
