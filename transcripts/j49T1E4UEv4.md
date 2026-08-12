---
video_id: j49T1E4UEv4
title: Oscilloscope Alias Followup
url: https://www.youtube.com/watch?v=j49T1E4UEv4
source: youtube-asr
---

**Dave Jones:** Hi, in a quick video on the second channel which I'll link in if you haven't seen it. I just was playing around with different brands of oscilloscopes and showing to see it well to see if they alias with a 10 MHz

**Dave Jones:** signal. And Jason Long, I think it was in the comments, thank you, actually commented, is that actually aliasing or is it just a like a sample beat frequency because it's 10 MHz and the internal oscillator is 10 MHz or the and the

**Dave Jones:** sample rate will be in this particular case it's 2 gig samples per second. But anyway, let's reproduce the problem. So I've got a 10 MHz signal there. There you go, 10 MHz. Let's wind the time base down and I'm in auto memory depth by the

**Dave Jones:** way, I believe. Let's double check. No, I'm in 1 meg. Let's put on auto cuz sometimes some scopes will have like anti-aliasing but only in auto mode. Let's go down. Let's go down. Let's go down. If we go

**Dave Jones:** down to uh 2 5 So once we're down to 5 milliseconds per division, okay, we start to get that aliased signal. And there you go, it's 2 it's 2 hertz there. Okay? Or yeah, 1 point it's 1 1 hertz. There we

**Dave Jones:** go. But the hardware frequency counter is still measuring 10 MHz cuz that's actually there's hardware in there. It's probably inside the FPGA or something like that to yeah, to like feed in the signal directly. That's what a the advantage of

**Dave Jones:** a hardware frequency counter. So that's still displaying 10 MHz there. But you can see it's displaying a 1 hertz signal. But you notice that the sample rate is 5 meg samples per second. Sure enough, we are actually feeding in

**Dave Jones:** an exact 10 MHz signal. Well, let's actually change that, shall we? Let's actually change that over to let's go 9 MHz. Okay? So 9 MHz, whoop, it changed there. We now got 9 MHz and it's still aliasing there. So let me go down 8

**Dave Jones:** meg. Oh, kilohertz. No, 8 MHz. 8 MHz, still there. 7-MHz, oh, still there. 6-MHz, and you're getting the idea, right? But, I expected it to actually change if we do it to not possibly not do this if we

**Dave Jones:** select an oddball frequency. So, let's go 9. I don't know, 1 2 3 MHz, okay? 9.123, boom, there you go. We're not aliasing anymore because it does actually have to do with a sample rate, okay? Which is now 5

**Dave Jones:** megasamples per second. Oh, it's it's auto, it's gone to auto roll mode now, which is not Do we want We don't really want a 20 seconds per division. Okay, so it's not doing it anymore because we had an odd

**Dave Jones:** We're using an oddball frequency. So, let's go to I don't know, um 8.1 MHz. And boom, see? Instantly starts to alias. So, that's see? So, what's 8.1? I don't know. Get your confuser out. 8.1, figure out why 8.1's doing it at 5 megasamples per

**Dave Jones:** second with 1 megpoints. Um and 2 seconds, right? It's It's doing it, right? So, 8.1, 8.2 MHz. 8.2 MHz is still doing it. 8.123, do we have to get off? Yeah, see? If you do the .123 thing, it works. So, 8.1

**Dave Jones:** So, 8.1 doesn't do it. Oh, sorry, 8.1 aliases, okay? But, 8. Wait, let let's go 1 1. Okay? 8.11, way, there we go. There we go. That's interesting. So, 8.105 MHz and you guessed it. Changes the ripple frequency. That's not the correct

**Dave Jones:** term, but you know, stick with me, right? And yeah, but 8. 8.1 and anything oddball like 8.123 will actually like smooth that out so to speak MHz. 8.1 to any See, it doesn't do it anymore. Interesting, huh? So, if we

**Dave Jones:** actually stop that and stop is different, by the way. Look, it actually displays what is displayed on the screen is actually quite significantly different. We can actually go back, right? Wait, there we go. There we go. There's your

**Dave Jones:** There's There's your problem, right? There is no modulation on the signal, but it's showing it because it's an oddball and you can go into the math behind it and you can go into the sample theory and you go into the whole works,

**Dave Jones:** right? Because this does not have an anti-aliasing hardware filter in it. It's not doing that based on the sample rate. Whereas I think the Keysight does actually do that. Um So, anyway, so what else can we do? So, let's run that again. Let's actually

**Dave Jones:** go back to our uh What was it? 10? Let's go back to our 10 MHz, okay? Let's go back to our 10 MHz there. Okay, and we can Whoa, we really aliasing there. Let's stop, okay? It's going to

**Dave Jones:** definitely show up when we stop it. Still shows up like that. But and if we zoom in that No, it's definitely So, let's go What was it? 8.1 MHz. 8.1 MHz. Stop. And Whoa. So, nine nine did it, right?

**Dave Jones:** Let's go nine. no, 9 MHz. Didn't 9 Yeah, 9 meg did it as well. Okay, so let's go out. Let's go out. Come on. There we go. Right. That's beautiful. I love it. Look at that. And if we stop that,

**Dave Jones:** see, it's actually got um it's got the high frequency stuff in there, but that is probably going to be Whoa. See, you can see that really Whoa. And if you scroll through that, you'll notice that that will if we change the horizontal

**Dave Jones:** position, you'll notice that that Well, it just becomes No. That's very different, isn't it? Whoa. Okay, even though I'm zooming in at the same point. Oh, look at that. Just drops the amplitude like that. Funny business, huh? So, yeah. So, it's interesting. So, yes,

**Dave Jones:** it will actually have to do with um the input frequency that you've got. And it's going to show up worse if you're exactly on a multiple of uh the sample rate. But you see, like we were like like at 9 It doesn't at 9 MHz with 2 meg

**Dave Jones:** samples per second, so we're not you know, it's not like uh what's you know, and one sample and one meg points of memory, and what's like what's going on? Anyway, I'm not going to I'm not going to wrap my head around the numbers and

**Dave Jones:** try and sit down with pen and paper and figure it all out, but uh yeah, there you go. It's interesting, huh? So, it does actually make a difference, and you can set it, you know, 9.12345 MHz like that, and

**Dave Jones:** it's not going to apparently, on the display anyway, it's not going to alias. So, we can go like right down like that. Let's go to 1 second per division. Okay? So, this is 9.123 MHz, and we'll stop that,

**Dave Jones:** and we'll go in, and we can still see a sine wave, but it thinks it's 2.5 kHz, right? So, yeah. And will that yeah, that'll probably be based on the sample rate, right? And then the multiple of the frequency you

**Dave Jones:** put in, etc. And then see, it does like zoomed in like that, it looks okay. And it starts to do funny business, and it starts to do funny business like that. So, there's something there's something up with the like the the display

**Dave Jones:** algorithm there. Because it's like it's just chopping off points like that, right? Cuz cuz there's only one to one time base difference between like two time base differences between that's 200 microseconds per division, right? So, that's you know,

**Dave Jones:** 10. So, that's 2 milliseconds total, right? And I only have to go like that, and there's you know, there there's your 2 milliseconds, right? You're seeing all these little peaks and troughs in there, right? Whereas I go in in that 2 milliseconds

**Dave Jones:** in in two divisions there is equivalent to that, which shows a perfect sine wave, right? Let me zoom in on that so you can see it, okay? So, this is this is 2 milliseconds total for the entire screen, okay? And the sine wave looks

**Dave Jones:** absolutely perfect, right? But you go out to this is now 2 milliseconds like that, and you see look, see? So, it's all it's all coming out. Right? It's all funny business, but yes, it ultimately will it's still I would still call this

**Dave Jones:** aliasing. But how it implements itself on the screen in the hardware, you know, in the the once again, the the the the stopped display algorithm might be different to the real-time display algorithm as well. So, you know, and that looks to be sort

**Dave Jones:** of the case here because we run that, right? Look, right? And then if we stop it in there because we're stopped at a different sample, right? It's going to go, "Hey, it's going to be different again." There you go. Look at that. Look

**Dave Jones:** at that. Wow. Look at that. One time base difference between those. Funny business, right? And every scope's going to do this differently. Um so, yeah, but there's clearly no anti-aliasing filter in the scope, and I think most scopes

**Dave Jones:** don't have one, I think. Uh jeez, I don't know. Is there a comprehensive list anywhere of But I think the Keysight is supposed to have it at least the Keysight on the 10 MHz signal, which is kind of like, you

**Dave Jones:** know, worst case, um then it it doesn't do it. So, yeah, it's uh it's pretty schmick. So, it does the bit, but uh it doesn't have when you zoom in on the Keysight one, I'm not sure if I showed in the previous video,

**Dave Jones:** but it does like show like sampling jaggies and stuff like that, but it just the whole point is that it doesn't show you a different frequency to what you've actually got. Um and that that is the whole point of, you know, aliasing is

**Dave Jones:** that it shows a different different frequency signal. So, what do we got? Yeah, we got uh So, yeah, 10 MHz like that. And yeah, we zoom out like that, and it will show a physically different frequency. So, if you captured that, you know, if

**Dave Jones:** you weren't paying attention or whatever, and you capture that signal, sure, it's a sine wave, and what you've got is a sine wave, but it's, you know, completely different frequency. So, you can come a cropper. Aliasing's a uh thing you've got to

**Dave Jones:** watch out for, not just in scopes, all sorts of sampling systems. Um and then you can get uh you know, frequencies folding back into the you know, you have to get into the whole signal theory thing, and frequencies

**Dave Jones:** fold back into range and stuff, and can do all sorts of weird and wonderful uh things when you're doing, you know, analysis beyond just looking at a simple uh waveform and stuff like that. So, anyway, it's very interesting stuff, but um

**Dave Jones:** yeah, it's nothing inherently wrong with the Rigol scope, I don't think. It just doesn't have an an any alias in filter in like it seems like most scopes don't. So, there you go. Interesting. Anyway, thanks for the comment. Prompted this

**Dave Jones:** video. Catch you next time.
