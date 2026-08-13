---
video_id: -bPGrSSaXhE
title: Goldshell LBC LBRY ASIC Miner Teardown & Troubleshooting
url: https://www.youtube.com/watch?v=-bPGrSSaXhE
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 14, "2": 38, "3": 57, "4": 74, "5": 97, "6": 120, "7": 132, "8": 158, "9": 172}
---

**Dave Jones:** Hi, I am replacing the, or swapping, the controller boards, as you asked. This is the faulty unit, so I've called it number two here, and I've noticed that this capacitor here is bulged. It's got a bulge in the top, and this capacitor here is completely...

**Dave Jones:** looks like the bottom seal has completely gone on that. It's hard to see in there, sorry, but it is... it looks like that capacitor may have failed. Anyway, I've... so I've labeled this board number two. There it is there, controller board number two.

**Dave Jones:** So this is the faulty unit, and this is the good unit over here. So I've called that unit number one, and I've labeled it number one and number one down there. So what I'm going to do first is put the number... the faulty controller board into the good unit,

**Dave Jones:** and we'll see what happens. All right, I've now got unit number two, so the faulty controller board in the... with the good... the working hash board. So I'll apply power and see what happens. Yeah, instantly it comes green like that, whereas the faulty board became red.

**Dave Jones:** I will double check that the... that the actual miner works, but I'm pretty sure it won't... it will work just fine, because the fault was... was that the red LED came on permanently, but now the green comes on. So that indicates that this controller board is fine.

**Dave Jones:** So what I'll do now is I'll put the good controller board number one into the faulty hash board number two, and we'll try the same thing. Oh no, it's red now. Is that because I have not plugged in the ethernet, probably? And yes, that's

**Dave Jones:** confirmed. I plugged in the ethernet, and 30 seconds later it went to green. So I have no doubt that one is working. Okay, I've now got the good controller board number one in the... with the faulty hash board number two, and let's power that on.

**Dave Jones:** And it's red. It... well, it almost flickered to green for a split second there, but no, it's staying red. So this was a previously working good controller board. So it's almost certain that this hash board is faulty, and given those capacitors on there,

**Dave Jones:** that is potentially what the issue is. But I also noticed, and I'm not sure if it's going to show up here, but the soldering on some of the MOSFETs down there is not very good. So yeah, whereas it's better on the other unit.

**Dave Jones:** So I'm not sure if that's anything to do with it, but soldering is not good on those at all. But anyway, yeah, it looks like maybe some capacitors have failed on that board, and it's definitely the hash board confirmed. Thanks.
