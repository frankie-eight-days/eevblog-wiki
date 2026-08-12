---
video_id: 5v8qX9PrjnA
title: Brymen BM257 vs BM235 Multimeter IR Serial Protocol
url: https://www.youtube.com/watch?v=5v8qX9PrjnA
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 57, "3": 73, "4": 86, "5": 99, "6": 123, "7": 134, "8": 143, "9": 154, "10": 168, "11": 178, "12": 196, "13": 211, "14": 228, "15": 251, "16": 263, "17": 279, "18": 298, "19": 305, "20": 317, "21": 330, "22": 341, "23": 353, "24": 372}
---

**Dave Jones:** Hi, I just wanted to do a quick video looking at a potential hack for the EVBlog BM235 meter to give it PC com capability PC serial RS232 communications that you could get on the BM257 and the two meters are all very equivalent meters almost equivalent functionality except this one does have the PC coms on it and this one doesn't.

**Dave Jones:** But interestingly if you've seen the teardown, I wanted to see if it was possible look like it might actually have a pad in there for an infrared diode that we could infrared LED that we could hack into convert this to RS232 capability because these two do actually use exactly the same case and you'll note that it does actually have those two holes in there are for the RS232.

**Dave Jones:** Okay, so we've got ones over here and they actually have if you have a look in here let's have a look ta-da behind the curtain they oh yes, they both have the transparent holes in there.

**Dave Jones:** Everything's the same. They've actually changed look the piezo transducer is now on the board with the BM 235 and quite a few significant changes inside. There's less internal wiring.

**Dave Jones:** They don't have a shield like they do under here. You can see see that plastic uh insulated shield down in there. They don't have that. They've changed the organization of the amps jack and the milliamp microamp.

**Dave Jones:** They swapped those around and they've put the chipsets on the top. The chipset has changed. You can tell that when a multimeter chipset changes by the fact that now they've got volts AC and DC on the same range whereas this one here had volts DC and AC separately, and how all those ranges configured will be different depending on which multimeter chipset it uses.

**Dave Jones:** And I do not know which multimeter chipset they use in here. It's Brymen branded, so they won't tell me. They just say no, it's proprietary. Sorry, we're not going to tell you.

**Dave Jones:** Anyway, so they've got the multimeter chipset. It'll be like a variation of one of the commercial off-the-shelf ones or an identical off-the-shelf one, but I don't know exactly what one is.

**Dave Jones:** Haven't traced out the pinouts or reverse engineered it or anything. And we've got an LCD driver up here. So, you know, there are significant changes, but interestingly, look, here we go.

**Dave Jones:** That's Where's my poker? Here we go. There's our little infrared LED there. Notice that it only transmits. It does not have a receiver, even though there's a hole in the case.

**Dave Jones:** There's two holes in the case, one for transmit, one receive. It only transmits the data. That's it. And interestingly, the EE blog BM235 has a pad here for a diode.

**Dave Jones:** Look at that. And it looks to be in almost identical location to line up with that hole. Pretty darn close. So, I thought, "Aha!" But, if we actually get in closer here, sorry, I'm going to film this in one shot.

**Dave Jones:** Couldn't be bothered putting my macro lens on. So, hopefully you can see that. The LCD driver chipset is the HY2613C. And you'll note that that trace goes up there, goes to a cap, which then goes down to ground, and it goes around over to pin four down there.

**Dave Jones:** And yeah, that thought, "Well, okay, maybe it does that." And the cap didn't make sense, but Brymen actually released the RS232 protocol for this thing. And you know, it's a it's a weird ass protocol.

**Dave Jones:** I might have to link in link down the uh PDF down below, but it's available on their website. And this is for their 6,000 count digital multimeters. And um what it does is it basically in like instead of outputting an RS232 number like as a string or or whatever, it actually outputs the LCD digits and it maps them.

**Dave Jones:** Which is rather unusual. So, you've got to um decode that output. What a pain in the butt. But obviously, that's how they implemented it in the or the manufacturer of the chipset implemented it.

**Dave Jones:** So, that's the That's the protocol for the output. Really unusual. So, it kind of made sense that this thing actually connected up to the LCD chipset. Aha, does the LCD chipset actually have a built-in, you know, um RS232 output that outputs this protocol with all the segments?

**Dave Jones:** It was looking promising, but Take a look at the data sheet here for the uh QFP-48 package, which is the one we've got here. Sorry. Pin four on the C model, there's different models here.

**Dave Jones:** Uh the C model it has like a back light inverter and one doesn't or something like that. Um it's the LCD power voltage control input charge pump power output.

**Dave Jones:** So, that's why there's a cap on there because it's a charge pump output. It needs a capacitor on there to do that. So, it's got nothing to do at all with the um any of this uh protocol.

**Dave Jones:** It's just a coincidence that it happened that they've left a pad here. Why they've left a pad for the diode, I'm not uh entirely sure. Maybe there's another mode for the um charge pump or something.

**Dave Jones:** Anyway, so they've got that going to a rail there, whatever rail that is, um a positive rail, presumably. So, there um yeah, they just left that part out. Just happens to be in the same location.

**Dave Jones:** So, what I'm afraid I don't even have to probe that one with the scope to know that's not going to work because well, we have the data sheet unless No, there's just no other option.

**Dave Jones:** There is no unless. Okay, it's a charge pump. It just Yeah, a coincidence. So, there you go. 6-minute video to tell you that. Sorry. Um yeah, this thing has no secret uh serial output hack, I'm afraid.

**Dave Jones:** Bummer. Catch you next time.
