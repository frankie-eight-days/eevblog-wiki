---
video_id: YkgCcYG29nk
title: Siglent SDS1000X HD Display Update Rate + Web Interface
url: https://www.youtube.com/watch?v=YkgCcYG29nk
source: youtube-asr
timestamps: {"0": 0, "1": 12, "2": 22, "3": 44, "4": 57, "5": 70, "6": 86, "7": 94, "8": 103, "9": 121, "10": 132, "11": 146, "12": 163, "13": 173, "14": 189, "15": 203, "16": 218, "17": 226, "18": 252, "19": 261, "20": 288, "21": 313, "22": 323, "23": 335, "24": 343, "25": 359, "26": 372, "27": 379, "28": 391, "29": 402, "30": 416, "31": 427, "32": 434, "33": 442, "34": 454, "35": 462, "36": 471, "37": 486, "38": 497, "39": 511, "40": 532, "41": 543, "42": 562, "43": 570}
---

**Dave Jones:** Hi, just a quick follow-up on this uh Siglent SDS uh 1204 X HD as compared to uh the 2354 XR HD. So, So, basically the 1000 X HD versus the 2000 XR HD.

**Dave Jones:** And you know how I noted in the video, sorry about my voice, it's just awful at the moment, um that the waveform update rate seemed faster on this one.

**Dave Jones:** It was just like like in terms of visually, not actual waveform updates uh per second because as it so happens, they speak if you go look at the spec sheet, the 1000 X is actually 120,000 or max 120,000 uh waveform updates per second, whereas the uh 2000 X HD is actually only 100,000.

**Dave Jones:** So, technically at the fastest uh time base, this this lower-end cheaper scope is actually supposed to be a little bit faster, but that could vary. You'd have to measure every time base range or then memory depths and everything else uh involved in that.

**Dave Jones:** But anyway, um I've got them of course both set up for the 1 ms per division here. It's got uh we've got two meg points on this one, and this one can't do uh two meg points, it can only do 2.5.

**Dave Jones:** So, it's actually got more uh data to actually process here, but the same 1 ms per division, the same free running uh trigger here. The trigger point is exactly the same, it's above there, so it's not going to uh trigger on that.

**Dave Jones:** So, it's just going to be auto uh triggering um for the wire sweep. And what I've done is I've put the statistics on, and we can actually get the count for this.

**Dave Jones:** So, I started these, I synced them at the same time. You notice that we're just over 14,000 counts here, but we're now over 20,000 counts on the 1000 X.

**Dave Jones:** So, the 1000 X is actually faster updating as you know, you kind of expect from the uh technically faster um um, update uh, rate in the uh done it, you know, the basic banner spec, but I swear it's not me, right?

**Dave Jones:** Leave it in the comments down below. This just looks like a faster update rate. And yes, these waveforms are the same. Um, I've actually got it's just the inputs open, 50 ohm uh, terminated input.

**Dave Jones:** I set it to 20% waveform intensity and well, this just visually looks way faster so than this. Please leave it in the comments if you think I'm wrong, but like even like the smaller detail in there, it just looks faster.

**Dave Jones:** So, I'm I'm guessing that this has because the architecture is different. This one um, I believe if you look at the teardown, had a uh, separate uh, FPGA or CPLD dedicated to the video uh, the display.

**Dave Jones:** So, maybe it's pi- maybe it's like a totally different architecture and it's piping the information quicker to the screen than what this one does where it has to go through the zinc processor.

**Dave Jones:** That's what it appears like at the PCB level, but we don't actually have the architecture block diagrams or anything like that. But so, it's interesting that it's not a waveform update uh, per second issue in terms of uh, the acquisition capture and you know, dumping the memory and then analyzing it.

**Dave Jones:** It's it's actually a faster scope than the uh, more expensive but a year older uh, 2000X and of course they've changed uh, the architecture somewhat in terms of the FPGAs and stuff like that.

**Dave Jones:** And if you want, I could do like I could dig deeper uh, comparing the actual FPGAs used in this and the amount of density and the uh, in- internal um, arm cortex uh, speed which is running the uh, operating system which is running the scope and everything else.

**Dave Jones:** You know, you could actually do a comparison like that. But yeah, it just um, seems to be uh, piping the data faster to the screen on this one as opposed to over here.

**Dave Jones:** So, which which is of course an advantage of this, I think, but I'm just basing this on visual stuff cuz there's no way to actually know that. Well, maybe there's some thing I could concoct that might actually with like infrequent data and stuff like that, which might be I might be able to somehow visually capture that update rate, but off hand I don't know.

**Dave Jones:** So, leave it in the comments down below if you got any ideas like that. If I sat down and think and thought about it, I probably could come up with something, perhaps, but yeah, it just looks slower.

**Dave Jones:** So, but it ain't. That's interesting, huh? I synced those at exactly the same time. So, it's just that the architecture differences when they change from this older design to presumably this newer design, which they'll go using scopes going forward, I would suggest, is perhaps slower screen updating as opposed to waveform updating.

**Dave Jones:** Very different thing. Unfortunately, we can't get we we can get a trigger out, which tells us the waveform updates per second, but it doesn't tell us how fast then it actually dumps that to memory, but we do know how fast it's actually doing the doing the data analysis here for the statistics for example, and that's one useful metric, and in that case, the new scope is quicker,

**Dave Jones:** which is good because and it's like half the price of the other scope. It's more quicker, but the display a little bit slower. Anyway, curious. And then somebody who asked about the web interface here.

**Dave Jones:** So, I hooked it up, couldn't get it working at first. It was giving, you know, 10.11.something else. It didn't even though I put it on automatic, you know, IP detection and stuff like that.

**Dave Jones:** Wouldn't work, and then I plugged it into the 2000, and it did the same thing, and then I was mucking around, and then I plugged it back, and finally it did it.

**Dave Jones:** So, it just needs a kick up the backside or something. So, I don't know what's going on there, but it did automatically detect it. Maybe I had to set the I automatic IP, close the menu, disconnect, reconnect, and then it it eventually did it.

**Dave Jones:** Yeah, so it yeah, so it just dynamically generated the IP address here. You type in the IP address in your browser, you can password protect it. That's in the manual here.

**Dave Jones:** And the updating seems instant like you know, I can play around and I can hear it beep over there. So, it's like I'm actually pressing the buttons over there.

**Dave Jones:** And the scope actually does support a keyboard and mouse as well. But I haven't actually tried it, but it's supposed to anyway. So, yeah, you've got your full display over here.

**Dave Jones:** It's nice down here. You can do us a screenshot. So, yeah, there it is over there. No worries. So, you can do a waveform binary file save or save it as a CSV.

**Dave Jones:** Very nice. What's the file converter? I don't know. Insecure download blocked. Okay. It's a bit dodgy. Anyway, and you can do firmware update here as well. So, let's let's try it actually.

**Dave Jones:** But anyway, I just want to show you that the updating is like near instant on this, right? So, I can I can drag this waveform around. No problems whatsoever.

**Dave Jones:** That's as good as as instant as you're going to get. Of course, when you're moving it around, the waveform updating stops, but that's got nothing to do with the web interface.

**Dave Jones:** It does that on the physical scope over there. If I actually go over and I'll physically move it with my finger, I can see it's actually stopped as well.

**Dave Jones:** So, there you go. Yeah, it's not a web update. So, the web updating is excellent. You can do the skippy commands, of course. And you can go full screen if you want to.

**Dave Jones:** So, if you want to do the screen capture, you know how it doesn't have the HDMI output, you can do it like this um the web interface and you can capture this.

**Dave Jones:** You can do a screen capture using whatever program you want and you could um you know, put this into a projector or something and show a class or whatever.

**Dave Jones:** So, it's certainly possible. Not as handy and convenient as a HDMI output, but yeah, it's pretty good and you'll see it's it is definitely not upscaling this uh to full 1920 by 1080, which is what I'm capturing this at because the screen I think is only what is it?

**Dave Jones:** 1200 by 600 or something like that. Don't quote me. It's But it's not it's definitely not full HD output. But even the cheapest Rigol one would actually rescale um it to full HD so it looked better.

**Dave Jones:** You didn't actually get any extra I don't think you got any extra room, but it just it rescaled it nicer. Um but still it it works fine. So, yeah, I've got no problems with that whatsoever and it's all it's all really instant stuff.

**Dave Jones:** So, yeah, fantastic. So, you can call up menus. We we can't use the mouse wheel, unfortunately. So, there you go. I can reset my statistics down there. Um but yeah, we can't Yeah, I can't use the uh the mouse center wheel scroll wheel to adjust that at all.

**Dave Jones:** So, I don't know. I've got to type it in. Left right mouse button. I can't do anything. I don't know what's going on. No. I can't adjust that. That's a bit of a bummer.

**Dave Jones:** So, it looks like the only way I can do that is to click on it and then manually enter, you know? So, uh I would have preferred to be able to mouse that because it has the control it's got like it that there should be a control there, but they haven't mapped that to the uh control.

**Dave Jones:** So, that's a that's a bit of a bummer. Um I can't recall if the Rigol did that or not. And if we go into the 2000, I plug that in, it gave me an IP of 143.

**Dave Jones:** It's exactly the same thing. So, yep, they've got exactly the same configuration there. No worries, and it works in exactly the same way. So, yeah. Yep, as you'd expect.
