---
video_id: 9lC-k5yU9W4
title: EEVblog 1671 - Beware of Multimeter Continuity Latching
url: https://www.youtube.com/watch?v=9lC-k5yU9W4
source: youtube-asr
---

**Dave Jones:** Hi, in a previous quick video looking at a new experimental firmware version for the BM786 multimeter, like making a change to the continuity tester in it and how it changed to a basically from a latched version to an

**Dave Jones:** unlatched version. Brymen actually took a look at the video and they said, "Ah, you're not comparing the latest production version." And sure enough, I wasn't. So, this was the one I was actually comparing, 609, and that is actually um rather old. This is the

**Dave Jones:** latest one that's actually shipping and this is version 11. And this is the experimental version 12 here. Now, they have actually changed the continuity in this version 11 compared to the version 9 here. So, let's take a look at it,

**Dave Jones:** shall we? So, let's switch them all on and we'll go to continuity, continuity on all of them, okay? So, this is the older one that I was testing and you'll notice that is and if I leave the probes just like

**Dave Jones:** gently touching like that, ooh. Okay, let's try the 11 version 11 the firmware. It is quicker. It is definitely quicker. Still, I would still call that I would still call that very fast latched. It's not quite It's It's a little You

**Dave Jones:** might think it's itchy and scratchy, but it's not it's not as itchy and scratchy as I would expect. So, let's go to this experimental version over here with the different thresholds and Woah. Is it my imagination or is the backlight

**Dave Jones:** not as coming on and staying on for as long? Let me go back to here. They had already changed a good lot of that in between version 9 and version 11. There you go. And let's see where the lower threshold is. Oh, oh, there we

**Dave Jones:** go. It's actually, yeah, 280. Oh, looks like we have to go to three 300 before we get out of that. So, yeah, it is still very high at the 290 ohms there. So, 88 87 86 85 And equal Yeah, about 282 ohms there.

**Dave Jones:** Yeah, so, it's still high. So, that's what they tried to fix on this experimental version. And if we do our pulse test here, 99.9% duty cycle here. So, it goes low for only 0.1% of the time. This is the

**Dave Jones:** shipping production version 11. And sure enough, they've actually significantly changed this since that version 9 version. There you go. It still does it at 99.999%. What is that? 10 microseconds or something? And we go over to the that

**Dave Jones:** new threshold 12 version over here. It's basically basically the same. I'm not sure you can barely see the backlight. You can see the backlight flashing there. So, it's basically identical performance to the shipping version 11. There you go. So, yes,

**Dave Jones:** Brymen are indeed correct when they say that this new experimental version 12 with the lower threshold continuity threshold value is basically exactly the same as the current shipping version like this. Now, Brymen said that they actually made this

**Dave Jones:** change from 9 to 11 or really from 10 to 11, but I'm not sure if I shipped any version 10 units. So, I'm not exactly sure when that happened, but they basically said they made that change from the version 9 to a the faster

**Dave Jones:** version 11 to be in line with the BM um, 869S meter. And I don't have one of those and not a recent version anyway that I can actually uh test that with. So, um yeah, apparently this was a deliberate change.

**Dave Jones:** This is not an issue with this new experimental version. They have actually successfully changed the threshold value on version 12 here to a lower value, which most people kind of agree is probably a better uh optimal value than the like 280 ohms

**Dave Jones:** that you get on this one or whatever it is. And they said, uh sorry, but no, we don't have enough firmware um space available inside these things. They're very limb memory limited. Don't have enough firmware space available to make

**Dave Jones:** it user selectable. Um they probably would if they could, but they said they don't um have it available. So, sorry, can't be done, but uh yeah, there you go. That's interesting. Change that back to 99% and there. That's the 99%

**Dave Jones:** one. And um yeah, there you go. So, let me know what you think about the lower threshold value. I know some people are going to prefer the higher value, others are going to prefer the lower. I'd say low

**Dave Jones:** low is probably better in the scheme of things, but I have had uh practical applications um in industry where the higher value is better. So, it would have been great if it was user selectable, but unfortunately, um they

**Dave Jones:** don't seem to be able to uh have the space available to do that. As always, Brymen are on point. Uh it wasn't a bug. They had a specific reason uh for doing this and uh changing it to match their

**Dave Jones:** um 869S. So, why did they make this change from uh the version 9 to version 11 here? Well, it has to do with uh uh practicality of making continuity measurements in circuit when you've got capacitors in circuit because remember,

**Dave Jones:** as soon as you apply a voltage to a capacitor, it acts like a short circuit. And if you're quickly probing across your PCB uh you know, trying to uh trace down shorts or whatever, you don't necessarily want those pesky capacitors

**Dave Jones:** getting in the way cuz they can give you a false beep like this. So, I've got the old version here. Now, Brymen have said they basically designed it around a 0.1 microfarad value. So, with this version 9, we'll find that if we probe Now, I've

**Dave Jones:** already charged it up. So, we would can go the other direction like this, you'll see that it actually beep, right? And we'll go the probes back the other direction, you'll see that it beeps. And that can give you a false,

**Dave Jones:** you know, continuity reading in the circuit. And you can waste a lot of time doing that. Now, if I use the new version 11, and this will be also the same with version 12 as well, we should get

**Dave Jones:** nothing. OR OH, OH, I HEARD THE FAINTEST OF faint beeps there. Faintest of faint beeps, but you don't certainly get it latched, and you don't get the visual continuity thing there. So, that can make a big difference in circuit. Now, I'll just to

**Dave Jones:** pick a random board here and see if we can actually get something here. So, as a practical demonstration, I'll I'll use this board here. We've got a a voltage regulator here. So, let's just probe two points here around the regulator.

**Dave Jones:** Boom! Look at that. That is picking up, right? We're getting essentially a false continuity reading there. Not every time, but there you go. Yeah, look, right? False continuity reading like that. Now, if you put it in actual ohms

**Dave Jones:** over here, right? It's like 1.75 K. So, there's obviously capacitance in that circuit that's briefly causing this because it's continuity it's latching response is so fast, it picks up, you know, micro seconds, you know, small amounts of capacitance in there, and is

**Dave Jones:** then pulse effectively pulse stretching that and giving you a false reading. But, if we do absolutely identical probing over here and see if we get it. Nope. I'm in the same Oh! I heard the faintest of faint beeps

**Dave Jones:** there. You definitely wouldn't have picked that up on the microphone, but it's certainly there's no visual continuity at all. They're exactly the same points. And no, see? There you go. So, that's how practically this new firmware, this newer firmware, can eliminate um

**Dave Jones:** potentially eliminate, not in all cases of course, greatly depends upon the uh circuit and what sort of capacitance and other active electronics is in there and stuff like that. But, yeah, um it can help prevent um sort of those uh phantom

**Dave Jones:** uh continuity uh pulses which can waste a lot of your time cuz you might hear it and see it um visually. Oh, there must be a short there, but it's not. It's capacitor in your circuit. So, there you

**Dave Jones:** go. Um so, that's actually a a decent upgrade, I think. Even if you're not that you know, a a fan of the faster sort of semi-latched, almost itchy and scratchy. It's not quite. It's not as worse as um meters that I've seen that

**Dave Jones:** have absolutely no latching at all and they sound really screechy. But, uh this one is just super super fast while trying to eliminate uh those voltages. Out of curiosity, I want to see what some other meters do. Of course, the 0.1

**Dave Jones:** microfarad value here is just basically an arbitrary value, you know, the old school bypass capacitor value, I guess. I You could argue that in modern times it should be higher like a microfarad or something, but it doesn't really matter.

**Dave Jones:** It's just a reference point to actually design around and that's what uh Brymen have chosen. So, let's do the old school BM235 and nothing that direction. Nothing. Okay. So, it's not fooled. The new BM2257, let's give that a whirl.

**Dave Jones:** Nothing that direction. Ooh, we got a beef uh brief beep there. Yeah, so it looks like it's very short, but technically it Oh, no, it didn't didn't actually beep then. So, it's Oh, right on the border. So, you

**Dave Jones:** know, of course, the design of these meters is slightly different, of course. So, you got to tweak the values depending on the specific meter. So, it looks like they've gotten reasonably close to the BM 786 there, but still

**Dave Jones:** that one does beep. Let's try the 121. 121. Nope. And Nope. No, it's not fooled at all. Double-check the in-circuit that we had before, and no, no, it's not fooled. And out of curiosity, and what were we getting? 1.7k before. Of course, this is

**Dave Jones:** going to It's not a real resistance value. It's just whatever the meter happens to be. Is this similar? Yeah, 1.8k. The old store what? The old faithful 87V here. Let's go. Nope. And Oh, yes. 87V does it. Yep. Yep, that's very consistent. Yep.

**Dave Jones:** UT1273AX, which is an itchy scratchy one. It is not latched. So, nothing there. Oh, the slightest. But yeah, no, you really wouldn't expect it if it's not latched. If it's not latched, it's one of the advantages of not latched. You're probably not going

**Dave Jones:** to get anything from a cap like that because like it just charges up too quickly. And the ANENG AN8008 and the ANENG Q1 here. It is latched, so but I wouldn't expect it with such slow continuity to capture that.

**Dave Jones:** Nope, not at all. Once again, not particularly quick, not the fastest one out there, so I'd be surprised if this actually captures it. It is an issue with really fast latching continuity testers. Nope. So, that is one of the advantages of slower meters.

**Dave Jones:** You're not not going to get fooled by in-circuit capacitance, at least. It's a trade-off, isn't everything? So, there you go. Latched versus non-latched continuity testers and tweaking of their latching time, which is essentially the pulse stretching time. Then,

**Dave Jones:** yeah, you've got to design it around some sort of reference, whether or not you want to design it so you get rid of, you know, 0.1 microfarads like that. But, when you go to a big value like this,

**Dave Jones:** um nope. You know, you're you're going to capture that every single time with a big value cap. So, what can you do? Nothing, really. It's a big trade-off. Even meters like this one, you're going to get fooled by those

**Dave Jones:** big-ass cap values. You know, nothing you can do about it. So, there you go. I hope you enjoyed that video and found it interesting about latched versus non-latched and pulse stretching and all the rest of it. It's just something to

**Dave Jones:** be aware of when you're doing continuity testing. And let us know in the comments down below, which approach do you prefer? Yeah, it'd be nice to have it infinitely selectable so that, you know, you can choose whatever you want for any

**Dave Jones:** particular probing scenario that you're doing. But, basically, every meter out there is like they just make the design choice to do whatever. And, well, you've got to live around those limitations, really, for your multimeter. It's just something to be aware of. So, let us

**Dave Jones:** know, latched versus unlatched fanboys, what are you? Leave it in the comments down below. Anyway, if you like that, please give it a big thumbs up. As always, discuss down below. And you can discuss it on the EEVblog. And you can

**Dave Jones:** get my meters at the EEVblog.store, cuz I don't plug it enough. So, I'm plugging it. Catch you next time.
