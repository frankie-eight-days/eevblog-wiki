---
video_id: muMjiao5i0k
title: Rigol HDO4000 PSU Teardown
url: https://www.youtube.com/watch?v=muMjiao5i0k
source: youtube-asr
timestamps: {"0": 0, "1": 27, "2": 60, "3": 90, "4": 121, "5": 139, "6": 177, "7": 206, "8": 220, "9": 256, "10": 284, "11": 305, "12": 320, "13": 334, "14": 365}
---

**Dave Jones:** Hi, just a quick second channel video back on the Rigol HDO 4000 series oscilloscope. I completely forgot to tear down the power supply in it. And well, yeah, I thought that's a first, isn't it? Anyway, um cuz it's usually one of the first things I look at. Yeah, yeah, I looked a bit difficult to get out, so I thought I'll leave it until the end and then the end came and I forgot and I was excited that I'd finished the video and I went to edit it. Anyway, um here it

**Dave Jones:** is. It's actually a rather than just you know, like a bare board like stuck on some standoffs in here, it's actually screwed into the side like this and a post down here. So, rather than just like a bare board and then have like a custom shield over it, it looks like they've gone for like and just an off-the-shelf brick, a Mornsun brand. I've certainly heard of them. And it's an LM15020B12 for those playing along at home. So, it's like they've just taken it and off-the-shelf module. They haven't

**Dave Jones:** actually commissioned anything specific because well, they don't need anything fancy. As I said, like there's just like presumably it's set to 12 volts. I haven't actually measured it. And it's just one of those adjustable output voltage jobbies and mains in and it's just it's all done for you. But usually they you know, companies try and reduce the cost a bit by actually getting something at least like you know, custom tailor cuz you might be able to save a few cents that way. But they've they've gone with it just an

**Dave Jones:** off-the-shelf brick and it seems to meet their requirements. So, they went yeah, no worries. So, we'll have a quick squeeze. And of course, dumb ass me didn't engage brain. I just saw two screws on the side and I unscrewed them and the dull I I little bracket fell out inside because that was holding one of the power devices. That had nothing to do with actually clamping on the lid. So, yeah, we can actually have to get in here like this and taking it off they've got the clips in here. I

**Dave Jones:** can probably push in there and get it out but yeah, though yeah, it turns out it's got little clever hooks in there and stuff like that. So it actually just slides off the end like that but yeah, there was the that would ruin your day if you had that flapping around in the breeze in there.

**Dave Jones:** Yeah, you'd really come a gutter. So yeah, that is designed you see that they've got the gigantic like gigantic silicone condom on there. Yeah, they've completely covered the package and that's just designed to physically hold pressure on there and just even though they've got that's possibly thermal adhesive in there not entirely sure but they've got it on those ones up there as well and that plate just holds those in place. Anyway, forgive me for not unscrewing all that. I just couldn't be bothered. Anyway, here's the mains input

**Dave Jones:** over here big bridge rectifier there and the two big DC filter caps. What brand have we got? I don't know. It's under the bottom. I don't want to take it off 105° C rated. I don't know RTM in brackets model number B3A not sure. Maybe I can search for that but I can't see any of the custom transformer in there but yes, it's all wrapped for our protection.

**Dave Jones:** That's some serious common mode choke action happening there. I really like that. Oh, look at that. That's just that's a Bobby dazzler really beautiful. I love the exposed just having the exposed coils and the look look at the green core in there.

**Dave Jones:** Thing of beauty joy forever. Anyway, it looks like a bunch of wire class caps going down the ground all the nice isolation shots slots. Everything's hunky-dory. We've got filtering on the input and output of our common mode choke. There's a varistor on the input there. That looks like a fuse, little line fuse on the mains input and the output filtering is, you know, pretty minimal here. It's just got some polymer they look like polymer. None of that electrolyte rubbish. They look like solid electrolyte and you've got to make

**Dave Jones:** Why would you go with these and then have that one as well? Different values, different functions, but yeah, it's just funny that they've gone with an old school vented one there and that looks like solid ones here, but it's all she wrote. Like I won't get the board out. There's SMD circuitry on the bottom, no doubt because like this is going to have some secondary side regulation here. So I would say that there's going to be circuitry on the bottom. Oh, all right, there you go. I know people just

**Dave Jones:** complain if I don't do it. There's the secondary side. Oh, look at that. They got all the thieving squares there. Somebody somebody had fun. It's only a three pin jobby on there and oh, look, you can see the glue. You can see the glue holding it well that were supposed to be holding down the components that aren't there.

**Dave Jones:** That's what that little thing in the middle there is. Hopefully you can see that. That is some They've applied the glue, but they haven't applied the part because well, presumably it's not needed on this model, but anyway, um these are not switching on the output.

**Dave Jones:** These are just diodes. You can tell they're only two pin and it looks like so there's only a sub 23 here, but you can see some optocoupler feedback here. In fact, it's coming. You can see the traces running all the way around there.

**Dave Jones:** All the way, follow the money. They're running to the output here and there's an optocoupler there which does So they're effectively doing primary side regulation there by the looks of it, but anyway, that's pretty groovy. I like all the isolation slots. That is a well-designed uh power supply. I you know, the cap brands, meh, whatever, but uh yeah, they've actually used a uh complete off-the-shelf module. That's interesting. I think that's possibly the first time I've ever seen that in a scope teardown. Please tell me if

**Dave Jones:** I'm wrong down below, but um yeah, it's quite unusual to just literally use like an off-the-shelf um you know, package. Usually they, you know, save a few cents by custom designed it in some way.
