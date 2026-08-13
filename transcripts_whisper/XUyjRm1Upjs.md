---
video_id: XUyjRm1Upjs
title: That moment you realise the Schematic & PCB don't match
url: https://www.youtube.com/watch?v=XUyjRm1Upjs
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 17, "2": 33, "3": 53, "4": 69, "5": 85, "6": 97, "7": 109}
---

**Dave Jones:** And it's that point in the video where I thought I was going insane. But, no, it turns out, Murphy has bitten us on the arse. Look at this. I was wondering why I was measuring, like, you know, the voltages weren't off and then I started, they were off

**Dave Jones:** and then I started to check grounds going to the chip and the grounds didn't match up and everything. Like, over here on the schematic, pins 19 and 20, right? I was using those as a ground, I was tracing that back as a ground reference, and I was wondering why

**Dave Jones:** 19 and 20 weren't shorted. Wah, wah, wah, wah. Look at the silkscreen. 19 and 20 over here are LED standby and key into. Um, it's 14 and 15 that are actually ground. The schematic does not match the PCB. Yet, this is the schematic for this model

**Dave Jones:** number, but maybe they've got a different rev board or something. Unbelievable. Anyway. Oh, shh. The moral to that story is, like, when you notice something weird, follow it. Like, I noticed that, oh, okay, the voltages like, I wasn't getting the voltage I wanted.

**Dave Jones:** Like, I was measuring there's another pin on the chip, which is VP, and I was like I was measuring that and I wasn't getting it. I was trying to trace it back because you need a ground reference, of course, to measure it. And I was choosing the connector over there and it wasn't right.

**Dave Jones:** And then I thought, something started going down the rabbit hole. Well, is this ground? Have I got a dry joint? Is there a bad link? Or, you know, in one of the links, because this is all single-sided board, so there's all these links in there

**Dave Jones:** it's got to jump or the ground has to jump over. Maybe one of those is bad or something. So I was following it back and I could not buzz the ground pin of this. I ultimately went, right, I'm checking that the ground pin of this

**Dave Jones:** goes over to the ground here. And it didn't. And then I kept following and then I realized, d'oh, the pin-out's wrong.
