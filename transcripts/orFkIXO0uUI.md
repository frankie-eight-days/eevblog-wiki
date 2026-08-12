---
video_id: orFkIXO0uUI
title: EEVblog #631 - How To: Soniq LCD TV Repair Part 2
url: https://www.youtube.com/watch?v=orFkIXO0uUI
source: youtube-asr
---

**Dave Jones:** Hi. In the previous video, we looked at uh troubleshooting and attempting to repair this uh heap of crap uh Sonic brand uh you know, one hung low brand LCD uh TV. And well, we pretty much uh ruled out uh most of the power supply

**Dave Jones:** and your traditional uh failure points with the electrolytic capacitors. There was nothing wrong with those. I measured rails and scoped it and uh got it with the meter. And everything looked fine. But, it seemed very intermittent. Now, a

**Dave Jones:** lot of people uh responded with lots of comments. So, thank you very much for that uh tips and all sorts of things. And as to be expected, everyone sort of had like a different opinion of what was wrong with this. Some said, "Oh, it's

**Dave Jones:** beyond economical repair." And well, it certainly could be, but upon replaying the video, I noticed something that I didn't notice before and that I didn't notice at the time cuz I wasn't actually looking at it. And uh a couple of people also uh noted it as

**Dave Jones:** well. They they saw it on the video. And it was when I actually uh when I was playing around with the thing, I touched the TV like this and it changed. It the image actually vanished or or flickered

**Dave Jones:** or did something. So, um that indicates that there's some sort of physical it was too much of a coincidence, okay? That I just like I was playing around with it and I was look going towards the back like this and uh you know, I just

**Dave Jones:** touched gently we touched the front of it and the image vanished. So, really that indicates that there's a physical uh component to this fault. It doesn't mean it's the only fault, but certainly a physical component and it's most likely

**Dave Jones:** the main fault. A physical component in terms of some sort of connection or something like that. And that makes sense when you're talking about one of the symptoms for this thing was that it got uh it was getting audio. Audio was

**Dave Jones:** working fine, but we're getting no picture. That was one of the symptoms of various uh things that were going wrong and very, you know, flickering in the display and stuff like that. Certainly could be a bad contact. Now, we ruled

**Dave Jones:** out the power supply, of course. So, the process the power supply is basically powering all of the processing uh engine down here in the main board and through that through to the LCD panel up the top here. So, uh really I'm going to rule

**Dave Jones:** out any connections to do with the power supply. All the power supply go into the processor board here. So, what's left? Well, the only thing left is this multiway ribbon cable here going from the processor board up to this board up

**Dave Jones:** here, which upon investigation is uh apparently called a T-con board, a timing control board. And that uh basically uh splits out or handles the timing and splitting of the signal going from the main processor board to powering the LCD display up here. I've

**Dave Jones:** seen ones where they uh this sort of stuff is embedded on the main top. There's a whole top board up here, but we've basically got two big multiway rib flat flex ribbon cables going here. So, I'm going to suspect that it's one of

**Dave Jones:** those ribbon cables. First thing I'm going to do though is power this thing on, see if I can reproduce the fault uh based on just physically tapping or, you know, physically flexing the display. Or maybe I'll get in here with my poker and

**Dave Jones:** I'll have a poke around on the an insulated poker, of course. Uh poke around with the flat flex ribbon cables in there and see if anything happens. Let's give it a go. Now, the thing just powered up and uh

**Dave Jones:** the I got the power up sound and everything like that, but I didn't uh I'll turn my LCD around here, but I didn't get uh anything on the display. So, let me start having a poke around.

**Dave Jones:** So, like it like it to be like completely gone now. That's what I said at the end of the last video. And uh the backlight's on, and of course all the power supply stuff is still working, but sort of give it a flex.

**Dave Jones:** No, I think it's sort of permanently permanently gone now. So, I don't like Look at that. It was nice It was nicer when it was intermittent. Now it's like completely failed. So, that's good and bad. Uh um In this case, though, it's

**Dave Jones:** it's kind of bad from the aspect of me trying to play around with the thing. Anyway, what I'll do now is I'll reseat these uh flat flex connectors cuz these can be a pain in the ass, uh these flat

**Dave Jones:** flex connectors. So, I'll reseat those and uh turn the power off first to reseat them and then uh try it again. So, yeah, these can actually be a real problem. So, what you do is you just lift up the

**Dave Jones:** connector on these. Some of these work uh differently to others, but this one is uh designed to pop out like that. And these multiway ribbons, they can be quite troublesome. Like the the actual ribbon itself, like these things inside

**Dave Jones:** never break. Um virtually never do. So, but the connectors can be a bit dicky, especially if they're pulled in uh with somebody not using the right tongue angle. Um So, anyway, let me uh let me reseat that sucker. And is it in?

**Dave Jones:** Uh sorry, my fingers are in the way here. You won't be able to see anything, but let's push that back in and reseat that sucker there. And I'll just re-power it step by step, so I'll know if it comes good now, I'll

**Dave Jones:** know which one it actually is. So, the backlight come on there, but no no boot image. There we go, so it wasn't that connector. Actually, just as a little aside, this is a good example of capacitor dielectric absorption. Now, what I've

**Dave Jones:** done is I've disconnected the TV, okay? So, that main capacitor, as I explained in the last video, is uh still retaining a ton of charge, okay? There's no bleed resistor across that, so that's going to still going to have a couple of hundred

**Dave Jones:** volts on it easy, and it'll take, you know, it could take tens of minutes for that to actually decay. Now, as I said, you can use a multimeter with the low low impedance voltage measurement, usually designed for eliminating ghost

**Dave Jones:** voltages and stuff like that, but you can use it for safely discharging a capacitor like this, because it's low impedance. So, we'll get in there, and you'll probably see the voltage shoot up quite quickly. It might even overload.

**Dave Jones:** And then, yeah, overload, 40 volts, boom, and then drop down to zero volts. Now, look, I'm holding the probes on there, okay? So, this capacitor is now, you would think, discharged. Look, 0.1 volts, okay? But, due to the phenomenon of dielectric

**Dave Jones:** absorption, cap There we go, it's discharged to zero, okay? Went to within 0.1 volts there. All right, so what we'll do now, it's like a minute later, I'll switch it over to volts DC, okay? So, with the high impedance input,

**Dave Jones:** instead of the like 10 meg input impedance, instead of the low input impedance of a couple of K, which we discharged that capacitor with. We saw it discharge to zero, but watch this. I mean, this is a significant time later.

**Dave Jones:** Look at this, it's recovered to 2.9 volts, and increasing. That is dielectric absorption, okay? We'll do it again. Here we go.

**Dave Jones:** There we go. I just charged the thing up. We'll change it to low impedance mode. We'll do this. Boom. There we go. It's discharging and we'll do it straight away now. Okay? It's completely discharged. Look at that. Let's make sure it goes down to

**Dave Jones:** 0.0. Come on. Ah, near enough. Good enough for Australia. Here we go. And Look at that voltage creeping back up. That's dielectric absorption, the phenomenon of a capacitor to recover from its charge after it's been discharged. And I'll leave that to you

**Dave Jones:** to go Google and have a research on dielectric absorption cuz it is quite a interesting subject. So, well worth looking at. Now, this connector up the top here, I've taken that out. It's a different type. It's a physically got a

**Dave Jones:** connector mounted on the end of the flat flex like that. It's got some shielding tape over that. So, I'll just reseat that back in and see if that makes a difference. And I'll also just might as well just reseat these suckers as well.

**Dave Jones:** But, hey, I'll do it step by step. No, still no boot image. Bummer. Next up, we got the top side connector. Absolutely tiny and these things are a real even more of a pain in the ass than the one down on the processor board. So,

**Dave Jones:** I mean, you know, there's not much that can go wrong on this uh T-con board here, really. I mean, there's a couple of passive bypasses. Oh, does I don't know. Hang on. Uh sorry about the shaky image here. I can't uh

**Dave Jones:** get my macro lens on my tripod. Does that look like a fuse? Hmm. Well, I've taken this little T-con board out here. It was stuck on with uh double sided tape held into a little plastic holder on there and it's an LG

**Dave Jones:** display. So, presumably it's an LG panel in here. So, LG display TL 2336ML. Couldn't get any data on that off the bat. But, anyway, it is There you go. LG Display Co. Limited and designed in 2009. Probably reused in a whole bunch of

**Dave Jones:** different panels, no doubt. So, um this takes the differential Here we go. Takes the differential pair LVDS signals coming in. There you go. And basically does timing and control stuff and has differential pairs coming out that go to the main panel and drives the

**Dave Jones:** panel. But, look at this. Look at this. Look what we have here. We have ourselves When you have When you see a a flat flex cable like this and you got multiple pins in parallel like we do here. They're That's obviously the power

**Dave Jones:** input pin cuz they need, you know, a fair bit of power. These flat flex and these connectors don't have much current capacity per pin and per wire. So, often it's a very common to parallel them up like that. In

**Dave Jones:** this case, we got four passing through a cap not one but two zero ohm resistors there and they go into what looks like There you go. A poly switch or fuse that then it goes through to the bypass caps

**Dave Jones:** on here. So, let's measure that sucker and see what we get because I tried playing around with the connector up here and that didn't fix the issue. So, let's measure that puppy. And Hello. I'm making contact there. There that's

**Dave Jones:** my probe shorted out. Hello. I think we have a file that is open and that sucker ain't going to work. That's why we're now getting no picture at all and no amount of prodding and poking and shaking and

**Dave Jones:** trying to coerce this thing into working will get that to work. We've got ourselves a blown fuse or poly switch on the board there. Yeah, I'm not sure offhand TC not sure of the code there but Jeez, yep, that ain't going to work.

**Dave Jones:** Need to fix that. Now, I'm not sure of the exact brand of that but I did find a reference to TK in a little fuse data sheet and it is actually fuse not a poly fuse or a poly switch like a resettable

**Dave Jones:** fuse. I think it is just a fuse. That's why it's a blowing like that. I'm not sure why it would have blown whether or not it was, you know, just a dodgy part that was going intermittent and eventually failed. I don't know or the

**Dave Jones:** intermittency could have to do with the fact that it was something to do with with the flat flex connections and then I don't know some surge current eventually took it out. I you know, I don't know but anyway,

**Dave Jones:** that that marking is for according to little fuse 1 and 1/2 amps. So, I don't have one of those to hand but I can probably budge something in there. That's for sure or hey, just to get it up and running

**Dave Jones:** short it out. Well, the best I had to hand was a axial fuse like this. I just budge that in there. That'll get us up and running. All right, let's give it a whirl again and plug it in.

**Dave Jones:** I've reconnected the board up and uh Let's give it a go. Hello, McFly. There we go. Hey, there we go. Look. Look. Well, not surprising cuz that thing did uh did blow. So, I don't know why it actually did that,

**Dave Jones:** but look at that. There we go. We've got our image back. Sorry I can't uh get the camera on a good angle. Okay, let's uh have a poke around here and uh I'll turn the LCD around so I can actually see it.

**Dave Jones:** It's good to have a mirror or something like that for this sort of thing cuz you don't want to go sort of mhm sticking your head around the front like this with your tongue at the right angle trying to poke at the back. Uh not that

**Dave Jones:** great as I said insulated poker, but uh uh all right. Hey, look at that. I'm touching that ribbon cable at the top. That's the one on the bottom of the T-con connector.

**Dave Jones:** Okay, that's the top of the T-con connector. This is the ribbon cable down on the processor board. There you go. So, it is Look at that.

**Dave Jones:** Son of a gun. I'll hold that in. I'll physically hold that in. Hold it and release. Ta-da! Look at that. Ha-ha! It is an intermittent connector. That one with the actual connector on it. It's not the one It's

**Dave Jones:** not the actual flat flex one. It's the one with the um with the physical sort of, you know, semi-latching connector on there. But, I think I think we've solved our issue. I'm not sure why that fuse went. Uh no idea. Um I'm not going to fuss

**Dave Jones:** over that at this stage. Uh we've got ourselves a win. So, there you go. It does look like that one is the culprit. And yeah, I was like poking that connector down in and down in there like that. And I can actually see a

**Dave Jones:** reflection off the back wall of that thing actually going off and on. So, there you go. Just physically poking that a bit can cause that. Of course, um you'll get thermal issues with this as well as the as the thing heats up, you know, a

**Dave Jones:** slight expansion in uh stuff and so that can uh cause an issue both mechanically as part of the thing and also perhaps thermally. So, um because you're going to get that heat rise of course from the uh from the big power supply right down

**Dave Jones:** under here. So, there you go. That was the issue. Um well, I'm going to say it is anyway. Um um I'm going to call that one uh done and dusted. I'm going to have a bit more uh play around with it um to sort of,

**Dave Jones:** you know, uh see exactly. I don't think it's a reflow issue. I don't think it's a solder joint on there. I did look at this under the uh Mantis microscope and it looked pretty good. So, I'm not going

**Dave Jones:** to like reflow that board or anything like that. It's not uh it's not worth it, I don't think. But uh yeah, I'm going to certainly have a um bit more play around with this with this connector here. Got to be careful cuz it

**Dave Jones:** is right next to the uh power supply here. So, you know, um best to dick around with that with the power off if you physically going to get your little uh fingers in there and have a play. But

**Dave Jones:** there you go. I'm going to call that one found and potentially fixed. Awesome. And I've had a bit more trouble with this thing. So, I've just sprayed some uh contact cleaner up into there and the contacts as well. I don't trust this

**Dave Jones:** bloody connector. It's uh man, just looks and feels dodgy. Don't like it. It doesn't lock into place properly and uh no. Now, I've actually found the thing is more reliable once I've actually got it out and free hanging like that. So,

**Dave Jones:** maybe I'm I should really get in there, tape up, you know, bog up that connector something like that and maybe re-feed it back. I could even put like a mylar sheet over the power supply some sort of insulating

**Dave Jones:** sheet over the power supply and just I don't leave it free hanging, I guess. Yeah, once I do up that connector and everything can't see why I couldn't do that but or maybe even feed it back under once I've

**Dave Jones:** um really fixed up this connector and, you know, taped it up, maybe bogged it up properly. I don't know, but yeah, it's seems to be going okay now with it free hanging. So, it's definitely the issue. Now, there's one viewer who did actually

**Dave Jones:** suggest that a common issue with these things is as the backlight ages it starts to interfere with the LVDS lines and one way to solve it is to put shielding tape like all over the thing like completely cover the thing to

**Dave Jones:** isolate it. I I don't know. I don't necessarily buy into that one. But, yeah, I mean we're certain because we were getting like physical poking, you know, I could physically make it come and go like that and well,

**Dave Jones:** yeah, proximity not a huge deal. But, anyway, yeah, this thing is essentially fixed back up and running works very reliably now. Really taped up, you know, I've put tape on there to really physically hold the connector in place and it seems to work

**Dave Jones:** really well now. Ta-da! That's a win. It's back together and I'm all happy and I've, you know, banged it around, done all sorts of weird and wonderful stuff and it seems fine. I don't have the uh um And, Raspberry Pi plugged in anymore,

**Dave Jones:** but there you go. Menu, everything's fine. Bang, bang, bang. Boop, boop, boop. That's was just That wasn't me. That was just the timeout on the menu. So, everything's fine. Looks like we had at least a dodgy flat flex

**Dave Jones:** one of those flat flex interconnect connectors in there. Real pain in the butt on that T-con board and that blown fuse. I'm not exactly sure why the fuse blew, but replaced it with the same rating one and everything's hunky-dory.

**Dave Jones:** That's a win. Catch you next time.
