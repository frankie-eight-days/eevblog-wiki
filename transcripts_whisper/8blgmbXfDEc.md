---
video_id: 8blgmbXfDEc
title: New Dumpster Diving Monitor Score
url: https://www.youtube.com/watch?v=8blgmbXfDEc
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 18, "2": 35, "3": 51, "4": 67, "5": 90, "6": 112, "7": 132, "8": 147, "9": 166, "10": 186, "11": 207, "12": 224, "13": 247, "14": 264, "15": 281, "16": 297, "17": 315, "18": 333, "19": 350, "20": 364, "21": 381, "22": 399, "23": 414, "24": 428, "25": 443, "26": 457, "27": 475, "28": 495, "29": 512, "30": 528, "31": 543, "32": 558, "33": 574, "34": 594, "35": 614, "36": 629, "37": 647, "38": 664, "39": 680, "40": 694, "41": 713, "42": 729, "43": 745, "44": 758, "45": 776, "46": 795}
---

**Dave Jones:** Hi, it's dumpster diving time again, and this is my first score from the new office dumpster. No, the lab is still in the same location, but I do actually have a small secondary office now down the road where I do all my editing stuff like that, gives me more room here in the lab.

**Dave Jones:** Anyway, it's got another dumpster room I've got access to. Yes, it's in these commercial office buildings. For those who wonder where I get this stuff from, commercial office buildings, you know, multi-storey commercial office complexes, almost always, well, they must, because where do you put your trash?

**Dave Jones:** Otherwise, they have garbage rooms, which then get emptied several times a week. They have huge dumpsters in there, and they're always under lock and key or pass card access. So the general public can't access these things. Anyway, this is the first score from there,

**Dave Jones:** and I was actually clued up, somebody in the know actually clued me up that they do throw out some good stuff in that building. So I need to keep a regular check on that one. Anyway, we've got ourselves yet another monitor. The favorite thing that people throw out, the thing I've scored most often.

**Dave Jones:** Mondas, this is a Dell S2309W. It's a 23-inch monitor. It's from 2009, so it's reasonably old. But hey, it's a full HD 23-inch monitor, you know, quality brand, with a DVI input as well. I generally don't touch monitors these days, unless they've got a DVI input.

**Dave Jones:** And this genuinely comes from the dumpster, because look what it's on here. This, hang on, smells like some sort of hot chocolate that somebody's dumped. This did actually come from inside the dumpster, so I had garbage bags on top, and somebody's tossed their hot chocolate or whatever it was in there.

**Dave Jones:** So yeah, we'll clean that up. And I don't expect, I think 90% chance this is not going to work. People are not going to throw out a 23-inch Dell full HD monitor with DVI. I mean, I've seen crazier stuff thrown out, but hey, you know, when things are obsolete, they get new ones.

**Dave Jones:** You know, sometimes they just toss them out, not giving a thought. But most likely, this has got some sort of fault with it. And if you've seen my previous videos, you know what's probably wrong with it. Yeah, anyway, let's power it up. Here we go.

**Dave Jones:** Hey, hello? Hello? Oh, you saw it? I really have to get a, and wipe all this crap off, but look. Hey, this sucker's working. Well, at least it's getting that. I mean, I don't see, it doesn't look like it's been cracked or dropped or anything else.

**Dave Jones:** And there it is, S2309W. Wow! I was hoping this would be a repair video. So, probably not, unless it's got some sort of intermittent fault, it could. And if it is, it's most likely to be the capacitors in the thing, as you've seen in many previous videos.

**Dave Jones:** So, oh, I was kind of disappointed it works. I was, wow, I only gave that a 10% chance. I'll update you later, I'll start using this thing and update you if it continues to work. But, jeez, that's no worries whatsoever. Maybe we should just open it anyway, and have a look for the caps.

**Dave Jones:** So, yeah, we'll give that a go, but let me get cleaned up first. But, it works! Bummer. And we're in like Flynn, look at that, there's our Raspberry Pi, and that's looking quite good. I haven't quite cleaned all that, there's still a bit of gunk left in the corner.

**Dave Jones:** But, yeah, that seems to be working fine. It's been going for a little bit now, and there seems to be no issues. That's 100% working, don't see any missing pixels, dead pixels, nothing. No scan, you know, columns, row issues. That's a perfectly good 23-inch Dell Full HD monitor.

**Dave Jones:** Wow, and it's even got the original protective sticker. Thank you very much. And as is common with these monitors, there are no screws on the back, so you just have to lift up, prise up the bezel right around the outside. So that's really the only thing holding it in, just the plastic retention clips.

**Dave Jones:** And then the back just swings off once again with no screws. Very easily, they do this to minimize cost in assembly. It's just, you know, somebody doesn't have to sit there with the screwdriver and go But this one's actually particularly annoying, because usually then once you get inside here,

**Dave Jones:** you get screws holding on this back, and you can just get the shielded back off and access the circuitry. But this one has got screws in the side, and this whole metal thing lifts off, complete with the backlight connections. It's really quite annoying from a service point of view.

**Dave Jones:** And you can tell this is not a modern LED backlight. One, it's a cold cathode. One, they're going to take more power, but you know, you're not going to complain when you've got a working 23-inch full HD Delmonda. So you just disconnect the two cold cathode lamps here,

**Dave Jones:** and we should be able to lift this out. Ta-da! Oh, we're in. Nope, we're stuck. Got to get out the main display cable too. And then, once you've gone to all the effort to get that up, well, you get mooned! Look at this, the back of the boards!

**Dave Jones:** Geez! Now to access the top of these, just to inspect the capacitors to see if there's any bulges in them, you've got to now take out the main power supply board. Crazy! I much prefer the ones like, you know, we've seen many Samsung ones before

**Dave Jones:** and other brands, where, as I said, you know, you just lift off the top of this, and bingo! There's, you know, it's usually components up, and you can see all the components, you can inspect them in a couple of seconds, but this one takes a little bit more work.

**Dave Jones:** And I do like how they've got the silkscreen designators on the bottom of the board. They're in black, which is a little bit annoying. But then you can actually see the component values, so you can actually just measure some stuff from the bottom if you want.

**Dave Jones:** Here's the mains input, obviously, here's our common mode choke, that's an inductor, that goes up here, and we're going to have a bridge rectifier in there somewhere? Yep, is that our diode bridge? Anyway, it goes up there, looks like our main capacitor, probably in there like that.

**Dave Jones:** So what we want to do is just make sure it's not charged, I mean it's going to have a bleeder on it, but this is where the low impedance, the low Z function in your multimeter comes in handy, because it puts a couple of K across that capacitor,

**Dave Jones:** as well as measuring it at the same time. Eh, it's not measuring anything, so it's safe to disconnect this. And here's our main power supply board, very simple, although it's got some stuff on the back, and this is the primary side here, of course.

**Dave Jones:** Here's our mains input, as I said, it's got the requisite protection, a fuse, sometimes, hey, a fuse might blow for whatever reason, even just, I don't know, it could be a manufacturing issue or something like that, or it could be something further down the chain took it out,

**Dave Jones:** or just a surge from the main capacitor might take one out occasionally, but I haven't seen many of those. And we've got a common mode choke protection, and there's our main DC filter cap that we measured before, it's 450 volts, we'll take a look at the brand there.

**Dave Jones:** There's our diode bridge, and there's our isolation transformer, they've marked that on the silkscreen. So this is all the primary mains side, and this is our lower voltage secondary side. And then over here we've got our low voltage to high voltage drivers, there we go, there's a little warning, high voltage there.

**Dave Jones:** And you might notice the isolation slots cut into the PCB there, they've just routed out the isolation slots there. Very high voltage going to the cold cathode tubes over there. And, well, what do you do? That's what I'm going to look for. Any bulges in them, any leaks of course around the outside,

**Dave Jones:** nothing seems to be bulging on the vent at the top. There's nothing you can get down an angle, but usually you can, you know, see them. So they all look good, no worries. And then our primary, our main DC filter cap, there's nothing doing it there at all,

**Dave Jones:** so that looks all in good nick, all our caps look good. I think somebody, unless there's some other, I mean, you know, that doesn't mean that there's nothing wrong with these caps. You'd have to get your ESR meter on them individually to check the ESR of each one to see if they're any good,

**Dave Jones:** and you might want to go to that effort. Personally I'm not going to yet, because nothing's failed yet. So unless I put it back together, I use it for a week, and then it, you know, intermittently fails or something like that, then I'd get in there and get the ESR meter at 100 kilohertz measure.

**Dave Jones:** All of those caps, either in circuit or if you want to do it properly, you can actually pull them out, but in circuit you can use like a Bob Parker ESR meter, which I've shown before. But they look all in good nick, so no worries.

**Dave Jones:** I think somebody's just tossed this out, most likely now, because it was obsolete. Go figure, 23 inch full HD. And both the main DC filter cap and all of the secondary ones, usually there's a mix and match of brands, but not in this case.

**Dave Jones:** This is the Elite brand. There you go, it's upside down. All the electrons are going to fall out. You don't, I haven't very rarely see this one. This is actually Chinsan. They're a Taiwanese capacitor manufacturer. Not one of the mainstream, you know, they're not a Panasonic or a Nippon Chemicon,

**Dave Jones:** but hey, they're, you know, probably not bad at all. And they actually warn on their website about counterfeit Elite brand caps. So there you go. Yeah, look out for dodgy Elite ones. Hmm. Anyway, the fact that they're stuck with the one brand for all of their different types of caps,

**Dave Jones:** that's not all that common. Usually there's a mix and match, you know. They'll use the good brand ones where it matters, and some crappy brand ones from the Shenzhen market where it doesn't matter. But no, these are all at least consistent brand. That's, you know, reasonable quality assurance.

**Dave Jones:** So anyway, I can't really fault that unless I go measuring. And as I said, I'm not really going to bother. The digital board, that seems to be working, so I'm not even going to bother taking that out. This bugger all on it. Just a, you know, main LSI these days to do everything.

**Dave Jones:** So I'm going to whack this thing back together and just start using the thing for a while and see how she goes. So there you have it. A working Dell 23-inch monitor straight out of the dumpster with all sorts of crap tossed on top of it.

**Dave Jones:** And clean it up, and it works just fine. As I said, but I'll let you know. The verdict is still out. I probably should have measured those caps while they're in there, but ah, what the hell. I'll give it a bell. And no, it's now, probably most likely,

**Dave Jones:** this was just, became obsolete. They got a new system. I don't know, it might have come, I don't know, who knows. Maybe they got some new Macintosh thing with, you know, the building screen and everything else. I don't need this anymore. And they tossed it out.

**Dave Jones:** So I think this is probably the best monitor score I've gotten. I don't think I've gotten, I think I might have gotten a 22-inch before. This is a 23-inch full HD monitor, and it's a Dell, so quality brand, and it's working. Beautiful. There's no, like, issues with the backlight or anything like that.

**Dave Jones:** It seems to be working just a treat. It's not even full brightness. There you go. So, wow. I am happy with that. What a score. Ah, it's the Whopper. Love the Whopper. You've got to watch War Games if you haven't seen it. Anyway, what do you mean?

**Dave Jones:** You're watching the EEVBlog and you haven't seen War Games. Give me a break. And by the way, that's still running, boinking the background on all four cores there. You can see that running, and it's still playing a video, a YouTube video on my website.

**Dave Jones:** Yeah, it's a little bit jerky, but it still does it. All that stuff at once. Neat. But there you go. I think that's the best score we've had. Amazing what people throw out. Absolutely incredible. I mean, it's not worth a huge amount. What is it?

**Dave Jones:** I don't know, 100, 150 bucks used, working, or something like that. But still, 23-inch full HD monitor. That's a win. Catch you next time. Hi, guys. Yes, it's nighttime here. We're going on a stealth raid to the garbage room. Some dumpster diving and nighttime stuff.

**Dave Jones:** Secret squirrel. We found the PC Motherlode today. So let's go have a stealth raid. It's late at night. Don't think anyone will notice. Let's go. Here we go, folks. Let's go in before anyone sees us. Let's check it out. Now normally, you know,

**Dave Jones:** we'd be lucky if we find, like, a monitor in here.
