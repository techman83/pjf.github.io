---
tags: programming perl lca2014
title: Automating AV&#58; EventStreamr
---

[EventStreamR](https://github.com/lukejohnosmahi/eventstreamr/) come to inception from a collection of experiences amongst our local LUG the [Perth Linux User Group](https://www.plug.org.au). Although we call ourselves PLUG, we have members from all over the state. Western Australia being quite large, 2,529,875 square km or over 10 times bigger than Victoria; so some of our members find it quite difficult to attend. A few years ago an initiave started by [James Bromberger](http://blog.james.rcpt.to/) was to film and live stream all PLUG talks so that every member had an oppurtunity to attend our meetings, even if they couldn't necessarily make it in person.
<!--more-->

Between our experience streaming and attending LCA2013 to get a feel for how the conference ran, we had come to the conclusion that the Open Source Video mixing stack we use (DVswitch), whilst being easy to use and quite fit for purpose; it can be a little unreliable. Along with that DV aka Digital Video as a dying standard. To my knowledge there isn't a lot of work being put into the project as the world is moving on from DV. In light of all that we had come up with a list of requirements to bring reliability to the table.

- Open Source
- Be able to scale up and down
- Easy to setup and use
- Work on any hardware
- Central Configuration Management + Control
- Able to operate independently (Locations with no network or failure of networking)
  
Ability to scale down was particularly important to us, as we want to be able to use this solution at our local LUG and also encourage other LUGs to generate content. Which was something that I felt was lacking in some of the established solutions (eg. Matterhorn, though I'm happy to be shown otherwise). So after gathering our requirements, there was also figuring out what problems we needed to solve.

- DVswitch - It sometimes goes bang
- DVgrab - does not fail gracefully
- Setup for mutliple stations and rooms is time consuming

There are 2 major components to EventStreamR, I'll cover the engine that sits in the background doing all the hardwork. I had pondered for some time about how I was going to solve the above problems and also meet our requirements. I felt Perl would be up to the challenge (and also happens to be the language I have the most exeprience in). It's a language I frequently use to glue things together in my day job and there are many libraries availble, which means less time re-inventing the wheel.

With [Luke](https://github.com/lukejohnosmahi) writing the framework for the frontend, it left me focus on the backend. Which at it's core is a single daemon.
