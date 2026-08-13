---
video_id: pW4HjuH1QRY
title: EEVblog #1046 - Mysterious Digital Voltage Doubling (LCD design)
url: https://www.youtube.com/watch?v=pW4HjuH1QRY
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 35, "3": 58, "4": 76, "5": 95, "6": 113, "7": 128, "8": 146, "9": 167, "10": 183, "11": 202, "12": 219, "13": 241, "14": 259, "15": 279, "16": 301, "17": 320, "18": 334, "19": 350, "20": 376, "21": 398, "22": 412, "23": 429, "24": 448, "25": 470, "26": 487, "27": 506, "28": 530, "29": 551, "30": 582, "31": 600, "32": 629, "33": 646}
---

**Dave Jones:** Hi, in my previous video, we looked at driving LCD displays, and I'll link that one in down below. And at the end, for those who haven't seen it, because it might not make a huge amount of sense, although I'll try to explain it without requiring the other video,

**Dave Jones:** this is a response video to some comments on the previous video. A couple of people couldn't quite figure out how we were getting the voltage doubling across here, because what we were doing is driving an LCD with a 5V digital logic, an XOR gate and a buffer here,

**Dave Jones:** just, you know, 5V TTL type logic. In fact, we showed an example with an Arduino actually driving the thing. And we magically got plus 5V and minus 5V down here for a total of 10V peak to peak. Where does the 10V peak to peak come from?

**Dave Jones:** They couldn't quite figure it out when you only had a single 5V supply. And effectively, just by adding some digital logic gates, we've magically created 10V peak to peak. How is this possible? So they thought, hey, maybe I actually got it wrong, or maybe the math measurement I showed it on the oscilloscope

**Dave Jones:** was actually wrong, and it was the wrong scale or something like that. No, that's not the case. It is, we do actually get 10V peak to peak across this LCD for a 5V supply. So it is actually really voltage doubling, and stick around, I'll actually demonstrate in a minute.

**Dave Jones:** Now let me actually redraw this and try and explain it a bit clearer, because a lot of people rightly don't understand this alternate phase thing and actually getting a difference or a subtraction function, a difference function of a waveform and how it can actually double the voltage.

**Dave Jones:** So let's say that we have a 74HC04 inverter, for example. You're familiar with those? I'll show you this on the bench in a minute that this actually does work. And it's powered from your typical plus 5V. So you've got plus 5V, so you've got your circuit ground down here,

**Dave Jones:** and you're feeding a 5V peak to peak square wave. And, of course, if you measure just the output here, we'll call that B, you get your 5V peak to peak square wave, right? It goes from 0 to 5, 05, 05. But if we probe across A and B, the input and the output here,

**Dave Jones:** because they've got alternate phases, because it's inverted, and this is exactly what we're doing with the LCD. We're effectively connecting the LCD across the input and the output of an inverter like that. You magically get 10V peak to peak. And this is not just some theoretical, you know, magical pie-in-the-sky thing.

**Dave Jones:** You actually get 10V peak to peak, because you're subtracting A minus B. You're getting a difference function, and that gives you double your voltage. But it's still not clear. I'll try and explain further. Now, let's say you've got an oscilloscope. Here's my crude oscilloscope.

**Dave Jones:** This is the screen, and we've got our positive and negative input, i.e., like, that's our B and C input, the probe positive, and your ground clip lead is your negative. Okay, so let's assume that we connect single-endedly to the circuit common here with your ground clip lead on your oscilloscope,

**Dave Jones:** and then you probe either signal A or B like this. What will you see? Obviously, you'll see exactly what you expect. A 5V, if that's the ground reference on your scope there, you'll see a positive 0 to 5V peak to peak signal, regardless of anywhere in your digital circuit you probe,

**Dave Jones:** because you're measuring everything relative to the circuit common. So, everyone's familiar with doing exactly this. But when you're talking about a difference signal, which we're looking at here, you've got to not think in terms of the circuit common. That is incorrect. When you're actually measuring a difference, one signal minus another signal,

**Dave Jones:** a differential probe, for example, just measures the difference between the two input lines. It's not relative to anything, and we'll demonstrate this on the bench in a minute. So, you've got to wrap your head around not trying to think in terms of relative to the circuit voltage.

**Dave Jones:** So, let's demonstrate this by taking the negative ground lead of our oscilloscope. Ground is not the same as circuit ground here, unless you actually connect it to the circuit ground. So, let's actually connect that up to point A up there, and then let's probe point B there.

**Dave Jones:** What you end up seeing here is this signal going negative. I use that term in quote marks because it's relative to the negative input here, not to this circuit ground. So, we'll try another way to think of it. If you use the ground as your reference, then what do you get?

**Dave Jones:** You get a waveform that switches between plus 5 relative to this and this reference, i.e. plus 5, 0. Right? So, that's your regular TTL signal that you're familiar with. But if you take your reference from up here, what happens? You've changed your entire reference.

**Dave Jones:** It's no longer relative to this ground. So, what if you move your reference, not from here going like this, but up to here like this? If you've got a 0 on the- just assume you've got a- imagine you've got a 0 on the input there.

**Dave Jones:** Well, the output's a 1, right? It's positive. So, it goes from 0 to plus 5 volts. But then what happens if you've got a 1 here? What happens to the output here? Well, it's got to go to a 0. So, it actually flips negative down like this.

**Dave Jones:** It flips to another level up minus 5 volts like this. So, it actually toggles, if you use this as a reference, it toggles between plus minus 5 like that. Effectively, you basically get a voltage doubling peak to peak. So, you're effectively going from like this to this.

**Dave Jones:** Your reference is now up here, and you're flipping like that. So, you're flipping the polarity, so it's got to be double relative to one of those pins. I hope that's clear. Let's just go to the bench and verify this. Okay, so what I've got here is a 74HCR14, which is a hex Schmitt inverter.

**Dave Jones:** It's a Schmitt trigger, it's just the same as the 04, but it's got Schmitt inputs. By the way, I powered that from 5 volts, and I'm probing the input and the output. So, I'm just feeding in a 1 kHz square wave, and we're getting the inverted out.

**Dave Jones:** So, channel 1, channel 2. So, let's have a look up on the scope here, and exactly what we get. This is exactly the same as the last video, basically. We've got 5 volts per division here, okay? So, 5 volts and 5 volts for both channels, and you'll see that they're one division.

**Dave Jones:** And, so they're 5 volts peak-to-peak signals, channel A and channel B. And you'll note that they're out of phase. When one's zero, the other's high, and vice versa. So, our LCD is hooked across those two pins. And, this actually gives you a good indication of what's going to happen.

**Dave Jones:** Your voltage reference, actually, instead of being ground here, we shift it up to here. And you'll note that it goes up by one division, and down by one division. And, if we look at our math function here, we've got A minus B, which is basically a differential function, and the scale is 5 volts.

**Dave Jones:** And the commenters said, oh, maybe I had the scale wrong, it's doing it wrong. But, no, look, it's actually 10 volts peak-to-peak. But, is there something funny happening in this telescope? Is this math operator incorrect? Well, we have a way to verify this.

**Dave Jones:** So, if you don't trust pesky math functions like this, I'm sure you'll trust an instrument, available on the EEVblog store, by the way, at a discount price if you put in the coupon code bargainprobe. Anyway, it's linked in down below. And on amazon.com as well.

**Dave Jones:** It's 100 bucks off on Amazon. Anyway, this is the EEVblog HVP70 differential probe. A very nice differential probe, if I may so say myself. It's a 10 to 1 division ratio, and this measures the true differential voltage between these two probes. So we can put these probes across the input and the output here,

**Dave Jones:** and we'll do that. We'll hook input, and I'll put it, for convenience sake, there we go. We've hooked it across the input and the output. So our voltage reference is no longer relative to our signal ground input here. These scope probes do not matter anymore.

**Dave Jones:** It's measuring the absolute differential voltage across the input and the output. And what do we get? Well, let's switch on channel 3, which is 5 volts per division, and let's have a look. Where is our signal? It's that purple one there. Ta-da! It matches absolutely perfectly to the software mathematical function that we had in there,

**Dave Jones:** which was the, you know, the A minus B. It's exactly right. 5 volts per division, it's 10 volts peak to peak across the input and the output. So if you put your LCD or anything else across the input and output of a digital logic gate like that,

**Dave Jones:** you get 10 volts, a real 10 volts peak to peak. Simply changing your reference, as I said, from, you know, basically a little ground down there, it's sort of like shifting up, so to speak. I know this isn't a 100% accurate thing, but it kind of gives you an idea of how changing your circuit reference ground can actually give you double the voltage.

**Dave Jones:** So anyway, I hope you found that video interesting. I hope that's an adequate explanation. If I come up with something, a better physical representation of how this actually works, or if you've got a better way to explain this, then leave it in the comments.

**Dave Jones:** Anyway, if you liked the video, please give it a big thumbs up, and as always, discuss down below. Catch you next time. Thank you.
