#!/usr/bin/env ruby
Lists = ARGV[0].scan(/(?<=from:)(.\d+)|(?<=to:)(.\d+)|(?<=flags:)([0-9|:|-]+)/).split()
puts List.join(',')
