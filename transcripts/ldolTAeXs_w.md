---
video_id: ldolTAeXs_w
title: EEVblog #1297 - Turn an LCD into E-Paper!
url: https://www.youtube.com/watch?v=ldolTAeXs_w
source: youtube-asr
---

**Dave Jones:** Hi, for those who aren't subscribed to my EEVblog 2 channel and you really should be because you'll miss interesting art stuff like this. And so I'll link in my EEVblog 2 channel down below and at the end if you're not

**Dave Jones:** subscribed, set the notification bell and all that sort of stuff. Anyway, I had to check the date for this but back in December 2017, I set up this long-term LCD experiment. A lot of people have been asking me over the

**Dave Jones:** years what's the update on this LCD experiment that I did. Now, this came about because of my LCD tutorial I did, how to actually drive seven-segment displays like this and I'll link that in and the end and down below as well cuz

**Dave Jones:** it's a very interesting tutorial on how to drive LCDs and you basically you have to drive them with a AC waveform. You've the polarity has to alternate between the common and the segment. So, this is why you need like a special LCD driver

**Dave Jones:** to drive LCDs but I can't remember why at the time but anyway, I decided to set up this experiment to see if a typical LCD like this would actually die, like how long it would last if you actually drove it incorrectly with just

**Dave Jones:** DC. I E on the common pin, you put ground and on the segment, you just put 5 volts and you just left it there. Like this is totally against the recommendations of all the LCD manufacturers because LCDs of course

**Dave Jones:** liquid crystal display. There's actually liquid crystals inside there and depending on the electrostatic polarity of it, you can either turn them on the individual segments which are filled with the liquid crystals on or off and you can't just keep DC on there.

**Dave Jones:** But it does actually work in quote marks. You can actually drive it cuz this is the experiment that I set up. I'm actually driving this with an Arduino Uno down here. I set up two examples for this. I had I think it may

**Dave Jones:** be in my driving tutorial I I had the Arduino set up to drive it correctly with the reverse polarity. You would just reverse the pins on the segments and you could actually drive an LCD properly. But of course you run out of pins pretty pretty

**Dave Jones:** quick to do that. But you can certainly do that. So I decided to set up this experiment. This one has been was running since then. It was running for a couple of years until like I moved here and then the flood happened or

**Dave Jones:** something. And it hasn't been running since. So a lot of people have been asking what's the update cuz I'm I'm driving this with just 5 volts DC. So the common's just connected to ground as you can see down here and it just

**Dave Jones:** drive it just puts 5 volts in any of the LCD segments. So rather than just turn them all on I thought I'd just have it boringly count um from zero to nine and then reset. And it's actually been as you can see it

**Dave Jones:** works. But when I powered this up like I've had no results over the last couple of years. But when I powered it up I just got it out of storage to like see if this thing like to basically just put it back on

**Dave Jones:** power and I noticed something unusual. Check this out, right? It it just counts like normal. But if I actually remove the power from it they I noticed that the segments stayed there. Now I covered this in my original

**Dave Jones:** video where you can actually get that. It's like electro it's a capacitive charge like capacitive charge build up. You can actually get segments to stay on for a quite a substantial amount of time. But it that's not what that's not

**Dave Jones:** you they would have faded by now. But that's not what's happening in this particular case. It it doesn't matter like we can just stop it on any segment like this and it actually it the segments just like permanently

**Dave Jones:** stay on. This is unbelievably bizarre. This is like opposite to what I uh sort of expected to happen because uh from kind of some stuff I read, if I remember correctly back in the day, I was like, "If you drive these with DC, then the

**Dave Jones:** liquid crystals can get uh they get bogged up, lethargic, so they can't actually stay on or, you know, you just can't drive these segments anymore. Like, it just kills the LCD uh basically." And I don't know, I haven't

**Dave Jones:** driven this with like a higher frequency. I haven't modified the firmware to go higher in frequency, but this is this is bizarre. It'll just reset like this, and as far as I know, there's I can't say maybe you can see at

**Dave Jones:** home, but there's nothing there's like Hang on. Wait. I'll pull it out. There we go. And that there's seems to be no like lag or fade in those segments at all. So, like, it's almost as if this is like

**Dave Jones:** taken on the properties of like a e-ink e-paper type display, where it doesn't require power to actually maintain the image. Isn't that cool? This is totally not what I expected. Um but this seems to be well, in this

**Dave Jones:** particular case with this particular LCD, this is a uh Lumex one. I'll try and link in the data sheet down below. You can buy it on Digikey, and it's a nice big seven-segment uh display. But this particular one seems to be now

**Dave Jones:** acting like an e-ink or e-paper display, where you do not need power to actually And I've left this off for ages. So, I'll just leave that off. Uh and it'll it'll just stay like that. It's absolutely incredible. So, I don't know

**Dave Jones:** what the heck heck is causing that. So, if there's any uh liquid crystal uh experts out there, please let us know. But isn't that cool? So, probably um do some experiments on your own. Like, I obviously it might

**Dave Jones:** take a long time uh for this effect actually happen for this LCD to e-ink conversion to actually e-paper. What do they call them these days? E-paper or e-ink? Anyway, it might take a while to get this to happen. Maybe there's some way to

**Dave Jones:** accelerate the process or something like that, but definitely try and experiment with like driving maybe if driving at a higher DC voltage or something. I don't know. You might be able to accelerate the process, but clearly the liquid

**Dave Jones:** crystals are doing something really bizarre. Like they're just staying on. They're I I stay like I I just No. I I have no idea what's going on. So, I'm going to hand this over to the audience, but that

**Dave Jones:** that is really cool. Can we convert an LCD into an e-ink or e-paper display? Hey, so that could be really cool if you've got like a a favorite seven segment display that you want to use and you want to

**Dave Jones:** like use the properties of e-ink which it retains the image with no power. Um so, yeah. Anyway, I left this like overnight and it's was still holding the thing on there and holding the image on there. It's just

**Dave Jones:** incredible. It seems to have converted it into some form of e-ink display. So, that could be really useful. Anyway, I'm going to have to let me know in the comments down below some more experiments you want me to do

**Dave Jones:** with this like I drive at high frequency and you know, maybe the high-speed camera to see if there's any lag in the segments at higher update rates and and things like that. I don't know. There's a bit of work involved in doing

**Dave Jones:** something like that, but isn't that weird? Anyway, that is bizarre. So, please if you know heard of this effect before, I couldn't find any info on it. So, let me know in the comments down below. So, anyway, I hope you enjoyed that. If

**Dave Jones:** you did, please give it a big thumbs up. As always, discuss down below and also over on my library channel I'm about to hit 15,000 subs over there. Absolutely fantastic. Catch you next time.
