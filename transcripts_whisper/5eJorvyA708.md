---
video_id: 5eJorvyA708
title: Altium Designer Serious ERC bug
url: https://www.youtube.com/watch?v=5eJorvyA708
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 29, "2": 29, "3": 58, "4": 88, "5": 117, "6": 146, "7": 195, "8": 220, "9": 255, "10": 272, "11": 315, "12": 344, "13": 374}
---

**Dave Jones:** Hi, I wanted to just show you what I think I've found a bug in Altium Designer 17. This is the absolute latest release as of the release date of this video and I was just actually making a video on ERC, Electrical Rules Checking in Schematics, and I was trying to like force an error and it wasn't being detected and this is really rather unusual, okay?

**Dave Jones:** So what I've got here is I've deliberately introduced several errors into this schematic here. One is a data out, an output pin of this chip is connected over to another output here, okay? So two outputs shorted together, it should detect that, you know, as a fail, okay?

**Dave Jones:** And then I've got, well, I've got two floating, I've got a floating input here, so two inputs connected together with no driving source, okay? It should detect that and I've got another one here where the data output pin is connected through to ground, so it's connected to a power net.

**Dave Jones:** Once again, a really bad error which should be picked up by an ERC. So, hey, look, I'll go into my out job here, okay? I've got my out job set for my Nixie Tube display project, here we go, and I'll run that and bingo, look, okay, I've got a couple that are saying there's no driving source, okay?

**Dave Jones:** That's fine, net's hidden, but there is no warning or error flagged for two output pins shorted together or for an output pin shorted to a ground, like a power net, okay? And just to prove that it's all hunky-dory, I'll go into my project options here, my connection matrix, look, here it is, output pin to output pin, shorted together, so there it is, output pin to output pin generates an error.

**Dave Jones:** It should generate an error, you can have a no report, a warning, an error or a fatal error and trust me, I've experimented with this, doesn't matter what you set here, it does not detect it and power nets and everything else by default should actually detect this sort of stuff and you go, okay, don't use an out job, but hey, an out job is supposed to be the final step, critical design step before you manufacture or do anything else.

**Dave Jones:** So there's something wrong, I'm not sure where it's getting and if I just, where it's getting those options from, whether or not it's a bug that's missing it or it's getting some ERC options, matrix options from somewhere else, I don't know. So anyway, if I go to the schematic document over here and I right click and I compile that document, which is the same thing as doing that ERC and I'm specifically, I want to compile this one sheet like this, so I compile that Nixie sheet like that and sorry, it didn't pop up, there's a window here, there's a display window, a messages window, I'll actually clear that and I'll run that again, okay, compile, boom, there you go, it's done.

**Dave Jones:** And it, look, compile successful, no errors found, it did not even warn that those two outputs are connected together. Now the only way to make this work and I spoke to Altium and they said, yeah, do this and it'll work and sure enough, it does, I haven't used Altium 17 before, my previous version was Altium 10, so yeah, I'm a newbie to Altium 17 here.

**Dave Jones:** So let's go over to here, if I go compile PCB. Project, now the project, which contains a blank PCB, it doesn't matter, but if I do compile the PCB project, bingo, it finds it, okay, exactly what you want, here we go, no dry, ground, there it is, ground contains output pin, blah, blah, blah, blah, blah, okay, so it's found it, I don't like the fact that it really doesn't highlight, you know, you've got to like search through, where is it, where is it, well, there it is in there.

**Dave Jones:** Yeah, so it doesn't, anyway, and of course, it, and it's generated other warnings here, like component has unused subparts, which we didn't see before and things like that, so clearly it's getting rules from somewhere else and here's the multiple output pin error, for example.

**Dave Jones:** So it has now detected it, it's detected it just fine, multiple output pins, exactly as you would expect it to when you do an ERC, but if you go like this. And compile that, where, look, it's not there, it's not there, that to me has got to be a bug, there's no way that you can miss critical errors on a schematic, I want to check that one schematic, I'm asking it to do that, and once again, the out job will do exactly the same thing, it'll miss those errors, so what the, like here's the, like if I put that to a PDF report, I could,

**Dave Jones:** feed that to a PDF report, give that to management and say, hey, look, it's passed ERC, no worries whatsoever, let me go onto the PCB layout, and they'll go, yeah, no worries, and my schematic contains, like, really gross errors that are going to release the magic smoke from these chips, I mean, it's just, nah, there's something seriously wrong here, so I want to know where it's getting the rules from to do that compile document there,

**Dave Jones:** because it's certainly not coming from the project option, and fair enough, the, when I do the project compile, the project options uses the connection matrix, but where else is it getting the rules from to do the compile, so if it might be some legacy thing, because Altium's full of legacy stuff and things like that, but please comment below if you think this is, like, a genuine bug, or you know some way around it, or I'm doing something dumb, I'm still talking about it,

**Dave Jones:** I'm still talking with Altium on this, so I'm sort of, like, prematurely releasing this, but I just wanted to document that issue, so there you go, I think that is a major issue, if I compile a document, or do an out job, especially an out job ERC, like, you know, there it is, electrical rules check, thank you very much, I expect it to catch all those errors and it doesn't, anyway, enough rambling, catch you next time.
