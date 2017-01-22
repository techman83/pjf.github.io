title: Hacking your Conference badge for Hugs & Profit
date: 2017-01-22
tags: programming, arduino, linuxconfau, lca2017
category: hardware
slug: hacking_hugs_profit

Last week was [Linux Conf AU 2017](http://lca2017.org), which is a community run Free and Open Source Software conference that is in a different A/NZ city every year. This year I'd managed to attend the [Open Hardware MiniConf](http://www.openhardwareconf.org/) and was inspired to build something during the conference. I'm not sure how it occurred to me to build a 'Hug Detector' into my Conference badge, but it did and after talking about it with some fellow delegates, the feedback was overwhelmingly positive.

So after heading to my room early to get some sleep, I got sidetracked. Armed with an [ESP8266](https://espressif.com/en/products/hardware/esp8266ex/overview) based [D1 Mini](https://www.wemos.cc/product/d1-mini.html), some sensors, a breadboard, and some wires I stayed up until 1am. Then a wild [GitHub repository](https://github.com/techman83/been_hugged) occurred.

@Techman_83/status/821716638235906050

I popped by the rego desk the next morning, to acquire an extra badge holder. Which was met with some initial quizzical expressions, followed by intrigue whilst handing it over. Sitting up the back of the sessions and stabbing myself several times, I managed to get something of a working concept. 

@johndalton/status/821918573215895552

That evening I set about tidying up the wires and got it working well enough with the sensors I had on hand. However I really wanted to get the [Freepixels](http://www.freetronics.com.au/products/freepixel-addressable-rgb-led-module) I'd attached to display feedback about 'Hug Quality' and was hitting a strange problem with the micro controllers memory disappearing when ever I utilised them. As it turns out there was a dev from [Expressif Systems](https://espressif.com/) who was intrigued by my badge and when I mentioned my problem it was met with "Want me to take a look at the code". 

@Techman_83/status/822267900585123840

As it turns out the bug was in how I was iterating over the LED modules:

    ::::c++
    for(i = 0; i <= NUM_LEDS; i++) {
    	leds[i] = CRGB::Red;
    	leds[i].maximizeBrightness();
    	FastLED.show();
    }

'NUM_LEDS' is configured as '2', but arrays start at '0' in a lot of languages (including c++) so I was iterating past the end of 'leds' array and corrupting the micro controllers memory. I'd missed that entirely and as I generally work in higher level scripting languages, this kind of thing normally blows up the runtime in quite an obvious way. Below is the single character change that fixed the problem.

    ::::c++
    for(i = 0; i < NUM_LEDS; i++) {
    	leds[i] = CRGB::Red;
    	leds[i].maximizeBrightness();
    	FastLED.show();
    }

Overall I really enjoyed working on the project. It was a fun way to make new friends and make a positive contribution to what was an exceptional LCA. Here are some extra tweets that shared the joy <3

@r1chardj0n3s/status/821975880498974720

@vmbrasseur/status/822198988577198080

@The_McJones/status/822198909896257536

@johndalton/status/822219959610707969

@Charcol0x89/status/822294441813622784

@ITProAssoc/status/822298107274821632

@evildeece/status/822301398767259649
