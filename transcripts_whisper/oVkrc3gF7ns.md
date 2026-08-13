---
video_id: oVkrc3gF7ns
title: Conducted Mode EMC Emissions Demo
url: https://www.youtube.com/watch?v=oVkrc3gF7ns
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 30, "2": 44, "3": 66, "4": 82, "5": 98, "6": 116, "7": 134, "8": 134, "9": 154, "10": 176, "11": 206, "12": 246, "13": 274, "14": 289}
---

**Dave Jones:** ...electronics in the UK, and Julia Moses from Wirth Electronics Australia to showcase the EMI debugging demo based on Wirth EMC demo boards, power supplies from Rodent shorts and our latest MX04 oscilloscope. So yeah, to begin the demo, I would like to invite Glenn to brief about the experimental setup or the demo setup.

**Dave Jones:** So what we have here is a good design, bad design of a boost converter. So it's normally running about 300 kilohertz switching frequency. So we've got an input voltage of 19 volts, and we're boosting up to 24 volts. That will go through to our electronic load.

**Dave Jones:** So I'll be drawing around about 420 milliamps off of that. What we're doing is actually hooking the demo board up to a Cisco 25 listen. So this has been developed in partnership with Wirth Electronics and Rodent shorts. So what makes this listen slightly different compared to what's typically on the market is it has dual outputs.

**Dave Jones:** So basically we can measure both in effect like live and neutral line or positive and zero volt line. Benefit with this, coupled with things like the MX04, is that what we can actually separate out is from a conductive emissions plot, both the common mode noise and differential mode noise.

**Dave Jones:** So by using this listen, we can help identify when types of solutions are applicable. And this is partly what we're going to be doing today. So what we'll start off with is our bad design. So I'll switch on, hopefully if I'm doing this right, switch on the power supply.

**Dave Jones:** And I'll now set the load to draw the 420 milliamps. What we can now see on the screen. So we've basically got in time domain. So we're actually measuring the noise coming, being conducted through the power supply into the listen being extracted off channel.

**Dave Jones:** Let's have a look, probably channel A. We can now see in the time domain and the reciprocal in the frequency domain. So we're looking at things like conductive emissions, so from 9 kilohertz to 30 megahertz. So yeah, as far as a design engineer, I might not be keeping my job too well because I've got all this harmonic noise running through.

**Dave Jones:** So this is basically now my noise source. And what I want to do is now implement what a good design looks like. So what do we mean by a good design? So we've got a second circuit on the board that I'll now switch in.

**Dave Jones:** And this will have improvements to things like common mode chokes, differential mode filtering, better layout. And what we can now see, it will be the end result. So let me just power this down, switch it over to a good design, power back up and set my emissions.

**Dave Jones:** So if you now look on the screen, we can actually see in the time domain, we have virtually suppressed all that noise that was coming off the bad design. And so this is implementation of things like common mode choke, better layout. We can see the resultant conductive emissions has significantly dropped.

**Dave Jones:** We've probably dropped it down by about 20 to 30 dB in certain frequencies. So that's that. What I can now also do is go a step further and introduce a secondary common mode choke and differential mode filter on its input. So let me just power this down.

**Dave Jones:** Okay, so I've switched it back onto the bad design. And my output is on. So what we can actually see is we've got a reference versus our current at the moment. So basically what we have is this particular new board that we've now introduced has a mains rated common mode choke.

**Dave Jones:** So it's made of manganese and corn material. So this will typically operate around about sort of nine kilohertz up to probably about one to two megahertz in frequency, along with a X capacitor. So this would be doing some more low frequency filtering. Whereas when I now, if I now power it down and switch in the good design as well as so in effect, I've now got two stage EMI filter.

**Dave Jones:** What we've got is the reference trace. And now we've got the real time measurement, along with both the filters, and we can see that we have now significantly attenuated any of the EMI noise that's now being conducted from that bad design through to the LISN and then being measured on the MX04.

**Dave Jones:** So once again, we're just trying to show a very practical demonstration here, coupled with Rhoda Schwartz's equipment, how you can do at a bench level DC power supply filtering on a noisy source. Thank you.
