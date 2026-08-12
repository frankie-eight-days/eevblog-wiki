---
video_id: YkgCcYG29nk
title: Siglent SDS1000X HD Display Update Rate + Web Interface
url: https://www.youtube.com/watch?v=YkgCcYG29nk
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 32, "3": 50, "4": 62, "5": 75, "6": 88, "7": 100, "8": 118, "9": 132, "10": 146, "11": 166, "12": 177, "13": 189, "14": 205, "15": 218, "16": 232, "17": 247, "18": 260, "19": 275, "20": 293, "21": 308, "22": 323, "23": 337, "24": 350, "25": 365, "26": 378, "27": 392, "28": 410, "29": 424, "30": 436, "31": 449, "32": 460, "33": 473, "34": 486, "35": 499, "36": 514, "37": 528, "38": 543, "39": 556, "40": 567, "41": 584}
---

**Dave Jones:** Hi, just a quick follow-up on this uh Siglent SDS uh 1204 X HD as compared to uh the 2354 XR HD. So, So, basically the 1000 X HD versus the 2000 XR HD. And you know how I noted in the video, sorry about my

**Dave Jones:** voice, it's just awful at the moment, um that the waveform update rate seemed faster on this one. It was just like like in terms of visually, not actual waveform updates uh per second because as it so happens, they speak if you go

**Dave Jones:** look at the spec sheet, the 1000 X is actually 120,000 or max 120,000 uh waveform updates per second, whereas the uh 2000 X HD is actually only 100,000. So, technically at the fastest uh time base, this this lower-end cheaper scope

**Dave Jones:** is actually supposed to be a little bit faster, but that could vary. You'd have to measure every time base range or then memory depths and everything else uh involved in that. But anyway, um I've got them of course both set up for the 1

**Dave Jones:** ms per division here. It's got uh we've got two meg points on this one, and this one can't do uh two meg points, it can only do 2.5. So, it's actually got more uh data to actually process here, but

**Dave Jones:** the same 1 ms per division, the same free running uh trigger here. The trigger point is exactly the same, it's above there, so it's not going to uh trigger on that. So, it's just going to be auto uh

**Dave Jones:** triggering um for the wire sweep. And what I've done is I've put the statistics on, and we can actually get the count for this. So, I started these, I synced them at the same time. You notice that we're just over 14,000

**Dave Jones:** counts here, but we're now over 20,000 counts on the 1000 X. So, the 1000 X is actually faster updating as you know, you kind of expect from the uh technically faster um um, update uh, rate in the uh done it, you

**Dave Jones:** know, the basic banner spec, but I swear it's not me, right? Leave it in the comments down below. This just looks like a faster update rate. And yes, these waveforms are the same. Um, I've actually got it's just the inputs open,

**Dave Jones:** 50 ohm uh, terminated input. I set it to 20% waveform intensity and well, this just visually looks way faster so than this. Please leave it in the comments if you think I'm wrong, but like even like the smaller detail in there, it just

**Dave Jones:** looks faster. So, I'm I'm guessing that this has because the architecture is different. This one um, I believe if you look at the teardown, had a uh, separate uh, FPGA or CPLD dedicated to the video uh, the display. So, maybe it's pi- maybe

**Dave Jones:** it's like a totally different architecture and it's piping the information quicker to the screen than what this one does where it has to go through the zinc processor. That's what it appears like at the PCB level, but we

**Dave Jones:** don't actually have the architecture block diagrams or anything like that. But so, it's interesting that it's not a waveform update uh, per second issue in terms of uh, the acquisition capture and you know, dumping the memory and then

**Dave Jones:** analyzing it. It's it's actually a faster scope than the uh, more expensive but a year older uh, 2000X and of course they've changed uh, the architecture somewhat in terms of the FPGAs and stuff like that. And if you want, I could do

**Dave Jones:** like I could dig deeper uh, comparing the actual FPGAs used in this and the amount of density and the uh, in- internal um, arm cortex uh, speed which is running the uh, operating system which is running the scope and

**Dave Jones:** everything else. You know, you could actually do a comparison like that. But yeah, it just um, seems to be uh, piping the data faster to the screen on this one as opposed to over here. So, which which is of course an advantage of this,

**Dave Jones:** I think, but I'm just basing this on visual stuff cuz there's no way to actually know that. Well, maybe there's some thing I could concoct that might actually with like infrequent data and stuff like that, which might be I might

**Dave Jones:** be able to somehow visually capture that update rate, but off hand I don't know. So, leave it in the comments down below if you got any ideas like that. If I sat down and think and thought about it, I probably could

**Dave Jones:** come up with something, perhaps, but yeah, it just looks slower. So, but it ain't. That's interesting, huh? I synced those at exactly the same time. So, it's just that the architecture differences when they change from this older design

**Dave Jones:** to presumably this newer design, which they'll go using scopes going forward, I would suggest, is perhaps slower screen updating as opposed to waveform updating. Very different thing. Unfortunately, we can't get we we can get a trigger out, which tells

**Dave Jones:** us the waveform updates per second, but it doesn't tell us how fast then it actually dumps that to memory, but we do know how fast it's actually doing the doing the data analysis here for the statistics for example, and that's one

**Dave Jones:** useful metric, and in that case, the new scope is quicker, which is good because and it's like half the price of the other scope. It's more quicker, but the display a little bit slower. Anyway, curious. And then somebody who asked about the

**Dave Jones:** web interface here. So, I hooked it up, couldn't get it working at first. It was giving, you know, 10.11.something else. It didn't even though I put it on automatic, you know, IP detection and stuff like that. Wouldn't work, and then

**Dave Jones:** I plugged it into the 2000, and it did the same thing, and then I was mucking around, and then I plugged it back, and finally it did it. So, it just needs a kick up the backside or something. So, I don't know what's going

**Dave Jones:** on there, but it did automatically detect it. Maybe I had to set the I automatic IP, close the menu, disconnect, reconnect, and then it it eventually did it. Yeah, so it yeah, so it just dynamically generated the IP address

**Dave Jones:** here. You type in the IP address in your browser, you can password protect it. That's in the manual here. And the updating seems instant like you know, I can play around and I can hear it beep over there. So, it's like I'm

**Dave Jones:** actually pressing the buttons over there. And the scope actually does support a keyboard and mouse as well. But I haven't actually tried it, but it's supposed to anyway. So, yeah, you've got your full display over here. It's nice down here. You can

**Dave Jones:** do us a screenshot. So, yeah, there it is over there. No worries. So, you can do a waveform binary file save or save it as a CSV. Very nice. What's the file converter? I don't know. Insecure download blocked. Okay.

**Dave Jones:** It's a bit dodgy. Anyway, and you can do firmware update here as well. So, let's let's try it actually. But anyway, I just want to show you that the updating is like near instant on this, right? So, I can I can

**Dave Jones:** drag this waveform around. No problems whatsoever. That's as good as as instant as you're going to get. Of course, when you're moving it around, the waveform updating stops, but that's got nothing to do with the web interface. It does

**Dave Jones:** that on the physical scope over there. If I actually go over and I'll physically move it with my finger, I can see it's actually stopped as well. So, there you go. Yeah, it's not a web update. So, the web updating is

**Dave Jones:** excellent. You can do the skippy commands, of course. And you can go full screen if you want to. So, if you want to do the screen capture, you know how it doesn't have the HDMI output, you can do it like this

**Dave Jones:** um the web interface and you can capture this. You can do a screen capture using whatever program you want and you could um you know, put this into a projector or something and show a class or whatever. So, it's certainly possible.

**Dave Jones:** Not as handy and convenient as a HDMI output, but yeah, it's pretty good and you'll see it's it is definitely not upscaling this uh to full 1920 by 1080, which is what I'm capturing this at because the screen

**Dave Jones:** I think is only what is it? 1200 by 600 or something like that. Don't quote me. It's But it's not it's definitely not full HD output. But even the cheapest Rigol one would actually rescale um it to full HD so it looked better. You

**Dave Jones:** didn't actually get any extra I don't think you got any extra room, but it just it rescaled it nicer. Um but still it it works fine. So, yeah, I've got no problems with that whatsoever and it's all it's all really instant stuff. So,

**Dave Jones:** yeah, fantastic. So, you can call up menus. We we can't use the mouse wheel, unfortunately. So, there you go. I can reset my statistics down there. Um but yeah, we can't Yeah, I can't use the uh the mouse center

**Dave Jones:** wheel scroll wheel to adjust that at all. So, I don't know. I've got to type it in. Left right mouse button. I can't do anything. I don't know what's going on. No. I can't adjust that. That's a bit of a

**Dave Jones:** bummer. So, it looks like the only way I can do that is to click on it and then manually enter, you know? So, uh I would have preferred to be able to mouse that because it has the control

**Dave Jones:** it's got like it that there should be a control there, but they haven't mapped that to the uh control. So, that's a that's a bit of a bummer. Um I can't recall if the Rigol did that or not. And

**Dave Jones:** if we go into the 2000, I plug that in, it gave me an IP of 143. It's exactly the same thing. So, yep, they've got exactly the same configuration there. No worries, and it works in exactly the same way. So, yeah. Yep, as you'd

**Dave Jones:** expect.
