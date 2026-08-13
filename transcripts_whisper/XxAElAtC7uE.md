---
video_id: XxAElAtC7uE
title: EEVblog #785 - Sydney Maker Faire 2015 Interviews
url: https://www.youtube.com/watch?v=XxAElAtC7uE
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 32, "2": 42, "3": 62, "4": 71, "5": 91, "6": 103, "7": 111, "8": 126, "9": 146, "10": 168, "11": 186, "12": 207, "13": 221, "14": 237, "15": 253, "16": 272, "17": 287, "18": 298, "19": 314, "20": 329, "21": 344, "22": 361, "23": 373, "24": 394, "25": 410, "26": 422, "27": 443, "28": 457, "29": 473, "30": 485, "31": 500, "32": 511, "33": 528, "34": 541, "35": 551, "36": 565, "37": 575, "38": 588, "39": 603, "40": 620, "41": 637, "42": 653, "43": 663, "44": 678, "45": 695, "46": 713, "47": 731, "48": 747, "49": 761, "50": 780, "51": 798, "52": 818, "53": 842, "54": 855, "55": 871, "56": 888, "57": 901, "58": 919, "59": 935, "60": 952, "61": 966, "62": 976, "63": 991, "64": 1007, "65": 1026, "66": 1039, "67": 1054, "68": 1069}
---

**Dave Jones:** I'm here with Asfand from Aurora 3D. Tell us about what you guys do. Well, we build a 3D scanner that's powered by a smartphone. So, essentially it's the opposite of a 3D printer. What it does is you put an object in front of it, it's got

**Dave Jones:** a green laser, sweeps across the object and basically turns it into a digital model. Right. How does the smartphone work? Well, the big thing about the smartphone is that you have a camera on it, a really high quality camera, and today's smartphones are really, really powerful.

**Dave Jones:** So, what it does is basically as it scans across the object, the laser scans across the object, it uses the smartphone to essentially rebuild that object in 3D. So, it analyses that line as it scans across the object. Why a smartphone and not just a regular PC?

**Dave Jones:** Well, because smartphones, it's something that everyone has and it's a big factor in reducing cost. So, what happens with a 3D scanner is you need three things. You need a camera, you need a lot of processing power and you need a laser, basically.

**Dave Jones:** And two of the three are in a smartphone and pretty much everyone's got a smartphone. So, why not? By bringing your own smartphone, you essentially reduce the cost. Got it. Alright, show us the hardware. Well, here it is. This is the prototype. This is the prototype.

**Dave Jones:** This is the prototype. On a breadboard. Okay, so we've got our smartphone. So, the camera is, of course, facing the object here. Our object there. And it has to be on a black board? Basically, just to get rid of the background. It doesn't have to be, it can be any colour,

**Dave Jones:** it doesn't matter. Right, okay. Because we're in a public space, you know, just to get rid of the background. Yeah, but it can't be a complex background, otherwise it will... It can be anything. Oh, really? As long as it's stationary, it can be any background.

**Dave Jones:** Oh, stationary, so it uses motion to... Motion to detect. Right, got it. Exactly. Got it. What is on the breadboard? Well, the breadboard is actually, we've been using it for a while now. We have an Arduino on there, Pro Mini. We have a DRV8834 motor controller.

**Dave Jones:** And we've got a couple of voltage regulators. But, it's 100% Bluetooth now. That's our Bluetooth evaluation board. So, the Arduino is actually doing nothing at the moment. Right. So, it runs off an ARM M0. And everything is Bluetooth controlled from the smartphone. How did you get that here in one piece without it...

**Dave Jones:** We have a bit of experience with that now. Right, okay. Alright, so, show us. Can we see it doing something? You want to scan? Yes, absolutely. Yeah, let's run a scan. Alright, so what I'll do is I'll restart our app. Press scan. The object comes up.

**Dave Jones:** Essentially, the object is a little bit in the field of view. There we are. And we just press start. Go. And we can't see the laser. It'll come up. It'll come up. Give it a couple of seconds. And it's a green laser? It's a green laser.

**Dave Jones:** Oh, there it is. So, there we are. Scanning across. So, basically, we use a green laser because it's essentially twice as sensitive. Right. Most sensors are twice as sensitive to green compared to red or blue. So, we get basically better sensitivity. And, yeah, so what it's doing now is it's setting exposure.

**Dave Jones:** And then it'll sort of sweep back on itself and it'll start scanning the object. Why did it sort of do it in little bursts? Is it caching the data? Basically, what it's doing is it's trying to sample the entire scene first. Right. And it's trying to essentially get the exposure setting.

**Dave Jones:** Right. How much light, how much brightness is just the camera for. Yep. And then it's doing the scan right now. Got it. So, what it's doing, it'll take about two to three minutes for it to scan across. And so right now what it's doing is essentially taking snapshots off the object

**Dave Jones:** and then analyzing the beam as it goes across. I can see it moving a little step each time. A little step each time. Yep. So, what we've tried to do here is try to build a really high-precision scanner. There's a couple of other scanners on the market, but they're very, their accuracy is really,

**Dave Jones:** for big objects it's okay, but for something like this we want something that's very high accuracy. Got it. And you guys have made this little thing, the scanner itself, or is it just basically some nice packaging? No, basically 100% electronics, coding, industrial design, everything is done by us.

**Dave Jones:** Basically, us phones, Rahul and Richard in the back. Right. Those are the three co-founders. Yep. And we're basically going to kick-start at the end of September. Fantastic. That's our launch date for our... What's your goal? Goal will be about 80,000 or so. Okay, that's doable.

**Dave Jones:** Yeah, yeah. Sure. Just for the nature of our products, we think it's a good goal to have. And next week you're at the World Maker Faire, is that right? Yes, basically September 27th is the World Maker Faire, and we intend to launch at the World Maker Faire.

**Dave Jones:** Fantastic. And probably going to be kick-starting the campaign literally at the event. How many other 3D scanners do you expect there? Probably a few, but... A few dozen, I suspect. But I don't think there'll be one exactly the way our scanner is, and especially at the price point.

**Dave Jones:** Right. Early Bird is basically $199. $199? Early Bird price point for kick-starting. Yeah, that sounds pretty good. So I think you'll be hard-pressed to find something in that price range. Can we see the electronics inside one, or you don't have one? Electronics inside one.

**Dave Jones:** Oh, that's it. There we go. There we go. If we had one more day, this would have been working. Right, okay. So basically, if you have a look at it, that little Bluetooth module there, that's the little unit right on there. Got it.

**Dave Jones:** That's development board, and here's our actual on-circuit. So everything's been done, just got to plug the firmware, and we're good to go. And that's got a little stepper motor driver in it, does it? That's the DRV834, that's the little stepper motor driver, Bluetooth controller, a couple of filter caps and little things here and there.

**Dave Jones:** So that's it? Yeah, that's it. Awesome. Thanks, mate. No worries. Good luck at the Boardmaker Fair. Thank you for that. Thanks, David. All right, I'm here with Matt. You may have heard of, well, you haven't heard of Matt, but you've heard of his company Breadboard Killer.

**Dave Jones:** So tell us all about it. What do you do? Show us. Yeah, well, we are a printed circuit board supplier in Australia. Yeah, we started off batching orders together of printed circuit boards, and that started about a year and a bit ago. And so it's like a side thing for me.

**Dave Jones:** So I started off doing that, and my goal is to bring it back to doing that. But at the moment, we're offering more flexibility, so you can kind of order your boards with, you know, like custom solder masks and stuff like that. Trace spacing if you need to.

**Dave Jones:** 4-4. Yeah, you can get down to 4-4, which is, I haven't had anyone do that yet. Yeah, which is pretty insane. That usually costs a lot more to get down to 4-4. Yeah, it does cost a bit more. I think it's $40 extra.

**Dave Jones:** Right. But yeah. So it's an Australian printed circuit board supplier. Yep. How much are your boards? So if you want a 5x5cm board, it's $25 plus shipping, so that ends up at $36. Yep. Or if you wanted a 10x10cm board, it's only $5 more, so it's up to $46 with the standard shipping.

**Dave Jones:** And how many boards do you get? You get 5 boards. You get 5 boards for that. Yep. When I was a boy, you could get one board for like $800. Oh yeah, yeah, yeah. That seems worth it. Fantastic. So we obviously know where they're made.

**Dave Jones:** They're made in China. They are, yeah. Do you take the files manually and do it, or do you have like a OSH Park type automated process to do it? So for a two-layer design, you can upload your Gerbers directly to the website. You can like just zip your files and drag and drop them, and then you can kind of like select, you know,

**Dave Jones:** which layer goes where if it's not a standard format. Otherwise, it'll, you know, guess which layers or which of your Altium or Eagle standard outputs. So does it show you on the website? Does it show you like a preview of the... Yeah, it does.

**Dave Jones:** If I can get it to show up at some point, or I can show you on my laptop. There you go. So you kind of just like drag and drop your file. Yep. It'll upload. And then you can see renderings of your board.

**Dave Jones:** Very nice. You can see the layers, and you can select which way is which and all that kind of stuff. And then on the next page, you can like select solder mask, and it'll render it in red or whatever, so you can see the colors and stuff like that.

**Dave Jones:** How long did it take you to put together to code all that sort of stuff? Is that easy? Not super easy. It took about 150 hours of coding. Is that a lot? Yeah. I don't know. I feel like that's a lot. Yeah. So, and then, I mean, that was like to do the base stuff, and then I've just like kind of progressively worked on it.

**Dave Jones:** It's kind of like, you know. So, do you penalize batching with others? Is that how you do it on one panel? No, not at the moment. The manufacturer I use actually penalizes them, so that's what gets the cost down. But they aggregate like orders from a lot of other people and penalize them.

**Dave Jones:** Right, so they actually do it for you. So you just send them a bunch of individual files. That's right, yeah. Okay. And so my goal is to move it towards in the future. I want to be more like the Osh Park of Australia.

**Dave Jones:** And like there are a lot of people in Australia who get PCBs manufactured. And, you know, I want a low-cost service that's quick turnaround plus the breadboard killer, you know. If you can replace the breadboard, then go ahead and do it, you know.

**Dave Jones:** I think it'd be awesome. And so the lead time is, did you mention that? So at the moment, if you use standard shipping, it's about three weeks from when you order it to when you receive it. And if you go express shipping, it's a week and a half.

**Dave Jones:** That's pretty good, a week and a half. Yeah. That's not bad at all. Do you have any plans for like a real express service, like a two, three-day turn kind of? Not at the moment. I'd have to see if there's like some demand for it, if people like really want that.

**Dave Jones:** I tend to find like the price really skyrockets when you look at that, like $250 a board. And, I mean, most hobbyist makers, which is who this is mostly aimed at, people like me, who want to, you know, like get their prototype up and working, you know,

**Dave Jones:** don't want to throw $300 to get your design here like a few days or, you know, a few weeks. Or whatever. Yeah. All right. So mostly Australian clients? Yeah. Yep. Pretty much. Very large majority is Australian clients. Yep. Thanks, Matt. Yeah, you're very welcome.

**Dave Jones:** Check them out. Redboardkiller.com.au. Yeah. Oh, I got the Australian one. Yeah, just to be Aussie. All right. Thanks, Matt. You're welcome. And I'm here with Peter from Robots and Dinosaurs. He's going to tell us all about, he's funky. What is it? This is, so this is a video game, Kerbal Space Program.

**Dave Jones:** I have built a hardware control interface to let me control what I'm flying in the game and give me readouts about the status of my ships. Got it. So it's basically a custom hardware interface to an existing, the Kerbal Space Program. That's right.

**Dave Jones:** So otherwise people normally just operate it with a joystick or whatever. With a joystick or keyboard and mouse. Or keyboard. And it's just not as fun, right? It works great, but it's kind of boring. Yeah, yeah. Right. Well, tell us about the hardware.

**Dave Jones:** What's running it? What's it got? So I have two Arduinos on board. One of them manages all of my switches and my dials and has a serial connection back to the game. I have a second Arduino that just manages these displays and the LEDs.

**Dave Jones:** Got it. And all of these light up? They do light up. This is for launching? A lot of it is good for launching. I've got parachutes and heating, so I get to find out if I'm about to explode. Got it. And here's the ACE to AUX button.

**Dave Jones:** We need an ACE to AUX. That's coming in version 2. Right. Excellent. How long did it take you to build it? About a year and a half off and on. Yep. Started planning around January last year. Started buying components around March last year.

**Dave Jones:** I mostly finished it this week. Oh, fancy. Just before, just, yep. Just in time. I was crunching fairly hard, yes. Fantastic. And we can drive a rover on Mars as I did yesterday. Yes. Fantastic. So what else? We've got some, I love the analog VU, the analog meters.

**Dave Jones:** Those currently aren't hooked up. But they will be. Oh. That's also coming very soon. Got it. I'm intending those to show my speed and descending and altitude. They'll be beautiful for landing with. And the, I love the blue LED displays. Those are absolutely gorgeous.

**Dave Jones:** They are gorgeous, aren't they? I bought those from our friends at Little Bird here today. Oh, fantastic. So what do they show? What can you program them to show? They can, I can program them to show all sorts of things. When I'm in orbit, I can show my apoapsis and periapsis,

**Dave Jones:** which are highest and lowest parts of an orbit. I can show how much fuel I have on board. None right now because this is an electric rover. I can show, when I plan for a maneuver, I can show how far away that is and how much power I need to use to get there.

**Dave Jones:** And I can show my altitude. So right now it's telling me that we're at two kilometers above sea level. And that's about it. Sea level on Mars? Where the sea would be. Where would be, right. I guess there's a mean level where they, just like on, yeah.

**Dave Jones:** Yes. Got it. Fantastic. Thanks, Peter. Thank you. Now here with Ian, tell us about your podcast. Hey, I've got a weekly science technology. If you want wacky, weird, unusual, funny science every week. Awesome. Diffusion Science Radio at diffusionradio.com. Diffusionradio.com. There you go, folks.

**Dave Jones:** Show us your stuff. Well, I see he's wandering around with his podcast. Wandering around with my equipment. He's probing through his microphone. That's right. Show us your other stuff. I've got the NeoPixel goggles. Yep. Nice work. Put them on like that. Yep. Awesome.

**Dave Jones:** And you've got a head-mounted camera. And I've got a little head-mounted camera. Is that permanently on? It's not permanently on. Oh, right. I don't have the battery for it. Look, it's a LookSee that I've modified. Yep. And LookSee don't make them anymore. Right.

**Dave Jones:** So it's not fully supported anymore. And it's better if I just record when I want to record. Got it. And then switch it off. Got it. Awesome. Thanks, Ian. Thank you. We've got Nathan from the Uni of New South. And he's going to tell us all about these fantastic little Pac-Man robot things.

**Dave Jones:** Take it away, Nathan. So we're a group called Create at the University of New South Wales. We're a maker club. And this is our latest project. So this is a robotic Pac-Man game. Excellent. And tell us about the tech in it. So these little robots are running Arduinos inside of them.

**Dave Jones:** We've got these stepper motors on the bottom here, which is exactly the same as the ones in your 3D printers. And they're used to drive the robots around with these omnidirectional wheels that allow the robots to sort of move forward, back, left, and right

**Dave Jones:** without having to turn. And we're using these infrared sensors to do some line following, basic line following on an interactive course with some image recognition. Because you've got some leds in here, and they're the dots, right? Yeah, they are. So they're the dots, and the Pac-Mans eat the dots.

**Dave Jones:** Yep. So as Pac-Man moves around the course, we've got a little overhead webcam, and it keeps track of Pac-Man, and it turns off the dots as Pac-Man goes and eats them. Fantastic. And where's the webcam? The webcam's all the way up there, that little tiny little green dot.

**Dave Jones:** And I can even show you a little bit of what it looks like on this program. So we've got Pac-Man moving around, and the webcam is actually tracking where Pac-Man is. And we've got the Blue Ghost obviously on screen as well. Fantastic. How long did it take you to put this together?

**Dave Jones:** Oh, about five weeks. About five weeks? So not very long. Okay, so you did this actually for the fair? We did it actually, it was originally for Vivid, but we've improved it since then and made it ready for the fair. I didn't see this at Vivid.

**Dave Jones:** No, it was actually at UNSW Art and Design Campus to begin with, so it was a bit off-site, but this is such a massive event, we've wanted to show it here for a long time. Does it play a main game of Pac-Man? Oh, it does.

**Dave Jones:** It's a work in progress. So we're setting up a Wi-Fi network to send all the robots information about the location of all other robots, so they can make smart decisions so that Pac-Man can avoid the ghosts and the ghosts can chase after Pac-Man.

**Dave Jones:** It's really exciting. Good work. Thanks Nathan. Thank you very much. I'm here with Aileen from The Missing Link, and she's going to tell us all about this. It's not chain mail, what is it? It is scale mail. What is scale mail? Scale mail is made with a bunch of tiny little scales,

**Dave Jones:** like this or like this, and they're all joined individually with links, kind of like chain mail. Awesome. But instead of joining up the links to themselves, they link into scales. Now this style of armour has been around for ages. This is before chain mail?

**Dave Jones:** Yeah, actually it was a precursor to chain mail. It was about a thousand years beforehand was about when it started. Wow. The Japanese were very fond of it. They used to make it out of paper, leather, metal, anything that they could come to hand.

**Dave Jones:** The scales weren't necessarily this shape, they were other shapes. They used to have them in squares and rectangles, things like that, and they'd join them up with either links or leather, or they'd tie them on. And how long does it take to manufacture that?

**Dave Jones:** This took me 22 hours. 22 hours? Is that more? I expected more than that. I'm pretty fast. Oh, right. The chain around it, the actual custom bandolier to hold it on, that took me six months. Six months? It was the first piece I ever made.

**Dave Jones:** I was just learning at the time, and it gave me a good basis. Fantastic. Thank you very much. No worries. Thank you.
