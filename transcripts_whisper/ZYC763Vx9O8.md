---
video_id: ZYC763Vx9O8
title: eevBLAB #6 - Don't Assume It's Faulty
url: https://www.youtube.com/watch?v=ZYC763Vx9O8
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 40, "3": 64, "4": 76, "5": 96, "6": 112, "7": 128, "8": 140, "9": 160, "10": 176, "11": 196, "12": 212, "13": 236, "14": 256, "15": 272, "16": 284, "17": 296, "18": 316, "19": 336, "20": 352}
---

**Dave Jones:** Hi, welcome to another EEVblab episode. This one I wasn't going to do because it's rather embarrassing. But I thought, hey, this could be a learning experience for some people. Now, this is my EDC Cronheight MV106 voltage standard. If you haven't seen it before, I'll link in videos down below.

**Dave Jones:** Very nice metrology grade voltage reference standard. And I was testing a multimeter the other day, plugging it into it, and as usual I set it for 10.0000 volts. And this thing is absolutely a bang on. I've had it tested at a traceable Cal Standards lab.

**Dave Jones:** And this is what I got. 10.470 volts. Now, I sort of freaked out for a second because I actually had the multimeter switch to ohms when I actually plugged it in. And, of course, in ohms mode, the multimeter will try and generate a voltage and try and generate a current

**Dave Jones:** into this thing. And I've done that before without problem, but I was sure that this thing actually worked before I plugged in that particular multimeter on the ohms. And as soon as I plugged it in, wham! All of a sudden it was giving out 10.47 volts.

**Dave Jones:** And look, if I switch it down to 9 here, well, it's still 9.47, so it had all that resolution, right? So it had all the typical resolution there. So it seems to work, but it was out. And if I turn it down to 100 millivolts here, right?

**Dave Jones:** It's bang on, of course. And if I turn it down to 10 millivolts, it was bang on again. It was only the 10 volt range like this. So I thought, oh no! Somehow this multimeter in ohms range is blowing this thing. But I knew, you know, that's

**Dave Jones:** a real remote possibility, because this thing's only going to generate like a milliamp at most, and this thing is pretty robust. It's going to handle that. As I said, I've done it before, but hey, those were the symptoms. And you know, look, it's not a dicky connection or anything like that.

**Dave Jones:** And I turn it negative, and we get the negative. And it works fine on the 100 millivolt range. So I thought, you know, somehow I've blown maybe the output of an op-amp or something in the feedback loop or something like that, you know.

**Dave Jones:** Even though the remote possibility, what it was. And that was what I got. So I thought, you know, that's got to be, like, the problem. And I thought, oh great, okay, I can do a repair video of this. I got all like super excited that, you know, I'd be able to actually repair

**Dave Jones:** this thing. Because it's a nice, you know, all through-hole design and everything in there. So I got all excited, so I moved it over here, and onto the main bench where I shoot videos here. Took the lid off like this, and then I realized, oh

**Dave Jones:** what the problem was. And no, it's not blown. It's a pebcac. Problem exists between keyboard and chair, i.e. me. I was fooled into thinking this thing had failed due to various circumstances, but it hasn't. Now, if you want to try and figure it out, pause the video now

**Dave Jones:** and try and figure it out. So I'll twiddle my thumbs until you go on, pause it, try and figure it out. You should be able to. Maybe not by what you actually see here, but by a bit of deductive reasoning, you might be able to figure it

**Dave Jones:** out. And as I said, no, it's not dicky connections. Down here like this, we've got our sense terminals there, everything's just fine. So what's wrong here? Well, it is those sense terminals. Watch this. Ta-da! Look at that! It wasn't making contact on that sense terminal.

**Dave Jones:** And if I put it negative like this, bingo, the negative one also was like just a smidgen out. It wasn't making contact. So these sense terminals here of course, in these sorts of instruments, not only in these metrology-grade instruments, but like a 4 ohms

**Dave Jones:** terminal measurement, that's what you have to have here. A 4 ohms measurement because you have to sense right at the load. In this case we don't have to, hence we can use these shorting bars here because the multimeter load is only 10 meg, of course.

**Dave Jones:** It's very, very small. And these wires here, they're only like a milli-ohm or something, so do-ohms law, you can figure out the voltage drop across these cables. These bugger all, hence why we can just sense here, but larger loads we'd have to sense there.

**Dave Jones:** Anyway, that's what it was! Just a tight, it wasn't tight on there, you know, I wiggled them around, it looked like they were in, you know, but it was only like, you know, a smidgen, like half a turn out or something like that.

**Dave Jones:** That's all it had to be. But it just didn't make good enough contact, just a tiny smidgen out. So there you go, a trap for young players. What's happening, of course, is that the feedback loop in here, if it's got no sense, if it's not reading that sense voltage back, it'll just go to

**Dave Jones:** full scale. So obviously, that's what it's doing. It's going to 10.5 as full scale, and then negative 10.5 down there as full scale, and that will of course change, even if you go down like that. So that's what the problem was! Oh! Yes, it's incredibly embarrassing,

**Dave Jones:** but I thought that might be a lesson for some people. Don't assume something's faulty. I got a bit too excited there that I'd be able to do a cool little repair video with this thing, I think, rather than think about it. But I ultimately did discover the problem pretty darn quick, so

**Dave Jones:** it's not that embarrassing. But anyway, I thought I'd share. Hope you learned something there. Catch you next time.
