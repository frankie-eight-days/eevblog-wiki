---
video_id: RUNqDK2Ryrg
title: EEVblog #40 - Dilbert and the world of micro managed Engineering
url: https://www.youtube.com/watch?v=RUNqDK2Ryrg
source: youtube-asr
timestamps: {"0": 10, "1": 21, "2": 42, "3": 63, "4": 74, "5": 89, "6": 103, "7": 116, "8": 128, "9": 141, "10": 162, "11": 172, "12": 184, "13": 195, "14": 203, "15": 217, "16": 234, "17": 249, "18": 260, "19": 275, "20": 284, "21": 301, "22": 314, "23": 325, "24": 337, "25": 350, "26": 363, "27": 371, "28": 391, "29": 410, "30": 432, "31": 442, "32": 460, "33": 474, "34": 487, "35": 503, "36": 511, "37": 537, "38": 554, "39": 565, "40": 580, "41": 591}
---

**Dave Jones:** I'm going to let you in on a little secret. Everyone's favorite electrical engineer from MIT, Dilbert, he's right on the money when it comes to how engineering companies operate in the real world.

**Dave Jones:** So, here we go. Now, if you aren't busy being micromanaged or trying to avoid the HR people or massaging some data, trying to figure out how to pass the buck, or trying to figure out how to look busy, or trying to meet some ridiculous deadline you couldn't even meet if you had a DeLorean, or whether or not you're trying to do something for the fifth time cuz management didn't

**Dave Jones:** listen to you in the first place, or whether or not you're trying to design some early warning boss detection system for your cubicle, or whether you're just idling time listening to a stupid blog like this, then odds are you're working on a project that everyone knows is doomed to fire or it's just going to get shit-canned in the next company restructure.

**Dave Jones:** So, I present to you my top five list of dead projects. Projects I've worked on that have never seen the light of day for whatever reason, but ultimately, because mismanagement reigned supreme at every engineering company.

**Dave Jones:** It's just the way it is. Number five on my list, my automated functional tester. Yes, you've seen this before in a previous blog. This was designed to actually replace a 19-in rack-mount system which sat on a big mobile trolley.

**Dave Jones:** It was mains-powered, it had 19-in rack instruments, an Agilent and Fluke LCR meter, an IR meter, and it had an industrial PC in there running Windows 3.11 and some Visual Basic software.

**Dave Jones:** So, the project goal, it was pretty good idea. It was pretty solid. The old system cost about $30,000. This was going to cost about five. The old system you had to wheel around on a trolley.

**Dave Jones:** It was big and heavy and cumbersome, but this thing you could fit in a suitcase and carry it around with you. And the old one had really troublesome test leads, which you had to plug in, whereas this one just plugged straight into the product under test.

**Dave Jones:** It was a winner. So, how could it go wrong? It technically wasn't that hard. I had the prototype up and running and demoed within a month or something like that, and it was on track and looking good.

**Dave Jones:** The first problem was the changing customer requirements. The goal post just kept moving. Woohoo! All over the place. One week they wanted it powered from an embedded industrial PC, the next they wanted it to hook up to a notebook, then they wanted high voltage testing, and then they didn't, and then they wanted this and that functionality, and then they didn't want test leads, and then they wanted test leads.

**Dave Jones:** It was crazy. It kept changing. Then they wanted me to investigate the feasibility of actually ditching the hardware I just developed for some off-the-shelf solution they had just found and made it with my software.

**Dave Jones:** And so, I had to spend a month on that, just investigating the damn thing. It turns out, no, it wasn't suitable. Back to the hardware. Then, of course, I got tasked onto other projects as well that sucked up all my time.

**Dave Jones:** So, what did they do? They sent me on some time and resource management course. So, after 6 months of mucking around, management finally got focused and they wanted a final demo.

**Dave Jones:** So, we did a final demo for the customers and everyone thought it was really cool. It was really great, but they didn't know if they really wanted it, cuz they didn't still didn't know what their needs were.

**Dave Jones:** Unbelievable. So, what happened in the end? Well, the project just dissipated. One of my favorite words. Projects just vanish. They just dissipate into the ether. And the customer realized, well, the old solution wasn't that bad.

**Dave Jones:** Windows 3.11, we'll just order another 10 of those, thanks. Number four on my list is some production acoustic test software. I was tasked to write some new software for for existing production hardware test jig we had for measuring the acoustic performance of hydrophones.

**Dave Jones:** And the old system ran on Windows 3.11 and you know, 16-bit. Now, due to some internal company politics, I was forced to write it in LabWindows/CVI, which is LabView's version of C for Windows, basically.

**Dave Jones:** And I hadn't used it before, but instead of just jumping into it and working on the project, no, they sent me on some silly course first, thinking that I'd be more productive.

**Dave Jones:** Now, the software wasn't actually that complex. I had a demo, a suitable demo up and running in a couple of weeks. But that's when the micromanagement took over. So, every nitpicky thing I did and every nitpicky decision I made had to be overanalyzed and justified.

**Dave Jones:** I had to spend all most of my time just doing documentation on what I had just done or what I was going to do next month instead of cutting code.

**Dave Jones:** It was just ridiculous. Number three on my list the next generation seismic streamer. Now, as always, it wasn't a bad idea. The company decided to invest some money into development of a complete system product so we'd become a big player in the oil survey market.

**Dave Jones:** Now, this project was huge. It cost close to $10 million and spanned about 2 and 1/2 or 3 years, I think it was, and they ran it in the classic MBA textbook style, step-by-step.

**Dave Jones:** They weren't going to miss a damn thing. They were going to manage this one to perfection. So, of course, this project had all the highlights for me a classic over-managed project.

**Dave Jones:** Number one, recruit the best and brightest people you can get and then ignore their advice. Have 10 meetings a week that achieve absolutely nothing except resolving unsolved issues from the previous meeting.

**Dave Jones:** Hey, hop on the meeting merry-go-round. Woohoo! Always run the project in the state of crisis. And if something's not a crisis, well, just leave it alone until it becomes one.

**Dave Jones:** Make sure all tasks have equal priority, no matter how trivial they are. Invent standard ways to do things, even if they're fundamentally wrong. At least you can't be accused of not following the standard.

**Dave Jones:** Okay, the product, it did actually make it to trial a couple of years later, but it just died in the ass because, well, it was too late and the whole landscape had changed.

**Dave Jones:** Oh, well. What's 10 million bucks? Number two on my list, the seismic telemetry system. As the previous project was slowly sliding down the hill towards oblivion, they decided to spend up big again and design our own state-of-the-art electronics telemetry system.

**Dave Jones:** Now, previously, we actually had a third-party company design and supply the telemetry electronics for the product. Well, the company didn't want to pay the royalties anymore, so they hired a bunch of smart guys and they formed a team and a Chinese wall, of course, so that we couldn't infringe any intellectual property and we designed our own.

**Dave Jones:** It was a very cool state-of-the-art system. It was like up to 10,000 channels of 24-bit analog-to-digital conversion all in real-time synchronous sampling across like 10 km of cable and it was uh E1 protocol over an ATM fiber optic network and it had a 500-V DC power distributed transmission system.

**Dave Jones:** Because we weren't being micro-managed and the hardware team were left to their own devices, we had a demo running within like a month or 2 months. It was super quick and it was state-of-the-art.

**Dave Jones:** Everyone loved it, industry-leading performance and it was all fantastic and looking good. So, what happened? Well, it all just dissipated again because the company figured uh it was probably going to be a big no-show and, well, it doesn't help when your company's bought out by a bigger company that has competing technology.

**Dave Jones:** So, they just let it go for a while, but then they weren't really serious. It was going to be shitcanned from day one. Oh, well, it's not a bad way to spend a year or so in a high-tech development project.

**Dave Jones:** Could be worse. And number one on my list is a 3D underwater sonar system. This one was a biggie. It was a government contract upwards of $12 million I think it was, and it was to develop a world-first 3D underwater sonar system.

**Dave Jones:** And well, it was a pretty good idea at the time. All the individual aspects of the product and of the concept you could actually had been demonstrated in ideal conditions in their own little elements.

**Dave Jones:** So, all we had to do is put it together, right? How hard can that be? It's just a system. That's what you have systems engineers for and systems managers, right?

**Dave Jones:** So, what do you do? Well, you take a ragtag bunch of developers who are constantly revolving through different parts of the organization, and you put them together, form a team, and to develop this high-end FPGA hardware and system solution, and well, you get them to write some VHDL which they're not very good at, and then well, you try and make the whole thing work.

**Dave Jones:** And then you add in some management or mismanagement, and bingo, you've got a classic project. I won't bore you with the details, but one person nailed it on the head when they said this project was a triumph of workmanship over engineering.

**Dave Jones:** The result? Well, it didn't quite work as expected at each milestone. So, the government just keep lowering the bar of the requirements so that they couldn't be accused of funding yet another failed project.

**Dave Jones:** And of course, it all worked out well. Everyone got a big pat on the back, and the government said, "Oh, that was interesting and fantastic and money well spent, but I don't think we'll fund the production of this thing.

**Dave Jones:** Ah, well. What's 12 million bucks or more? So, next time you find yourself working on a dead end project, don't worry about it. It's normal. It happens to everyone.

**Dave Jones:** So, have a laugh, have some fun, read Dilbert, watch Office Space again, and just take home your paycheck and be happy.
