#!/usr/bin/perl

#
# Simple Playlist Post creator
# 2014-01-24 - Leon Wright - techman83@gmail.com
#
# A developer account is needed with the relevent scopes associated - https://cloud.google.com/console/
#

use strict;
use Config::YAML;
use JSON;
use LWP::UserAgent;
use LWP::Authen::OAuth2;
use FindBin qw($Bin);
use DateTime::Format::ISO8601;
use Data::Dumper;

# PLUG Channel details
#'channelId' => 'UCeE_8OWFvGMYydlIOYU_G0g',
#'playlistId' => 'UUeE_8OWFvGMYydlIOYU_G0g',
#'channelTitle' => 'Perth Linux Users Group (PLUG)',

my $self;
$self->{playlistId} = "UUeE_8OWFvGMYydlIOYU_G0g";
$self->{post_path} = "$Bin/../plug/_posts";

### Get oauth2 authorisation
my $googleapi = Config::YAML->new( config => "$ENV{HOME}/.googleapi.yml" );
my $oauth2;

if (! $googleapi->{token_string}) {
  $oauth2 = LWP::Authen::OAuth2->new(
                client_id => $googleapi->{client_id},
                client_secret => $googleapi->{client_secret},
                service_provider => "Google",
                redirect_uri => "urn:ietf:wg:oauth:2.0:oob",
                scope => 'https://www.googleapis.com/auth/youtube.upload',
            );
  my $url = $oauth2->authorization_url();
  print "Log into the youtube account and, set your channel and browse the following url\n";
  print "$url\n";
  my $code = &Prompt("Paste code result here");
  $oauth2->request_tokens(code => $code);
  $googleapi->{token_string} = $oauth2->token_string;
  $googleapi->write;
} else {
  $oauth2 = LWP::Authen::OAuth2->new(
                client_id => $googleapi->{client_id},
                client_secret => $googleapi->{client_secret},
                service_provider => "Google",
                redirect_uri => "urn:ietf:wg:oauth:2.0:oob",
  
                # This is for when you have tokens from last time.
                token_string => $googleapi->{token_string},
            );
}

## Get initial result list
my $response = $oauth2->get(
       "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=$self->{playlistId}",
       client_id => $googleapi->{client_id},
       client_secret => $googleapi->{client_secret},
       Authorization => "Bearer $googleapi->{auth_token}",
       Host => 'www.googleapis.com',
       );

my $content = from_json($response->decoded_content);

my @items = @{$content->{items}};

## PLUG only has 38 videos, at some stage there will be more and this will handle it.
while ($content->{nextPageToken}) {
  $response = $oauth2->get(
       "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId=$self->{playlistId}&pageToken=$content->{nextPageToken}",
       client_id => $googleapi->{client_id},
       client_secret => $googleapi->{client_secret},
       Authorization => "Bearer $googleapi->{auth_token}",
       Host => 'www.googleapis.com',
       );

  $content = from_json($response->decoded_content);
  @items = (@items, @{$content->{items}});
}

foreach my $item (@items) {
  my $publishedAt = DateTime::Format::ISO8601->parse_datetime($item->{snippet}{publishedAt});
  my $date = $publishedAt->ymd;
  my $filename = "$self->{post_path}/$date-$item->{snippet}{resourceId}{videoId}.md";
  
  # Colons are not compatible with yaml
  $item->{snippet}{title} =~ s/:/&#58;/g;
  if (! -e "$filename" ) {
    print "$filename\n";
    open my $fh, ">", $filename or die $!;
    binmode($fh, ":utf8");
    print $fh <<EOF;
---
title: $item->{snippet}{title}
tags: av plug
---

{% youtube $item->{snippet}{resourceId}{videoId} %}

<!--more-->
$item->{snippet}{description}
EOF
    close $fh;
  }
}

sub Prompt { # inspired from here: http://alvinalexander.com/perl/edu/articles/pl010005
  my ($question,$default) = @_;
  if ($default) {
    print $question, "[", $default, "]: ";
  } else {
    print $question, ": ";
  }

  $| = 1;               # flush
  $_ = <STDIN>;         # get input

  chomp;
  if ("$default") {
    return $_ ? $_ : $default;    # return $_ if it has a value
  } else {
    return $_;
  }
}

__END__
$VAR37 = {
           'etag' => '"qQvmwbutd8GSt4eS4lhnzoWBZs0/IQQr8E_V0YuVBs7ApsynWMKZ0Ig"',
           'snippet' => {
                          'channelId' => 'UCeE_8OWFvGMYydlIOYU_G0g',
                          'playlistId' => 'UUeE_8OWFvGMYydlIOYU_G0g',
                          'channelTitle' => 'Perth Linux Users Group (PLUG)',
                          'position' => 36,
                          'description' => '',
                          'publishedAt' => '2012-09-06T14:11:16.000Z',
                          'resourceId' => {
                                            'kind' => 'youtube#video',
                                            'videoId' => '35D0_feZnK8'
                                          },
                          'title' => 'PLUG: UEFI and Secure Boot - Jeremy Kerr',
                          'thumbnails' => {
                                            'high' => {
                                                        'url' => 'https://i1.ytimg.com/vi/35D0_feZnK8/hqdefault.jpg'
                                                      },
                                            'standard' => {
                                                            'url' => 'https://i1.ytimg.com/vi/35D0_feZnK8/sddefault.jpg'
                                                          },
                                            'medium' => {
                                                          'url' => 'https://i1.ytimg.com/vi/35D0_feZnK8/mqdefault.jpg'
                                                        },
                                            'default' => {
                                                           'url' => 'https://i1.ytimg.com/vi/35D0_feZnK8/default.jpg'
                                                         }
                                          }
                        },
           'kind' => 'youtube#playlistItem',
           'id' => 'UU_OJOX2bDbM9SHmIgwyIu1oqsHihQqIDq'
         };

