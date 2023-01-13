#!/usr/bin/env ruby
x = ARGV[0].scan(/(?<=from:)(.\d+)|(?<=to:)(.\d+)|(?<=flags:)([0-9|:|-]+)/).split()
puts x.join(',')
