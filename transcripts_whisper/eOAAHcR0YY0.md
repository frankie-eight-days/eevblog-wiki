---
video_id: eOAAHcR0YY0
title: BlackMagic ATEM Mini Pro Audio/Video Delay Measurement
url: https://www.youtube.com/watch?v=eOAAHcR0YY0
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 16, "2": 36, "3": 56, "4": 68, "5": 84, "6": 105, "7": 117, "8": 141, "9": 161, "10": 178, "11": 194, "12": 210, "13": 230, "14": 247, "15": 263, "16": 283, "17": 299, "18": 315, "19": 327, "20": 340, "21": 360, "22": 384, "23": 400, "24": 425, "25": 445, "26": 458, "27": 478, "28": 490, "29": 510, "30": 526, "31": 542, "32": 555, "33": 571}
---

**Dave Jones:** Hi, just a quick second channel video. I'm just analyzing the audio on my Blackmagic ATEM Mini Pro. And by the way, just today, Blackmagic, they've seen my video, it's upside down, all the elec- is it? Yeah, all the electrons are going to fall out.

**Dave Jones:** They've seen my videos, and they like my stuff, and they dropped by their latest, ta-da! The Blackmagic ATEM Mini Pro. Blackmagic ATEM Mini Pro Extreme, or Extreme Pro. Mini Extreme I- sorry, Mini Extreme ISO. There's so many variations of this thing, it's crazy.

**Dave Jones:** Anyway, thank you very much, Blackmagic. Yes, I will be doing a teardown of this, because I've actually maxed out, I'll have to link in the videos, I've actually maxed out my ATEM, my 4-channel ATEM Mini Pro, because I've got 2 microphone inputs and 4 video inputs, and even technically that wasn't enough.

**Dave Jones:** I had to actually disconnect one of them the other day to feed in my wafer microscope into it, camera into it. So yeah, I'm actually out of input. So anyway, yeah, I've got a new one, which has a lot more bells and whistles.

**Dave Jones:** So very cool, thank you very much. Yes, I'm floating Dave head because I'm wearing a green shirt. I just happen to be wearing a green shirt today, so sorry about that. But what I've done is a little test, because people, and I've noticed it myself,

**Dave Jones:** try to be, if I'm fussy about the video, I have actually corrected the audio sync in my editor, because there seems to be an audio sync between the microphone, because I use one of the microphone inputs, there's inputs on this thing, and over here there's 2 microphone inputs, and I use

**Dave Jones:** one of these coming from a shotgun microphone, another one coming from the wireless microphone. So that's where I get my main audio from, although this can actually record the audio from all the cameras as well, it's just that the shotgun's better, so I use the audio from that.

**Dave Jones:** And there's a delay between the HDMI video captured and the audio sync. Now, so I just shot some test footage here, and I just want to see, and I'm using chroma key, and you see how I've got picture in picture here? I thought, and a lot of people sort of

**Dave Jones:** confirm this, that you can't do green screen chroma keying using the picture in picture function. So to use the picture in picture function like that, you can't do chroma keying on a picture in picture. But that doesn't mean I can't do Talking Dave here with this thing, because I've

**Dave Jones:** actually, I have tested it, and it does actually work. You've got to use the, well, you've got to use the key over here, okay? So yeah, so it does actually work. I can do Talking Dave head on my ATEM mini pro, which is great, although I don't have the big green screen over on the

**Dave Jones:** bench that I do behind me here, and it's huge. Big green screen, and it's hard to move. But anyway, yeah, so what I wanted to do is just test the sync here. So what I've got is you can see, I can actually step frame by frame, and you can see

**Dave Jones:** there's a difference. Look, just going from this, you can see the main camera up here is like, it's, because this is only shot at 30 frames per second, or 29.97 frames per second for those playing long at home. But you can see that there is a difference between the main camera,

**Dave Jones:** it's the same image, but it's overlaying it. And it actually turns out it takes one frame, it's one frame behind. So the chroma key window, the keying window, is one frame behind. So there you go, it takes one frame to catch up to where it actually was in the main frame.

**Dave Jones:** So there you go, and you can even see my hand movement as well. So, yeah. So that is, I guess, that's the process in delay. I mean, they could have delayed, if they wanted to fix that in the firmware in this thing, they could have, or the HTML,

**Dave Jones:** the HTML in here, the HTML, HDMI and HTML, too similar. They could have fixed that in, like the PGA in here and actually delayed the main camera to see that they're, you know, to then have these synced up. But just be aware of that.

**Dave Jones:** There is actually, it looks like, precisely a one frame delay on the image. Because this image source is coming from the same source this is, but to get it overlaid like that in the chroma key in the processing, it's doing that delay. I should have done, I should have actually recorded

**Dave Jones:** picture-in-picture, actually, to see what the delay was. But anyway, I'd expect a similar sort of delay. It could even be more for picture-in-picture, I don't know. But definitely for the chroma key, and for Talking Davehead, there's one frame out. So that's interesting. The other thing I wanted to test is also

**Dave Jones:** here we go, is the audio sync. Because people have been commenting on this if I don't actually fix it myself manually, and I haven't been doing a clapper board to, you know, sync my normally don't sync my audio at all. I just capture it in camera.

**Dave Jones:** But with the ATEM Mini, there has been a slight difference. And people have noticed it. And I've noticed it too when I actually hear and watch and edit my videos. And I've tried to actually shift the audio and actually correct it. It's a real pain in the ass.

**Dave Jones:** So I believe there is actually a way in the control for this thing to set an audio delay or something like that. But I just wanted to measure it. I wanted to quantify this thing. So let's go over to this one. This one looks a bit

**Dave Jones:** nicer, right? So I'm using a clapper. And you can see that the audio has come through. Okay, the audio has come through first. Okay? So it looks like there is so this is a delay in the video processing side of things. Because as I said, the audio is coming from the microphone input.

**Dave Jones:** And I'm using a direct analog, I'm feeding my shotgun mic into a NASCAM, which is a purely XLR recorder thing. And that's all analog. So it feeds straight out. So there should essentially be no delay in there. And you can see that the audio arrives first

**Dave Jones:** and I haven't actually hit the hammer down. So let's count the number of frames. 1, 2, 3, 4, 5, bang! And then it hits. And there'll be a slight acoustic delay when it goes to the shotgun mic. But I'm not, you know, not that fussy.

**Dave Jones:** There's at least a 5 frame delay at 29.97 frames per second. So that's about 16.6 millisecond delay there. It could be either 5 or 6, you know. And you can actually see the difference in the chroma key there. You can see that the thing, that the whole board doesn't move

**Dave Jones:** a frame later. There you go. So there's the 1 frame delay. But it looks like there's either 5 or 6. So it's somewhere between 16 and 20 milliseconds actual delay on this thing. I assume the Mini Extreme will be exactly the same. And they could actually fix this because

**Dave Jones:** it's a known thing. They could actually, there should be, I was just talking to them today, there should actually be a checkbox in the control software for this thing. It's incredibly extensive. The stuff you can do with this is just insane. It's absolutely insane.

**Dave Jones:** This would be, this functionality would have cost, you know, $50,000 or $100,000 10 years ago. Now it's just unbelievable. The entire production studio. Anyway, they, yeah, they could have, they should know that system delay. They should know that precisely. I mean, I've done my measurements here

**Dave Jones:** from, you know, between 16 and 50 millisecond, 16 and 50 milliseconds, something like that. But they should know the precise delay. There should be like a checkbox to go, like, delay audio to sync up with audio input to sync up with the video.

**Dave Jones:** And yeah, I think that would be a really useful feature. Because obviously the audio is getting recorded before the video is being processed. And fair enough. You know, it takes time to process video. But there you go. That's evidence that that is yeah, 1, 2, 3,

**Dave Jones:** 4, I'm not counting that one, because it hasn't hit yet and it hasn't moved it. 5. It's at least 5. It's either 5 or 6 frames delay. Isn't that cool? There you go. So yeah, it'd be nice if it had that so I don't have to fix that.

**Dave Jones:** And I think there is. I think I haven't really have not looked at the, because the control panel you get for this thing which is all Ethernet based, it's all web based, is insane. I think I saw somewhere that there's an acoustic, there's some sort

**Dave Jones:** of phase delay or, you know, delay on the audio somewhere I can do it. So, you know, but it'd be nice if just there was a checkbox that just said, you know, fix it. And you didn't have to dick around with putting in some exact value.

**Dave Jones:** So there you go. That's very cool. Anyway, yeah, thanks again Blackmagic for dropping this bad boy off. I did actually need two of these, actually. I needed one for the microscope bench and I was going to have one here for my editing bench

**Dave Jones:** as well. So yeah, that's going to come in real handy. So there you go. I think that's cool. Measured. Quantified. Winner winner chicken dinner. Catch you next time.
