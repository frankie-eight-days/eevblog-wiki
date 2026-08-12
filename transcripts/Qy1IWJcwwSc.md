---
video_id: Qy1IWJcwwSc
title: Home Assistant Install 2 - Electric Boogaloo
url: https://www.youtube.com/watch?v=Qy1IWJcwwSc
source: youtube-asr
timestamps: {"0": 0, "1": 9, "2": 28, "3": 44, "4": 55, "5": 69, "6": 88, "7": 106, "8": 115, "9": 137, "10": 146, "11": 153, "12": 167, "13": 180, "14": 192, "15": 205, "16": 217, "17": 232, "18": 247, "19": 264, "20": 278, "21": 298, "22": 312, "23": 328, "24": 347, "25": 365, "26": 382, "27": 396, "28": 421, "29": 433, "30": 446, "31": 457, "32": 474, "33": 497, "34": 503, "35": 515}
---

**Dave Jones:** Hi, just a quick follow up to the previous video on the home assistant install. I've got it running no problems. I'll tell you how in a second. It is drawing what it just JUMPED UP.

**Dave Jones:** I SWEAR IT WAS SITTING AT 8 THERE WE GO. SITTING AT 8 it was sitting at 8.8 watts forever. So yeah, it's around about 8.8 watts idle at the home assistant prompt on the T6 30 here.

**Dave Jones:** So that's not too shabby. But somebody in the comments said if I try this T6 20 here it is for those playing along at home. If you want to see inside the T6 20 they said this might be lower power consumption.

**Dave Jones:** So yeah, I'll give that a go. You can see that the heat sinks are considerably smaller, isn't it? So you would imagine it's going to be using less power perhaps.

**Dave Jones:** We've only got the one m.2 at 16 gig. That's smaller. Bugger. So that does look significantly simpler than the is that is that a heat sink running under there as well.

**Dave Jones:** That's interesting. Anyway, yeah, I'll I'll try that out. But okay, for those how I got it running obviously thank you for all those who tried to help and uh for those who complained that you didn't read the home assistant instructions, you idiot.

**Dave Jones:** Yes, I did. I read the home assistant instructions. Yes, they're excellent. But no, they did not tell me what I wanted to do, which was to in transfer a home assistant install from the external USB stick to the internal solid state drive.

**Dave Jones:** That's what I was trying to do and the instructions do not tell you how to do that. That's why at that point I had two options. One is to try and Google the damn thing, right?

**Dave Jones:** And I end up going down some bloody Reddit thread rabbit hole or some forum thing where I don't know if I might get lucky people might tell me that that's not possible or do it this way or something or I could spend a couple of minutes and try grok try a large language model and to see if there was any solution for that.

**Dave Jones:** And you know, it's not like I spent hours on the large language model. It was worth a shot just taking a couple of minutes. It gave me various suggestions and I said oh this one doesn't work.

**Dave Jones:** It gave me another one another one another one another one and I tried like you know, four different ways or something and it turns out none of them worked.

**Dave Jones:** But I don't think it was large language model hallucinating. I think it was technically possible in a previous build for some previous builds of home assistant. But it turns out it is not possible as far as I'm aware.

**Dave Jones:** I don't know. Leave in the comments down below. But for home assistant, it is not possible from the home assistant prompt. It doesn't have the Linux tools installed in there.

**Dave Jones:** Whatever it is, right? It doesn't have the tools installed the format tools. It doesn't have the you know, the transfer. It doesn't have all those Linuxy command line tools that from the home assistant prompt.

**Dave Jones:** You can't actually transfer this OS from the external drive to the internal drive. It's not possible. So all I did to get it working was to simply remove the solid state drive, whack it in my desktop.

**Dave Jones:** It was a bit annoying cuz I had to remove one of my cards there to get access to the slot. Had to remove my other thing. But I whacked it in there and bam, I just used Balena Etcher to transfer that over.

**Dave Jones:** And yes, everyone's now telling me what did you use Balena Etcher for? They steal your data. God, I can't bloody win. People tell me to follow the home assistant instructions, which tells me to use the Balena Etcher.

**Dave Jones:** And then I've got people telling me oh no, don't do that. That's ridiculous. Oh, you bloody what a whoop whoop something. Anyway, for future reference for those trying to do this, it is just way simpler to simply remove the drive, put in another machine and install it that way.

**Dave Jones:** Yes, I'm aware that I could have installed a Linux boot thing on a USB stick and then plugged it in and then formatted this drive for a Linux install or whatever and then try to install this over it's just no.

**Dave Jones:** No, simply it was easier for me to simply remove that, whack it in the other one, use the exact exact procedure they tell you on the home assistant thing use Balena Etcher to transfer the image over and Bob's your uncle.

**Dave Jones:** It just works. So yeah, let me just transfer this over to here. See what the power consumption is. Well, this is a pain in the ass. The little plastic clip thing does not want to screw in here at all and it's got this stupid little clip well, it's actually a very nicely designed clip.

**Dave Jones:** But as it turns out it just doesn't want to line up at all. Let me use this one which which looks identical except it's black instead of blue. That came from the other that came from the other one.

**Dave Jones:** That looks like it might do it. Yeah. No. Yes, that one does it. Okay. Can anyone explain why this blue clip is different from this black clip, please? I just had this fall out.

**Dave Jones:** I swear I didn't touch anything. It just fell out from somewhere. Beulah Beulah What is that? I don't know. Um I'll leave it out. I assume it's not required for electrical function.

**Dave Jones:** Actually, do find it interesting how they've got this shielding cage over the two memory slots here. Not sure why that's required for EMC stuff. It's got the same you know, shielded back in on it as the other model.

**Dave Jones:** So I'm not not sure what's doing there. It's not for heat sinking. It's for EMC. But yeah, bloody studio lights. There you go. During boot 12 watts. It looks like it's uh Yeah, yeah, it's going through yeah, it's booting no problems.

**Dave Jones:** Oh, down to seven. Down to seven. It could be lower consumption. Let's see what we get when we get to the get get to the prompt, shall we? Waiting for home assistant command line to be ready.

**Dave Jones:** I don't remember that last time. Yep, there we go. Supervisor startup. Yeah, yeah, we're good to go. We're at the prompt. We're at the prompt and what what what what um that's settling to like 11-ish.

**Dave Jones:** 11 and a half peaking. Oh no, no. Just down. Come on. What's it doing? Um it's it's not like Windows like it's got there we go. It is down to 7 and a half.

**Dave Jones:** There you go. So that must be the yeah, the maybe the processor throttling or whatever. So yeah, that is a watt less. So that is worthwhile, I guess. A watt is a watt or just a like 1.3 watts or whatever it is.

**Dave Jones:** So yeah, that is technically less. And yeah, I don't need all the power of the 630. So the T6 20 here that'll do the business just fine by the looks of it.

**Dave Jones:** So yeah, no worries. I'll stick with that. So there you go. That's just a follow up video explaining what I was trying to do there cuz I think a lot of people didn't realize what I was trying to do there and technically but leave in the comments down below.

**Dave Jones:** It's not physically it's not actually possible in this build of home assistant from this prompt. If you're running this from an external USB drive, you've got it installed. I don't think it's possible to transfer that from that USB the OS from that USB stick to the internal SSD without other without another Linux boot USB stick.

**Dave Jones:** And then you can format the drive and everything. It's not possible to do it from the home assistant prompt. So there you go. Lesson learned. So there you go.

**Dave Jones:** In the comments, don't be too hasty to jump to conclusions. I was ultimately right. It wasn't possible to do this thing and it wasn't in the instructions on the home assistant website.

**Dave Jones:** Catch you next time.
