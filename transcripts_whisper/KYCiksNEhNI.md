---
video_id: KYCiksNEhNI
title: EEVblog #351 - Silicon Chip Magazine - Electronex 2012
url: https://www.youtube.com/watch?v=KYCiksNEhNI
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 28, "3": 45, "4": 61, "5": 71, "6": 85, "7": 100, "8": 115, "9": 129, "10": 147, "11": 165, "12": 180, "13": 197, "14": 210, "15": 222, "16": 240, "17": 254, "18": 272, "19": 288, "20": 305, "21": 320, "22": 333, "23": 344, "24": 356, "25": 368, "26": 384, "27": 397, "28": 416, "29": 430, "30": 447, "31": 466, "32": 485, "33": 503, "34": 519, "35": 534, "36": 548, "37": 568, "38": 582, "39": 603, "40": 615, "41": 631, "42": 644, "43": 658, "44": 672, "45": 690, "46": 704, "47": 720, "48": 733, "49": 751, "50": 763, "51": 779, "52": 794, "53": 807, "54": 824, "55": 841}
---

**Dave Jones:** And I'm here with Nicholas Vinnen from Silicon Chip. Hey, Nicholas, how are you doing? Fine, thanks. How's the stand going? Not bad. We've had quite a bit of feedback the last day, most of it positive, which is good. And even the people who had criticisms were pretty nice about it.

**Dave Jones:** Right, yeah. You can't please everyone with every project, right? No, that's right. Yeah, because you're the main project designer for Silicon. I don't know if I say main, but certainly myself and John Clark are the two people who do most of the work.

**Dave Jones:** How long does it take you to develop these projects, which we're going to take a look at? Well, in terms of, well, there's the throughput and the latency. Right, yeah, yeah. The throughput is about once a month, sometimes a little bit more. Latency is more like, well, some of them take six months, some take three months.

**Dave Jones:** Right. I usually have to start them well in advance, because I usually have one being designed, one that's being made, one where I've built it, and one where I'm testing it and writing software and so on. Because some of your projects are quite complex software-wise, so they take some time.

**Dave Jones:** Yes, they can be. Some of them can. Sometimes it might take me a whole month pretty much just to write the software. A lot of the time I can reuse bits of code. I mean, I find it works pretty well actually. I usually program in C.

**Dave Jones:** Actually, let me just turn this down. Yeah, let's turn it down. There we go. So it's not interfering with what I'm saying. I mean, well, for example, with this project, I've used the SD card code that we've had before. I've used a lot of the same audio code.

**Dave Jones:** So it's sort of a matter of taking the different modules, putting them together, getting it to work, and then a little bit of custom code for the project. Lots of late hours working on the projects? No, not really. No, you don't? Pretty well.

**Dave Jones:** You're pretty efficient at it? Yes. You learn to be efficient. Yeah, it's more a matter of scheduling and just planning ahead than anything else. Right. And also the main thing is trying not to introduce too many bugs and then not have to spend much time fixing them.

**Dave Jones:** That's it. And ideas? No shortage of ideas? Not really, no. No? Pretty much I don't have to try to come up with them. By the time I need a new project idea, usually there's one waiting. Right. At some point I'm sure I'll run out, but it hasn't happened yet.

**Dave Jones:** Okay. Plenty of suggestions. One day we might have viewers, but at the moment it's readers. Shall we check out some projects? Sure, if you'd like. Take us through some. Well, this is the induction motor speed controller. This is a contributed design. Very well thought out one, I think.

**Dave Jones:** It's a pretty heavy-duty piece of gear. Huge heat sink on the bottom? Yes. Well, it's got a lot of power. It's got a lot of torque. It's a pretty heavy-duty piece of gear. Huge heat sink on the bottom? Yes. Well, even if it's 95% efficient, if it's running a 1.5 kilowatt motor,

**Dave Jones:** that's quite a bit of heat to dissipate. And yes, it's quite heavy-duty. You certainly don't want to touch it while it's operating, that's for sure. At 350 volts DC. No, it's pretty serious. There's a schematic, which you can get if you order a silicon chip.

**Dave Jones:** It's published in the magazine. It is. And what have we got? We've got LED music alarm. Yes, this is a sneak peek. This is coming up in the October and November issues. And it's basically – it plays music. It also controls 16 strips of LEDs.

**Dave Jones:** And it's essentially a spectrum analyzer. It varies the brightness with frequency and power. Okay, good. So it's pretty much the idea is you build it, you plug it in, you play music, and you have a light show. No extra effort required. Got it.

**Dave Jones:** Man, hey. Yep. We've got Agilent have loaned you a new – Yep, this is some sort of a portable scope, which seems pretty nice, actually. Are you going to do a review of that? If they give it to us for review, yeah. Oh, right.

**Dave Jones:** Okay. I wouldn't mind. All right. And here we have the – this device is supposed to discourage barking dogs. Does it work? According to Ross, yes, with some caveats. All right. So the dogs learn just to not bark near the device. They're pretty smart.

**Dave Jones:** They are smart. They're certainly smart enough. But anyway, that's sort of the aim anyway is to get them not to sit on your fence and bark at you all day. Got it. All right. Yep. Oh, this looks nice. This is our Ultra-LD Mark III power amplifier.

**Dave Jones:** A lot of tweaking on this one. I'm pretty happy with the way it turned out. It's almost as good performance as our Class A amplifier, but with less heat and quite a bit more power. I saw a couple of kids building this. If you saw my video at the local school, HSC kids were building a couple of these.

**Dave Jones:** Oh, okay. They built some. That's a pretty serious thing to take on. Yeah, yeah. But, yeah, so I've been – I mean, there are obviously some HSC-age students who are very capable and – They're very capable. Really into electronics. They are. Yep. Next up.

**Dave Jones:** This is my PIC-AVR programming adapter board, which basically solves a problem that I've run into many times, which is that you have an in-circuit programmer, you've built your board for whatever reason, you don't have a header on it to program your chip, and you need a way to do it.

**Dave Jones:** And I got sick of building rigs for every different chip to program it. Right. So this one is basically intended to be one device you can reconfigure to route the programming and power signals to your microcontroller. There you go. And it supports every –

**Dave Jones:** Pretty much every PIC-AVR. Almost every PIC-AVR. The 32s? I don't know about the 32s. I don't think they were in DIP package when I designed this. Ah, yeah, they may not be. And I don't – it depends on the pin configuration. It's possible that they're programmed.

**Dave Jones:** A lot of PICs use the same – you know, there's probably about eight different configurations that are used by most PICs, but then there are some oddball ones, and I couldn't support them all. Yeah, of course not. But, yeah, pretty much every one that we've used in a project

**Dave Jones:** can be programmed with this board. Got it. So that was the main goal. Brilliant. And did you write your own software for that, or was it – This doesn't have software, actually. It's all discrete logic. Oh, right. There's a few reasons for doing that.

**Dave Jones:** One of them is I didn't want people to have to program a PIC in order to program PICs. Got it. Chicken and egg. Yes, yes. And the other reason was if I had a microcontroller controlling it, because of the MOSFET gate drive, I'd need a lot of level shifting,

**Dave Jones:** and it would have ended up being almost as complicated anyway. Got it. So I thought discrete logic was the way to go. Excellent. And we've got – what's this? Six test instruments in one. Yeah, this is – it's essentially a USB sound card with a scope-type interface.

**Dave Jones:** So you can use it as an audio frequency scope in combination with the correct software. You can also use it as a spectrum analyzer. The software will also do distortion measurement. So it's a pretty handy tool to have, especially if you don't have an oscilloscope,

**Dave Jones:** or even if you do, it can do some things that scopes can't easily do. Right. So it's just basically an input scope preamp and offset shifter? It's pretty much – it's really only for AC-coupled signals. Oh, only for AC. Yeah. Got it. Oh, because the sound card's only AC.

**Dave Jones:** Well, yeah, the sound – Most sound cards are AC-coupled. Yeah. Well, it's actually – it has its own sound card, essentially, but that chip is designed for AC-coupled inputs. Got it. Yeah. OK, so it uses a Cirrus Logic – It's actually – it's a Texas Instruments Burr-Brown USB audio chip.

**Dave Jones:** Got it. And next up, high-quality digital audio signal generator. Yes. We have that feeding the test instrument interface, generating a sweep at the moment. It can also generate a pulse. It can do mixed sine waves. You can also do square waves, triangle, sawtooth.

**Dave Jones:** And it has analog and SPDIF and TOSLINK outputs. Very nice. My necklace. Sorry, mate. That's all right. Hey, it's Leo Simpson, the editor. How are you doing, Leo? I'm well. We're just running through our projects here. Oh, that's good, good. Excellent. How's the magazine going?

**Dave Jones:** It's going reasonably well. We've got this champion contributor here. He is. He is. Yeah, that's right. And what – your subscribers mostly Australian still, or are they – you're getting overseas? The vast majority. Right. OK. Because I – everyone – I hear a lot of talk.

**Dave Jones:** They're saying that Silicon Chip is the best-produced electronics magazine in the world. Well, I love to hear that sort of thing, David. That's wonderful. Just keep that coming. That's really good. Well, actually, we don't know what will happen to the subscriber base once we go live with our new website, with our page to view and all the rest of it.

**Dave Jones:** So it will be quite a lot better than our – That's interesting. What's the rationale behind that? Well, we think our existing website is well past its years by a judge. You could say that. I think that's the sort of fairly subdued way of putting it.

**Dave Jones:** Yeah. And what will be on the new website? Well, all the magazines that are presently there. Right. But it will be page to view. So, you know, you just turn the pages and all the adverts and everything. So it will be quite a big step up from our existing website.

**Dave Jones:** And if you're an existing subscriber, do you get that access to that? Yes. If you've got access to a particular issue in the old format, you will have access. Oh, if you're an old digital subscriber. Well, when I should say old, I should say a legacy subscriber.

**Dave Jones:** A legacy. Yes. So when we go live, we should have about five years of new archive material. The old material will still be there, so people will still be able to access all of that material that was there before. Got it. Any plans on releasing all the old EA stuff on DVD?

**Dave Jones:** No, it's too hard. Well, you know, I've got to get it scanned. And, you know, then it's got to be searchable. I mean, I'm told the best way to do that is to send it to India. Right. But there are copyright issues for some of the stuff.

**Dave Jones:** They are? Yes. For the contributors like myself? Exactly. That's right. So while we own the entire copyright for ETI and Electronics Australia and going much further back, still the original copyright thing that contributors may or may not have, you know, given over to EA,

**Dave Jones:** and we don't know who did what. Yep. Okay? Because as a contributor to EA, I didn't sign anything. So you didn't sign anything. I didn't give anything away, no, exactly. Well, then your copyrights, well, you're just a very lean person, aren't you? Right.

**Dave Jones:** No, you can have my, you can reprint, you have my permission. Well, I'd always talk to you anyway. But no, there are copyright issues, and the same thing applies to Electronics today, or ETI, or whatever it was called in its various guises. So it is a bit difficult for us.

**Dave Jones:** But you released Wireless Weekly on DVD. Ah, yes, but, ah, no, we didn't. Not Wireless Weekly. Ah, what was it? Radio TV. With Radio TV and Hobbies. With Radio TV and Hobbies, that's right. You see, now that's out of copyright, so we don't have an issue there.

**Dave Jones:** And, you know, we didn't have those sort of copyright issues in those days anyway. Yep. Life was much simpler here. Much simpler, everyone was much kinder, everyone wasn't trying to sell everyone. Well, I don't know that everything was, no, I wouldn't necessarily, I think people are still reasonable, you know.

**Dave Jones:** Yes, of course. You know, I didn't have any road rage on the way here this morning. No, that's right. And I didn't, I wasn't subjected to anything, so. No, anyway, so that's it. So. And we'll have, we'll also have a shop, so people will be able to buy stuff.

**Dave Jones:** We don't know the full details yet. We're presently negotiating with the people who actually house our website now, so. Right. We're hoping to transfer that over within a month or so. I noticed you're now selling the PCBs. Yes, so all the projects that you see here, we would have the PC boards available.

**Dave Jones:** So it's not all the boards going back, but I think we've probably got most of the boards going for the last two years or so, something like that. Right, okay. And if people really want something, well, we can have a look and see whether it's economic for us to order it in.

**Dave Jones:** Right. Obviously, we have to process the board artworks and then send them off to get them made. Of course. But they're very high-quality boards, which you've probably seen. Who actually makes those? A little Chinese person or something. Right, yeah, some one-hung low Chinese.

**Dave Jones:** Yeah, that's right. PCB factory, okay. Yeah, that's right. Because there's not much PCB, I don't think there's one. Actually, there's quite a bit, actually. Are they left in Australia? I don't know, there's quite a bit. Because I'm getting mine made in New Zealand now by Circuit Labs, who are also here.

**Dave Jones:** There's some people in Newport, isn't it, who will do a quick prototype for us and good quality and all the rest of it. So we've used them from time to time. But there are other PC board manufacturers. Now, whether they farm some of that offshore…

**Dave Jones:** Sure to, and they don't tell you. I don't know, I don't know. Yeah, you have to ask. But obviously there's a lot of PC board assembly in this country. Yes, there is. I get my boards assembled here in Sydney. Do you? Yes. So it's not all black.

**Dave Jones:** In fact, people say, oh, you know, there's no manufacturing in Australia. Well, there wouldn't be a show like this if there wasn't manufacturing in Australia. Yes, a lot of it's sort of niche manufacturing, highly specialised. There's very little consumer manufacturing these days, but Australia's still kicking up there.

**Dave Jones:** It is, it's still doing good. So the stand's doing good here. Yeah. Lots of people coming through. Yes, yes, that's right. Terrific. A lot of them just saying hello, because the vast majority of people do know us. Of course. So, yeah. Love it.

**Dave Jones:** And we're looking at some of your, well, I think we've done most of the projects. Well, this is only a very small selection, David. A very small selection. That's right. How many projects on average each month? Oh, three to four. Three to four projects.

**Dave Jones:** You're the only magazine in the world doing that, I think, really, to that frequency. Oh, yes. It's got to be. Well, they're a store still, and they're a circuit seller, but they're not doing the same sort of stuff as we do. I don't think they're as hands-on or as hobbyist-friendly or accessible, that sort of thing.

**Dave Jones:** EPE magazine in the UK, which, of course, is on sale in Australia, well, you can buy that if you will find it's full of Slip'n'Ship projects. Exactly, because they're republished. Which is done under licence. Yes. That's fine. Yeah. Terrific. Thanks, Leo. Okay, well, thank you, David, and all the best for the show.

**Dave Jones:** Excellent. Thank you, guys. Thanks.
