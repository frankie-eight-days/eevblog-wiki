---
video_id: r-V_Z3bD_PA
title: EEVblog #1107 - Shocking 4K BENQ Monitor Problem!
url: https://www.youtube.com/watch?v=r-V_Z3bD_PA
source: youtube-asr
timestamps: {"0": 1, "1": 13, "2": 33, "3": 50, "4": 67, "5": 78, "6": 91, "7": 105, "8": 120, "9": 134, "10": 148, "11": 162, "12": 175, "13": 189, "14": 211, "15": 227, "16": 247, "17": 260, "18": 275, "19": 296, "20": 316, "21": 336, "22": 350, "23": 363, "24": 378, "25": 392, "26": 406, "27": 423, "28": 439, "29": 452, "30": 474, "31": 489, "32": 503, "33": 514, "34": 526, "35": 540, "36": 552, "37": 565, "38": 596}
---

**Dave Jones:** Hi, please excuse the crudity of this video. I didn't have time to build it to scale or to paint it. I just found an interesting thing which goes way back to a video I done which I'll probably have

**Dave Jones:** to link in way back like in the first 30 videos or uh something like that. Check this out. I got my new 4K monitor which is the uh BenQ EW3270 and watch this. Here we go. Did it? It switched off and switched back on

**Dave Jones:** when I get up off my chair. Hang on. I'll do it again. There we go. And then switches back on. It does it almost every time. And I thought like I originally thought that this was something where it was like

**Dave Jones:** some whiz-bang auto sensor power saving thing where it was sensing that I'm like sitting here and when I move it switches off. I didn't didn't think much about it. And uh not Look at that. And you might have uh or you may be able to

**Dave Jones:** guess. I don't know. Guess. Answers on the back of a postcard what the problem is here. No, it's not some whiz-bang super technology inside this that's sensing that whether I'm sitting in front of it or not. If I put my

**Dave Jones:** headphones on, maybe we can't hear this. Maybe I'll I'll try and mix in the audio. See if we can hear it. But let me stand up.

**Dave Jones:** I'm not sure if that'll come through or not because it depends on the system, but I can hear a little click click click in here when I stand up. And that's due to the static discharge of me standing up from the chair. Like if I

**Dave Jones:** stand up slowly Ah, that's It's going to make a fool of But I can feel I'm wearing kind of s- little bit not not stretch denim, but you know, kind of like a little bit stretchy jeans. They are a bit static-y

**Dave Jones:** and I can actually feel the static build up when I stand up on here. So, when I stand up off the chair, it causes that impulse and I've got a very interesting story back in that old video about how this caused a really

**Dave Jones:** troublesome bug back in the day in the lab at a company that I was working at and finally figured out that I getting off the chair was the problem and generating static and that was upsetting my long-term experiment or whatever it

**Dave Jones:** was. Anyway, that's the problem. So, this monitor is I've got another BenQ monitor here, which is a 24-in one, exactly like they're not exactly the same model, but near enough and it doesn't do it at all. So, there's

**Dave Jones:** some sort of static impulse, which is obviously getting into the you know, the audio system somehow. I'm not sure how it's getting in, so that's why you may or may not hear that click. But there you go, it's interesting. It I

**Dave Jones:** don't know the path that it's getting in. Is it via like the HDMI cable like the shield on the HDMI cable is the electric field that I'm generating actually inducing some voltage in there, which is sort of like you know, tripping

**Dave Jones:** tripping this thing up and causing it to reset like that. But anyway, thought I'd show you that. It's really interesting and just to show you the difference here, I'm actually now sitting on a cardboard a 121 GW box and let's give it a go.

**Dave Jones:** There you go. Doesn't cause the problem because the fabric on the chair combined with my jeans and probably you know, it probably has like one nylon thread for every other thread just to make it a little bit stretchier is um

**Dave Jones:** causing that static and if I whack my headphones back in, yep, confirmed. No more click in the headphones. So, and and I can feel it as well. I can feel that there's less like a almost basically no static build up.

**Dave Jones:** Whereas, I can physically feel that, you know, like your little hairs stand on your end and stuff like that. You can feel that static impulse. So, there you go. Interesting, huh? I never thought I'd revisit that old video, but yeah,

**Dave Jones:** keeps coming up. Okay, so let's get a slight bit more scientific about this, shall we? I got a scope here. Watch this. Ready? Hopefully, it won't make a fool out of me. Ta-da! There's our impulse. Let me do it again.

**Dave Jones:** I want the damn screen to go off. Ah, come on. Ta-da! There's our impulse. That's at uh what's that? 10 nanoseconds per division? There, so you know, hundredish meg, something like that. So, near enough. And that's what my original

**Dave Jones:** video was about was that I originally was picking up because the scope probe is an antenna. If I actually disconnect this, we probably won't get any coupling cuz we don't have an antenna. There you go. But, you plug it in

**Dave Jones:** and got our antenna earth lead on it. And no wackers. Straight in there like that. And no, it's not the the piezoceramic effect in there, which is an entirely different lower frequency thing. This is a high frequency impulse

**Dave Jones:** into the lead of the oscilloscope coupling through the front end. It gets all complex and through like common mode interference and stuff like that. And it generates um, because static can generate tens of thousands of volts and generates an

**Dave Jones:** electric field around you and that's why, you know, you can spark across and that's why it, uh, whoop. Oh. There we go. Just sitting down did it. And that's why it, uh, can generate impulses like that in the scope and

**Dave Jones:** obviously something's going into the system here, uh, on the, uh, shield of the mains and or HDMI. That's where it's sneaking in. Perhaps that couldn't, you know, that'd be my guess, but it could certainly be just going directly into the circuitry of the

**Dave Jones:** monitor. I just don't know. Maybe I can pull it a bit closer or something like that. So, I'm going to, even though it may not have the frequency range required, going to try some, uh, little, um, ferrite clamps because I, I'm just going to

**Dave Jones:** whack them on the HDMI and the mains cables to see if I can stop them actually getting into the monitor and causing, uh, whatever it is, uh, in the part, you know, if the monitor the reset or maybe it locks up and it's got a

**Dave Jones:** watchdog timer or something like that. Takes a couple, takes two or three seconds to recover. Going to put one of these clamps on the HDMI cable and see if that's the, uh, issue. You know, you could get maybe a better quality

**Dave Jones:** HDMI cable. Some of them even have the ferrite clamps built in and stuff like that. I'll see if I can reproduce it. Cuz all I need is one failed result to prove that that doesn't fix it. So, I'll get back to you.

**Dave Jones:** And check this out. I found a way to that feels like I'm generating a lot of static. A big packing bag and one of my, um, one of my multimeters. If I put that in and out, wow, I can feel the hairs on

**Dave Jones:** the back of my arm, but I can't do anything. So, I can't trigger that. That's right near the cables right at the back of the monitor. So, I'm not sure. No. It's the magic chair, I'm telling you. Oh, no. Got it. There you go. Got it.

**Dave Jones:** So, that had the that had the ferrite clamp on it down there. So, there you go. Um didn't stop it. Not terribly surprising. I thought, you know, I'd give it a go. But, you only have to get one case like that for it to

**Dave Jones:** fail. And it's not, you know, it's obviously um it still doesn't mean it's not getting through the HDMI cable. Uh you know, getting on getting into the receiver in there. Maybe doing some SCR latch-up or something like that and the

**Dave Jones:** monitor's detecting that. And as I said, it's probably got some sort of like watchdog timer or something like that. And it just like resets itself. Something else is latching up in there. It kind of detects that, which is really

**Dave Jones:** good and fixes itself. So, I guess that's a pretty good design. Um but, yeah. It's susceptible. This one here does it and it doesn't do it. This one over here doesn't do it. So, something very specific in there. But,

**Dave Jones:** that's pretty hard. Even though if you put it through, uh you know, compliance testing and stuff like that, I don't know. Uh compliance testing for monitors, you know, whether or not they do some sort of ESD test or anything like that. No

**Dave Jones:** idea. If you do, let us know in the comments. Um but, even if you do that, it you know, there's so many injection paths and different ways to go in there. It's infinite. You can't possibly test them all. So,

**Dave Jones:** there you go. It's not that. Eh, might have to do some more work on it. Anyway, hope you found that interesting. I'll link in my really old videos at the end of this. It was actually a three-parter. So, anyway, hope you found

**Dave Jones:** that interesting. If you did, give it a big thumbs up and all that stuff. Catch you next time.

**Dave Jones:** Mhm.
