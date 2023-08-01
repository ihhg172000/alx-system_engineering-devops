#!/usr/bin/env ruby
$sender = ARGV[0].scan(/\[from:[^ ]+\]/).join.scan(/:.+\]/).join.scan(/[^:\]]/).join
$receiver = ARGV[0].scan(/\[to:[^ ]+\]/).join.scan(/:.+\]/).join.scan(/[^:\]]/).join
$flags = ARGV[0].scan(/\[flags:[^ ]+\]/).join.scan(/:.+\]/).join.scan(/-?\d/).join(":")

puts "#$sender,#$receiver,#$flags"
