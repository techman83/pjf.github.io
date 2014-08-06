#!/usr/bin/perl -w
use 5.010;
use strict;
use warnings;
use autodie qw(:all);
use File::Path qw(remove_tree);
use FindBin qw($Bin);

chdir("$Bin/..");

# Hack to avoid blatting things I've forgotten to commit..
my $clean = `git status -s`;

if ($clean) {
  say "You have untracked/uncommited files";
  say "Please commit or remove them";
  exit 0;
}

system("jekyll build");
system("git checkout master");

# I work from many systems, trying to 
# push a commit when the branch isn't up
# to date is a pain in the bum.
system("git pull origin master");

# Make a hash of all our (non-dot) files
my %files;
@files{ glob("*") } = ();

# Remove _site from that list
delete $files{_site};

# But get rid of all the rest.
remove_tree(keys %files);

# Move everything in site up a level
system("mv _site/* .");

# Add domain info
open(my $fh, '>', 'CNAME');
say {$fh} "www.techman83.me";
close($fh);

# Tell github it shouldn't run jekyll a second time.
open(my $nojekyll, '>', '.nojekyll');
close($nojekyll);

# Take a timestamp, and send everything to github.

my $time = localtime();

system("git add -A");
system(qq{git commit -m"Site update at $time"});
system("git push");

# Finally, return home
system("git checkout build");
